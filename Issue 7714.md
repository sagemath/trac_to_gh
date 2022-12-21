# Issue 7714: bug in matrix rank over multivariate polynomial ring

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-12-16 16:37:08

Assignee: malb

CC:  burcin


```
sage: matrix([PolynomialRing(GF(2),2,'x').gen()]).rank()
[x0]
1
{(0, 0): x0}
---------------------------------------------------------------------------
RuntimeError                              Traceback (most recent call last)

/scratch/wstein/sage/temp/sage.math.washington.edu/22996/_scratch_wstein_sage_init_sage_0.py in <module>()

/scratch/wstein/build/sage-4.3.rc0/local/lib/python2.6/site-packages/sage/matrix/matrix0.so in sage.matrix.matrix0.Matrix.rank (sage/matrix/matrix0.c:16202)()

/scratch/wstein/build/sage-4.3.rc0/local/lib/python2.6/site-packages/sage/matrix/matrix0.so in sage.matrix.matrix0.Matrix.pivots (sage/matrix/matrix0.c:16074)()

RuntimeError: BUG: matrix pivots should have been set but weren't, matrix parent = 'Full MatrixSpace of 1 by 1 dense matrices over Multivariate Polynomial Ring in x0, x1 over Finite Field of size 2'
```



---

Comment by malb created at 2010-07-12 15:24:50

Changing status from new to needs_review.


---

Comment by jason created at 2010-09-23 22:55:37

This shouldn't print out things before throwing the error.


---

Comment by jason created at 2010-09-23 22:55:37

Changing status from needs_review to needs_work.


---

Attachment

Fixed.


---

Comment by malb created at 2010-11-03 15:34:02

Changing status from needs_work to needs_review.


---

Comment by malb created at 2010-11-23 17:36:06

Jason, can you take another look at this ticket?


---

Comment by lftabera created at 2010-12-04 16:51:48

The bug of the ticket is correctly solved by the patch. However, current doctest just shows that the bug is solved by a corner case, but not a normal usage. Please, add an example of a normal case. Something like a 3x4 matrix of rank 2.


---

Comment by lftabera created at 2010-12-04 16:51:48

Changing status from needs_review to needs_work.


---

Attachment


---

Comment by lftabera created at 2011-09-13 11:11:04

Changing status from needs_work to needs_review.


---

Comment by lftabera created at 2011-09-13 11:11:04

I give a positive review to Martin's patch.

I also send a reviewr patch uptading the doctest (pivots return a tuple) and adding another example.


---

Comment by malb created at 2011-09-13 11:44:16

Reviewer patch looks good.


---

Comment by malb created at 2011-09-13 11:44:16

Changing status from needs_review to positive_review.


---

Comment by leif created at 2011-09-17 04:30:02

Resolution: fixed
