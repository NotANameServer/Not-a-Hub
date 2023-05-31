---
layout: post
author: Julien Castiaux
date: 2022-06-27
title: "Relatif vs Absolu, démystifions les imports python"
---

Dans cet article, nous étudierons les modules en python avec un regard poussé sur la notion de package. Nous étudierons aussi la manière de définir des modules et la manière de les importer de sorte à créer des arborescences cohérentes et à prévenir certains problèmes, notamment les problèmes liés aux imports relatifs.

Cet article part du principe que vous avez déjà utilisé `import` et que vous avez déjà écrit vos propres modules. Si vous pensez avoir besoin d'une remise à niveau, nous vous conseillons de relire le chapitre 7 "Pas à pas vers la modularité (2/2)" du livre "[Apprenez à programmer en Python][goff11]" de Vincent le Goff.

Package
-------

Dans le jargon python, un *package* est un dossier qui contient un fichier `__init__.py` où sont regroupés des modules python. Dans la bibliothèque standard on retrouve par exemple `asyncio`, `email`, `html`, `http`, `importlib`, `tkinter`, `unittest`, `urllib` et `xml`. Côté PyPI on peut citer `flask`, `numpy`, `matplotlib`, `requests`, `fastapi` et `sqlalchemy`. Tous sont des packages où sont regroupés parfois jusqu'à plusieurs centaines de modules python.

Il est rare de développer un projet qui ne va tenir que dans un seul module, la plupart du temps un projet est implémenté au travers de plusieurs modules qui vont s'importer mutuellement et qui sont regroupés dans différents dossiers. Tous ces modules regroupés en différents dossiers doivent pouvoir utiliser les fonctions et les classes qui sont définies dans les autres modules, il est donc important de pouvoir importer et de pouvoir être importé facilement. Python propose deux mécanismes pour importer des choses venant d'autres modules : les imports absolus (au `sys.path`) et les imports relatifs (au package courant).

Import absolu et `sys.path`
---------------------------

Lorsque vous écrivez `import x` ou `from x import y`, vous faites un import absolu. La bibliothèque (le module ou le package) doit se trouver soit dans le *working-directory*, soit être installée dans l'environnement virtuel courant, soit être installée au niveau de l'utilisateur, soit être installée au niveau du système. Python scanne ces différentes sources à la recherche de la bibliothèque demandée pour l'importer. Si après avoir scanné l'ensemble des sources possibles python ne trouve pas la bibliothèque demandée alors il lève une erreur du type `ModuleNotFoundError: No module named 'x'`.

L'ensemble des dossiers que python va scanner à la recherche de la bibliothèque demandée varie d'un système à l'autre. Heureusement, il est possible de récupérer cette information depuis l'interpréteur python via la variable `sys.path`. Ci-dessous un exemple de ce que contient cette variable sur le PC d'un des auteurs :

    >>> import sys
    >>> sys.path
    ['',
    '/usr/lib/python38.zip',
    '/usr/lib/python3.8',
    '/usr/lib/python3.8/lib-dynload',
    '/home/julien/.local/lib/python3.8/site-packages',
    '/usr/local/lib/python3.8/dist-packages',
    '/usr/lib/python3/dist-packages',
    '/usr/lib/python3.8/dist-packages']

Les différents dossiers à scanner sont listés dans l'ordre. La string vide en tout premier est remplacée au moment de l'import par le *working-directory* (`os.getcwd()`), c'est à dire le dossier d'où a été lancé l'interpréteur python. Dans notre cas python a été lancé depuis le dossier `/home/julien`, on obtient donc :

    >>> import os
    >>> os.getcwd()
    '/home/julien'

Au moment de faire un import absolu python va donc chercher la bibliothèque dans l'ordre des dossiers : `/home/julien`, `/usr/lib/python38.zip`, `/usr/lib/python3.8`,…, `/usr/lib/python3.8/dist-packages`. Dans les deux exemples ci-dessus, pour `sys` et `os`, il n'aura scanné que `/home/julien` et `/usr/lib/python38.zip` avant de trouver les deux fichiers `os.py` et `sys.py` dans le dossier `/usr/lib/python3.8`.

Import relatif et `__package__`
-------------------------------

Lorsque vous écrivez `from . import x` ou `from .x import y` vous faites un import relatif. Python n'utilise plus le `sys.path` mais la variable magique `__package__` du module courant pour déterminer où trouver le module à importer. La variable `__package__` est similaire à la variable `__name__` : il s'agit d'une string qui représente le nom du package actuel qui s'ajoute aux noms des différents packages parents. La plupart du temps, `__package__` est juste `__name__` auquel on a retiré le nom du module courant pour n'y laisser que la partie package, nous verrons par la suite qu'il y a quelques exceptions.

