# Issue 3202: show() smashes multiplied numbers together so the product looks like a number

Issue created by migration from https://trac.sagemath.org/ticket/3202

Original creator: jason

Original creation time: 2008-05-14 06:04:13

Assignee: boothby

To see this, evaluate the following in a notebook cell:


```
var('r,z')
a=(r*z^2).integrate(z,0,r).integrate(r,0,sqrt(9/2))*2*pi
a.show()
print a
```


Firefox 3 Beta 5; Ubuntu 8.04


---

Comment by boothby created at 2009-01-22 00:36:44

This is a problem with that object's show method, not with the notebook.


---

Comment by boothby created at 2009-01-22 00:36:44

Changing assignee from boothby to burcin.


---

Comment by boothby created at 2009-01-22 00:36:44

Changing component from notebook to calculus.


---

Comment by burcin created at 2009-04-11 16:13:33

This should be fixed in the pynac symbolics after #5753 is in.


---

Comment by burcin created at 2009-05-25 10:28:33

Changing status from new to assigned.


---

Comment by burcin created at 2009-05-25 10:28:33

This is fixed in 4.0.rc0. There is a doctest mentioning this bug on line 492 of sage/symbolic/expression.pyx.

This bug should be closed as fixed.


---

Comment by mhansen created at 2009-05-26 17:02:06

Resolution: fixed
