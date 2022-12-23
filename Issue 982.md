# Issue 982: abs(x) returns incorrect LaTex

Issue created by migration from https://trac.sagemath.org/ticket/982

Original creator: mhansen

Original creation time: 2007-10-24 17:39:00

Assignee: was


```
sage: f = abs(x)
sage: latex(f)
\abs \left( x \right)
```


but it should be


```
sage: latex(f)
\mathrm{abs} \left| x \right|
```



---

Comment by mhansen created at 2007-10-24 17:39:06

Changing assignee from was to mhansen.


---

Comment by mhansen created at 2007-10-24 17:39:06

Changing status from new to assigned.


---

Comment by mhansen created at 2007-10-24 17:42:13

Oops.  I mean to write, it should be:

```
sage: latex(abs)
\mathrm{abs}
sage: latex(abs(x))
\left| x \right|
```



---

Attachment


---

Comment by mhansen created at 2007-10-24 17:50:42

Replying to [comment:1 mhansen]:


---

Comment by malb created at 2007-10-24 19:16:39

applied to 2.8.9.alpha1


---

Comment by malb created at 2007-10-24 19:16:39

Resolution: fixed
