# Issue 5189: notebook -- now possible to delete all computation cells

Issue created by migration from Trac.

Original creator: TimothyClemans

Original creation time: 2009-02-05 22:42:23

Assignee: boothby

This is a bug in counting the number of cells to make sure the number is >= 2. The counter should only count computation cells.

Deleting all computation cells makes it impossible to create new ones.


---

Comment by mabshoff created at 2009-02-05 22:44:39

This is definitely a blocker.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-05 22:44:39

Changing priority from major to blocker.


---

Attachment


---

Comment by jason created at 2009-02-06 08:24:04

Changing status from new to assigned.


---

Comment by jason created at 2009-02-06 08:24:04

Changing assignee from boothby to jason.


---

Comment by mabshoff created at 2009-02-06 21:53:40

Resolution: fixed


---

Comment by mabshoff created at 2009-02-06 21:53:40

Merged in Sage 3.3.alpha6.

Cheers,

Michael
