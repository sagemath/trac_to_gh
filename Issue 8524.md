# Issue 8524: DisjointUnionEnumeratedSets should have a private __classcall__ method

Issue created by migration from https://trac.sagemath.org/ticket/8524

Original creator: hivert

Original creation time: 2010-03-13 14:53:53

Assignee: sage-combinat

CC:  sage-combinat

Keywords: DisjointUnionEnumeratedSets, inheritance

In order to be easily inherited from, `DisjointUnionEnumeratedSets` should have a private `__classcall__` method. Indeed most of the time, when inheriting from it, the family used in the union will be constructed in the `__init__` method of the subclass. Having `__classcall__` inherited force the user to have its own `__classcall__`.


---

Comment by hivert created at 2010-03-13 16:28:12

Changing assignee from sage-combinat to hivert.


---

Comment by hivert created at 2010-03-13 16:30:26

The patch should be ready for review. I've one question: There is a very long doc in the class but nothing in the `__init__` nor in the file itself. Any idea about what is best here ?

Florent


---

Comment by hivert created at 2010-03-13 16:30:26

Changing status from new to needs_review.


---

Comment by hivert created at 2010-03-20 09:43:12

Rebased against 4.3.4


---

Attachment

I just rebased this patch against 4.3.4. 
Nicolas: Please don't forget reviewing it. It is needed by #8519 which is close to be positive reviewed.


---

Attachment

Replaces the previous ones


---

Comment by nthiery created at 2010-04-16 21:21:36

Positive review (finally!)

Florent: I made a couple little changes in place (mostly doc). Please re-proofread, and set the positive review status.


---

Comment by hivert created at 2010-04-16 23:47:16

Your change are ok with me. Thanks for the review.


---

Comment by hivert created at 2010-04-16 23:47:16

Changing status from needs_review to positive_review.


---

Comment by jhpalmieri created at 2010-04-19 05:14:12

Merged "trac_8524-disjoint_union_classcall_private-fh.2.patch" into 4.4.alpha1.


---

Comment by jhpalmieri created at 2010-04-19 05:14:12

Resolution: fixed
