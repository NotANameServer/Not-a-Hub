---
layout: post
author: Raphaël Fromentin et TheElectronWill
date: 2022-09-16
last_update: 2023-05-21
title: "Programmer en Scala 3 : Booléens et conditions"
---

*Précédemment : [Types et variables](./programmer-en-scala-3-types-et-variables)*

## Les booléens

Nous avons vu précédemment comment stocker des valeurs et les manipuler en utilisant des opérations.

Dans le monde réel, un programme informatique a souvent besoin de vérifier si certaines propositions sont vraies ou
fausses. En reprenant l'exemple du jeu Mario Bros, le jeu doit vérifier si :

- Mario est vivant
- Mario possède encore des vies
- Mario a 100 pièces
- etc...

Une proposition est représentée par un type de données très courant en informatique : un booléen. Ce type ne peut
prendre que deux valeurs : "vrai" ou "faux".

En Scala, le type "booléen" s'écrit `Boolean`. Les valeurs "vrai" et "faux" s'écrivent respectivement `true` et `false`.

```scala
val x = true // "vrai"
val y = false // "faux"
```

### Opérations booléennes

À l'instar des types de données vus dans le cours précédent, les booléens possèdent des opérations qui leur sont propres dont trois principales, "non", "ou", "et".
On les appelle également des "opérations logiques".

*Note : ces opérations sont issues de l'[Algèbre de Boole](https://fr.wikipedia.org/wiki/Algèbre_de_Boole_(logique))
, souvent étudié en classe préparatoire ou en licence.*

#### Non

L'opération "non" est une opération qui retourne "vrai" si le booléen donné est "faux" et "faux" si le booléen est "
vrai". En pratique, on peut dire que cette opération "inverse" le booléen donné :

| Entrée | Résultat |
|--------|----------|
| Vrai   | Faux     |
| Faux   | Vrai     |

Le "non" en Scala s'écrit `!` avant la valeur à "inverser" :

```scala
!true // false
```

#### Ou

Le "ou" est une opération qui prend deux booléens pour renvoyer "vrai" si __au moins__ un des deux booléens l'est également. On parle aussi de "ou inclusif" :

| A    | B    | Résultat |
|------|------|----------|
| Vrai | Vrai | Vrai     |
| Vrai | Faux | Vrai     |
| Faux | Vrai | Vrai     |
| Faux | Faux | Faux     |

Cette opération s'écrit `||` en Scala :

```scala
true || false // true
```

#### Et

L'opération "et", à l'instar du "ou", prend deux booléens. Elle renvoie "vrai" si et seulement si les deux booléens sont
vrais :

| A    | B    | Résultat |
|------|------|----------|
| Vrai | Vrai | Vrai     |
| Vrai | Faux | Faux     |
| Faux | Vrai | Faux     |
| Faux | Faux | Faux     |

Cette opération s'écrit `&&`:

```scala
true && true // true
```

## Les comparaisons

En plus des opérations entre booléens citées ci-dessus, Scala met à disposition d'autres opérations qui retournent des booléens comme les comparaisons.

### Égalité

L'opérateur classique en Scala pour vérifier l'égalité entre deux valeurs est le double égal `==` :

```scala
1 == 2 // false
4 == 4 // vrai
"a" == "a" // vrai
```

Attention : comme vu dans le cours précédent, certaines valeurs, bien que similaires, n'ont pas le même type ! Elles ne
sont donc pas égales :

```scala
"1" == 1 // false
```

Comme la négation de l'égalité ("est différent de") est une opération très courante, Scala comme beaucoup d'autres
langages propose un opérateur dédié pour éviter de faire `!(a == b)`. Cet opérateur est noté `!=` :

```scala
!(1 == 2) //true
1 != 2 //true
```

### Inégalités

Pour les types numériques, Scala propose en opérateurs les inégalités de base :

```scala
1 < 3 //infériorité stricte
1 <= 3 //infériorité large (inférieur ou égal)
1 > 3 //supériorité stricte
1 >= 3 //supériorité large (supérieur ou égal)
```

*Attention : pour les inégalités larges, le "égal" doit être placé après le symbole `<` ou `>`. En Scala, l'opérateur `=>`
existe également et n'a aucun lien avec `>=`.*

## Les conditions

