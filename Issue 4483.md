# Issue 4483: Add coefficient_field() method to ModularSymbols/ModularForms

Issue created by migration from https://trac.sagemath.org/ticket/4483

Original creator: jonhanke

Original creation time: 2008-11-09 22:43:46

Assignee: craigcitro

## Define a newform (up to conjugation)
`time nf = ModularSymbols(100,2,1).cuspidal_subspace().new_subspace().decomposition()[0]`

`nf.coefficient_field()` -- should return the field of definition of the newform.  (This appears to be accomplished with `nf.eigenvalue(1).parent()`.  It would be nice to know that this really does give the field of definition.)

`nf.degree()` -- should return the degree of the coefficient field.


---

Comment by AlexGhitza created at 2010-01-05 11:23:33

There is something like this in Sage: look at the class `Newform` in modular/modform/element.py.  It has a method `hecke_eigenvalue_field()` which returns the field of definition of the newform.  There is no `degree()` method, although that's of course easy to get at this point as `nf.hecke_eigenvalue_field().degree()`.

It remains to add such a method to modular symbols (`nf.eigenvalue(1).parent()` is indeed correct), and maybe make `coefficient_field()` an alias for `hecke_eigenvalue_field()`.
