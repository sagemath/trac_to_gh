# Issue 6182: notebook -- saving a worksheet with double quotes in the worksheet name fails with a weird error

Issue created by migration from https://trac.sagemath.org/ticket/6182

Original creator: was

Original creation time: 2009-06-02 07:26:37

Assignee: boothby

CC:  was mhansen mpatel




---

Comment by timdumol created at 2010-01-18 04:44:12

This works now. Confirm and close?


---

Comment by timdumol created at 2010-01-18 19:10:56

Escapes worksheet names passed to javascript


---

Attachment

I take that back. It doesn't fail immediately, but it does fail.


---

Comment by timdumol created at 2010-01-18 19:12:41

Changing status from new to needs_review.


---

Comment by timdumol created at 2010-01-18 19:20:15

This should depend on #7650, #7294 and #7786 and their dependencies. Possibly some others.


---

Comment by mpatel created at 2010-01-20 02:03:07

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-01-20 02:03:07

V2 is rebased to drop changes to `template.py` (earlier patch).


---

Attachment

Rebased version without changes to `template.py`. Replaces previous.


---

Comment by mpatel created at 2010-01-25 00:51:58

Resolution: fixed
