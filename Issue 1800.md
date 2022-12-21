# Issue 1800: bug with RealIntervalField / MPFI

Issue created by migration from Trac.

Original creator: mhansen

Original creation time: 2008-01-17 06:08:25

Assignee: jkantor


```
sage: a = factorial(100)/exp(2)
sage: bits = 427; RealIntervalField(bits)(a).upper() - RealIntervalField(bits)(a).lower()
7.9228162514264337593543950336000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000e28
sage: bits = 428; RealIntervalField(bits)(a).upper() - RealIntervalField(bits)(a).lower()
0.00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
```



---

Comment by cwitty created at 2008-01-17 07:14:45

Changing status from new to assigned.


---

Comment by cwitty created at 2008-01-17 07:14:45

Changing assignee from jkantor to cwitty.


---

Comment by cwitty created at 2008-01-17 07:14:45

It looks like coercion from symbolic expressions to intervals is broken (because nobody ever wrote the code to do it, and the generic code that happens to be used doesn't work).


---

Attachment


---

Comment by cwitty created at 2008-01-19 14:53:31

Changing priority from minor to major.


---

Comment by ncalexan created at 2008-01-19 18:59:17

Solution seems correct.


---

Comment by mabshoff created at 2008-01-19 19:56:02

Resolution: fixed


---

Comment by mabshoff created at 2008-01-19 19:56:02

Merged in Sage 2.10.1.alpha0
