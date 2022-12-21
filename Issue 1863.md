# Issue 1863: implement f.change_ring(R) for f a multivariate polynomial

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-01-20 16:36:56

Assignee: malb

This works:

```
sage: R.<x> = QQ[]
sage: f = x^3 + 3/5
sage: f.change_ring(GF(7))
x^3 + 2
```

This should work:

```
sage: R.<x,y> = QQ[]
sage: f = x^3 + 3/5*y + 1
sage: f.change_ring(GF(7))
Traceback (most recent call last):
...
AttributeError: 'sage.rings.polynomial.multi_polynomial_libsingular' object has no attribute 'change_ring'
```



---

Attachment


---

Comment by malb created at 2008-03-28 12:11:46

The attached patch implements `change_ring`.


---

Attachment


---

Comment by mhansen created at 2008-03-31 14:46:59

Looks good to me.  1863.patch is rebased and the one to apply.


---

Comment by mabshoff created at 2008-03-31 15:01:53

Merged trac_1863_change_ring.patch in Sage 3.0.alpha0


---

Comment by mabshoff created at 2008-03-31 15:01:53

Resolution: fixed
