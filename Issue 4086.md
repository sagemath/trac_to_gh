# Issue 4086: [with spkg, needs review] Fix polybori-0.5rc.p3.spkg build issue from vanilla tarball

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2008-09-09 10:18:04

Assignee: mabshoff

In spkg-install we touch pbori.pyx to force a rebuild. But when building from a vanilla tarball that file does not exist and spkg-install exists with a non-zero status and fails. The spkg at 

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.1.2/rc2/polybori-0.5rc.p4.spkg

fixes the issue.

Build tested on x86, x86-64 and Itanium Linux as well as OSX.

Cheers,

Michael


---

Comment by mabshoff created at 2008-09-09 10:18:10

Changing status from new to assigned.


---

Comment by malb created at 2008-09-09 10:29:19

New spkg at:

  http://sage.math.washington.edu/home/malb/spkgs/polybori-0.5rc.p4.spkg

which replaces the `test -a` with `test -f` since that seems to be the safe choice. I only checked the SPKG by reading the changes, I didn't test it on a bunch of platforms yet.


---

Comment by mabshoff created at 2008-09-10 02:35:30

Spkg looks good to me. I will post a followup polybori-0.5rc.p5.spkg with the OSX 10.4 fix at #4090.

Cheers,

Michael


---

Comment by mabshoff created at 2008-09-10 02:39:01

Merged in Sage 3.1.2.rc2


---

Comment by mabshoff created at 2008-09-10 02:39:01

Resolution: fixed