Comme indiqué dans l'introduction, les conditions permettent de faire certaines actions si une proposition, c'est-à-dire un
booléen, est vrai ou faux.

Par exemple, __si__ Mario est mort, __alors__ il faut lui soustraire une vie. __Si__ Mario a encore une vie __alors__ on
le fait recommencer le niveau __sinon__, c'est un Game Over.

### Si ... alors

À l'instar de la plupart des langages de programmation, Scala propose un moyen simple de définir une condition, en
utilisant les mots-clés `if` (si) et `then` (alors):

```scala
if true then
  println("hello")

if false then
  println("world")
```

Sortie:

> hello

Seul le `println("hello")` a été exécuté car la proposition testée est vraie (`true`).

La valeur passée entre le `if` et le `then` est tout simplement un booléen comme vu ci-dessus. Toute opération/variable
produisant un booléen est donc utilisable !

#### Indentation

Notez dans cet exemple ainsi que le précédent les deux espaces avant le `println` :

```scala
val pieces = 100

//Dans le jeu Mario Bros, Mario gagne une vie toutes les 100 pièces.
if pieces == 100 then
  println("+1Up")
  println("Félicitations")
```

Ces deux espaces, appelés "indentation" permettent d'indiquer que ces deux lignes sont dans la condition et pas en dehors :

```scala
val pieces = 100

//Dans le jeu Mario Bros, Mario gagne une vie toutes les 100 pièces.
if pieces == 100 then
  println("+1Up")
println("Félicitations")
```

Dans ce nouvel exemple, "Félicitations" sera affiché peu importe si la condition a été remplie.

Avec 100 pièces :

> +1Up\
> Félicitations

Avec un nombre pièces différent de 100 :

> Félicitations

L'indentation est donc cruciale : si elle n'est plus la même alors le code peut ne pas avoir la même signification !

Une condition qui n'exécute qu'une seule ligne/instruction peut être également écrite sur une ligne sans indentation :

```scala
if pieces == 100 then println("+1Up")
```

Cette forme plus compacte est couramment utilisée en Scala pour de petites conditions.

L'indentation n'est pas propre aux conditions en Scala. Elle s'applique à presque toutes les structures du langage : conditions, boucles, fonctions (que nous aborderons plus tard) et même variables :

```scala
val x =
  2
```

### Sinon

Dans de nombreux cas, nous voudrions exécuter une action si la proposition testée est vraie et une autre si elle est
fausse. Par exemple :

```scala
val sante = 2

if sante > 0 then
  println("Mario est vivant")

if sante <= 0 then
  println("Mario est mort")
```

Ce programme en l'état va afficher "Mario est vivant". Si je change la première ligne par `val sante = 0` (ou un nombre
négatif) alors il affichera "Mario est mort".

Ce cas de figure est très courant en informatique, c'est pourquoi la plupart des langages possèdent un mot clé "sinon"
pour raccourcir ces deux conditions en une seule. En Scala, il s'agit du mot-clé `else`:

```scala
val sante = 2

if sante > 0 then
  println("Mario est vivant")
else
  println("Mario est mort")
```

Cette condition peut se traduire par

> Si `sante` est supérieur à 0, alors afficher "Mario est vivant", sinon afficher "Mario est mort".

Le `else` nous a permis d'éviter une répétition et de rendre notre code plus lisible.

### Condition en tant que valeur

En Scala, la plupart des structures du langage sont des expressions, c'est-à-dire qu'elles renvoient une valeur. C'est le cas
de la condition `if ... else`:

```scala
val sante = 2

val statut =
  if sante > 0 then
    "Vivant"
  else
    "Mort"

println("Mario est " + statut)
```

> Mario est vivant

Et si nous changeons la valeur de `sante` à 0 :

> Mario est mort

La condition étant une valeur comme une autre, on peut l'utiliser partout à la place d'une variable ou d'une valeur
directement écrite. On appelle cette fonctionnalité "if as expression" ou en français "if en tant qu'expression".

## Conclusion

Nous avons aujourd'hui vu comment exécuter des actions suivant une condition en Scala. Cela nous permet maintenant de
faire plus que de simples opérations mathématiques.

Nous aborderons dans le prochain chapitre les boucles qui nous permettront de répéter des actions.

*Suite : [Mutabilité et boucles](./programmer-en-scala-3-mutabilite-et-boucles)*
