# Programmer en Scala 3 : Les prérequis

## Qu'est-ce que Scala ?

Scala, dont le nom veut dire "Scalable language" (Langage qui s'adapte à la taille du projet), est un langage orienté objet et fonctionnel créé par Martin Odersky.

Scala est un langage dit "general purpose", qui n'est pas centré sur un domaine précis. Toutefois, le langage brille particulièrement dans deux domaines:
- Systèmes concurrents et distribués, c'est à dire des systèmes se coordonant et se répartissant les tâches. (LinkedIn, Twitter, Netflix...)
- Traitement des données, Big Data. (Netflix, Disney+, AdColony...)

Les entreprises citées ci-dessus utilisent Scala pour plusieurs raisons dont:
- La polyvalence: le langage est très versatile et peut-être adapté au domaine que l'on souhaite
- La maintenabilité: le langage dispose de nombreuses fonctionnalités permettant de rendre son code durable et d'éviter au maximum les bugs
- Les performances: l'implémentation principale du langage, la JVM (que nous aborderons plus tard), a été conçue pour être très performante et adaptée aux programmes gérant de larges volumes de données/d'utilisateurs.

## Installation

Maintenant que nous avons brièvement présenté le langage, nous allons commencer la pratique.

*Note: La dernière version de Scala à la date où cet article est écrit est la 3.1.3. La plupart des exemples seront cependant utilisables tels quels en Scala 3.0 ou supérieur.*

Scala peut être installé sur n'importe quel système UNIX (Mac OS, Linux) et également sur Windows. Pour ce tutoriel et les futurs cours, nous utiliserons [Scala CLI](https://scala-cli.virtuslab.org), un outil pour facilement créer de petits programmes en Scala. En voici la [page d'installation](https://scala-cli.virtuslab.org/install).

## Lancement d'un premier programme en Scala

Une fois Scala CLI installé nous pouvons écrire notre premier programme. Commençons d'abord par créer un premier fichier que nous appellerons `hello.sc`. Le nom n'a pas d'importance mais si vous en choisissez un autre, pensez à remplacer également le nom du fichier utilisé dans les commandes énoncées plus tard.

Ouvrons le fichier et commençons avec un classique de la programmation: un "Hello World". Il s'agit d'un programme qui consiste juste à afficher la phrase "Hello World" ("Bonjour Monde") une fois lancé. Voici à quoi ressemble un tel programme en Scala 3:
```scala
println("Hello World")
```

*Note: `println` sert à afficher du texte dans la console puis retourner à la ligne.*

Ouvrez maintenant votre terminal à l'endroit où vous avez créé le fichier et entrez la commande suivante:

```sh
scala-cli hello.sc
```

Vous obtiendrez la sortie suivante:
```
Hello World
```

Félicitations, vous venez de lancer votre premier programme écrit en Scala !


## Conclusion

Nous avons vu dans ce chapitre les différents prérequis pour programmer en Scala après en avoir fait une présentation. Nous aborderons la prochaine fois les bases du langage.

Voici quelques liens utiles:
- [Site officiel du langage](https://scala-lang.org/)
- [Site de Scala CLI](https://scala-cli.virtuslab.org/)

*Suite : [Types et variables](./programmer-en-scala-3-types-et-variables)*