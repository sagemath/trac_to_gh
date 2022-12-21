# Issue 2976: get rid of /home/jec/sage-3.0.rc0/tmp/test-dsage.log error at the end of tests

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-04-20 22:07:38

Assignee: failure




---

Comment by yi created at 2008-04-20 22:18:58

This bug is caused by the commenting out of dsage unit tests. The fix is

1) Someone (was?) reviews #2553
2) Uncomment line 15 of sage-maketest


---

Comment by was created at 2008-04-20 23:26:40

Resolution: duplicate


---

Comment by was created at 2008-04-20 23:26:40

This will be fixed by #2553... Closed as a dup.
