# Issue 1538: upgrades of sage_scripts can confuse bash

Issue created by migration from Trac.

Original creator: cwitty

Original creation time: 2007-12-16 16:01:56

Assignee: was

Doing an upgrade of sage_scripts may modify files in local/bin while bash is executing them.  This means that bash may attempt to execute some mixture of the old and new versions (which will usually lead to an error, because bash will begin executing the new version in the middle of a line).

Currently Sage includes an effective workaround for this problem... the upgrade is automatically retried if it fails.  However, we should put in a real fix.


---

Comment by cwitty created at 2007-12-16 16:06:19

Changing assignee from was to mabshoff.


---

Comment by cwitty created at 2007-12-16 16:06:19

Changing component from algebraic geometry to distribution.


---

Attachment


---

Comment by jdemeyer created at 2012-10-05 13:18:27

Changing component from distribution to build.


---

Attachment


---

Comment by jdemeyer created at 2013-12-19 12:16:03

This is solved by the git workflow because everything is now updated *before* the build, not *during* the build.


---

Comment by jdemeyer created at 2013-12-19 12:17:12

Changing status from new to needs_review.


---

Comment by jdemeyer created at 2013-12-19 12:17:17

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2013-12-20 15:59:23

Resolution: fixed
