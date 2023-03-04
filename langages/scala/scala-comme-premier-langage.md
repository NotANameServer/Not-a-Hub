# Scala comme premier langage de programmation

## Introduction

Quel langage de programmation enseigner aux débutants ? Faut-il leur apprendre un langage bas niveau comme le [C](https://fr.wikipedia.org/wiki/C_(langage)) ou haut niveau comme [Python](https://python.org/) ? Faut-il prendre un langage populaire ou est-ce qu'un langage moins connu peut faire l'affaire ? La question du langage à enseigner aux néophytes est largement débattue, et certains ont un avis très tranché. Nous ne proposons pas de donner une réponse définitive ici, mais d'exposer ce qui, selon nous, fait du langage Scala un bon candidat.

Cet article s'adresse principalement aux professeurs enseignant la programmation.

## Accessibilité

Il est important que le langage soit utilisable par le plus grand nombre, peu importe le niveau, c'est-à-dire qu'il soit accessible. On peut en effet supposer qu'un débutant ne possède pas de compétences techniques avancées. Plus il sera facile de commencer à utiliser le langage, moins le débutant se découragera, et plus il pourra se concentrer sur son apprentissage.

Un critère d'accessibilité important est le caractère multiplateforme : le novice doit pouvoir facilement utiliser le langage sur le système d'exploitation avec lequel il est le plus à l'aise. [Scala peut être exécuté sur Windows, Mac OS et Linux](https://www.scala-lang.org/download/).

Que le langage fonctionne sur sa machine c'est bien, mais c'est insuffisant ! Il faut que les outils autour du langage suivent. Le développeur, néophyte inclus, a besoin de facilement éditer son code, de l'exécuter, de le déboguer. Scala propose de nombreux outils, dont certains très faciles d'utilisation. Citons notamment le REPL, installé de base avec le langage, qui permet d'exécuter quelques lignes de Scala à la volée. En voici un aperçu :

![REPL Scala en action]({{ site.baseurl }}/assets/images/scala-repl-screenshot.png)


Notons que cette interface interactive embarque de la coloration syntaxique et de l'autocomplétion ! Elle permet de facilement tester de petits fragments de code. À l'opposé, un éditeur comme Visual Studio Code couplé avec un outil de build convient pour des scripts et des projets de plusieurs fichiers. Il existe plusieurs outils, mais le plus accessible est certainement [Scala CLI](https://scala-cli.virtuslab.org/), qui se veut plus simple que Maven, Gradle, etc.

Il existe aussi [Scastie, un éditeur en ligne](https://scastie.scala-lang.org/) qui permet d'expérimenter avec Scala et de partager facilement son code, sans rien installer.

Enfin, Scala est un [langage plutôt populaire](https://redmonk.com/rstephens/2022/10/20/top20-jun2022/) qui dispose d'une communauté active (notamment sur les plateformes [Scala Users Forum](https://users.scala-lang.org/) et [Discord](https://discord.gg/scala)) ainsi que de nombreuses [ressources en ligne](https://docs.scala-lang.org/learn.html) (cours vidéo, livres, articles, etc.). Non seulement le débutant peut apprendre en autonomie, mais il peut aussi obtenir de l'aide quand il en a besoin.

## "Scalable language"

Le nom "Scala" est la contraction de "Scalable language", que l'on peut traduire littéralement par "langage capable de passer à l'échelle" ou en meilleur français, "langage évolutif". En d'autres termes, Scala se veut aussi bien adapté pour de petits scripts de quelques lignes que pour de gros projets en entreprise. De ce fait, il permet d'enseigner les bases de la programmation mais aussi des concepts avancés, tels que la programmation parallèle ! L'enseignant pourra donc commencer son cours par des exemples simples dans son navigateur ou dans le REPL, puis entraîner les étudiants sur de petits scripts, et pourquoi pas les faire travailler sur un projet plus important à la fin du semestre.


> The scalable language also scales for teaching!
> − *Julien Richard-Foy, CTO au Scala Center.*

Scala combine la programmation orientée objet et la programmation fonctionnelle. Cela peut paraître étrange, mais force est de constater que de nombreux langages orientés objet incorporent aujourd'hui des éléments de programmation fonctionnelle : Java possède des "lambdas" depuis plusieurs années, Python propose depuis peu des "dataclasses", etc... Cette combinaison n'est pas forcée : le langage met simplement les outils à disposition du programmeur. Cela permet au débutant de travailler chaque paradigme séparément et de manière progressive, sans avoir besoin d'apprendre une nouvelle syntaxe et de nouveaux outils. C'est aussi un gain de temps pour l'enseignant, qui peut se concentrer sur les concepts et non sur les détails d'un langage supplémentaire.

Avec Scala, le professeur peut enseigner la programmation [impérative](https://fr.wikipedia.org/wiki/Programmation_imp%C3%A9rative) et [procédurale](https://fr.wikipedia.org/wiki/Programmation_proc%C3%A9durale), puis aborder la programmation orientée objet et la programmation fonctionnelle dans l'ordre de son choix. L'étudiant pourra alors découvrir les avantages de chaque paradigme.

## Pédagogie

Le choix du premier langage est important : il doit inculquer aux élèves les paradigmes, modes de pensée et bonnes habitudes générales, réutilisables dans les autres langages.

C'est pourquoi son aspect pédagogique joue un rôle capital.

### Une syntaxe claire

À l'instar de [Python](https://fr.wikipedia.org/wiki/Python_(langage)), Scala 3 possède une syntaxe concise et lisible. En voici une illustration :

```scala
case class User(name: String)

val friends = List(User("Bob"), User("Alice"))
val sortedFriends = friends.sortBy(_.name)

for friend <- sortedFriends do
  println(friend)
```

Bien que Scala soit statiquement typé, il est possible d'omettre les annotations de type dans de nombreux cas. Dans l'exemple ci-dessus, nous aurions pu écrire `val friends: List[User]`, mais Scala l'a inféré pour nous.

La [syntaxe basée sur l'indentation](https://wikipedia.org/fr/Indentation_comme_syntaxe) permet de réduire le "bruit" qui nuit à la lecture du code en laissant optionnel l'usage de délimiteurs explicites là où ils sont utiles.

Un autre avantage de la syntaxe présentée ci-dessus est sa lisibilité, qui résulte en partie de l'équilibre entre concision et verbosité. La verbosité d'un langage est souvent vue d'un mauvais oeil car considérée comme distrayant le programmeur ; mais il ne faut pas raccourcir la syntaxe au point qu'elle devienne obscure (un langage comme [05AB1E](https://github.com/Adriandmen/05AB1E) n'a d'intérêt que pour les compétitions de *code golf*).

### Régularité

En plus d'avoir une syntaxe lisible, le langage est également très cohérent et régulier.

Un bon porte-étendard de cette régularité est l'aspect "orienté objet pur" de Scala : toute valeur est objet. Il n'y a pas de primitif ou autre valeur "spéciale" : tout se traite de la même façon. Par exemple, voici une procédure en Scala :

```scala
def sayHello(): Unit =
  println("Hello World")
```

On peut noter deux choses :
- Le type de retour d'une fonction se note comme le type d'une variable, avec deux-points suivi du type. Quel est le type de `sayHello()` ? C'est `Unit`.
- Dans la plupart des langages mainstreams, le type de retour d'une [procédure](https://fr.wikipedia.org/wiki/Routine_(informatique)) est un type particulier souvent appelé "vide"/"void". En Scala, `Unit` est un type comme les autres.

Concrètement, cela veut dire que `Unit` se traite comme les autres types et fonctionne très bien avec les génériques, ce qui n'est pas le cas en [Go](https://fr.wikipedia.org/wiki/Go_(langage)) par exemple.

En Scala :
```scala
def workOnData[R](f: String => R): Unit = ???

workOnData(s => s.length) // ok
workOnData(s => println(s)) // ok
```

En Go :
```go
func workOnData[R any](f func(string) R) {}
func getLength(s string) int { // renvoie un int
    return len(s)
}
func display(s string) // ne renvoie rien

workOnData(getLength) // ok
workOnData(len) // erreur! "len (built-in) must be called"
workOnData(display) // erreur! "type func(s string) of display does not match func(string) R (cannot infer R)"
```

D'une manière générale, il y a peu de cas particuliers en Scala. Il n'y a par exemple pas de fonction "built-in" dont le status serait différent des autres. La bibliothèque standard fournit des fonctions comme les autres. Encore une fois, ce n'est pas le cas en Go qui traite `len` différemment. En choisissant Scala, on évite de passer du temps à expliquer ce genre de subtilités.

D'autres exemples de régularité :
- Les fonctions sont des objets comme les autres, on peut par exemple les stocker dans des variables.
- Le type d'une fonction qui prend un paramètre de type `A` et renvoie une valeur de type `B` s'écrit `A => B`, tout comme les lambdas : `a => b`
- Le corps d'une variable et d'une fonction sont exactement pareils
- Les opérateurs sont des fonctions comme les autres, par exemple `def +`. On ne définit pas de méthode "magique" (comme `__add__` en Python mais qui s'utilise finalement `+`).

### Typage statique et erreurs claires

Nous l'avons dit dans la section précédente : contrairement à Python, Scala est statiquement typé. Cela veut dire que le type de chaque fonction, variable et opération est connue à la compilation (avant exécution du programme). La cohérence entre ces types peut donc être vérifiée pour détecter les erreurs.

Prenons ce code en Python :
```python
def double(x):
    return x*2
```

si l'on affiche le résultat de `double(1)`, nous obtiendrons `2`. Cependant, si l'élève se trompe de valeur en faisant `double("1")`, il obtiendra en console `"11"` et peut ainsi penser à tort que sa fonction ne marche pas.

Voici l'équivalent en Scala :
```scala
def double(x: Double) =
  x*2
```

```scala
double(1) //Retourne 2
```
```scala
double("1") //Erreur à la compilation : "1" de type String n'est pas un Double
```

Note : `Double` représente en Scala un nombre à virgule flottante (à double précision).

Voici l'erreur exacte :
```scala
-- [E007] Type Mismatch Error: -------------------------------------------------
1 |double("1")
  |       ^^^
  |       Found:    ("1" : String)
  |       Required: Double
  |
  | longer explanation available when compiling with `-explain`
1 error found
```

L'erreur ci-dessus est très claire : elle indique de manière concise ce qui ne va pas, où et pourquoi.

Certains messages d'erreur proposent même des solutions :

```scala
import scala.mat //il manque un h
```

```scala
-- [E008] Not Found Error: -----------------------------------------------------
1 |import scala.mat
  |             ^^^
  |             value mat is not a member of scala - did you mean scala.math?
1 error found
```

Le fait de retourner des erreurs explicatives permet aux étudiants de pouvoir eux-mêmes comprendre et résoudre leur problème. Ils gagnent ainsi en autonomie.

> *In my experience with Scala, the dialog with the compiler about static errors strongly supports conceptual learning and strengthens self-efficacy: "I can do this and I’m getting a grip of it!".*
> -- Björn Regnell, Lund University, Sweden.

### Discipline

Scala incite les élèves à utiliser de bonnes pratiques reconnues et à prendre de bonnes habitudes de programmation, réutilisables dans d'autres langages.

Par exemple, la bibliothèque standard du langage utilise l'objet `Option` pour gérer l'absence potentielle de valeur :

```scala
val a: List[Int] = List(1, 2, 3)
val b: List[Int] = List.empty

a.headOption //Some(1)
b.headOption //None
```

Cela permet de forcer l'utilisateur à prendre en compte la possible absence de valeur et donc à prévenir les bugs/oublis :

```scala
val list: List[Int] = ???

list.headOption * 2
```
```scala
-- [E008] Not Found Error: -----------------------------------------------------
3 |list.headOption * 2
  |^^^^^^^^^^^^^^^^^
  |value * is not a member of Option[Int], but could be made available as an extension method.
1 error found
```

> `Option[Int]` ne possède pas d'opérateur `*`

Il y a plusieurs moyens d'utiliser `Option` mais une méthode courante est d'utiliser le [pattern matching](https://docs.scala-lang.org/tour/pattern-matching.html) :

```scala
list.headOption match
  case Some(head) => head * 2
  case None => 0
```

Si la liste est vide alors ce programme retournera `0`. Si cette liste a comme tête `2` alors ce programme retournera 4.

Autre exemple : par défaut, les variables en Scala sont immuables.

```scala
val x = 5
x = 4 //Erreur
```

Les structures de données par défaut le sont également. Par exemple, aucune méthode de `List` ne change son contenu mais renvoie à la place une nouvelle liste.

```scala
val list = List("Bob", "Clara", "Alice")

list.sorted //List("Alice", "Bob", "Clara")
list.reverse //List("Alice", "Clara", "Bob")
list.sorted.reverse //List("Clara", "Bob", "Alice")
```

Même si cela peut parraître contre-intuitif pour quelqu'un qui programme en C ou Python, la non-muabilité par défaut permet de libérer son esprit de tout souci de mutation non-contrôlée (les fameuses "mutation races").

Prenons l'exemple de la liste en Python qui est muable :

```python
l = []

do_something(l)
do_another_thing(l)
```

*Est-ce qu'à la fin de ce programme `l` a changé ? Si oui où ça ? Est-ce que l'ordre à de l'importance ?* Ces problèmes sont prévenus par l'immuabilité :

```scala
val list = List(1, 2, 3)

doSomething(l)
doAnotherThing(l)
```

Ici, nous savons que `list` n'a pas été modifiée donc nous n'avons pas à nous poser les questions ci-dessus. Nous pouvons ainsi nous focaliser localement, sans nous préoccuper de nos `doSomething` et `doAnotherThing`.

## Conclusion

Nous avons vu que Scala possède des atouts qui font de lui un langage adapté à l'enseignement de la programmation. Certaines fonctionnalités de Scala le démarquent de C ou Python comme l'immuabilité par défaut ou encore le typage statique (comparé à Python).