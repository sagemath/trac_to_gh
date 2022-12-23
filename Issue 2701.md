# Issue 2701: simple bug fixed for linear_codes

Issue created by migration from https://trac.sagemath.org/ticket/2701

Original creator: wdj

Original creation time: 2008-03-28 17:22:00

Assignee: rlm

The attached patch fixes two bugs - one in spectrum and one in zeta_polynomial,
both of which either failed or behaved badly for codes over non-prime fields.
I also added som doctests for non-prime fields. 

It passes sage -testall except for plot.py and polynomial_modn_dense_ntl.pyx.
(I reran sage -t on polynomial_modn_dense_ntl.pyx and it passed the second time.)
I think these have nothing to do with the patch but here are the details:

sage -t  devel/sage-coding/sage/rings/polynomial/polynomial_modn_dense_ntl.pyx**********************************************************************
File "polynomial_modn_dense_ntl.pyx", line 495:
    sage: q == qbar - d
Expected:
    True
Got:
    False
**********************************************************************
1 items had failures:
   1 of  37 in __main__.example_10
***Test Failed*** 1 failures.

sage -t  devel/sage-coding/sage/plot/plot.py                **********************************************************************
File "plot.py", line 3506:
    sage: plot(x^(1/3), (x,-1,1))
Expected nothing
Got:
    WARNING: When plotting, failed to evaluate function at 100 points.
    Last error message: 'negative number cannot be raised to a fractional power'
    <BLANKLINE>
**********************************************************************
1 items had failures:
   1 of  28 in __main__.example_111
***Test Failed*** 1 failures.


---

Attachment


---

Comment by wdj created at 2008-03-28 17:24:37

The attachment is based on sage-2.11.alpha1


---

Comment by mabshoff created at 2008-03-28 18:08:53

Both of the above failures have been fixed in 2.11.alpha2, out in a couple hours at the most.

Cheers,

Michael


---

Comment by rlm created at 2008-03-28 22:17:42

Looks good. As long as the tests pass, I say apply.


---

Comment by mabshoff created at 2008-03-29 00:03:22

Merged in Sage 2.11.alpha2


---

Comment by mabshoff created at 2008-03-29 00:03:22

Resolution: fixed


---

Attachment

A doctest fix for a long case


---

Comment by mabshoff created at 2008-03-29 00:43:18

David,

the new patch fixes a doctest failure. Mathematically those two polynomials are mathematically equivalent, but can you confirm that this is the correct fix.

Cheers,

Michael
