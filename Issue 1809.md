# Issue 1809: [with patch] refactoring to improve finite field reference manual

Issue created by migration from Trac.

Original creator: malb

Original creation time: 2008-01-17 21:29:18

Assignee: mabshoff

The patch removes `FiniteField_prime_modn` from `finite_field.py` because it was odd that this implementation was the only showing up in the reference manual. Also, `GF` is now defined in `rings.all` rather than in `rings.finite_field` to avoid that the documentation for it shows up twice. Finally, a more verbose description of the finite field module is given at the top of the `finite_field.py` file and some doctests were added to `FiniteField_prime_modn`.


---

Comment by malb created at 2008-01-17 22:14:08

Resolution: duplicate
