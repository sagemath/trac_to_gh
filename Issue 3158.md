# Issue 3158: singular-3-0-4-2-20080405.p1 requires flex

Issue created by migration from https://trac.sagemath.org/ticket/3158

Original creator: mabshoff

Original creation time: 2008-05-11 12:35:49

Assignee: mabshoff

singular-3-0-4-2-20080405.p1 requires flex to build. This is because libparse.l has the same time stamp as libparse.cc:

```
[mabshoff@eno Singular]$ ls -al libparse.*
-rw-r----- 1 mabshoff sage 109970 2008-03-19 13:44 libparse.cc
-rw-r----- 1 mabshoff sage   1524 2008-03-25 11:04 libparse.h
-rw-r----- 1 mabshoff sage  31422 2008-03-19 13:44 libparse.l
-rw-r----- 1 mabshoff sage     52 1998-04-20 06:05 libparse.sed
```

The fix is to touch libparse.cc so that the time stamp is older. I did that in the spkg linked at #2983.

Cheers,

Michael


---

Comment by mabshoff created at 2008-05-11 12:36:03

Changing status from new to assigned.


---

Comment by broune created at 2008-05-11 13:12:41

The spkg is functional (see review at #2983) and the issue is now resolved for the person who reported it. Positive review.


---

Comment by mabshoff created at 2008-05-11 13:13:35

Merged in Sage 3.0.2.alpha0


---

Comment by mabshoff created at 2008-05-11 13:13:35

Resolution: fixed
