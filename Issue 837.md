# Issue 837: RealNumber should have abs method

Issue created by migration from https://trac.sagemath.org/ticket/837

Original creator: dmharvey

Original creation time: 2007-10-07 15:22:26

Assignee: somebody

This violates the principle of least surprise, at least for me:


```
sage: x = -2.0
sage: x.abs()
---------------------------------------------------------------------------
<type 'exceptions.AttributeError'>        Traceback (most recent call last)

/Users/david/sage-2.8.5/<ipython console> in <module>()

<type 'exceptions.AttributeError'>: 'sage.rings.real_mpfr.RealNumber' object has no attribute 'abs'
```




---

Comment by mabshoff created at 2007-10-19 19:01:13

Changing assignee from somebody to cwitty.


---

Attachment


---

Comment by cwitty created at 2007-10-20 20:06:06

The attached patch actually adds an abs() method to every RingElement (that just forwards to the `__abs__` method).


---

Comment by malb created at 2007-10-23 21:00:25

Resolution: fixed


---

Comment by malb created at 2007-10-23 21:00:25

applied to 2.8.9.alpha0
