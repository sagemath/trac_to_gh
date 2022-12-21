# Issue 5089: [with patch, needs review] add kernel method for sparse integer matrices

Issue created by migration from Trac.

Original creator: jhpalmieri

Original creation time: 2009-01-24 16:29:12

Assignee: was

Keywords: sparse integer matrix kernel


```
sage: M = matrix(ZZ, 2, 3, [1,2,3,4,5,6])
sage: M.kernel()
```

works fine, while

```
sage: M = matrix(ZZ, 2, 3, [1,2,3,4,5,6], sparse=True)
sage: M.kernel()
```

gives an error, `TypeError: Argument K (= Integer Ring) must be a field.`

The attached patch fixes this -- it adds a kernel method for sparse integer matrices, which just calls `self.dense_matrix().kernel(...)`.




---

Attachment


---

Comment by was created at 2009-01-24 16:40:47

looks good.


---

Comment by mabshoff created at 2009-01-24 18:08:22

Merged in Sage 3.3.alpha2

Cheers,

Michael


---

Comment by mabshoff created at 2009-01-24 18:08:22

Resolution: fixed
