# Issue 46: modular symbols -- crash when computing an eigenform

Issue created by migration from https://trac.sagemath.org/ticket/46

Original creator: was

Original creation time: 2006-09-13 03:40:57

Assignee: was


```
sage: M = ModularSymbols(12,4,sign=1).cuspidal_submodule()

sage: M.decomposition()[1].q_eigenform(10)
Traceback (most recent call last):
...
TypeError: Unable to coerce x (=[   0    1   -1    0 -7/2  7/2  3/2 -3/2    0]) to a morphism in Set of Morphisms from Modular Symbols subspace of dimension 1 of Modular Symbols space of dimension 9 for Gamma_0(12) of weight 4 with sign 1 over Rational Field to Modular Symbols space of dimension 9 for Gamma_0(12) of weight 4 with sign 1 over Rational Field in Category of sets
```




---

Comment by was created at 2006-09-13 03:52:45

It's really A.factorization() that's not implemented yet when A involves old forms.


---

Comment by was created at 2006-09-13 03:57:29

The factorization fails because A.degeneracy_map(1)  fails.


---

Comment by was created at 2006-09-13 04:11:05

Resolution: fixed


---

Comment by was created at 2006-09-13 04:11:05

OK, fixed.  The problem was that a self.category() instead of sub.category() in modules/matrix_morphism.py
