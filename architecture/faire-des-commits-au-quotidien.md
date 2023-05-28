Faire des commits au quotidien
==============================

Vous savez donc comment faire des beaux [messages de commit dans git] mais au moment de passer à la pratique vous êtes perdus. Vous aviez l'habitude de créer des nouveaux commits à intervalle régulier pour envoyer votre travail sur GitHub et ainsi avoir une copie de secours. Vos commits étaient courts, écrits à coup de `-m`, et décrivaient ce que vous aviez changé ces deux/trois dernières heures.

Vous avez aussi commencé à travailler avec d'autres personnes et donc à faire ou à recevoir des *reviews* sur GitHub. Vous êtes ainsi tombés sur une branche avec des dizaines de commits, résultat de la pratique de commit le travail effectué toutes les deux/trois heures, branche que vous vous retrouvez soudainement à review... Dur travail...

Vous voudriez continuer de créer des commits toutes les deux/trois heures pour garder une sauvegarde sur GitHub... Vous voudriez aussi qu'au moment de la review, tous les commits soient bien remis dans l'ordre et que chacun soit accompagné d'un chouette message.

Cet article vous explique comment réconcilier les deux, comment continuer à faire des petits commits incrémentaux pendant le développement, comment nettoyer sa branche juste avant d'ouvrir la pull/merge-request et comment continuer à commit dessus. En des termes plus techniques, cet article vous explique comment réécrire l'historique de vos branches.

[messages de commit dans git]: https://hub.notaname.fr/architecture/les-messages-de-commit-dans-git

## Solution du pauvre : Squash and Merge

Une première solution (très facile) est de faire fi de l'historique des commits dans la branche, vous vous dites qu'au final ce qui compte c'est ce qui arrivera sur la branche `main` pour la postérité, que vous pouvez vous débrouiller pour votre review avec ce qui est écrit dans le message de la pull/merge-request.

GitHub a une solution pour ça, c'est ce bouton:

![IDEs chart]({{ site.baseurl }}/assets/images/github-squash.png)

En utilisant cette approche, au moment de merger votre branche, GitHub va fusionner tous les commits de la branche en un seul. Il vous demandera aussi de choisir un titre et un message pour ce nouveau commit, il vous proposera par défaut le titre et le message de la pull/merge-request.

Super facile donc ! Au moment d'ouvrir votre pull/merge-request, vous pouvez prendre le temps d'écrire un bon titre et un bon message. Vos collègues reviewers seront contents parce qu'il y aura une bonne description du travail, description qui se retrouvera aussi dans l'historique de la branche `main` une fois la PR/MR mergée !

Attention, cette approche ne fonctionne pas si la branche contient plusieurs travaux indépendants, par exemple un petit correctif de bug en marge du travail principal. Imaginez la situation si dans quelques semaines vous étiez amenés à *revert* le commit en question, vous ré-introduiriez le bug qui avait été corrigé. Idéalement il aurait dû y avoir deux commits séparés, pas possible d'utiliser *squash and merge* dans ce cas là.

## Réécrire tout l'historique de sa branche

Une seconde solution est de décider de ne pas se préoccuper de ses commits le temps du développement, de faire des petits commits type "wip" régulièrement et de les envoyer sur GitHub histoire d'avoir une copie quelque part. Ensuite au moment venu de proposer sa branche dans une PR/MR, d'annuler uniquement les commits tout en gardant les fichiers modifiés sur le disque, ouvrant ainsi la possibilité de *refaire* des commits bien propre.

### Reset

Pour cette approche, il est possible d'utiliser la commande `reset`. Très précisément, `reset` permet de faire pointer la branche courante sur un autre commit, la commande pourrait être `move-this-branch-to-another-commit` mais `reset` est plus court à écrire. La commande prend un numéro de commit comme argument, le numéro du commit sur lequel faire pointer la branche. Dans ce cas-ci comme nous voulons annuler tous les commits propres à la branche, vous devez *reset* sur le commit sur lequel votre branche est basée, c'est-à-dire le commit qui précède les commits propres à votre branche.

