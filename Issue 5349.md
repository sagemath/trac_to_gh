# Issue 5349: [with patch, needs review] Make extensions linking against libSingular depend on $SAGE_LOCAL/include/libsingular.h

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2009-02-23 15:07:57

Assignee: mabshoff

CC:  georgsweber

The summary says it all. It causes the extensions to be automatically being rebuild when the singular.spkg has been rebuild.

Georg: Can you review this?

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-23 15:08:19

Changing status from new to assigned.


---

Attachment


---

Comment by cwitty created at 2009-02-23 19:05:35

I tested it; it works.  Positive review.


---

Comment by mabshoff created at 2009-02-24 19:51:53

Merged in Sage 3.4.alpha0.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-24 19:51:53

Resolution: fixed
