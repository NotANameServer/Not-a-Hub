---
layout: post
author: Raphaël FROMENTIN
date: 2026-06-25
title: "Parser combinators : construire des parsers résilients plus facilement"
---

Habituellement, lorsque j'ai à écrire un [parser] pour un projet comme un langage de programmation, j'utilise des [parser combinators]. Cette approche issue de la programmation fonctionnelle est très pratique puisqu'elle me permet de construire mon parser comme la composition de plus petits parsers. Par exemple, pour exprimer la grammaire d'une liste en JSON, je peux simplement combiner des parsers représentant : 

- Un délimiteur d'ouverture `[`
- Un élément
- Un séparateur `,`
- Un délimiteur de fermeture `]`

```scala
val elementParser: Parser[Char, Json] = ???

val arrayParser: Parser[Char, List[Json]] = Parser.inOrder(
  Parser.literal('['),
  Parser.separatedBy(elementParser, Parser.literal(',')),
  Parser.literal(']')
)
```

C'est donc une technique très efficace pour rapidement construire le parser de son langage. Le code a aussi le mérite d'être clair et facilement factorisable. Typiquement, mes opérateurs infixes sont souvent représentés comme ceci :

```scala
val binaryAddOps: Map[Char, (Expr, Expr) => Expr] = Map(
  '+' -> Expr.Add.apply,
  '-' -> Expr.Sub.apply
)

val binaryMulOps: Map[Char, (Expr, Expr) => Expr] = Map(
  '*' -> Expr.Mul.apply,
  '/' -> Expr.Div.apply
)

// Code qui utilise `binaryAddOps` et `binaryMulOps`
val infixOpsParser: Parser[Char, Expr] = ???
```

Enfin, l'écosystème du langage de programmation que j'utilise, [Scala], possède de nombreuses bibliothèques de parser combinators[^1][^2][^3][^4]. Ces raisons combinées me confortent bien dans mon choix.

Seulement, pour [mon projet de langage éducatif], je me suis demandé si cette approche était la bonne.

[parser]: https://fr.wikipedia.org/wiki/Analyse_syntaxique
[parser combinators]: https://fr.wikipedia.org/wiki/Combinateur_d%27analyseurs
[Scala]: https://scala-lang.org/
[mon projet de langage éducatif]: https://algorab.org/?lang=fr


## Critères d'un parser moderne

Un bon parser de langage de programmation, qui plus est un langage destiné à l'enseignement, implique plusieurs prérequis. 

Il doit d'abord pouvoir détecter toutes les erreurs de syntaxe présentes dans le code. En reprenant l'exemple de la liste en JSON, un bon parser devrait être capable de produire deux erreurs dans le cas suivant :

```json
[1,oups,2,3
```

- `oups` qui n'est pas une expression valide
- Un crochet fermant `]` est manquant

Le tout sans produire plusieurs erreurs en cascade pour une même faute.

Enfin, il est nécessaire de pouvoir comprendre le code au maximum même si celui-ci présente des erreurs de syntaxe. Cela permet au compilateur de tout de même vérifier les parties du code non concernées et, avec l'avènement de LSP, de fournir des informations à l'éditeur comme de la coloration syntaxique, de la navigation ou encore de l'auto-complétion.

En bref, le code dont la syntaxe est partiellement ou totalement erronée fait partie du quotidien d'un parser de langage de programmation. Ces erreurs sont à traiter comme des erreurs métier et doivent être aussi bien gérées que les cas où le code est entièrement valide.

*Note : Dans certains cas, les performances sont également importantes mais dans le contexte d'un langage de programmation, le parsing est rarement le goulot d'étranglement.*

Problème : les bibliothèques existantes, en Scala et dans la majorité des autres langages, se focalisent sur le "happy path" c'est-à-dire le cas où le code est syntaxiquement valide. La gestion des erreurs se résume souvent à remonter la première et s'arrêter sans produire de résultat partiel.

```scala
type Parser[I, +A] = List[I] => Either[ParseError, (remaining: List[I], output: A)]
```

Les bons messages d'erreur et la capacité à produire des résultats partiels sont pendant longtemps restés des caractéristiques attribuées aux parsers construits manuellement : compliqués à construire, compliqués à faire évoluer, mais vous y gagniez une bonne gestion des erreurs en cas d'entrée invalide.

