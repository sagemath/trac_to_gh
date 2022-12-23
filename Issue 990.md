# Issue 990: no support for asinh/acosh etc. in symbolic expressions

Issue created by migration from https://trac.sagemath.org/ticket/990

Original creator: moretti

Original creation time: 2007-10-25 01:17:12

Assignee: was

Add support for inverse hyperbolic functions in Sage


---

Comment by mhansen created at 2007-11-30 23:32:43

This was fixed in an earlier patch.


```
sage: asinh(I)
I*pi/2
sage: asinh(2.0)
1.44363547517881
sage: acosh(2.0)
1.31695789692482
sage: atanh(1.0)
+infinity
sage: atanh(0.2)
0.202732554054082
```



---

Comment by mhansen created at 2007-11-30 23:32:43

Changing assignee from was to mhansen.


---

Comment by mhansen created at 2007-11-30 23:32:43

Changing status from new to assigned.


---

Comment by mhansen created at 2007-11-30 23:34:28

Resolution: fixed
