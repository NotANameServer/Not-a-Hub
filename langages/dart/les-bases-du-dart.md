---
layout: post
author: Rapougnac
date: 2023-12-20
title: "Les bases du Dart"
---

## Introduction
Dart est un langage de programmation orienté object, est statiquement et fortement typé, c'est à dire que les types des variables sont connus à la compilation et qu'ils ne peuvent être changés. Il est développé par Google et est utilisé pour le développement d'applications mobiles, desktop et web, ainsi que pour le développement de serveurs.

Sa syntaxe est proche de celle de Java et de C#. Mais se veut moins verbeuse et plus moderne. Il est compilé en code machine, JavaScript ou bien WebAssembly.

<!-- TODO: Regarder l'étape d'installation? -->
<!-- ## Installation -->

## L'IDE
Celui recommandé par Dart est [VSCode](https://code.visualstudio.com/) avec [l'extension Dart Code](https://marketplace.visualstudio.com/items?itemName=Dart-Code.dart-code) d'installée, cependant, si cela ne vous convient pas, il y a une liste non-exhaustive qui les rcensent [ici](https://dart.dev/tools#ides-and-editors).

Vous pouvez aussi suivre ce petit tutoriel directement sur [DartPad](https://dartpad.dev/). Ce qui vous permettra de tester le code sans avoir à installer quoi que ce soit 😊. Veuillez noter que DartPad ne permet pas de faire de l'IO (Input/Output) ni de réflexion, donc les imports `dart:io` et `dart:mirrors` ne sont pas disponibles.

## L'arborescence
Une fois Dart installé, nous pouvons ouvrir un terminal et executer `dart create myapp` pour initialiser un projet de base.
On remarquera plusieurs dossiers et fichiers qui on étés créés.
Les principaux sont :
- `bin/`, qui correspondra, majoritairement à là où nous allons exécuter notre programme.
- `lib/`, est l'endroit de notre projet principal, nous pourrons y mettre notre logique et classes.
- `test/`, il est créé automatiquement pour gérer les tests unitaires, ça ne sera pas utile pour aujourd'hui.
- `analysis_options.yaml` - Il est présent pour customiser comment fonctionne l'analyseur.
- `pubspec.yaml` - Il permet de gérer nos dépendances et les données concernant notre paquet.

## Création de notre premier programme
Maintenant que nous avons appris les rudiments, on peut à présent se rendre dans le fichier situé dans `bin/`, il porte le même nom que ce qu'on a nommé plus tôt, en l'occurence, `myapp.dart`.
On peut enlever le code par défaut, et garder la fonction `main()`, c'est ici notre point d'entrée.
```dart
void main(List<String> arguments) {
  print('Hello, Dart!');
}
```
Nous pouvons maintenant éxecuter `dart run` afin de lancer notre programme fraîchement créé:
```
Hello, Dart!
```

## Conclusion
Nous avons vu dans ce chapitre l'installation de Dart, son IDE, l'arborescence d'un projet et comment créer notre premier programme. Dans le prochain chapitre, nous verrons les variables et les types de base.
