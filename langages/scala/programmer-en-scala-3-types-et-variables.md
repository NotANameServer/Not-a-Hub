# Programmer en Scala 3 : Types et Variables

## Les variables

### Introduction

Un programme informatique manipule souvent un grand nombre d'informations. Prenons l'exemple d'un jeu vidéo comme Mario Bros : le jeu doit stocker la santé de Mario (petit, grand...), le nombre de pièces ou encore le nombre de vies restantes.

Ces données sont stockées dans la mémoire de l'ordinateur (ou de la console de jeux) à une certaine adresse. Chaque case mémoire possède une adresse qui permet de lire et d'écrire la valeur qui y est stockée, un peu comme un grand tableau.

![adresses mémoires](/assets/images/memory-scheme.png)

*Remarque : notez que la première adresse est l'adresse 0, et non l'adresse 1 ! C'est courant en informatique de compter à partir de zéro. Puisque c'est le premier chiffre, ne pas l'utiliser pour numéroter reviendrait à "perdre" un numéro.*

Dans des temps reculés, il fallait retenir à quelle adresse était stockée chaque valeur ce qui, avec le nombre de valeurs à stocker, devenait rapidement compliqué ! Où as-tu stocké le nombre de pièces déjà ? Adresse 756 ou 759 ?

C'est pour résoudre ce problème que les variables ont été créées. L'idée est d'utiliser des noms compréhensibles par les humains, et de laisser la machine s'occuper des adresses automatiquement. C'est un peu comme si on mettait une étiquette sur les adresses des cases mémoires. On appelle le nom qu'on utilise (l'étiquette choisie) et la valeur qui lui est associée (stockée dans la case mémoire) une **variable**.

![variables](/assets/images/variable-scheme.png)

Et voilà ! Pas besoin de retenir les adresses mémoires, il suffit de retenir le nom de la variable !

### Utilisation

En Scala, une variable se crée en utilisant le mot-clé `val` suivi d'un égal et d'une valeur:

```scala
val x = 1
println(x) // 1
```

Dans ce petit exemple, nous avons créé une variable avec pour nom `x` et pour valeur `1`. On peut alors dire que "x vaut 1". Nous avons ensuite affiché la valeur de `x` avec `println`. Le suffixe `ln` est une abbréviation de "line", il signifie que l'on affiche une valeur puis que l'on saute une ligne.

Ainsi, le code suivant :

```scala
println(1)
println(2)
```

affiche chaque valeur sur une ligne différente :

> 1\
> 2


Bien sûr, Scala n'est pas limité aux nombres. Il est aussi possible d'afficher du texte, en l'écrivant entre guillemetes doubles (`"`). Par exemple :

```scala
println("Bonjour !")
```

affiche :

> Bonjour !

## Les types

En cuisine, il est important de savoir ce que l'on manipule. (Comment ça je ne peux pas couper des oignons avec une cuillère ?!)

En programmation aussi ! On aimerait bien savoir :
- le genre de valeur que l'on est en train d'utiliser / on a le droit d'utiliser : un nombre entier ? du texte ? une liste de courses ?
- ce que l'on peut faire avec : multiplier deux nombres semble logique et utile, mais multiplier deux bouts de texte... moins.
- comment l'ordinateur doit stocker les informations dans les cases mémoires

Toutes ces informations sont données par le **type** de la valeur.

En Scala, toute valeur et toute variable possède un type. Le type d'une variable est connu avant le lancement du programme, et restreint les valeurs qu'elle accepte. Par exemple, une variable de type "nombre entier" ne peut contenir que des nombres entiers, et pas du texte. Le langage définit certains types de base, et il est possible d'en définir de nouveaux (nous verrons cela plus tard).

Voici quelques types de base :

| Type   | Ce qu'on peut mettre dedans | Exemple de valeur |
|--------|-----------------------------|-------------------|
| Int    | un nombre entier            | `1`               |
| Double | un nombre décimal           | `1.5`             |
| String | du texte                    | `"Bonjour !"`     |

Ajoutons les types sur notre schéma. On voit que chaque variable a finalement un nom, un type, une adresse mémoire, et une valeur. Par exemple :
- `x` a pour type `Int`, pour adresse `0` et pour valeur `1`.
- `nombrePieces` a pour type `Int`, pour adresse `756` et pour valeur `102`.

![variables typées](/assets/images/variable-type-scala-scheme.png)

### Opérations

Comme nous l'avons dit plus haut, le type permet de connaître les opérations que l'on peut faire avec les valeurs. Certaines opérations ne sont possibles qu'avec certains types. C'est le cas de la plupart des opérations arithmétiques :

```scala
4 - 1 // 3
"4" - "1" // Erreur ! Comment soustraire deux textes ?
```

Nous pouvons écrire `4 - 1` car le type `Int` définit un "opérateur" `-` (prononcé "moins"), qui effectue une soustraction entre deux nombres entiers. En revanche, le type `String` ne définit pas cet opérateur, et Scala nous informe donc le code `"4" - "1"` n'est pas valide.

Certains opérateurs existent pour plusieurs types mais se comportent différemment. C'est le cas de l'opérateur `+` qui additionne les nombres et concatène les textes (c'est-à-dire qui les colle bout à bout). Ne vous a-t-on jamais fait la blague "1 et 1 font 11" ? Nous pouvons rencontrer le même genre de facétie en informatique :

```scala
1 + 1 // 2: Int (entier)
1.0 + 1.0 // 2.0: Double (décimal)
"1" + "1" // 11: String (texte)
```

`1 + 1` font `2` car il s'agit de deux entiers que l'on additionne tandis que `"1" + "1"` font `"11"` car il s'agit de deux textes que l'on concatène. `1` et `"1"` n'ont pas le même type et se comportent donc différemment malgré leur apparente similitude.

En plus des soustractions et des additions, on peut également effectuer des multiplications avec l'opérateur `*` et des divisions avec l'opérateur `/`. Pas de surprise avec les multiplications, mais attention avec la division. Si on divise deux nombres entiers, le résultat est un nombre entier *tronqué*. Si on divise deux nombres décimaux, le résultat est un nombre décimal.

```scala
6 / 2 // 3: Int
5 / 2 // 2: Int - Attention: la partie décimale est tronquée (supprimée)
5.0 / 2.0 // 2.5: Double
5 / 2.0 // 2.5: Egalement un Double !
```

### Type explicite

En Scala, les variables possèdent toutes un type. Mais, comme vous l'avez peut-être remarqué, nous n'avons jamais écrit ce type dans notre code pour l'instant ! En effet, Scala est capable de trouver automatiquement le type des variables, en fonction de la valeur que l'on donne lors de leur création. On appelle ce mécanisme _l'inférence de type_.

Reprenons le premier exemple de ce chapitre :
```scala
val x = 1
```

`x` est ici une variable qui stocke des nombres entiers, son type est donc `Int`. Scala a trouvé le type tout seul, il n'est pas écrit.

Il est possible d'expliciter le type d'une variable en écrivant après son nom `: NomDuType` :

```scala
val x: Int = 1 // toujours de type Int, mais explicitement écrit
```

### Conversions implicites

Les valeurs de certains types peuvent être converties vers un autre. C'est le cas des nombres entiers vers les nombres décimaux :
```scala
val x: Int = 1 // 1: Entier
val y: Double = x // 1.0: Nombre décimal
```

Notons cependant que ce n'est pas réciproque :
```scala
val x: Double = 1.0
val y: Int = x // Erreur
```

Dans le cas présent, cela est dû au fait qu'un nombre décimal n'est pas forcément un entier : `1.0` a comme équivalent `1` mais quel est l'équivalent entier de `1.5` ?

## Conclusion

Nous avons vu comment stocker des données en utilisant les variables. Nous avons également parlé de la notion de type lié aux valeurs manipulées, importante en Scala.

Nous aborderons dans le cours suivant les conditions.
