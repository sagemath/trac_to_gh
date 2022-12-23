# Issue 835: cannot coerce real numbers to Integer

Issue created by migration from https://trac.sagemath.org/ticket/835

Original creator: dmharvey

Original creation time: 2007-10-06 15:33:28

Assignee: somebody

If a real number is exactly an integer, it should be possible to coerce to an Integer, but this is what happens:


```
sage: Integer(RR(2.0))
---------------------------------------------------------------------------
<type 'exceptions.TypeError'>             Traceback (most recent call last)

/Users/david/sage-2.8.5/<ipython console> in <module>()

/Users/david/sage-2.8.5/integer.pyx in integer.Integer.__init__()

<type 'exceptions.TypeError'>: unable to coerce element to an integer
```




---

Comment by mabshoff created at 2007-10-07 14:36:51

Changing priority from major to critical.


---

Attachment


---

Comment by was created at 2007-10-13 05:46:07

Resolution: fixed
