# Issue 3300: [with patch; needs review] ntl soname for Debian package

Issue created by migration from https://trac.sagemath.org/ticket/3300

Original creator: tabbott

Original creation time: 2008-05-25 18:57:23

Assignee: tabbott

I've attached the patch to make the ntl Debian package use the soname library patch we made earlier (with a few other improvements).


---

Attachment


---

Attachment


---

Comment by tabbott created at 2008-05-25 22:29:28

I've also attached the patch that removes the ntl version number from spkg-install.


---

Comment by tabbott created at 2008-05-26 04:36:28

I've also attached a patch that changes the ntl priority to optional and makes the copyright file not have a trivially weird format.


---

Attachment


---

Comment by mabshoff created at 2008-05-28 07:41:12

Positive review on the two patches for the Debian dist directory, but I will not apply ntl-forget-version.patch since that results in libntl.so and libntl-5.4.2.so being identical copies. There is a special option for cp on Linux [-d] that preserves the link, but this might break on Cygwin for example. Since updating NTL is rare we can certainly deal with changing the so name on occasion.

Cheers,

Michael


---

Comment by mabshoff created at 2008-05-28 07:43:55

Resolution: fixed


---

Comment by mabshoff created at 2008-05-28 07:43:55

Merged in Sage 3.0.3.alpha0

The patches have been merged in 

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.0.3/alpha0/ntl-5.4.2.p3.spkg

without incrementing the patch level to avoid rebuilds.

Cheers,

Michael
