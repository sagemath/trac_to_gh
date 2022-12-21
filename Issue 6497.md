# Issue 6497: [with patch, needs review] symbolic functions should understand numpy arrays

Issue created by migration from Trac.

Original creator: robertwb

Original creation time: 2009-07-09 10:14:40

Assignee: burcin

We want


```
sage: import numpy
sage: sin(numpy.arange(5))
array([ 0.        ,  0.84147098,  0.90929743,  0.14112001, -0.7568025 ])
```



---

Attachment

This depends on #5081.


---

Comment by mvngu created at 2009-07-30 01:42:31

With the patches at #5081 and #6506, and `6497-numpy-sin.patch` on this ticket, I got one doctest failure:

```
sage -t -long devel/sage-main/sage/modules/vector_double_dense.pyx
**********************************************************************
File "/scratch/mvngu/release/sage-4.1.1.alpha1/devel/sage-main/sage/modules/vector_double_dense.pyx", line 663:
    sage: v.stats_kurtosis()
Expected:
    -1.23
Got:
    doctest:106: SyntaxWarning: assertion is always true, perhaps remove parentheses?
    -1.23
**********************************************************************
1 items had failures:
   1 of   6 in __main__.example_29
***Test Failed*** 1 failures.
For whitespace errors, see the file /scratch/mvngu/release/sage-4.1.1.alpha1/tmp/.doctest_vector_double_dense.py
	 [2.5 s]
```



---

Comment by robertwb created at 2009-09-10 09:28:08

I am unable to reproduce the error above on 4.1.1, so I am re-instating the positive review. (Also, the error itself seems totally unrelated to this patch.)


---

Comment by mvngu created at 2009-09-10 09:31:54

Replying to [comment:3 robertwb]:
> I am unable to reproduce the error above on 4.1.1, so I am re-instating the positive review. (Also, the error itself seems totally unrelated to this patch.)
The above error is not due to the patch. Ticket #6825 contains steps to reproduce the errors.


---

Comment by mvngu created at 2009-09-10 09:41:40

Resolution: fixed
