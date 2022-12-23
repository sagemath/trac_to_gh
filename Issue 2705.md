# Issue 2705: random_matrix with sparse=True is very slow

Issue created by migration from https://trac.sagemath.org/ticket/2705

Original creator: dfdeshom

Original creation time: 2008-03-28 18:41:29

Assignee: was

Creating a 2000x200 full matrix is much faster than creating a 500x500 sparse matrix:


```
sage: %time A = random_matrix(ZZ,2000)
CPU times: user 0.97 s, sys: 0.28 s, total: 1.25 s
Wall time: 1.25

sage: %time B = random_matrix(ZZ,500,sparse=True)
CPU times: user 7.20 s, sys: 0.00 s, total: 7.20 s
Wall time: 7.20
```



---

Comment by malb created at 2009-01-22 23:09:35

Changing type from defect to enhancement.


---

Comment by ryan created at 2011-06-15 06:34:51

Changing status from new to needs_info.


---

Comment by ryan created at 2011-06-15 06:34:51

could it have anything to do with the fact that a random matrix is not sparse in nature?


---

Comment by ryan created at 2011-06-15 06:46:32

I noted that even when we specify the density of nonzero entries, a sparse matrix still takes a significant amount of time.


```
sage: time B = random_matrix(ZZ, 2000, density=.05, sparse=True)
Time: CPU 7.02 s, Wall: 8.77 s
sage: time A = random_matrix(ZZ 2000, density=.05, sparse=False)
Time: CPU 1.20 s, Wall: 1.70 s
```



---

Comment by ryan created at 2011-06-15 07:12:18

Well...apparently density=.05 is too dense for a 2000x2000 matrix


```
sage: time A = random_matrix(QQ, 2000, density=.01, sparse=True)
Time: CPU 2.17 s, Wall: 2.82 s
sage: time A = random_matrix(QQ, 2000, density=.01, sparse=False)
Time: CPU 3.25 s, Wall: 3.57 s
```


However, sparse matrices in sage are in need of some tender loving care (according to some other sage devs)


---

Comment by ryan created at 2011-06-15 07:14:54

Changing keywords from "" to "sd31".
