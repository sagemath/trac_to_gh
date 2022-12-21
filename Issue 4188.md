# Issue 4188: [with spkg, needs review] Fix cvxopt.spkg build on Solaris due to broken complex.h headers

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2008-09-24 10:11:56

Assignee: mabshoff

complex.h on Solaris is broken - see http://bugs.opensolaris.org/bugdatabase/view_bug.do?bug_id=6549313

This causes the build of cvxopt to fail. The spkg at 

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.1.3/alpha1/cvxopt-0.9.p7.spkg

fixes that problem.

Cheers,

Michael


---

Comment by mabshoff created at 2008-09-24 10:12:01

Changing status from new to assigned.


---

Comment by craigcitro created at 2008-09-24 10:29:47

I tested on my machine, and it installs fine, and seems to work (doctests in `sage/numerical` all pass). Michael tells me that it also works on Sun, which was the issue, so that's what we needed.


---

Comment by mabshoff created at 2008-09-24 10:35:48

Merged in Sage 3.1.3.alpha1


---

Comment by mabshoff created at 2008-09-24 10:35:48

Resolution: fixed
