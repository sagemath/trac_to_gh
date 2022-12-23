# Issue 5957: 3.4.2.rc0: Maxima related doctest failure in matrix/matrix_symbolic_dense.pyx

Issue created by migration from https://trac.sagemath.org/ticket/5957

Original creator: mabshoff

Original creation time: 2009-05-01 13:34:36

Assignee: mabshoff

This happens with gcc 4.3.3 on iras and cicero:

```
sage -t -long "devel/sage/sage/matrix/matrix_symbolic_dense.pyx"
**********************************************************************
File "/home/mabshoff/build-3.4.2.rc0/sage-3.4.2.rc0-ciero-gcc-4.3.3/
devel/sage/sage/matrix/matrix_symbolic_dense.pyx", line 413:
   sage: M.determinant()
Expected:
   4*x - 6
Got:
   determinant(sage513)
**********************************************************************
```



---

Comment by jsp created at 2009-05-03 22:36:13

Maybe it is good to mention I had this failure already in sage-3.4.2.alpha0.

Both with Fedora 9 and 10, 32 bit.

gcc version 4.3.0, resp. 4.3.2

Jaap


---

Attachment


---

Comment by mabshoff created at 2009-05-04 04:54:37

This is William's patch, so I can review it :)

Cheers,

Michael


---

Comment by mabshoff created at 2009-05-04 05:02:01

Positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2009-05-04 05:02:58

Resolution: fixed


---

Comment by mabshoff created at 2009-05-04 05:02:58

Merged in Sage 3.4.2.final.

Cheers,

Michael
