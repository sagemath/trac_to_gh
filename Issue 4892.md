# Issue 4892: Changing precision of a Complex can convert it to a real

Issue created by migration from https://trac.sagemath.org/ticket/4892

Original creator: cremona

Original creation time: 2008-12-30 09:40:16

Assignee: somebody

Keywords: real complex precision

georg.grafendorfer reported this to sage-support:

```
sage: a = CC(-5).n(prec=100)
sage: b = ComplexField(100)(-5)
sage: a == b
True
sage: type(a) == type(b)
False
sage: ln(a)
NaN
sage: ln(b)
1.6094379124341003746007593332 + 3.1415926535897932384626433833*I
```

The issue is that both a and b are equal to -5 (exactly, to 100 bit precision) but a is a Real while b is a Complex.  This happens because 

```
Looking at the code for numerical_approx() in sage.misc.functional,
this happens because the attempt to coerce z into RealField(100)
succeeds.  To fix this (if it is agreed that it is a bug) that
function would need to test the type of the input and return something
of the same type (real/complex).
```

The suggested fix is that the numerical_approx function should always return a complex number to the appropriate precsion if the input has type complex, even if the coercion into a real succeeded.


---

Attachment


---

Comment by rlm created at 2009-01-22 06:50:57

Changing status from new to assigned.


---

Comment by rlm created at 2009-01-22 06:50:57

Changing assignee from somebody to rlm.


---

Comment by AlexGhitza created at 2009-01-23 20:34:13

Looks good to me.


---

Comment by mabshoff created at 2009-01-25 02:13:22

This patch causes the following doctest failure:

```
mabshoff@geom:/scratch/mabshoff/sage-3.3.alpha2$ ./sage -t -long devel/sage/sage/modules/vector_double_dense.pyx
sage -t -long "devel/sage/sage/modules/vector_double_dense.pyx"
**********************************************************************
File "/scratch/mabshoff/sage-3.3.alpha2/devel/sage/sage/modules/vector_double_dense.pyx", line 531:
    sage: _.parent()
Expected:
    Vector space of dimension 3 over Real Field with 53 bits of precision
Got:
    Vector space of dimension 3 over Complex Field with 53 bits of precision
**********************************************************************
File "/scratch/mabshoff/sage-3.3.alpha2/devel/sage/sage/modules/vector_double_dense.pyx", line 535:
    sage: _.parent()
Expected:
    Vector space of dimension 3 over Real Field with 75 bits of precision
Got:
    Vector space of dimension 3 over Complex Field with 75 bits of precision
**********************************************************************
```


Given that this is vector_double_dense.pyx it seems odd.

Cheers,

Michael


---

Comment by AlexGhitza created at 2009-01-25 02:30:30

Oops I should have tested modules/ during the review of rlm's patch.

But the doctests were indeed wrong to start with, the vector spaces *should* be complex.  I've added a trivial patch that fixes this.


---

Attachment

apply after the other patch


---

Comment by rlm created at 2009-01-25 21:22:55

+1 to the second patch


---

Comment by mabshoff created at 2009-01-28 15:23:18

Merged both patches in Sage 3.3.alpha3.

Cheers,

Michael


---

Comment by mabshoff created at 2009-01-28 15:23:18

Resolution: fixed
