# Issue 8999: sage-4.4.2 test "groups/matrix_gps/matrix_group.py" fails on x86_64-Linux-nehalem-fc

Issue created by migration from https://trac.sagemath.org/ticket/8999

Original creator: mariah

Original creation time: 2010-05-20 13:10:10

Assignee: joyner


```
sage-4.4.2 built with gcc-4.5.0 on x86_64-Linux-nehalem-fc (Skynet/taurus) fails test:

taurus% ./sage -t  -long "devel/sage/sage/groups/matrix_gps/matrix_group.py"
sage -t -long "devel/sage/sage/groups/matrix_gps/matrix_group.py"
**********************************************************************
File "/home/mariah/sage/sage-4.4.2-x86_64-Linux-nehalem-fc/devel/sage/sage/groups/matrix_gps/matrix_group.py", line 626:
    sage: G.random_element()
Expected:
    [2 1 1 1]
    [1 0 2 1]
    [0 1 1 0]
    [1 0 0 1]
Got:
    [0 1 1 0]
    [1 2 2 2]
    [1 1 1 0]
    [2 0 1 2]
**********************************************************************
File "/home/mariah/sage/sage-4.4.2-x86_64-Linux-nehalem-fc/devel/sage/sage/groups/matrix_gps/matrix_group.py", line 637:
    sage: G.random_element()
Expected:
    [1 3]
    [0 3]
Got:
    [4 2]
    [1 0]
**********************************************************************
File "/home/mariah/sage/sage-4.4.2-x86_64-Linux-nehalem-fc/devel/sage/sage/groups/matrix_gps/matrix_group.py", line 640:
    sage: G.random_element()
Expected:
    [2 2]
    [1 0]
Got:
    [4 1]
    [0 2]
**********************************************************************
File "/home/mariah/sage/sage-4.4.2-x86_64-Linux-nehalem-fc/devel/sage/sage/groups/matrix_gps/matrix_group.py", line 643:
    sage: G.random_element()
Expected:
    [4 0]
    [1 4]
Got:
    [2 4]
    [2 3]
**********************************************************************
1 items had failures:
   4 of  10 in __main__.example_21
***Test Failed*** 4 failures.
For whitespace errors, see the file /home/mariah/.sage//tmp/.doctest_matrix_group.py
         [68.8 s]
 
----------------------------------------------------------------------
The following tests failed:


        sage -t -long "devel/sage/sage/groups/matrix_gps/matrix_group.py"
Total time for all tests: 68.8 seconds
taurus%

```



---

Comment by mariah created at 2010-05-20 19:06:58

Resolution: worksforme


---

Comment by mariah created at 2010-05-20 19:06:58


```
bug disappeared when I rebuilt sage.
```

