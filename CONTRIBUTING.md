# Comment contribuer

Tous les contributeurs sont priés de respecter les règles de NaN qui sont
disponibles sur notre serveur Discord et sur le repository [https://github.com/NotANameServer/discord/](https://github.com/NotANameServer/discord/).

Les articles doivent être rédigés en français, les messages de commit ainsi que l'activité sur GitHub peuvent être fait en français ou en anglais.

## Proposer un article

Commencez par ouvrir une issue dans laquelle vous proposez le sujet de votre article. Cette issue servira à discuter du sujet, rassembler les idées et se mettre d'accord sur le contenu. Cette issue servira aussi à rassembler des ressources et à vérifier qu'il n'existe pas déjà des articles/tutoriels francophone de qualité sur le sujet.

## Rédiger un article

Créez une nouvelle branche dans un fork (ou directement ici si vous le pouvez) dans laquelle vous rédigerez votre premier brouillon, puis ouvrez une pull request en draft pour voir ce qui peut être conservé, modifié, ou écarté, pour faire vérifier l'orthographe, etc.

Lorsque tout le monde est d'accord sur le contenu de votre contribution, elle est fusionnée au dépôt et automatiquement publiée sur le site.

## Modifier un article

Même protocole que pour la rédaction d'un article, créez une branche (dans un fork ou ici si vous le pouvez), puis soumettez vos modifications dans une pull request.

## Autre chose

Ouvrez une issue.

## Contribuer au site

Pour les modifications concernant le site en lui-même, vous devez créer un fork afin de pouvoir tester vos modifications. En effet, le [paramètre](https://github.com/NotANameServer/Not-a-Hub/settings/pages) pour selectionner la branche sur laquelle se base le site est global au repo, si vous le modifiez, le changement sera visible à tous, vous devez donc créer un fork et modifier ce paramètre sur votre repo.

## Convention pour les messages de commit

Chaque message doit commencer par un titre séparé du reste du commit par une ligne vide. Le titre doit de préférence ne pas dépasser 50 caractères et doit commencer par l'un des tags suivant:
 - `add: ` pour l'ajout d'un nouvel article
 - `edit: ` pour la modification du contenu sémantique d'un article
 - `fix: ` pour une correction orthographique ou grammaticale
 - `meta: ` pour tout ce qui ne touche pas un article

Lorsque vous ajoutez un article ou renommez un article sur disque, pensez à exécuter l'indexeur automatique: `python3 index.py` à la racine du repo.

Si vous avez peur d'oublier, vous pouvez le définir comme pre-commit-hook:

	ln -s ../../index.py .git/hooks/pre-commit
