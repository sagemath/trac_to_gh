# Issue 3701: [with spkg, needs review] Solaris: fix polybori build due to bashism

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2008-07-21 21:55:21

Assignee: mabshoff

Polybori.spkg contains some bashism that cause trouble on Solaris. So change the shebang to use "#1/usr/bin/env bash". That is the only change in the spkg at

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.0.6/alpha1/polybori-0.3.1.p4.spkg

Cheers,

Michael


---

Comment by mabshoff created at 2008-07-21 21:55:28

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-07-21 22:12:32

Resolution: fixed


---

Comment by mabshoff created at 2008-07-21 22:12:32

Merged in Sage 3.0.6.rc0
