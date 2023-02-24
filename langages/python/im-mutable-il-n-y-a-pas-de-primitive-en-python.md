# (Im)mutable - Il n'y a pas de primitives en Python !

Vous avez certainement déjà fait une addition en Python, vous avez aussi certainement déjà incrémenté un compteur, un simple `i += 1`, mais vous êtes-vous déjà posé la question de ce que Python a fait sous le capot pour augmenter `i` de `1` ?

Si vous venez d'un langage de programmation où il est possible de manipuler des primitives, comme C, C++, Java ou C#, vous devez vous dire qu'incrémenter un entier en Python ne doit pas être fondamentalement différent.

Vous devez vous dire que *la variable `i` désigne un emplacement en mémoire*, que dans cet emplacement mémoire *se trouve un entier sur x bits* et que l'opération `+= 1` aura juste *modifié ces bits pour augmenter la valeur de 1*. 

Vous vous trompez.

Vous vous rappelez alors qu'en Python "tout est objet" et que donc *techniquement* la variable `i` *ne désigne pas directement l'entier mais un objet qui à son tour désigne l'entier en mémoire*...

Vous auriez raison jusque là...

...*et que l'opération `+= 1` aura modifié l'entier référencé par l'objet*.

Vous vous trompez à nouveau.

## Tout est objet !

Tout est objet !

> Oui, c'est la 3e fois que tu le dis

Si tout est objet, ça veut donc dire qu'il n'y a aucune primitive !

> Oui, c'est juste tournée dans l'autre sens

Et qu'il n'y a donc aucun passage par valeur non plus !

> Oui on sait, quand on passe une liste en argument à une fonction, on passe la référence à la liste à la fonction... Tes entiers sont quand même passé en valeur.

J'ai dit, **aucun** passage par valeur !

> Même pas les entiers ?!

Même pas les entier !

> Mais je ne comprend pas, si je passe un entier à une fonction et que je modifie cet entier dans la fonction, l'entier original n'est pas modifié. C'est bien la preuve qu'il est passé en valeur !

L'entier original n'a pas été modifié effectivement et pourtant cet entier a bel et bien été passé par référence à la fonction.

> Mais comment ça marche alors ?!

C'est pour ça que tu vas lire cet article jusqu'à la fin :D

## Question de mutabilité

Dans le paradigme impératif, il est de base possible de modifier toutes les variables à l'exceptions de celles marquées comme constantes. Dans le paradigme fonctionnel, une fois qu'une valeur est associée à une variable, il n'est plus possible de la changer (sauf quelques exceptions tordues).

Python n'est ni un langage impératif, ni un langage fonctionnel. Il n'y a pas de notion de "constantes" intrinsèques au langage: ce n'est pas un langage impératif. Il n'y a pas non plus de sacro-sainte-règle qui dise qu'il est interdit de modifier une variable: ce n'est pas un langage fonctionnel.

Python est en langage orienté objet et les langages orientés objets apportent une notion intéressante qui vient régir la manipulation des variables (ou plutôt des objets associés à ces variables), il s'agit de la notion de *mutabilité*.

Dans les langages orientés objets, savoir si on peut ou non modifier un objet dépend en fait de la nature de cet objet, de son type. Les objets des types qu'on ne peut modifier seront qualifiés d'objets *immuables*, les autres seront qualifiés d'objet *mutables*.

Quand on dit qu'un objet est mutable, on parle par exemple des instances des classes définies par l'utilisateur, modifier un attribut de l'objet 

```py
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

bob = Person('Bob', 20)
bob.age += 1
```

