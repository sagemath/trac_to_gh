# Issue 7046: Singular fails to build on OS X 10.6 with case sensitive file system

Issue created by migration from Trac.

Original creator: iandrus

Original creation time: 2009-09-28 08:34:12

Assignee: tbd

There is a typo in spkg-install so that a patched file doesn't get copied and building fails.


---

Comment by mvngu created at 2009-09-28 08:38:59

Changing priority from major to blocker.


---

Comment by mvngu created at 2009-09-28 08:41:29

Should be patched against the `spkg-install` of the Singular spkg.


---

Comment by mvngu created at 2009-09-28 08:42:52

Changing assignee from tbd to mabshoff.


---

Comment by mvngu created at 2009-09-28 08:42:52

Changing component from build to packages.


---

Comment by mvngu created at 2009-09-28 08:52:27

based on Sage 4.1.2.alpha4


---

Attachment

Updated Singular package at

http://sage.math.washington.edu/home/mvngu/release/spkg/standard/singular-3-1-0-4-20090818.p1.spkg


---

Attachment

doctest log for bsd.math with Sage 4.1.2.alpha4 and updated Singular spkg


---

Comment by mvngu created at 2009-09-30 04:26:33

doctest log for cicero with Sage 4.1.2.alpha4 and updated Singular spkg


---

Attachment

install log for t2.math with Sage 4.1.2.alpha4 and updated Singular spkg


---

Attachment

Report of my testing on various platforms with the updated Singular package and the cliquer spkg at #6681:

 * sage.math: 64-bit Ubuntu 8.04.3 LTS --- compile OK; all doctests pass.
 * bsd.math: 64-bit Mac OS X 10.6 --- compile OK; many doctest failures, all of which have been reported to [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/cdcf10c5c730f5b5). The full doctest log is attached.
 * rosemary.math: 64-bit RHEL 5.4 --- compile OK; all doctests pass.
 * cicero on SkyNet: 32-bit Fedora 9 --- compile OK; some doctest failures, all of which have been reported to [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/6abc4e530a6cd626). The full doctest log is attached.
 * eno on SkyNet: 64-bit Fedora 9 --- compile OK; all doctests pass.
 * lena on SkyNet: 64-bit RHEL 5.3 --- compile OK; all doctests pass.
 * menas on SkyNet: 64-bit openSUSE 11.1 --- compile OK; all doctests pass.
 * t2.math: SPARC Solaris with GCC 4.4.1 --- compilation abort when trying to install sage-4.1.2.alpha4.spkg; got past installing Singular, though. The full install log is attached.


---

Comment by mvngu created at 2009-09-30 12:32:53

Resolution: fixed


---

Comment by mvngu created at 2009-09-30 12:32:53

Merged `singular-3-1-0-4-20090818.p1.spkg` in the standard packages repository.
