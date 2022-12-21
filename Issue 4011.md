# Issue 4011: notebook -- copying a worksheet on worksheet listings page results in the new worksheet being listed as running

Issue created by migration from Trac.

Original creator: TimothyClemans

Original creation time: 2008-08-31 01:08:02

Assignee: boothby

Why is the new worksheet, copy of another worksheet, running? It hasn't been accessed by the user.


---

Comment by TimothyClemans created at 2008-09-09 16:25:52

Please delete sage-4011_1.patch.

Patch sage-4011_1.patch doesn't seem to resolve the problem.


---

Attachment


---

Comment by mhansen created at 2009-01-24 06:21:23

I've added a test to my Selenium test suite for this since it requires the Javascript to run.


---

Comment by mhansen created at 2009-01-24 06:21:23

Changing status from new to assigned.


---

Comment by mhansen created at 2009-01-24 06:21:23

Changing assignee from boothby to mhansen.


---

Comment by jason created at 2009-02-07 17:43:51

This might be really nitpicky, but can we make the code not have a double negative?  I.e., `if no_load is in ctx`, rather than `if no_load not in ctx`.  Having a double negative makes the code a bit more confusing.


---

Comment by jason created at 2009-02-07 17:45:10

And if you're modifying the patch anyway, you might fix the typo in the docs in js.py for this function: worsheet -> worksheet.


---

Attachment


---

Attachment

Apply trac_4011.2.patch


---

Comment by mabshoff created at 2009-03-24 23:26:00

Merged trac_4011.2.patch in Sage 3.4.1.alpha0.

Cheers,

Michael


---

Comment by mabshoff created at 2009-03-24 23:26:00

Resolution: fixed
