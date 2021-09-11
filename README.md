# Not a Hub

<https://hub.notaname.fr>

## Comment contribuer

Tous les contributeurs sont priés de respecter les règles de NaN qui sont
disponibles sur notre serveur Discord.

Vous pouvez contribuer selon le flux classique: fork, nouvelle branche,
commit, pull-request. Les articles doivent être rédigé en français. Les
messages de commit ainsi que l'activité sur GitHub peuvent être fait ou
en français ou en anglais.

Vous êtes prié de suivre notre convention concernant les messages de
commits. Chaque message doit commencer par un titre séparé du reste du
commit par une ligne vide. Le titre doit de préférence ne pas dépasser 50
caractères et doit commencer par l'un des tags suivant: `add: ` pour
l'ajout d'un nouvel article, `edit: ` pour la modification du contenu
sémantique d'un article, `fix: ` pour une correction orthographique ou
grammaticale, `meta: ` pour tout ce qui ne touche pas un article.

Lorsque vous ajoutez un article ou renommer un article sur disque, pensez
à exécuter l'indexer automatique: `python3 index.py` à la racine du repo,
si vous avez peur d'oublier, vous pouvez le définir comme pre-commit-hook:

	ln -s ../../index.py .git/hooks/pre-commit
