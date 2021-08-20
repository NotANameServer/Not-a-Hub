# Programmer en Python, quel IDE choisir

Python est un langage suffisamment simple pour qu'un IDE complet ne soit pas *nécessaire* à avoir une bonne vélocité de développement. Contrairement des langages à la syntaxe plus lourde, il n'est pas forcément nécessaire d'avoir toute une série de patterns automatiquement générée par l'éditeur.

Python a un système de module léger : contrairement à Java où une classe = un fichier, il n'est pas rare d'avoir toute une série de classes liées définies au sain d'un même module. Ceci limite drastiquement la quantité d'`import` nécessaire en début de fichier et extensiblement la nécessité d'avoir ces lignes d'`import` faites automatiquement.

Python propose nativement un environnement REPL (Read-Eval-Print-Loop) via le terminal ou IDLE. Il est donc aisé de tester un bout de code, d'accéder à la documentation au moyen de la fonction `help` ou de lister l'ensemble des méthodes/fonctions d'une classe ou d'un module via la fonction `dir`. Personnellement je trouve qu'il est tout aussi rapide d'ouvrir l'interpréteur et de taper `dir(list)` suivi de `help(list.extend)` que d'utiliser la documentation fournie par un IDE ou de laisse l'autocomplétion me faire des suggestions.

Python est dynamiquement typé. Bien qu'il existe des outils comme [mypy](mypy-lang.org) qui peuvent aider à la vérification des types, peu de modules tirent avantage de la bibliothèque `typing` et un IDE se retrouve fort peu utile pour lever des warning en cas d'incohérence de types.

Tout ceci explique pourquoi un IDE n'est pas *nécessaire* au développement en python. Un éditeur de texte plus léger reste un choix tout aussi viable.

## Mais donc quel IDE ?

Au final il n'y pas d'éditeur qui se démarque particulièrement des autres. Il s'agit surtout d'en choisir un et se l'approprier.

La liste suivante présente une liste non exhaustive:

* [IDLE](https://docs.python.org/3/library/idle.html) (pro: installé de base, con: vraiment limité)
* [Neovim](https://neovim.io/) (pro: très puissant, con: difficile à prendre en main)
* [Onivim](https://v2.onivim.io/) (pro: interface graphique moderne, con: projet très jeune)
* [Emacs](https://www.gnu.org/software/emacs/) (pro: très puissant, con: difficile à prendre en main)
* [Sublime text](https://www.sublimetext.com/3) (pro: léger et rapide, con: pas fort extensible)
* [VS Code](https://code.visualstudio.com/) (pro: complet et extensible, con: lourd)
* [Atom](https://atom.io/) (pro: moderne et open-source, con: lent au démarrage)
* [Pycharm](https://www.jetbrains.com/pycharm/) (pro: IDE complet, con: très lourd)

## Qu'est-ce qu'utilise la populace ?

![langchar](/assets/images/py-ide-langchart.png)