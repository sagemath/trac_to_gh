# Issue 2101: debianize various spkgs

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2008-02-08 05:54:41

Assignee: tabbott

We started with NTL:

http://sage.math.washington.edu/home/mabshoff/SPKG-Debian/ntl-5.4.1.p11.spkg

More to come.


---

Comment by tabbott created at 2008-02-08 09:12:04

More spkgs for merging:
http://sage.math.washington.edu/home/tabbott/cddlib-094b.p1.spkg
http://sage.math.washington.edu/home/tabbott/eclib-20080127.p0.spkg
http://sage.math.washington.edu/home/tabbott/flintqs-20070817.p2.spkg
http://sage.math.washington.edu/home/tabbott/givaro-3.2.6.p6.spkg
http://sage.math.washington.edu/home/tabbott/iml-1.0.1.p9.spkg
http://sage.math.washington.edu/home/tabbott/lcalc-20070107.p1.spkg
http://sage.math.washington.edu/home/tabbott/libm4ri-20071224.p1.spkg
http://sage.math.washington.edu/home/tabbott/palp-1.1.p1.spkg
http://sage.math.washington.edu/home/tabbott/symmetrica-2.0.p1.spkg
http://sage.math.washington.edu/home/tabbott/sympow-1.018.1.p4.spkg


---

Comment by tabbott created at 2008-02-09 04:26:56

More spkgs few merging:
http://sage.math.washington.edu/home/tabbott/flint-1.06.p1.spkg
http://sage.math.washington.edu/home/tabbott/singular-3-0-4-1-20071209.p4.spkg
http://sage.math.washington.edu/home/tabbott/libfplll-2.1.6-20071129.p1.spkg
http://sage.math.washington.edu/home/tabbott/linbox-20070915.p4.spkg
http://sage.math.washington.edu/home/tabbott/genus2reduction-0.3.p1.spkg


---

Comment by tabbott created at 2008-02-10 01:06:00

Quaddouble in Debian is too old and not in Lenny at all. I filed a bug.  Here's an updated spkg for quaddouble with sloppy Debian build support for now (I grabbed the debian/ directory from Debian but didn't fix the fact that shared libraries and .la files weren't being built.).  It needs testing on other distros.

http://sage.math.washington.edu/home/tabbott/quaddouble-2.3.4.p1.spkg


---

Comment by mabshoff created at 2008-02-14 23:21:40

Resolution: fixed


---

Comment by mabshoff created at 2008-02-14 23:21:40

Merged all new spkgs but quaddouble-2.3.4.p1.spkg in Sage 2.10.2.alpha0