Attention, il est impératif que vous utilisiez `reset` **sans** les options `--hard` ou `--soft` :

* `--hard` aurait pour effet d'annuler toutes vos modifications sur disque, dans le cas présent vous voulez justement conserver toutes ces modifications ;
* `--soft` aurait pour effet de recréer un seul commit sur base de tous les fichiers modifiés, dans le cas présent vous voulez potentiellement refaire plusieurs commits ou bien ne pas conserver certains fichiers.

Une fois la commande exécutée, vous pouvez recréer vos commits un à un cette fois en prenant le temps de rédiger de beaux messages et en séparant dans différents commits ce qui doit l'être.

Une fois l'historique correctement réécrit, il sera nécessaire d'envoyer les changements sur GitHub avec `push`, GitHub vous empêchera d'envoyer vos modifications parce que l'historique des deux branches (locale sur votre machine vs distante sur GitHub) n'est plus cohérent. C'est normal puisque l'historique vient d'être réécrit, dans cette situation il est donc normal d'utiliser `push` avec `--force-with-lease`.

Attention, utiliser `--force` écrase systématiquement la branche sur GitHub par votre branche sur votre PC. Si vous avez un collègue qui a poussé des commits sur votre branche entre temps, utiliser `--force` écrasera son travail. Utiliser `--force-with-lease` permet d'éviter cette situation, il force uniquement si il n'y a pas de nouveaux commits.

### Exemple

Prenons la branche dans laquelle ce présent article est rédigé à titre d'exemple:

```bash
$ git log --oneline
c66a677 wip
6554ca8 wip
bc92aa7 add: how to cleanup git branches before a review
d64706e edit: ajout de liens entre articles
84481d7 fix: wrong index
```

De tous ces commits, uniquement les trois premiers (`c66a677`, `6554ca8` et `bc92aa7`) font partie de notre branche, les deux derniers sont d'anciens commits de la branche master. Puisque nous voulons annuler tous les commits de notre branche, nous voulons déplacer (*reset*) notre branche sur le 1er commit ne faisant par partie de notre travail, nous voulons donc la déplacer sur `d64706e edit: ajout de liens entre articles`.

```bash
$ git reset d64706e
$ git status
On branch lazor/new-git-cleanup
Your branch is behind 'origin/lazor/new-git-cleanup' by 3 commits, and can be fast-forwarded.
  (use "git pull" to update your local branch)

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   architecture/index.md
	modified:   index.md
	modified:   sitemap.txt

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	architecture/nettoyer-sa-branche-git-avant-d'ouvrir-une-pr.md
	assets/images/github-squash.png

no changes added to commit (use "git add" and/or "git commit -a")
```

Si nous décidons de créer un seul commit avec l'ensemble des modifications, nous pouvons faire:

```bash
$ git add -A
$ git commit
[lazor/new-git-cleanup 7b99b92] new: how to cleanup git branches before a review
 5 files changed, 91 insertions(+)
 create mode 100644 architecture/nettoyer-sa-branche-git-avant-d'ouvrir-une-pr.md
 create mode 100644 assets/images/github-squash.png
```

Nous constatons comme attendu que l'historique de notre branche locale n'est plus cohérent avec celui de notre branche sur GitHub et il nous faut donc forcer (avec `--force-with-lease` qui est plus sur que `--force`) GitHub à utiliser notre branche locale. Notez que le conseil de git qui voudrait qu'on `pull` est complètement idiot dans le cas présent.

```bash
$ git status
On branch lazor/new-git-cleanup
Your branch and 'origin/lazor/new-git-cleanup' have diverged,
and have 1 and 3 different commits each, respectively.
  (use "git pull" to merge the remote branch into yours)

nothing to commit, working tree clean

$ git push --force-with-lease
Enumerating objects: 17, done.
Counting objects: 100% (17/17), done.
Delta compression using up to 16 threads
Compressing objects: 100% (10/10), done.
Writing objects: 100% (10/10), 16.46 KiB | 8.23 MiB/s, done.
Total 10 (delta 4), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (4/4), completed with 4 local objects.
To github.com:NotANameServer/Not-a-Hub.git
 + c66a677...7b99b92 lazor/new-git-cleanup -> lazor/new-git-cleanup (forced update)
```

