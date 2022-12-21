# Issue 9291: Constructing a root system / coxeter group from a pair of matrices

Issue created by migration from Trac.

Original creator: nthiery

Original creation time: 2010-06-21 08:22:28

Assignee: sage-combinat

CC:  sage-combinat

Constructing root systems / coxeter groups / ... from a pair of
matrices describing the coordinates of the roots and coroots in
their respective basis. Interface:


```
    sage: T = CartanType(roots_as_matrix, coroots_as_matrix)
    sage: T.root_space()
    sage: T.root_space().simple_roots()
    sage: T.coroot_space()
    sage: WeylGroup(T.root_space())
    sage: WeylGroup(T)
    sage: ReflectionGroup(T)
```


The root system code is designed to support such features. Attached: a
one page proof of feasibility (not following the above interface).



---

Attachment


---

Comment by chapoton created at 2012-12-17 17:07:50

Changing keywords from "" to "coxeter".
