# Issue 6991: lattice polytope nfacets method broken for non-reflexive polytopes

Issue created by migration from https://trac.sagemath.org/ticket/6991

Original creator: mhampton

Original creation time: 2009-09-22 18:45:43

Assignee: mhampton

CC:  novoselt

In the nfacets method, for non-reflexive lattice polytopes this is computed from:

```
self._nfacets = len(self._facet_normals)
```

but self._facet_normals is a matrix, which does not have a len method.  So I think this should instead be

```
self._nfacets = self._facet_normals.nrows()
```


A doctest should also be added for this case.


---

Comment by novoselt created at 2009-09-22 19:46:19

This is actually fixed by this patch (which needs a review):

http://trac.sagemath.org/sage_trac/ticket/6778


---

Comment by mhampton created at 2009-09-22 20:51:21

OK, sorry about that.  I am working through your tickets and I should have looked more closely.  This ticket can be closed as a duplicate of 6778.

-Marshall


---

Comment by mhampton created at 2009-09-22 20:51:21

Changing priority from minor to trivial.


---

Comment by novoselt created at 2009-12-19 00:43:03

Resolution: duplicate
