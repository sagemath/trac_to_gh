# Issue 2112: __contains__ sometimes fails with SR elements due to == returning an equation

Issue created by migration from Trac.

Original creator: mhansen

Original creation time: 2008-02-08 13:02:59

Assignee: somebody


```
sage: SR(2) in ZZ
False
```


This is easy to fix by having __contains__ use bool(foo==bar) rather than just foo == bar.


---

Comment by mhansen created at 2008-02-08 13:03:09

Changing assignee from somebody to mhansen.


---

Comment by mhansen created at 2008-02-08 13:03:09

Changing status from new to assigned.


---

Attachment

Cause no problems with -testall on my machine.


---

Comment by ncalexan created at 2008-02-15 04:16:37

So small, I say apply.


---

Comment by mabshoff created at 2008-02-15 04:51:38

Resolution: fixed


---

Comment by mabshoff created at 2008-02-15 04:51:38

Merged in Sage 2.10.2.alpha0
