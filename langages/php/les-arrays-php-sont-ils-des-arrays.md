---
layout: post
author: Adrien Baudet
date: 2023-08-21
title: "Les arrays php sont-ils des arrays ?"
---
Si vous êtes utilisateur de PHP, cette question vous déroutera peut-être, ou vous donnera l'impression d'être face à une blague. Au cours de cet article, j'espère néanmoins vous avoir convaincu de sa pertinence.


## Que sont les arrays de php ?

Une chose assez commune en programmation c'est que **les noms ne sont pas toujours consistants entre deux langages** : une boucle for en Python s'écrira foreach en PHP; un hashmap en Java sera un map en Javascript, ou un dictionnary en C#. En fait cela vient tout simplement de la diversités des langages et de leurs façons de faire : Il n'y a pas une façon parfaite qui domine les autres mais plusieurs approches, souvent complémentaires, pour résoudre des problèmes et le vocabulaire d'un langage va s'adapter à son approche.

Qu'en est-il alors des arrays de PHP ? Voyons ce que la [documentation](https://www.php.net/manual/en/language.types.array.php) a à nous apprendre :


> An array in PHP is actually an ordered map. A map is a type that associates values to keys. This type is optimized for several different uses; it can be treated as an array, list (vector), hash table (an implementation of a map), dictionary, collection, stack, queue, and probably more. As array values can be other arrays, trees and multidimensional arrays are also possible. 


Ici on parle de map, comme je le citais plus haut, mais on mentionne aussi de nombreux autres usages. Cela veux donc dire que l'array php serait tout cela à la fois ? Pour mieux comprendre, je vous propose une définition des collections.


## Quels types de collections existe-t-il ?

Pour cette partie je vais définir des collections d'un point de vue purement algorithmique, c'est à dire qu'on ne s'attachera ni à un langage ni à une implémentation précise : on visera un contexte plus général et abstrait. On pourra citer trois types principaux de collections :


### Les arrays

Un array est une collection linéraire où les éléments sont placés les uns après les autres. Chaque élément est accessible dans l'array à partir de sa position, en commençant généralement par la position 0. 

Par exemple :
```
array = [1, 14, 42]
```

Ici on pourra accéder à la valeur `1` via la position `0` (e.g : `array[0]`) et la valeur `42` à la position `2`. Si on venait à supprimer la valeur `14`, alors la valeur `42` serait accessible à la position `1`, puisqu'il vient de passer une place en avant.

Selon l'implémentation, il arrive qu'un array soit de taille fixe. Quand l'array n'est pas de taille fixe, il est alors courant d'ajouter des valeurs au début où à la fin du array, offrant alors la possibilité de modifier leurs positions.


### Les listes chainées

Une liste chainée est une collection dynamique constituée d'une paire contenant un élément et un lien vair une paire suivante contenant l'élément suivant et un nouveau lien, et ce autant de fois qu'il y a d'éléments dans la liste.


### Les dictionnaires

Un dictionnaire est une collection de paires de clés-valeurs. On n'accède plus à une valeur par le biais de sa position mais par le biais de sa clé correspondante. De plus il n'est pas nécessaire d'utiliser des clés numériques : on peut utiliser potentiellement n'importe quel type arbitraire, comme des chaines de caractères. On peut alors associer cette collection à un dictionnaire physique, où chaque définition est accédée via le terme d'elle définit.

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


### Ordonnés ou pas ?

Petite subtilité qui nous servira pour après : on a dit plus haut que dans le cas d'un array les valeurs étaient récupérables d'après leur position. Comme ce n'est pas le cas pour le dictionnaire et le set, il est courant de les retrouver sous une forme non ordonnée : c'est à dire qu'en les parcourant on ne retrouvera pas les valeurs dans l'ordre où elle ont été insérées.


## Qu'en est-il donc du array de php ?

