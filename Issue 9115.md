# Issue 9115: smart summing

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2010-06-02 22:23:29

Assignee: jason

CC:  robertwb ncohen

We should extend the Sage sum function to call a magic method to handle summing things in the case of the python sum calling convention (and we shouldn't use the "sum()" method, as that name is probably way too likely to be used, and may be used for something else!)

This can take care of the performance issues at #9089 and #9061.


---

Comment by jason created at 2010-06-02 22:25:27

Changing status from new to needs_work.


---

Attachment

Here is an unfinished rough patch for the feature suggested at #9089.
