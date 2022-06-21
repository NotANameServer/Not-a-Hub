Relatif vs Absolu, démystifions les imports python
==================================================

Dans cet article nous étudierons les modules en python avec un regard poussé sur la notion de package. Nous étudierons aussi la manière de définir des modules et la manière de les importer de sorte à créer des arborescences cohérentes et à prévenir certains problèmes, notamment les problèmes liés aux import relatifs.

Cet article part du principe que vous avez déjà utilisé `import` et que vous avez déjà écrit vos propres modules. Si vous pensez avoir besoin d'une remise à niveau, nous vous conseillons de relire les deux chapitres "Pas à pas vers la modularité" du livre "[Apprenez à programmer en Python][goff11]" de Vincent le Goff.

Package
-------

Vous connaissez certainement les deux variables magiques `__file__` et `__name__`, ces deux variables sont définies automatiquement par python pour chaque module, la première contient le chemin complet où se trouve le fichier sur le disque et la seconde contient le nom du module courant, relatif à la racine du projet.

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

Dans le jargon python, un *package* est un dossier qui contient un fichier `__init__.py` et dans lequel se trouvent généralement d'autres modules python (des fichier se finissant en `.py`). Il n'y a qu'assez peu de packages dans la bibliothèque standard de python: `email`, `html`, `http`, `importlib`, `tkinter`, `unittest`, `urllib` et `xml`. Ils sont par contre très communs lorsqu'on regarde du côté des bilbiothèques hébergées sur pypi: `flask`, `numpy`, `matplotlib`, `requests`, `fastapi` et `sqlalchemy`; tous sont des packages où sont regroupés parfois jusqu'à plusieurs centaines de modules python.

Il est rare de développer un projet qui ne va tenir que dans un seul module python, la plupart du temps un projet est implémenté au travers de plusieurs modules qui vont s'importer mutuellement et qui sont regroupés dans différents dossiers. Tous ces modules regroupés en différents dossiers doivent pouvoir utiliser les fonctions et les classes qui sont définies dans les autres modules, il est donc important de pouvoir importer et de pouvoir être importé facilement. Python propose deux méchanismes pour importer des choses venant d'autres modules : les import relatifs (au package courant) et les import absolus (au `sys.path`).

Import relatif vs import absolu
-------------------------------

Lorsque l'instruction `import` est évaluée, python va analyser la ligne pour déterminer où il doit aller trouver l'élément à importer. Lorsque le nom du module à importer commence par un point, python charge ce module depuis le package courant, on parle d'un import relatif. Lorsque le nom du module à importer ne commence pas par un point on parle alors d'un import absolu.

Il y a des situations où l'on n'a pas d'autre choix que d'utiliser un import absolu, par exemple lorsque ce qu'on importe ne se trouve pas dans le package courant ni dans le package parent. Par exemple, tous les modules de la bibliothèque standard ainsi que tous les modules qui ont été installés via pip ne peuvent être importés qu'avec un import absolu. Il n'y a pas d'autre moyen d'importer le module `random` que de taper `import random`.

Lorsqu'on est dans son propre logiciel, qu'on veut importer un fichier qui se trouve dans le même dossier, alors la question se pose. Mieux vaut-il préférer un import relatif ou bien un import absolu ? En fait, il n'y a pas de réponse définitive à cette question, certains priviligeront des imports absolus, d'autres des imports relatifs, d'autres un judicieux mélange des deux en fonction des situations.

Pour reprendre l'exemple fourni dans le tutoriel officiel sur les modules:

    sound/                          Top-level package
          __init__.py               Initialize the sound package
          formats/                  Subpackage for file format conversions
                  __init__.py
                  wavread.py
                  ...
          filters/                  Subpackage for filters
                  __init__.py
                  equalizer.py
                  ...

Dans le module `sound.filters.equalizer` il est possible d'importer `wavread` soit avec un import absolu en repartant du top-level package: `from sound.formats import wavread`, soit avec un import relatif: `from ..formats import wavread`.

To be or not to be?
-------------------

Le truc pourri en python par rapport aux packages est qu'un module python se trouvant dans un dossier n'aura pas forcément ce dossier comme package, même si le dossier en question possède un fichier `__init__.py`. En réalité, tout dépend de comment a été chargé le module en question. Nous avons vu plus haut que les imports relatifs reposent sur le package du module courant et que ce nom de package était repris dans la variable magique `__package__` qui est propre à chaque module.

Étudions à présent le programme suivant:

    ~ $ ls monpkg/
    __init__.py  __main__.py
    ~ $ cat monpkg/__init__.py
    print(__file__, f'{__name__=}', f'{__package__=}')
    ~ $ cat monpkg/__main__.py
    print(__file__, f'{__name__=}', f'{__package__=}')

Il s'agit d'un package minimaliste, seulement deux fichiers : `__init__.py` et `__main__.py`, tous les deux exécutent la même instruction: afficher leur propre file, name et package. Petit rappel : lorsqu'un package est importé pour la première fois, son fichier `__init__.py` est exécuté. Deuxième petit rappel : lorsqu'un package ou un dossier est exécuté, son fichier `__main__.py` est exécuté.

Étudions maintenant 4 exécutions de ce même programme.

