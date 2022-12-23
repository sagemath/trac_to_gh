# Issue 6570: indexing a matrix with a non-integer should return an IndexError, not a TypeError

Issue created by migration from https://trac.sagemath.org/ticket/6570

Original creator: jason

Original creation time: 2009-07-20 14:05:39

Assignee: was


```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: a=random_matrix(ZZ,4)
sage: a[1,1.5]  
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
| Sage Version 4.1, Release Date: 2009-07-09                         |
| Type notebook() for the GUI, and license() for information.        |
/home/grout/.sage/temp/tiny/11658/_home_grout__sage_init_sage_0.py in <module>()

/home/grout/sage/local/lib/python2.6/site-packages/sage/matrix/matrix0.so in sage.matrix.matrix0.Matrix.__getitem__ (sage/matrix/matrix0.c:4772)()
    837             else:
    838                 if not PyIndex_Check(col_index):
--> 839                     raise TypeError, "index must be an integer"
    840                 col = col_index
    841                 if col < 0:

TypeError: index must be an integer
sage: a[1.5,1]
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/grout/.sage/temp/tiny/11658/_home_grout__sage_init_sage_0.py in <module>()

/home/grout/sage/local/lib/python2.6/site-packages/sage/matrix/matrix0.so in sage.matrix.matrix0.Matrix.__getitem__ (sage/matrix/matrix0.c:4487)()
    811             else:
    812                 if not PyIndex_Check(row_index):
--> 813                     raise TypeError, "index must be an integer"
    814                 row = row_index
    815                 if row < 0:

TypeError: index must be an integer
```



---

Comment by rbeezer created at 2009-07-21 03:29:30

The Python Docs at

http://docs.python.org/library/exceptions.html

say:

`IndexError`

    Raised when a sequence subscript is out of range. (Slice indices are silently truncated to fall in the allowed range; if an index is not a plain integer, `TypeError` is raised.)

This seems to be the way these are both being used in the locations referenced.  So it would appear that current use is consistent with the Python standards?


---

Comment by jason created at 2009-07-21 07:00:55

Thanks for looking this up.  This ticket is obviously invalid, then.

I feel silly.  I've had my hands in this code before, and now that you bring this up, it feels like I've looked this up before...


---

Comment by mvngu created at 2009-07-21 07:02:41

Resolution: invalid
