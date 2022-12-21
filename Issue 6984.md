# Issue 6984: cygwin port: make lapack into a dummy spkg that requires systemwide lapack

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-09-22 06:35:20

Assignee: tbd

CC:  jpflori dimpase




---

Comment by kcrisman created at 2013-04-26 01:24:00

Changing status from new to needs_review.


---

Comment by kcrisman created at 2013-04-26 01:24:00

I think this can safely be closed, based on all the stuff going on with Cygwin and the dependency we make explicit now for Cygwin.  JP or someone else, feel free to set to positive review if you agree.


---

Comment by kcrisman created at 2013-04-26 01:24:13

Changing component from build to porting: Cygwin.


---

Comment by dimpase created at 2013-04-26 02:20:51

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2013-04-26 15:33:41

In any case, it is also obsoleted by #10508.


---

Comment by kcrisman created at 2013-04-26 16:59:44

> In any case, it is also obsoleted by #10508.
True, but who knows when that will get in.


---

Comment by jdemeyer created at 2013-04-28 12:46:34

Resolution: invalid
