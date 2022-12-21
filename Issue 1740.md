# Issue 1740: Fix Pentium M detection for ATLAS BLAS

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2008-01-10 05:05:29

Assignee: mabshoff

There is a know problem with ATLAS BLAS that misdetects Pentium Ms as CoreDuos and consequently takes a long, long time tuning to build. This patch by Paul Zimmermann fixes the issue. It has been integrated into 

http://sage.math.washington.edu/home/mabshoff/release-cycles-2.10/alpha1/atlas-3.8.p7.spkg

Cheers,

Michael


---

Comment by mabshoff created at 2008-01-10 05:21:30

FYI: I posted the patch at 

https://sourceforge.net/tracker/index.php?func=detail&aid=1868203&group_id=23725&atid=379483

Once I hear back from Clint I will let you guys know.

Cheers,

Michael


---

Comment by mabshoff created at 2008-01-10 05:42:00

Merged in Sage 2.10.alpha1.

Cheers,

Michael


---

Comment by mabshoff created at 2008-01-10 05:42:00

Resolution: fixed
