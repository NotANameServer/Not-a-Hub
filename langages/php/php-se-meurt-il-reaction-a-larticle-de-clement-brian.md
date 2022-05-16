# À propos du fait que PHP se meurt et réaction à l'article de Clément Brian

Hello à tous.  Récemment, j'ai vu l'article [PHP Is Dying Fast](https://levelup.gitconnected.com/php-is-dying-a3805e23a3b8) de Clément Brian passé sur certains Discord. Je voulais en faire une réaction, factuel et prendre point par point ce qu'il avance dans celui-ci.

Pour commencer, pour me présenter rapidement, je suis Mishaa, j'ai 4 ans d'expérience professionnelle en tant que développeur. Je fais autant de front que de back et le métier de développeur me passionne depuis que je suis jeune. 

Au niveau de mon objectivité, je vais essayer d'être le maximum factuel dans mes propos, il faut savoir que j'ai fait beaucoup de TypeScript, de PHP et également du Rust en ce moment. J'ai testé pas mal de framework (Type|Java)script, et également quelques frameworks PHP (Surtout Laravel).

Selon mon expérience personnelle, je trouve que les frameworks PHP et l'écosystème sont très qualitatifs, Laravel offre un confort de développement assez énorme. 

### PHP et son évolution

Mon billet n'est pas destiné uniquement aux développeurs PHP, je dois donc parler rapidement de PHP et de son évolution afin de casser les idées reçues que l'on peut souvent lire à droite à gauche.

En 1994, Rasmus Lerdor crée Personnal Home Page Tools (qui plus tard sera renommé en PHP), dont l'idée était juste de pouvoir tracer des utilisateurs sur son site. Il va rapidement ajouter de nouvelles fonctionnalités. 

Il va rapidement rendre PHP public et en 1996, il décide de réécrire complètement PHP depuis zéro, la syntaxe à cette époque  était semblable  au langage Perl, bien que beaucoup plus limitée et un peu incohérente. C'est vraiment cette version qui marque la transition d'un simple outil à un véritable langage de programmation.

Vers 1998, en raison de certaines limitations du langage pour un projet d'e-commerce dans un cadre universitaire, Andi Gutmans et Zeev Suraski propose à Rasmus Lerdor de réécrire entièrement le moteur de PHP ainsi que d'améliorer le langage, c'est comme ça que fut sorti la version 3.0 de PHP. (Le moteur sort un peu après PHP 3.0)

C'est notamment grâce à cette évolution, qui ajoute au langage une certaine capacité d'extension et du fait qu'il propose une infrastructure mature pour de multiples bases de données, protocoles, et APIs que le langage attira énormément de développeur du monde entier. C'est également sur cette version que le modèle orienté objet apparait.  

Il faut savoir que lors de la sortie de la version 3.0 du langage, PHP était déjà installé sur plus de 70 000 domaines dans le monde entier, ce qui représentait 10% des serveurs web de l'époque.

En 1999, la version 1.0 du nouveau moteur de PHP sort, appelé Zend Engine, qui améliore les performances de PHP sur les applications, un peu complexes ainsi que la modularité du code. C'est en s'appuyant sur ce moteur que sortira la version 4.0 de PHP qui ajoute énormément de fonctionnalité, comme la gestion des sessions HTTP, la gestion de plus de serveurs, l'amélioration de la configuration de PHP via le fichier php.ini...

En 2004, la version 5.0 de PHP se basant sur la version 2.0 de Zend Engine sort, c'est l'une des mises à jour les plus importantes de PHP, cette dernière propose beaucoup d'amélioration du modèle objet ainsi que beaucoup d'autres fonctionnalités. PHP est devenu très populaire, il est installé sur des centaines de millions de serveurs.

Cette version a été rendue possible par le travail de dizaine de développeurs sur le langage, le moteur ainsi que les extensions autour. 

Pour faire rapide, la version PHP 6.0 sera abandonné suite à un développement, un peu chaotique et un gros risque de casser la rétro comptabilité. Fin d'année 2015, la version 7.0 de PHP sort, avec amélioration de performance et des nouvelles fonctionnalités. Plusieurs mises à jour mineures sortent, généralement jusqu'à la version x.4 (7.1, 7.2, 7.3, 7.4) avec la correction de bugs, l'ajout de fonctionnalités et l'amélioration des performances. 

Grâce à la simplicité, la modularité de PHP ainsi que sa popularité, beaucoup d'outils et de librairies sont sortis, comme le très connu WordPress mais également des frameworks complets comme Symfony, Laravel, Cake PHP et pleins d'autres, ce qui en faisait en choix évident pour beaucoup de développeur et d'entreprise.

La simplicité de PHP réside beaucoup du fait qu'il est possible de mélanger du code HTML avec PHP, de la façon suivante : 
```php
<?php if (strpos($_SERVER["HTTP_USER_AGENT"], 'Firefox'))
    <p>Il me semble que vous utilisez Firefox !</p>
<?php endif; ?>
<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi felis.</p>
```
Ici, par exemple, le paragraphe <``Il me semble que vous utilisez Firefox``> sera affiché uniquement si l'user-agent de l'utilisateur correspond à Firefox.  

Cette façon de faire ne plait pas à tout le monde et c'est une des critiques que l'on peut souvent lire, car cela pose potentiellement des problèmes d'organisation et de responsabilité. 

À l'heure où je fais cet article, nous sommes à la version 8.1 de PHP, la version 8.0 et cette dernière ont ajouté énormément de fonctionnalité, surtout au niveau des types. Voici une petite liste non exhaustive des améliorations : 

- Argument nommé (qui permet de spécifier uniquement certains paramètres requis dans l'ordre que l'on veut)
- Attributs
- Promotion de propriétés de constructeur
- Type union (permet d'avoir, par exemple, une méthode qui attend un string ou un nombre en paramètre) 
- L'instruction match qui permet de simplifier certaines utilisations de switch / if
- Le nullsafe opérateur 
- La compilation juste à temps (JIT) qui améliore significativement les performances
- Les énumérations
- Les propriétés readonly
- L'initialisation de propriété directement dans le constructeur
- Les classes finales 
- L'opérateur numérique octal
- Les Fibers qui permettent de faire de la concurrence plus facilement  (à condition d'avoir l'implémentation d'une event-loop)

[En savoir plus sur la version 8.0](https://www.php.net/releases/8.0/fr.php) / [En savoir plus sur la version 8.1](https://www.php.net/releases/8.1/en.php)
 
 La dernière version mineure (PHP 8.1) est sorti en novembre 2021, l'équipe de PHP continue à proposer des améliorations ainsi des fixes de sécurité en fonction des [versions supportées](https://www.php.net/supported-versions.php). La résolution de bugs et l'amélioration de la sécurité est très régulières, généralement une fois par mois, via la sortie de nouvelle version mineure, comme la version 8.1.6, sortie le 12 mai 2022. 

L'évolution du langage et l'ajout de fonctionnalité suit un [processus déterminé](https://blogs.oracle.com/opal/post/the-mysterious-php-rfc-process-and-how-you-can-change-the-web), via des RFC. Mais concrètement pour faire simple, il s'agit d'abord de discuter de l'implication de l'ajout avec plusieurs acteurs via le mail liste interne. En suite, un document standardisé est rédigé qui explique en détail les raisons du changement, ce que ça apporte, les éventuels problèmes, un exemple d'utilisation, ... ce genre de chose. (Petite note, **il ne s'agit pas uniquement des ajouts de fonctionnalité**, par exemple, le fait de supprimer ou de rendre obsolète certaines fonctionnalités sont aussi soumises aux RFC, en fonction de l'implication sur les utilisateurs du langage)

Toutes les RFC sont ensuite discutées et débattues avec l'équipe interne de développement de PHP (core team) ainsi que certains acteurs majeurs qui sont derrières certaines librairies ou qui participe activement à l'écosystème de PHP. Elles sont ensuite votées (généralement + de 65% des membres doivent être favorables pour qu'une RFC soit acceptée), une implémentation/POC est aussi généralement nécessaire.

[Voir la liste des RFC](https://wiki.php.net/RFC) 

## PHP se meurt-il ? 

Maintenant que nous avons vu l'histoire de PHP ainsi que son évolution, nous savons que le langage évolue quand même beaucoup. Néanmoins, on peut souvent voir des articles sur quoi PHP serait en train de mourir et qu'il va bientôt être remplacé par d'autres langages comme Python ou JavaScript.

Je vais me fonder sur les propos de l'article à chaque fois. 

> Avant de choisir une technologie pour votre projet, l'une des choses les plus importantes que vous puissiez faire est de vérifier sa tendance.
> Cela devient super précieux si vous avez pour objectif d'accélérer vos projets pour de nombreuses années à venir. Les projets à long terme nécessitent de faire les choses de la bonne manière. Vous ne voulez pas être coincé dans une technologie qui diminue et finir par manquer de support ou d'autres nécessités essentielles à l'avenir. C'est le cas de PHP.

Il prend pour source ensuite, cette image : 

![](https://miro.medium.com/max/1400/1*bHXOU-t5GPfSWUyV7ncxZw.png)
Alors selon moi, c'est un élément à vérifier, effectivement. 

Tout d'abord, chaque version de PHP est supportée pendant 2 ans pour l'ajout de fonctionnalités, l'amélioration de performance, les corrections de sécurité et la correction de bugs. À la fin de cette période, la version est supportée durant 1 an supplémentaire pour les corrections de vulnérabilités et de sécurité [[1]](). 

Cette période va s'appliquer pour **chaque version de PHP, mineure ou majeure**. 

Il faut savoir que PHP propose pour chaque nouvelle version mineure ou majeure un guide de migration, qui explique très bien et dans les détails l'ensemble des changements. Voici, par exemple, le guide de migration de la version PHP 7.3 à la version PHP 7.4 :

![Guide de migration PHP, proposé pour chaque version de PHP](https://i.imgur.com/gY8TOjg.png)

Vous pouvez voir que c'est très clair, et que vous avez une partie fonctionnalités obsolètes qui vous permet de directement voir à quoi vous devez faire attention. Et surtout, durant les mises à jour mineures, il n'y a aucun changement cassant. Cela veut dire qu'il est très peu probable que vous code arrête de fonctionner lorsque vous faites une mise à jour mineure (PHP 7.3 à PHP 7.4) 

La communauté met aussi à dispositions de superbes outils comme [Rector](https://getrector.org/), qui permet de faire les migrations de mise à jour de manière semi-automatique à l'aide d'un CLI et de configuration. Pour l'avoir déjà utilisé, c'est très impressionnant. 

N'importe quel développeur / entreprise qui fait attention aux mises à jour (afin d'éviter d'accumuler la dette technique) peut facilement réaliser des montées de version, grâce à ce que propose le langage et la communauté. Le cas échéant, par manque de temps, par exemple, PHP dispose d'un temps de support assez élevé (3 ans, par version). 

Maintenant, concentrons-nous sur cette phrase :
> Vous ne voulez pas être coincé dans une technologie qui diminue et finir par manquer de support ou d'autres nécessités essentielles à l'avenir. C'est le cas de PHP. 

Alors, cette phrase est très polarisée, en dehors d'une bête image Google Trend (et l'on va en reparler), il n'apporte absolument aucune source de ce qu'il affirme. C'est quelque chose qui va être très récurant dans cet article. 

Pour faire simple, c'est absolument faux. PHP est toujours le langage de programmation côté serveur le plus utilisé au monde, avec une part de marché de 77.4% en mai, 2022. [[2]](https://w3techs.com/technologies/history_overview/programming_language/ms/y) Traçons une courbe afin de voir l'évolution sur le fil des années.

![Évolution des parts de marché de PHP de l'année 2011 à l'année 2022](https://i.imgur.com/ikynkvA.png)
On peut remarquer que l'évolution de part de marché de PHP reste très stable, et ce, depuis de nombreuses années. 

Néanmoins, en 2014, 12,278 % de toutes les pull requests concernaient des projets PHP, et c’était le quatrième langage le plus répandu sur le site. En 2015, ce pourcentage a glissé à 10,223 %, et en 2018, il n’était plus que de 6,109 %. [[3]](https://kinsta.com/fr/part-de-marche-php/). C'est très difficile d'interpréter ce chiffre, cela peut être dû à toute une multitude de facteurs. 

 Pour ma part, je pense que PHP est très bien installé et ce n'est pas près de changer, même si, en raison de la diversité de technologie, de framework et de langage, certains développeurs se tournent vers d'autres langages. 

Aussi, les frameworks front-end comme, React, Vue,... sont très populaires, de même pour les applications mobiles avec ReactNative, avoir un écosystème complètement en JavaScript plaît énormément aux entreprises. 

Passons à un autre argument.

> A partir de 2022, choisir PHP pour votre projet n'est plus dans le manuel. Sauf si c'est quelque chose de temporaire. Si vous tenez vraiment à votre projet, vous devriez choisir un langage moderne. Un langage qui est en plein essor ou à son apogée. Cela garantit la sécurité, la survie et la croissance dans le futur.

Ici, c'est très vague. L'auteur va énormément parler de Django (et non pas Python...), donc je vais prendre l'exemple de Python 3. Il nous parle de langage moderne, sans nous donner une définition de ce qu'il considère comme un langage dit "moderne", la première version de Python date de 1991, et la sortie de la version 3.0 de Python est sortie le 3 décembre 2008 [[4]](https://www.python.org/download/releases/3.0/). Django lui, existe depuis 2005. 

Faites-en ce que vous voulez, mais je ne sais pas trop quoi répondre pour ce point. Comme je l'ai dit plus haut, la dernière version de PHP (PHP 8.1) est sorti en novembre 2021, et la préparation de la version PHP 8.2 est en cours. (Voir la page des RFC) 

> Les programmeurs de la nouvelle génération ne choisissent pas PHP comme langage à maîtriser. Ils choisissent node.js plutôt que PHP. Ce sont eux qui domineront le Web de demain.

Difficile de réagir, on dirait une prédiction sortie d'une boule de cristal. 

> Ils comprennent les frictions liées à l'utilisation de deux langages et les inconvénients de PHP. Ils savent que la maîtrise de PHP ne leur apportera pas la plus grande valeur ajoutée.

Ce point-ci est intéressant, cependant il ne détaille pas les « inconvénients de PHP ». Donc, je vais me concentrer sur le fait de devoir utiliser et apprendre deux langages. 

Effectivement, c'est vrai, encore plus quand on utilise un langage de programmation comme JavaScript, qui évolue beaucoup, ainsi que ses outils et framework. Il faut mettre en place une stratégie pour mettre à jour les dépendances, suivre l'évolution des frameworks, faire de la veille, etc. 

Pour une équipe réduite, le fait de n'avoir qu'un langage de programmation (donc un seul et même écosystème) peut être une véritable plus-value et peut éventuellement soulager l'équipe. 

Toutefois « Ils savent que la maîtrise de PHP ne leur apportera pas la plus grande valeur ajoutée », PHP a beaucoup à offrir par son écosystème et surtout ses frameworks, comme Laravel qui offre énormément de fonctionnalité et qui offre un gros confort pour les développeurs. Ils ont l'avantage d'être là depuis longtemps et d'être très fiable et mature. Il y a également énormément de bonnes ressources pour apprendre et monter en compétence. 

>Les recruteurs en sont également conscients. Un grand nombre d'entre eux remplacent lentement le code PHP par node.js ou d'autres alternatives.
>Les programmeurs compétents qui changent de secteur ne choisissent pas non plus PHP comme langage à maîtriser. (Par exemple, les gars qui étaient auparavant des développeurs de jeux et qui veulent s'aventurer dans le développement web). La plupart d'entre eux choisissent Node.js.
> Voici comment PHP se compare à d'autres frameworks back-end comme Node.js et Django.
Django est relativement jeune, l'avenir est prometteur. Je comprends qu'il n'est pas encore totalement mature. À l'avenir, ce sera probablement une bête. Il n'est pas en déclin.

![](https://miro.medium.com/max/1400/1*Ufin9NSVTen2qyfKu7-xHQ.png)
![](https://miro.medium.com/max/1400/1*xWY7tB5oBtwzmmdqXJ7xfQ.png)

Alors pour cette partie, c'est assez drôle. 

Premièrement, Django est bien loin d'être jeune, il est sorti en 2005. Laravel est quant à lui, sorti en 2011, soit 6 ans plus tard. Donc cet argument est complètement faux, en plus de prouver le point inverse. 

Ensuite, il nous parle de Node.JS, mais... Node.JS, c'est un runtime, pas un framework backend. Il existe une multitude de framework JavaScript, donc impossible de savoir de qui il parle. 

Pour répondre à son image Google Trends (je précise que je trouve ça absolument pas représentatif) 

![enter image description here](https://i.imgur.com/19Z79PR.png)

Django est au raz des pâquerettes et "Node" (qui ne veut rien dire) et Laravel est au même niveau. 
En conclusion, les arguments avancés aussi sont très bancals et hors de la réalité. 

> Node.js a plus d'attention que Django. Il s'agit clairement du favori. Ce qui est similaire cependant, c'est que les deux frameworks sont en pleine croissance. À l'avenir, ils seront probablement plus robustes.
Ces frameworks et d'autres langages modernes comme Rust et Go sont sans doute meilleurs que PHP.
Ils corrigent les inconvénients de PHP, ont été créés de manière systématique et sont plus organisés. Ils sont donc plus solides que PHP.

Je ne sais pas sur quoi il se base pour dire que les frameworks sont en pleine croissance. Ensuite, il nous dit que « Go & Rust sont meilleurs que PHP, car ils corrigent les inconvénients de PHP (sans nous détailler ce point), ont été créés de manière systématique et sont plus organisés. Ils sont donc plus solides que PHP ».

Il n'a absolument aucun sens de dire ça, sans détailler de quoi il parle. Go & Rust sont des langages qui répondent à certains besoins (étant un amoureux de Rust), mais affirmer qu'ils sont meilleurs est quelque chose de stupide. (C'est comme dire que le bleu est meilleur que l'orange) 

Le seul point implicite que je peux extraire, c'est le fait que de base, PHP n'était pas un langage de programmation. Mais, ce point est complètement caduc en raison de la réécriture complète du langage et de l'évolution de ce dernier (depuis longtemps). 

Je vais passer la partie "# The Tech Stack Has Changed" car je n'ai absolument rien à dire dessus, et que je ne connais pas le web 3.0 (qui semble être bien loin d'être le futur, selon moi, mais je n'ai pas les connaissances suffisantes pour réagir) 

> Les téléphones mobiles et les tablettes dominent le web. Nous transportons nos téléphones presque partout où nous allons.
La majorité du trafic web provient actuellement d'appareils mobiles. Une personne moyenne passe plus de temps sur son téléphone que sur tout autre appareil.
La société technologique en est consciente et les entreprises déplacent leurs services du web vers les applications mobiles. Cela a provoqué une énorme migration qui se produit actuellement et se produira à l'avenir.
En bref, c'est une bonne nouvelle pour les développeurs d'applications mobiles. Qu'il s'agisse de Swift ou de Kotlin, ils vont se régaler.
La mauvaise nouvelle, c'est que PHP ne fait pas partie de cette migration. Il n'est pas adapté aux applications mobiles. Il n'a même pas été conçu pour elles. Il s'agit d'un langage côté serveur, adapté au Web.

Cette partie est lunaire selon moi. L'auteur nous a parlé de Rust, Django, et même de Node.JS. Ensuite, il nous parle d'application mobile, j'imagine pour le fait que JavaScript permet de faire des applications mobiles.

Alors, PHP est, en effet, pas adapté pour faire des applications mobiles, mais... je ne vois pas trop pourquoi ça serait un problème. Les applications mobiles font des requêtes API (requête HTTP, donc) à des serveurs pour récupérer des données ou effectuer des opérations. 

Elles représentent uniquement la partie logique et visible à l'utilisateur, mais à partir du moment ou vous avez besoin de compte, de paiement, de liste, d'ami, etc. Vous allez avoir besoin d'une partie serveur. 

De ce fait, il y aura toujours la nécessité d'avoir des langages qui sont capables de faire du server side, que ce soit django, Node.JS ou même Laravel.

Laravel (et n'importe quel langage de programmation de manière générale) est complètement adapté pour réaliser des API's Restful, du GraphQL ou même du RPC. Laravel possède une multitude de librairies pour ce genre d'utilisation, et même [un gros framework pour GraphQL](https://lighthouse-php.com/).

Donc dire que PHP ne fait pas partie de cette migration n'a absolument aucun sens, hors du fait que certaines équivent vont éventuellement choisir d'utiliser exclusivement un langage, comme dit plus haut.

> In the future, both are likely to have a decent share in mobile applications. Django is already a pioneer. It powers Instagram which is the [6th most visited website](https://www.statista.com/statistics/1201880/most-visited-websites-worldwide/) in the world.

Alors... : 

![enter image description here](https://memegenerator.net/img/instances/59669839.jpg)

### En conclusion

Selon moi, l'auteur ne sait malheureusement pas de quoi il parle, il prend des Google Trends et tire des conclusions fumeuses sur l'évolution de PHP. 

Ses propos mettent en évidence son manque de connaissance de PHP ainsi que de son écosystème. Il semble confondre beaucoup de choses et est monté dans l'hype train des technologies, sans même prendre du recul. 

**Maintenant, pourquoi je réagis à cet article complètement débile ?** 

Le problème, c'est que ce dernier a été vu et lu énormément de fois, et même si les propos sont fumeux, pour un débutant, ça peut être complètement crédible.

Certes, beaucoup de gens ont réagi comme je le fais dans les commentaires, d'ailleurs l'auteur semble répéter cette phrase en boucle (pour se convaincre ?)

![enter image description here](https://i.imgur.com/zA2979L.png)

Mais faut-il encore lire les commentaires...

Je vois énormément d'idée reçue, d'avis négatif sur PHP, des gens qui blaguent en disant qu'ils vont faire du PHP, ce genre de chose. Le problème, c'est qu'à force de répéter ce genre de chose, les gens finissent par y croire, et quand on demande de citer un problème sur le langage, soit, ils en sont incapables, soit, ils vont sortir des arguments qui sont faux ou complètement pétés. 

Donc s'il vous plaît, essayez de prendre du recul sur la situation et d'arrêter de critiquer tout le temps certaines technologies, ou soyez sûr d'avoir des arguments solides et d'avoir fait un minimum de veille sur le sujet. Prenez des pincettes sur tout ce que l'on peut vous dire, surtout si les avis sont à ce point polarisé et extrême. 

Le meilleur langage de programmation, c'est celui que l'on utilise et celui qui nous permet d'être le plus productif tout en appréciant ce que l'ont fait. Les langages de nos jours sont multi-usages et très polyvalents, donc dire que tel langage est mieux qu'un autre sera toujours futile et faux. 

Je vous remercie d'avoir pris votre temps pour lire cet article, n'hésitez pas à le partager.


### Source 
[[1]](https://www.php.net/supported-versions.php) : Page officiel du support des versions de PHP 
[[2]](https://w3techs.com/technologies/history_overview/programming_language/ms/y) : Tendances annuelles historiques des statistiques d'utilisation des langages de programmation côté serveur pour les sites web (W3Techs) 
[[3]](https://kinsta.com/fr/part-de-marche-php/) : Part de marché de PHP en 2022
[[4]](https://www.python.org/download/releases/3.0/) : Date de sortie de Python 3
