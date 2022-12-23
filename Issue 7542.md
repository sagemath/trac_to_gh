# Issue 7542: Security issues in gnutls-2.2.1

Issue created by migration from https://trac.sagemath.org/ticket/7542

Original creator: drkirkby

Original creation time: 2009-11-27 14:11:52

Assignee: mvngu

CC:  david.kirkby@onetel.net

According to the Simon Josefsson, there are security issues with version 2.2.1. 

_"Unless you back-port security fixes to 2.2.x, you want to use the 2.8.x release to get proper security fixes."_

There are two other issues with 2.2.1 I am aware of. 
 * #7387 gnutls not building on OpenSolaris (x86)
 * #7511 gnutls-2.2.1 fails to build on HP-UX 

I do not know exactly what the bug is, but I'm told there are security issues with this release.

I tried to create a .spkg from the latest release, but that failed to build on Solaris 10 (SPARC) so was worst than the older release, though the developers tell me it should be ok. 

dave 



---

Comment by jdemeyer created at 2012-10-05 09:13:38

Resolution: invalid


---

Comment by jdemeyer created at 2012-10-05 09:13:38

GNUTLS is no longer part of Sage.
