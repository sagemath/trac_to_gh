# Issue 7020: Fix 32-bit versus 64-bit boolean_function issue in crypto

Issue created by migration from https://trac.sagemath.org/ticket/7020

Original creator: kcrisman

Original creation time: 2009-09-27 00:52:13

Assignee: tbd

See #6870 for some discussion.  A random test behaves differently in 32/64 cases:

```
sage -t -long devel/sage/sage/crypto/boolean_function.pyx
**********************************************************************
File "/scratch/mvngu/release/sage-4.1.2.alpha2/devel/sage-main/sage/crypto/boolean_function.pyx", line 1013:
    sage: B.nonlinearity()
Expected:
    217
Got:
    222
**********************************************************************
1 items had failures:
   1 of   6 in __main__.example_36
***Test Failed*** 1 failures.
For whitespace errors, see the file /home/mvngu/.sage//tmp/.doctest_boolean_function.py
	 [5.3 s]
```



---

Comment by kcrisman created at 2009-09-27 00:53:31

Either this patch or an identical one but with the other # (217 or 222) in the - line should apply and fix this.  Probably it should be renamed as well!


---

Comment by mvngu created at 2009-09-28 03:54:32

based on Sage 4.1.2.alpha4


---

Attachment


---

Comment by jsp created at 2009-09-28 09:45:54

Works for me on Fedora 11, 32 bit:



```
[jaap@paix sage-4.1.2.alpha4]$ ./sage -t  "devel/sage/sage/crypto/boolean_function.pyx"
sage -t  "devel/sage/sage/crypto/boolean_function.pyx"      
	 [8.9 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 8.9 seconds

```



---

Comment by mvngu created at 2009-09-29 11:37:12

Resolution: fixed
