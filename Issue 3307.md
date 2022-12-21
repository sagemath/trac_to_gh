# Issue 3307: [with patch; needs review] Move genus2reduction to /usr/lib for Debian package

Issue created by migration from Trac.

Original creator: tabbott

Original creation time: 2008-05-26 04:24:51

Assignee: tabbott

I've attached a patch that moves genus2reduction to /usr/lib in my Debian package because it's not a program you run directly and doesn't have a man page.  The patch also fixes all the other minor issues with the package I'm aware of.


---

Attachment


---

Comment by mabshoff created at 2008-05-28 06:41:36

Patch looks good to me. I have slipped it into

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.0.3/alpha0/genus2reduction-0.3.p3.spkg

without incrementing the patch level to avoid rebuilds.

Cheers,

Michael


---

Comment by mabshoff created at 2008-05-28 06:41:52

Resolution: fixed


---

Comment by mabshoff created at 2008-05-28 06:41:52

Merged in Sage 3.0.3.alpha0
