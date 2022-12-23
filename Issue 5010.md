# Issue 5010: [with patch, needs review] Solaris 10: rings/real_double.pyx doctests failure: nan vs. NaN

Issue created by migration from https://trac.sagemath.org/ticket/5010

Original creator: mabshoff

Original creation time: 2009-01-18 06:39:47

Assignee: mabshoff

We are seeing the following doctest failure:

```
**********************************************************************
File "/home/mabshoff/build-3.2.3.final/sage-3.2.3.final-fulvia/devel/sage/sage/rings/real_double.pyx", line 1311:
    sage: RDF(0).log()
Expected:
    -inf
Got:
    -Infinity
**********************************************************************
File "/home/mabshoff/build-3.2.3.final/sage-3.2.3.final-fulvia/devel/sage/sage/rings/real_double.pyx", line 1313:
    sage: RDF(-1).log()
Expected:
    nan
Got:
    -NaN
```

This is because we are using the C library instead of RDF to create inf and nan.

Note that this is a different issue than #672.

Cheers,

Michael


---

Attachment


---

Comment by craigcitro created at 2009-01-18 12:35:05

This looks good.


---

Comment by mabshoff created at 2009-01-18 13:57:34

Resolution: fixed


---

Comment by mabshoff created at 2009-01-18 13:57:34

Merged in Sage 3.3.alpha0
