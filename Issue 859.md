# Issue 859: Cannot coerce numpy integral types to ZZ

Issue created by migration from Trac.

Original creator: cwitty

Original creation time: 2007-10-12 05:16:54

Assignee: cwitty


```
sage: import numpy
sage: ZZ(numpy.int64(3))
---------------------------------------------------------------------------
<type 'exceptions.TypeError'>             Traceback (most recent call last)

/home/cwitty/my-sage/<ipython console> in <module>()

/home/cwitty/my-sage/integer_ring.pyx in integer_ring.IntegerRing_class.__call__()

<type 'exceptions.TypeError'>: unable to coerce element to an integer
```



---

Attachment


---

Comment by was created at 2007-10-13 07:41:51

Resolution: fixed
