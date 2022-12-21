# Issue 4768: magma -- speed up conversion of integer, rational and modn matrices from sage to magma

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-12-12 06:59:56

Assignee: was

By writing a little specialized code, I can probably speed up some of these conversions by an order of magnitude, and also make them way more efficient memory-wise.


---

Comment by was created at 2008-12-12 07:27:04

Here is a before and after over ZZ:
BEFORE:

```
sage: v = random_matrix(ZZ,1000)
sage: time k = magma(v)
CPU times: user 17.03 s, sys: 0.43 s, total: 17.47 s
Wall time: 18.88 s
```


AFTER:

```
sage: m = random_matrix(ZZ,1000,x=0,y=17)
sage: time w = magma(m)
CPU times: user 0.18 s, sys: 0.10 s, total: 0.28 s
Wall time: 1.68 s
```


Here is a before/after over the rational numbers:
BEFORE:

```
sage: m = random_matrix(QQ,1000)
sage: time k = magma(m)
CPU times: user 9.41 s, sys: 0.39 s, total: 9.80 s
Wall time: 11.60 s
```

AFTER:

```
ge: m = random_matrix(QQ,1000)
sage: time k = magma(m)
CPU times: user 0.48 s, sys: 0.16 s, total: 0.64 s
Wall time: 1.16 s
```



---

Attachment

Patch applies cleanly, doctests in sage/matrix pass, reads good.


---

Comment by mabshoff created at 2008-12-12 15:32:44

The matrix_rational_dense.pyx doctest around line 225 needs the line

```
sage: m = matrix(QQ,2,3,[1,2/3,-3/4,1,-2/3,-45/17])
```

added for the doctest to pass.

Cheers,

Michael


---

Attachment

Merged both patches in Sage 3.2.2.alpha2


---

Comment by mabshoff created at 2008-12-12 16:04:31

Resolution: fixed
