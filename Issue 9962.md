# Issue 9962: non-nef divisors can have sections, too

Issue created by migration from https://trac.sagemath.org/ticket/9963

Original creator: vbraun

Original creation time: 2010-09-21 20:51:14

Assignee: AlexGhitza

CC:  novoselt

`ToricDivisor_generic.sections()` has an incorrect shortcut if the divisor is not nef. The cohomology of the divisor is computed correctly:

```
sage: rays = [(1,0,0),(0,1,0),(0,0,1),(-2,0,-1),(-2,-1,0),(-3,-1,-1),(1,1,1),(-1,0,0)]
sage: cones = [[0,1,3],[0,1,6],[0,2,4],[0,2,6],[0,3,5],[0,4,5],[1,3,7],[1,6,7],[2,4,7],[2,6,7],[3,5,7],[4,5,7]]
sage: X = ToricVariety(Fan(rays=rays,cones=cones))
sage: D = X.divisor(2); D
V(z2)
sage: D.is_nef()
False
sage:  D.sections()
()
sage: D.cohomology(dim=True)
(1, 0, 0, 0)
```

Attached one-line patch fixes this issue and adds doctest.


---

Attachment

Initial patch


---

Comment by vbraun created at 2010-09-21 20:57:45

Changing status from new to needs_review.


---

Comment by novoselt created at 2010-09-22 00:00:07

Changing status from needs_review to positive_review.


---

Comment by novoselt created at 2010-09-22 00:00:07

Passes tests on 4.6.alpha1!


---

Comment by mpatel created at 2010-09-29 08:39:13

Resolution: fixed
