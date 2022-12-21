# Issue 6501: [with SPKG, needs review] Coin-or CLP/CBC

Issue created by migration from Trac.

Original creator: ncohen

Original creation time: 2009-07-09 16:21:06

Assignee: tbd

Following this message on SAGE-devel :
http://groups.google.com/group/sage-devel/browse_thread/thread/9da47e06bcdfc49f

This is the package containing Clp/Cbc, the LP solvers from Coin-Or http://www.coin-or.org/.

The goal is to built a native LP support for sage using GLPK ( a different solver ) because of License problems. This being said, Coin-OR is way more efficient and should be preferred by most people needing LP solvers ( with or without integer variables )

This package only contains the sources of the last Cbc release, installed with the original Makefile in SAGE.

It can be downloaded there : http://www-sop.inria.fr/members/Nathann.Cohen/cbc.spkg

Nathann


---

Comment by ncohen created at 2009-07-25 10:43:26

Should be deleted. I created a new ticket by mistake, and the other one is more recent than this one.

http://trac.sagemath.org/sage_trac/ticket/6603


---

Comment by mvngu created at 2009-08-04 06:56:13

Nathann: So you're saying this ticket should be closed as a duplicate of #6603?


---

Comment by ncohen created at 2009-08-04 07:28:00

Indeed !!!


---

Comment by mvngu created at 2009-08-04 07:31:56

Closing this as a duplicate of #6603.


---

Comment by mvngu created at 2009-08-04 07:31:56

Resolution: duplicate
