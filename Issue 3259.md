# Issue 3259: [with patch; needs review] shared library versioning for flint

Issue created by migration from https://trac.sagemath.org/ticket/3259

Original creator: tabbott

Original creation time: 2008-05-19 22:26:53

Assignee: mabshoff

CC:  f.r.bissey@massey.ac.nz

I've attached a patch which should add shared library versioning to libflint.so.

It includes the relevant patch for the Debian package and spkg-install, and also the relevant change s to the Debian packaging.


---

Attachment

I forgot to note this, but because flint doesn't have a static library, we only need to build it with -fPIC, which is accomplished by setting MAKECMDGOALS=library


---

Comment by fbissey created at 2008-05-19 22:55:28

I had forgotten about flint. Easy to do as my gentoo patch
is a one liner sed command to add a soname. 

The patch to the makefile looks good to me, I won't comment 
on the debian package rules. The makefile already use -fpic,
do you have to overrule that in debian?


---

Comment by mabshoff created at 2008-05-28 08:24:49

Patch looks good to me. The only issue along with #3300, i.e. that due to the copy operation we do not end up with a dynamic library and a link, but two identical copies. I fixed that in spkg-install. Positive review. The patches have been merged into 

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.0.3/alpha0/flint-1.06.p3.spkg

Cheers,

Michael


---

Comment by mabshoff created at 2008-05-28 08:25:13

Resolution: fixed


---

Comment by mabshoff created at 2008-05-28 08:25:13

Merged in Sage 3.0.3.alpha0
