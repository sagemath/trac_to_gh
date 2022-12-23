# Issue 2202: [with spkg; needs review] Debianize rubiks spkg

Issue created by migration from https://trac.sagemath.org/ticket/2202

Original creator: tabbott

Original creation time: 2008-02-18 02:05:29

Assignee: tabbott

I created a new spkg for rubiks that has a global Makefile, and added Debian build support to it:

http://sage.math.washington.edu/home/tabbott/rubiks-20070912.p2.spkg

The process involved adding distclean targets to the individual Makefiles for the various solvers; for now I made these changes in the spkg because I'm a bad person; but we should submit them upstream for those that we are not the official distribution point for.  I've attached patches for each to this ticket which we can submit to the upstream authors.

There are two things that bug me about this package.  One is that I'm not convinced Debian will want this motley assortment of rubiks cube solvers (so that we might end up leaving it as part of the "sagemath" package), and the other is that we don't install all the solvers that we build.


---

Attachment


---

Attachment


---

Attachment


---

Comment by mabshoff created at 2008-02-18 13:39:49

spkg looks good, nice fixes for the makefile.

Cheers,

Michael


---

Comment by mabshoff created at 2008-02-18 13:40:03

Resolution: fixed


---

Comment by mabshoff created at 2008-02-18 13:40:03

Merged in Sage 2.10.2.alpha1


---

Comment by robertwb created at 2008-02-18 23:32:04

The look fine to me.

The main reason for the rubiks solvers is that David Joyner has a book out on Rubik's cubes, and solving them via the word problem is *extremely* slow.
