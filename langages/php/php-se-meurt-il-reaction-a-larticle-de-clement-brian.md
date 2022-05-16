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

[...]