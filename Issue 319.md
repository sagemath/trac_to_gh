# Issue 319: can't divide matrix over QQ by a rational

Issue created by migration from Trac.

Original creator: dmharvey

Original creation time: 2007-03-12 05:16:04

Assignee: somebody


```
sage: Matrix(QQ, 2, 2, [1, 1, 1, 1]) / 2
---------------------------------------------------------------------------
<type 'exceptions.TypeError'>             Traceback (most recent call last)

/home/dmharvey/sage-2.2/<ipython console> in <module>()

/home/dmharvey/sage-2.2/element.pyx in element.RingElement.__div__()

/home/dmharvey/sage-2.2/element.pyx in element.bin_op_c()

<type 'exceptions.TypeError'>: unsupported operand parent(s) for '/': 'Full MatrixSpace of 2 by 2 dense matrices over Rational Field' and 'Integer Ring'
```




---

Comment by dmharvey created at 2007-08-18 17:13:03

Resolution: fixed


---

Comment by dmharvey created at 2007-08-18 17:13:03

this is apparently fixed at least as of 2.8
