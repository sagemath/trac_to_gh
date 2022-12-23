# Issue 2431: [optional spkg] polymake-2.2.p3.spkg fix

Issue created by migration from https://trac.sagemath.org/ticket/2431

Original creator: mhampton

Original creation time: 2008-03-08 22:59:37

Assignee: mhampton

Two issues: the install script needs to be changed to use cddlib-094b.p1 instead of p0; a version with this change is at:
http://www.d.umn.edu/~mhampton/polymake-2.2.p3.spkg

The install also fails on a binary installation since its relies on the cddlib spkg being in spkg/standard, instead of the dummy version.  I will try to fix this; I am a little puzzled about it.


---

Comment by mabshoff created at 2008-03-19 10:24:12

Changing component from packages to optional packages.


---

Comment by mabshoff created at 2008-03-19 11:12:19

Resolution: fixed


---

Comment by mabshoff created at 2008-03-19 11:12:19

I fixed some small issues with the SPKG:

 * added an hg repo and .hgignore
 * rename SAGE.txt to SPKG.txt

The new spkg builds fine for me and is at

http://sage.math.washington.edu/home/mabshoff/SPKG/polymake-2.2.p4.spkg

Positive review, I will upload the new spkg to the optional package repo shortly. It already seems to be there, so I am not sure why this ticket was never closed.

Cheers,

Michael


---

Comment by mabshoff created at 2008-03-19 11:14:46

Merged in the optional package repo and mirrored out.
