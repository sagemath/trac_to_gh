# Issue 7111: timeout when doctesting partition refinement code

Issue created by migration from https://trac.sagemath.org/ticket/7111

Original creator: was

Original creation time: 2009-10-04 17:16:56

Assignee: tbd

On many platforms this times out:

```
sage -t -long "devel/sage/sage/groups/perm_gps/partn_ref/refinement_matrices.pyx"
*** *** Error: TIMED OUT! PROCESS KILLED! *** ***
*** *** Error: TIMED OUT! *** ***
A mysterious error (perhaps a memory error?) occurred, which may have crashed doctest.
         [1800.1 s]

The test that fails with a timeout is:

sage.groups.perm_gps.partn_ref.refinement_matrices.random_tests(180.0, 100, 200, 40)
```



---

Comment by was created at 2009-10-07 12:22:28

After deleting the line causing the timeout, I found a *bug* in partition refinement by testing on Centos32!

```
wstein@centos53-32:/tmp/wstein/farm/sage-4.1.2.rc1.alpha3$ ./sage -t devel/sage/sage/groups/perm_gps/partn_ref/refinement_matrices.pyx 
init.sage does not exist ... creating
sage -t  "devel/sage/sage/groups/perm_gps/partn_ref/refinement_matrices.pyx"
**********************************************************************
File "/tmp/wstein/farm/sage-4.1.2.rc1.alpha3/devel/sage/sage/groups/perm_gps/partn_ref/refinement_matrices.pyx", line 340:
    sage: sage.groups.perm_gps.partn_ref.refinement_matrices.random_tests()
Expected:
    All passed: ... random tests on ... matrices.
Got:
    M:
    [ 0 18  0  0  0  0  0  0  4  0  0  0  0  0  0  0  0  0  0  0  0  0  4]
    [ 0  0  0  0  0  0  0  0  0  0  0 15  0  0  0  0  0  0  6  0  0  0  0]
    [ 0  0  0  0  0  0  0  0  0  0  0  0  0  8  0  0  0  0 15  0  0 13  0]
    [ 0  0  0  0  7  0  0  0  0  0 16  0  0  0  0  0  0  0  0 22  0  0  0]
    [ 0  0 14  0  0  0  0  0  2  0  0  0  0  0  0  0 12  0  0  0  0  0  0]
    [ 0  0 13  0  0  0 21  0  0 16  0  0  0  0  0  0  0  0  0  0  0  0  0]
    [ 0  0  0 18  0  0  0  0  0  0  0  0  0  0  0  0  0 13  0  0  0  0  0]
    [ 0  0 18  0  3  0  0  0  0  0  0  0 22  0  0  0  0  0  0  0  0  0  0]
    [ 0 12  0  0  3  0  0  0  0  0  0  0  0  0  0  0  0 16  0  0  0  0  0]
    [ 0  0  2 13  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0 21]
    [ 0  0  0 21  0  0  0  0  0  0  0  1  0  0  9  0  0  0  0  0  0  0  0]
    [ 0 11  0  0  6  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0 21  0]
    [19  0  0  0  0  0  0  0  0  0  0  0  0  0  8  0 17  0  0  0  0  0  0]
    [ 0  1  0  0  0  0  0  0  0 14  0  0  0  0  0 16  0  0  0  0  0  0  0]
    [ 0  0  6  0  0  0  0  0  0  0  0  0  3  1  0  0  0  0  0  0  0  0  0]
    [ 0  0  0  0  0 11  0  0 15  0  0  0  0  0  0  0  0  0  0  0  0  0  0]
    [ 0  0  0  0  0  0  0  0  0  0  0  0  0  2 12  0  0 10  0  0  0  0  0]
    [ 0  0  0  0  0  0  0 19  0  0  0  0  0  0  0  0  0  0  0 17  0  0  0]
    [ 0  0  2 11  0  0  0  0  0  4  0  0  0  0  0  0  0  0  0  0  0  0  0]
    [ 0  0  0  0  0  0  6  0  0  0  0  0  0 10  0  0  0 10  0  0  0  0  0]
    perm:
    [15, 5, 17, 20, 10, 3, 21, 7, 11, 8, 4, 16, 19, 2, 9, 12, 6, 22, 14, 0, 13, 18, 1]
**********************************************************************
1 items had failures:
   1 of   4 in __main__.example_6
***Test Failed*** 1 failures.
For whitespace errors, see the file /scratch/wstein/sage//tmp/.doctest_refinement_matrices.py
         [8.0 s]
exit code: 1024
 
----------------------------------------------------------------------
The following tests failed:


        sage -t  "devel/sage/sage/groups/perm_gps/partn_ref/refinement_matrices.pyx"
Total time for all tests: 8.0 seconds
wstein@centos53-32:/tmp/wstein/farm/sage-4.1.2.rc1.alpha3$ 
```


