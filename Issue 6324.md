# Issue 6324: optional doctest failure -- sloane functions and gap database

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-06-16 14:54:36

Assignee: tbd


```
sage -t -long --optional devel/sage/sage/combinat/sloane_functions.py
**********************************************************************
File "/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/combinat/sloane_functions.py", line 354:
    sage: sloane.A000001._eval(51) #optional requires database_gap
Expected nothing
Got:
    1
**********************************************************************
1 items had failures:
   1 of   4 in __main__.example_13
***Test Failed*** 1 failures.
```



---

Comment by slabbe created at 2015-07-13 12:24:14

Changing status from new to needs_review.


---

Comment by slabbe created at 2015-07-13 12:24:14

On sage-6.8.beta8, this problem seems fixed:


```
$ sage -t --long --optional=sage,database_gap,internet src/sage/combinat/sloane_functions.py
Running doctests with ID 2015-07-13-14-22-17-a3f279bb.
Git branch: develop
Using --optional=database_gap,internet,sage
Doctesting 1 file.
sage -t --long --warn-long 2.3 src/sage/combinat/sloane_functions.py
    [1241 tests, 0.93 s]
----------------------------------------------------------------------
All tests passed!
----------------------------------------------------------------------
Total time for all tests: 1.2 seconds
    cpu time: 0.7 seconds
    cumulative wall time: 0.9 seconds

```



---

Comment by jdemeyer created at 2015-07-13 13:39:56

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2015-07-17 20:05:53

Resolution: fixed
