# Issue 2390: numerical noise in devel/sage-main/sage/structure/factorization.py

Issue created by migration from Trac.

Original creator: jsp

Original creation time: 2008-03-05 00:11:06

Assignee: cwitty



```
[jaap`@`paix sage-2.10.3.rc1]$ ./sage -t  devel/sage-main/sage/structure/factorization.py
sage -t  devel/sage-main/sage/structure/factorization.py    **********************************************************************
File ".doctest_factorization.py", line 479, in __main__.example_17
Failed example:
    F = factor(-Integer(2)*x**Integer(2) - Integer(1)); F###line 602:_sage_    >>> F = factor(-2*x^2 - 1); F
Expected:
    (-2.0) * (1.0*x^2 + 0.5) * (1.0*x^2 + 1.11022302463e-16*x + 0.5)  
Got:
    (-2.0) * (1.0*x^2 - 1.82173070032e-16*x + 0.5) * (1.0*x^2 + 0.5)
**********************************************************************
1 items had failures:
   1 of   3 in __main__.example_17
***Test Failed*** 1 failures.

A mysterious error (perphaps a memory error?) occurred, which may have crashed doctest.
         [2.7 s]
exit code: 256
 
----------------------------------------------------------------------
The following tests failed:


        sage -t  devel/sage-main/sage/structure/factorization.py
Total time for all tests: 2.7 seconds
[jaap`@`paix sage-2.10.3.rc1]$ 

```




---

Comment by mabshoff created at 2008-03-05 00:30:51

Changing assignee from cwitty to was.


---

Comment by mabshoff created at 2008-04-04 22:12:28

Resolution: fixed


---

Comment by mabshoff created at 2008-04-04 22:12:28

This has been fixed in Sage 2.10.3.final. I believe the patch was contributed by Gary Furnish, but my recollection might be a little hazy here.

Cheers,

Michael
