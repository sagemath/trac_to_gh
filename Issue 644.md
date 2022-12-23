# Issue 644: (sin + cos)(1) does not work

Issue created by migration from https://trac.sagemath.org/ticket/644

Original creator: robertwb

Original creation time: 2007-09-12 19:00:58

Assignee: was

Both sin and cos are functions of one (undetermined) variable, and can be called, but when one performs arithmetic on them this changes. 

Maybe there should be a CallableSymbolicExpressionRing with an unnamed variable that coerces into any CallableSymbolicExpressionRing with a specified variable name? 

sage: f = sin
sage: g = cos
sage: f(1)
sin(1)
sage: g(1)
cos(1)
sage: h = f+g
sage: h(1)
sin + cos # should be sin(1)+cos(1)
sage: f = 3*sin
sage: f(1)
3*sin # should be 3*sin(1)


---

Comment by robertwb created at 2007-09-12 19:02:20

Better formatting: 

```
sage: f = sin
sage: g = cos
sage: f(1)
sin(1)
sage: g(1)
cos(1)
sage: h = f+g
sage: h(1)
sin + cos         # should be sin(1)+cos(1), or at least throw an error
sage: f = 3*sin
sage: f(1)
3*sin             # should be 3*sin(1)
```



---

Comment by robertwb created at 2007-09-13 09:12:41

Also should have 


```
sage: f(x) = x^2
sage: f + sin
x |--> sin(x) + x^2
```



---

Comment by robertwb created at 2007-09-13 09:13:02

See much discussion at http://groups.google.com/group/sage-devel/browse_thread/thread/2f627fbe8d0f71c0


---

Comment by mhansen created at 2007-12-01 06:50:49

Changing status from new to assigned.


---

Comment by mhansen created at 2007-12-01 06:50:49

Changing assignee from was to mhansen.


---

Comment by mhansen created at 2007-12-01 06:50:49

This patch should be applied after #644.


---

Attachment

Merged in 2.8.15.alpha1.


---

Comment by mabshoff created at 2007-12-01 16:16:45

Resolution: fixed
