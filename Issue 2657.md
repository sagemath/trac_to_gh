# Issue 2657: [with patch; needs review] Debian package cleanups

Issue created by migration from Trac.

Original creator: tabbott

Original creation time: 2008-03-24 01:26:18

Assignee: tabbott

I had an unnecessary and already wrong dependency on fplll for Debian.  I've attached a patch to fix this.



---

Attachment


---

Comment by mabshoff created at 2008-03-24 10:19:28

Patch looks good to me. The spkg at

http://sage.math.washington.edu/home/mabshoff/release-cycles-2.11/alpha2/libfplll-2.1.6-20071129.p2.spkg

fixes some small additional issues.

Cheers,

Michael


---

Comment by mabshoff created at 2008-03-24 10:19:45

Resolution: fixed


---

Comment by mabshoff created at 2008-03-24 10:19:45

Merged in Sage 2.11.alpha2
