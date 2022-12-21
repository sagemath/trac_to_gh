# Issue 1714: [with patch, needs review] allow keyword arguments for remote sage methods (sage0)

Issue created by migration from Trac.

Original creator: malb

Original creation time: 2008-01-07 15:37:02

Assignee: was

keyword arguments were not passed through to the remote sage instance now they are.


---

Attachment

Since #1843 has been merged this patch needs to be revisited now.

Cheers,

Michael


---

Comment by malb created at 2008-01-29 16:24:04

rebased patch against 2.10.1.rc2 (without cputime method)


---

Comment by malb created at 2008-01-29 16:24:52

Changing type from defect to enhancement.


---

Attachment

The new attached patch `sage0_keywords.2.patch` which replaces the old patch applies cleanly against `2.10.1.rc2`.


---

Comment by ncalexan created at 2008-02-14 23:38:21

Second patch looks fine, I say apply.

There are no docstrings, but is this code even doctested?  I don't know.


---

Comment by mabshoff created at 2008-02-15 00:24:38

Merged sage0_keywords.2.patch in Sage 2.10.2.alpha0


---

Comment by mabshoff created at 2008-02-15 00:24:38

Resolution: fixed
