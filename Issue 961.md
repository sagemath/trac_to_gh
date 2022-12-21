# Issue 961: sage -standard fails without write permission to $SAGE_LOCAL/tmp

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2007-10-21 14:19:24

Assignee: mabshoff

Hello,

I am not sure if this qualifies as a bug, but by storing the list in ~/.sage the following should work even if the user doesn't have write permission below $SAGE_LOCAL:

```
mabshoff`@`sage:/tmp/Work-mabshoff/sage-2.8.8$ sage -standard
Using SAGE Server http://www.sagemath.org//packages
http://www.sagemath.org//packages/standard/list --> /home/was/s/tmp/list
[Errno 13] Permission denied: '/home/was/s/tmp/list'



********************************************************************************



Error contacting http://www.sagemath.org//packages/standard/list. Try using an alternative server.
For example, from the bash prompt try typing

   export SAGE_SERVER=http://sage.scipy.org/sage/

then try again.



********************************************************************************
```

Cheers,

Michael


---

Comment by mabshoff created at 2007-10-21 14:19:30

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-10-30 06:24:54

The same applies for -optional, -experimental and so on. This ought to be fixed since it has been hit a bunch of times by various people.

Cheers,

Michael


---

Comment by jdemeyer created at 2013-05-16 07:47:51

Resolution: worksforme
