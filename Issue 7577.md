# Issue 7577: move multivariate polynomials over RR to libsingular

Issue created by migration from Trac.

Original creator: malb

Original creation time: 2009-12-01 23:14:00

Assignee: malb

CC:  burcin nchoen

Singular supports real numbers as 'base field', we only need to implement the conversion routines.


---

Attachment

I am CCing burcin because he knows libSingular and I am CCing ncohen because I wrote this patch in order to speed up the linear programming interface.


---

Comment by mhansen created at 2009-12-02 13:04:15

Changing status from new to needs_work.


---

Comment by mhansen created at 2009-12-02 13:04:15

I get the following failures with this patch:


```
        sage -t  devel/sage-main/sage/matrix/matrix_sparse.pyx # 1 doctests failed
        sage -t  devel/sage-main/sage/calculus/desolvers.py # Segfault
        sage -t  devel/sage-main/sage/rings/polynomial/multi_polynomial.pyx # 2 doctests failed
        sage -t  devel/sage-main/sage/matrix/matrix_mpolynomial_dense.pyx # 2 doctests failed
```



---

Comment by malb created at 2009-12-02 13:30:21

On what kind of machine?


---

Comment by mhansen created at 2009-12-02 13:31:58

On sage.math.  This is with the new Singular spkg from 7194.


---

Comment by malb created at 2009-12-02 14:13:35

I can reproduce


```
sage -t  devel/sage-main/sage/matrix/matrix_sparse.pyx # 1 doctests failed
sage -t  devel/sage-main/sage/calculus/desolvers.py # Segfault
sage -t  devel/sage-main/sage/matrix/matrix_mpolynomial_dense.pyx # 2 doctests failed
```


but not


```
sage -t  devel/sage-main/sage/rings/polynomial/multi_polynomial.pyx # 2 doctests failed
```


I am attaching a fix for the failures I can reproduce.


---

Comment by malb created at 2009-12-02 14:14:42

There is another issue: Singular uses MPF instead of MPFR to implement floating point numbers. Thus, we get less assurance about the precision with this new patch.


---

Comment by malb created at 2009-12-02 14:14:42

Changing status from needs_work to needs_info.


---

Attachment
