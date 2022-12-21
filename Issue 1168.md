# Issue 1168: asinh/acosh/atanh are only partially known to sage

Issue created by migration from Trac.

Original creator: zimmerma

Original creation time: 2007-11-13 22:58:42

Assignee: was


```
sage: asinh(1)
<type 'exceptions.NameError'>: name 'asinh' is not defined
sage: asinh(x)
<type 'exceptions.NameError'>: name 'asinh' is not defined
```

but:

```
sage: integrate(1/sqrt(9+x^2), x)
asinh(x/3)
sage: (1.0).asinh()
0.881373587019543
```

The same holds for acosh and atanh.


---

Comment by mhansen created at 2007-11-30 23:38:24

This was fixed in an earlier patch.

```
sage: asinh(1)
asinh(1)
sage: asinh(x)
asinh(x)
sage: acosh(x)
acosh(x)
sage: atanh(x)
atanh(x)
```



---

Comment by mhansen created at 2007-11-30 23:38:24

Changing status from new to assigned.


---

Comment by mhansen created at 2007-11-30 23:38:24

Changing assignee from was to mhansen.


---

Comment by mhansen created at 2007-11-30 23:38:30

Resolution: fixed
