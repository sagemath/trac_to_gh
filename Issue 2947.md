# Issue 2947: [with patch; needs review] block_matrix([]) fails

Issue created by migration from https://trac.sagemath.org/ticket/2947

Original creator: wjp

Original creation time: 2008-04-17 22:19:05

Assignee: was

While debugging #2946 on IRC, Jason found that `block_matrix()` doesn't properly handle an empty list.

The attached patch makes `block_matrix([])` return a 0x0 matrix over ZZ. If nrows and ncols are also specified, and subdivide isn't false, this 0x0 matrix will be further subdivided into nrows x ncols 0x0 matrices. This subdivision might be overkill, but it's probably the most consistent return value. Other opinions are welcome, of course.


---

Attachment


---

Comment by mhansen created at 2008-04-18 03:24:21

Looks good to me.


---

Comment by mabshoff created at 2008-04-18 06:15:16

There are rejection problems [with or without #2946 applied]:

```
mabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.0.alpha6/devel/sage$ patch -p1 < trac_2947_block_matrix_empty.patch
patching file sage/matrix/constructor.py
mabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.0.alpha6/devel/sage$ patch -p1 < trac_2946_noninvertible_jordan_form.patch
patching file sage/matrix/matrix2.pyx
Hunk #1 succeeded at 3591 (offset 59 lines).
Hunk #2 FAILED at 3601.
Hunk #3 FAILED at 3630.
2 out of 3 hunks FAILED -- saving rejects to file sage/matrix/matrix2.pyx.rej
(reverse-i-search)`rm': patch -p1 < trac_2946_noninvertible_jordan_form.patch
```


Cheers,

Michael


---

Comment by mabshoff created at 2008-04-18 06:17:55

Disregard the last comment, it should have been on the #2947 ticket. My bad.

Cheers,

Michael


---

Comment by mabshoff created at 2008-04-18 06:18:10

Resolution: fixed


---

Comment by mabshoff created at 2008-04-18 06:18:10

Merged in Sage 3.0.alpha6
