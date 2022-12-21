# Issue 323: make and upgrade fails on Ubuntu Edgy (6.10)

Issue created by migration from Trac.

Original creator: malb

Original creation time: 2007-03-16 10:01:22

Assignee: was

Ubuntu Edgy uses dash to provide /bin/sh. However the/some SAGE build scripts seem to assume that /bin/sh is provided by bash which is not necessarily true. Consequently, make and upgrade fail on Ubuntu Edgy (6.10). This bug was reported to me by Ralf Weinmann and I cannot personally confirm this as I don't have access to a Ubuntu Edgy install.


---

Comment by was created at 2007-03-21 22:44:01

Resolution: invalid


---

Comment by was created at 2007-03-21 22:44:01

This bug is too imprecise to be of any use, especially since I build SAGE regularly on Edgy eft and it works fine.   (In fact it's my main devel environment.)
