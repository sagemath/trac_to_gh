# Issue 7460: numerical noise on itanium (iras)

Issue created by migration from https://trac.sagemath.org/ticket/7460

Original creator: was

Original creation time: 2009-11-14 18:08:08

Assignee: was


```
wstein@iras:~/screen/iras/build/sage-4.2.1.rc0> ./sage -t -long "devel/sage/doc/en/numerical_sage/cvxopt.rst"
sage -t -long "devel/sage/doc/en/numerical_sage/cvxopt.rst"
**********************************************************************
File "/home/wstein/screen/iras/build/sage-4.2.1.rc0/devel/sage/doc/en/numerical_sage/cvxopt.rst", line 137:
    sage: print sol['x']
Expected:
       1.0000e+00
       1.0000e+00
Got:   
       1.0000e-00
       1.0000e+00
    <BLANKLINE>
**********************************************************************
1 items had failures:
   1 of  11 in __main__.example_2
***Test Failed*** 1 failures.
For whitespace errors, see the file /home/wstein/.sage//tmp/.doctest_cvxopt.py
         [3.8 s]
exit code: 1024

```



---

Comment by was created at 2009-11-14 18:11:55

With the attached patch:

```
wstein@iras:~/screen/iras/build/sage-4.2.1.rc0> ./sage -t -long "devel/sage/doc/en/numerical_sage/cvxopt.rst"
sage -t -long "devel/sage/doc/en/numerical_sage/cvxopt.rst" 
         [3.7 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 3.7 seconds
```



---

Attachment


---

Comment by was created at 2009-11-14 18:13:33

Changing status from new to needs_review.


---

Comment by mhansen created at 2009-11-15 14:13:57

Looks good to me.


---

Comment by mhansen created at 2009-11-15 14:13:57

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2009-11-17 05:55:04

Resolution: fixed
