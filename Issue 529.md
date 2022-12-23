# Issue 529: Add hex printing for FiniteFieldElements

Issue created by migration from https://trac.sagemath.org/ticket/529

Original creator: malb

Original creation time: 2007-08-30 16:19:12

Assignee: somebody

Let k = GF(2**n). Often elements in k are represented using hexstrings in literature (e.g. cryptography). Thus, allowing finite field elements to be printed as hex strings is sometimes convenient. A decision whether this should happen in big endian or little endian ordering would be required also. SAGE prefers little endian while most literature seems to prefer big endian ordering in that case.


---

Comment by was created at 2007-08-31 23:32:32

Changing assignee from somebody to malb.


---

Comment by malb created at 2007-10-21 22:53:06

Changing status from new to assigned.


---

Comment by malb created at 2008-01-18 16:26:34

Resolution: wontfix


---

Comment by malb created at 2008-01-18 16:26:34

I don't think that this would be such an awesome idea anymore, invalidating it.
