Import relatif vs import absolu, démystifions les modules python
================================================================

Dans cet article nous étudions les modules en python avec un regard poussé sur
la notion de package. Nous étudions la manière de définir des modules et la
manière de les exécuter de sorte à créer des arborescences cohérentes et à
prévenir certains problèmes, notamment les problèmes liés aux import relatifs.

Cet article part du principe que vous avez déjà utilisé `import` et que vous
avez déjà écrit vos propres modules. Si vous pensez avoir besoin d'une remise à
niveau, nous vous conseillons de relire les deux chapitres "Pas à pas vers la
modularité" dans l'introduction du livre "Apprenez à programmer en Python" de
Vincent le Goff. Le livre est consultable en ligne [ici](goff11).


Module ou package ?
-------------------

En python, on appelle "module", un ficher ou un dossier qui est *importable*,
c'est-à-dire un fichier ou un dossier qu'il est possible d'`import`. Il est
possible d'importer un fichier lorsque ce fichier est accessible depuis le
`sys.path`, que le nom de celui-ci se termine avec l'extension `.py` et que le
contenu respecte la syntaxe de python.  Il est possible d'importer un dossier
lorsque ce dossier est accessible depuis le `sys.path`, qu'il contient un
fichier appelé `__init__.py` et que ce fichier respecte de syntaxe de python.





[goff11](https://user.oc-static.com/ftp/livre/python/apprenez_a_programmer_en_python.pdf)
