# Issue 1792: Make Install problem with DESTDIR/sage script

Issue created by migration from Trac.

Original creator: pgrinber

Original creation time: 2008-01-16 04:56:34

Assignee: cwitty

when running "make install" a script will be created in $DESTDIR called sage. This is intended to be the main executable for sage. However, SAGE_ROOT is not set correctly in this file. It would be nice if the make install process correctly set SAGE_ROOT=$DESTDIR during its installation.


---

Comment by mabshoff created at 2008-03-16 08:16:00

Changing assignee from cwitty to mabshoff.


---

Comment by mabshoff created at 2008-03-16 08:16:00

Changing status from new to assigned.


---

Comment by jdemeyer created at 2016-05-20 08:28:47

Changing status from new to needs_review.


---

Comment by jdemeyer created at 2016-05-20 08:28:47

New commits:


---

Comment by zimmerma created at 2016-05-20 08:42:52

why remove this feature, which I'm using when compiling Sage from source since several years, and which is very useful for me (at least)?

Paul


---

Comment by jdemeyer created at 2016-05-20 08:48:05

Given that it doesn't work, you cannot really argue that I'm removing a feature.

I'm just pointing out that it's not supported and that it's unlikely to become supported.


---

Comment by vbraun created at 2016-05-23 22:27:20

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2016-05-23 22:27:20

This is definitely broken now


---

Comment by vbraun created at 2016-05-24 16:41:17

Resolution: fixed
