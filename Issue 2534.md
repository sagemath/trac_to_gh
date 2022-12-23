# Issue 2534: Sage does not handle Symmetrica's large integers

Issue created by migration from https://trac.sagemath.org/ticket/2534

Original creator: mhansen

Original creation time: 2008-03-15 23:36:24

Assignee: was

This causes problems when working with larger partitions.  For example,

```
sage: s = SFASchur(QQ)
sage: a = s([8,8])
sage: a.itensor(a)
```

gives the wrong results.


---

Comment by mhansen created at 2008-03-15 23:36:45

Changing status from new to assigned.


---

Comment by mhansen created at 2008-03-15 23:36:45

Changing assignee from was to mhansen.


---

Comment by mhansen created at 2008-03-15 23:36:45

I have a fix for this, but cannot get the Cython generated code to compile.


---

Attachment


---

Attachment

Only apply 2534.2.patch which was made against 2.10.4.alpha0.


---

Comment by mabshoff created at 2008-03-16 05:07:03

Patch looks good to me, testall shows no problem.


---

Comment by mabshoff created at 2008-03-16 05:23:43

Merged in Sage 2.10.4.rc0 - I will valgrind this once rc0 is out.


---

Comment by mabshoff created at 2008-03-16 05:23:43

Resolution: fixed
