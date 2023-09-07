---
layout: post
author: Julien Castiaux
date: 2023-03-12
title: "Les messages de commit dans git"
---

Au moment de créer un nouveau commit, git demande à l'utilisateur de décrire les changements effectués via le *message de commit*. La rédaction de ces messages peut sembler fastidieuse voire inutile, aussi bien aux novices qu'aux personnes plus expérimentés, mais est d'une importance capitale pour mener à bien un projet de développement informatique sur le long terme.

Ce document se découpe en plusieurs parties. La première est consacrée à expliquer l'origine des messages de commit et leurs liens avec les emails échangés entre les contributeurs au kernel Linux. La seconde découpe la structure d'un message de commit et explique quoi mettre à quel endroit. La troisième explique où et quand sont lus les messages de commit et explicite pourquoi il est important de prendre du temps à rédiger des bons messages de commit. Pour finir une quatrième est plus succincte et donne quelques pistes pour évaluer la qualité des commits et de l'historique git d'un projet et comment l'améliorer.

## Origine

Git a été développé afin de rendre possible la collaboration à grande échelle sur le noyau Linux. Avant d'utiliser git, les développeurs du noyau collaboraient à l'aide de mailing lists, ils discutaient des changements à venir ou en cours via mail et s'échangeaient du code en pièce jointe.

Le développement d'une nouvelle fonctionnalité commençait par l'envoi d'un e-mail à tous les inscrits de la mailing list pour décrire les nouveaux besoins. Si vous trouviez un bug dans le noyau, vous pouviez envoyer un mail à cette mailing list pour décrire le bug et demander à ce qu'il soit corrigé. Quiconque intéressé pouvait alors "répondre à tous" sur cet e-mail et ouvrir une discussion autours de la fonctionnalité à développer ou du bug à corriger. Après quelques jours, quelqu'un répondait à la suite d'e-mails avec un *patch*, c'est à dire une archive compressée contenant l'ensemble des *diff* à appliquer aux fichiers sources du noyau. Les autres développeurs répondaient avec cet e-mail pour donner leur avis sur les changements dans le but d'arriver à la meilleure solution. Une fois le patch approuvé par tout le monde (enfin surtout par Linus), il pouvait être appliqué sur le noyau et inclus dans les nouvelles versions.

Dans le lot, le développeur qui avait pris la peine de proposer un patch ne devait pas se contenter de répondre un e-mail vide avec le code en pièce jointe. Il avait aussi la responsabilité de résumer les discussions préalables et d'apporter des possibles éclaircissements sur son code. L'idée générale étant de faire gagner du temps à tout le monde (et surtout à Linus) en rappelant le contexte, les besoins et en apportant des explications quant à l'implémentation si ce n'était pas trivial.

Comme git a été développé avec comme objectif d'être utilisé par les contributeurs du noyau Linux, cette idée d'accompagner chaque contribution par un message explicatif a été reprise et a donné les messages de commit.

## Structure

À la manière des e-mails dont les messages sont inspirés, un message de commit se compose en 2 parties: le titre et le corps. Le titre s'inspire des sujets pour les e-mails tandis que le corps s'inspire du corps des e-mails. Le corps du message peut contenir plusieurs paragraphes de texte qui apportent toutes les infos nécessaires à la compréhension du commit. Le corps du message peut se terminer par un pied de page où sont repris différentes méta-informations, par exemple une liste de co-contributeurs, des notes de bas de page ou encore des références vers des numéros de tickets ou des issues.

	type(scope): titre sous 50 caractères............

	Corps avec plusieurs paragraphes, chaque ligne sous 72 caractères et...
	qui rappelle le contexte, explique pourquoi les changements sont.......
	nécessaires et apporte des éclairsissements si le code est compliqué...

	Après le corps on peut retrouver une série de références, notez que....
	certains [mots-clés] sont automatiquement reconnus par github..........

	[mots-clés]: https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/using-keywords-in-issues-and-pull-requests

### Titre

Le titre doit être un résumé concis et de préférence sous 50 caractères du contenu du commit. Normalement, il s'agit d'une phrase à l'infinitif en français (à l'impératif en anglais) qui peut compléter la phrase "Thanks to this commit we can ...", par exemple "*Thanks to this commit we can* fix bad smtp To headers for unicode addresses".

Selon les organisations, les titres des commits peuvent suivre un format précis où le *type* du changement et *l'endroit* du changement doivent être systématiquement écris. Par exemple en suivant la convention de [conventional commits], le précédent titre deviendrait "fix(smtp): bad To header for unicode addresses". En suivant la convention en vigueur à [Odoo], il deviendrait "[FIX] smtp: bad To headers for unicode addresses".

[conventional commits]: https://www.conventionalcommits.org/en/v1.0.0/
[Odoo]: https://www.odoo.com/documentation/master/contributing/development/git_guidelines.html

### Corps

Le corps du message est la partie la plus importante, c'est dans cette partie que sont formellement décrits tous les changements que le commit apporte. C'est aussi, malheureusement, la partie la moins comprise et la plus souvent ignorée par les novices de git.

