# Issue 3993: implicit multiplication doesn't work in notebook

Issue created by migration from https://trac.sagemath.org/ticket/3993

Original creator: jason

Original creation time: 2008-08-29 18:00:58

Assignee: somebody

CC:  was

In a notebook cell, do

```
implicit_multiplication(True)
2x
```


It returns a syntax error.  Things work fine from the command line.


---

Comment by AlexGhitza created at 2009-01-22 18:18:06

Changing type from defect to enhancement.


---

Comment by kcrisman created at 2009-11-18 17:30:42

To release manager:  Is this dealt with by one of the SageNB upgrades?  I think there was a recent post about this.


---

Comment by AlexGhitza created at 2010-01-02 02:13:05

Changing component from basic arithmetic to notebook.


---

Comment by was created at 2010-01-02 08:08:16

This is fixed by #7514.


---

Comment by was created at 2010-01-02 08:08:25

Resolution: fixed
