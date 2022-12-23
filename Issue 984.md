# Issue 984: sage-2.8.9.rc1: sage-banner is empty

Issue created by migration from https://trac.sagemath.org/ticket/984

Original creator: cwitty

Original creation time: 2007-10-25 00:50:42

Assignee: was

sage is missing its startup message in 2.8.9.rc1:

```
cwitty@magnetar:~/sage-2.8.9.rc1$ ./sage

sage: 
```




---

Comment by was created at 2007-10-25 07:56:00

When I do sage -sdist even using that binary I get that a banner
is created.  I banner certainly gets created when I do -sdist from
my sage install.  So it will be in the released version.


---

Comment by mabshoff created at 2007-10-25 10:48:23

So this ought to be close against 2.8.9 then.

Michael


---

Comment by mabshoff created at 2007-10-27 05:17:10

Fixed in final 2.8.9 and verified with local build.

Cheers,

Michael


---

Comment by mabshoff created at 2007-10-27 05:17:37

Resolution: fixed
