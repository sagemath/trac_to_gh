# Issue 3405: [with spkg, needs review] update Singular SPKG to newest upstream release

Issue created by migration from https://trac.sagemath.org/ticket/3405

Original creator: malb

Original creation time: 2008-06-12 22:36:32

Assignee: mabshoff

Keywords: singular

# New upstream release

Tue Jun 10 18:51:53 CEST 2008 Singular-3-0-4-3

Changes with respect to 3-0-4-2

 *  code depending on certain cpus is now selected by SI_CPU_*
  in mod2.h (for libsingular.so), set by configure
 *  licence clarified:
   * kernel/htmlhelp.h changed to LGPL 2.1
   * kernel/htmlhelp.lib removed
   * not-up-to-date stuff removed
 *  more static p_Procs: faster on systems which do not support/
  do not use DL_KERNEL
 * new target libsingular.a (for gfan)

This includes the fix for Solaris. Also note that libSingular is now also used for gfan :-)

The SPKG is here:

   http://sage.math.washington.edu/home/malb/spkgs/singular-3-0-4-2-20080611.p0.spkg


---

Comment by craigcitro created at 2008-06-15 21:53:08

Changing keywords from "singular" to "singular, editor_mabshoff".


---

Comment by mabshoff created at 2008-06-26 06:47:23

Spkg builds and doctests fine on Linux and OSX. Positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2008-06-26 06:47:23

Resolution: fixed