Voici quelques exemples de ce que contiennent les variables `__name__` et `__package__` pour quelques modules connus :

    >>> # random est un fichier random.py accessible directement depuis le sys.path
    >>> import random
    >>> random.__name__, random.__package__
    ('random', '')

    >>> # urllib est un dossier avec un fichier __init__.py
    >>> import urllib
    >>> urllib.__name__, urllib.__package__
    ('urllib', 'urllib')

    >>> # urllib.parse est un fichier parse.py dans le dossier urllib
    >>> import urllib.parse
    >>> urllib.parse.__name__, urllib.parse.__package__
    ('urllib.parse', 'urllib')

Au moment de jouer l'instruction `from . import x`, c'est comme si python remplaçait le `.` par le contenu de la variable `__package__`. Disons que cette variable contient la valeur `a.b`, l'instruction devient alors `from a.b import x` : un import absolu.

Si au moment de jouer l'instruction `from . import x`, le module courant n'était pas lié à un quelconque package (sa variable `__package__` était vide), l'erreur suivante se serait produite : `ImportError: attempted relative import with no known parent package`. L'erreur dénote l'impossibilité de faire un import relatif du fait que le module courant n'est pas lié à un package.

La fausse intuition, le piège
-----------------------------

Nous venons de voir les notions de package, d'import absolu et d'import relatif. Nous avons vu qu'un package est un dossier contenant un fichier `__init__.py`, que les imports absolus reposent sur le `sys.path` et que les imports relatifs reposent sur la variable `__package__`.

Cependant cette variable `__package__` nous réserve quelques surprises.

Notre intuition de développeur fait que nous pensons qu'un package est un dossier contenant des modules python, avec un artefact supplémentaire : le fichier `__init__.py`. En suivant notre intuition nous pensons donc qu'à partir du moment où un fichier se trouve dans un tel dossier, il aura forcément une variable `__package__` contenant le nom du dossier.

Notre intuition est fausse : le package n'est pas défini par le dossier, *le package est défini au moment où le fichier `__init__.py` est exécuté*. Si un module python se trouve dans un dossier ayant un fichier `__init__.py` mais que ce fichier `__init__.py` n'a pas été évalué avant d'exécuter le module alors le module aura une variable `__package__` vide !

En d'autres termes, pour qu'un module soit lié à un package, pour qu'un module ait une variable `__package__` définie et non-vide, il **faut** que le fichier `__init__.py` ait été exécuté avant.


Le piège en pratique
--------------------

Étudions le programme suivant :

    ~ $ ls monpkg/
    __init__.py __main__.py tartempion.py
    ~ $ cat monpkg/__init__.py
    print(__file__, f'{__name__=}', f'{__package__=}')
    ~ $ cat monpkg/__main__.py
    print(__file__, f'{__name__=}', f'{__package__=}')
    ~ $ cat monpkg/tartempion.py
    print(__file__, f'{__name__=}', f'{__package__=}')

Il s'agit d'un package minimaliste, seulement trois fichiers : `__init__.py`, `__main__.py` et `tartempion.py`. Les trois fichiers exécutent la même instruction : afficher leurs propres variables `__file__`, `__name__` et `__package__`.

Rappelons que lorsqu'un *package* est importé (lorsque vous faites `import monpkg`), le fichier `__init__.py` est automatiquement joué. Rappelons aussi que lorsqu'un *dossier* est exécuté (lorsque vous faites `python3 monpkg`), le fichier `__main__.py` est automatiquement joué.

Nous allons maintenant étudier 5 manières différentes d'exécuter ce programme.

### Directement exécuter le fichier tartempion.py

    ~ $ python3 monpkg/tartempion.py
    /home/julien/monpkg/tartempion.py __name__='__main__' __package__=None

Dans ce premier exemple, le fichier `tartempion.py` est directement exécuté via la ligne de commande.

Nous constatons que ni le fichier `__init__.py` ni le fichier `__main__.py` n'ont été exécutés automatiquement. Le fichier `__init__.py` n'a pas été exécuté parce que le package n'a pas été importé. Le fichier `__main__.py` n'a pas été exécuté parce le dossier n'a pas été exécuté.

Nous constatons également que le nom du module est `'__main__'` au lieu d'être `'tartempion'`. Il s'agit ici d'une règle en python, le module qui est exécuté en tout premier, le point d'entré, a toujours une variable `__name__` défini à `'__main__'`.

Nous constatons pour finir que le module n'est pas rattaché à un quelconque package puisque le fichier `__init__.py` n'a pas été chargé. Les imports relatifs ne fonctionneront pas dans le cas présent pour le module tartempion.


### Directement exécuter le fichier \_\_main\_\_.py

Dans ce second exemple, le fichier `__main__.py` est directement exécuté via la ligne de commande.

    ~ $ python3 monpkg/__main__.py
    /home/julien/monpkg/__main__.py __name__='__main__' __package__=None

