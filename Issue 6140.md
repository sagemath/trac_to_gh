# Issue 6140: Upgrade numpy to 1.3.0

Issue created by migration from https://trac.sagemath.org/ticket/6140

Original creator: jason

Original creation time: 2009-05-27 21:20:16

Assignee: mabshoff

Here is an spkg: http://sage.math.washington.edu/home/jason/numpy-1.3.0.spkg


---

Comment by jason created at 2009-05-27 21:21:36

This is related to #3391.  Also, #4205 can likely be closed once this ticket is closed.


---

Attachment

There are a few minor doctest updates that need to be done.  See above for a patch which addresses at least some of these.

When doing all doctests on 4.0.rc0, I get failures in:


```
The following tests failed:

        sage -t  devel/sage/sage/misc/banner.py # 5 doctests failed
        sage -t  devel/sage/sage/matrix/matrix_symbolic_dense.pyx # 3 doctests failed
        sage -t  devel/sage/sage/matrix/tests.py # 1 doctests failed
        sage -t  devel/sage/sage/rings/polynomial/polynomial_element.pyx # 2 doctests failed
        sage -t  devel/sage/sage/calculus/functions.py # 1 doctests failed
        sage -t  devel/sage/sage/plot/plot_field.py # 1 doctests failed
----------------------------------------------------------------------
```


However, some of these failures are from rc0, not from the numpy update.  The patch above corrects the failures that I know are from the numpy updated.  Please let me know if there are any other doctests that need to be updated in this ticket.


---

Comment by jkantor created at 2009-06-01 08:18:59

Everything looks good, except I get one trivial test failure. As you can see its just the difference between +0 and -0. It should probably be fixed. Positive review pending a fix of that. 

sage -t  "devel/sage-main/sage/rings/polynomial/polynomial_element.pyx"
**********************************************************************
File "/home/jkantor/sage-4.0/devel/sage-main/sage/rings/polynomial/polynomial_element.pyx", line 4059:
    sage: p.roots(ring=RR)
Expected:
    [(0.000000000000000, 1)]
Got:
    [(-0.000000000000000, 1)]
**********************************************************************


---

Comment by jason created at 2009-06-03 02:20:06

Also, #5090 might be able to be closed after this is merged.


---

Comment by craigcitro created at 2009-06-11 09:37:43

This looks good. I'm attaching a second patch for that one doctest failure. 

For the record, this spkg and the two patches have been merged in `4.0.2.alpha0` -- but I want to take a few minutes and carefully close all the appropriate tickets linked in the discussion above, so I'll officially close this tomorrow.

I'm going to be bold and say that my one-character patch doesn't really need a review; if someone wants to agree that it's fine, that wouldn't be bad.


---

Attachment

apply after spkg and patch above


---

Comment by craigcitro created at 2009-06-12 06:56:52

Resolution: fixed


---

Comment by craigcitro created at 2009-06-12 06:56:52

spkg and patches merged in 4.0.2.alpha0.
