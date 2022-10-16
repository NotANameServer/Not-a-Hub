# Les idées reçues sur C

Le C est un langage de programmation très répandu. Il a été utilisé, enseigné
et éprouvé pendant des années. Cependant, rien de tout cela n'est parfait, et
même parfois bien en dessous de ce que l'on pourrait attendre aujourd'hui. Pour
autant énormément de fausses croyances circulent sur le langage, croyances qui
sont parfois utilisées pour justifier le fait de débuter par C. Pour essayer
d'y voir un peu plus clair dans tout ça, cet article propose de passer en revue
quelques une de ces idées reçues. Le but est de donner une vision globale de
tout cela, aussi j'essaierai au maximum de **ne pas** rentrer trop dans les
détails.

## Le C est proche de la machine

Cette idée reçue est très probablement la plus répandue de toutes. Ce qu'elle
nous dit en substance, c'est que C est un "langage de bas-niveau". Regardons
cela de plus près, et en particulier, demandons-nous ce que veut dire "être
proche de la machine" et si C correspond bien à cela.

Dans un système, on considère vulgairement que la pièce de logiciel de plus bas
niveau est le système d'exploitation (et on peut faire aussi le parallèle avec
les logiciels que l'on exécute sur tout ce qui est microcontrôleurs par
exemple). Ce logiciel a principalement pour rôle de faire le pont entre le
matériel et les logiciels de l'utilisateur (c'est plus compliqué, mais ça nous
suffira ici). Le système d'exploitation pilote donc le matériel. Mais quel
matériel ? Et quel est le rapport avec C ?

Le matériel concerné est basiquement le processeur, la mémoire et les autres
composants de la machine. Cependant, tout n'est pas possible. En particulier,
sur les ordinateurs modernes, même une pièce aussi basique que le processeur
est aujourd'hui un objet d'ingénierie complexe qui fait intervenir de nombreux
sous-composants. Même le système d'exploitation n'a finalement que peu de
contrôle sur tout ce qui se passe au niveau du processeur. En particulier, le
contrôle des caches du processeur, des unités de calculs, etc, n'est pas
directement accessible. Le peu de contrôle que l'on peut obtenir a ce sujet
n'est que très indirect : c'est en observant la réaction du système à certaines
manières de programmer que l'on déduit comment on *devrait (semble-t-il)* écrire
le programme pour être efficace. Mais nous n'avons aucune garantie que cela
restera toujours le cas. Un certain nombre de ces "manières d'écrire" sont par
ailleurs renseignées dans les heuristiques des compilateurs pour les aider à
optimiser.

Quel est maintenant le rapport avec C ? Et, bien tristement, il y en a assez peu.
En effet, bien que C soit très utilisé pour écrire des systèmes d'exploitation,
**rien** dans la définition du langage (la norme C) ne parle de tout cela. Par
exemple, dans [la norme C11](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1548.pdf),
la section 5.1.2.3 nous dit :

> The semantic descriptions in this International Standard describe the behavior
> of an **abstract** machine in which issues of optimization are irrelevant.

Par ailleurs, la section 5.1.2.4 décrit à très haut niveau le comportement du
modèle *multi-thread* du langage. Le lien entre la machine **abstraite** du C et
le matériel est laissé à charge des implémentations. **Cela ne fait pas partie
de la définition du langage C**. Une conséquence de cela est qu'écrire du code
de bas niveau n'est pas fondamentalement écrire en langage C "pur", c'est écrire
en langage C auquel est accolé toute la documentation du système cible et de la
chaîne de compilation utilisée, ce qui sort largement du cadre du langage.

Cette absence des questions de matériel et de bas niveau dans la norme est
*très* importante. Loin d'être un défaut, c'est justement ce qui permet aux
implémentations de fournir des interfaces raisonnablement efficaces pour le
développeur à plus haut niveau et qui laisse un maximum de liberté sur le design
du matériel et de l'implémentation.

