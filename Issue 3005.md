# Issue 3005: mobabar -- failure to compute endomorphism ring

Issue created by migration from https://trac.sagemath.org/ticket/3005

Original creator: was

Original creation time: 2008-04-23 13:08:04

Assignee: was

This is an example of computing an endomorphism ring of a J1 modular abelian variety -- it fails because of some mysterious issue in sage-3.0. 


```
age: J = J1(17)
sage: D = J.decomposition(); D
[
Simple abelian subvariety 17aG1(1,17) of dimension 1 of J1(17),
Simple abelian subvariety 17bG1(1,17) of dimension 4 of J1(17)
]
sage: Phi, _ = D[0].intersection(D[1]); Phi
Finite subgroup with invariants [2, 2] over QQ of Simple abelian subvariety 17aG1(1,17) of dimension 1 of J1(17)
sage: E = D[1].endomorphism_ring(); E
Endomorphism ring of Simple abelian subvariety 17bG1(1,17) of dimension 4 of J1(17)
sage: E.gens()
Traceback (most recent call last):
...
TypeError: Cannot coerce element into this number field
```



---

Comment by craigcitro created at 2008-04-24 07:06:27

Changing assignee from was to craigcitro.


---

Comment by craigcitro created at 2008-04-24 07:06:27

Bug was actually with modular symbols -- when finding eigenvalues, there was a place where the name parameter didn't get passed along. As a result, the eigenvalue getting returned couldn't be coerced into the number field, and all hell broke loose. 

Fixed, added a doctest to catch it (to modular symbols, not abelian varieties).


---

Comment by craigcitro created at 2008-04-24 07:06:27

Changing status from new to assigned.


---

Attachment

This is obviously right.


---

Comment by mabshoff created at 2008-04-24 14:38:04

Resolution: fixed


---

Comment by mabshoff created at 2008-04-24 14:38:04

Merged in Sage 3.0.1.alpha0
