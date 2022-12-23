# Issue 5742: ATLAS.spkg: parallel make breaks on system with "real" sh

Issue created by migration from https://trac.sagemath.org/ticket/5742

Original creator: mabshoff

Original creation time: 2009-04-11 01:23:52

Assignee: mabshoff

The spkg-install-$FOO script that actually builds atlas uses `/bin/sh` as shebang and does not export MAKE properly. So if one builds Sage on Solaris or FreeBSD with parallel make where sh is the real shell things blow up since ATLAS does not handle parallel make too well :)

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-18 06:56:01

Changing status from new to assigned.


---

Comment by mabshoff created at 2009-04-18 23:24:50

Resolution: fixed


---

Comment by mabshoff created at 2009-04-18 23:24:50

Fixed in Sage 3.4.1.rc4 via #5219.

Cheers,

Michael
