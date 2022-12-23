# Issue 4966: Switch gmp to eMPIRe svn1555

Issue created by migration from https://trac.sagemath.org/ticket/4966

Original creator: mabshoff

Original creation time: 2009-01-12 06:19:49

Assignee: mabshoff

CC:  mhansen

The eMPIRe.spkg is nearly a drop in for the old gmp-4.2.1.spkg. There are a couple doctests to fix (see upcoming patches) and the ecmgmp.spkg also needs a bump since it requires a recompile. 

Cheers,

Michael


---

Comment by mabshoff created at 2009-01-12 06:19:55

Changing status from new to assigned.


---

Comment by mabshoff created at 2009-01-18 16:58:30

The spkg can be found at

http://sage.math.washington.edu/home/mabshoff/spkgs/gmp-mpir-svn1555.spkg

To review also apply the two patches I will add momentarily. One also needs to force a rebuild of ecmgmp and the libecm extension. During the upgrade this will be accomplished via #5016.

Cheers,

Michael


---

Attachment


---

Attachment

Note that the spkg is larger than the old one due to two things:

 * we are shipping a copy of yasm to build MPIR since the one in the system is usually too buggy to work
 * we are shipping Brian Gladman's VS 2008 build files

The spkg has been tested on

 * FC 9 x86
 * FC 9, OpenSUSE 10.3 x86-64
 * RHEL 5.2, SLES 10 Itanium
 * Solaris 10 Sparc and x86
 * OSX 10.4 ppc
 * OSX 10.5 x86 *and* x86-64
 * YDL 6.1 PS3 (a G5 variant)

Cheers,

Michael


---

Comment by was created at 2009-01-18 20:53:52

REVIEW:

(1) All doctests pass with the applied patches.

(2) 
Just for fun I checked to see how bad the xgcd speed regression is:

```
BEFORE (with GMP):
sage: n = ZZ.random_element(0,2^(2^20)); m = ZZ.random_element(0,2^(2^20))
sage: time k = m.xgcd(n)
CPU times: user 0.73 s, sys: 0.00 s, total: 0.73 s
Wall time: 0.74 s


AFTER (with eMPIRe):
sage: n = ZZ.random_element(0,2^(2^20)); m = ZZ.random_element(0,2^(2^20))
sage: time k = m.xgcd(n)
CPU times: user 2.39 s, sys: 0.00 s, total: 2.39 s
Wall time: 2.39 s
```


I did some multiplication timings (by multiplying m, n as above and bigger) and empire is always about 3-5% FASTER.

preliminary *positive review*.

I will look this over again a little more carefully, but so far it looks very very good.


---

Comment by mabshoff created at 2009-01-19 02:09:59

Resolution: fixed


---

Comment by mabshoff created at 2009-01-19 02:09:59

Merged two patches and the spkg in Sage 3.3.alpha0

Mike: Note that there are doctest changes in the doc repo, too.


---

Comment by mabshoff created at 2009-01-19 02:25:41

I found one buglet that slipped by, i.e. we need to unset PYTHON since Yasm gets confused by it. I also did not check in the changes to spkg-install, so I did so.

Cheers,

Michael
