# Issue 8264: swap_row does not work on modular matrices

Issue created by migration from https://trac.sagemath.org/ticket/8264

Original creator: janwil123

Original creation time: 2010-02-14 17:50:43

Assignee: was

For some reason, swap_row does not work if the elements of the matrix are treated as integers modulo something. The code to reproduce the bug is the following:



```
A = matrix(ZZ, 2,[1,2,3,4])
B = copy(A)
B.swap_rows(0,1)
print B,'\n'
B.swap_columns(0,1) # So far so good
print B,'\n'
C = A.apply_map(lambda x:mod(x,8))
C.swap_rows(0,1) # This line does not work
print C,'\n'
C.swap_columns(0,1) # But this one does
print C
```


The bug reproduces every time on Mac OSX 10.6, SAGE version 4.3.1.


---

Attachment


---

Comment by mhansen created at 2010-03-05 23:29:27

Changing status from new to needs_review.


---

Comment by nborie created at 2010-03-06 10:14:20

The patch fix the ticket and add the good test.

Positive review from me.


---

Comment by nborie created at 2010-03-06 10:14:20

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2010-03-06 23:57:22

Resolution: fixed
