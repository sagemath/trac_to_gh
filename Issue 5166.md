# Issue 5166: Sage 3.3.a4: sage/symbolic/function.pyx doctest failure on OSX

Issue created by migration from https://trac.sagemath.org/ticket/5166

Original creator: mabshoff

Original creation time: 2009-02-03 17:32:50

Assignee: burcin


```
sage -t -long "devel/sage/sage/symbolic/function.pyx"       
**********************************************************************
File "/Users/mabshoff/sage-3.3.alpha4/devel/sage/sage/symbolic/function.pyx", line 377:
    sage: f_list[8] # indices here depend on the GiNaC library
Expected:
    gamma
Got nothing
**********************************************************************
File "/Users/mabshoff/sage-3.3.alpha4/devel/sage/sage/symbolic/function.pyx", line 379:
    sage: f_list[12]
Expected:
    exp
Got:
    <function O at 0x8210170>
**********************************************************************
File "/Users/mabshoff/sage-3.3.alpha4/devel/sage/sage/symbolic/function.pyx", line 442:
    sage: f_list[14]
Expected:
    sin
Got:
    <function log at 0xa2a8b30>
**********************************************************************
File "/Users/mabshoff/sage-3.3.alpha4/devel/sage/sage/symbolic/function.pyx", line 444:
    sage: f_list[15]
Expected:
    cos
Got:
    sin
**********************************************************************
2 items had failures:
   2 of   6 in __main__.example_6
   2 of   6 in __main__.example_7
***Test Failed*** 4 failures.
```



---

Attachment


---

Comment by cwitty created at 2009-02-05 06:59:12

New doctests look good, and pass.  (Under Linux; I didn't try OSX.)

Positive review.


---

Comment by mabshoff created at 2009-02-05 10:37:48

Merged in Sage 3.3.alpha6. It also fixes the issue on OSX.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-05 10:37:48

Resolution: fixed
