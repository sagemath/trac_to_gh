# Issue 2834: [with patch, needs review] PyLint import cleanup for sage.rings.polynomial

Issue created by migration from https://trac.sagemath.org/ticket/2834

Original creator: malb

Original creation time: 2008-04-06 22:18:51

Assignee: cwitty

Keywords: pylint

I ran `pylint --enable-checker=imports` on `sage.rings.polynomial` and attempted to fix what it reported
 * relative imports
 * double imports
 * circular imports

The patch could be considered controversial, please check carefully.


---

Attachment

All tests pass for me.  I'd give it a positive review, but I'd also like to hear others' comments.


---

Comment by mabshoff created at 2008-04-07 00:04:49

I like this patch. But after applying and doing a `sage -ba` I see the following failure with `-long`:

```
sage -t -long devel/sage/sage/coding/linear_code.py         
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.0.alpha2/tmp/linear_code.py", line 724:
    sage: C.chinen_polynomial()       # long time
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/release-cycle/sage-3.0.alpha2/local/lib/python2.5/doctest.py", line 1212, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_12[2]>", line 1, in <module>
        C.chinen_polynomial()       # long time###line 724:
    sage: C.chinen_polynomial()       # long time
      File "/scratch/mabshoff/release-cycle/sage-3.0.alpha2/local/lib/python2.5/site-packages/sage/coding/linear_code.py", line 737, in chinen_polynomial
        from sage.rings.polynomial.polynomial_ring import PolynomialRing, polygen
    ImportError: cannot import name PolynomialRing
**********************************************************************
```


Cheers,

Michael


---

Attachment


---

Comment by malb created at 2008-04-07 13:08:08

The attached patch fixes the issue reported by mabshoff and also cleans up `linear_code.py`.


---

Comment by mabshoff created at 2008-04-07 16:05:55

The new patch fixes the issue I reported. Doctests pass after a `-ba` now. Positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2008-04-07 16:08:02

Merged in Sage 3.0.alpha3


---

Comment by mabshoff created at 2008-04-07 16:08:35

Merged in Sage 3.0.alpha2 - an now it is closed, too. ;)


---

Comment by mabshoff created at 2008-04-07 16:08:35

Resolution: fixed
