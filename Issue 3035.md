# Issue 3035: calculus/equations.py
segfault with new cython & -ba

Issue created by migration from https://trac.sagemath.org/ticket/3035

Original creator: gfurnish

Original creation time: 2008-04-26 23:48:15

Assignee: was

calculus/equations.py segfaults on test with patched cython and -ba.  However it only segfaults most of the time on automated testing, and does not segfault for gdb, valgrind, etc.

The test in question is 

```
    sage: loads(dumps(eqn)) == eqn 
    True
```



---

Comment by gfurnish created at 2008-04-27 00:30:00

This also happens with stefan's cython-dev code.


---

Comment by gfurnish created at 2008-04-27 00:56:16

This does not segfault as of sage-3.0.alpha0


---

Comment by gfurnish created at 2008-04-27 02:52:37

This problem is introduced after sage-3.0.rc0


---

Comment by was created at 2008-04-27 03:16:02

This is caused by #2419, according to gfurnish.


---

Comment by gfurnish created at 2008-04-27 03:28:31

Specifically this is caused by sage-2419-refactor.patch


---

Comment by gfurnish created at 2008-04-27 03:40:07

Everything in that patch except the functions

```
    def _crash_msg(self):
    def _interrupt(self):
```

cause segfaults.


---

Comment by gfurnish created at 2008-04-27 03:43:20

Correction:
Everything in that patch that alters expect.py except the functions

```
    def _crash_msg(self):
    def _interrupt(self):
```

cause segfaults


---

Comment by gfurnish created at 2008-04-27 21:27:57

This does not segfault if you first delete ~/.sage/ or if it does not already exist.  It does segfault after it is run once until the folder is again deleted.


---

Comment by gfurnish created at 2008-05-01 10:24:26

This seems to have "magically" fixed itself for me after 3.0.1.alpha1.  After consulting with mabshoff we have decided to close this as something likely caused by my local machine.


---

Comment by gfurnish created at 2008-05-01 10:24:26

Resolution: fixed
