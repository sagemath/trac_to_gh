# Issue 967: [with patch] inplace operators for GF(p),GF(p^n) and MPolynomial_libsingular

Issue created by migration from Trac.

Original creator: malb

Original creation time: 2007-10-21 22:37:50

Assignee: somebody

The attached patches implement inplace operators for `IntegerMod`, `FiniteFieldElement_givaro` and `MPolynomial_libsingular`.

Some timings for GF(q)

Before:


```
sage: k.<a> = GF(2^15)
sage: A = [a^i for i in range(k.order())]
sage: %timeit _ = sum(A)
100 loops, best of 3: 6.79 ms per loop
```


After:


```
sage: k.<a> = GF(2^15)
sage: A = [a^i for i in range(k.order())]
sage: %timeit _ = sum(A)
100 loops, best of 3: 2.05 ms per loop
```



---

Attachment


---

Attachment


---

Comment by malb created at 2007-10-21 22:44:27

Changing assignee from somebody to malb.


---

Comment by malb created at 2007-10-21 22:44:27

Changing status from new to assigned.


---

Comment by malb created at 2007-10-23 19:55:30

Resolution: fixed


---

Comment by malb created at 2007-10-23 19:55:30

This was applied to 2.8.9.alpha0
