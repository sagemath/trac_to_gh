# Issue 9809: Heisenbug in RationalPolyhedralCone.facets

Issue created by migration from Trac.

Original creator: vbraun

Original creation time: 2010-08-26 21:12:05

Assignee: mhampton

CC:  novoselt

The `faces` method of a cone in a fan manages to screw up subsequent `facet` output:

```
sage: cone = toric_varieties.dP8().fan().generating_cone(0)
sage: cone
2-d cone of Rational polyhedral fan in 2-d lattice N
sage: cone.facets()
(1-d cone of Rational polyhedral fan in 2-d lattice N, 1-d cone of Rational polyhedral fan in 2-d lattice N)
sage: cone.faces()
((0-d cone of Rational polyhedral fan in 2-d lattice N,), (1-d cone of Rational polyhedral fan in 2-d lattice N, 1-d cone of Rational polyhedral fan in 2-d lattice N), (2-d cone of Rational polyhedral fan in 2-d lattice N,))
sage: cone.facets()
(2-d cone of Rational polyhedral fan in 2-d lattice N,)
```

This is on vanilla Sage 4.5.2 without any patches applied. Andrey, I think its somewhere in your code so you'll probably find it faster than I can.


---

Attachment


---

Comment by novoselt created at 2010-08-26 21:33:22

Changing status from new to needs_review.


---

Comment by novoselt created at 2010-08-26 21:33:22

Should be 2 instead of 1... Thanks for catching!


---

Comment by vbraun created at 2010-08-26 21:52:05

Fixes it!


---

Comment by vbraun created at 2010-08-26 21:52:05

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-09-15 09:57:07

Resolution: fixed
