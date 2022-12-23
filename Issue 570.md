# Issue 570: rubik.solve doesn't work (sage -t --long groups/perm_gps/cubegroup.py  fails.)

Issue created by migration from https://trac.sagemath.org/ticket/570

Original creator: was

Original creation time: 2007-09-02 17:39:12

Assignee: somebody


```
sage -t --long groups/perm_gps/cubegroup.py                 **********************************************************************
File "cubegroup.py", line 979:
    sage: rubik.solve(state)  # long time; *computationally intensive* even for simple moves
Exception raised:
    Traceback (most recent call last):
      File "/home/was/s/local/lib/python2.5/doctest.py", line 1212, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_15[2]>", line 1, in <module>
        rubik.solve(state)  # long time; *computationally intensive* even for simple moves###line 979:
    sage: rubik.solve(state)  # long time; *computationally intensive* even for simple moves
      File "/home/was/s/local/lib/python2.5/site-packages/sage/groups/perm_gps/cubegroup.py", line 999, in solve
        soln = hom.PreImagesRepresentative(gap(str(g)))
      File "/home/was/s/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 674, in __call__
        return cls(self, x)
      File "/home/was/s/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 904, in __init__
        raise TypeError, x
    TypeError: Gap produced error output
    Syntax error: literal expected in /home/was/.sage//temp/ubuntu/13323//interfac\
    e//tmp line 1
    $sage14:={'right': [[19, 29, 32], [18, 0, 31], [17, 28, 30]], 'up': [[3, 5, 38\
    ], [2, 0, 36], [1, 4, 25]], 'back': [[48, 26, 27], [45, 0, 37], [43, 39, 40]],\
     'down': [[41, 42, 11], [44, 0, 21], [46, 47, 24]], 'front': [[9, 10, 8], [20,\
     0, 7], [22, 23, 6]], 'left': [[33, 34, 35], [12, 0, 13], [14, 15, 16]]};;
             ^

       executing Read("/home/was/.sage//temp/ubuntu/13323//interface//tmp");
**********************************************************************
1 items had failures:
   1 of   3 in __main__.example_15
***Test Failed*** 1 failures.
For whitespace errors, see the file .doctest_cubegroup.py
         [13.5 s]
```



---

Attachment


---

Comment by wdj created at 2007-09-06 01:53:25

Fixed the docstring and now all tests pass:


```
wdj@wooster:~/sagefiles/sage-2.8.3.rc3> ./sage -t --long "/home/wdj/sagefiles/sage-2.8.3.rc3/devel/sage-cube/sage/groups/perm_gps/cubegroup.py"
sage -t --long devel/sage-cube/sage/groups/perm_gps/cubegroup.py
         [31.1 s]

----------------------------------------------------------------------
All tests passed!
Total time for all tests: 31.2 seconds
```



---

Attachment


---

Comment by robertwb created at 2007-09-06 19:20:47

Added parse() method to take several kinds of inputs, re-enabled doctest for solve.


---

Comment by robertwb created at 2007-09-06 19:20:47

Resolution: fixed


---

Comment by robertwb created at 2007-09-06 19:20:47

Changing component from basic arithmetic to combinatorics.


---

Comment by robertwb created at 2007-09-06 20:21:48

Resolution changed from fixed to 


---

Comment by robertwb created at 2007-09-06 20:21:48

Changing status from closed to reopened.


---

Comment by was created at 2007-09-07 04:34:07

Resolution: fixed
