# Issue 7086: vanilla hg vs. "sage -hg"

Issue created by migration from Trac.

Original creator: hemmecke

Original creation time: 2009-09-30 23:20:20

Assignee: cwitty

CC:  hemmecke

Keywords: hg

Vanilla hg accepts something like

  hg commit -m 'some comment'

However, if hg is a script that calls "sage -hg" (like /usr/local/bin/hg on sage.math.washington.edu), then the above command does not work.

The following was issued on the above server:
mkdir a
cd a
hg init
echo "abc def" > abc
hg add abc
hg commit -m 'some comment'
comment: No such file or directory
abort: file comment not found!


---

Comment by jdemeyer created at 2010-10-10 21:36:26

Changing status from new to needs_review.


---

Comment by jdemeyer created at 2010-10-10 21:36:26

This seems to be fixed now.


---

Comment by mpatel created at 2010-10-22 09:20:29

Resolution: worksforme
