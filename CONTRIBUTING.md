# Comment contribuer

Tous les contributeurs sont priés de respecter les règles de NaN qui sont disponibles sur notre serveur Discord et sur le repository [https://github.com/NotANameServer/discord/](https://github.com/NotANameServer/discord/). Les articles doivent être rédigés en français, les messages de commit ainsi que l'activité sur GitHub peuvent être fait en français ou en anglais. Il est préférable de commencer par ouvrir une issue pour ouvrir une discussion avant d'ouvrir une pull-request pour proposer les changements.

Nous distingons la rédaction des articles (`add`/`edit`/`fix`) des contributions au site-même (`meta`). Il vous est possible de tester vos modifications soit en local en [installant jekyll](https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll/testing-your-github-pages-site-locally-with-jekyll) et quelques [dépendances](https://github.com/NotANameServer/Not-a-Hub/blob/master/Gemfile) supplémentaires sur votre propre machine. Il vous est aussi possible de fork ce repository et de changer un paramettre (repo > settings > pages > branch) pour laisser github s'occuper du rendu de votre branche.

## Contribuer aux articles

Nous avons créé toute une série de templates dans les issues pour vous guider. Vous pouvez [proposer un nouvel article](https://github.com/NotANameServer/Not-a-Hub/issues/new?assignees=&labels=article&template=proposer-un-article.yaml&title=%5BNOUVEL+ARTICLE%5D+) afin d'ouvrir une discussion sur ce que devrait contenir cet article avant de proposer un premier brouillon via une pull-request. Vous pouvez également [commenter un article existant](https://github.com/NotANameServer/Not-a-Hub/issues/new?assignees=&labels=article&template=commenter-un-article.yaml&title=%5BCommentaire%5D+) pour rapporter une erreur ou simplement ouvrir une discussion ou poser une question sur cet article.

## Contribuer au site

Nous vous recommandons de commencer par ouvrir une nouvelle issue "vierge" (sans passer par les templates) pour ouvrir la discussion quant à ce que vous voudriez changer. Vous pouvez ensuite proposer vos changements via une pull-request.

## Convention pour les messages de commit

Chaque message doit commencer par un titre séparé du reste du commit par une ligne vide. Le titre doit de préférence ne pas dépasser 50 caractères et doit commencer par l'un des tags suivant:

 - `add: ` pour l'ajout d'un nouvel article
 - `edit: ` pour la modification du contenu sémantique d'un article
 - `fix: ` pour une correction orthographique ou grammaticale
 - `meta: ` pour les contributions au site même

Faites l'effort de rédiger un message de commit, notez à minimal un paragraphe qui explique *pourquoi* ces changements sont bienvenues et référencez aussi la/les issues auxquelles votre commit est lié.

## Indexage des articles

Lorsque vous ajoutez ou renommez un article, pensez à ajouter un entête de cette forme au début du fichier markdown:

```
---
layout: post
author: <Le nom sous lequel vous souhaitez publier votre article (attention, il sera public)>
date: <La date au format ISO-8601>
title: "Le titre de votre article"
---

```

Cela permettra à l'action GitHub Pages d'indexer automatiquement votre article. Lorsque vous mettez à jour un article, vous pouvez aussi ajouter le champ `last_update` dans l'entête pour indiquer la date de dernière mise à jour tout en conservant la date de publication initiale.

Pensez également à placer le fichier markdown dans le bon dossier correspondant au sujet de votre article pour que les tags appropriés soient automatiquement ajoutés.
Par exemple un article placé dans le dossier `/langages/python/` aura les tags `langages` et `python`.
