# Issue 2396: add support for matrix numpy-style indexing

Issue created by migration from https://trac.sagemath.org/ticket/2396

Original creator: dfdeshom

Original creation time: 2008-03-05 16:35:19

Assignee: was

Dan Christensen:

```
>  
>  Another nice feature of numpy is *assigning* using numpy-style indexing.
>  For example, to add a multiple of column j to column i, you can do
>  
>   A[:,i] += m*A[:,j]
>  
>  And you can zero out a region with
>  
>   A[2:4, 3:8] = 0    (broadcasting used here)
```


This is currently not implemented in sage.


---

Comment by dfdeshom created at 2008-03-20 17:56:39

Changing assignee from was to dfdeshom.


---

Comment by jason created at 2009-02-03 21:42:16

See #4972, which may fix this.


---

Comment by mvngu created at 2009-10-01 05:46:11

Resolution: duplicate


---

Comment by mvngu created at 2009-10-01 05:46:11

This has been fixed in Sage 4.1.2.alpha4:

```
[mvngu@sage sage-4.1.2.alpha4-sage.math]$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
**********************************************************************
*                                                                    *
* Warning: this is a prerelease version, and it may be unstable.     *
*                                                                    *
**********************************************************************
sage: M = MatrixSpace(QQ, 9)
sage: A = M.random_element(); A
| Sage Version 4.1.2.alpha4, Release Date: 2009-09-27                |
| Type notebook() for the GUI, and license() for information.        |
[   1   -2    2    2    0   -2  1/2    1  1/2]
[   0   -1    1    2    2    0    1   -1  1/2]
[ 1/2    2   -1    2  1/2    0   -1    2    1]
[   1   -1   -2    0 -1/2   -1   -1    0    2]
[   0   -1    0    0 -1/2   -2   -1    2    2]
[  -1    1   -1    0    2    0    1    0    1]
[   0    1    0    1 -1/2    1    1    2   -1]
[  -1 -1/2   -1    0   -1    0    0    2    0]
[   0 -1/2   -1    2    1    0    0    0    0]
sage: m = 3
sage: A[:,1] += m * A[:,4]
sage: A

[   1   -2    2    2    0   -2  1/2    1  1/2]
[   0    5    1    2    2    0    1   -1  1/2]
[ 1/2  7/2   -1    2  1/2    0   -1    2    1]
[   1 -5/2   -2    0 -1/2   -1   -1    0    2]
[   0 -5/2    0    0 -1/2   -2   -1    2    2]
[  -1    7   -1    0    2    0    1    0    1]
[   0 -1/2    0    1 -1/2    1    1    2   -1]
[  -1 -7/2   -1    0   -1    0    0    2    0]
[   0  5/2   -1    2    1    0    0    0    0]
sage: 
sage: A[2:4, 3:8] = 0
sage: A

[   1   -2    2    2    0   -2  1/2    1  1/2]
[   0    5    1    2    2    0    1   -1  1/2]
[ 1/2  7/2   -1    0    0    0    0    0    1]
[   1 -5/2   -2    0    0    0    0    0    2]
[   0 -5/2    0    0 -1/2   -2   -1    2    2]
[  -1    7   -1    0    2    0    1    0    1]
[   0 -1/2    0    1 -1/2    1    1    2   -1]
[  -1 -7/2   -1    0   -1    0    0    2    0]
[   0  5/2   -1    2    1    0    0    0    0]
sage: A[:,:] = 0
sage: A

[0 0 0 0 0 0 0 0 0]
[0 0 0 0 0 0 0 0 0]
[0 0 0 0 0 0 0 0 0]
[0 0 0 0 0 0 0 0 0]
[0 0 0 0 0 0 0 0 0]
[0 0 0 0 0 0 0 0 0]
[0 0 0 0 0 0 0 0 0]
[0 0 0 0 0 0 0 0 0]
[0 0 0 0 0 0 0 0 0]
```

Closing this as a duplicate of #4972.
