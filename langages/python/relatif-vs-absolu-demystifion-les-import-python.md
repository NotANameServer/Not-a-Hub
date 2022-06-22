Relatif vs Absolu, démystifions les imports python
==================================================

Dans cet article, nous allons étudier la notion de package. De sa définition jusqu'à son utilisation, nous tâcherons de montrer comment réaliser une arborescence cohérente prévenant ainsi les erreurs.

Cet article suppose que vous êtes familiers avec les imports et la manipulation de modules. Si vous pensez avoir besoin d'une remise à niveau, nous vous conseillons de lire ou de relire "Pas à pas vers la modularité" du livre "[Apprenez à programmer en Python][goff11]" de Vincent le Goff.

Package
-------

Si vous lisez ceci, vous connaissez certainement `__file__` et `__name__`, ces deux variables magiques sont définies automatiquement pour chaque module. Pour rappel, `__file__` contient le chemin d'accès absolu du fichier, alors que `__name__` contient le nom du module courant relatif à la racine du projet.

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

Mais vous êtes-vous déjà intéressé à `__package__` ?

Au même titre que `__file__` et `__name__`, `__package__` est une variable magique. Elle contient le nom du *package* dans lequel se trouve le module.

    >>> import random
    >>> random.__package__
    ''

    >>> import urllib.parse
    >>> urllib.parse.__package__
    'urllib'

Formellement, un *package* est un dossier contenant un fichier `__init__.py`. Si la simple présence de ce fichier suffit à définir un dossier en tant que package, on y retrouve habituellement des modules, des dossiers, mais aussi des packages. En effet, un package peut contenir des packages ! On parle alors de sub packages.

Il est rare de développer un projet dans un seul et unique module. En règle général, un projet est fragmenté en modules, packages, dossier. Sans tenir compte de son emplacement, un module doit pouvoir faire appel aux fonctionnalités défini dans des modules distincts. Afin d'y parvenir, nous devons utiliser les imports. Python en propose deux variations : les import relatifs (au package courant) et les import absolus (au `sys.path`).

Import relatif vs import absolu
-------------------------------

Lorsque l'instruction `import` est évaluée, python analyse l'entièreté de la ligne afin de déterminer où trouver l'élément à importer. Si l'import commence par un point, python charge l'élément depuis le package courant, on parle d'un import relatif. Inversement, si l'import ne commence pas par un point, on parle d'un import absolu.

L'import absolu s’avère intéressant lorsque l'élément importé ne se trouve ni dans le package courant ni dans le package parent. C'est le cas pour l'ensemble des modules de la bibliothèque standard ainsi que pour ceux installés avec pip.

Il n'y a pas d'autre moyen d'importer `random` qu'avec `import random`.

Lorsque les deux imports sont possibles, mieux vaut-il préférer un import relatif ou un import absolu ? En fait, il n'y a pas de réponse définitive à cette question. Certains privilégieront les imports absolus, quand d’autre se tourneront vers les imports relatifs. Enfin, en fonction des situations, une judicieuse combinaison d’imports absolus et relatifs peut s’avérer plus intéressante.

Illustrons ces propos par un exemple :

On retrouve dans le tutoriel officiel sur les modules la structure suivante :

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

Admettons que l’on se situe dans equalizer.py et que l’on souhaite importer wavread.py. Nous pouvons utiliser un import absolu, dans ce cas, on part du top-level package pour atteindre le module cible. On a alors : `from sound.formats import wavread`. L’autre possibilité est d’utiliser un import relatif, se traduisant comme suit : `from ..formats import wavread`. Comme nous pouvons le remarquer, une manière d’importer ne prévaut pas sur une autre, cela relève davantage de la préférence du développeur.

To be or not to be?
-------------------

Si on ne cesse de faire l'éloge de Python (à juste titre), il comporte aussi son lot de fragilités, l’une d’elle étant liée aux packages. En effet, un module python qui se trouve dans un package ne sera pas forcément affilié à celui-ci ! En réalité, cela va dépendre de la manière dont a été chargé le module en question. Pour illustrer ce propos, nous allons étudier quatre exemples durant lesquels l’utilité de `__package__` sera pleinement révélé !

Supposons que l’on dispose d’un package structuré ainsi :

    ~ $ ls monpkg/
    __init__.py __main__.py
    ~ $ cat monpkg/__init__.py
    print(__file__, f'{__name__=}', f'{__package__=}')
    ~ $ cat monpkg/__main__.py
    print(__file__, f'{__name__=}', f'{__package__=}')

