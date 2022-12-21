# Issue 4439: Sage 3.2.a2: make three doctests from #788 random again

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2008-11-04 13:57:11

Assignee: mabshoff

The following tests should be made random again:

```
(make #random again)
sage -t  devel/sage/sage/matrix/matrix_complex_double_dense.pyx
**********************************************************************
File "/home/mabshoff/build-3.2.a2/sage-3.2.alpha2-menas/tmp/matrix_complex_double_dense.py", line 899:
    sage: U*S*V.transpose()
Expected:
    [...e-1...                1.0]
    [               2.0                3.0]
    [               4.0                5.0]
Got:
    [  0 1.0]
    [2.0 3.0]
    [4.0 5.0]
**********************************************************************

(make random again)
sage -t  devel/sage/sage/matrix/matrix_real_double_dense.pyx
**********************************************************************
File "/home/mabshoff/build-3.2.a2/sage-3.2.alpha2-menas/tmp/matrix_real_double_dense.py", line 786:
    sage: U*S*V.transpose()
Expected:
    [...e-1...               1.0               2.0]
    [              3.0               4.0               5.0]
Got:
    [0.0 1.0 2.0]
    [3.0 4.0 5.0]
**********************************************************************
File "/home/mabshoff/build-3.2.a2/sage-3.2.alpha2-menas/tmp/matrix_real_double_dense.py", line 794:
    sage: U*S*V.transpose()
Expected:
    [...e-1...                1.0]
    [               2.0                3.0]
    [               4.0                5.0]
Got:
    [0.0 1.0]
    [2.0 3.0]
    [4.0 5.0]
**********************************************************************
```



---

Attachment

Looks good.


---

Comment by mabshoff created at 2008-11-05 23:14:25

Merged in Sage 3.2.alpha3


---

Comment by mabshoff created at 2008-11-05 23:14:25

Resolution: fixed
