---
layout: post
author: Adrien Baudet
date: 2023-08-21
title: "Les arrays php sont-ils des arrays ?"
---

Si vous êtes utilisateur de PHP, cette question vous déroutera peut-être, ou vous donnera l'impression d'être face à une blague. Au cours de cet article, j'espère néanmoins vous avoir convaincu de sa pertinence.



## Que sont les arrays de php ?

Une chose assez commune en programmation c'est que **les noms ne sont pas toujours consistants entre deux langages** : une boucle for ne s'écrira pas pareil en C ou en Python; un hashmap en Java sera un map en Haxe, ou un dictionnaire en C#. En fait cela vient tout simplement de la diversités des langages et de leur façon de faire : Il n'y a pas une façon parfaite qui domine les autres mais plusieurs approches, souvent complémentaires, pour résoudre des problèmes et le vocabulaire d'un langage va s'adapter à son approche.

Qu'en est-il alors des arrays de PHP ? Voyons ce que la [documentation](https://www.php.net/manual/en/language.types.array.php) a à nous apprendre :


> An array in PHP is actually an ordered map. A map is a type that associates values to keys. This type is optimized for several different uses; it can be treated as an array, list (vector), hash table (an implementation of a map), dictionary, collection, stack, queue, and probably more. As array values can be other arrays, trees and multidimensional arrays are also possible. 


Ici on parle de map, comme je le citais plus haut, mais on mentionne aussi un usage comme un array, une liste, une pile et une file. Cela veux donc dire que php serait tout cela à la fois ? Pour mieux comprendre, je vous propose une définition des collections.



## Quel types collections existent-ils ?

Pour cette partie je vais définir des collections d'un point de vue purement algorithmique, c'est à dire qu'on ne s'attachera ni à un langage ni à une implémentation précise : on visera un contexte plus général et abstrait. En terme de collections on pourra citer trois types de collections principaux :


### Les tableaux

Un tableau est une collection linéraire où les éléments sont placés les uns après les autres. Chaque élément est accessible dans le tableau à partir de sa position, en commençant généralement par la position 0. 

Par exemple :
```
tableau = [1, 14, 42]
```

Ici on pourra accéder à la valeur `1` via la position `0` (e.g : `tableau[0]`) et la valeur `42` à la position `2`. Si on venait à supprimer la valeur `14`, on accèderais alors la valeur `42` serait accessible à la position `1`, puisqu'il vient de passer une place en avant.

Selon l'implémentation, il arrive qu'un array soit de taille fixe et qu'on ne puisse donc pas la modifier. Dans le cas contraire il est alors courant d'ajouter des valeurs au début où à la fin du tableau, pouvant alors modifier les positions des valeurs à l'intérieur.


### Les dictionnaires

Un dictionnaire (ou tableau associatif) est une collection de paires de clés-valeurs. On n'accède plus à une valeur par le biais de sa position mais par celui de sa clé correspondante. De plus il n'est pas nécessaire d'utiliser des clés numériques : on peut utiliser potentiellement n'importe quel type arbitraire, comme des chaines de caractères ou des symboles. On peut alors associer cette collection au dictionnaire, ou chaque définition est accédée via le terme d'elle définit.

Par exemple :
```
dictionnaire = [
  "eau" => "du liquide",
  "la reponse" => "42",
]
```

Ici on pourra accéder à la réponse en faisait `dictionnaire["la reponse"]`


### Les sets

Un set est une collection de valeurs en exemplaires uniques, c'est à dire qu'il n'est pas possible pour cette collection de posséder des duplicatas.


Par exemple :
```
set = {1, 3, 46, 72}
```

Dans cet exemple tenter de rajouter les valeurs `3`, ou `72` n'aura aucun effet car elles sont déjà présentes dans le set.



## Qu'en est-il donc de l'array de php ?

