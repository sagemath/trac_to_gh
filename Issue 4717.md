# Issue 4717: [with patch, needs review] matrix_plot should also accept numpy arrays

Issue created by migration from https://trac.sagemath.org/ticket/4717

Original creator: whuss

Original creation time: 2008-12-05 13:22:19

Assignee: whuss




---

Attachment


---

Attachment


---

Comment by mhansen created at 2008-12-08 01:50:23

Everything looks good except that it's the transpose of what is what wanted.  I attached a patch which removes the transpose.  I'm not sure if that needs an additional review or not.  Wilfried, do you want to take a look?

Apply only trac_4717.patch.


---

Comment by whuss created at 2008-12-08 12:59:33

With the transpose removed, the following doctest fails,


```
sage -t  "devel/sage-matrix_plot/sage/plot/matrix_plot.py"  
**********************************************************************
File "/local/data/huss/software/sage-3.2.1/devel/sage-matrix_plot/sage/plot/matrix_plot.py",
line 40:
    sage: list(sorted(m.get_minmax_data().items()))
Expected:
    [('xmax', 4), ('xmin', 0), ('ymax', 3), ('ymin', 0)]
Got:
    [('xmax', 3), ('xmin', 0), ('ymax', 4), ('ymin', 0)]
**********************************************************************
```


and the rows of matrices are plottet as columns.

Greetings,

Wilfried


---

Comment by mhansen created at 2008-12-08 13:06:14

Weird, with the transpose I get that the rows are plotted as columns.  For example, with your original patch, 


```
sage: matrix_plot([[1,1,10],[1,1,1],[1,1,1]])
```


produces http://sage.math.washington.edu/home/mhansen/4717.png .


---

Attachment

final version


---

Comment by whuss created at 2008-12-09 08:49:01

You are right, the transpose was wrong.
But I also mixed up the xrange and yrange, that was why I got
strange results for non square matrices.

The new patch fixes it. Now matrix_plot behaves the same as
without the patch.

Apply only trac_4717.2.patch

Greetings,

Wilfried.


---

Comment by mabshoff created at 2008-12-10 07:52:53

Resolution: fixed


---

Comment by mabshoff created at 2008-12-10 07:52:53

Merged trac_4717.2.patch in Sage 3.2.2.alpha1
