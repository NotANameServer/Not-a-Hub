#!/usr/bin/env python3

"""
Utility to rewrite all index.md files with the list of markdown articles
discovered on disk. If an index.md file exist already, this utility
conserve all lines prior to an "## Index" title (or the whole file if
that title is missing).
"""

import dataclasses
import itertools
import subprocess as sp
from collections import defaultdict
from contextlib import suppress
from datetime import datetime
from functools import partial
from operator import attrgetter
from os import getenv, linesep, sep
from shutil import which
from pathlib import Path
from typing import List


ROOT = Path(__file__).resolve().parent
GIT_PATH = getenv('GIT_PATH', which('git'))
SKIP_FILES = {'index.md', 'README.md', 'CONTRIBUTING.md'}


def Tree():
    return defaultdict(Tree)


@dataclasses.dataclass
class Article:
    title: str
    write_date: datetime
    create_date: datetime
    authors: List[str] = dataclasses.field(default_factory=list)
    paths: List[Path] = dataclasses.field(default_factory=list)

    @property
    def name(self):
        return self.paths[0].name

    @property
    def paths_parts(self):
        # [/srv/git/Not-a-hub/langages/cpp/foo.md]
        # => [["langages", "cpp"]]
        return [path.parts[len(ROOT.parts):-1] for path in self.paths]

    @property
    def uris(self):
        # [/srv/git/Not-a-hub/langages/cpp/foo.md]
        # => ["/langages/cpp/foo.md"]]
        return [str(path)[len(str(ROOT)):].replace(sep, '/') for path in self.paths]

    @property
    def tags(self):
        # [/srv/git/Not-a-hub/langages/cpp/foo.md]
        # => {('langages', '/langages'), ('cpp', '/langages/cpp')}

        def addsep(uri, part):
            return f'{uri}/{part}'

        to_uri = partial(itertools.accumulate, func=addsep)

        return list(sorted({
            (part, f'/{uri}')
            for parts in self.paths_parts
            for part, uri in zip(parts, to_uri(parts))
        }))

    def uri_for_root(self, root):
        """
        From all the paths of the current file, return one that starts
        with ``root``.
        """
        return next(uri for uri in self.uris if uri.startswith(root))


def extract_title(path):
    """ Extract the first top level title of a markdown document """
    assert path.suffix == '.md'

    with open(path, encoding='utf-8') as fd:
        # lookahead the next line of every line during iteration
        it1, it2 = itertools.tee(fd)
        with suppress(StopIteration):
            next(it2)
        for current_line, next_line in itertools.zip_longest(it1, it2):
            # ATX title style
            if current_line.startswith('# '):
                return current_line.strip(f'# {linesep}')
            # Setext title style
            if next_line and all(char == '=' for char in next_line.rstrip()):
                return current_line.strip()

    return None


def extract_git_metadata(path):
    """
    Extract the file last write date, the file creation date and the
    authors of a file using it's git metadata
    """

    # Get newest commit date as timestamp
    cmd = [GIT_PATH, 'log', '--follow', '-1', r'--pretty=format:%at', str(path)]
    proc = sp.run(cmd, capture_output=True, check=True)
    write_date = datetime.fromtimestamp(int(proc.stdout.strip()))

    # Get oldest commit date as timestamp
    # command does not work
    #cmd = [GIT_PATH, 'log', '--follow', '--reversed', '-1', r'--pretty=format:%at', str(path)]
    #proc = sp.run(cmd, capture_output=True, check=True)
    #create_date = datetime.fromtimestamp(int(proc.stdout.strip()))
    create_date = write_date

    # Get the authors from all the "add" and "edit" type commits
    cmd = [GIT_PATH, 'log', '--follow', '--grep', r'^\(add\|edit\):', '--pretty=full', str(path)]
    proc = sp.run(cmd, capture_output=True, check=True)
    authors = {  # extract "John" from "Author: John <john@example.com>"
        line.partition(b': ')[2].partition(b' <')[0].strip()
        for line in proc.stdout.splitlines()
        if line.lower().startswith(b'author: ')
           or line.lower().startswith(b'    co-authored-by: ')
    }

    return write_date, create_date, authors


def discover_articles(root):
    """ Discover all articles under ``root``. """

    articles = {}
    for path in root.glob('**/*.md'):
        if path.name in SKIP_FILES:
            continue

        if path.name not in articles:
            title = extract_title(path) or path.name
            write_date, create_date, authors = extract_git_metadata(path)
            articles[path.name] = Article(title, write_date, create_date, authors)
        articles[path.name].paths.append(path)

    return list(articles.values())


def create_index(articles):
    """
    Populate an index, a filesystem-like structure where directories are
    dictionnaries and where file are articles, with all the articles.
    """

    index = Tree()
    for article in articles:
        for parts in article.paths_parts:
            # /srv/git/Not-a-Hub/langages/cpp/foo.md
            # index["langages"]["cpp"]["foo.md"] = article
            subindex = index
            for part in parts:
                subindex = subindex[part]
            subindex[article.name] = article

    return index


def walk(dir_, index, *, rewrite=False):
    """ Recursively get all articles published under this index """
    articles = []

    for name, article_or_index in index.items():
        if isinstance(article_or_index, Article):
            article = article_or_index
            articles.append(article)
        else:
            subindex = article_or_index
            articles.extend(walk(f'{dir_}{name}/', subindex, rewrite=rewrite))

    if rewrite:
        rewrite_index_file(dir_, articles)

    return articles


def rewrite_index_file(dir_, articles):
    """
    Rewrite the index file, conserve what's before the "## Index" title
    or the whole file it this title is missing then write the index
    using the following format:

    ## Index

    ### 2021

    * [Article feb](/tag1/tag2/article-4.md) <kbd>[tag1](/tag1)</kbd> <kbd>[tag2](/tag1/tag2)</kbd>
    * [Article jan](/tag1/tag2/article-3.md) <kbd>[tag1](/tag1)</kbd> <kbd>[tag2](/tag1/tag2)</kbd>

    ### 2020

    * [Article dec-2](/tag1/article-2.md) <kbd>[tag1](/tag1)</kbd>
    * [Article dec-1](/tag1/article-1.md) <kbd>[tag1](/tag1)</kbd>
    """

    index_path = ROOT.joinpath(f'{dir_}index.md'.lstrip('/'))

    # Sort and group the articles by date
    articles.sort(key=attrgetter('create_date'), reverse=True)
    articles_per_year = itertools.groupby(articles, attrgetter('create_date.year'))

    # Conserve what exist before the generated index
    # mode 'a', seek(0) to create the file if it does not exist
    with open(index_path, 'a+b') as index_file:
        index_file.seek(0)
        index_pos = 0
        while True:
            line = index_file.readline()
            if line in (b'', b'## Index' + linesep.encode()):
                break
            index_pos += len(line)
        index_file.seek(index_pos)
        index_file.truncate()

    # Write the index
    with open(index_path, 'a', encoding='utf-8') as index_file:
        index_file.write("## Index\n")
        for year, articles in articles_per_year:
            index_file.write(f"\n### {year}\n\n")
            index_file.write(''.join(
                "* [{title}]({uri}) {tags}\n".format(
                    title=article.title,
                    uri=article.uri_for_root(f'/{dir_}'.rstrip('/')),
                    tags=' '.join(
                        f"[<kbd>{tag}</kbd>]({uri})"
                        for tag, uri in article.tags
                    )
                )
                for article in articles
            ))


def main():
    """ Rewrite all index files """
    articles = discover_articles(ROOT)
    index = create_index(articles)
    walk('', index, rewrite=True)


if __name__ == '__main__':
    main()
