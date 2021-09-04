import { spawnSync } from 'node:child_process';
import { statSync, readdirSync, readFileSync, writeFileSync } from 'node:fs';
import { join, relative } from 'node:path';
import { fileURLToPath } from 'node:url';

// the full path of the parent directory of this file
const dirPath = fileURLToPath(new URL('.', import.meta.url));

function exec(cmd, args, enc) {
  try {
    return spawnSync(cmd, args).stdout.toString(enc);
  } catch {}
}

/**
 * Get the creation date of a path from git, and fallback to the creation date
 * from the filesystem (probably because the file is not yet committed).
 */
function getCreationDate(file) {
  const creationDate = exec('git', ['log', '-1', '--diff-filter=A', '--format=%aI', file], 'ascii').split('\n')[0];
  return creationDate ? new Date(creationDate) : statSync(file).birthtime;
}

/**
 * Return the relative path of the given path from the given base.
 * Backslashs are converted to slashs (for Windows users).
 */
function relativePath(base, path) {
  return `./${relative(base, path).replaceAll('\\', '/')}`;
}

const months = ['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre', 'Décembre'];

/**
 * Transform multiple posts into stringified posts, grouped and sorted by their creation date.
 * ```md
 * ### Juillet 2021
 * * [Ceci est un post](/langages/python/ceci-est-un-post) [<kbd>langages</kbd>](./langages) [<kbd>python</kbd>](./langages/python)
 *
 * ### Juin 2021
 * * [Ceci est un post](/langages/python/ceci-est-un-post) [<kbd>langages</kbd>](./langages) [<kbd>python</kbd>](./langages/python)
 * ```
 */
function makeIndex(base, posts) {
  // groups posts by the month and year
  const groups = {};
  // iterate over posts sorted by creation date
  for (const post of posts.sort((a, b) => b.createdAt - a.createdAt)) {
    // Date -> "Juillet 2021"
    const dating = `${months[post.createdAt.getMonth()]} ${post.createdAt.getFullYear()}`;
    // if the group doesn't exist yet, add it
    if (!(dating in groups)) groups[dating] = [];
    // the post relative path, extension excluded
    const postPath = relativePath(base, post.path.slice(0, -3));
    const tags = post.tags.map((tag, i, tags) => {
      // tags are just the names directories, joining them reveals the true path.
      const path = join(dirPath, tags.slice(0, i + 1).join('/'));
      return `[<kbd>${tag}</kbd>](${relativePath(base, path)})`;
    }).join(' ');
    groups[dating].push(`* [${post.title}](${postPath}) ${tags}`.trimEnd());
  }
  // merge groups' title and posts
  return Object.entries(groups).map(([date, posts]) => `### ${date}\n${posts.join('\n')}`).join('\n\n');
}

// Match the posts section of a index.
// The `d` flag allows to have the match indices (start and end).
// This will deliberately not match the extra line breaks (at the end of the section).
const postsSectionRegex = /## Articles\n(?:### .+\n(?:\* \[.+\]\(.+\)\n)*(?:\* \[.+\]\(.+\))\n\n)*(?:### .+\n(?:\* \[.+\]\(.+\)\n)*(?:\* \[.+\]\(.+\)))|## Articles/di;

/**
 * Write a index in the given directory.
 * If the index file and posts section already exists,
 * the posts section will be updated.
 * If the index file already exists but non the posts section,
 * the posts section will be appended.
 * If the index file does not exists, it will be created,
 * with only the posts section.
 */
function writeIndex(dirPath, posts) {
  const path = join(dirPath, 'README.md');
  const postsSection = `## Articles\n${makeIndex(dirPath, posts)}`;
  let content;

  try {
    content = readFileSync(path, 'utf8');
  } catch (error) {
    if (error.code === 'ENOENT') content = '';
    throw error;
  }

  // if the file is empty (or doesn't exist),
  // create/write to it with only the posts section.
  if (content === '') {
    writeFileSync(path, `${postsSection}\n`);
    return;
  }

  const match = content.match(postsSectionRegex);
  if (!match) {
    // If the file already ends with a line break,
    // there is no need to add a new one.
    // Else we add prefix the index with a line break.
    const prefix = content.endsWith('\n') ? '' : '\n';
    content += `${prefix}\n${postsSection}\n`;
  } else {
    // replace the posts section with the new one
    const [start, end] = match.indices[0];
    content = `${content.slice(0, start)}${postsSection}${content.slice(end)}`;
  }

  writeFileSync(path, content);
}

const ignoredPaths = [join(dirPath, 'assets')];
const ignoredNames = ['README.md'];
/**
 * Recursively scan the given directory and return an array of posts,
 * with their path, title, creation date, and tags, and create the
 * indexes files in each parent folder.
 * The folder 'assets', README.md files, and files starting with a dot
 * are excluded.
 */
function* makeIndexes(path, tags = []) {
  for (const file of readdirSync(path, { withFileTypes: true })) {
    const filePath = join(path, file.name);
    if (file.name.startsWith('.') || ignoredPaths.includes(filePath) || ignoredNames.includes(file.name)) {
      continue;
    }

    if (file.isDirectory()) {
      const posts = [...makeIndexes(filePath, [...tags, file.name])];
      if (posts.length > 0) {
        yield* posts;
        writeIndex(filePath, posts);
      }
    } else if (file.name.endsWith('.md')) {
      const file = readFileSync(filePath, 'utf8');
      // retrieve the post title
      const titleStart = file.indexOf('# ');
      yield {
        tags,
        title: file.slice(titleStart + 2, file.indexOf('\n', titleStart)),
        path: filePath,
        createdAt: getCreationDate(filePath),
      };
    }
  }
}

writeIndex(dirPath, [...makeIndexes(dirPath)]);