## PureParser : des parser combinators modernes

Lors de mes recherches, je suis tombé sur un papier de recherche[^5] et une bibliothèque répondant aux contraintes précédemment citées : [Chumsky] en [Rust]. Cette bibliothèque ainsi qu'un article de son auteur[^6] m'ont fortement inspiré pour créer [PureParser], ma tentative en Scala pour répondre à ces exigences. Mention honorable à [MegaParsec] qui possède également un système de recouvrement d'erreurs plus rudimentaire.

Le changement principal réside dans la définition même d'un parser car celui-ci peut maintenant retourner des erreurs et tout de même une valeur.

```scala
type Parser[I, +A] = List[I] => (
  remaining: List[I],
  output: Option[A],
  errors: List[ParseError]
)
```

Comme PureParser est basé sur [PureLogic], une bibliothèque utilisant les [capabilities de Scala 3], un parser est défini comme ceci :

```scala
type Parser[-I, +A] = (State[Int], Reader[IndexedSeq[I]], Writer[ParseError[I]], Abort[Unit]) ?=> A
```

Dans la définition de PureParser, `Parser` n'est qu'un programme renvoyant `A` et présentant plusieurs effets :

- `State[Int]` : état mutable, ici l'indice du token à lire
- `Reader[IndexedSeq[I]]` : accès à la liste de tokens
- `Writer[ParseError]` : possibilité d'émettre 0, 1 ou plusieurs erreurs
- `Abort[Unit]` : possibilité de s'arrêter, de "couper" une branche de décision

Ce programme peut être évalué par la fonction `Parser.apply` qui retourne un `ParseResult` défini de la sorte :

```scala
case class ParseResult[A](
  output: Option[A],
  errors: Seq[ParseError],
  endPosition: Int
)
```

On voit clairement qu'il est possible ici de renvoyer une valeur indépendamment du nombre d'erreurs.

[Chumsky]: https://docs.rs/chumsky/latest/chumsky/
[Rust]: https://rust-lang.org/fr/
[PureParser]: https://github.com/Iltotore/pureparser
[MegaParsec]: https://github.com/mrkkrp/megaparsec
[PureLogic]: https://ghostdogpr.github.io/purelogic/
[capabilities de Scala 3]: https://nrinaudo.github.io/articles/capabilities.html

### Quelques stratégies de recouvrement

En reprenant le précédent exemple :

```json
[1,oups,2,3
```

Un résultat comme celui-ci est attendu :

```scala
ParseResult(
  output = Some(List(Literal(1), Invalid, Literal(2), Literal(3))),
  errors = Seq(
    ParseError(expected = Label("expression"), at = 3),
    EOF
  ),
  endPosition = 11
)
```

Le parser sans stratégie de recouvrement pour une telle expression est celui-ci :

```scala
enum Expr:
  case Literal(value: Int)
  case Array(elements: List[Expr])
  case Invalid //Nous servira plus tard

val literalParser: Parser[Char, Expr] = Expr.Literal(
  Parser
    .regex("[0-9]+")
    .toIntOption
    .getOrElse(Parser.abort)
)

val arrayParser: Parser[Char, Expr] = Expr.Array(
  Parser.inOrder(
    Parser.literal('['),
    Parser.separatedBy(exprParser, Parser.literal(',')),
    Parser.literal(']')
  )
)
                   
val exprParser: Parser[Char, Expr] = Parser.expect(
  Parser.firstOf(
    literalParser,
    arrayParser
  ),
  "expression"
)
```

Une expression telle que `[1,2,3]` est correctement lue mais `[1,oups,2,3]` nous renvoie une erreur et aucun résultat.

Dans PureParser, le recouvrement se fait par le combinateur `Parser.recoverWith` qui demande une `RecoveryStrategy`. Une stratégie de recouvrement peut être vue comme un parser de secours pouvant éventuellement être construit à partir du parser mis en échec :

```scala
type RecoveryStrategy[I, +A] = Parser[I, A] => Parser[I, A]
```

