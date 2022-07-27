# Programmer en Scala 3 : Types et Variables

## Les types de données en Scala

Dans notre tout premier exemple, nous avons affiché en console le message "Hello World" avec le code suivant :
```scala
println("Hello World")
```

Intéressons-nous-y de plus près. Nous pouvons séparer en deux parties ce programme :
- `println` qui sert à afficher un texte
- `"Hello World"`

`"Hello World"` est une valeur qui représente un texte. On appelle ce type de valeur une chaîne de caractères, `String` en Scala.

En Scala, toute valeur, à l'instar de notre `"Hello World"`, a un type. Cela concerne également des valeurs numériques comme des entiers, des nombres à virgule etc...

Le langage met à notre disposition plusieurs types "de base":

| Nom     | Description                           | Note                                                                                |
|---------|---------------------------------------|-------------------------------------------------------------------------------------|
| Boolean | Un booléen                            | Peut être `true` (vrai/oui) ou `false` (faux/non)                                   |
| Byte    | Un entier sur un octet                | Entre -128 et 127                                                                   |
| Short   | Un entier sur deux octets             | Entre -2^15 et 2^15-1                                                               |
| Int     | Un entier sur quatre octets           | Entre -2^31 et 2^31-1, type entier par défaut.                                      |
| Long    | Un entier sur huit octets             | Entre -2^63 et 2^63-1                                                               |
| Float   | Un nombre à virgule sur quatre octets | Entre 1.40129846432481707e-45 et 3.40282346638528860e+38                            |
| Double  | Un nombre à virgule sur huit octets   | Entre 4.94065645841246544e-324 et 1.79769313486231570e+308, type décimal par défaut |
| Char    | Un seul caractère (sur 2 octets)      | S'écrit entre apostrophes. Exemple : 'a'                                             |
| String  | Une chaîne de caractères              | S'écrit entre guillemets. Exemple : `"Bonjour"`                                      |

Note : un octet est un groupe de 8 bits. Un bit est la plus petite unité en binaire qui peut uniquement valoir 0 ou 1.

### Opérations arithmétiques

Avec ces valeurs sont fournies différentes opérations comme les opérations arithmétiques pour les types numériques :
```scala
println(1 + 1) // 2
println(4 - 1) // 3
println(3 * 8) // 24
```

Attention : la multiplication se note avec l'astérisque `*` pour ne pas être confondue avec la lettre `x`.

La division peut se comporter de manière inattendue pour les débutants. Par exemple, `5/2` vaut `2` et `10/6` vaut `1`.
Cela s'explique par le fait qu'en Scala (comme dans de nombreux langages), la division de deux entiers donne aussi un entier (`Int`), la valeur étant tronquée. Pour avoir une division décimale, il faut que le diviseur ou le dividende soit aussi un nombre décimal :
```scala
println(5 / 2) // 2
println(5 / 2.0) // 2.5
println(5.0 / 2) // 2.5
println(5.0 / 2.0) // 2.5
```

### Opérations logiques sur les booléens

Il existe également trois opérations booléennes de base :
- Le "non" `!a`
- Le "et" `a && b`
- Le "ou" `a || b`

Le "non" booléen bascule simplement la valeur de notre booléen :
```scala
println(!true) // false
println(!false) // true
```

Le "et" booléen est vrai si et seulement si les deux booléens testés sont vrais :
```scala
println(true && true) // true
println(true && false) // false
println(false && true) // false
println(false && false) // false
```

Le "ou booléen" est vrai si au moins un des deux booléens testés est vrai :
```scala
println(true || true) // true
println(true || false) // true
println(false || true) // true
println(false || false) // false
```

Note : pour les curieux, ces opérations sont issues de [l'Algèbre de Boole](https://fr.wikipedia.org/wiki/Alg%C3%A8bre_de_Boole_(logique)), d'où leur nom.


### Concaténation de chaînes

Il existe aussi des "opérations de base" sur les chaînes de caractères. La plus connue est la concaténation, qui "colle" deux chaînes entre elles. Elle se note comme l'addition :

```scala
println("sca" + "la") // scala
```

On peut concaténer deux strings, mais aussi une string et n'importe quoi d'autre:
```scala
println("1+2 = " + (1+2)) // 1+2 = 3
```

## Les variables

### Introduction

Nous avons vu comment effectuer des opérations simples sur les types de base de Scala. Mais pour des valeurs différentes nous devons répéter le code. Les variables nous permettent de palier à ce problème en stockant des valeurs que nous pouvons réutiliser.

### Muabilité et immuabilité

En Scala, il existe deux types de variable: les variables muables et immuables.

Les variables _muables_ se déclarent avec le mot clé `var` :
```scala
var x = 5
println("x vaut " + x) // x vaut 5
println(x * 2) // 10
```

Ces variables ont la capacité de pouvoir être changées :
```scala
var x = 5
println(x * 2) // 10
x = 3
println(x * 2) // 6
```

Les variables _immuables_ se déclarent avec le mot-clé `val`. Elles ne peuvent pas être modifiées.
```scala
val message = "bonjour"
println(message) // bonjour
message = "salut" // Erreur !
```

En général, on utilise `val` sauf si on a une bonne raison de modifier la variable plus tard, auquel cas on utilise `var`.

### Le type des variables

Nous avons dit plus haut :

> En Scala, toute valeur, à l’instar de notre "Hello World", a un type.

Les variables ne font pas exception à cette règle ! Elles ont toutes un type. Il est interdit d'assigner à une variable muable une valeur du mauvais type.

```scala
var x = 1 // x est de type Int
x = "string" // Erreur !
x = 2.0 // Erreur !
```

Le compilateur trouve tout seul le type des variables, on dit qu'il _infère_ leur type. On  peut aussi expliciter le type avec la syntaxe suivante :

```scala
val one: Int = 1
val str: String = "message"
```

Bien sûr, le compilateur vérifie que l'on n'initialise pas une variable avec une valeur du mauvais type.

```scala
val pasBien: Int = "pas un entier" // Erreur !
```

Note : en Scala, la convention pour les noms de variables est le `camelCase`, c'est-à-dire que l'on colle les différents mots ("pas" et "bien" dans notre exemple) entre eux, en mettant une majuscule à chaque début de mot, sauf le premier. `commeCeciVousVoyez`, mais `pas_comme_ça` et `PasCommeÇa` non plus.

## Conclusion

Nous avons vu les différents types de données de base, leurs opérations, ainsi que les variables en Scala.
Nous aborderons prochainement les conditions.