# Issue 6753: sage-4.1.1 -- bug in integral_elements_in_box

Issue created by migration from https://trac.sagemath.org/ticket/6753

Original creator: was

Original creation time: 2009-08-15 16:35:53

Assignee: was


```

There are actually three real test failures on OS X 10.5 PPC.  They both probably involve rounding issues.  The second is harmless.  The first looks serious. 

sage -t -long "devel/sage/sage/rings/number_field/totallyreal_rel.py"
**********************************************************************
File "/Users/wstein/build/sage-4.1.1/devel/sage/sage/rings/number_field/totallyreal_rel.py", line 47:
    sage: sage.rings.number_field.totallyreal_rel.integral_elements_in_box(K, [[0,5],[0,5]])
Expected:
    [0, 5, -alpha + 2, -alpha + 3, 1, 2, 3, 4, alpha + 2, alpha + 3]
Got:
    [0, -alpha + 3, -alpha + 2, 4, 3, 2, 1, alpha + 3, alpha + 2]
**********************************************************************
1 items had failures:
   1 of   7 in __main__.example_1
***Test Failed*** 1 failures.
For whitespace errors, see the file /Users/wstein/build/sage-4.1.1/tmp/.doctest_totallyreal_rel.py
         [9.9 s]
```



---

Comment by was created at 2009-10-02 16:18:51

Resolution: fixed
