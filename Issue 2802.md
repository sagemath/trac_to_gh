# Issue 2802: Sage 3.0.alpha1: sage/misc/inline_fortran.py doctest failure

Issue created by migration from https://trac.sagemath.org/ticket/2802

Original creator: mabshoff

Original creation time: 2008-04-05 00:10:01

Assignee: jkantor

I am seeing the following failure with 3.0.alpha1 on sage.math:

```
sage -t -long devel/sage/sage/misc/inline_fortran.py
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.0.alpha1/tmp/inline_fortran.py", line 28:
    sage: test_fortran(s)           # -- requires fortran
Expected nothing
Got:
    Found executable /scratch/mabshoff/release-cycle/sage-3.0.alpha1/local/bin/sage-g77_shared
    Found executable /scratch/mabshoff/release-cycle/sage-3.0.alpha1/local/bin/sage_fortran
    Found executable /usr/bin/ld
    Found executable /usr/bin/ar
    Found executable /usr/bin/ranlib
    <BLANKLINE>
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.0.alpha1/tmp/inline_fortran.py", line 31:
    sage: fib(n,int(10))            # -- requires fortran
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/release-cycle/sage-3.0.alpha1/local/lib/python2.5/doctest.py", line 1212, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[7]>", line 1, in <module>
        fib(n,int(Integer(10)))            # -- requires fortran###line 31:
    sage: fib(n,int(10))            # -- requires fortran
    NameError: name 'fib' is not defined
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.0.alpha1/tmp/inline_fortran.py", line 32:
    sage: n                         # -- requires fortran
Expected:
    array([  0.,   1.,   1.,   2.,   3.,   5.,   8.,  13.,  21.,  34.])
Got:
    array([ 0.,  1.,  2.,  3.,  4.,  5.,  6.,  7.,  8.,  9.])
**********************************************************************
```



---

Comment by jkantor created at 2008-04-08 06:43:40

This should fix the problem

http://sage.math.washington.edu/home/jkantor/patches/inline_fortran_fix.patch


---

Attachment

jkantor's patch


---

Comment by mabshoff created at 2008-04-08 10:36:05

The patch does not fix the issue for me. Is this a fix for a general inline Fortran issue?

Thoughts?


---

Comment by jkantor created at 2008-04-08 16:56:37

Ok, lets try this one (apply against the previous one)

http://sage.math.washington.edu/home/jkantor/patches/inline_fortran_2.patch


---

Comment by mabshoff created at 2008-04-08 17:54:19

Yep. Both patches together fix the issue. Positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2008-04-08 17:54:58

Resolution: fixed


---

Comment by mabshoff created at 2008-04-08 17:54:58

Merged in Sage 3.0.alpha3


---

Comment by mabshoff created at 2008-04-08 17:56:13

jkantor's second patch
