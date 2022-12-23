# Issue 416: Faster GF(2^n) arithmetic for n >= 16

Issue created by migration from https://trac.sagemath.org/ticket/416

Original creator: malb

Original creation time: 2007-08-10 14:43:59

Assignee: somebody

Using a Python wrapper around Pari is too slow.  ntl.GF2E on the other hand should be a lot faster.


---

Comment by malb created at 2007-10-21 22:54:25

Changing assignee from somebody to malb.


---

Comment by malb created at 2007-10-21 22:54:25

Changing status from new to assigned.


---

Attachment


---

Comment by malb created at 2007-10-25 13:03:34

The attached patch implements GF(2<sup>n</sup>) for n >= 16 using NTL's GF2E and also refactors `FiniteField*` such that writing GF(p<sup>n</sup>) for p<sup>n</sup> >= 2<sup>16</sup> should be easier. This patch also fixes an issue with `ntl.GF2X` and applies cleanly against 2.8.9. 'make test' passes.

Speed:


```
sage: F1 = FiniteField_givaro(2^15,'a')
sage: F2 = FiniteField_ntl_gf2e(2^15,'a')
sage: F3 = FiniteField_ext_pari(2^15,'a')

sage: F1.polynomial()
a^15 + a^5 + a^4 + a^2 + 1
sage: F2.polynomial()
a^15 + a^5 + a^4 + a^2 + 1
sage: F3.polynomial()
a^15 + a^5 + a^4 + a^2 + 1

sage: e1 = F1.random_element(); f1 = F1.random_element()
sage: e2 = F2.random_element(); f2 = F2.random_element()
sage: e3 = F3.random_element(); f3 = F3.random_element()

sage: %timeit e1*f1
1000000 loops, best of 3: 249 ns per loop
sage: %timeit e2*f2
1000000 loops, best of 3: 496 ns per loop
sage: %timeit e3*f3
10000 loops, best of 3: 36.9 µs per loop

sage: %timeit e1+f1
1000000 loops, best of 3: 255 ns per loop
sage: %timeit e2+f2
1000000 loops, best of 3: 391 ns per loop
sage: %timeit e3+f3
10000 loops, best of 3: 12.9 µs per loop
```



---

Comment by cwitty created at 2007-10-27 02:48:13

Resolution: fixed
