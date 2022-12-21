# Issue 4034: [with spkg, needs review] Fix rubiks.spkg build on Solaris

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2008-09-01 09:50:03

Assignee: mabshoff

This is a similar problem like the singular.spkg: /usr/bin/install does not exist. The spkg at

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.1.2/alpha4/rubiks-20070912.p8.spkg

works around that.

Cheers,

Michael


---

Comment by mabshoff created at 2008-09-01 09:50:18

Changing status from new to assigned.


---

Comment by malb created at 2008-09-01 10:35:28

Installs fine on my 64-bit Debian/GNU Linux Core2Duo. `sage -t interfaces/rubik.py` works.


---

Comment by mabshoff created at 2008-09-01 11:34:23

Resolution: fixed


---

Comment by mabshoff created at 2008-09-01 11:34:23

Merged in Sage 3.1.2.alpha4
