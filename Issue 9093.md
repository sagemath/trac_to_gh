# Issue 9093: is_square broken for constant polynomials

Issue created by migration from https://trac.sagemath.org/ticket/9093

Original creator: robertwb

Original creation time: 2010-05-30 08:37:36

Assignee: AlexGhitza


```
sage: R.<x> = QQ[]
sage: R(1).is_square()
False
```




---

Attachment


---

Comment by robertwb created at 2010-05-30 08:45:25

Changing status from new to needs_review.


---

Comment by robertwb created at 2010-05-30 09:28:54

Changing priority from major to critical.


---

Comment by cremona created at 2010-06-02 14:37:08

Changing status from needs_review to positive_review.


---

Comment by cremona created at 2010-06-02 14:37:08

Patch applied fine to 4.4.3.alpha0.  Code looks fine, and all tests in sage/rings/polynomial pass.

Note (needs another ticket?)   I do not think that this is correct:

```
sage: R.<x> = ZZ[]
sage: R(100).squarefree_decomposition()
100
```

But it works better now than it did before by a long way, so I will give this a positive review and suggest that another ticket is opened.


---

Comment by robertwb created at 2010-06-02 17:28:04

Thanks! As with factoring, we don't decompose the unit part. There should probably be at least a note about this.


---

Comment by cremona created at 2010-06-02 19:53:18

My point was that in ZZ[X], as opposed to QQ[X], 100 is *not* a unit factor so should be included in the squarefree factorization.  It would have to be done differently, of course (and Integers don't have a squarefree_decomposition method, presumably because over ZZ there is no known algorithm which avoids factoring).


---

Comment by was created at 2010-06-03 04:33:11

Resolution: fixed
