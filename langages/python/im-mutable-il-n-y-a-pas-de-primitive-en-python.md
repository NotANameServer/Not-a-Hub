# (Im)mutable - Il n'y a pas de primitives en Python !

Vous avez certainement déjà fait une addition en Python, vous avez aussi certainement déjà incrémenté un compteur, un simple `i += 1`, mais vous êtes-vous déjà posé la question de ce que Python a fait sous le capot pour augmenter `i` de `1` ?

Si vous venez d'un langage de programmation où il est possible de manipuler des primitives, comme C, C++, Java ou C#, vous devez vous dire qu'incrémenter un entier en Python ne doit pas être fondamentalement différent.

Vous devez vous dire que *la variable `i` désigne un emplacement en mémoire*, que dans cet emplacement mémoire *se trouve un entier sur x bits* et que l'opération `+= 1` aura juste *modifié ces bits pour augmenter la valeur de 1*. 

Vous vous trompez.

Vous vous rappelez alors qu'en Python "tout est objet" et que donc *techniquement* la variable `i` *ne désigne pas directement l'entier mais un objet qui à son tour désigne l'entier en mémoire*...

Vous auriez raison jusque là...

...*et que l'opération `+= 1` n'aura pas modifié l'objet mais aura modifié l'entier référencé par l'objet*.

Vous vous trompez à nouveau.
