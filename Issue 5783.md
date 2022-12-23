# Issue 5783: [with patch, needs review]  Lazy attributes: fix infinite recursion bug + support for cpdefs methods

Issue created by migration from https://trac.sagemath.org/ticket/5783

Original creator: nthiery

Original creation time: 2009-04-14 06:55:25

Assignee: cwitty

CC:  sage-combinat

The summary says it all.


---

Comment by nthiery created at 2009-05-18 03:07:16

Changing assignee from cwitty to nthiery.


---

Attachment


---

Comment by nthiery created at 2009-05-19 06:21:14

Changing status from new to assigned.


---

Comment by nthiery created at 2009-05-19 06:22:08

Updated patch:
 - fix ReST doc (indentation, ::, ...)
 - fix introspection
 - adds a hook for this in sage.misc.sageinspect.sage_getsourcelines


---

Comment by roed created at 2009-05-19 08:00:59

Adds lots of good documentation, fixes some problems, though additional feature requests remain.  Positive review.


---

Comment by mabshoff created at 2009-05-19 15:06:52

David,

please remember to change the summary if you do reviews of tickets.

Michael


---

Comment by mabshoff created at 2009-05-19 19:21:58

Merged in Sage 4.0.rc0.

Cheers,

Michael


---

Comment by mabshoff created at 2009-05-19 19:21:58

Resolution: fixed
