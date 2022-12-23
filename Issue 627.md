# Issue 627: fix pari build on PPC 32bit Linux

Issue created by migration from https://trac.sagemath.org/ticket/627

Original creator: mabshoff

Original creation time: 2007-09-09 05:39:28

Assignee: mabshoff

pari needs a single line patch to build properly on 32 bit PPC Linux so that the linker doesn't throw a fit. Aside from trivial DSage that makes all doctests pass on that platform and elevates it to a fully supported platform.

The obvious next step is to get Sage to also build in 64 bit mode.

A patch will be attached to this ticket in the next 12 hours.

Cheers,

Michael


---

Comment by mabshoff created at 2007-09-09 05:39:35

Changing status from new to assigned.


---

Comment by mabshoff created at 2007-09-09 10:51:26

A patch for the issue can be found at:

http://fsmath.mathematik.uni-dortmund.de/~mabshoff/patches/pari-add_-fPIC_to_DLCFLAGS_for_PPC_Linux.patch

An updated pari.spkg can be found at:

http://fsmath.mathematik.uni-dortmund.de/~mabshoff/sage/pari-2.3.2.p2.spkg

Cheers,

Michael


---

Comment by was created at 2007-09-09 14:27:54

I made a couple of cosmetic changes to this patch to make pari-2.3.2.p3.spkg, which is available
at sagemath.org at patches/standard:

   1. mv get_dlcflags into patches/
   2. apply get_tdlcflags at build time
   3. put the original get_dlcflags back in src/config, since src/ is supposed to be 100% plain vanilla sources.
   4. did "hg ci" which was forgotten.


---

Comment by was created at 2007-09-09 14:27:54

Resolution: fixed


---

Comment by was created at 2007-09-09 14:31:02

actually the patch is at:
  http://sage.math.washington.edu/tmp/
