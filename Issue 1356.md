# Issue 1356: [with patch] fix bug when taking abs() of exactly known QQbar

Issue created by migration from https://trac.sagemath.org/ticket/1356

Original creator: cwitty

Original creation time: 2007-12-02 01:25:31

Assignee: somebody

The following test fails in 2.8.15.alpha1:

```
            sage: v = QQbar.zeta(3) + 1
            sage: v.exactify()
            sage: v.abs().minpoly()
```

but the attached patch fixes it.


---

Attachment

Now:

```
sage: v = QQbar.zeta(3) + 1
sage: v.exactify()
sage: v.abs().minpoly()
x - 1
```



---

Comment by was created at 2007-12-02 19:38:10

looks good to me.


---

Comment by mabshoff created at 2007-12-02 20:12:08

Merged in 2.8.15.rc0.


---

Comment by mabshoff created at 2007-12-02 20:12:08

Resolution: fixed
