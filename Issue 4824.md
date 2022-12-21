# Issue 4824: speed up conversion of matrices from sage to pari

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-12-18 01:25:11

Assignee: was

This is kind of sad, given that pari(...) is done entirely in C-level Cython compiled code in memory, and the magma(...) conversion is done using pexpect and the file system!

```
sage: a = random_matrix(ZZ,1000,x=-10,y=10)
sage: time m = magma(a)
CPU times: user 0.14 s, sys: 0.02 s, total: 0.16 s
Wall time: 0.36 s
sage: time b= pari(a)
CPU times: user 21.51 s, sys: 0.72 s, total: 22.23 s
Wall time: 22.24 s
```


Fixing this will help with some algorithms, such as Hermite form. 


---

Comment by tscrim created at 2013-04-02 15:17:52

This was fixed at some point:

```
sage: a = random_matrix(ZZ, 1000, x=-10, y=10)
sage: %time p = pari(a)
CPU times: user 0.20 s, sys: 0.36 s, total: 0.56 s
Wall time: 1.07 s
sage: a = random_matrix(ZZ, 1000, x=-10, y=10)
sage: %time p = pari(a)
CPU times: user 0.17 s, sys: 0.02 s, total: 0.19 s
Wall time: 0.24 s
```



---

Comment by tscrim created at 2013-04-02 15:17:52

Changing status from new to needs_review.


---

Comment by jdemeyer created at 2013-04-09 14:23:06

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2013-04-10 08:13:20

Resolution: worksforme