Si on regarde à nouveau la [documentation](https://www.php.net/manual/en/language.types.array.php) de php on observe le texte suivant

```php
// An array can be created using the array() language construct. It takes any number of comma-separated key => value pairs as arguments.
// A short array syntax exists which replaces array() with []. 

array(
    key  => value,
    key2 => value2,
    key3 => value3,
    ...
)
```

On parle bien ici ce paire de clés-valeurs : l'array php est donc bien un dictionnaire ?


### Mais qu'en est-il de la syntaxe sans clés ?

En effet il existe une seconde syntaxe possible où aucune clé n'est renseignée. Si on regarde la doc :

```php
// The key is optional. If it is not specified, PHP will use the increment of the largest previously used int key.
<?php
$array = array("foo", "bar", "hello", "world");
var_dump($array);
?>

// The above example will output:
array(4) {
  [0]=>
  string(3) "foo"
  [1]=>
  string(3) "bar"
  [2]=>
  string(5) "hello"
  [3]=>
  string(5) "world"
}
```

De fait, certes on n'a mentionné aucune clé mais elles sont toujours là, *les clés sont seulement définie implicitement par le compilateur*.

À partir de ce constat, la conclusion me semble assez évidente : les arrays de PHP sont en fait indéniablement des dictionnaires.


## Qu'en est-il à l'usage ?

Malgré cette conlusion, il me semblait intéressant d'ajouter un dernier point sur l'usage que l'on peut avoir des arrays PHP, en dehors se sa pure définition.

En premier lieu et pour simplifier mon propos je vais introduire le terme de liste. Une liste en PHP est un array dont les clés sont constituées de nombres consécutifs de 0 à count($array)-1. Cela correspond à la définition fournie par la fonction standarde de PHP [array_is_list](https://www.php.net/manual/en/function.array-is-list.php). 

Par extension et si on reprend les exemples de syntaxe au dessus, une liste est ce que founit PHP quand on ne mentionne aucune clé dans son tableau, soit donc le cas le plus éloigné syntaxiquement du dictionnaire.


### Tests de l'array PHP

Pour tester comme PHP traite les listes, j'ai testé le comportement de plusieurs fonctions qui insèrent ou enlèvent des valeurs pour voir comment les clés sont traitées. Les fonctions testée sont:

- array_filter
- array_shift
- array_slice
- array_splice
- array_splice pour un ajout
- array_unshift
- shuffle (car il modifie l'ordre)

Pour être sûr de ne rien louper je fais les tests avec 

- un array avec clés explicites
- une liste avec clés explicites
- une liste avec clés explicites dans l'ordre inverse
- une liste avec clés implicites.

Mon script ressemble à ceci pour array_filter :

```php
<?php
// $numbers = ["zero" => 0, "un" => 1, "deux" => 2];
// $numbers = [0 => 0, 1 => 1, 2 => 2];
// $numbers = [2 => 0, 1 => 1, 0 => 2];
$numbers = [0, 1, 2];


$test = array_filter($numbers, fn($value) => ($value % 2) !== 0);
var_dump("Array filter");
var_dump($test);
```


### Résultats

Ce que j'ai pu constater d'abord c'est que dans les deux cas de liste, les résultats sont identiques, et ce n'est pas tellement surprenant. On remarque aussi que pour toutes les fonctions hormis `array_filter`, les clés sont modifiées pour que l'array reste une liste.

Dans le cas d'un array non liste, au contraire, les clés ne sont pas modifiées, hormis la fonction `shuffle`, qui semble transformer l'array en liste.

On nottera aussi que splice va traiter l'offset de modification d'après ordre dans lequel les valeurs sont insérées et non pas d'après les clés ainsi `array_splice($test, 1, 1)` ou `$test = [1 => 0, 2 => 1, 0 => 2]` supprimera la paire `2 => 1`.


## Conclusion

Pour conclure on a vu que par définitions les arrays de PHP ne sont pas vraiment des arrays mais des dictionnaires. On remarquera cependant que les fonction et la syntaxe sont conçu pour les utiliser comme de vrai tableaux en camouflant potentiellement les clés tout le long de la manipulation. Il faudra tout de même faire attention car certaines fonctions comme `array_filter` ne font pas le nécessaire et il faudra garder cela en tête afin de ne pas être surpris.

Je ne les ai pas testé mais il y a aussi les fonction de tris qui peuvent changer l'ordre des valeurs, dans ce cas cependant c'est le choix la fonction et non pas la nature de l'array qui déterminera ou non la réassignation des clés.

Donc les arrays php sont-ils des arrays ? Techniquement non, mais on peut faire comme si.