Il s'agit d'un package minimaliste composé uniquement de deux fichiers : `__init__.py` et `__main__.py`. Tous deux exécutent la même instruction : afficher leur propre file, name et package. Pour rappel, lorsqu'un package est importé son fichier `__main__.py` est exécuté. De plus, s'il s'agit de la première fois, son fichier `__init__.py` est aussi exécuté.

### Exécuter le fichier main.py

Le fichier `__main__.py` est directement exécuté via la ligne de commande.

    ~ $ python3 monpkg/__main__.py
    /home/julien/monpkg/__main__.py __name__='__main__' __package__=None

En premier lieu, il est à noter que__init__.py n’a pas été joué automatiquement. Plus intéressant encore, `__package__` contient « None », cela nous indique que le fichier __main__.py est affilié à aucun package. En fait, il s’agit d’une cause bien connue de l'erreur "attempted relative import with no known parent package". `__main__.py` étant directement exécuté, Python l’interprète comme un simple module, de ce fait, il n'est donc pas possible de réaliser un import relatif ... (ceux-ci étant propre aux packages)

### Exécuter le dossier monpkg

    ~ $ python3 monpkg
    /home/julien/monpkg/__main__.py __name__='__main__' __package__=''

Voyons ce qu’il en est lorsque nous essayons d'exécuter le package directement.
Si `__init__.py` n’a pas été joué, `__main__.py` a quant à lui bien été exécuté ! Cependant, on remarque que ce dernier n'est toujours pas lié au package. En effet, `__package__` est à nouveau vide…

### Importer main.py depuis l'extérieur

    ~ $ python3 -c 'import monpkg.__main__'
    /home/julien/monpkg/__init__.py __name__='monpkg' __package__='monpkg'
    /home/julien/monpkg/__main__.py __name__='monpkg.__main__' __package__='monpkg'

Cette fois-ci, nous avons choisi d’utiliser l'interpréteur en lui demandant de jouer `import monpkg.__main__`.

En réalisant un `import`, nous évitons les comportements induits par la ligne de commande. Avec cette manipulation, le package est correctement chargé. `__package__` contient `monpkg` et le fichier `__init__.py` a été chargé à la volée. Seule ombre au tableau, `__name__` du fichier `__main__.py` contient `monpkg.__main__` et non pas `__main__`. Ce comportement s'explique par le fait que `__main__` , dans ce contexte, renvoie à ce qui a exécuté en premier lieu : `import monpkg.__main__`.

Il est toutefois important de noter qu’il s’agit d’un défaut qui n’en a que le nom. En effet, le but premier étant que `__package__` soit correctement rempli.

À titre informatif, nous aurions obtenu le même comportement si nous avions exécuté un programme (nommé habituellement `run.py`). En effet, ce dernier se serait situé au même niveau que le package (donc en *dehors* du package, à *côté* de celui-ci) et aurait pour seule instruction `import monpkg.__main__`. Enfin, on aurait remplacé `python3 -c 'import monpkg.__main__` par `python3 run.py`.

### Exécuter le package avec -m

    ~ $ python3 -m monpkg
    /home/julien/monpkg/__init__.py __name__='monpkg' __package__='monpkg'
    /home/julien/monpkg/__main__.py __name__='__main__' __package__='monpkg'

Dans ce dernier exemple, nous exécutons `monpkg` avec l'option `-m` de la ligne de commande. Dans le manuel Python, elle est décrite de la manière suivante : "run library module as a script". En réalité, cette phrase ne saurait suffire à traduire le potentiel de cette option. En effet, avec cette dernière, le package est enfin chargé de la manière escomptée. `__init__.py` et `__main__.py` sont automatiquement exécuté et pour chacun d’eux, `__name__` et `__package__` contiennent les valeurs attendues. Plus encore, nous n'avons eu recours à aucun artifice (un module supplémentaire dont le seul but étant l'`import` de notre main).

Conclusion
----------

Bien que nécessaire à la compréhension des imports, des structures et de la bonne exécution d’un projet, la notion de *package* reste mal comprise des développeurs python.

Nous pouvons regretter que le chapitre traitant des modules dans [le tutoriel officielle][pydoc/tuto/module] de python soit approximatif. Faute de ressources complètes et fiables à ce propos, les différents cours tant francophones qu'anglophones ne font guère mieux.

Cet article a pour objectif de venir combler ces lacunes. Il a montré le rôle essentiel de la variable magique `__package__`, tout en soulignant l’importance de la manière dont est exécuté un projet. Finalement, au travers de l'ensemble des cas pratiques, cet article a démontré que l'option en ligne de commande `-m` était la meilleure solution pour lancer un projet.

[pydoc/tuto/module]: https://docs.python.org/3/tutorial/modules.html
[goff11]: https://user.oc-static.com/ftp/livre/python/apprenez_a_programmer_en_python.pdf