La conséquence de cela est que C n'est pas un langage proche de la machine.
Certaines variantes (donc embarquant aussi la définition du système cible et un
modèle de compilateur) l'ont peut-être été historiquement, mais ce n'est plus le
cas pour les systèmes modernes. On peut même se demander si la notion de langage
(*general purpose*) de bas niveau a encore un sens aujourd'hui. Pour plus de
détails sur ce sujet, je vous conseille
[cet article](https://queue.acm.org/detail.cfm?id=3212479).

### En apprenant C, j'apprends la programmation bas niveau

Une variante de cette idée reçue est que C nous apprend la programmation de bas
niveau. Il y a un fond de vérité là-dedans, à condition d'en changer un peu la
formulation. Le C *peut être utilisé comme outil* pour apprendre la programmation
de bas niveau. Apprendre la programmation de bas niveau consiste précisément à
écrire du code de bas niveau. Or si les cours de programmation de bas niveau
utilisent très souvent C pour la pratique, la vaste majorité des cours pour
apprendre la programmation C ne sont pas des cours de programmation bas niveau.

Tout au plus, les cours de C descendront jusqu'à la différence entre la pile et
le tas (*stack* et *heap*). Du côté du tas, seules les fonctions d'allocation et
libération de la bibliothèque standard de C seront présentées et utilisées.
La notion d'adresse mémoire *au sens C du terme* sera présentée et utilisée. Ce
ne sont pas des notions de bas niveau. Ces notions *cachent* justement tout ce
qui doit être fait au niveau de la machine et du système d'exploitation pour
arriver à ce résultat en présentant une vision conforme à la machine
**abstraite** du C. Il y a littéralement des milliers de lignes de code qui font
ce travail du côté de l'implémentation, on est *loin* de la machine.

En revanche, C peut effectivement être utilisé comme support pour apprendre la
programmation de bas niveau. Par exemple, pour illustrer les notions apprises
pendant un tel cours. Mais le focus de ce cours serait alors l'apprentissage de
la programmation système ou bas niveau, pas l'apprentissage du langage C.

### En comprenant la machine, je comprends ce qui se passe en C

Une autre variante de cette idée reçue est l'idée inverse : connaître le bas
niveau permettrait de facilement comprendre ce qui se passe dans un programme
écrit en langage C. À nouveau, s'il y a un fond de vérité derrière cette idée,
il ne faut pas du tout la prendre pour argent comptant, car l'implémentation est
à nouveau prête à nous donner tort.

En effet, nous avons déjà insisté sur l'importance de l'implémentation de la
machine abstraite comme un facteur nous cachant le comportement réel du
matériel. Mais l'implémentation peut aussi faire l'inverse : exploiter le
comportement voulu par la machine abstraite pour demander à la machine réelle
des choses que nous n'avions pas prévues. Prenons le programme suivant :

```c
#include <limits.h>
#include <stdio.h>

void function(int x){
  int old = x ;
  x++ ;
  printf("X is: %d\n", x);
  if(x > old){
    printf("%d > %d\n", x, old);
  }
}

int main(void){
  int x = INT_MAX ;
  function(x);
}
```

Si l'on compile et exécute ce programme, nous obtenons le résultat suivant :

```sh
$ gcc ub-overflow.c && ./a.out
X is: -2147483648
```

Et par la connaissance du fonctionnement du
[complément à deux](https://fr.wikipedia.org/wiki/Compl%C3%A9ment_%C3%A0_deux)
utilisé sur notre processeur, nous pouvons avoir le raisonnement suivant : *mais
oui, c'est évident, mon entier déborde et revient donc à `INT_MIN`, cet entier
est inférieur à `INT_MAX` et donc le second message ne s'affiche pas*.

Sauf que si l'on demande au compilateur d'optimiser (et ici avec les
optimisations les moins agressives par exemple) :

```sh
$ gcc ub-overflow.c -O1 && ./a.out
X is: -2147483648
-2147483648 > 2147483647
```

Le résultat est tout autre. La raison est que la très vaste majorité du temps,
comprendre le comportement de la machine ou du système n'est absolument pas
suffisant pour comprendre ce que fait un code ... surtout quand il est invalide.

Le code ci-dessus est invalide. En C, le débordement d'un entier signé est un
comportement indéterminé, même quand sur la machine, c'est parfaitement
déterminé. Le compilateur est en droit de *supposer* que le code ne contient pas
de comportement indéterminé *au sens de la norme C*. Par exemple ici, le code
incrémente `x`, donc `x` est *nécessairement* supérieur à `old` après cela (il
n'y a pas de débordement, c'est interdit). En conséquence, la branche est
toujours prise : pas besoin de vérifier la condition. Le compilateur supprime
donc ce `if` inutile, et ne laisse que l'affichage qui lit tout de même les
valeurs réelles de `x` et `old`.

Naturellement, des outils existent pour détecter ce genre de problèmes, mais
nous reviendrons plus tard sur ce sujet.

## Si je comprends C, je comprendrai tous les autres langages

Généralement, cette affirmation est agrémentée d'une autre, qui nous dit que
C est le père de tous les langages de programmation. Et donc si on connaît ce
langage, apprendre ses descendants (tous les langages), c'est facile. Non ?

Commençons par une mauvaise métaphore (il n'y a pas de raison que je n'ai pas le
droit de faire aussi des affirmations fumeuses) : nous n'avons pas eu besoin
d'apprendre toutes les variantes du latin, puis du vieux français pour ensuite
apprendre le français d'aujourd'hui. Pourquoi en serait-il différent pour un
langage de programmation ? L'argument est peut-être faible, mais pas plus que
l'argument de base.

### Le C est le père de tous les langages de programmation

D'une part, C n'est pas arrivé de nulle part. Il a été influencé
par d'autres langages, notamment [Fortran](https://fr.wikipedia.org/wiki/Fortran)
qui est toujours utilisé aujourd'hui dans le domaine scientifique.

D'autre part, avant l'existence de C (et également dans les mêmes années),
d'autres langages ont été créés, et ceux-ci ont eu une très forte influence
*aussi* sur les langages de programmation utilisés aujourd'hui. On notera
[Lisp](https://fr.wikipedia.org/wiki/Lisp_(langage)) dont certains dialectes
comme [Common Lisp](https://fr.wikipedia.org/wiki/Common_Lisp) ou
[Closure](https://fr.wikipedia.org/wiki/Clojure) sont encore en usage, mais qui
a également influencé [Haskell](https://fr.wikipedia.org/wiki/Haskell), qui
n'est pas influencé par C. Ou encore [Simula](https://fr.wikipedia.org/wiki/Simula)
qui a influencé [Smalltalk](https://fr.wikipedia.org/wiki/Smalltalk), ce dernier
ayant eu un impact majeur sur presque tous les langages orientés objets par la
suite. On peut citer les langages de la famille
[ML](https://fr.wikipedia.org/wiki/ML_(langage)), qui ont amené à
[OCaml](https://fr.wikipedia.org/wiki/OCaml) que C n'a pas influencé et qui est
une des influences principales de [Rust](https://fr.wikipedia.org/wiki/Rust_(langage)).
Les familles Lisp et ML ont aujourd'hui un impact fort sur les langages de
programmation plus *mainstream* qui embarquent de plus en plus de fonctionnalités
qui viennent de là. Finalement, même sur les langages qui sont directement
influencés par C, les ressemblances se limitent surtout à des éléments de
syntaxes et la sémantique de ce sous-ensemble de syntaxes. Et de manière très
générale, l'ensemble des langages de programmation présents aujourd'hui sont
beaucoup plus influencés par les usages industriels que l'on en a fait et par la
recherche sur le sujet.

### Et pour ce qui est de comprendre ses descendants ?

Il faut bien distinguer ce qui est :
- commun à la majorité des langages de programmation,
- spécifique à un langage de programmation.

Pour ce qui est du premier point, oui bien sûr qu'une fois ces éléments bien
compris, ils seront bien plus simples à répliquer lors de l'apprentissage d'un
nouveau langage de programmation. Mais ce n'est absolument pas spécifique à C :
les mêmes syntaxes aurait pu être assimilées également dans n'importe quel autre
langage avec le même effet.

Viennent ensuite les éléments qui sont spécifiques au langage, et sur ce point,
non, connaître les spécificités de C n'est pas une aide pour apprendre un autre
langage dans lequel ces spécificités n'existent pas, ou sont différentes, ou
pire, existent, sont similaires, mais sont considérées comme de mauvaises
pratiques.

Pour un exemple de ce dernier cas, l'allocation dynamique manuelle de mémoire
qui est évidemment nécessaire en C, existe en C++, où elle est considérée comme
un *code-smell* (à raison) :
[Cpp Core Guidelines - ES.60](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#es60-avoid-new-and-delete-outside-resource-management-functions).

En bref, C n'est pas différent des autres langages en ce qui concerne la capacité
à en apprendre d'autres par la suite. Pour les éléments de base, il a le même
effet, pour ce qui est spécifique, il faudra être tout aussi vigilant qu'avec
un autre langage.

## C est un très bon langage pour apprendre la programmation

Le précédent point nous amène au fait que C serait un très bon langage pour
apprendre la programmation. C'est de loin la question la plus complexe. La
raison pour cela est que d'un côté, nous avons des langages qui sont conçus pour
apprendre, mais ne sont pas utilisés pour l'industrie (ce qui est normal), et
inversement des langages qui sont utilisés dans l'industrie, mais qui, à raison,
ne sont pas conçus pour apprendre. Il n'y a pas de langage parfait pour
apprendre donc je ne vais clairement pas donner une réponse définitive. Mais
je vais lister ce qui, selon moi, fait de C un mauvais candidat pour un
*premier pas* dans la programmation.

Demandons-nous d'abord ce qui importe pour qu'un langage soit un bon candidat
pour débuter. À nouveau, il n'y a pas de réponse définitive à cette question.
On peut tout de même dégager un ensemble de caractéristiques qui semblent assez
admises, le langage doit (par ordre subjectif du plus au moins important) :
- embarquer les structures les plus communes en programmation,
- permettre à l'apprenant de se rendre compte de ses erreurs,
- rester raisonnablement simple à utiliser,
- avoir un outillage raisonnablement simple,
- avoir une bibliothèque de ressources de bonne qualité accessible.

C remplit le premier objectif comme nous l'avons déjà dit précédemment. La
dernière caractéristique est aussi remplie, notamment parce qu'il existe une
quantité incroyable de ressources à son sujet, produites pendant des décennies.
Cependant, c'est aussi à double tranchant : il y a du très bon comme du très
mauvais, et il est difficile (pour ne pas dire impossible) pour un débutant de
faire seul le travail de séparer le bon grain de l'ivraie dans cette masse
d'information.

### Le langage C est simple, donc il est simple de l'utiliser

Une idée reçue reliée et relativement commune sur le C est que, puisque le
langage est simple, il est simple à utiliser. Si le langage C est effectivement
simple (en fait, on pourrait même dire "simpliste", il y a une vraie volonté
d'embarquer peu de choses), cela ne veut pas dire qu'il est simple à utiliser :
pour toute fonctionnalité absente du langage, si l'on en a besoin, on doit faire
manuellement le même travail (ou faire l'effort d'intégrer une bibliothèque
spécifique pour cela). Prenons un exemple : la plupart des langages embarquent
des structures de données dans leur bibliothèque standard. Réimplémenter ces
structures *n'est pas* simple. C'est un premier point, mais dans le cadre d'un
cours pour débutant, ce n'est pas le plus important.

Même les éléments les plus basiques du langage C ne sont pas simples à utiliser.
Une fonctionnalité aussi basique que la saisie d'une valeur entière n'est pas si
simple :
```c
#include <stdio.h>

int main(void){
  int x, err ;
  do {
    err = scanf("%d", &x);
    if(err != 1) scanf ("%*[^\n]");
  } while(err != 1);

  printf("Input was: %d\n", x);
}
```

Naturellement, les cours ont tendance à simplifier tout cela en :

```c
#include <stdio.h>

int main(void){
  int x ;
  scanf("%d", &x);
  printf("Input was: %d\n", x);
}
```

Mais selon l'implémentation, cela pourrait avoir des comportements très étranges
en cas d'erreur de saisie, qu'un débutant pourrait avoir grand-peine à
comprendre. Au contact de débutants, on constate d'ailleurs que la manipulation
des flux pose énormément de problèmes. Notamment pour savoir quand le flux est
dans quel état. Et les cours sont généralement très évasifs à ce sujet parce que
... ce *n'est pas* simple. Les débutants se cassent donc les dents très souvent
sur ce problème au cours de leur apprentissage alors que ce problème n'a
**aucun** intérêt d'un point de vue pédagogique. C'est de la pure considération
technique associée à C.

Un autre exemple classique est la distinction entre pointeur et tableau qu'aucun
débutant ne saisit dès la première itération "cours + exercices", d'autant moins
quand le cours fait volontairement l'amalgame entre les deux, ce qui est commun.
Il leur faut généralement plusieurs itérations et même plusieurs retours sur
cette partie après avoir continué le cours parce que ce n'est pas encore
compris. La distinction est ici difficile à faire pour le débutant parce que les
conversions implicites de l'un à l'autre sont systématiques dans beaucoup de
cas, c'est une spécificité pénible du C qui n'a aucun intérêt pédagogique.

Un autre exemple est la gestion des erreurs, qui est traitée de manière très
lapidaire dans la majorité des cours de C. Avec comme conséquence que les
débutants écrivent du code qui ne contient presque aucun traitement des erreurs.
Sujet qui, par ailleurs, est très important en programmation. La raison de cela
est que la gestion des erreurs en C est assez pénible et donc beaucoup de cours
font l'impasse dessus pour ne pas perdre le débutant.

Les fonctionnalités de base du langage ne sont donc déjà pas si simples à
utiliser et pire encore, il est très facile de *mal* les utiliser et donc de
produire du code contenant des bugs. Que l'on soit bien d'accord, il est tout
à fait normal d'écrire du code contenant des bugs, trouver et corriger les bugs
est une part importante de notre métier. Cependant, en C, une catégorie de bugs
est particulièrement importante : ce sont les comportements indéterminés. La
norme C liste **presque 200 cas** de mauvaises utilisations du langage pouvant
amener à ce type de comportements (cf. Annexe J dans la norme C11 par exemple).
Et la vaste majorité de ces utilisations ne sont pas des cas tordus qui
n'arrivent jamais, ce sont des exemples extrêmement communs. La présence d'un
tel comportement dans le code induit que le programme va avoir un comportement
qui est *imprévisible*. Le programme ne va pas forcément faire une erreur, on ne
sait pas *a priori* ce qu'il va faire.

Programmer en C *demande* donc une discipline de fer.

### Le C apprend la discipline

Ce qui nous amène à l'idée reçue que C nous apprend la discipline. À nouveau,
c'est assez faux. Bien programmer en C *demande* de la discipline, mais rien
dans le langage n'est présent pour imposer cette discipline. Ce qui nous amène
au point qui à mon sens pose le plus de problème pour en faire un langage pour
débutant : il est très facile pour un débutant d'écrire un code qui contient des
comportements indéterminés, qui sont très difficiles à détecter sans une
très bonne méthodologie de vérification.

Détecter les comportements indéterminés nécessite au minimum d'apprendre au
débutant à ajouter une foultitude d'options à ses outils, d'ajouter de nombreux
outils à son environnement de travail, de lui apprendre immédiatement à écrire
plein de tests, donc de lui apprendre immédiatement des méthodologies pour bien
tester ... Si l'on ne fait pas cela, il est **certain** que le débutant écrira
des codes qui contiennent des nombreuses erreurs qu'il ne pourra jamais corriger
alors que c'est une phase extrêmement importante de son apprentissage. Or,
rappelons qu'on parle d'une personne qui n'a *jamais* programmé, une personne
qui ne connaît aucun de ces outils, et pour qui écrire une boucle demande un
effort intellectuel significatif (puisque c'est tout nouveau).

Alors certes, sans écrire de tests, il est aussi certain qu'un débutant dans un
autre langage pourra écrire des codes qui contiennent des erreurs non détectées.
En C, la différence est que *même en présence de ces tests*, sans une bonne
configuration de l'ensemble de son environnement, les problèmes pourraient
rester invisibles au débutant. Et sans un apprentissage de l'utilisation
d'outils d'analyse et de debug, comprendre les bugs sera très difficile. Par
exemple, la "bonne vieille méthode du `print`" n'est pas utilisable en pratique
en C, car ces affichages peuvent changer le comportement d'un programme qui
contient un comportement indéterminé.

### Pour conclure sur le C comme premier langage

Si le C embarque effectivement les structures les plus communes en programmation
et beaucoup de ressources sont disponibles à son sujet, il faut garder en tête
que ces ressources sont de qualité très variable. Le langage en lui-même est
simpliste, mais contient de nombreux cas tordus, et il n'est pas simple à
manipuler de manière correcte. Il est par ailleurs difficile pour un apprenant
de détecter et corriger ses erreurs sans la présence d'un outillage très complet.

D'autres langages peuvent faire mieux. On citera notamment Python. Ou Ada, si
vous êtes allergique au typage dynamique. Ou Go si vous voulez quelque chose de
plus mainstream. Ou Java, modulo un peu d'huile de coude au démarrage pour
éjecter un peu de complexité. Ou OCaml si vous n'êtes pas inquiets que vos
débutants maudissent la syntaxe des autres langages ensuite.

## Avec C, on contrôle tout

Nous avons déjà vu que c'est plutôt faux, notamment dans un cours pour débutant.
Au-delà de cette considération, on peut également se demander s'il est bien
pertinent de tout contrôler : si on utilise un compilateur qui transforme
automatiquement notre code en code machine, c'est bien que l'on n'a pas envie de
contrôler cet aspect par exemple. Si on utilise les fonctions de la bibliothèque
standard du langage, c'est aussi parce qu'on s'en moque de contrôler ce qui se
passe dedans. De manière assez directe : on va contrôler ce que l'on a besoin de
contrôler et laisser le reste à des procédures plus automatiques ou à des
bibliothèques tierces. Par ailleurs, de nombreux langages permettent tout à fait
le même niveau de contrôle que ce que l'on peut obtenir en C, tout en ne
l'imposant pas (ce que ne fait pas toujours C), on pourra citer Rust, C++ ou Ada
notamment.

Par ailleurs, cette vision est assez naïve et ne prend pas en compte ce qu'est
un processus de développement réel. Le développement d'un logiciel demande du
temps. Du temps, on en a plus ou moins, et nos efforts vont se répartir de
manière différente en fonction de besoin et de l'outillage à notre disposition.
Pour pouvoir exercer le contrôle disponible dans notre langage, il faut que
le temps nous le permette. Or généralement, bien avant d'aller utiliser toutes
les possibilités que nous offre un langage, beaucoup d'autres tâches nous
attendent.

Avant de faire un code extrêmement rapide, il est déjà de bon ton de le faire
raisonnablement rapide déjà, et même en fait de le faire correct d'abord, et
même de le faire en fait. L'étape de développement en C est plus coûteuse que
dans beaucoup d'autres langages. Nous l'avons déjà dit plus tôt : C est
simpliste, il ne nous donne pas beaucoup de fonctionnalités, beaucoup de choses
vont nous demander plus d'efforts. Rendre le code correct n'est pas une tâche
facile non plus.

### Le C, c'est bien pour faire du code sécurisé

J'ai déjà pu croiser cette idée reçue, mais beaucoup moins souvent que les
autres, ce qui est plutôt une bonne chose, cela veut dire que la sensibilisation
sur le sujet fonctionne. Faire du code sécurisé en C, c'est **dur**. Cela
demande un outillage important et des bases de tests comme on en rencontre
rarement dans le monde du développement.

La principale raison de cela est liée partiellement liée aux comportements
indéterminés. Le moindre comportement indéterminé dans un code C est un risque
d'un point de vue sécurité. Nous l'avons vu, ces comportements n'entraînent pas
forcément des erreurs immédiatement visibles et détectables, ils peuvent
silencieusement introduire des failles critiques de sécurité (c'est par exemple
le cas des *buffer-overflows*, la hantise des développeurs C faisant du logiciel
sécurisé). Traquer et corriger ce type d'erreur demande du travail
supplémentaire, qui n'existerait pas dans un langage qui permet de limiter (et
parfois presque totalement régler) le problème des comportements indéterminés.

Une seconde raison est liée au côté simpliste de C. Comme réaliser la plupart
des actions du programme nécessite généralement plus de lignes de code, c'est
autant de risque supplémentaire de faire des erreurs et autant de temps
nécessaire en plus pour en faire la vérification, nécessitant donc plus de
tests et autres procédures de vérification. Les entreprises (ou autres acteurs)
capables d'encaisser ce coût supplémentaire de vérification ne courent pas les
rues.

Néanmoins, le C reste effectivement présent dans *certains* secteurs où l'on
attend une grande fiabilité. En revanche, la raison n'est pas que C permet
d'obtenir des garanties sur la fiabilité du code écrit avec facilement. Nous
reviendrons sur ce point plus tard.

### Le C donne du code performant

Une idée reçue reliée est que le C donne du code performant. Ce n'est pas
complètement faux, mais c'est plus compliqué que ça. Faire du code réellement
performant en C demande un effort de développement important (à nouveau).
C donne avant tout *du contrôle* sur les performances du code. Encore faut-il
exercer ce contrôle.

Sur des problèmes très simples tels que ceux présents dans les micro-benchmarks,
il est vrai que C tient généralement le haut du classement, talonné de très près
par C++ et Rust (avec des différences de 5% dans les pires cas). Pour un exemple
de ce type de comparaison, il y a [cet article](https://haslab.github.io/SAFER/scp21.pdf).
Seulement, le travail d'un développeur n'est pas d'écrire des programmes de
micro-benchmark. Sur des logiciels plus complexes, ces différences tendent
progressivement à s'effacer. Cela dépend des moyens disponibles pour travailler
sur l'optimisation du code (rappel : un projet sans contrainte de coût,
*ça n'existe pas*).

L'optimisation du code intervient après avoir réalisé et fiabilisé le code de
base (ce qui, nous l'avons vu, a un coût élevé en C). À partir de ce point, il
faut prendre le temps de faire les mesures nécessaires pour optimiser ce qui
doit l'être. Les premières phases d'optimisation interviennent généralement sur
le plan algorithmique. Ce type d'optimisation n'est pas spécifique au langage C,
il est possible d'en faire autant dans presque tous les langages. En revanche,
ce sont des nouveaux développements qui vont avoir les mêmes limitations que le
reste du développement en C en termes de coûts.

Une fois ces optimisations réalisées, à condition que les performances soient
encore insuffisantes, alors seulement, nous allons nous attarder sur les
optimisations liées à la bonne utilisation du matériel. Elles sont effectivement
relativement faciles d'accès en C, même si cela impose d'écrire du code qui est
très indirect dans sa manière de manipuler le comportement du matériel (par la
connaissance du comportement *habituel* du compilateur et du matériel, on peut
écrire du code qui va être bien optimisé par le compilateur et permettre une
réponse positive des différentes heuristiques des contrôleurs du processeur).
Notons que ces optimisations restent accessibles dans beaucoup de langages. C++
a les mêmes possibilités, Rust en a même des supplémentaires (liées à la
séparation de la mémoire) même si le compilateur bénéficie de moins d'années
d'améliorations. Beaucoup de langages permettent de partiellement répondre aux
mêmes types de besoin avec un peu moins de facilité d'accès (mais un coût de
développement moindre).

Donc oui, C permet d'écrire des morceaux de codes simples dont le temps
d'exécution est court. Mais sur de vrais problèmes, le coût d'optimisation
devient très rapidement prohibitif pour beaucoup de projets, surtout au regard
du coût de développement qui est déjà très élevé.

## C est populaire, c'est parce qu'il est très bien

Nous l'avons vu, C a une très longue histoire et il a été utilisé tôt sur des
projets qui ont perduré jusqu'à aujourd'hui. Il a également fait très tôt partie du paysage dans l'enseignement. Il y a donc une très forte raison
*historique* dans l'usage de C. À l'époque de sa création, les langages de
programmation *general-purpose* utilisés à grande échelle ne sont pas légions.
On voit bien comment l'inertie peut se mettre en place :
1. le langage est utilisé dans l'industrie,
1. donc on l'enseigne,
1. donc on a plein de nouveau développeurs qui peuvent travailler avec,
1. donc revenir à l'étape 1.

Au-delà de cela, on peut différencier deux aspects liés à cette histoire :
- la dette technique,
- le capital technique.

La dette technique est un élément important de la popularité de C. Il n'y a
généralement pas beaucoup de raisons qui peuvent pousser à réécrire
intégralement un logiciel depuis un langage vers un autre. Ce type de
réécriture demande un investissement colossal (qui plus est quand le logiciel
existe depuis longtemps), pour un gain qui en fonction du projet n'est parfois
qu'hypothétique : un logiciel avec un bon processus de vérification est
généralement très stable, l'impact du changement de langage ne serait pas
forcément rentable. Pour autant, la maintenance de ces logiciels doit être
assurée et éventuellement l'ajout de nouvelles fonctionnalités. La première
implique de continuer à développer en C, la seconde l'encourage fortement pour
ne pas payer la mise en place d'une interaction multilangage.

Toujours au rang d'une certaine forme de dette technique. Dans les domaines de
l'embarqué, les plateformes hardware exotiques sont plutôt communes. Ces
plateformes exotiques ont très généralement accès à un compilateur C
(principalement en réponse à la connaissance de C par les développeurs du
domaine) mais pas souvent pour d'autres langages. Dans cette situation, le
choix du langage est fait rapidement, mais pas très librement.

Ces éléments de dette technique représentent plutôt la raison désagréable qui
fait cette popularité.

À l'inverse, une raison plutôt rassurante de cette popularité est le capital
technique accumulé au fil des années. D'abord par la quantité de développeurs
experts du langage, mais également sur le plan de l'outillage. Tout d'abord sur
le sujet de la compilation, les compilateurs
([Clang](https://fr.wikipedia.org/wiki/Clang),
[GCC](https://fr.wikipedia.org/wiki/GNU_Compiler_Collection),
[MSVC](https://fr.wikipedia.org/wiki/Visual_C++) pour ne citer que les plus
gros) ont plusieurs dizaines d'années de travail de maturation. Ce sont des
logiciels bien testés et éprouvés avec globalement peu de problèmes sur du code
courant. On peut également citer
[CompCert](https://fr.wikipedia.org/wiki/CompCert) qui va encore plus loin
en proposant un compilateur dont la correction est prouvée formellement. Comme
le langage est (nous l'avons vu) un nid à pièges, de nombreux outils d'analyse
ont été développés au fil des années pour faciliter la mise au point du code.
Depuis les *warnings* de compilateurs, en passant par des outils d'analyse
statique *unsound* (comme [CodeSonar](https://fr.wikipedia.org/wiki/GrammaTech),
[CppCheck](https://fr.wikipedia.org/wiki/Cppcheck),
[PVS Studio](https://en.wikipedia.org/wiki/PVS-Studio), ...), ou encore des
outils d'instrumentation (comme [ASan](https://en.wikipedia.org/wiki/AddressSanitizer)),
des outils de debug (comme [GDB](https://fr.wikipedia.org/wiki/GNU_Debugger),
[Valgrind](https://fr.wikipedia.org/wiki/Valgrind), ...), les frameworks de test
(comme [CppUnit](https://en.wikipedia.org/wiki/CppUnit),
[GoogleTest](https://en.wikipedia.org/wiki/Google_Test), ...), jusqu'aux outils
de vérification formelle de code
(comme [Astrée](https://en.wikipedia.org/wiki/Astrée_(static_analysis)),
[Frama-C](https://en.wikipedia.org/wiki/Frama-C),
[Verifast](https://github.com/verifast/verifast), ...). Ces outils sont
aujourd'hui nombreux à avoir une très bonne maturité, sont bien compris du
monde industriel et avec une bonne méthode d'utilisation permettent (au prix
d'un très fort investissement en temps) d'améliorer significativement la qualité
des logiciels développés en C. Seulement, on est en droit de se demander quelle est la part
de ce travail qui est gratuite (ou presque) lorsque l'on travaille dans d'autres
langages.

Nous sommes donc bien loin d'un monde idyllique où le C serait tellement génial
que l'on devrait l'utiliser partout. Une part significative de la raison réelle
est surtout que parfois on est bien obligé de faire avec.

### C est très demandé, j'aurai plein de travail

Cette idée reçue est moins courante, cependant il me semble important de
revenir dessus. Si C est effectivement toujours utilisé, il ne représente plus
une part si significative du marché de l'emploi et se cantonne à des secteurs
d'activité qui sont aujourd'hui assez spécifiques (certains travaillant dur à
migrer vers d'autres technologies).

### La popularité de C dans des secteurs critiques

Nous l'avons dit plus tôt, certains secteurs, y compris dans ceux qui visent la
sécurité, continuent d'utiliser C malgré le risque que présente le langage. Et
ils ont raison. Pourquoi diable ?

Je vais mettre de côté les raisons liées à la dette technique et d'écosystème.
Il est évident que si les développeurs que l'on forme pour ce domaine sont
majoritairement formés à C et si les systèmes existants sont majoritairement
développés en C, cela joue en la faveur de C. Il serait difficile de sortir des
généralités, aussi je vais me concentrer sur deux exemples d'usage, on peut
faire ce genre d'analyse pour d'autres.

Premier exemple : les bibliothèques de communication sécurisées. Elles sont
effectivement très souvent écrites en C, malgré le risque en termes de sécurité.
Risque qui se manifeste régulièrement d'ailleurs par des failles de sécurité.
Cependant, les bibliothèques de communication sont utilisées sur un panel très
vaste de matériel (on attend donc une très bonne portabilité), et bénéficient
d'un énorme travail d'optimisation pour la vitesse, car elles sont critiques
*aussi* d'un point de vue performance dans les réseaux. Changer de langage n'est
donc pas si simple (même si certains projets comme
[Everest](https://project-everest.github.io/) ont déjà de belles réussites sur
leur tableau de chasse, leur mise en place dans des infrastructures réseaux
haute performance est encore impossible).

Second exemple : dans les domaines embarqués critiques (avionique ou ferroviaire
par exemple), il est commun de trouver du C en usage. Dans ce type de domaines,
la réalisation et la vérification du code doivent répondre à des normes strictes.
Cela impose notamment de qualifier la méthodologie de développement et faire
certifier les outils utilisés, faire certifier la chaîne de construction du
système, et de qualifier la méthodologie de vérification ainsi que faire
certifier les outils utilisés dans la vérification. Tout ce processus est long
et coûteux. Et parmi les arguments qui peuvent être mis en avant, la maturité
technologique des systèmes utilisés est un argument des plus valides. C présente
de ce côté, l'avantage indéniable de permettre les accès à une foule d'outils
avec de hauts degrés de maturité dont certains déjà plusieurs fois certifiés à
différentes périodes et dans différents cadres d'utilisation, ce qui n'est pas
forcément le cas pour d'autres langages (même si de ce côté on pourra sans
problème citer des langages/plateformes comme Ada ou Atelier B). Il s'ajoute à
cela la capacité à assurer la traçabilité des exigences jusqu'au niveau les plus
bas (après compilation) grâce au bon paramétrage de la chaîne de compilation
(notamment en interdisant toute optimisation ou en utilisant des compilateurs
formellement corrects). Tout cela combiné avec des investissements en
vérification et validation allant gentiment taquiner les 90% du temps de
développement, et on peut comprendre que l'inquiétude des acteurs du domaine ne
se trouve pas dans le choix du langage, mais dans le choix de ses outils.

Ces deux exemples permettent de comprendre comment C peut encore se montrer
parfois très utile ... tant que l'on comprend bien à quel point ces cas sont
extrêmement spécifiques et pas représentatifs de la majorité des usages du
langage.

## Mais alors ... Il ne faudrait surtout pas apprendre C ?

Vous faites ce que vous voulez.

Mon point est le suivant : n'apprenez pas C pour de mauvaises raisons. En
particulier, pas en vous justifiant cet apprentissage à l'aide des idées reçues
citées plus haut.

Si vous voulez apprendre la programmation bas niveau, bien sûr qu'il vous sera
utile d'apprendre C à un moment ou un autre pour avoir accès aux ressources qui
existent sur le sujet. Si vous voulez travailler dans un domaine où l'on
utilise C, bien sûr que vous allez apprendre C. Si vous avez envie d'apprendre
C parce que ça vous intrigue de comprendre les interactions entre ce qui est
défini dans la norme du langage, ce que fait un compilateur et ce qui a trait au
matériel, et comment tout ça a évolué au cours du temps, bien sûr que vous allez
apprendre C.

Le tout à mon avis est de procéder de manière logique. Il n'est peut-être pas la
peine de démarrer avec C, sauf si le semestre prochain, vous enquillez direct
sur de la programmation bas niveau parce que ça va être au centre de vos études.
Apprendre à programmer en C, ça demande d'être capable de mettre en place de
nombreux outils (compilateur, debugger, analyseur statique, profiler, système de
build, etc) dont l'intégration n'est pas toujours aisée. Si vous ne mettez pas
en place ces outils, *vous allez louper des erreurs dans vos programmes*, que
vous ne corrigerez jamais, et c'est autant de chances d'apprendre au passage qui
sont *perdues*. C'est pour cela que l'on peut fortement pester contre les
enseignements qui commencent avec ce langage, détecter toutes les erreurs bêtes
d'un programme écrit en C, c'est *dur*. Et les enseignants ne peuvent pas
regarder en détails les programmes des étudiants avec un niveau d'attention
suffisant pour tout remarquer. C'est plus facile quand on a la certitude qu'un
cas de test bien senti fera toujours péter un code buggé. Donc *pas* en C.

Démarrer par C alors que déjà, il va falloir apprendre à écrire des algorithmes,
ça s'appelle quand même "charger la mule". Mais si vous avez déjà un peu
d'expérience en programmation, pourquoi pas ? Ça vous fera une expérience avec
un langage défini de manière bizarroïde par des années d'évolution.