Nous constatons à nouveau que le fichier `__init__.py` n'a pas été automatiquement chargé. Qu'encore une fois la variable `__package__` est donc vide et qu'encore une fois les imports relatifs ne fonctionneront pas. À minima, nous constatons qu'au moins cette fois-ci, le nom du module est cohérent avec le nom du fichier.

### Directement exécuter le dossier monpkg

Dans ce troisième exemple, le dossier `monpkg` est directement exécuté via la ligne de commande.

    ~ $ python3 monpkg
    /home/julien/monpkg/__main__.py __name__='__main__' __package__=''

Force nous est de constater qu'encore une fois le fichier `__init__.py` n'a pas été automatiquement chargé. De ce fait la variable `__package__` est vide et les imports relatifs ne fonctionneront toujours pas.

### Importer \_\_main\_\_.py depuis l'extérieur

Dans ce quatrième exemple, nous ajoutons un fichier `run.py` avec `import monpkg.__main__` pour seule instruction. Nous plaçons ce fichier à côté du dossier monpkg et nous l'exécutons. L'idée ici est de charger à la fois `__init__.py` et `__main__.py` pour avoir à la fois un package (via init) et l'exécuter (via main).

    ~ $ ls
    monpkg run.py…
    ~ $ cat run.py
    import monpkg.__main__
    ~ $ python3 run.py
    /home/julien/monpkg/__init__.py __name__='monpkg' __package__='monpkg'
    /home/julien/monpkg/__main__.py __name__='monpkg.__main__' __package__='monpkg'

Nous constatons cette fois-ci que les deux fichiers `__init__.py` et `__main__.py` ont bien chacun été chargés et exécutés. Nous constatons également que chacun des deux modules partagent une variable `__package__` défini au nom du dossier. Nous sommes enfin dans une situation où les imports relatifs vont fonctionner.

Notez que la ligne `import monpkg.__main__` fait un import absolu. Il fonctionne dans le cas présent car le package `monpkg` se trouve dans le working directory. Pour que le fichier `run.py` puisse être exécuté de partout, même depuis un dossier différent ce celui où ce fichier se trouve, il faut modifier le `sys.path` manuellement *avant* d'importer le package :

    import sys
    import os.path
    sys.path.insert(1, os.path.parent(__file__))
    import monpkg.__main__

Le lecteur attentif aura relevé que le nom du module `__main__.py` n'est pas `'__main__'` mais bien `'monpkg.__main__'`. En effet, du fait que ce module a été importé et non pas directement exécuté, il n'est pas le point d'entré du programme et ne s'appelle donc pas `__main__`. Celui qui s'appelle `__main__` est en fait le fichier `run.py`, c'est lui le point d'entré.

### Exécuter le package avec -m

Dans ce cinquième et dernier exemple, nous utilisons l'option `-m` de la ligne de commande python pour lancer notre package.

    ~ $ python3 -m monpkg
    /home/julien/monpkg/__init__.py __name__='monpkg' __package__='monpkg'
    /home/julien/monpkg/__main__.py __name__='__main__' __package__='monpkg'

Dans ce tout dernier exemple nous constatons à nouveau que les deux fichiers ont été chargés et exécutés. Nous constatons à nouveau que la variable `__package__` est correctement définie et donc que les imports relatifs vont fonctionner. En bonus par rapport à la solution précédente, nous n'avons pas dû recourir à artifice supplémentaire dont le seul rôle était d'importer notre programme.

Conclusion
----------

Les imports relatifs et absolus sont des mécanismes équivalents qui permettent à Python d'être un langage modulaire. Nous avons vu sur quoi reposaient ces deux mécanismes et nous avons étudié en profondeur la notion de package, quelle est leur nature et quel est leur rôle. Nous avons vu que la nature des packages n'était pas aussi simple et intuitive qu'il pourrait sembler. Nous avons cerné en quoi la nature réelle des packages avait son lot d'implication quant à la manière de les exécuter.

Nombreux sont les développeurs, pas si débutants que ça, qui peinent à comprendre et à résoudre les erreurs du type `ImportError: attempted relative import with no known parent package` ou encore `ModuleNotFoundError: No module named ...`. Leur solution est souvent de fournir un fichier supplémentaire, un artifice, un module dont le seul rôle est de modifier le `sys.path` et d'importer leur projet. La réelle solution trop peu connue repose en fait sur l'option `-m` de la ligne de commande python.

Nous pouvons regretter que les nombreux cours négligent d'apporter des explications sur comment structurer des projets python au vu de la nature des packages. Nous pouvons également regretter que le sujet est fort peu documenté même dans la documentation officielle. En outre, l'article du tutoriel officiel de python comporte son lot d'erreurs qui n'ont jamais été adressés en plus de 15 ans.

[goff11]: https://user.oc-static.com/ftp/livre/python/apprenez_a_programmer_en_python.pdf
