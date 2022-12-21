# Issue 1653: Bug raising an integer to a float  (probably really easy to fix in integer.pyx!)

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-01-02 06:29:41

Assignee: somebody

This is a bug:


```
sage: 2^float(3.1)
---------------------------------------------------------------------------
<type 'exceptions.TypeError'>             Traceback (most recent call last)

/Users/was/<ipython console> in <module>()

/Users/was/integer.pyx in sage.rings.integer.Integer.__pow__()

<type 'exceptions.TypeError'>: exponent (=3.1) must be an integer.
Coerce your numbers to real or complex numbers first.

Note:
sage: int(2)^float(3.1)
8.574187700290345
sage: (2/1)^float(3.1)
8.574187700290345
```


Note that


---

Comment by dmharvey created at 2008-01-02 18:22:39

Changing assignee from somebody to dmharvey.


---

Comment by dmharvey created at 2008-01-02 18:22:39

Changing status from new to assigned.


---

Attachment


---

Comment by mabshoff created at 2008-01-20 03:16:33

Resolution: fixed


---

Comment by mabshoff created at 2008-01-20 03:16:33

Merged in Sage 2.10.1.alpha0
