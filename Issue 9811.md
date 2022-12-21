# Issue 9811: Sorting bug in fan subdivision

Issue created by migration from Trac.

Original creator: novoselt

Original creation time: 2010-08-26 22:23:58

Assignee: mhampton

CC:  vbraun


```
sage: C = Cone([(1,0,0), (0,1,0), (1,0,1), (0,1,1)])
sage: F = Fan([C]).make_simplicial()
sage: [cone.ambient_ray_indices() for cone in F]
[(1, 3, 0), (1, 2, 0)]
```

While the output is mathematically correct, ambient ray indices are supposed to be sorted and violating this condition can lead to errors later. The attached patch adds extra sorting in the proper place. This means that polytopes constructed during subdivision can no longer be cached because of the potentially wrong vertex order, which is OK.


---

Attachment


---

Comment by novoselt created at 2010-08-26 22:28:09

Changing status from new to needs_review.


---

Comment by vbraun created at 2010-08-28 00:17:40

good catch!


---

Comment by vbraun created at 2010-08-28 00:17:40

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-09-15 09:57:23

Resolution: fixed
