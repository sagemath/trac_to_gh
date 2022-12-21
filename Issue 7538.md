# Issue 7538: equality of posets is broken !

Issue created by migration from Trac.

Original creator: hivert

Original creation time: 2009-11-26 21:34:36

Assignee: mhansen

CC:  sage-combinat nborie

Keywords: posets

It answer always true if two posets have the same size:

```
sage: p1 = Posets(2)[0]; p2 = Posets(2)[1]
sage: p1.cover_relations()
[]
sage: p2.cover_relations()
[This is the Trac macro *0, 1* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#0, 1-macro)
sage: p1 == p2
True
```



---

Attachment


---

Comment by hivert created at 2009-11-26 21:53:02

Changing status from new to needs_info.


---

Comment by hivert created at 2009-11-26 21:53:02

The fix posted here solve the problem of equality but raise a much more subtle one

```
sage: p1, p2 = Posets(2).list()
sage: p2 < p1
True
sage: [[p1.__cmp__(p2) for p1 in Posets(2)] for p2 in Posets(2)]
[[0, 1], [1, 0]]
sage: [[p2.__cmp__(p1) for p1 in Posets(2)] for p2 in Posets(2)]
[[0, 1], [-1, 0]]
sage: p2 < p1
False
```


I forward the discussion to sage-combinat-devel.


---

Comment by hivert created at 2009-11-28 14:38:04

Changing assignee from mhansen to hivert.


---

Comment by nborie created at 2010-02-23 22:14:06

Changing status from needs_info to needs_review.


---

Comment by saliola created at 2010-02-24 13:55:34

Changing status from needs_review to needs_work.


---

Comment by saliola created at 2010-02-24 13:55:34

Hello Nicolas. Since you are implementing `__eq__`, it is a good idea to also implement `__ne__`. (It is does not work the way you might think it should.)


---

Comment by nborie created at 2010-02-24 21:20:25

Mouhahaha Franco!!! You don't want me to sleep during these Sage Days 20 but I will win the commiting contest! Good review!


---

Comment by nborie created at 2010-02-24 21:20:25

Changing status from needs_work to needs_review.


---

Attachment

Looks good to me, passes all doctests.

Only the second patch should be applied.


---

Comment by novoselt created at 2010-04-15 23:51:25

Changing status from needs_review to positive_review.


---

Comment by jhpalmieri created at 2010-04-16 17:28:22

Resolution: fixed


---

Comment by jhpalmieri created at 2010-04-16 17:28:22

Merged "trac_7538_poset_equal_fix-nb.patch" into 4.4.alpha0.
