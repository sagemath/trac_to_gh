# Issue 6778: [with patch, needs review] Fix nfacets for non-reflexive lattice polytopes

Issue created by migration from https://trac.sagemath.org/ticket/6778

Original creator: novoselt

Original creation time: 2009-08-19 23:01:45

Assignee: mhampton

There is a silly bug in computing the number of facets of non-reflexive lattice polytopes:

```
sage: p = LatticePolytope(matrix([1, 2]))
sage: p.nfacets()
Traceback (most recent call last):
...
TypeError: object of type 'sage.matrix.matrix_integer_dense.Matrix_integer_dense' has no len()
```

The attached one-line patch fixes it:

```
sage: p = LatticePolytope(matrix([1, 2]))
sage: p.nfacets()
2
```




---

Attachment

This is a simple patch for a simple bug.  I filed a duplicate ticket for this at #6991 which should be closed as well.


---

Comment by mvngu created at 2009-09-23 02:45:27

Resolution: fixed


---

Comment by mvngu created at 2009-09-27 09:45:44

There is no 4.1.2.alpha3. Sage 4.1.2.alpha3 was William Stein's release for working on making the notebook a standalone package.
