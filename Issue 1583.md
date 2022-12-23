# Issue 1583: simple modules of modular symbols over finite fields

Issue created by migration from https://trac.sagemath.org/ticket/1583

Original creator: AlexGhitza

Original creation time: 2007-12-21 17:47:00

Assignee: was

There are instances in which Sage thinks that a one-dimensional space of modular symbols is not simple, and it decomposes the space into a one-dimensional and a zero-dimensional subspace:


```
sage: C=ModularSymbols(1,14,0,GF(5)).cuspidal_submodule()
sage: C
Modular Symbols subspace of dimension 1 of Modular Symbols space of dimension 2 for Gamma_0(1) of weight 14 with sign 0 over Finite Field of size 5
sage: C.is_simple()
False
sage: C.simple_factors()

[Modular Symbols subspace of dimension 1 of Modular Symbols space of dimension 2 for Gamma_0(1) of weight 14 with sign 0 over Finite Field of size 5,
 Modular Symbols subspace of dimension 0 of Modular Symbols space of dimension 2 for Gamma_0(1) of weight 14 with sign 0 over Finite Field of size 5]
```




---

Comment by craigcitro created at 2008-01-21 06:10:22

Changing assignee from was to craigcitro.


---

Comment by craigcitro created at 2008-01-21 06:10:22

Changing status from new to assigned.


---

Attachment

Added a patch to fix this. I actually add the _is_simple flag when the cuspidal subspace is created -- when that's one-dimensional, we know it must be simple, so it seems easier to tag it then, rather than do something involving checking stability under the Hecke operators ...


---

Comment by mabshoff created at 2008-01-21 07:59:43

Resolution: fixed


---

Comment by mabshoff created at 2008-01-21 07:59:43

Merged in Sage 2.10.1.alpha1
