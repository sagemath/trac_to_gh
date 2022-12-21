# Issue 6805: [with patch, needs review] Integrality check in LatticePolytope

Issue created by migration from Trac.

Original creator: novoselt

Original creation time: 2009-08-22 20:25:59

Assignee: mhampton

It is possible now to create a lattice polytope with rational vertices, which allows things to work, but causes wrong answers:

```
sage: m = matrix([1/2, 3/2])
sage: m
[1/2 3/2]
sage: LatticePolytope(m).points()
[0 1]
```

This patch adds an extra check/conversion to the constructor to prevent this:

```
sage: m = matrix([1/2, 3/2])
sage: m
[1/2 3/2]
sage: LatticePolytope(m).points()
Traceback (most recent call last):
...
ValueError: Points must be integral!
Given:
[1/2 3/2]
```



---

Attachment

Seems like a reasonable change, and tests out OK, so positive review.


---

Comment by mhampton created at 2009-10-29 18:42:50

Changing status from needs_review to positive_review.


---

Comment by novoselt created at 2009-10-30 05:35:17

This patch is included as a part of a rebased patch for #6831.


---

Comment by mhansen created at 2009-11-02 04:36:31

Resolution: fixed


---

Comment by mhansen created at 2009-11-02 04:36:31

Fixed in #6831.
