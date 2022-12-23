# Issue 6392: modular abelian quotient -- something goes wrong

Issue created by migration from https://trac.sagemath.org/ticket/6392

Original creator: was

Original creation time: 2009-06-24 09:53:32

Assignee: craigcitro

CC:  mderickx

This isn't right:

```
sage: J = J0(43)
sage: G,_ = J[0].intersection(J[1])
sage: J[1]/G
Simple abelian subvariety 43b(1,43) of dimension 2 of J0(43)
```


This is

```
sage: J[0]/G

(Abelian variety factor of dimension 1 of J0(43),
 Abelian variety morphism:
  From: Simple abelian subvariety 43a(1,43) of dimension 1 of J0(43)
  To:   Abelian variety factor of dimension 1 of J0(43))
```


For some reason J[1]/G isn't even creating the right output (i.e., pair (abvar, map)). 


---

Comment by mderickx created at 2010-12-21 15:41:18

G is strictly speaking not a subgroup of J[1] in this example it's a subgroup of J[0]. What happens if you travel down the code is equivalent to this:

```
G=J[1].finite_subgroup(G) #This should raise an error since J[0] and J[1] have empty intersection
J[1]._quotient_by_finite_subgroup(G):
```


Now the source code of _quotient_by_finite_subgroup is


```
def _quotient_by_finite_subgroup(self, G):
    if G.order() == 1:
        return self
    L = self.lattice() + G.lattice()
    A = ModularAbelianVariety(self.groups(), L, G.field_of_definition())
    M = L.coordinate_module(self.lattice()).basis_matrix()
    phi = self.Hom(A)(M)
    return A, phi
```

So i guess it should instead return

```
return self, self.Hom(self).identity()
```


There is also a problem with the is_subgroup code:
sage: G.is_subgroup(J[1])
True
This error is caused by the intersection code:
sage: G.intersection(J[1])
Finite subgroup with invariants [2, 2] over QQ of Simple abelian subvariety 43b(1,43) of dimension 2 of J0(43)

Maybe I'm a bit confused but is the intersection of abelian varieties defined in an other way than just the set theoretic one. Because by reading the source code I really get the feeling that it does. The errors certainly seem to come from different assumtions about this in different parts of the code.


---

Comment by mderickx created at 2010-12-21 15:50:47

My confusion mainly comes from the following:


```
sage: J[1].finite_subgroup(G)
Finite subgroup with invariants [] over QQ of Simple abelian subvariety
43b(1,43) of dimension 2 of J0(43)
J[1].intersection(G)
Finite subgroup with invariants [2, 2] over QQ of Simple abelian
subvariety 43b(1,43) of dimension 2 of J0(43)
```



---

Comment by klui created at 2018-09-19 23:19:44

The issue was in `finite_subgroup`. We had to include the lattice of the ambient jacobian and not just the ambient abelian subvariety. 

This branch returns the identity map as well when quotienting by a trivial group. 
----
New commits:


---

Comment by klui created at 2018-09-19 23:20:00

Changing status from new to needs_review.


---

Comment by chapoton created at 2018-09-20 12:11:47

ok, let it be. Please add author full name.


---

Comment by chapoton created at 2018-09-20 12:11:47

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2018-09-20 17:48:04

Changing status from positive_review to needs_work.


---

Comment by vbraun created at 2018-09-20 17:48:04

Author name is missing..


---

Comment by chapoton created at 2018-09-20 17:49:02

Changing status from needs_work to positive_review.


---

Comment by vbraun created at 2018-09-21 22:20:29

Resolution: fixed
