# Issue 2715: sage -coverage currently counts functions that are defined in doctests

Issue created by migration from Trac.

Original creator: mhansen

Original creation time: 2008-03-29 02:41:45

Assignee: cwitty




---

Attachment


---

Comment by cwitty created at 2008-03-29 21:52:39

Looks good.  (I looked at the diff of coverage runs before and after the patch, and it looks like it works correctly; and raises coverage 0.2%.  There is at least one function it should ignore but does not: "mumble" in sage/misc/python.py; I looked at fixing this but couldn't see an easy fix.  Anyway, the patch is definitely an improvement and should be applied.)


---

Comment by mabshoff created at 2008-03-29 21:57:28

Merged in Sage 2.11.rc0


---

Comment by mabshoff created at 2008-03-29 21:57:28

Resolution: fixed
