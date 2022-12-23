# Issue 2542: [with patch, needs review] implement right_kernel() and right_nullity() for matrices

Issue created by migration from https://trac.sagemath.org/ticket/2542

Original creator: AlexGhitza

Original creation time: 2008-03-16 03:49:14

Assignee: was

I implemented right_kernel() and right_nullity() for matrices in the simplest possible way (calling the left_ functions on the transpose of self).  This is a tiny little step in the direction of #1607.



---

Attachment


---

Comment by mhansen created at 2008-03-16 04:13:05

Looks good to me.  Apply 2542-2.patch which is rebased against 2.10.4.alpha0.


---

Comment by mabshoff created at 2008-03-16 05:39:48

This patch causes a doctest failure for me:

```
sage -t -long devel/sage/sage/matrix/matrix2.pyx
**********************************************************************
File "matrix2.pyx", line 1170:
    sage: A.right_nullity()
Expected:
    1
Got:
    0
**********************************************************************
1 items had failures:
   1 of   4 in __main__.example_26
***Test Failed*** 1 failures.
For whitespace errors, see the file .doctest_matrix2.pyx
```


Cheers,

Michael


---

Comment by mabshoff created at 2008-03-16 06:45:10


```
[06:34] <mhansen> mabshoff: For 2542, the doctest is wrong and the answer returned is correct.
```


Cheers,

Michael


---

Comment by mabshoff created at 2008-03-16 07:06:50

Resolution: fixed


---

Comment by mabshoff created at 2008-03-16 07:06:50

Merged 2542-2.patch with corrected doctest in Sage 2.10.4.rc0
