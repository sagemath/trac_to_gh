# Issue 3303: [with patch; needs review] Add shared library to tachyon Debian package

Issue created by migration from https://trac.sagemath.org/ticket/3303

Original creator: tabbott

Original creation time: 2008-05-25 22:17:00

Assignee: tabbott

CC:  f.r.bissey@massey.ac.nz

I've attached a patch that adds a shared library to tachyon.

My patch includes the necessary changes to the Debian package.

Looking at spkg-install, it looks like SAGE doesn't actually use the tachyon library, only the binary, so I'm not including any changes to the spkg-install system.

Once this gets merged, I'll email John Stone with the patch to tachyon upstream.


---

Attachment


---

Comment by mabshoff created at 2008-05-28 07:50:53

Patch looks good to me and has been merged in 

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.0.3/alpha0/tachyon-0.98beta.p5.spkg

without incrementing the patch number to avoid unneeded rebuilds.

Cheers,

Michael


---

Comment by mabshoff created at 2008-05-28 07:51:04

Merged in Sage 3.0.3.alpha0


---

Comment by mabshoff created at 2008-05-28 07:51:04

Resolution: fixed
