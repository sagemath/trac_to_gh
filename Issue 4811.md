# Issue 4811: doctesting line numbers in report are now completely broken.  They were fine ins age-3.2.1

Issue created by migration from https://trac.sagemath.org/ticket/4811

Original creator: was

Original creation time: 2008-12-16 07:25:21

Assignee: mabshoff

Try breaking any doctest and you get stuff like this:

```
was@sage:~/build/sage-3.2.2.alpha2$ ./sage -t devel/sage/sage/matrix/matrix_modn_dense.pyx
sage -t  "devel/sage/sage/matrix/matrix_modn_dense.pyx"     
**********************************************************************
File "/home/was/build/sage-3.2.2.alpha2/devel/sage/sage/matrix/matrix_modn_dense.pyx", line 276, in __main__.example_6
Failed example:
    m###line 554:_sage_    >>> m

```


Notice the line 276 there.   In the old sage:

```
was@sage:~/d/sage/matrix$ sage -t matrix_modn_dense.pyx
sage -t  "devel/sage-main/sage/matrix/matrix_modn_dense.pyx"**********************************************************************
File "/home/was/s/devel/sage-main/sage/matrix/matrix_modn_dense.pyx", line 554:
    sage: m
Expected:
    [19 18 17]
    [16 15 14]
    [13 12 11]
Got:
```

}}}


---

Attachment


---

Comment by gfurnish created at 2008-12-16 07:37:39

Changing status from new to assigned.


---

Comment by gfurnish created at 2008-12-16 07:37:39

Changing assignee from mabshoff to gfurnish.


---

Comment by mabshoff created at 2008-12-17 04:02:28

Positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2008-12-17 14:03:15

Resolution: fixed


---

Comment by mabshoff created at 2008-12-17 14:03:15

Merged in Sage 3.2.2.rc1
