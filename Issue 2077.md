# Issue 2077: matrix.column(i) should throw error when i is larger than the number of columns in the matrix (minus 1).

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2008-02-06 23:29:16

Assignee: was


```
sage: a=matrix([[1,2],[3,4]])
sage: a.column(0)
(1, 3)
sage: a.column(1)
(2, 4)
sage: a.column(3)
(2, 4)
sage: a.column(2)
(1, 3)
```


The documentation for a.column says that it behaves like list indexing when given a negative index.  We should probably also act like list indexing for positive indices that are too big and throw an error:


```
sage: l=range(3); l
[0, 1, 2]
sage: l[3]
---------------------------------------------------------------------------
<type 'exceptions.IndexError'>            Traceback (most recent call last)

/home/grout/downloads/cython-callback/<ipython console> in <module>()

<type 'exceptions.IndexError'>: list index out of range
```




---

Attachment


---

Attachment

Apply the .2.patch (which corrects a minor typo).


---

Comment by mhansen created at 2008-02-07 08:16:28

Looks good to me.


---

Comment by mabshoff created at 2008-02-07 10:19:34

Resolution: fixed


---

Comment by mabshoff created at 2008-02-07 10:19:34

Merged matrix-column-wrapping.2.patch in Sage 2.10.2.alpha2
