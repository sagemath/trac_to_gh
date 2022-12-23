# Issue 2677: sage 2.11.alpha1: doctest failures in real_double_dense.pyx

Issue created by migration from https://trac.sagemath.org/ticket/2677

Original creator: dfdeshom

Original creation time: 2008-03-26 18:04:16

Assignee: dfdeshom


```
Re the doctest failure on Clement's G5:

sage -t  devel/sage-main/sage/matrix/matrix_real_double_dense.pyx
**********************************************************************
File "matrix_real_double_dense.pyx", line 331:
    sage: ~A
Expected:
    [ 0.1  0.0]
    [ 0.0 0.01]
Got:
    [ 0.1 -0.0]
    [-0.0 0.01]
**********************************************************************
File "matrix_real_double_dense.pyx", line 349:
    sage: A.inverse()
Expected:
    [nan nan]
    [nan inf]
Got:
    [ nan  nan]
    [ nan -inf]
**********************************************************************

It is a sign issue, but I am not sure what we can do here.

Cheers,

Michael 
```



---

Attachment


---

Comment by mabshoff created at 2008-03-26 22:16:45

Patch looks good to me and fixes the issue. Positive review.


---

Comment by mabshoff created at 2008-03-26 22:18:18

Merged in Sage 2.11.alpha2


---

Comment by mabshoff created at 2008-03-26 22:18:18

Resolution: fixed
