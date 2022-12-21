# Issue 929: wrap fpLLL-2.0

Issue created by migration from Trac.

Original creator: malb

Original creation time: 2007-10-19 17:29:00

Assignee: malb

Damien Stehle published a new and much improved version of his fpLLL package at http://perso.ens-lyon.fr/damien.stehle/english.html . This should be wrapped for SAGE instead of fpLLL-1.3. This makes the fpLLL patch attached to #723 obsolete and should also provide SAGE with a performance comparable to MAGMA for LLL computations.


---

Attachment

The attached patch requires http://sage.math.washington.edu/home/malb/pkgs/libfplll-2.0-20071020.spkg to be installed. After that package has be installed and the patch was applied, fpLLL is the default implementation for Matrix_integer_dense.LLL. I'd appreciate if somebody more into LLL would check my documentation.


---

Comment by malb created at 2007-10-21 16:24:12

The mandatory benchmarks of Stehle vs. Stehle :-)


```
sage: a = random_matrix(ZZ,200)
sage: time b=a.LLL()
CPU times: user 1.90 s, sys: 0.02 s, total: 1.92 s
Wall time: 1.94
sage: m = magma(a)
sage: time c=m.LLL()
CPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s
Wall time: 1.53

sage: a = random_matrix(ZZ,400)
sage: time b=a.LLL()
CPU times: user 18.77 s, sys: 0.11 s, total: 18.88 s
Wall time: 19.08
sage: time c=magma(a)
CPU times: user 0.31 s, sys: 0.04 s, total: 0.34 s
Wall time: 0.54
sage: time d=c.LLL()
CPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s
Wall time: 19.48
```


Also, the `sage.libs.fplll.fplll` module contains several generators for random matrices with interesting shapes.


---

Comment by malb created at 2007-10-21 22:44:29

Changing status from new to assigned.


---

Comment by malb created at 2007-10-23 19:39:38

This is applied to 2.8.9.alpha0 and thus fixed.


---

Comment by malb created at 2007-10-23 19:39:38

Resolution: fixed
