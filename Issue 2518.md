# Issue 2518: improve the SAGE_ROOT/local/bin/sage-cleaner script so that it kills those damn lisp.run processes

Issue created by migration from https://trac.sagemath.org/ticket/2518

Original creator: was

Original creation time: 2008-03-14 19:25:20

Assignee: cwitty

CC:  was mhansen robertwb

Fact is, several people have observed lisp.run's getting left running.

If *anybody* can find a 100% reliable way to replicate this problem, PLEASE LET US KNOW!


---

Comment by mabshoff created at 2008-07-29 17:23:54

Changing assignee from cwitty to mabshoff.


---

Comment by mabshoff created at 2008-07-29 17:23:54

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-07-29 17:23:54

The issue here is likely that we use

```
os.kill(int(pid),0)
```

It is likely that using "kill -9 $PID" via os.system() ought to fix the issue.

Cheers,

Michael


---

Comment by mabshoff created at 2009-05-13 18:41:51

I believe the problem was that if clisp crashed and restarted those processes could get stuck at 99% and not be killed at exit.

This hasn't been reported in a while, so I would prefer to close this as fixed. Thoughts?

Cheers,

Michael


---

Comment by timdumol created at 2010-01-19 07:15:54

Resolution: fixed


---

Comment by timdumol created at 2010-01-19 07:15:54

Since this hasn't been reported in around 8 months, I think this should be closed.


---

Comment by mhansen created at 2010-01-19 07:17:56

Resolution changed from fixed to invalid


---

Comment by mhansen created at 2010-01-19 07:17:56

Seems reasonable to me.
