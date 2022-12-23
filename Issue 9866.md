# Issue 9866: getting rid of endianness-dependent behaviour in GAP random sources

Issue created by migration from https://trac.sagemath.org/ticket/9867

Original creator: dimpase

Original creation time: 2010-09-07 13:04:14

Assignee: joyner

CC:  simonking

in the thread [How to deal with GAP's machine dependent random generator?] on sage-devel Simon King mentioned that GAP own random source dependes on endianness of the machine.
While Sage sort of takes care of this in misc/randstate.pyx,
it still does not fix GAP internals. So, to make it good and proper, we essentially add the fix in misc/randstate.pyx to GAPROOT/src/integer.c, and remove it from misc/randstate.pyx
The updated gap spkg is here:

http://boxen.math.washington.edu/home/dima/packages/gap-4.4.12.p5.spkg


---

Attachment


---

Comment by dimpase created at 2012-09-25 06:40:19

Changing status from new to needs_review.


---

Comment by dimpase created at 2012-09-25 07:00:04

This will be fixed in #13211. Let us close this one as obsolete.


---

Comment by kcrisman created at 2012-09-25 12:22:23

I can confirm that the current code is no longer needed as of #13211; see [comment:49:ticket:13211 here].


---

Comment by kcrisman created at 2012-09-25 12:22:23

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2012-10-05 08:52:31

Resolution: duplicate
