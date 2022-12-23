# Issue 3890: exact division syntax in finite fields of prime order

Issue created by migration from https://trac.sagemath.org/ticket/3890

Original creator: jbmohler

Original creation time: 2008-08-18 13:56:34

Assignee: somebody

It appears that the // operator is supported for most fields, but not for GF(prime).

The example involving GF(7,'a') should not produce a TypeError.


```
sage: GF(49,'a')(121)//GF(49,'a')(124)
6
sage: GF(7,'a')(121)//GF(7,'a')(124)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/joel/sage-patches/<ipython console> in <module>()

TypeError: unsupported operand type(s) for //: 'sage.rings.integer_mod.IntegerMod_int' and 'sage.rings.integer_mod.IntegerMod_int'
```




---

Attachment


---

Comment by kedlaya created at 2009-01-23 21:49:21

Not much to say here. Positive review.


---

Comment by mabshoff created at 2009-01-25 20:58:30

Merged in Sage 3.3.alpha3.

Cheers,

Michael


---

Comment by mabshoff created at 2009-01-25 20:58:30

Resolution: fixed
