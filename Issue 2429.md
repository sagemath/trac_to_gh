# Issue 2429: block_matrix command should be consistent with the syntax of the matrix command

Issue created by migration from https://trac.sagemath.org/ticket/2429

Original creator: jason

Original creation time: 2008-03-08 20:23:19

Assignee: was

CC:  jdemeyer

The block matrix command uses a slightly different syntax than the matrix command, leading to confusion.  It would be great to fix it so that the following examples would work.  Assume that the xi variables below are matrices


```
sage: # Throw an error if the dimensions of the blocks don't match up correctly.
sage: # explicitly specify the positions of the blocks
sage: block_matrix([[x1,x2],[x3,x4]])
sage: block_matrix([[x1,x2,x3],[x4,x5,x6]])
sage: # dimensions are the numbers of block rows and columns
sage: block_matrix(2,3, [x1,x2,x3,x4,x5,x6])
sage: # coerce the matrix to a specific ring
sage: block_matrix(QQ,2,3,[x1,x2,x3,x4,x5,x6])
sage: # 1 and 0 should still be interpreted as the identity and zero matrices
sage: block_matrix([[x1,1],[1,x2]])
sage: # if only one dimension is given, assume the matrix is square
sage: block_matrix(QQ,2,[x1,x2,x3,x4])
sage: block_matrix(2,[x1,x2,x3,x4])
sage: # the following works now
sage: block_matrix([x1,x2,x3,x4])
```




---

Comment by jbmohler created at 2008-11-11 15:09:23

As commented in the original patch, the command 

```
sage:  block_matrix([x1,x2,x3,x4])
```

"works" where "works" means that it makes a 2x2 matrix of submatrices.  While that was what I expected when I used the command, it is quite ambiguous and I felt like I was on shaky ground while writing my own code on top of it.  I do not like the ambiguity of that.

Note that it is also inconsistent with the matrix command:

```
sage: matrix([1,2,3,4])
[1 2 3 4]
```

which makes a 1x4 matrix.

I'd say they should both make an 1xn matrix (or matrix of submatrices).  Indeed, I'd almost rather that the syntax with a simple list and no explicit dimensions be banned outright when we don't know the dimensions from some parent object due to ambiguity.  Seems to go along with "Explicit is better than implicit."


---

Comment by wjp created at 2011-01-12 01:48:23

There is now a patch at #4492 that handles this issue too.


---

Comment by wjp created at 2011-02-16 10:09:07

Since ticket #4492 has been merged, this can now be closed too. Jeroen, could you do so?


---

Comment by jdemeyer created at 2011-02-16 10:36:07

Resolution: duplicate
