# Issue 9933: Toric divisor class -> divisor lift should be integral

Issue created by migration from https://trac.sagemath.org/ticket/9934

Original creator: vbraun

Original creation time: 2010-09-17 14:00:03

Assignee: AlexGhitza

CC:  novoselt

An integral divisor class should lift to an integral divisor. But:

```
sage: rays = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, 0, 1), (2, -1, -1)]
sage: cones = [(0, 2, 3), (0, 2, 4), (0, 3, 4), (1, 2, 3), (1, 2, 4), (1, 3, 4)]
sage: X = ToricVariety(Fan(cones=cones, rays=rays))
sage: X.rational_class_group().gen(1).lift()
-1/2*V(z0) + 1/2*V(z1)
```

The attached patch fixes this and any doctest fallout.


---

Comment by vbraun created at 2010-09-17 14:02:55

Initial patch


---

Comment by vbraun created at 2010-09-17 14:03:39

Changing status from new to needs_review.


---

Attachment


---

Comment by novoselt created at 2010-09-17 19:08:22

Changing status from needs_review to positive_review.


---

Comment by novoselt created at 2010-09-17 19:08:22

Changing type from defect to enhancement.


---

Comment by novoselt created at 2010-09-17 19:08:22

Nice improvement! (Not quite defect ;-))

Tested on 4.5.3 with all the toric patches that got merged to 4.6.alpha1.


---

Comment by mpatel created at 2010-09-29 08:39:09

Resolution: fixed
