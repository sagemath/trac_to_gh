# Issue 2735: [with patch; needs review] minor eclib build system improvements

Issue created by migration from https://trac.sagemath.org/ticket/2735

Original creator: tabbott

Original creation time: 2008-03-30 06:48:39

Assignee: tabbott

CC:  cremona

The eclib root makefile doesn't have a way to install the programs such as mwrank that it builds.  

There's currently a hack around this in the spkg-install script, but I'd prefer to not reproduce this random list of programs for the Debian package.

So, I've written some code to add to its root makefile that will call "make install_progs" in each of the subdirectories, and modified the Debian rules file to use it to install the non-test binary programs.  I notice that one of the test binary programs is installed by SAGE, so this new makefile can't yet simplify the dpkg-install by much.

The patches are attached.


---

Attachment

Patch is good. Positive review.

John: the patch has been merged in eclib-20080310.p1.spkg which will be part of Sage 3.0.alpha0. It only touches code inside the dist/debian directory.

Cheers,

Michael


---

Comment by mabshoff created at 2008-04-01 21:10:13

Resolution: fixed


---

Comment by mabshoff created at 2008-04-01 21:10:13

Merged in Sage 3.0.alpha0
