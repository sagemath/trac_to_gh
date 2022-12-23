# Issue 6779: [with patch, needs review] positive_integer_relations bug in lattice_polytope

Issue created by migration from https://trac.sagemath.org/ticket/6779

Original creator: novoselt

Original creation time: 2009-08-20 00:04:40

Assignee: mhampton

Since gcd(3/2, 9/5) used to be 3/10, it was used in lattice_polytope functions for rescaling to primitive integral vectors in the given rational direction. This is no longer true and leads to bugs:

```
sage: p = ReflexivePolytope(2, 1)
sage: lattice_polytope.positive_integer_relations(p.vertices())
Traceback (most recent call last):
...
TypeError: matrix has denominators so can't change to ZZ.
```

The patch adds a function integral_length and uses it instead of gcd:

```
sage: p = ReflexivePolytope(2, 1)
sage: lattice_polytope.positive_integer_relations(p.vertices())
[2 1 1]
```



---

Comment by mhampton created at 2009-10-24 15:44:28

Changing status from needs_review to positive_review.


---

Attachment

Looks good, positive review.


---

Comment by novoselt created at 2009-10-30 05:34:40

This patch is included as a part of a rebased patch for #6831.


---

Comment by mhansen created at 2009-11-02 04:35:39

Resolution: fixed


---

Comment by mhansen created at 2009-11-02 04:35:39

Fixed as part of #6831