### Exécuter le fichier main.py

    ~ $ python3 monpkg/__main__.py
    /home/julien/monpkg/__main__.py __name__='__main__' __package__=None

Dans ce premier exemple, le fichier `__main__.py` est directement exécuté via la ligne de commande. On constate avec étonnement que la variable magique `__package__` dénote l'absence de package courant. On constate également que le fichier `__init__.py` n'a pas été automatiquement joué, ceci vient confirmer que le module a été chargé *sans être lié au package monpkg*.

Vous cherchiez une explication sur pourquoi dans vos propres projets vous aviez des erreurs du type "attempted relative import with no known parent package", ne cherchez plus. Parce que `__main__.py` a été directement exécuté, python a décidé qu'il n'y avait pas de package et comme il n'y a pas de package il n'est pas possible de faire d'import relatif. Oui python est pourri à cet égard.

### Exécuter le dossier monpkg

    ~ $ python3 monpkg
    /home/julien/monpkg/__main__.py __name__='__main__' __package__=''

Dans ce second exemple, nous profitons du fait qu'il est possible d'exécuter un dossier via la ligne de commande. L'idée ici est de ne plus exécuter un fichier précis (ce qui mènerait à ce que ce fichier ne soit pas lié au package) mais bien d'exécuter le package directement. Malheureusement, on constate à nouveau que si le fichier `__main__.py` a été automatiquement joué, ce fichier n'est toujours pas lié au package et que le fichier `__init__.py` n'a pas non plus été chargé et exécuté. On constate à nouveau que python est pourri à cet égard.

### Importer main.py depuis l'extérieur

    ~ $ python3 -c 'import monpkg.__main__'
    /home/julien/monpkg/__init__.py __name__='monpkg' __package__='monpkg'
    /home/julien/monpkg/__main__.py __name__='monpkg.__main__' __package__='monpkg'

Dans ce troisième exemple, nous ne lançons plus le programme directement via la ligne de commande, à la place nous invoquons l'interpréteur pour qu'il joue l'instruction `import monpkg.__main__`. L'idée ici est de contourner les bizzareries de la ligne de commande pour à la place `import` notre package. Nous constatons que grâce à cette petite astuce, cette fois-ci, le package est bien correctement chargé : les variables `__package__` contiennent ce qu'on s'attend à voir et les fichier `__init__.py` a été chargé à la volée. Le seul bémol est que le `__name__` du fichier `__main__.py` atteste `monpkg.__main__` et non pas simplement `__main__`. Ce bémol s'explique par le fait que ce qui s'appelle `__main__` dans ce contexte est ce qui a été exécuté en premier lieu : l'instruction contenue dans le `-c` de la ligne de commande.

Il est tout à fait possible de décider d'ignorer que le fichier `__main__.py` n'est pas le véritable `__main__` du programme. L'essentiel est que la variable `__package__` soit correctement remplie et avec les bonnes informations, cet objectif est atteint.

Notez qu'au lieu de faire `-c 'import monpkg.__main__` on aurait pu écrire un programme (exemple `run.py`) qui se serait trouvé au même niveau que le package (donc en *dehors* du pacakge, à *côté* de celui-ci) et dont la seule instruction aurait été la fameuse `import monpkg.__main__`. On aurait alors exécuté `python3 run.py` à la place de `python3 -c 'import monpkg.__main__`.

### Exécuter le package avec -m

    ~ $ python3 -m monpkg
    /home/julien/monpkg/__init__.py __name__='monpkg' __package__='monpkg'
    /home/julien/monpkg/__main__.py __name__='__main__' __package__='monpkg'

Dans ce quatrième et dernier exemple, nous lançons le programme au moment de l'option `-m` de la ligne de commande. Cette option est succintement décrite comme "run library module as a script" dans le manuel de python. La réalité est beaucoup plus intéressante que ne le laisse entendre la toute petite phrase du manuel, on constate qu'en utilisant cette option le package est enfin chargé de la manière escompté : le package est chargé, les variables `__name__` et `__package__` sont justes et nous n'avons pas eu recours à un quelconque artifice (un module en plus dont le seul but était d'`import` notre main).

**Nous vous recommandons de systématiquement lancer vos projets avec l'option `-m` !**

Conclusion
----------

La notion de *package* est une notion qui est mal comprise de la part des développeurs python, autant novices qu'avancés. Cette notion est cependant primordiale pour correctement comprendre comment fonctionnent les imports relatifs et donc comment structurer et exécuter ses projets.

Nous pouvons regretter que le chapitre qui aborde les modules dans [le tutoriel officielle][pydoc/tuto/module] de python soit approximatif. Nous pouvons aussi regretter que faute de resources complètes et fiables à ce propos, les différents cours tant francophones qu'anglophones tombent aussi dans le travers de n'apporter que de piètre explications sur la manière de structurer un projet python.

Cet article est venu combler ces lacunes. Il a montré le rôle essentiel qu'a la variable magique `__package__` et que le contenu de cette variable dépend de la manière dont est exécuté un projet python. Il a aussi démontré que l'option en ligne de commande `-m` était la meilleure solution pour lancer un projet python.



[pydoc/tuto/module]: https://docs.python.org/3/tutorial/modules.html
[goff11]: https://user.oc-static.com/ftp/livre/python/apprenez_a_programmer_en_python.pdf
