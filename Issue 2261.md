# Issue 2261: setup.py: Don't add emtpy Debian directory to scripts section

Issue created by migration from https://trac.sagemath.org/ticket/2261

Original creator: mabshoff

Original creation time: 2008-02-22 18:04:05

Assignee: mabshoff

The directory entry causes the sage lib to fail building on a minimal Debian install. Go figure.

Cheers,

Michaek


---

Comment by mabshoff created at 2008-02-22 18:04:19

Changing status from new to assigned.


---

Attachment


---

Comment by jason created at 2008-02-22 18:39:49

this looks like it follows William's request exactly.


---

Comment by mabshoff created at 2008-02-22 18:44:28

Merged in Sage 2.10.2.final


---

Comment by mabshoff created at 2008-02-22 18:44:28

Resolution: fixed
