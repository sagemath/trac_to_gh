# Issue 5354: [with patch, needs review] stop paying attention to <stdlib.h> RAND_MAX (should fix problems on Solaris)

Issue created by migration from Trac.

Original creator: cwitty

Original creation time: 2009-02-24 02:21:00

Assignee: mabshoff

The randstate framework always provides 31-bit random numbers regardless of platform, so RAND_MAX should be ignored.


---

Attachment


---

Comment by mabshoff created at 2009-02-24 07:15:59

Nice. Positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-24 19:50:21

Resolution: fixed


---

Comment by mabshoff created at 2009-02-24 19:50:21

Merged in Sage 3.4.alpha0.

Cheers,

Michael
