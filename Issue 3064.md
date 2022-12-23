# Issue 3064: empty matrices: density() function throws a ZeroDivisionError

Issue created by migration from https://trac.sagemath.org/ticket/3064

Original creator: dfdeshom

Original creation time: 2008-04-30 15:12:48

Assignee: was


```
sage: a = matrix([])

sage: a.density()
---------------------------------------------------------------------------


<type 'exceptions.ZeroDivisionError'>: Rational division by zero
```



---

Attachment

Patch attached.


---

Comment by mabshoff created at 2008-05-01 05:45:57

Resolution: fixed


---

Comment by mabshoff created at 2008-05-01 05:45:57

Merged in Sage 3.0.1.alpha1