So the timeout is probably really a hang caused by a serious bug.  (?)


---

Comment by rlm created at 2009-10-30 05:06:22

Changing status from new to needs_review.


---

Attachment

This was due to a bad assumption I made while I was writing `refinement_matrices`. This fixes that assumption, and the fact that this fixes at least the example above is shown here:


```
sage: M = matrix([[0, 18, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
   ....:  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 15, 0, 0, 0, 0, 0, 0, 6, 0, 0, 0, 0],
   ....:  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 0, 0, 0, 0, 15, 0, 0, 13, 0],
   ....:  [0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 16, 0, 0, 0, 0, 0, 0, 0, 0, 22, 0, 0, 0],
   ....:  [0, 0, 14, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 12, 0, 0, 0, 0, 0, 0],
   ....:  [0, 0, 13, 0, 0, 0, 21, 0, 0, 16, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
   ....:  [0, 0, 0, 18, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 13, 0, 0, 0, 0, 0],
   ....:  [0, 0, 18, 0, 3, 0, 0, 0, 0, 0, 0, 0, 22, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
   ....:  [0, 12, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 16, 0, 0, 0, 0, 0],
   ....:  [0, 0, 2, 13, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 21],
   ....:  [0, 0, 0, 21, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 9, 0, 0, 0, 0, 0, 0, 0, 0],
   ....:  [0, 11, 0, 0, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 21, 0],
   ....:  [19, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 0, 17, 0, 0, 0, 0, 0, 0],
   ....:  [0, 1, 0, 0, 0, 0, 0, 0, 0, 14, 0, 0, 0, 0, 0, 16, 0, 0, 0, 0, 0, 0, 0],
   ....:  [0, 0, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
   ....:  [0, 0, 0, 0, 0, 11, 0, 0, 15, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
   ....:  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 12, 0, 0, 10, 0, 0, 0, 0, 0],
   ....:  [0, 0, 0, 0, 0, 0, 0, 19, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 17, 0, 0, 0],
   ....:  [0, 0, 2, 11, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
   ....:  [0, 0, 0, 0, 0, 0, 6, 0, 0, 0, 0, 0, 0, 10, 0, 0, 0, 10, 0, 0, 0, 0, 0]])
sage: perm = [15, 5, 17, 20, 10, 3, 21, 7, 11, 8, 4, 16, 19, 2, 9, 12, 6, 22, 14, 0, 13, 18, 1]
sage: from sage.groups.perm_gps.partn_ref.refinement_matrices import MatrixStruct
sage: MS = MatrixStruct(M)
sage: MS.run()
sage: N = Matrix(M.base_ring(), M.nrows(), M.ncols())
sage: for j in range(M.ncols()):
   ....:     N.set_column(perm[j], M.column(j))
   ....: 
sage: NS = MatrixStruct(N)
sage: NS.run()
sage: M_relab = MS.canonical_relabeling()
sage: N_relab = NS.canonical_relabeling()
sage: M_C = matrix(M.base_ring(), M.nrows(), M.ncols())
sage: N_C = matrix(M.base_ring(), M.nrows(), M.ncols())
sage: for j in range(M.ncols()):
   ....:     M_C.set_column(M_relab[j], M.column(j))
   ....:     N_C.set_column(N_relab[j], N.column(j))
   ....: 
sage: M_C = matrix(M.base_ring(), sorted(M_C.rows()))
sage: N_C = matrix(M.base_ring(), sorted(N_C.rows()))
sage: M_C==N_C
True
```



---

Comment by mhansen created at 2009-11-05 03:31:14

Looks good.


---

Comment by mhansen created at 2009-11-05 03:31:14

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2009-11-05 03:31:25

Resolution: fixed
