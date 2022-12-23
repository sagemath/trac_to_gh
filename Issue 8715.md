# Issue 8715: fortran-20100118 ignores SAGE_FORTRAN on Linux

Issue created by migration from https://trac.sagemath.org/ticket/8715

Original creator: logix

Original creation time: 2010-04-19 13:14:38

Assignee: GeorgSWeber

On Linux, fortran-20100118.spkg's spkg-install ignores SAGE_FORTRAN and instead overrides it with the first "gfortran" it finds in $PATH.  In my environment this fortran compiler is (more or less) broken, so I have to it explicitly and I then want it to be used.  The simple attached fix executes the relevant code path only if SAGE_FORTRAN is not set yet.


---

Attachment


---

Comment by logix created at 2010-04-22 14:20:20

Changing status from new to needs_review.


---

Comment by leif created at 2010-04-22 19:33:48

Well, the patch you uploaded is not a Mercurial "ChangeSet"...

http://www.sagemath.org/doc/developer/producing_patches.html


---

Comment by leif created at 2010-04-22 19:43:41

and/or http://www.sagemath.org/doc/developer/patching_spkgs.html


---

Comment by was created at 2010-04-28 22:06:39

Resolution: fixed


---

Comment by was created at 2010-04-28 22:06:39

Good idea.  Looks good.  Thanks! Positive review, and merged into 4.4.1.alpha1.
