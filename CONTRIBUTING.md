# Comment contribuer

Tous les contributeurs sont priés de respecter les règles de NaN qui sont
disponibles sur notre serveur Discord.

Les articles doivent être rédigés en français.

## Schéma à suivre:

 - Ouvrez une issue pour discuter de l'article que vous souhaiteriez écrire, définir quel en sera le contenu, rassembler des idées.
 - Créez une nouvelle branche dans un fork, et faites vos commits dans cette branche
 - Rédigez un brouillon de votre coté, puis ouvrez une pull request en draft pour voir ce qui peut être conservé, modifié, ou écarté, pour faire vérifier l'orthographe, etc

Lorsque tout le monde est d'accord sur le contenu de votre contribution, elle est fusionnée au dépôt, et automatiquement publiée sur le site.

## Convention pour les messages de commit

Les messages de commit ainsi que l'activité sur GitHub peuvent être fait en français ou en anglais.
Chaque message doit commencer par un titre séparé du reste du commit par une ligne vide. Le titre doit de préférence ne pas dépasser 50 caractères et doit commencer par l'un des tags suivant:
 - `add: ` pour l'ajout d'un nouvel article, `edit: ` pour la modification du contenu sémantique d'un article
 - `fix: ` pour une correction orthographique ou grammaticale
 - `meta: ` pour tout ce qui ne touche pas un article.

Lorsque vous ajoutez un article ou renommez un article sur disque, pensez à exécuter l'indexer automatique: `python3 index.py` à la racine du repo.

Si vous avez peur d'oublier, vous pouvez le définir comme pre-commit-hook:

	ln -s ../../index.py .git/hooks/pre-commit
