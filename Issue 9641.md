# Issue 9641: Race condition with sage -tp

Issue created by migration from Trac.

Original creator: robertwb

Original creation time: 2010-07-29 21:34:32

Assignee: AlexGhitza

CC:  craigcitro

All files are named .sage/tmp/filename. At high parallelism, there are often conflicts (e.g. all.py, proof.py, ...) that result in untested code and spurious errors. 


---

Comment by AlexGhitza created at 2010-09-02 11:06:30

Changing component from algebra to doctest.


---

Comment by AlexGhitza created at 2010-09-02 11:06:30

Changing assignee from AlexGhitza to mvngu.


---

Comment by wjp created at 2011-01-11 01:21:20

Is this a duplicate of #9739 ? (This one is older, but #9739 has work in progress.)


---

Comment by jdemeyer created at 2011-01-11 06:17:41

Resolution: duplicate
