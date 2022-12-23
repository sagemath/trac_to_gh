# Issue 4573: Permutation not callable, but PermutationGroupElement is.

Issue created by migration from https://trac.sagemath.org/ticket/4573

Original creator: saliola

Original creation time: 2008-11-20 22:15:08

Assignee: saliola

CC:  sage-combinat


```
sage: p = PermutationGroupElement([2, 1, 4, 5, 3])
sage: p(1)
2
sage: q = Permutation([2, 1, 4, 5, 3])
sage: q(1)
...
TypeError: 'Permutation_class' object is not callable
```


This causes me some confusion.


---

Attachment

(against 3.2.rc2)


---

Comment by mhansen created at 2008-11-21 14:47:06

Looks good.


---

Comment by mabshoff created at 2008-11-21 20:23:17

Merged in Sage 3.2.1.alpha0


---

Comment by mabshoff created at 2008-11-21 20:23:17

Resolution: fixed
