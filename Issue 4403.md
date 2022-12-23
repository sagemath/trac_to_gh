# Issue 4403: Fix "Install from Source Code" section in "Sage Installation Guide"

Issue created by migration from https://trac.sagemath.org/ticket/4403

Original creator: mabshoff

Original creation time: 2008-10-30 18:12:07

Assignee: tba

CC:  mhansen

Fix the following issues in section 3:

 * We do support gcc 4.3
 * We are not working on SunForte or Intel CC support

Cheers,

Michael


---

Comment by mabshoff created at 2008-10-30 18:12:15

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-10-30 18:12:15

Changing assignee from tba to mabshoff.


---

Attachment

fixes documentation on compiler support


---

Comment by mvngu created at 2008-11-06 07:45:43

The patch *4403_compiler-support.patch* updates the installation guide on issues concerning compiler support. It was produced using sage-3.1.4. I'm not an expert on compiler issues specific to building Sage or various packages that are distributed with the Sage tarball. If I've missed anything, please help to update the installation guide.


---

Comment by mhansen created at 2008-11-21 15:52:38

Looks good.  I made these changes in the ReST version of the documentation too.


---

Comment by mabshoff created at 2008-11-21 23:07:12

Resolution: fixed


---

Comment by mabshoff created at 2008-11-21 23:07:12

Merged in Sage 3.2.1.alpha0
