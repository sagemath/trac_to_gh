# Issue 660: allow reverse order if converting GF(p^n) element to GF(p)^n element [with patch]

Issue created by migration from https://trac.sagemath.org/ticket/660

Original creator: malb

Original creation time: 2007-09-15 13:10:14

Assignee: somebody

Let $e \in GF(q)$. Then `e.vector()` is implemented in little endian ordering in SAGE. This patch allows to reverse this order.


---

Attachment


---

Comment by was created at 2007-09-21 02:37:14

could use doctests.


---

Comment by was created at 2007-09-21 02:39:00

Resolution: fixed


---

Comment by was created at 2007-09-21 02:39:00

i added doctests to official repo.
