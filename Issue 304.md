# Issue 304: another modular forms bug

Issue created by migration from https://trac.sagemath.org/ticket/304

Original creator: was

Original creation time: 2007-03-01 18:06:29

Assignee: was


```
sage: m = CuspForms(11*2^4,2); m.set_precision(13)
sage: m.integral_basis()
[
q + O(q^13),
q^2 + q^8 + O(q^13),
q^3 + O(q^13),
q^4 + O(q^13),
q^5 + O(q^13),
q^6 + 2*q^8 + O(q^13),
q^7 + q^11 + O(q^13),
q^8 + O(q^13),
q^9 + O(q^13),
q^10 + O(q^13),
q^11 + O(q^13),
q^12 + O(q^13),
1 + O(q^13),
q + 6*q^5 + 2*q^8 + 13*q^9 + O(q^13),
q^2 + 4*q^6 + 6*q^10 + O(q^13),
q^3 + 2*q^7 + O(q^13),
q^4 + 4*q^12 + O(q^13),
3*q^8 + O(q^13),
2*q^11 + O(q^13)
]
```


there shouldn't be a series starting with 1.

Computing everything to higher precision yields the right answer.  So ??


---

Comment by was created at 2007-08-19 01:00:46

Fixed for sage-2.8.2


---

Comment by was created at 2007-08-19 01:00:46

Resolution: fixed
