# Issue 6350: [with spkg, needs review] update M4RI to newest upstream release (20090617)

Issue created by migration from https://trac.sagemath.org/ticket/6350

Original creator: malb

Original creation time: 2009-06-17 22:28:03

Assignee: malb

CC:  craigcitro

Keywords: m4ri

While fixing a few issues for OSX PPC and IA64 (Iras) I fixed L1 cache size detection for OSX x86 too. Thus, now M4RI uses the correct L1 cache size on OSX x86 machines.

The SPKG is at:

  http://sage.math.washington.edu/home/malb/spkgs/libm4ri-20090617.spkg


---

Comment by craigcitro created at 2009-06-17 23:56:37

Looks good, works on several platforms (including the two that had issues before).


---

Comment by craigcitro created at 2009-06-17 23:56:37

Resolution: fixed
