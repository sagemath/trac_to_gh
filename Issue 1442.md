# Issue 1442: wrong statement in calculus.py

Issue created by migration from https://trac.sagemath.org/ticket/1442

Original creator: zimmerma

Original creation time: 2007-12-09 21:36:34

Assignee: tba

I'm reading calculus.py (this is probably the best way to learn SAGE).
This statement seems wrong to me:

```
\sage predefines upper and lowercase letters as global
    indeterminates.
```

Indeed, I believe only 'x' is predefined.


---

Attachment


---

Comment by mhansen created at 2007-12-14 07:19:26

Changing assignee from tba to mhansen.


---

Comment by mhansen created at 2007-12-14 07:19:26

Changing status from new to assigned.


---

Comment by was created at 2007-12-15 10:38:56

This used to be true, but it caused way too much confusion, so we changed it.  But forgot to change the docs.


---

Comment by mabshoff created at 2007-12-15 11:58:46

Looks good to me.

Cheers,

Michael


---

Comment by mabshoff created at 2007-12-15 11:59:45

Merged in 2.9.rc0.


---

Comment by mabshoff created at 2007-12-15 11:59:45

Resolution: fixed
