# Issue 6610: Compiler environment variables should be consistent

Issue created by migration from https://trac.sagemath.org/ticket/6610

Original creator: ghtdak

Original creation time: 2009-07-24 04:21:32

Assignee: tbd

Keywords: Environment

Sage sets the environment variable LIBRARY_PATH which is a gcc variable.  OTOH, it doesn't set CPATH or C_INCLUDE_PATH or CPLUS_INCLUDE_PATH.  This causes inconsistencies, particularly since Sage replicates many Linux libraries potentially leading to version issues.

LD_LIBRARY_PATH is also set (appended / modified), as it would need to be, but that is for the loader (ld).  Sometimes this leads to difficulties when running non-Sage installed executables which use replicated libraries.  One example is Git which doesn't like Sage's zlib.

This latter problem is more difficult to address and rarely causes difficulty.  In fact, the only manifestation I've seen is git although it seems obvious that there are potential problems lurking.

In my case, I replace the symlinks for libz.so* to reference the system libraries.  This will work as long as major version's (interfaces) are consistent.




---

Comment by jdemeyer created at 2013-12-29 23:08:14

This is essentially a duplicate of #10572.


---

Comment by jdemeyer created at 2013-12-29 23:08:14

Changing status from new to needs_review.


---

Comment by jdemeyer created at 2013-12-29 23:08:23

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2014-01-04 04:27:49

Resolution: duplicate
