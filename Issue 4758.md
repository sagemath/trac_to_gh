# Issue 4758: eigenvalues of matrices over CDF is embarassingly frickin' slow!!!!!!!!!!!! (at least 100 times too slow!)

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-12-11 05:21:06

Assignee: was

CC:  jason

Below we compute the eigenvalues of a 100x100 random matrix over CDF in two ways.  Notices that the second way is 117 times faster than the first.  This is bad. 


```
sage: a = random_matrix(CDF, 100)
sage: time v = a.eigenvalues()
CPU times: user 9.32 s, sys: 0.05 s, total: 9.37 s
Wall time: 9.56 s
sage: a = random_matrix(CDF, 100)
sage: time w = a.left_eigenvectors()[0]
CPU times: user 0.08 s, sys: 0.00 s, total: 0.08 s
Wall time: 0.08 s



---

Comment by mhansen created at 2008-12-11 06:03:28

This is the culprit since all of the specialized methods were removed:

http://www.sagemath.org/hg/sage-main/diff/9550477ef46a/sage/matrix/matrix_complex_double_dense.pyx


---

Comment by mhansen created at 2008-12-11 06:13:47

Changing priority from major to blocker.


---

Comment by mhansen created at 2008-12-11 07:58:50

Changing status from new to assigned.


---

Comment by mhansen created at 2008-12-11 07:58:50

Changing assignee from was to mhansen.


---

Comment by mhansen created at 2008-12-11 07:58:50

Sorry, I didn't see that the specialized methods were moved to matrix_double_dense.pyx.

I've attached a patch to fix this which just uses scipy.linalg.eigvals.


```
sage: sage: a = random_matrix(CDF, 100)
sage: sage: time v = a.eigenvalues()
CPU times: user 0.40 s, sys: 0.05 s, total: 0.45 s
Wall time: 0.47 s
sage: %time w = a.left_eigenvectors()
CPU times: user 0.51 s, sys: 0.00 s, total: 0.51 s
Wall time: 0.65 s
```



---

Comment by mabshoff created at 2008-12-11 08:08:37

Where is the patch? :)

Cheers,

Michael


---

Attachment


---

Comment by jason created at 2008-12-11 08:59:03

Thanks.  Also, in matrix2.pyx, the eigenvalues command caches its result; we may want to add that here.  The code looks good; I can't test it right away.

Note that there was not a special method for eigenvalues in the previous matrix_complex_double_dense.pyx, so the switch to a numpy backend was not the actual culprit.

I'll be able to test this patch in the next day or two.


---

Comment by jason created at 2008-12-11 10:37:02

Also, there should probably be a test illustrating that the eigenvalues returned from an RDF matrix are CDF numbers.


---

Attachment

apply on top of previous patches


---

Comment by jason created at 2008-12-12 21:05:44

Positive review.  I added a few more doctests in the review patch.  Doctests pass in the file.  If caching becomes an issue, we can add it later.


---

Comment by jason created at 2008-12-12 21:06:38

And one more time, this was a NotImplementedError, not a WasHereButThenDeletedError error :).


---

Comment by mabshoff created at 2008-12-13 09:05:50

Merged both patches in Sage 3.2.2.alpha2


---

Comment by mabshoff created at 2008-12-13 09:05:50

Resolution: fixed
