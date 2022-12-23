# Issue 858: add support for numpy arrays with integer entries

Issue created by migration from https://trac.sagemath.org/ticket/858

Original creator: mhansen

Original creation time: 2007-10-12 04:51:54

Assignee: was

Keywords: numpy


```
sage: import numpy
sage: a = numpy.array([[1,2],[3,4]],'int32')
sage: matrix(a)
---------------------------------------------------------------------------
<type 'exceptions.TypeError'>             Traceback (most recent call last)

/home/mhansen/sage/devel/sage-856/<ipython console> in <module>()

/home/mhansen/sage/local/lib/python2.5/site-packages/sage/matrix/constructor.py in matrix(arg0, arg1, arg2, arg3, sparse)
    399                     raise TypeError("cannot convert numpy matrix to SAGE matrix")
    400             else:
--> 401                 raise TypeError("cannot convert numpy matrix to SAGE matrix")
    402 
    403         else:

<type 'exceptions.TypeError'>: cannot convert numpy matrix to SAGE matrix
```



---

Attachment

patch #1


---

Attachment

added doctest


---

Comment by mhansen created at 2007-10-12 05:47:01

#859 should be applied before these two patches


---

Comment by mhansen created at 2007-10-12 05:47:01

Changing assignee from was to mhansen.


---

Comment by mhansen created at 2007-10-12 05:47:01

Changing status from new to assigned.


---

Comment by was created at 2007-10-13 08:02:04

Resolution: fixed
