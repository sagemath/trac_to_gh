# Issue 3596: can't build tut.tex; latex errors in ref.tex

Issue created by migration from https://trac.sagemath.org/ticket/3596

Original creator: was

Original creation time: 2008-07-07 23:17:21

Assignee: tba




---

Attachment


---

Attachment


---

Attachment

OK, this patch puts the "rm *.ind" back, and simply issues two makes instead of one.  It works fine for me.


---

Comment by mabshoff created at 2008-07-08 00:45:14

All three patches look good to me. Positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2008-07-08 00:46:06

Resolution: fixed


---

Comment by mabshoff created at 2008-07-08 00:46:06

Merged in Sage 3.0.4.rc0
