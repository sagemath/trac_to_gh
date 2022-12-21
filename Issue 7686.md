# Issue 7686: Remove all "AppleDouble encoded Macintosh files" from the Sage source distribution

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-12-15 19:14:07

Assignee: tbd

The spkg's with ._ file crap all over the place are:

   * f2c-20070816.p1
   * flintqs-20070817.p4
   * ghmm-20080813.p0
   * lcalc-20080205.p3

This can be fixed by extracting the spkg, deleting the crap, and remaking it with "sage -pkg".  I think "sage -pkg" works correctly on OS X now-a-days, but certainly does on Linux.


---

Comment by jdemeyer created at 2016-04-11 09:52:17

Obsolete, we no longer use SPKG files.


---

Comment by jdemeyer created at 2016-04-11 09:52:17

Changing status from new to needs_review.


---

Comment by jdemeyer created at 2016-04-11 09:52:24

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2016-06-12 12:02:30

Resolution: fixed