Une technique très souvent utilisée pour tenter de récupérer le reste de l'expression à parser est le "mode panique" : lorsque le parser d'expression échoue, celui-ci va entrer en mode "panique" et sauter les tokens jusqu'à tomber sur un qui lui permet de retomber sur ses pattes, qu'on appelle "token de synchronisation". Ici, il est fort probable que l'expression invalide se termine juste avant une virgule ou un crochet fermant.

- `[1,oups,2,3]` -> `[1,<invalide>,2,3]`
- `[1,2,3,oups]` -> `[1,2,3,<invalide>]`

La règle de recouvrement serait donc "passer tous les tokens jusqu'à tomber sur une virgule ou un crochet fermant, et retourner un nœud invalide".

```scala
val exprParser: Parser[Char, Expr] = Parser.recoverWith(
  Parser.expect(
    Parser.firstOf(
      literalParser,
      arrayParser
    ),
    "expression"
  ),
  RecoveryStrategy.skipUntil(Parser.oneOf(",]"), Expr.Invalid)
)
```

Reste maintenant à gérer le manque de crochet fermant. Réussir à correctement réparer un délimiteur manquant s'avère souvent complexe. Comme notre syntaxe est assez simple, nous n'avons réellement qu'un cas de figure :
- `[1,2,3` -> `[1,2,3]`

Il suffit donc ici d'un parser de secours qui vérifierait que la fin de l'entrée a bien été atteinte, auquel cas nous pouvons partir du principe que le crochet de fermeture aurait dû se trouver ici.

```scala
val arrayParser: Parser[Char, Expr] = Expr.Array(
  Parser.inOrder(
    Parser.literal('['),
    Parser.separatedBy(exprParser, Parser.literal(',')),
    Parser.recoverWith(
      Parser.literal(']'),
      RecoveryStrategy.viaParser(Parser.eof)
    )
  )
)
```

L'exemple mis bout à bout nous permet bien d'obtenir le résultat voulu avec `[1,oups,2,3` : deux erreurs tout en réussissant à parser `[1,<invalide>,2,3]`. Des exemples plus poussés sont à retrouver [ici] ([sources]).

[ici]: https://iltotore.github.io/pureparser/examples/
[sources]: https://github.com/Iltotore/pureparser/tree/main/examples

## Conclusion

Après avoir lu sur le sujet et implémenté les idées déjà explorées par Chumsky, je suis convaincu qu'il est possible de faire des parsers répondant aux besoins des langages de programmation modernes prêts pour la production, le tout de manière déclarative grâce aux parser combinators.

L'approche est récente et minoritaire mais puisse-t-elle permettre d'écrire de bons parsers plus simplement. Je compte de mon côté faire évoluer PureParser notamment en [mangeant ma propre nourriture pour chien](https://en.wikipedia.org/wiki/Eating_your_own_dog_food) à travers [mon langage](https://algorab.org/?lang=fr).

[mangeant ma propre nourriture pour chien]: https://en.wikipedia.org/wiki/Eating_your_own_dog_food
[mon langage]: https://algorab.org/?lang=fr

## Références

[^1]: Scala Contributors, "scala-parser-combinators: simple combinator-based parsing for Scala. formerly part of the Scala standard library, now a separate community-maintained module,” GitHub, Aug. 15, 2013. https://github.com/scala/scala-parser-combinators
[^2]: H. Li, “com-lihaoyi/fastparse: Writing Fast Parsers Fast in Scala,” GitHub, Nov. 29, 2014. https://github.com/com-lihaoyi/fastparse
[^3]: J. Willis, “Parsley: The Fastest Parser Combinator Library in the West,” Master’s thesis, University of Bristol, 2018. [Online]. Available: https://github.com/J-mie6/Parsley/blob/master/parsley.pdf
[^4]: ZIO Contributors, “zio/zio-parser,” GitHub, Sep. 22, 2021. https://github.com/zio/zio-parser
[^5]: S. Medeiros and F. Mascarenhas, “Syntax error recovery in parsing expression grammars,” 33rd Annual ACM Symposium on Applied Computing, pp. 1195–1202, Apr. 2018, doi: 10.1145/3167132.3167261.
[^6]: J. Barretto, “Why can’t error-tolerant parsers also be easy to write?,” Jan. 13, 2022. https://blog.jsbarretto.com/post/parser-combinators-and-error-recovery