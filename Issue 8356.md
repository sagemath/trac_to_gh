# Issue 8356: python is configured with an unreconised option

Issue created by migration from https://trac.sagemath.org/ticket/8356

Original creator: drkirkby

Original creation time: 2010-02-25 03:58:59

Assignee: tbd

When python is configured, it is showing the following warning:


```
configure: WARNING: unrecognized options: --without-libpng
```


It would be good if when people update packages, they actually check things like the options. R recently had --without-iconv, despite that was no longer an option. 






---

Comment by drkirkby created at 2010-02-25 04:10:42

If the issues at #7867 can be solved by some updates to python, which may be the case, then I'll fix this as part of the fixes for #7867. Otherwise, it will have to wait for someone else to do it. 

I'm dropping the priority of this, as the warning is harmless.


---

Comment by drkirkby created at 2010-02-25 04:10:42

Changing priority from major to minor.


---

Comment by mhansen created at 2010-03-07 01:36:05

Fixed by #8440.


---

Comment by mhansen created at 2010-03-07 01:36:05

Resolution: fixed
