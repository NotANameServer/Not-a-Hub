---
layout: post
author: Julien Castiaux
date: 2023-04-07
last_update: 2023-05-28
title: "Comment structurer un projet Python"
---


* [Introduction](#introduction)
* [Mise en place du squelette du projet](#mise-en-place-du-squelette-du-projet)
* [Adaptation d'un programme existant](#adaptation-dun-programme-existant)
* [Isolation dans un environnement virtuel](#isolation-dans-un-environnement-virtuel)
* [Ajout de tests automatiques](#ajout-de-tests-automatiques)
* [Création d'une archive installable](#création-dune-archive-installable)
* [Configuration de VSCode](#configuration-de-vscode)
* [Configuration de PyCharm](#configuration-de-pycharm)
* [Choix des technologies](#choix-des-technologies)
* [Références](#références)

## Introduction

La plupart des cours que nous recommandons[^1] [^2] [^3] pour apprendre Python se concentrent sur l'enseignement de la programmation *au travers* de Python et se réservent bien d'enseigner comment *structurer et déployer* une application ou une bibliothèque écrite en Python.

Il existe en ligne une pléthore de tutoriels[^4] [^5] [^6] sur comment structurer son projet et comment le déployer. Cependant l'éco-système de Python a tellement évolué depuis 2018 sur tout ce qui est relatif au *packaging* qu'il a rendu bon nombre de ces tutoriels caduques[^7] [^8].

Cet article a donc pour objectif de guider les lecteurs vers une structure de projet adaptée aux usages de 2023. Parmi les usages communs, nous avons retenu pour cet article : comment [tester son application] et comment [partager son programme avec autrui].

Cet article s'appuie sur les recommandations de la [PyPA] (*Python Packaging Autority*) qui est en charge de *spécifier*, *maintenir* et *documenter* toute une série de pratiques et d'outils relatifs au partage des applications et des bibliothèques développées en Python. À défaut de recommandations de la PyPA, nous utiliserons les pratiques et les outils les plus répandus. Tous les partis pris par ce document sont discutés dans le [dernier chapitre].

[tester son application]: #ajout-de-tests-automatiques
[partager son programme avec autrui]: #création-dune-archive-installable
[PyPA]: https://www.pypa.io/en/latest/
[dernier chapitre]: #choix-des-technologies

## Mise en place du squelette du projet

*Vous avez toujours besoin de cette étape.*

Commencez par créer un dossier nommé selon le nom de votre projet, dans cet exemple nous allons nommer ce dossier `tartempion`. Déplacez vous ensuite à l'intérieur de ce dossier et créez les fichiers suivants:

* `README.md`
* `LICENSE.txt`

Le fichier `README.md` est le fichier qui décrit votre logiciel, comment l'installer, comment l'utiliser et pointe des ressources pour aller plus loin. À minima, ce fichier reprend le nom du projet ainsi qu'une courte description:

    tartempion
    ==========

    Un projet vide juste pour montrer comment structurer un projet en python.

Le fichier `LICENSE.txt` est un fichier à vocation légale, il explique qui a le droit de modifier et/ou d'utiliser votre projet. Par défaut, en l'absence d'un tel fichier, vous êtes le seul détenteur du logiciel, seul vous avez le droit de le modifier, de l'utiliser et de le commercialiser. Pour qu'il n'y ait aucune ambiguïté, vous pouvez rappeler votre droit d'auteur en écrivant ceci dans le fichier:

    Copyright (c) votre nom et prénom

Si vous souhaitez rendre votre projet open-source, avec plus ou moins de conditions, vous pouvez copier/coller le texte d'une licence existante. Vous trouverez une liste de licences communes sur le site <https://choosealicense.com/>.

Votre projet devrait ressembler à ceci :

    tartempion/
      LICENSE.txt
      README.md

En étant dans le dossier de votre projet, donc en étant à l'intérieur du dossier `tartempion`, créez un second dossier du même nom, c'est à dire créez à nouveau un dossier `tartempion`. Créez ensuite dans ce nouveau dossier, les deux fichiers suivants :

* `__init__.py`
* `__main__.py`

Ce second dossier contiendra votre programme, c'est-à-dire tous vos fichiers python (à l'exception des tests automatiques). Pour différencier les deux dossiers, nous appellerons le premier dossier (celui qui contient le fichier `README.md`) la *racine du projet* (*project root*).

Le fichier `__init__.py` fait en sorte que le dossier soit reconnu comme un *package* par python, c'est-à-dire comme un dossier contenant des fichiers python (appellés *modules*). Il sera automatiquement exécuté à chaque fois que le projet sera importé et/ou exécuté.

Le fichier `__main__.py` est le point d'entrée de votre application, il contient le code qui sera exécuté (après `__init__.py`) lorsque vous lancerez votre programme. Ce fichier n'est pas nécessaire si vous comptez développer une bibliothèque de fonctions et non pas un programme exécutable.

Au terme de cette étape, votre projet devrait ressembler à ceci:

    tartempion/
      tartempion/
        __init__.py
        __main__.py
      LICENSE.txt
      README.md

Si vous utilisez un logiciel de contrôle de version (comme *git*), vous pouvez d'ores et déjà initialiser votre logiciel avec les fichiers existants. Les utilisateurs de *git* peuvent donc taper la commande `git init` en étant à l'intérieur de la racine du projet, c'est-à-dire à l'intérieur du premier dossier `tartempion`.

### Lancement du projet

Pour vérifier que cette structure minimale fonctionne correctement, vous pouvez écrire ceci dans le fichier `__init__.py` :

```py
print("Dans __init__.py")
print("  file:", __file__)
print("  name:", __name__)
print("  package:", __package__)
```

et ceci dans le fichier `__main__.py` :

```py
print("Dans __main__.py")
print("  file:", __file__)
print("  name:", __name__)
print("  package:", __package__)
```

Ouvrez alors un terminal à la *racine du projet* (le premier dossier `tartempion`) et exécutez la commande suivante pour constater qu'il est possible d'*importer* votre projet comme une *bibliothèque de fonctions* (sur windows, remplacez `python3` par `py`) :

    python3 -c "import tartempion"

La commande va ouvrir un interpréteur python, exécuter l'instruction `import tartempion` et quitter. Le résultat de cette commande devrait être:

    Dans __init__.py
      file: __init__.py
      name: tartempion
      package: tartempion

Exécutez ensuite la commande suivante pour constater qu'il est possible d'*exécuter* votre projet comme un *programme* (sur windows, remplacez `python3` par `py`) :

    python3 -m tartempion

La commande va charger le module dans un interpréteur python et l'exécuter. Le résultat de cette commande devrait être :

    Dans __init__.py
      file: __init__.py
      name: tartempion
      package: tartempion
    Dans __main__.py
      file: __main__.py
      name: __main__
      package: tartempion

Une fois que vous avez vérifié que votre programme fonctionne bien, vous pouvez vider les deux fichiers, c'est-à-dire retirer tous les `print`. Ne supprimez pas les fichiers.

## Adaptation d'un programme existant

*Vous avez besoin de cette étape si vous avez déjà commencé à faire un programme mais qu'il n'était pas correctement structuré.*

Vous avez deux dossiers, un dossier mal structuré qui contient votre ancien programme et un dossier bien structuré (mais presque vide) que vous avez créé en suivant les instructions précédentes. Nous appellerons ici ces dossiers `old_tartempion` et `new_tartempion`.

### Structure de l'ancien projet

Votre dossier `old_tartempion` doit certainement avoir une structure similaire à la structure suivante :

    old_tartempion/
      tartempion.py
      tartes/
        tarte.py
        tarte_cerise.py
        tarte_pomme.py

Du point de vue des imports, le contenu de vos fichiers doit certainement ressembler à quelque chose dans le genre de :

```py
# tartempion.py
from tartes.tarte_cerise import TarteCerise

tarte = TarteCerise()
print(tarte)
```

```py
# tarte.py
class Tarte:
    ...
```

```py
# tarte_cerise.py
from . import tarte

class TarteCerise(tarte.Tarte):
    ...
```

```py
# tarte_pomme.py
from .tarte import Tarte

class TartePomme(Tarte):
    ...
```

Vous devez certainement lancer votre programme soit en faisant `python3 tartempion.py` depuis votre terminal soit en cliquant sur le bouton "run" tout en étant sur le fichier `tartempion.py` dans votre IDE.

Si la structure de votre projet actuel ne ressemble pas à celle décrite ici ou bien si vous n'êtes pas sûr alors venez nous demander de l'aide sur Discord. Faites bien attention à nous expliquer comment vos fichiers sont structurés, comment vous faites vos imports et surtout comment vous lancez votre programme.

### Structure du nouveau projet

Après adaptation, la structure de votre projet devrait plutôt ressembler à ceci:

    new_tartempion/
      tartempion/
        __init__.py
        __main__.py
        tartes/
            __init__.py
            tarte.py
            tarte_cerise.py
            tarte_pomme.py
      LICENSE.txt
      README.md

Le fichier `tartempions.py` est devenu le fichier `__main__.py` qui se trouve à l'intérieur du *package* `tartempion`. Le *package* `tartes` a été déplacé à l'intérieur du *package* `tartempion`. Deux nouveaux fichiers (vides) `__init__.py` ont été rajoutés, l'un dans le dossier `tartempion` et l'autre dans le dossier `tartes`.

Niveau imports dans vos fichiers, vous devez corriger toutes vos lignes où vous avez importé des modules de votre projet à l'aide d'un import absolu. Un import est absolu lorsqu'il ne commence pas par un point.

Exemple d'imports absolus (ne commencent pas par un point) :

```py
import tartes
from tartes import tarte_cerise
import tartes.tarte_cerise
from tartes.tarte_cerise import TarteCerise
```

Exemple d'imports relatifs (commencent par un point) :

```py
from . import tarte
from .tarte import TarteCerise
```

Vous pouvez en apprendre plus sur les différences entre imports absolus et imports relatifs dans [cet autre article](relatif-vs-absolu-demystifions-les-imports-python)

En reprenant la structure de `old_tartempion` en exemple ici, le seul import que vous devez corriger est celui qui provient du fichier `tartempion.py` (renommé `__main__.py` dans la nouvelle structure). Dans votre propre projet, vous devrez certainement en corriger plus.

```py
# tartempion.py
from .tartes.tarte_cerise import TarteCerise
#    ^ ya un point en plus ici

tarte = TarteCerise()
print(tarte)
```

Pour lancer votre projet depuis votre terminal, vous devez maintenant faire `python3 -m tartempion` (sur Windows, remplacez `python3` par `py`) en étant dans le dossier `new_tartempion`.

Si vous aviez l'habitude d'exécuter votre code depuis votre IDE, les étapes pour le configurer pour qu'il utilise aussi `-m` sont expliquées plus bas.

## Isolation dans un environnement virtuel

*Vous avez besoin de cette étape si vous voulez installer avec pip des applications, des outils ou bibliothèques supplémentaires comme `pylint`, `requests` ou `pygame`.*

### Introduction

Ouvrez un terminal et entrez la commande `python3 -m pip list` (sur windows, remplacez `python3` par `py`). Le résultat de cette commande devrait lister toutes les bibliothèques supplémentaires qui sont installées pour Python sur votre machine.

Si vous êtes sur Linux ou MacOS, cette liste devrait déjà être bien remplie comme les deux systèmes utilisent Python en interne pour toute une série de routines systèmes. Si vous êtes sur Windows, cette liste devrait être vide ou presque.

Vous pouvez répéter la commande avec l'option `--user` pour lister les bibliothèques qui sont installées pour l'utilisateur actuel, la liste devrait être (beaucoup) plus courte.

Les paquets qui sont installés au niveau du système sont les paquets que le système gère lui-même, par exemple avec `apt` sur Ubuntu, vous ne devriez jamais y toucher vous-même, ni installer de nouvelles bibliothèques, ni en supprimer. Les paquets installées pour l'utilisateur actuel sont des outils dont vous avez besoin dans votre vie de tous les jours, par exemple pour faire du scripting.

Lorsque vous développez un nouveau projet, il est important d'isoler les bibliothèques utilisées pour ce projet du reste des bibliothèques de votre système. Vous ne voudriez pas écraser une bibliothèque utilisée par votre système par une version trop récente/ancienne dans votre projet et ainsi compromettre le bon fonctionnement de votre système.

En Python, pour isoler les bibliothèques utilisées d'un endroit à autre, nous utilisons des environnements virtuels.

### Créer un environnement virtuel

Ouvrez un terminal à la racine de votre projet et entrez la commande `python3 -m venv .venv` (remplacez `python3` par `py` sur Windows). La commande va créer un nouvel environnement virtuel dans le dossier `.venv` à la racine de votre projet.

Une fois l'environnement créé, vous pouvez vérifier qu'il fonctionne bien en ouvrant l'interpréteur Python lié à ce nouvel environnement. Sur MacOS/Linux, vous pouvez exécuter la commande `./.venv/bin/python` dans votre terminal, sur Windows vous pouvez faire `.\.venv\Scripts\python`, dans les deux cas l'exécution de cette commande devrait ouvrir l'interpréteur que vous pouvez fermer en appelant la fonction `exit()`.

Vous pouvez aussi lister les modules supplémentaires qui sont installés dans cet environnement virtuel en faisant `./.venv/bin/pip list` (`.\.venv\Scripts\` sur Windows), vous devriez constater que seul `pip` (et peut-être aussi `setuptools`) est installé, malgré la possible présence de nombreux autres paquets installés sur votre système.

### Utiliser un environnement virtuel

Pour utiliser votre environnement virtuel, vous n'avez donc qu'à ouvrir un terminal à la racine de votre projet et utiliser le python et le pip qui se trouvent dans le dossier `.venv/bin/` (`.\.venv\Scripts\pip list` sur Windows).

Pour installer une bibliothèque, vous pouvez alors juste faire `./.venv/bin/pip install` suivi du nom des bibliothèques que vous voulez installer. Dans cet exemple, nous allons installer la bibliothèque `requests` qui permet de faire des requêtes sur internet en HTTP et vérifier qu'elle fonctionne. Vous faites `./.venv/bin/pip install requests` et vous ouvrez ensuite un interpréteur python avec `./.venv/bin/python` dans lequel vous pouvez entrer les instructions suivantes:

    Python 3.10.6 (main, Mar 10 2023, 10:55:28) [GCC 11.3.0] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    >>> import requests
    >>> print(requests.__version__)
    2.28.2
    >>> exit()

### Configurer son terminal pour ne pas devoir tout le temps écrire `./.venv/bin`

Vous constatez donc qu'il est nécessaire de toujours donner le chemin vers le python et le pip qui se trouvent dans votre environnement virtuel. Lorsque vous comptez travailler toute la journée sur un même projet, devoir répéter ces instructions peut être fastidieux. Les développeurs de Python ont prévu le coup, il est possible de reconfigurer son terminal pour remplacer `python` et `pip` de sorte à utiliser ceux de l'environnement virtuel plutôt que ceux du système. Précision importante, ce changement n'aura d'impact qu'à l'intérieur du terminal actuellement ouvert, le reste du système continuera bien d'utiliser le `python` et le `pip` installés au niveau du système (ceci inclut donc aussi les IDE).

Pour reconfigurer son terminal, ou comme nous disons dans le jargon *activer son environnement virtuel*, vous pouvez *sourcer* le script `activate` qui se trouve à côté de `python` et `pip` dans le dossier `bin` de votre environnement virtuel: `source ./.venv/bin/activate` (sur Windows, pas besoin de `source`, appelez `.\.venv\Scripts\activate` directement à la place).

Pour vérifier que la reconfiguration (l'activation) s'est bien déroulée, vous pouvez exécuter la commande `pip --version` (sans donner le chemin complet) et vérifier que le `pip` utilisé est celui de votre environnement virtuel.

    $ pip --version
    pip 22.0.2 from /tmp/.venv/lib/python3.10/site-packages/pip (python 3.10)

Pour faire la reconfiguration inverse, réutiliser les `python` et `pip` du système, ou comme nous disons dans le jargon *désactiver son environnement virtuel*, vous pouvez simplement exécuter la commande `deactivate`.

[venv]: https://docs.python.org/3/library/venv.html

## Ajout de tests automatiques

*Vous avez besoin de cette étape lorsque vous comptez vérifier le fonctionnement de votre application à l'aide de tests automatiques.*

Ouvrez un terminal à la racine de votre projet et créez un nouveau dossier `tests`, dans ce dossier créez deux fichiers: `__init__.py` et `test_tartempion.py`. La structure de votre projet devrait donc ressembler à ceci :

    tartempion/
      tartempion/
        __init__.py
        __main__.py
      tests/
        __init__.py
        test_tartempion.py
      LICENSE.txt
      README.md

Vous pouvez laisser le fichier `__init__.py` vide, il sert uniquement à indiquer que le dossier est un *package* pour python. À l'intérieur du fichier `test_tartempion.py` vous pouvez écrire ceci :

```py
import unittest
import tartempion

class TartempionTest(unittest.TestCase):
    def test_tartempion_loaded(self):
        self.assertTrue(tartempion)
```

Une fois le test écrit, assurez vous de vous positionner à la racine de votre projet dans votre terminal. Vous pouvez ensuite lancer les tests avec la commande `python3 -m unittest` (utilisez `py -m unittest` sur Windows, pensez à passer par votre environnement virtuel si vous en avez un). Vous devriez avoir un résultat comme suit:

    .
    ----------------------------------------------------------------------
    Ran 1 test in 0.000s

    OK

Chaque `.` sur la première ligne représente un test qui est passé, les tests échoués apparaissent avec un `!`. Vous pouvez aussi utiliser l'option `-v` si vous voulez plutôt énumérer le nom de tests un à un :

    test_tartempion (tests.test_tartempion.TestTartempion) ... ok

    ----------------------------------------------------------------------
    Ran 1 test in 0.000s

    OK

Le fonctionnement général d'[unittest] est qu'il chargera de lui-même tous les fichiers à l'intérieur du dossier `tests` qui commencent par `test_`. À l'intérieur de ces modules python, il exécutera de lui-même toutes les méthodes qui commencent par `test_` dans les classes qui héritent de `TestCase`.

Vous pouvez ajouter autant de modules de tests et de classes que vous voulez. Il peut être judicieux de définir les tests dans des modules différents en fonction de la partie du code qu'ils testent.

Il n'y a pas beaucoup de documentation disponible dans la sphère francophone sur le testing en Python. Si vous avez des questions à ce propos, n'hésitez pas à poser vos questions sur Discord.

[unittest]: https://docs.python.org/3/library/unittest.html

## Création d'une archive installable

*Vous avez besoin de cette étape si vous comptez partager votre programme à une tierce personne, si vous comptez héberger votre programme sur un serveur, ou bien si vous comptez rendre votre bibliothèque installable avec pip.*

Assurez-vous d'avoir toutes les dépendances suivantes installées sur votre système: [build], [setuptools], [wheel]. Sur les systèmes Linux dérivés de Debian/Ubuntu, vous pouvez utiliser votre package-manager: `apt install python3-build python3-setuptools python3-wheel`. Pour Windows, vous pouvez directement utiliser `pip` et installer ces bibliothèques au niveau de votre utilisateur (en dehors d'un environnement virtuel donc): `py -m pip install --user --upgrade build pip setuptools wheel`

Assurez-vous ensuite que ces libs sont également installées au niveau de votre environnement virtuel (si vous en utilisez un): `.venv/bin/pip install --upgrade build pip setuptools wheel` (`.venv\Scripts\pip` sur Windows, ou bien activez votre environnement virtuel).

### Déclaration du projet

Une fois les dépendances installées, vous pouvez définir les méta-données relatives à votre projet dans un nouveau fichier `pyproject.toml` que vous créez à la racine de votre projet. Nous vous proposons le fichier suivant, à titre d'exemple :

```toml
[project]
name = "tartempion_NaN"
version = "0.0.1"
description = "Une courte description sur une ligne"
readme = "README.md"
license = { file = "LICENSE.txt" }
authors = [
    { name = "Bob", email = "bob@example.com" },
]

classifiers = [
  "Private :: Do Not Upload",
]

# Exemple de dépendances
dependencies = [
    "pygame",
    "requests",
]

[build-system]
requires = ["setuptools>=61.0", "wheel"]
build-backend = "setuptools.build_meta"
```

Le fichier utilise un format relativement nouveau, le [TOML], il s'agit d'un format de fichier adapté aux fichiers de configuration.

La première partie du fichier, `[project]`, défini l'ensemble des méta-données relatives à votre projet. Il existe en tout plus d'une vingtaine de méta-données différentes, nous avons décidé de ne garder que les plus essentielles d'entre elles ici. La liste complète est définie dans la PEP [621]. Pensez à changer les valeurs pour le nom, la description et les auteurs. Pensez aussi à déclarer vos dépendances, si vous en avez, pour qu'elles soient automatiquement installées avec votre projet.

**Important**, le champ `name` dans ce fichier n'est pas obligatoirement le même que le nom de votre dossier. Il est d'ailleurs conseillé d'ajouter votre pseudo ou un autre élément unique à la fin pour vous assurer qu'il sera unique sur internet. Dans cet exemple nous avons ajouté `_NaN` pour "Not a Name", ce blog.

Contrairement à une croyance populaire, reprise par beaucoup de tutoriels erronés en ligne, les dépendances sont bien à inscrire dans le champ `dependencies` du `pyproject.toml` et non pas dans un fichier `requirements.txt`. Vous pouvez lire la discussion [install_requires vs requirements files] dans la documentation officielle pour en apprendre plus.

La liste associée au champ `classfiers` permet de catégoriser votre logiciel en fonction de l'audience visée, le sujet générale de votre logiciel et d'autres informations. Ce champ n'est pas essentiel. Si vous comptez héberger votre logiciel sur <pypi.org>, vous devrez retirer la ligne `"Private :: Do Not Upload",`.

La seconde partie du fichier, `[build-system]`, décrit quels outils seront utilisés pour créer les archives pour votre projet. Cette partie est obligatoire mais vous pouvez vous contenter de garder celle de l'exemple.

### Construction de l'archive

Une fois le fichier `pyproject.toml` complété, vous pouvez utiliser [build] pour créer une archive de votre fichier. Placez-vous à la racine de votre projet et lancer la commande `.venv/bin/pyproject-build` (`.venv\Scripts\pyproject-build` sur Windows). La commande est très verbeuse, parmi toutes les lignes affichées vous devriez voir celles-ci:

    * Creating venv isolated environment...
    * Installing packages in isolated environment... (setuptools)
    * Getting build dependencies for sdist...
    * Building sdist...
    * Building wheel from sdist
    * Creating venv isolated environment...
    * Installing packages in isolated environment... (setuptools)
    * Getting build dependencies for wheel...
    * Installing packages in isolated environment... (wheel)
    * Building wheel...
    Successfully built tartempion-0.0.1.tar.gz and tartempion-0.0.1-py3-none-any.whl

Le programme aura créé plusieurs fichiers et dossiers à la racine de votre projet, parmi ces dossiers un dossier `dist/` qui contient les deux archives créées : `tartempion-0.0.1.tar.gz` (`.zip` sur Windows) et `tartempion-0.0.1-py3-none-any.whl`.

La première archive au format `.tar.gz` ou `.zip` est une *distribution source*, elle est principalement à destination des développeurs. La seconde archive au format `.whl` est une *distribution wheel* (sur roulette), elle est principalement à destination des utilisateurs.

Chacune de ces deux archives est installable via [pip]. Vous pouvez donc les partagez autours de vous (préférez partager la wheel) et vos utilisateurs pourront l'installer sur leur propre machine.

[TOML]: https://toml.io/fr/
[621]: https://packaging.python.org/en/latest/specifications/declaring-project-metadata/#declaring-project-metadata
[install_requires vs requirements files]: https://packaging.python.org/en/latest/discussions/install-requires-vs-requirements/
[build]: https://pypa-build.readthedocs.io/en/stable/index.html
[setuptools]: https://setuptools.pypa.io/en/latest/
[wheel]: https://wheel.readthedocs.io/en/latest/
[pip]: https://pip.pypa.io/en/stable/

## Configuration de VSCode

*Vous avez besoin de cette étape si vous voulez que VSCode arrête de lever des erreurs pour des problèmes d'import et/ou pouvoir lancer votre projet directement depuis la console de VSCode.*

Installez l'extension Python de Microsoft pour VSCode, cette extension ajoute le nécessaire pour exécuter et debugger du code python directement depuis VSCode.

Ouvrez une nouvelle fenêtre dans VSCode (File > New Window), ouvrez le dossier qui contient votre projet. Une fois votre projet ouvert, assurez-vous que votre environnement virtuel a été chargé en regardant le coin inférieur droit, vérifiez de bien lire `('.venv': venv)` précédé de la version de Python avec laquelle vous aviez créé votre projet.

Pour lancer votre module directement depuis VSCode et profiter du debugger intégrer, ajoutez une nouvelle configuration pour le lancement de votre programme (Run > Add Configuration). VSCode vous proposera une configuration parmi d'autres, sélectionnez "**Module** Debug a Python module by invoking it '-m'", il devrait être le second dans la liste. VSCode vous demande ensuite de donner le nom de votre module, nous entrons `tartempion` dans notre cas, vous inscrivez le nom de votre module. Une fois la nouvelle configuration ajoutée, il vous reste à lancer le debugger avec F5 (ou bien Run > Start Debugging).

## Configuration de PyCharm

*Vous avez besoin de cette étape si vous voulez que PyCharm arrête de lever des erreurs pour des problèmes d'import et/ou pouvoir lancer votre projet directement depuis la console de PyCharm.*

<!-- Lazor: arrêtez de casser les couilles et utilisez Sublime Text avec un terminal. -->

## Choix des technologies

Tout au long de ce document, il n'a jamais été présenté qu'une seule approche, un seul choix. Il s'agit d'un choix assumé par la nécessité de dissimuler aux débutants toute la complexité réelle qui se cache derrière le *packaging* en Python. Dans cette section, nous présentons les alternatives connues pour chacune de nos décisions et nous justifions nos choix.

### Squelette du projet

Il existe deux manières de structurer un projet python[^9], ce document a présenté la structure dite "à plat" (*flat-layout*) mais certains projets préfèrent la structure dite "imbriquée" (*src-layout* ou *nested-layout*).

Structure à plat:

    tartempion/
      tartempion/
        __init__.py
        __main__.py
      tests/
        test_tartempion.py
      README.md

Structure imbriquée:

    tartempion/
      src/
        tartempion/
          __init__.py
          __main__.py
      tests/
        test_tartempion.py
      README.md

Nous avons préféré présenter la structure à plat car elle est plus simple. La structure imbriquée n'est utile que lorsqu'un même projet se décline en plusieurs modules dépendants les uns des autres qui ne doivent pas partager un même *namespace*. Plutôt rare comme cas de figure.

Un autre avantage de la structure à plat est de pouvoir lancer le programme et les tests automatiques depuis la racine du projet sans installation. Avec la structure imbriquée, il est obligatoire de recourir à un paquet installé en mode éditable dans l'environnement virtuel courant pour lancer et tester l'application. Le revers est qu'en cas d'erreur dans la construction d'une archive, dans le cas où les modules python n'ont pas été correctement inclus, ces modules *pourraient* apparaître comme accessibles (parce que se trouvant dans le working-directory) sans réellement l'être (parce que non inclus dans le package)[^10].

### Format du README

Il existe plusieurs formats de fichiers assez répandus pour la rédaction des fichiers README. Les plus communs sont le format texte, le format Markdown et le format reStructuredText. Sur <pypi.org>, le format utilisé par défaut est reStructuredText, cependant lorsqu'un projet est créé depuis [Github], le fichier README sera au format Markdown.

Il y a une grosse tendance à favoriser le Markdown pour l'écriture des fichiers README et cette tendance n'est pas spécifique à Python. Puisque le Markdown est également supporté sur <pypi.org> (via la directive `long_description_content_type=text/markdown`) et que le Markdown est généralement considéré comme plus simple à utiliser que le reStructuredText, nous avons choisi le format Markdown pour le README.

[Github]: https://github.com

### Environnement Virtuel

Il existe plusieurs logiciels capables de créer et de gérer des environnements virtuels parmi lesquels [venv], [virtualenv] et [pyenv-virtualenv]. Il existe aussi plusieurs logiciels de gestion de projet python "tout-en-un" qui intègrent un environnement virtuel par défaut comme [hatch], [pdm] ou [poetry].

Parmi tous ces outil, [venv] est disponible de base et était recommandé par la PyPA sur sa page des outils recommandés[^11] au moment de la rédaction de ce document. Le nom du dossier: `.venv` vient d'ailleurs de sa page de documentation:

> un nom habituel pour ce dossier cible est `.venv`

[venv]: https://docs.python.org/3/library/venv.html
[virtualenv]: https://virtualenv.pypa.io/en/stable/index.html
[pyenv-virtualenv]: https://github.com/pyenv/pyenv-virtualenv
[hatch]: https://hatch.pypa.io/latest/
[pdm]: https://pdm.fming.dev/
[poetry]: https://python-poetry.org/
[setuptools]: https://setuptools.readthedocs.io/en/latest/

### Tests automatiques

Il existe plusieurs bibliothèques pour écrire et lancer des tests unitaires sur Python. On peut citer [unittest], [pytest], [nose], [ward] et [hammett]. Parmi toutes ces bibliothèques, les deux plus répandues sont [unittest] et [pytest], ensemble elles dominent l'écosystème Python. Nous avons décidé de présenter [unittest] dans ce tutoriel car elle reste (à une très courte majorité) la bibliothèque la plus utilisée et parce qu'elle est disponible directement dans la bibliothèque standard.

[unittest]: https://docs.python.org/3/library/unittest.html
[pytest]: https://docs.pytest.org
[nose]: https://nose.readthedocs.io/en/latest/
[ward]: https://ward.readthedocs.io/en/latest/
[hammett]: https://github.com/boxed/hammett

### Distribution

Depuis 2018, de nombreux systèmes ont vu le jour avec comme objectif de simplifier la gestion des projets en Python. On peut citer [poetry] avec son système de gestion de dépendances novateur, [pdm] et sa volonté de fournir un outil semblable à npm, [flit] et sa volonté de fournir un logiciel *simple* et pour finir [hatch] qui se veut être un outil tout-en-un et qui est de plus en plus répandu.

Il a existé une époque entre 2018 et 2021 pendant laquelle les mises à jour de [setuptools] stagnaient derrière ces nouveaux outils en terme d'adoption des standards (PEP-[517]/[518]/[621]) et pendant laquelle il nous aurait été difficile de suivre la PyPA dans ses recommandations. Heureusement, la [version 61] de [setuptools] (avril 2021) a ajouté le support pour la PEP-[621] (*Storing project metadata in pyproject.toml*) et il est depuis lors raisonnable d'utiliser setuptools à nouveau.

Nous avons utilisé setuptools dans cet article car il est compatible avec les PEP-[517]/[621], car il semble toujours être le seul outil capable de gérer des extensions écrites en C et car il est toujours le seul outil recommandé[^11] par la PyPA.

[flit]: https://flit.readthedocs.io/en/latest/
[hatch]: https://hatch.pypa.io/latest/
[pdm]: https://pdm.fming.dev/
[poetry]: https://python-poetry.org/
[setuptools]: https://setuptools.readthedocs.io/en/latest/
[version 61]: https://setuptools.pypa.io/en/latest/history.html#v61-0-0

[517]: https://peps.python.org/pep-0517/
[518]:https://peps.python.org/pep-0518/
[621]:https://packaging.python.org/en/latest/specifications/declaring-project-metadata/#declaring-project-metadata

### IDE

Parmi tous les éditeurs de texte et IDE disponibles pour Python, nous avons décidé de n'en documenter que deux, [VSCode] et [PyCharm]. Cette décision repose sur l'expérience des auteurs quant à la fréquence des questions relatives à l'utilisation combinées des environnements virtuels et des éditeurs de texte/IDE, expérience qui a été confirmée par plusieurs sondages.

Les débutants qui utilisent [VSCode] et [PyCharm] utilisent souvent le bouton "run" de leur IDE pour exécuter leur programme tandis que les débutants qui utilisent d'autres éditeurs (comme [Sublime Text]) semblent préférer passer par un terminal. Ceci s'ajoute au fait que les utilisateurs débutants de VSCode et PyCharm utilisent souvent un linter intégré à leur IDE contrairement aux utilisateurs débutants qui utilisent d'autres éditeurs.

Ces deux aspects, le bouton "run" et le linter, font qu'il est crucial de correctement configurer ces IDE pour qu'ils utilisent le bon environnement virtuel. Ne pas configurer d'environnement virtuel est une source commune d'erreur chez les débutants qui se plaignent soit qu'ils n'arrivent pas à installer de bibliothèques soit que leur IDE ne reconnaît pas la bibliothèque qu'ils viennent d'installer. Les deux affirmations sont en fait la conséquence du même problème, la bibliothèque n'a pas été installée dans le même environnement virtuel que celui utilisé dans l'IDE.

Il est rare de voir des questions de ce genre pour d'autres IDE, nous n'avons donc pas cherché à les documenter dans cet article. Nous ne les recommandons d'ailleurs pas plus que d'autres éditeur de texte / IDE.

[VSCode]: https://code.visualstudio.com/
[PyCharm]: https://www.jetbrains.com/pycharm/
[Sublime Text]: https://www.sublimetext.com/

## Références

[^1]: entwanne “Un Zeste de Python.” dans : Zeste de Savoir [En ligne]. [s.l.]&nbsp;: Zeste de Savoir, 2022. Disponible sur : <https://zestedesavoir.com/tutoriels/2514/un-zeste-de-python/> (consulté le 19 Mars 2023)
[^2]: Swinnen G. “Apprendre à programmer avec Python 3: Avec 60 pages d'exercices corrigés!” 3e ed. Paris, France : Eyrolles, 2012.
[^3]: Champagne J. “Python - cours ✔.” dans : YouTube [En ligne]. [s.l.]&nbsp;: YouTube, 2017. Disponible sur : <https://www.youtube.com/playlist?list=PLrSOXFDHBtfHg8fWBd7sKPxEmahwyVBkC> (consulté le 19 Mars 2023)
[^4]: Reitz K., Schlusser T. “The hitchhiker's guide to python: Best practices for development.” Sebastopol, CA : O'Reilly Media, Inc., 2016.
[^5]: Stratis K. “Python application layouts: A reference.” dans : Real Python [En ligne]. [s.l.]&nbsp;: Real Python, 2023. Disponible sur : <https://realpython.com/python-application-layouts/> (consulté le 19 Mars 2023)
[^6]: Le J. P. “Guide to python project structure and packaging.” dans : Medium [En ligne]. [s.l.]&nbsp;: MLearning.ai, 2023. Disponible sur : <https://medium.com/mlearning-ai/a-practical-guide-to-python-project-structure-and-packaging-90c7f7a04f95> (consulté le 19 Mars 2023)
[^7]: Setuptools “Setup.py discouraged” dans : Quickstart - setuptools 67.6.0 documentation [En ligne]. [s.l.]&nbsp;: [s.n.], [s.d.]. Disponible sur : <https://setuptools.pypa.io/en/stable/userguide/quickstart.html#setuppy-discouraged> (consulté le 19 Mars 2023)
[^8]: Ganssle P. “Why you shouldn't invoke setup.py directly.” dans : Paul Ganssle Blog [En ligne]. [s.l.]&nbsp;: [s.n.], 2021. Disponible sur : <https://blog.ganssle.io/articles/2021/10/setup-py-deprecated.html> (consulté le 19 Mars 2023)
[^9]: PyPA. “src layout vs flat layout.” dans : Python Packaging User Guide [En ligne]. [s.l.]&nbsp;: Python Packaging Autority, [s.d.]. Disponible sur : <https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/> (consulté le 19 Mars 2023)
[^10]: Cristian Mărieș I. “Packaging a python library - thoughts on packaging python libraries.” dans : ionel's codelog [En ligne]. [s.l.]&nbsp;: [s.n.], 2019. Disponible sur : <https://blog.ionelmc.ro/2014/05/25/python-packaging/> (consulté le 19 Mars 2023)
[^11]: PyPA. “Tool recommendations” dans : Python Packaging User Guide [En ligne]. [s.l.]&nbsp;: Python Packaging Autority, [s.d.]. Disponible sur : <https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/> (consulté le 19 Mars 2023)