Si on regarde à nouveau la [documentation](https://www.php.net/manual/en/language.types.array.php) de php on peut lire :

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

On parle bien ici de paires de clé-valeur : l'array php est donc bien un dictionnaire ?


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

De fait, certes on n'a mentionné aucune clé mais elles sont toujours là, **les clés sont seulement définie implicitement par l'interpréteur'**.

À partir de ce constat, les arrays de PHP ont tout pour être des dictionnaires. Néanmoins, la possibilité d'accéder aux valeurs comme dans un array implique une subtilité supplémentaire en terme d'ordonancement. Comme je disais plus haut, les dictionnaires sont généralemrent non ordonnés ce qui implique que l'ordre d'insertion n'est pas conservé, contrairement aux arrays. Il ne s'agit donc pas de simples dictionnaires, mais de `dictionnaires ordonnés`.


## Qu'en est-il à l'usage ?

Malgré cette conlusion, il me semblait intéressant d'ajouter un dernier point sur l'usage que l'on peut avoir des arrays PHP, en dehors se sa pure définition.

En premier lieu et pour simplifier mon propos je vais introduire le terme de liste. Une liste en PHP est un dictionnaire dont les clés sont constituées de nombres consécutifs de 0 à count($array)-1. Cela correspond à la définition fournie par la fonction standarde de PHP [array_is_list](https://www.php.net/manual/en/function.array-is-list.php).

Par extension et si on reprend les exemples de syntaxe au dessus, une liste est ce que founit PHP quand on ne mentionne aucune clé dans son array, soit le cas le plus éloigné syntaxiquement du dictionnaire.


### Tests du array PHP

Pour tester comment PHP traite les listes, j'ai testé le comportement de plusieurs fonctions qui insèrent ou enlèvent des valeurs pour voir comment les clés sont traitées. Les fonctions testées sont:

- array_shift
- array_filter
- array_slice
- array_splice
- array_splice pour un ajout
- array_unshift
- shuffle (car il modifie l'ordre)

Pour être sûr de ne rien louper je fais les tests avec

- un array (associatif) avec clés explicites
- une liste avec clés explicites
- une liste avec clés explicites dans l'ordre inverse
- une liste avec clés implicites.

Pour `array_shift` et `array_filter`, mon script ressemble à ceci :

```php
<?php
// $numbers = ["zero" => 0, "un" => 1, "deux" => 2];
// $numbers = [0 => 0, 1 => 1, 2 => 2];
// $numbers = [2 => 0, 1 => 1, 0 => 2];
$numbers = [0, 1, 2];


$test = $numbers;
array_shift($test);
var_dump("Array shift");
var_dump($test);

$test = array_filter($numbers, fn($value) => ($value % 2) !== 0);
var_dump("Array filter");
var_dump($test);
```

Avec ce code on obtiendra le résultat suivant :

```php
string(11) "Array shift"
array(2) {
  [0]=>
  int(1)
  [1]=>
  int(2)
}

string(12) "Array filter"
array(1) {
  [1]=>
  int(1)
}
```

On remarque que pour array_shift les clés ont été changées, mais que pour array_filter la clé reste la même pour la valeur restante.


### Résultats

Ce que j'ai pu constater d'abord c'est que dans les deux cas de liste, les résultats sont identiques, et ce n'est pas tellement surprenant. On remarque aussi que pour toutes les fonctions hormis `array_filter`, les clés sont modifiées pour qu'un array reste une liste.

Dans le cas d'un array non liste, au contraire, les clés ne sont pas modifiées, hormis la fonction `shuffle`, qui semble transformer l'array en liste.

On notera aussi que splice va traiter l'offset de modification d'après ordre dans lequel les valeurs sont insérées et non pas d'après les clés ainsi `array_splice($test, 1, 1)` ou `$test = [1 => 0, 2 => 1, 0 => 2]` supprimera la paire `2 => 1`.


## Conclusion

Pour conclure on a vu que par définition les arrays de PHP ne sont pas vraiment des arrays mais des hashs. On remarquera cependant que les fonctions et la syntaxe sont conçus pour les utiliser comme de vrai arrays en camouflant potentiellement les clés tout le long de la manipulation. Il faudra tout de même faire attention car certaines fonctions comme `array_filter` ne font pas le nécessaire et il faudra garder cela en tête afin de ne pas être surpris.

Je ne les ai pas testé mais il y a aussi les fonctions de tri qui peuvent changer l'ordre des valeurs, dans ce cas cependant c'est le choix de la fonction et non pas la nature de l'array qui déterminera ou non la réassignation des clés.

Donc les arrays php sont-ils des arrays ? Techniquement non, mais on peut faire comme si.