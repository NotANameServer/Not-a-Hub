---
layout: post
author: Raphaël Fromentin
date: 2023-05-14
last_update: 2023-05-21
title: "Programmer en Scala 3 : Mutabilité et boucles"
---

*Précédemment : [Booléens et conditions](./programmer-en-scala-3-booleens-et-conditions)*

## La mutabilité

Nous avons vu précédemment un moyen de stocker des valeurs sous un nom grâce aux variables. Cependant, nous n'avons jusqu'à présent qu'utilisé des variables dites "immuables", que l'on ne peut modifier. Vous avez peut-être tenté de faire la chose suivante :

```scala
val x = 1
x = 3
```

en obtenant une erreur :

```scala
-- [E052] Type Error: ----------------------------------------------------------
1 |x = 3
  |^^^^^
  |Reassignment to val x
  |
  | longer explanation available when compiling with `-explain`
```

Pourtant, pouvoir changer la valeur d'une variable est parfois bien utile ! Par exemple le nombre de vies de Mario change quand il meurt ou ramasse 100 pièces. Son état (grand, petit, Mario de feu...) change également.

Nous pouvons le faire en Scala en utilisant un autre mot clé : `var`. À l'instar de `val`, `var` permet de déclarer une variable à la différence près que la valeur de celle-ci peut-être changée.

```scala
var x = 1
x = 3

println(x) //3
```

Bien sûr, il est possible de combiner cette fonctionnalité avec les autres vues précédemment :

```scala
var vies = 1
vies = vies + 1 //+1 Up !

println(vies) //2
```

Le langage propose aussi quelques contractions comme :

| Contracté | Non-contracté |
| --------- | ------------- |
| `x += y`  | `x = x + y`   |
| `x -= y`  | `x = x - y`   |
| `x *= y`  | `x = x * y`   |
| `x /= y`  | `x = x / y`   |

Ainsi, le code ci-dessus peut s'abréger en :

```scala
var vies = 1
vies += 1

println(vies) //Toujours 2
```

Note : en Scala et dans d'autres langages, on préfère utiliser `val` par défaut pour ne pas se soucier d'un potentiel changement de valeur. On utilise alors `var` uniquement en cas de besoin.

## Les boucles

Reprenons l'exemple de notre jeu Mario. Nous avons parfois besoin d'exécuter une même action plusieurs fois :
- Tant qu'il reste du temps (et que Mario n'est pas mort), la partie continue.
- Quand Mario lance une boule de feu, celle-ci rebondit 3 fois.

En Scala, ces répétitions peuvent être décrites en utilisant les boucles. Il en existe deux types.

### La boucle while

En anglais, "while" peut se traduire en "alors que"/"tant que". La boucle `while` répète une action tant qu'une condition (représentée par un booléen) est satisfaite.

Elle se présente sous cette forme :

```scala
while condition do
  action
```

À titre d'exemple, faisons un petit décompte avec cette boucle :

```scala
var restant = 5
while restant > 0 do
  println(restant)
  restant -= 1

println("Fin du temps")
```

Sortie :

> 5\
> 4\
> 3\
> 2\
> 1\
> Fin du temps

`println(restant)`

### La boucle for

En anglais, "for" veut dire "pour"... Ça ne nous aide pas ! La boucle `for` peut-être utilisée pour répéter une action n fois. Le code suivant aura la même sortie que notre précédent exemple :

```scala
for restant <- 5 until 0 do
  println(restant)

println("Fin du temps")
```

Ici, `restant` va prendre à la première itération ("tour de boucle") la valeur 5, puis 4 pour la seconde itération, puis 3, ... jusqu'à 1. `5 until 0` veut dire "de 5 jusqu'à 0 exclus"

Dans le cas des boules de feu de Mario, nous pouvons écrire le code suivant :

```scala
//Le nombre de rebonds que peut faire une boule de feu
val rebonds = 3

for i <- 0 until rebonds do
  val rebondActuel = i + 1
  println(rebondActuel + " rebonds effectués")

println("La boule de feu a disparu")
```

Sortie :

> 1 rebonds effectués\
> 2 rebonds effectués\
> 3 rebonds effectués\
> La boule de feu a disparu

Note : en réalité, la boucle `for` en Scala est plus puissante que ça mais nous en reparlerons plus tard.

## Conclusion

Nous avons aujourd'hui vu comment répéter une action un certain nombre de fois ou selon une condition. Les boucles et les conditions sont à la base de la plupart des langages de programmation.

Nous verrons d'autres utilisations de la boucle `for` dans un prochain article ainsi qu'un projet pour mettre en œuvre les notions que nous avons précédemment vues.
