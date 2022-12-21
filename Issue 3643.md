# Issue 3643: re-enable dsage/testdoc.py

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-07-11 18:41:37

Assignee: yi

I disabled dsage/testdoc.py for sage-3.0.5, since that system for doctesting dsage is BROKEN.
For example

```
sage -t  devel/sage/sage/dsage/tests/testdoc.py
********************************************************************
File "/home/was/build/sage-3.0.4/tmp/testdoc.py", line 14:
   sage: a
Expected:
   5
Got:
   No output.
```

and this is just a typical timing issue.  We have unit tests after all.


---

Comment by yi created at 2008-07-11 19:26:44

This is fine. I am working hard to fix this in ticket #3600.


---

Attachment

This seems to work correctly with #4745 applied, so after discussion with mabshoff perhaps we should reenable the doctest after #4745 to see if we can get it to fail again.


---

Comment by gfurnish created at 2008-12-09 18:43:35

Changing status from new to assigned.


---

Comment by gfurnish created at 2008-12-09 18:43:35

Changing assignee from yi to gfurnish.


---

Comment by mabshoff created at 2008-12-11 15:00:06

Positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2008-12-11 15:27:18

Merged in Sage 3.2.2.alpha2


---

Comment by mabshoff created at 2008-12-11 15:27:18

Resolution: fixed
