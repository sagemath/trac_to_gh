# Issue 6247: sage -optional tries to write to SAGE_ROOT

Issue created by migration from Trac.

Original creator: burcin

Original creation time: 2009-06-08 14:37:40

Assignee: cwitty

Reported by `somos` on `#sage-devel` on IRC


```
<somos> when I do 'sage -optional' it tried to make a temp file in SAGE_ROOT
...
<somos> This is ok if you are running as root user.
...
<mvngu> From the help:
<mvngu> -optional     -- list all optional packages that can be downloaded
<somos> Anyway, the problem is the temp file in SAGE_ROOT.
<somos> It should be in /tmp instead.
<mvngu> Can you explain why it should be in /tmp ?
<somos> Becuase SAGE_ROOT requires root permissions.
...
<somos> So, my suggestion is to avoid the temp file. #1
<somos> If a temp file is needed, I suggest TMP or TMPDIR instead.
```




---

Comment by jdemeyer created at 2013-08-13 15:51:02

Changing status from new to needs_review.


---

Comment by jdemeyer created at 2013-08-13 15:51:02

Duplicate of #12018.


---

Comment by jdemeyer created at 2013-08-13 15:59:08

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2013-08-16 11:10:59

Resolution: worksforme


---

Comment by jdemeyer created at 2013-08-16 11:11:14

Resolution changed from worksforme to duplicate
