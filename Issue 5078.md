# Issue 5078: bug in factoring out constant literal

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-01-23 22:23:39

Assignee: cwitty


```
sage: R1 = PolynomialRing(QQ, 'x,y,z')
sage: R1.0
Traceback (most recent call last):
...
NameError: name 'R1_sage_const_p0' is not defined
sage: R1.gen(0)
x
```



---

Attachment


---

Comment by boothby created at 2009-01-24 02:36:26

Works for me.


---

Comment by mabshoff created at 2009-01-24 16:28:32

Merged in Sage 3.3.alpha2


---

Comment by mabshoff created at 2009-01-24 16:28:32

Resolution: fixed
