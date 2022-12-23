# Issue 7055: Fix 32-bit versus 64-bit in pbori.pyx doctest

Issue created by migration from https://trac.sagemath.org/ticket/7055

Original creator: GeorgSWeber

Original creation time: 2009-09-28 18:59:24

Assignee: GeorgSWeber

With Sage-4.1.2.alpha4 on a 32-bit machine:

```
sage -t -long "devel/sage/sage/rings/polynomial/pbori.pyx"  
**********************************************************************
File "/Users/Shared/sage/sage-4.1.2.alpha4/devel/sage/sage/rings/polynomial/pbori.pyx", line 3940:
    sage: x.stable_hash()
Expected:
    173100285919
Got:
    -845955105
**********************************************************************
File "/Users/Shared/sage/sage-4.1.2.alpha4/devel/sage/sage/rings/polynomial/pbori.pyx", line 4849:
    sage: s.stable_hash()
Expected:
    173100285919
Got:
    -845955105
**********************************************************************
File "/Users/Shared/sage/sage-4.1.2.alpha4/devel/sage/sage/rings/polynomial/pbori.pyx", line 1976:
    sage: m.stable_hash()
Expected:
    173100285919
Got:
    -845955105
**********************************************************************
3 items had failures:
   1 of   4 in __main__.example_128
   1 of   5 in __main__.example_165
   1 of   5 in __main__.example_48
***Test Failed*** 3 failures.
For whitespace errors, see the file /Users/georgweber/.sage//tmp/.doctest_pbori.py
         [9.4 s]
exit code: 1024
 
----------------------------------------------------------------------
The following tests failed:


        sage -t -long "devel/sage/sage/rings/polynomial/pbori.pyx"
Total time for all tests: 9.4 seconds
```



---

Attachment

tested against 4.1.2.alpha4


---

Comment by jsp created at 2009-09-28 19:23:24

OK for me in Fedora 11, 32 bit



```
./sage -t  "devel/sage/sage/rings/polynomial/pbori.pyx"
sage -t  "devel/sage/sage/rings/polynomial/pbori.pyx"       
	 [15.3 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 15.3 seconds
[jaap@paix sage-4.1.2.alpha4]$ 

```



---

Comment by mvngu created at 2009-09-29 11:39:10

Resolution: fixed
