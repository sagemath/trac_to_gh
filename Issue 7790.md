# Issue 7790: Setting a default max/min bound when calling MixedIntegerLinearProgram.new_variable

Issue created by migration from https://trac.sagemath.org/ticket/7790

Original creator: ncohen

Original creation time: 2009-12-29 18:17:30

Assignee: jkantor

CC:  yzh

Being able to write something like :


```
p = MixedIntegerLinearProgram()
v = p.new_variable(min=3, max =8)
```


Would be really nice !


---

Comment by ncohen created at 2010-09-06 11:12:48

Changing component from numerical to linear programming.
