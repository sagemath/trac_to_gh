# Issue 4484: make a platform_quirks.h

Issue created by migration from Trac.

Original creator: craigcitro

Original creation time: 2008-11-09 23:05:29

Assignee: mabshoff

There are lots of platform-specific quirks in various parts of the Sage library. For instance, see the `#if defined(__sun)` at the top of `partitions_c.cc` (`partitions_c.h`). These should be moved to a single header in `libcsage`.


---

Comment by mabshoff created at 2008-11-10 08:59:39

Changing status from new to assigned.


---

Comment by jdemeyer created at 2013-05-19 13:09:55

Changing status from new to needs_review.


---

Comment by jdemeyer created at 2013-05-19 13:09:55

We managed to live without this, so I guess it's not really needed.


---

Comment by jdemeyer created at 2013-05-19 13:10:03

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2013-05-21 07:23:47

Resolution: wontfix