Là où la diff qui accompagne le message de commit explique formellement *comment* et *où* dans le code les changements ont été effectués, le corps du message de commit doit formellement expliquer *qu'est-ce qui* et *pourquoi* ça a été changé.

Il est inutile de répéter dans le message de commit ce qui peut être appris en lisant soit le titre soit la diff. Ceci implique qu'un effort a été réalisé pour rédiger du code propre et correctement documenté avec des docstrings et des commentaires. Il est parfois judicieux de profiter du message de commit pour rappeler comment une fonctionnalité a évolué au fil du temps, pour justifier l'état actuel du code source avec des explications historiques qui n'ont pas vraiment leur place ni en docstring ni en commentaire mais il ne faut pas expliquer le code. Lorsqu'on ressent le besoin d'expliquer la diff, c'est peut-être une indication que le code n'est pas très propre.

Dans le corps du message, il faut donc se concentrer à apporter les informations qui ne peuvent pas être comprises en lisant seulement la diff. Il faut notamment donner un bref rappel des fonctionnalités en cours de modification pour donner le contexte générale, une vue d'ensemble. Il faut aussi impérativement expliquer *pourquoi* les changements ont été réalisé, paraphraser les spécifications dans le cas d'une nouvelle fonctionnalité ou bien donner les étapes pour reproduire un bug qui a été corrigé.

