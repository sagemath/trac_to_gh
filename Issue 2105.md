# Issue 2105: Constructor for ntl.GF2X polynomials does not take Polynomials over  GF(2) as advertised by docstring

Issue created by migration from https://trac.sagemath.org/ticket/2105

Original creator: malb

Original creation time: 2008-02-08 09:42:46

Assignee: somebody

Marshall Buck on [sage-support] writes:


```
sage: R.<x> = GF(2)[]
sage: f = x^5+x^2+1
sage: fx = ntl.GF2X(f)
```

gives error:

```
Traceback (most recent call last):    fx
  File "ntl_GF2X.pyx", line 141, in
sage.libs.ntl.ntl_GF2X.ntl_GF2X.__init__
AttributeError: 'sage.rings.polynomial.polynomial_modn_dense_ntl.Po' object has no attribute '_Polynomial_dense_mod_n__poly'
```


`fx = ntl.GF2X(f.list())` works, as well as `fx = ntl.GF2X(f.ntl_ZZ_pX())`


---

Comment by malb created at 2008-02-18 15:25:32

Changing assignee from somebody to malb.


---

Comment by malb created at 2008-02-18 15:25:32

Changing status from new to assigned.


---

Comment by malb created at 2008-02-18 15:33:44

fix


---

Attachment


---

Comment by mhansen created at 2008-02-27 18:26:39

Looks good to me.


---

Comment by cremona created at 2008-02-27 18:30:00

And to me.


---

Comment by mabshoff created at 2008-02-28 00:06:04

Resolution: fixed


---

Comment by mabshoff created at 2008-02-28 00:06:04

Merged in Sage 2.10.3.rc0
