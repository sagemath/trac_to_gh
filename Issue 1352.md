# Issue 1352: [with patch] doctest error in 2.8.15.alpha0 polynomial_element.pyx

Issue created by migration from Trac.

Original creator: mhansen

Original creation time: 2007-12-01 18:32:53

Assignee: mhansen


```
sage: R.<x> = QQ[]; S.<y> = R[]
sage: f = x+y*x+y^2
sage: f(x=sqrt(2))
...
IndexError: tuple index out of range
```



---

Comment by mabshoff created at 2007-12-01 19:05:15

Resolution: fixed


---

Attachment

Merged in 2.8.15.alpha1.
