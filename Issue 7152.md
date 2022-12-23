# Issue 7152: Segmentation fault with monomials()

Issue created by migration from https://trac.sagemath.org/ticket/7152

Original creator: mraum

Original creation time: 2009-10-08 08:11:11

Assignee: tbd

CC:  mraum@mpim-bonn.mpg.de malb wjp

Keywords: monomials, multivariate polynomial ring, coercion

Using implicite coercion and then calling monomials might cause a segmentation fault. This is a side effect.


```
K.<rho> = NumberField(x**2 + 1)
R.<x,y> = QQ[]
p = rho*x
q = x
p.monomials()
 ...
q.monomials()
 ...
p.monomials()
 Segmentation Fault
```


Going back to line 5 you can avoid this by

```
p.parent()(p).monomials()
 ...
q.parent()(q).monomials()
 ...
p.parent()(p).monomials()
 ...
```

This might be used as a workaround.

If no implicite coercion is involved, everything works fine, i.e. use

```
R.<x,y> = K[]
```


This is most probably related to #6160.


---

Comment by burcin created at 2010-01-17 02:23:58

Changing keywords from "monomials, multivariate polynomial ring, coercion" to "monomials, singular".


---

Comment by burcin created at 2010-01-17 02:23:58

Changing status from new to needs_review.


---

Comment by burcin created at 2010-01-17 02:23:58

This segfaults because the `monomials()` method doesn't set the current ring. attachment:trac_7152-monomials_cring.patch contains the fix.


---

Attachment

set current ring for singular in monomials() method


---

Comment by wjp created at 2010-01-17 17:23:16

Changing status from needs_review to positive_review.


---

Comment by wjp created at 2010-01-17 17:23:16

Looks good.


---

Comment by rlm created at 2010-01-18 23:06:13

Resolution: fixed
