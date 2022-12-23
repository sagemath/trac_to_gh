# Issue 3920: [with patch, needs review] FiniteFieldElement.vector/matrix -> _vector_/_matrix_

Issue created by migration from https://trac.sagemath.org/ticket/3920

Original creator: malb

Original creation time: 2008-08-21 09:01:34

Assignee: was

CC:  robertwb

While reading the Developer's guide update at #3905 it occurred to me that `vector()`/`matrix()` methods are supposed to be called `_vector_`/`_matrix_()` methods so that `matrix(foo)` works. The attached patch changes those functions for finite field elements.


---

Comment by malb created at 2008-09-20 16:00:20

Changing status from new to assigned.


---

Comment by malb created at 2008-09-20 16:00:20

Changing assignee from was to malb.


---

Comment by jason created at 2008-09-26 16:15:19

Just a short comment: could you put back in the matrix() and vector() functions and add a deprecation warning for now?  That way code doesn't suddenly break.


---

Attachment

Since you use "\code" in the docstring for vector and matrix, the docstrings need to start with r""" instead of """.  Patch attached.


---

Attachment

apply after malb's patch


---

Comment by jhpalmieri created at 2008-10-17 21:30:45

Otherwise, your patch looks good to me. Now I finally know of an example of the `_vector_` method -- I was looking for one when I was revising the Developer's guide...

I've doctested the changed files with complete success. I'm currently running `sage -testall` to make sure nothing else is screwed up by this. I'll give it a tentative positive review now while I'm thinking about it, then change it one way or the other depending on how the testing works out.


---

Comment by jhpalmieri created at 2008-10-17 22:55:24

All tests passed!


---

Comment by mabshoff created at 2008-10-18 10:30:41

Positive review on John's additional patch.

Cheers,

Michael


---

Comment by mabshoff created at 2008-10-18 10:33:54

Robert: This patch touches

 * sage/rings/finite_field_givaro.pyx
 * sage/rings/finite_field_ntl_gf2e.pyx

Cheers,

Michael


---

Comment by mabshoff created at 2008-10-18 11:05:47

Merged both patches in Sage 3.2.alpha0


---

Comment by mabshoff created at 2008-10-18 11:05:47

Resolution: fixed
