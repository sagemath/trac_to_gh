# Issue 8813: symbolic expression -- doctest failure in sage-4.4.1.alpha0

Issue created by migration from https://trac.sagemath.org/ticket/8813

Original creator: was

Original creation time: 2010-04-29 00:33:47

Assignee: burcin


```
**********************************************************************
File "/mnt/usb1/scratch/wstein/build/release/4.4.1/sage-4.4.1.alpha1/devel/sage/sage/symbolic/expression.pyx", line 1284:
    sage: (-t0)._is_negative()
Expected:
    False
Got:
    True
**********************************************************************
1 items had failures:
   1 of   6 in __main__.example_40
***Test Failed*** 1 failures.
For whitespace errors, see the file /scratch/wstein/sage//tmp/.doctest_expression.py
         [34.8 s]

-----------------------------------------------
```



---

Comment by burcin created at 2010-04-29 03:28:27

This is fixed by the patch at #8565.


---

Comment by was created at 2010-04-29 04:19:25

Resolution: duplicate