## Juste modifier un précédent commit

Réécrire l'ensemble de l'historique à chaque changement peut être très fastidieux, imaginez la situation où vous avez réorganisé votre travail en 5 beaux commits et que lors de la review on vous demande d'apporter des modifications à plusieurs fichiers, certains dans votre 2e commit, certains dans votre 3e commit. Vous ne voulez pas perdre du temps à reset l'ensemble de vos commits, les recréer un à un en corrigeant ce qui doit l'être et repush. Vous voulez plutôt venir modifier un précédent commit sans changer les autres, c'est possible avec `--amend` et `--fixup`.

### Amend

Utiliser `commit` avec l'option `--amend` permet de modifier le tout dernier commit. Vous n'avez donc qu'à faire vos modifications, les `git add` et ensuite `git commit --amend` pour intégrer ces modifications dans le dernier commit. Vous aurez aussi l'occasion de modifier le message de commit, très pratique pour corriger les fautes d'orthographe.

### Fixup & Rebase

Utiliser `commit` avec l'option `--fixup` permet de créer un nouveau commit qui pourra être intégré avec n'importe quel commit existant. Comme pour *amend*, vous commencez par faire vos modifications, les `git add` et ensuite `git commit --fixup numéro-du-commit`, où "numéro-du-commit" correspond au commit à modifier. Contrairement à *amend* qui modifie directement le commit, *fixup* crée un *nouveau* commit par dessus tous les autres et il reste encore une étape à faire pour l'intégrer au bon endroit.

Git propose aussi un outil pour réordonner des commits et les fusionner, cet outil s'appelle le *rebase interactif* et permet de traiter automatiquement les commits *fixup*. Typiquement vous allez utiliser la commande suivante: `git rebase -i --autosquash numéro-de-commit` où le numéro de commit correspond à un commit suffisamment loin dans le passé, vous pouvez écrire HEAD~10 (le 10ème précédent commit) pour brasser large, vous pouvez réutiliser le même commit que vous aviez mis dans l'étape de *reset* plus haut, c'est à dire le commit sur lequel votre branche est basée.

En reprenant la même branche que dans le précédent exemple:

```bash
git add ...  # vous faites tous vos ajouts, peut-être avec -p

$ git log --oneline
7b99b92 new: how to cleanup git branches before a review
d64706e edit: ajout de liens entre articles
84481d7 fix: wrong index

$ git commit --fixup 7b99b92
[lazor/new-git-cleanup f77d973] fixup! new: how to cleanup git branches before a review
 1 file changed, 48 insertions(+), 6 deletions(-)

$ git rebase -i --autosquash 84481d7
Successfully rebased and updated refs/heads/lazor/new-git-cleanup.
```

Pendant l'étape du *rebase*, une fenêtre s'est ouverte pour vous demander comment réordonner l'historique, avec l'option `--autosquash` les commits fixup ont déjà été déplacés au bon endroit et la bonne action a déjà été sélectionnée, vous pouvez donc simplement sauvegarder et quitter.

À nouveau, puisque vous avez réécrit l'historique, vous devrez pousser vos commits avec l'option `--force-with-lease`.

## Conclusion

Dans cet article nous avons identifié différentes situations communes du cycle de vie d'une branche. Nous avons vu qu'on peut très bien créer des petits commits "wip" incrémentaux le temps du développement car il est parfaitement possible de tout nettoyer juste avant de proposer sa branche en pull/merge-request. Nous avons aussi vu qu'une fois qu'un historique est nettoyé, il est toujours possible de continuer à créer des petit commits "fixup" incrémentaux qui pourront être injectés au bon endroit dans l'historique le moment venu.
