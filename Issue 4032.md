# Issue 4032: [with spkg, needs review] Add x86 Solaris build support for libSingular

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2008-09-01 09:28:07

Assignee: mabshoff

The spkg at 

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.1.2/alpha4/singular-3-0-4-4-20080711.p1.spkg

fixes three issues:

 * remove non-POSIX behavior of tail in spkg-install
 * add options to build libsingular on x86 Solaris
 * work around problem when installing libsingular headers when /usr/bin/install is not installed


---

Comment by mabshoff created at 2008-09-01 09:50:10

Changing status from new to assigned.


---

Comment by malb created at 2008-09-01 10:11:32

Builds/runs fine on my 64-bit Debian/GNU Linux Core2Duo


---

Comment by mabshoff created at 2008-09-01 10:30:40

Resolution: fixed


---

Comment by mabshoff created at 2008-09-01 10:30:40

Merged in Sage 3.1.2.alpha4
