# Issue 1116: sage -sdist recreates certain empty files in local/bin

Issue created by migration from https://trac.sagemath.org/ticket/1116

Original creator: mabshoff

Original creation time: 2007-11-06 22:26:03

Assignee: mabshoff


```
mabshoff@sage:/tmp/Work-mabshoff/sage-2.8.12.alpha1/local/bin$ hg status
? sage-cleaner.orig
? sage-clone.orig
? sage-lo
? sage-make
```



---

Comment by mabshoff created at 2007-12-04 14:35:21

This annoys me and causes the $SAGE_LOCAL/bin/ repo to report files with unclear status.

Cheers,

Michael


---

Comment by mabshoff created at 2008-02-15 22:41:01

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-02-15 22:41:01

I removed the offending files from the sage_scripts repo. Once 2.10.2.alpha1 is out we ought to verify that the problem is really gone.

Cheers,

Michael


---

Comment by mabshoff created at 2008-02-17 04:37:17

I did some testing and it seems to work. I will reopen in case it turns out to be an incomplete fix.

Cheers,

Michael


---

Comment by mabshoff created at 2008-02-17 04:37:32

Resolution: fixed


---

Comment by mabshoff created at 2008-02-17 04:37:32

Merged in Sage 2.10.2.alpha1
