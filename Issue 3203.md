# Issue 3203: show() smashes multiplied numbers together so the product looks like a number

Issue created by migration from https://trac.sagemath.org/ticket/3203

Original creator: jason

Original creation time: 2008-05-14 12:13:05

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

Comment by dmharvey created at 2008-06-21 17:21:19

duplicate of #3202


---

Comment by dmharvey created at 2008-06-21 17:21:19

Resolution: duplicate
