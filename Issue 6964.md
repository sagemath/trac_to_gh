# Issue 6964: implement computation of Dirichlet character of irreducible cuspidal modular symbols space

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-09-20 00:43:57

Assignee: tbd

Implement this function q_eigenform_character described below:

```
sage: f = ModularSymbols(Gamma1(13),2,sign=1).cuspidal_subspace().decomposition()[0]
sage: f.q_eigenform(5,'a')
q + a*q^2 + (-2*a - 4)*q^3 + (-a - 1)*q^4 + O(q^5)
sage: f.q_eigenform_character('a')
Traceback (most recent call last):
...
AttributeError: 'ModularSymbolsSubspace' object has no attribute 'q_eigenform_character'
```


In case f.character() is not None, the above function should be easy to implement -- just return the character.  Otherwise it is harder.


---

Attachment


---

Attachment


---

Attachment


---

Attachment

fix warning when building reference manual


---

Comment by mvngu created at 2009-09-24 15:36:55

The patch `trac_6964-formatting-fix.patch` fix a warning when building the reference manual with the previous patches.


---

Comment by mvngu created at 2009-09-24 16:13:54

Merged patches in this order:

 1. `trac_6964.patch`
 1. `trac_6964-part2.patch`
 1. `trac_6964-part3.patch`
 1. `trac_6964-part4.patch`
 1. `trac_6964-formatting-fix.patch`


---

Comment by mvngu created at 2009-09-24 16:13:54

Resolution: fixed


---

Comment by mvngu created at 2009-09-27 10:23:46

There is no 4.1.2.alpha3. Sage 4.1.2.alpha3 was William Stein's release for working on making the notebook a standalone package.
