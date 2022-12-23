# Issue 3338: gfan tarball is not clean upstream

Issue created by migration from https://trac.sagemath.org/ticket/3338

Original creator: tabbott

Original creation time: 2008-05-30 17:32:39

Assignee: mabshoff

CC:  alexghitza mhampton

The gfan sources in SAGE are not quite the upstream sources:

[tabbott`@`debuild export$] diff -ur tmp/gfan0.3 tmp/gfan-0.3/ | diffstat
 gfan-0.3//.DS_Store         |only
 gfan-0.3//Makefile.orig03   |only
 gfan-0.3//Makefile2.2       |only
 gfan-0.3//Makefile2.2anders |only
 gfan-0.3//SAGE.txt          |only
 gfan-0.3//debian            |only
 gfan-0.3//oldsageMakefile   |only
 gfan-0.3/Makefile           |   55 ++++++++++++++------------------------------
 gfan0.3/doc                 |only
 gfan0.3/examples            |only
 gfan0.3/homepage            |only
 11 files changed, 18 insertions(+), 37 deletions(-)

I actually think that the SAGE changes may be mostly unecessary; the changes to the install target don't seem to be used, and the other changes aside from the removal of app_construction.o seem like they could be implemented via

make ADDTIONALINCLUDEOPTIONS=-I$(SAGE_LOCAL)/include ADDITIONALLINKOPTIONS=-lcddgmp -lgmp

If we can figure out how to fig the compilation problems related to app_construction.o (I don't see this problem on Debian with gfan 0.3), then we can stop modifying gfan at all.  But having a makefile patch isn't a big deal either.


---

Comment by drkirkby created at 2010-01-05 11:24:17

Note #7820 is aimed at updating gfan to the latest release, called "0.4plus".


---

Comment by mvngu created at 2010-01-25 14:15:40

Close as fixed by #7820.


---

Comment by mvngu created at 2010-01-25 14:15:40

Resolution: fixed
