Relatif vs Absolu, démystifions les imports python
==================================================

Dans cet article nous étudions les modules en python avec un regard poussé sur la notion de package. Nous étudions la manière de définir des modules et la manière de les importer de sorte à créer des arborescences cohérentes et à prévenir certains problèmes, notamment les problèmes liés aux import relatifs.

Cet article part du principe que vous avez déjà utilisé `import` et que vous avez déjà écrit vos propres modules. Si vous pensez avoir besoin d'une remise à niveau, nous vous conseillons de relire les deux chapitres "Pas à pas vers la modularité" du livre "[Apprenez à programmer en Python][goff11]" de Vincent le Goff.

Package
-------

Vous connaissez certainement les deux variables magiques `__file__` et `__name__`, ces deux variables sont définis automatiquement par python pour chaque module, la première contient le chemin complet où se trouve le fichier sur le disque et la seconde contient le nom du module courant relatif à la racine du projet.

    >>> import random
    >>> random.__name__
    'random'
    >>> random.__file__
    '/usr/lib/python3.9/random.py'

    >>> import urllib.parse
    >>> urllib.parse.__name__
    'urllib.parse'
    >>> urllib.parse.__file__
    '/usr/lib/python3.9/urllib/parse.py

Mais vous êtes vous déjà intéressé à la variable `__package__` ?

Au même titre que les deux autres, `__package__` est une variable magique qui contient non pas le nom du module courant mais bien le nom du *package* dans lequel le module se trouve.

    >>> import random
    >>> random.__package__
    ''

    >>> import urllib.parse
    >>> urllib.parse.__package__
    'urllib'

Dans le jargon python, un *package* est un dossier qui contient un fichier `__init__.py` et dans lequel se trouvent généralement d'autres modules python (des fichier se finissant en `.py`). Il n'y a qu'assez peu de packages dans la bibliothèque standard de python: `email`, `html`, `http`, `importlib`, `tkinter`, `unittest`, `urllib` et `xml`. Ils sont par contre très commun lorsqu'un regarde du côté des bilbiothèques hébergées sur pypi: `flask`, `numpy`, `matplotlib`, `requests`, `fastapi` et `sqlalchemy`; tous sont des packages où sont regroupés parfois jusqu'à plusieurs centaines de modules python.

Il est rare de développer un projet qui ne va tenir que dans un seul module python, la plupart du temps un projet est implémenté au travers de plusieurs modules qui vont s'importer mutuellement et qui sont regroupés dans différents dossiers. Tous ces modules regroupés en différents dossiers doivent pouvoir utiliser les fonctions et les classes qui sont définis dans les autres modules, il est donc important de pouvoir importer et de pouvoir être importé facilement. Python propose deux méchanismes pour importer des choses venant d'autres modules: les import relatifs (au package courant) et les import absolus (au `sys.path`).

Import relatif vs import absolu
-------------------------------




Comment lancer ses projets
--------------------------

TODO

Une documentation peu fiable
----------------------------

TODO

Conclusion
----------

La notion de *package* est une notion qui est mal comprise de la part des développeurs python, autant novices qu'avancés. Cette notion est cependant priomordiale pour correctement comprendre comment fonctionnent les imports relatifs et donc comment structurer et exécuter ses projets.

Nous pouvons regretter que le chapitre qui aborde les modules dans [le tutoriel officielle][pydoc/tuto/module] de python soit approximatif. Nous pouvons aussi regretter que faute de resources complètes et fiables à ce propos, les différents cours tant francophones qu'anglophones tombent aussi dans le travers de n'apporter que de piètre explications sur la manière de structurer un projet python.

Cet article est venu combler ces lacunes. Il a montré le rôle essentiel du fichier `__main__.py` et de l'option `-m` de la ligne de commande tout en démontrant que les alternatives n'étaient pas viable.



[pydoc/tuto/module]: https://docs.python.org/3/tutorial/modules.html
[goff11]: https://user.oc-static.com/ftp/livre/python/apprenez_a_programmer_en_python.pdf
