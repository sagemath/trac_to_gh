# Issue 4280: Syntax error for a comment line, then help query in a notebook cell

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2008-10-14 10:02:49

Assignee: boothby

In Sage (up through 3.1.3rc0), paste this into a notebook cell:


```
#
graphs?
```


and you get a syntax error when evaluating.  Removing the comment makes it work fine.


---

Attachment


---

Comment by mhansen created at 2009-01-24 04:48:55

Changing assignee from boothby to mhansen.


---

Comment by mhansen created at 2009-01-24 04:48:55

Changing status from new to assigned.


---

Comment by mhansen created at 2009-01-24 04:50:20

This depends on #3326.


---

Comment by jason created at 2009-02-06 18:19:39

This patch fixes the issue and looks correct.    Positive review.


---

Comment by mabshoff created at 2009-02-07 01:37:18

Merged in Sage 3.3.alpha6.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-07 01:37:18

Resolution: fixed
