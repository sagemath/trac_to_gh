# Issue 4091: Sage 3.1.2.rc1: matrix_real_double_dense.py doctest failure

Issue created by migration from https://trac.sagemath.org/ticket/4091

Original creator: mabshoff

Original creation time: 2008-09-09 18:45:48

Assignee: mabshoff


```

****************************************** 
File "/home/john/sage-3.1.2.rc1/tmp/matrix_real_double_dense.py", line 493: 
    sage: b = e * v 
Exception raised: 
    Traceback (most recent call last): 
      File "/home/john/sage-3.1.2.rc1/local/lib/python2.5/doctest.py", 
line 1228, in __run 
        compileflags, 1) in test.globs 
      File "<doctest __main__.example_8[8]>", line 1, in <module> 
        b = e * v###line 493: 
    sage: b = e * v 
      File "element.pyx", line 1384, in 
sage.structure.element.RingElement.__mul__ 
(sage/structure/element.c:9357) 
      File "coerce.pyx", line 662, in 
sage.structure.coerce.CoercionModel_cache_maps.bin_op 
(sage/structure/coerce.c:6364) 
    TypeError: unsupported operand parent(s) for '*': 'Complex Double 
Field' and 'Vector space of degree 3 and dimension 1 over Real Double 
Field 
    User basis matrix: 
    [0.440242867236 0.567868371314 0.695493875393]' 
********************************************************************** 
File "/home/john/sage-3.1.2.rc1/tmp/matrix_real_double_dense.py", line 494: 
    sage: diff = a.change_ring(CDF) - b 
Exception raised: 
    Traceback (most recent call last): 
      File "/home/john/sage-3.1.2.rc1/local/lib/python2.5/doctest.py", 
line 1228, in __run 
        compileflags, 1) in test.globs 
      File "<doctest __main__.example_8[9]>", line 1, in <module> 
        diff = a.change_ring(CDF) - b###line 494: 
    sage: diff = a.change_ring(CDF) - b 
    NameError: name 'b' is not defined 
********************************************************************** 
File "/home/john/sage-3.1.2.rc1/tmp/matrix_real_double_dense.py", line 495: 
    sage: abs(abs(diff)) < 1e-10 
Exception raised: 
    Traceback (most recent call last): 
      File "/home/john/sage-3.1.2.rc1/local/lib/python2.5/doctest.py", 
line 1228, in __run 
        compileflags, 1) in test.globs 
      File "<doctest __main__.example_8[10]>", line 1, in <module> 
        abs(abs(diff)) < RealNumber('1e-10')###line 495: 
    sage: abs(abs(diff)) < 1e-10 
    TypeError: bad operand type for abs(): 'function' 
**********************************************************************
```



---

Comment by jason created at 2008-09-10 02:41:23

I wonder if that first bug has anything to do with #3058, which gives problems when dealing with things with custom bases.


---

Comment by jason created at 2008-09-10 02:45:24

Never mind, it's probably just something to do with the new coercion stuff, just like it says.


---

Comment by craigcitro created at 2008-09-11 08:24:11

Changing assignee from mabshoff to craigcitro.


---

Comment by craigcitro created at 2008-09-11 08:24:11

Changing status from new to assigned.


---

Comment by craigcitro created at 2008-09-11 08:24:11

Actually, it wasn't coercion at all -- it was just as issue with linear algebra over inexact fields. Patch is attached. The issue had always been there, but it just became an issue since #3885 was fixed.

I'm just running a testall, I'll check out any errors in the morning.


---

Attachment


---

Comment by jason created at 2008-09-11 09:49:16

The patch fixes the errors in matrix/*.py[x] for me (ubuntu 8.04 32-bit).  In looking at the code, it seems okay.  However, something should be noted in the documentation that check only works if the ring is exact.


---

Comment by craigcitro created at 2008-09-11 10:21:09

Indeed, I should have added more documentation about this. I've added some documentation, and posted a second patch.


---

Attachment

I am happy with the second patch. Any followup should be dealt with via a new ticket since this one is holding up 3.1.2.rc2 :)

Cheers,

Michael


---

Comment by mabshoff created at 2008-09-12 23:29:31

Resolution: fixed


---

Comment by mabshoff created at 2008-09-12 23:29:31

Merged in Sage 3.1.2.rc2


---

Comment by mabshoff created at 2008-09-13 00:21:15

This patch fixes a couple noise issues