[![Des spécifications très complètes et très précises](/assets/images/strip-Les-specs-cest-du-code.jpg)](https://www.commitstrip.com/fr/2016/08/25/a-very-comprehensive-and-precise-spec/)

### Pied de page

En pied de page (footer, trailer) peuvent se trouver toutes une série de méta-information libres au format "Clé: valeur". On y retrouve:

* Les URLs pour tous les liens présents dans le corps du message.
* Les références vers les issues et les PR de Github.
* Les références vers les tâches ou les tickets dans les autres logiciels de gestion.
* Les références vers les autres commits liés au commit présent.
* Le nom des co-auteurs et de ceux qui ont effectué une relecture (*review*).

Dans le cas où notre commit est lié au ticket numéro 123 dans Jira et qu'il vient également clôturer l'issue 172 et la pull-request 173 dans Github, on écrira:

	Closes: #172
	Closes: #173
	JRA-123

Notez que pour éviter que le numéro d'un ticket dans un logiciel externe soit reconnu (à tord) comme le numéro d'une issue ou d'une PR dans Github, la convention est d'accoler le numéro avec un tiret plutôt que deux-points.

Dans le cas où notre commit est en relation avec un commit provenant d'une autre branche ou d'un autre projet, on écrira:

	Reference-to: orga/repo@1a2bc3 (fix bad smtp To header for unicode address)

Dans le cas où notre collègue John Doe nous a beaucoup aidé dans la conception ou la réalisation du travail et qu'on souhaiter le créditer, on écrira:

	Co-authored-by: John Doe <john.doe@example.com>

Comme ces champs sont libres, il n'existe pas de registre officiel où l'ensemble des clés possibles sont regroupées. Ces quelques précédents exemples ne sont que des exemples assez répandus.

Nous pouvons aussi citer `Helper-By`, `Acked-By` et `Signed-off-by` pour respectivement créditer quelqu'un qui a aidé pendant le développement, ceux qui ont review la pull request et celui qui prend la responsabilité légale des changements.

## Utilisation

Les commits et leurs messages sont lus à trois occasions différentes. Lors de la review par les reviewers, par intérêt général par les curieux qui lisent régulièrement l'historique pour se tenir au courant des modifications et au final par les collègues qui se creusent la tête au moment de debugger un bout de code qu'ils ne comprennent pas.

### Review

Lors de la review, les reviewers doivent comprendre l'ensemble des changements et les valider quant aux fonctionnalités qui étaient spécifiées. Ils étudient les changements en lisant scrupuleusement chaque ligne de code et en testant les nouvelles fonctionnalités. Le but de la review est de s'assurer que le travail est bien fait, de vérifier qu'il n'y a pas de bug et d'ouvrir une discussion pour proposer des améliorations avant que le code ne soit validé et fusionné.

Pour ouvrir une discussion constructive, il est donc important que les reviewers comprennent l'ensemble des changements apportés au code. Le message de commit doit leur permettre d'avoir une vue d'ensemble de ce qui est modifié de sorte à ce qu'il n'y ait pas de surprises, pas de moments "WTF?!", lorsqu'ils liront le code la première fois.

[![code review wtf/minutes](/assets/images/wtf.png)](https://commadot.com/wp-content/uploads/2009/02/wtf.png)

Ceci implique que le code doit être soigné et correctement structuré pour inviter des commentaires plus de fonds que de formes. Ceci implique aussi que les reviewers doivent avoir une vue d'ensemble de ce qui est modifié et comprendre les décisions qui ont été prises au moment du développement. C'est ici qu'intervient le message de commit. En rappelant le contexte générale et en justifiant les choix techniques.

Lorsque le message de commit est manquant, incomplet ou qu'il n'est pas correctement rédigé, les reviewers se retrouvent alors dans une situation où ils doivent beaucoup plus travailler pour comprendre ce qu'il se passe. Ils doivent relire l'ensemble des discussions autours de la spécification originale (si une telle spécification existe) et passer beaucoup plus de temps sur le code. Il y a alors un risque non négligeable que le reviewer ne prenne pas ce temps nécessaire et se contente d'une review minimale... avec son lot de répercutions sur la dette technique. Cette situation est bien reprise dans le short suivant, même s'il devrait plutôt être labellisé "how we write/review code in *shitty* companies": <https://youtube.com/shorts/0xB3T4MPEr0>.

### Blame

Le second moment où les messages de commit s'avèrent utiles est lorsqu'il s'agit d'étudier un bout de code, de comprendre le fonctionnement d'une fonction au travers du `git blame`.

`git blame` est une commande qui permet d'associer chaque ligne de code d'un fichier avec le commit qui en dernier a modifié la ligne. Il est alors possible d'étudier les changements qui ont été opérés sur une fonction pour mieux en comprendre son fonctionnement.

Le plus souvent cet outil est utilisé lorsqu'un bout de code est "WTF?!", que quelques lignes de code sortent de l'ordinaire, contrastent avec le reste d'une fonction sans qu'aucun commentaire/docstring ne l'explique, ou bien qu'il y a bel et bien un commentaire mais que celui-ci reste trop succin.

Le moment où une personne étudiera l'historique au travers du `git blame` sera souvent complètement déconnecté du moment où les changements auront été commités. On peut parler ici d'une différence allant même jusqu'à plusieurs années. Il est donc important de s'assurer au moment de créer les commits que chaque ligne dans la diff puisse être comprise via le message de commit. Il faut donc résister à l'envie de créer un seul gros commit pour plusieurs changements orthogonaux (des changements qui n'ont pas grand chose à voir les uns avec les autres) et au besoin isoler chaque groupe de changements dans des commits séparés. Il est d'ailleurs tout à fait acceptable d'avoir plusieurs commits dans une même pull request pour profiter d'une seule review pour l'ensemble des changements mais de tout de même correctement segmenter le travail en prévision d'un futur `git blame`.

### Log

Le dernier moment où quelqu'un est susceptible de lire les messages de commit est lorsque cette personne s'intéresse à l'historique en générale pour se tenir au courant des changements récents. C'est principalement le cas dans les petites équipes, lorsqu'il y est encore humainement faisable de se tenir au courant de l'ensemble des modifications apportées au projet. La plupart des bibliothèques open-source évoluent d'ailleurs suffisamment lentement pour qu'il soit possible de se tenir à jour des changements d'API.

Au moment d'écrire un message de commit, si le travail contient une nouvelle fonctionnalité ou un changement d'API, il est intéressant de rédiger un résumé explicatif des nouvelles fonctionnalités et de clairement expliquer tout changement d'API avec des exemples claires.

## Qualité

Déterminer la qualité d'un message de commit ou plus généralement d'un historique git est assez subjectif. Il n'y a pas de recette miracle pour améliorer sa rédaction en dehors de pratiquer régulièrement et de prendre la peine de s'auto-évaluer. Un exercice utile peut être de se porter régulièrement volontaire pour faire des reviews de pull requests et de porter un regard attentif au message de commit. À force de faire des reviews, vous apprendrez à reconnaitre ce qui est utile, nécessaire, voir même précieux dans l'ensemble de la paperasse (spec, message de commit, documentation, docstrings, commentaires, ...) et à reprendre les bons exemples et éviter les mauvais.

Vous pouvez vous poser la question quant à la fréquence à laquelle vous lisez les messages de commit. Que ce soit pendant les reviews, avec `git blame` ou avec `git log`. Si vous n'arrivez jamais à trouver les informations que vous cherchez ni avec blame, ni avec log, c'est certainement que l'historique et les commits ne sont pas bons. Si au contraire vous vous retrouvez régulièrement à naviguer dans l'historique, c'est certainement que le travail est bien fait.

## Conclusion

La rédaction des messages de commit fait parti intégrante du métier de développeur et vient, à l'instar de l'écriture des tests unitaires, différencier le développeur amateur du développeur professionnel.

Les messages de commit sont le cœur de la documentation technique à destination des mainteneurs. Ils sont écris pour les collègues d'aujourd'hui qui devront aussi bien valider notre travail via les pull requests, ils sont aussi écrits pour les collègues de demain qui devront étudier notre code pour le faire évoluer.

Grâce aux messages de commit, il est possible de retracer l'évolution d'un logiciel et de développer sa propre compréhension des différentes étapes qui l'ont mené à être ce qu'il est aujourd'hui. Il s'agit d'un atout précieux qui renforce la confiance des développeurs quant aux changements qu'ils apportent au logiciel.
