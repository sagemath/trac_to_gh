# Issue 645: multi-argument call for symbolic expressions

Issue created by migration from Trac.

Original creator: robertwb

Original creation time: 2007-09-12 21:32:07

Assignee: was


```
sage: x,y = var('x y')
sage: f(3)
y + 3
sage: f(3)(4)
7
sage: f(3,4)
---------------------------------------------------------------------------
<type 'exceptions.TypeError'>             Traceback (most recent call last)

/Users/robert/sage/sage-2.5/devel/sage-working/<ipython console> in <module>()

<type 'exceptions.TypeError'>: __call__() takes at most 2 arguments (3 given)
sage: 

```



---

Comment by mhansen created at 2007-11-30 23:24:03

Changing assignee from was to mhansen.


---

Comment by mhansen created at 2007-11-30 23:24:03

Changing status from new to assigned.


---

Attachment

This should be applied after #1345.


---

Comment by cwitty created at 2007-12-01 02:57:07

Looks good to me, and doctests still pass in sage/calculus/*.


---

Comment by mabshoff created at 2007-12-01 11:16:26

Resolution: fixed


---

Comment by mabshoff created at 2007-12-01 11:16:26

Merged in 2.8.15.alpha0.
