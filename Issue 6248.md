# Issue 6248: remove executable bits from sage-README-osx.txt

Issue created by migration from Trac.

Original creator: ddrake

Original creation time: 2009-06-08 14:41:05

Assignee: tbd

The file sage-README-osx.txt in SAGE_ROOT has mode 755, which is silly for a text file. Someone in charge of the "official" tarball should run a "chmod 644" on that file so it's not executable.


---

Comment by craigcitro created at 2009-06-18 10:32:06

Resolution: fixed


---

Comment by craigcitro created at 2009-06-18 10:32:06

Done.
