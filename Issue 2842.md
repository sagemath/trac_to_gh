# Issue 2842: [with patch, needs review] PyLint unused variable cleanup for sage.rings.polynomial

Issue created by migration from Trac.

Original creator: malb

Original creation time: 2008-04-07 13:10:29

Assignee: cwitty

Keywords: pylint

The attached patch
 * removes unused variables,
 * removes unused imports,
 * defines undefined variables,

from several files in sage.rings.polynomial. It doesn't fix all issues in that module but this patch is still open for reviews.


---

Attachment


---

Attachment

Looks good to me.  Apply just 2842.patch after #2844 .


---

Comment by mabshoff created at 2008-04-08 00:27:33

I am seeing one doctest failure on sage.math:

```
sage -t -long devel/sage/sage/rings/polynomial/multi_polynomial_libsingular.pyx
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.0.alpha3/tmp/multi_polynomial_libsingular.py", line 496:
    sage: R.<x,y> = QQ[]; S.<xx,yy> = GF(5)[]; S(5*x*y + x + 17*y)
Expected:
    xx + 2*yy
Got:
    xx + 0*yy
**********************************************************************
```

Martin will start poking around tomorrow.

Cheers,

Michael


---

Comment by mabshoff created at 2008-04-08 00:31:13

Note that post the #2844 merge you ought to apply 2842.patch.

Cheers,

Michael


---

Comment by mabshoff created at 2008-04-08 01:55:15

Oh well, just applying #2844 causes the above libSingular failures. So I am merging this patch since it works. I would recommend opening another ticket once somebody else can verify the same issue I see. A compile from scratch on sage.math ought to lead to the same result.

Cheers,

Michael


---

Comment by mabshoff created at 2008-04-08 01:56:36

Merged 2842.patch in Sage 3.0.alpha3


---

Comment by mabshoff created at 2008-04-08 01:56:36

Resolution: fixed
