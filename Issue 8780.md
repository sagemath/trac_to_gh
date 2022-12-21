# Issue 8780: add the Cephes spkg to Cygwin

Issue created by migration from Trac.

Original creator: mhansen

Original creation time: 2010-04-27 06:39:57

Assignee: tbd

CC:  pjeremy

On Cygwin, Sage needs c99 complex support which can be provided by the cephes library from netlib.org / www.moshier.net

There is an spkg at http://sage.math.washington.edu/home/mhansen/cygwin_port/cephes-2.8.spkg


We need to decide the best way to include this since it is only need on Cygwin (and maybe FreeBSD, etc.).


---

Comment by jason created at 2010-04-27 18:37:11

How about test the OS name in spkg-install, and if it is cygwin, do something, otherwise return successfully without doing anything?


---

Comment by dimpase created at 2010-04-28 06:08:30

Is it the same Solaris-only cvxopt problem that was solved (for cvxopt) by adding sun_complex.h there?
If yes, then it might be good to include Solaris in the list of architectures for which cephes is installed.


---

Comment by mhansen created at 2010-04-28 06:33:37

Sorry, I spoke too soon -- this doesn't quite fix the problem with cvxopt since it doesn't check $SAGE_LOCAL/include.  There is some other cleanup work that needs to be for the cvxopt-1.1.2 spkg as well.

Also, this is a little different than the Solaris issue since Cygwin doesn't have a complex.h, which is what the spkg provides.


---

Comment by was created at 2010-05-26 01:15:58

Resolution: fixed


---

Comment by was created at 2010-05-26 01:15:58

I did what Jason Grout suggests above as a little referee patch, and merged this into 4.4.3.alpha0.
