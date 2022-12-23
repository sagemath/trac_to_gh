# Issue 9473: notebook: execute bit set on pickle's, but shouldn't be (really easy to fix)

Issue created by migration from https://trac.sagemath.org/ticket/9473

Original creator: was

Original creation time: 2010-07-11 08:51:04

Assignee: jason, was

CC:  chapoton

The execute bit is set on some pickles in sage_notebook.sagenb for no reason:

```

executable bit set?  huh?

sage: !ls -l
total 28
-rwx------  1 sagenb sagenb   253 2010-07-06 00:52 conf.pickle
drwxr-xr-x 39 sagenb sagenb  4096 2010-05-22 08:58 home
-rw-r--r--  1 sagenb sagenb     4 2010-05-20 12:04 twistd.pid
-rw-r--r--  1 sagenb sagenb  2560 2010-05-20 12:04 twistedconf.tac
-rwx------  1 sagenb sagenb 11116 2010-07-06 00:52 users.pickle
```


Fix this.   This is probably really easy.   I think the notebook server does a chmod somewhere to make sure other and group don't have access, and this is done incorrectly.


---

Comment by mkoeppe created at 2020-08-18 00:36:52

Proposing to close all sagenb tickets as outdated, so that all remaining open tickets in the notebook component are about the Jupyter notebook.


---

Comment by mkoeppe created at 2020-08-18 00:36:52

Changing status from new to needs_review.


---

Comment by chapoton created at 2020-09-08 09:48:28

Resolution: invalid
