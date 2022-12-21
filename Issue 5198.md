# Issue 5198: apply_map skips zeroes in sparse vectors and matrices

Issue created by migration from Trac.

Original creator: cwitty

Original creation time: 2009-02-07 00:39:36

Assignee: was

Consider:

```
sage: vector(ZZ, range(3)).apply_map(lambda x: x+1)
(1, 2, 3)
sage: vector(ZZ, range(3), sparse=True).apply_map(lambda x: x+1)
(0, 2, 3)
```


and


```
sage: matrix(ZZ, range(3)).apply_map(lambda x: x+1)
[1 2 3]
sage: matrix(ZZ, range(3), sparse=True).apply_map(lambda x: x+1)
[0 2 3]
```




---

Attachment

The attached patch fixes the problem, and adds a sparse=True/False argument to apply_map that may be useful if you know that the result will have a different sparsity than the input.

I also fixed a bug along the way: apply_map didn't preserve subdivisions for sparse matrices.  Sorry, reviewer, whoever you are.


---

Comment by robertwb created at 2009-02-07 09:09:20

Ouch...that is a pretty bad bug. 

The patch fixes the above issues and works well for me (including the subdivisions fix).


---

Comment by mabshoff created at 2009-02-08 01:59:33

Resolution: fixed


---

Comment by mabshoff created at 2009-02-08 01:59:33

Merged in Sage 3.3.alpha6.

Cheers,

Michael
