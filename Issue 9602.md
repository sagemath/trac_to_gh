# Issue 9602: Fix gap on FreeBSD

Issue created by migration from Trac.

Original creator: pjeremy

Original creation time: 2010-07-26 11:22:14

Assignee: pjeremy

gap sysfiles.c is very host-dependent.  Current code includes a mixture of SYS_xxx and HAVE_xxx_H tests.  Whilst SYS_BSD might appear logical for FreeBSD, there is no testing for this, and recent FreeBSD variants support termios.h.

The attached patches (mostly taken from the FreeBSD port) add tests for HAVE_TERMIOS_H to make gap compile on FreeBSD 8.x.


---

Attachment

Stephen Montgomery-Smith has successfully compiled with a very similar (identical?) patch, attached.


---

Attachment


---

Comment by stephen created at 2012-04-08 14:47:50

I can confirm that this patch is needed to build sage-5.0.beta12.  It would be great if this patch could get put into sage.  It should be harmless to the builds under all other OS.


---

Comment by leif created at 2012-04-19 21:18:30

Just for the record:

There's also a new GAP spkg at #7041; one should perhaps base a new one here on the latter, although it currently doesn't yet use `patch`.  (I've added a couple of TODOs, some of which I'll probably address at #7041 as well, if I find the time...)


---

Comment by kcrisman created at 2012-06-20 19:22:04

Since #7041 didn't use patch, I don't think we need to do this either.

So we need a new spkg with this patch.


---

Comment by kcrisman created at 2013-01-16 01:38:07

Just FYI to all reading this, there is an even newer GAP with a number of things fixed in spkg-install in Sage 5.6.rc0.  So it's possible that this would have to be rebased ... or maybe even unnecessary?  (We can hope!)


---

Comment by vbraun created at 2013-03-12 13:54:58

The current `GAP-4.[5.6].x` doesn't have a `SYS_BSD` macro any more. This suggests that the issue has been fixed by upstream. I'm proposing to close this ticket as invalid/wontfix.


---

Comment by vbraun created at 2013-03-12 13:54:58

Changing status from new to needs_review.


---

Comment by kcrisman created at 2013-03-12 14:11:52

Stephen, what do you think?  [Your port](http://www.freebsd.org/cgi/cvsweb.cgi/ports/math/sage/files/) doesn't seem to have the GAP-specific patch I attached any more.


---

Comment by stephen created at 2013-03-13 01:14:33

Yes, at some point I seem to have removed the patch.  So it must be unnecessary now.


---

Comment by vbraun created at 2013-03-13 01:21:36

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2013-03-13 01:21:36

I'll take that as a "positive review"


---

Comment by jdemeyer created at 2013-03-15 13:02:07

Resolution: worksforme
