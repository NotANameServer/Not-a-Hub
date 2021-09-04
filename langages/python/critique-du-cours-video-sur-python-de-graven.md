# Critique du cours vidéo sur Python de Graven

Le cours intitulé "Apprendre le Python" est un cours proposé sur la chaîne YouTube Gravenilvectuto. Le cours se présente
comme un cours pour apprendre les fondamentaux du langage de programmation Python. Il est constitué de 9 vidéos sur le
langage d'une moyenne de 13 minutes et d'une vidéo sur la bibliothèque Tkinter de 40 minutes.

Avant tout chose, je (Julien -Dr Lazor- Castiaux) n'ai aucun grief contre Lorenzo, le vidéaste auteur de ce cours. La
qualité visuelle des vidéos est supérieure à ce que l'on trouve d'ordinaire, le rythme est correctement soutenu et les
exemples sont bien choisis. Les critiques de ce billet ne portent que sur le coté technique, le code source et les
explications.

## Les défauts du cours

### Épisode 1 - Introduction

Contrairement à ce qui est présenté dans la vidéo, un IDE (environnement de développement intégré) n'est
pas *nécessaire* pour développer. Il est d'ailleurs plus commun de croiser des développeurs Python qui utilisent le
combo éditeur de texte et terminal du fait de la légèreté du langage. [J'ai écrit un billet à ce sujet]
(https://docs.drlazor.be/python_ide.md).

L'ensemble des vidéos sera capturé dans cet environnement. On peut regretter que le vidéaste ne désactive pas les
différents linters et correcteurs orthographiques. Les démonstrations sont sans-cesse interrompues par myriade de
pop-up de conseil et les différents mots français sont régulièrement soulignés inutilement par le correcteur
orthographique.

Lors de l'installation de Python, l'attention du téléspectateur n'est pas attirée sur l'option "Add Python to PATH", il
s'agit d'une case à cocher qui rend accessible les programmes `python`, `py` et `pip` via la ligne de commande. Les
débutants ne savent généralement pas comment changer les variables d'environnement sur Windows et se plaignent de ne
pas réussir à lancer Python car `'python' n’est pas reconnu en tant que commande interne ou externe, un programme
exécutable ou un fichier de commandes.`.

Le tout premier bout de code montré à l'écran est le suivant :

```python
if __name__ == "__main__":
    print("Hello world")
```

Si il est commun de voir un `if __name__ == "__main__"` dans les projets Python, il n'est pas nécessaire et ne présente
un intérêt qu'au moment où les modules sont introduits. Il aurait été plus judicieux de ne pas l'introduire pour ne pas
rajouter de la complexité inutile.

Le dernier point sera heureusement rectifié dans deux vidéos.

### Épisode 2 - Variables

L'épisode est bon dans l'ensemble.

Je regrette néanmoins que la fonction `type()` n'ait pas été introduite, elle aurait permis de construire la notion de
type autrement que par la coloration syntaxique dans pycharm.

Je regrette également que la fonction `print` n'ait pas été utilisé correctement. La fonction peut prendre plusieurs
arguments qui seront tous castés en string et concaténés avec un espace. La solution proposée est de passer via le type
`str` pour convertir le nombre en chaîne de caractères.

Il aurait été judicieux de présenter ces types plus tôt, à savoir les types `int()`, `str()`, `float()` et `bool()`, et
de montrer qu'il peuvent être utilisés pour convertir les types entre eux. Les explications de la conversion en booléen
auraient par exemple pu servir de fondation pour l'épisode sur les conditions.

La fonction `format` sera présentée dans la vidéo suivante pour faciliter l'insertion de données dans les chaînes de
caractères.

### Épisode 3 - Conditions

Il existe une [syntaxe dédiée](https://www.python.org/dev/peps/pep-0308/) pour les ternaires depuis Python 2.5(sortie en
2006). La syntaxe est la suivante :

```python
x = true_value if condition else false_value
```

L'exemple d'expression ternaire présenté dans la vidéo, en plus d'être difficile à lire et obsolète, est faux. Le code
montré réalise un accès dans un tuple littéral. Cet accès est possible car le tuple possède deux éléments accessibles
aux indices 0 et 1 et que les deux valeurs booléenes ont un équivalent entier : 0 pour False, 1 pour True. Il est dit
dans la vidéo que le premier élément sera renvoyé si l'expression est vraie, or c'est le second qui sera renvoyé.

### Épisode 4 - Listes

Si l'ensemble des opérations présentées sur les listes sont correctes, l'attention quant à la complexité de ces
opérations n'est pas attiré. Bon nombre d'opérations (`del`, `insert`, `remove`) sont en complexité linéaire et non pas
constante. Utiliser ces opérations doit donc se faire avec parcimonie.

Pour récupérer le dernier élément d'une liste, la syntaxe `len(online_players) - 1` est présentée. Cette syntaxe, bien
que correcte, est inutilement verbeuse. Python est en fait capable de directement indexer en partant de la fin en
fournissant un indice négatif.

La vidéo présente la bibliothèque `statistics` pour calculer la moyenne d'une liste. Cette opération est en fait
facilement réalisable au moyen des fonctions `sum` et `len`.

Les listes seront d'ailleurs les seules structures de données présentées dans la vidéo, pas un mot sur les
dictionnaires, les sets ou la bibliothèque collections.

### Épisode 5 - Boucles

Le `for` traditionnellement utilisé dans les langages comme C, Java (`for (int x = 0; x < 5; x++)`) n'existe pas en
Python. Python n'est capable d'itérer que sur des objets itérables (ceux qui définissent les méthodes magiques
`__iter__` ou/et `__next__`). `range` est un de ces objets, bien qu'à l'utilisation il permet de simuler le `for`
classique, il n'en reste pas moins un objet qui implémente ces deux méthodes.

### Épisode 6 - Fonctions

Tout de suite après avoir montré comment définir et appeler des fonctions, l'auteur introduit les variables globales.
Les variables globales font partie des techniques appelées de *mémoire partagée*, un ensemble de la mémoire qui est
accessible et qui peut être modifié par plusieurs entités à la fois, ici les fonctions. Ces techniques sont connues
pour mener à des programmes qui sont difficiles à maintenir, qui présentent plus de bug et qui empêchent l'exécution
parallèle. Il est dangereux d'introduire ce mécanisme et on lui préférera systématiquement les fonctions
paramétriques.

En programmation orientée objet, lorsqu'une fonction nécessite un contexte pour fonctionner, on préférera utiliser un
objet pour sauvegarder ce contexte et écrire une *méthode*.

L'auteur se trompe lorsqu'il dit qu'il est nécessaire de marquer les variables globales comme globales pour pouvoir y
accéder. Il n'y a aucun problème à accéder en *lecture* (affichage, utilisation) aux variables définies dans le
contexte global. Ce mot clé n'est nécessaire que lorsqu'on *modifie* (affectation) les variables globales.

### Épisode 7 - Objets

La vidéo est d'une très grande qualité visuelle, les animations sont réussies, les exemples sont bien choisis et le tout
est correctement dynamique. En bref l'auteur réussi à expliquer le mécanisme de l'orienté objet dans une vidéo de
seulement 20 minutes, chapeau l'artiste !

Cependant, les bonnes pratiques de développement Python contrastent avec les bonnes pratiques d'autres langages de
programmation orientée-objet comme Java, C# ou PHP. En Python, la notion d'accessibilité des variables n'existe pas,
pas de mot clé `public` ou `private` pour définir la visibilité des attributs ou des méthodes. En réalité il s'agit
d'un choix d'implémentation, en Python on accédera directement à l'attribut tant en lecture qu'en écriture sans passer
par des méthodes `get_xyz()` ou `set_xyz()`. Si exécuter une fonction est nécessaire pour effectuer en traitement avant
de renvoyer une valeur, on préférera utiliser une propriété.

### Épisodes suivants

Les épisodes 8, 9 et 10 ne présentent pas de problème significatif.

## Discussion

### Structure de données

Les seules structures de données présentées dans le cours sont les listes et les objets. Python est un langage très
riche qui définit une abondance de structures de données qu'il est nécessaire de connaître et de savoir exploiter.

Un ensemble mathématique est une structure de données où les éléments sont ou ne sont pas présents. D'un point de vue
informatique, ils peuvent être considérés comme des listes non-ordonnées sans doublons. Ils sont implémentés en Python
via l'objet `set`.

Un dictionnaire est un livre qui associe chaque mot d'une langue à une définition. Il existe aussi des dictionnaires de
traduction où chaque mot d'une langue est associé au même mot dans une autre langue. En informatique, un dictionnaire
(aussi appelé tableau associatif ou *map*) est une structure de données qui associe un élément quelconque à un autre
élément quelconque. Ils sont implémentés en Python via l'objet `dict`. Les dictionnaires de base ne sont pas forcément
triés (avant Python 3.7), leur équivalent trié est implémenté via `collections.OrderedDict`.

Un multi-ensemble mathématique est un ensemble où les éléments peuvent exister plusieurs fois. En informatique ils sont
généralement implémentés comme un dictionnaire qui associe chaque élément au nombre de fois où il existe. En Python ils
sont implémentés via `collections.Counter`.

Une file ou une queue comme une file à la caisse est une autre structure de données où on ajoute des éléments d'un côté
et où on retire les éléments depuis l'autre côté. Si ces opérations sont possible sur des listes classiques, ces
opérations sont néanmoins non-optimisées. La structure optimisée pour gérer des files existe via l'objet
`collections.deque`.

Les bibliothèques `collections`, `queue`, `bisect` et `heapq` regorgent d'autres structures de données qui ne sont pas
reprises ici.

### Scope Python et variables globales

Ce qu'on appelle le *scope* est le niveau d'accessibilité des variables, c'est-à-dire quand et comment les variables du
programme sont accessibles.

Lorsque Python tente d'accéder à une variable *en lecture*, il va consulter le scope de la fonction : il commence par
consulter les variables locales à la fonction. S'il ne la trouve pas, il va consulter le scope de la fonction
supérieure et ainsi de suite jusqu'à arriver au scope dit *global* qui correspond à la racine du module. Si la variable
n'a été trouvée dans aucun scope, une erreur `NameError` sera remontée à l'utilisateur.

Lorsque Python tente d'accéder à une variable *en écriture*, il ne consulte *que* les variables locales, si la variable
n'existe pas elle sera créée dans les variables locales *même si* elle existait dans un scope supérieur. Pour pouvoir
modifier une variable d'un scope supérieur il est nécessaire d'utiliser les mots clés `global` ou `nonlocal`.

Si ce comportement est celui par défaut c'est qu'il est déconseillé de modifier les variables définies en dehors de sa
propre fonction. En effet, pour un programme conséquent, il devient difficile de déterminer quels sont les fonctions
qui modifient une variable, le développeur n'a pas d'autre solution que de scanner l'ensemble du programme pour
déterminer quelle fonction lit / écrit cette variable ce qui pose des problèmes quant à la compréhension du programme
en général.

Un autre problème survient lorsqu'on souhaite paralléliser un traitement sur plusieurs processeurs. Si un processeur lit
le contenu d'une variable globale en même temps qu'un autre processeur en change son contenu, on se retrouve dans une
situation où *l'on ne sait pas* ce qui a été lu. La lecture a-t-elle eu lieu avant la modification ? Après ? Ou pire...
Pendant ?

Ces problèmes ne se produisent pas lorsqu'on utilise une stratégie d'implémentation claire ou l'utilisation des
variables est clairement définie comme pour les fonctions paramétriques ou les objets.

### Visibilité des attributs et des méthodes

La visibilité en orienté objet est une notion qui permet de contrôler *qui* a accès (en lecture, en écriture ou en
exécution) aux attributs et aux méthodes d'un objet. Cette notion est implémentée dans nombre de langages orientés
objet statiques comme Java, C# et C++. Lorsqu'un attribut est déclaré avec `private` elle n'est accessible que par
l'objet courant, il en va de même pour les méthodes. Au contraire lorsqu'un attribut/une méthode est déclaré public,
tout le monde peut y accéder.

Cette notion de visibilité est absente de Python qui préfère *faire confiance aux développeurs* qu'ils n'aillent pas
toucher ce qu'ils ne devraient pas. Ainsi la seule notion qui sépare les attributs, propriétés et méthodes publiques de
celles considérées comme "privées" est une convention d'écriture. On préfixera ce qui est privé par un underscore. Le
développeur est libre de n'en faire qu'à sa tête de tout de même les utiliser même si c'est déconseillé.

Dans l'industrie il n'y a au final pas de problème à ce que le langage ne définisse pas lui-même de niveau de
visibilité. Une équipe constituée de développeurs compétents, que ce soit en Python ou dans un autre langage, est
capable de faire la part des choses. Il s'avère même parfois de meilleur goût de ne pas respecter cette convention de
visibilité et de tout de même utiliser une variable / méthode "privée".

### Accesseurs et mutateurs

Dans la même lignée qu'il n'y a pas de notion de visibilité en Python, les pratiques de développement Python conseillent
de directement modifier les attributs des objets sans passer par des méthodes de contrôle. Dit autrement, l'utilisation
systématique d'accesseurs (*getters*) et de mutateurs (*setters*) est déconseillé.

Dans l'industrie ceci ne pose en réalité aucun souci, les développeurs qui définissent les interfaces objets sont
généralement ceux qui les utiliseront ou qui seront chargés de relire le code des autres développeurs.

Cependant, il est parfois nécessaire d'effectuer des traitements à l'accès ou à la modification des attributs. Pour ce
faire, Python a opté pour les propriétés. Une propriété s'utilise comme une variable normale, on récupère la valeur en
donnant uniquement le nom de la propriété et on modifie sa valeur comme une simple affectation. La différence est qu'au
lieu d'être directement accédée ou modifiée, c'est une fonction de traitement qui sera chargée de renvoyer / modifier
la variable.

Via ce mécanisme, il est possible de laisser un attribut "public" (sans underscore en préfixe) et s'il s'avère à
l'utilisation qu'une fonction de traitement est nécessaire, il suffit de préfixer l'attribut pour qu'il soit "privé" et
de définir au niveau de la classe une propriété du même nom que l'ancien attribut public. Le code qui exploitait
l'attribut exploite maintenant la propriété indifféremment.

### Cours de Java... en Python...

Si la qualité visuelle des vidéos et la dynamique du cours sont supérieures à bon nombre de cours en ligne (gratuit et
payant), le côté technique est quant à lui approximatif. L'approche pédagogique de l'auteur souffre de nombreux biais
qui sont communs aux développeurs Java qui s'essaient au langage Python.

Plusieurs arguments penchent en cette faveur :

* Il est commun d'utiliser un IDE complet pour développer en Java, pas en Python ;
* Il y a conversion automatique des entiers vers les chaînes de caractère en Java, en Python elles doivent être
  explicites ;
* L'expression `condition ? true_value : false_value` est une expression ternaire en Java, l'expression Python `
  (false_value, true_value)[condition]` y ressemble fâcheusement (expressions finales d'un côté, condition de l'autre)
  mais n'est pas une expression ternaire en Python ;
* Le *for* classique n'existe pas en Python, il est simulé par l'objet `range` mais il n'existe bien en Python que ce
  que les développeurs Java appellent le *for each* ;
* Les bonnes pratiques Java dictent qu'il est important de définir des méthodes dédiées (*getters* et *setters*) pour
  manipuler les attributs d'un objet, les bonnes pratiques Python dictent de modifier directement l'attribut ou de
  passer par des propriétés.

## Conclusion

Le cours est gangrené par les habitudes de développeur Java de l'auteur. Certains concepts essentiels dans le
développement Python sont complètements omis comme les dictionnaires, les sets, les générateurs ou la bibliothèque
standard. Certains sont approximatifs comme les conditions ou les boucles. Les derniers introduisent des concepts qui
vont à l'encontre des bonnes pratiques de développement en Python comme les fonctions ou les objets.

Graven est certainement un très bon développeur Java !
