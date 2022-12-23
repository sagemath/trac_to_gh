# Issue 8584: implement latex'ing of Dirichlet characters

Issue created by migration from https://trac.sagemath.org/ticket/8584

Original creator: was

Original creation time: 2010-03-23 07:11:27

Assignee: craigcitro




---

Comment by was created at 2010-03-23 07:15:55

Changing status from new to needs_review.


---

Comment by craigcitro created at 2010-03-23 16:53:09

Changing status from needs_review to positive_review.


---

Attachment

Looks good, though I still agree with David Loeffler's complaint from another ticket that the print representation for Dirichlet characters isn't great. If we decide to change it, that means we need to remember to change this function, too (since it directly calls `values_on_gens`).


---

Comment by was created at 2010-04-02 13:47:17

> I still agree. .. print representation for Dirichlet characters isn't great. 

I don't agree.  I really like the print representation of Dirichlet characters.


---

Comment by davidloeffler created at 2010-04-05 13:03:46

I'm putting this back on "needs work" because it conflicts with #8133, and there seems to be a consensus on sage-nt that #8133 should go in.

David


---

Comment by davidloeffler created at 2010-04-05 13:03:46

Changing status from positive_review to needs_work.


---

Comment by davidloeffler created at 2010-04-05 13:18:51

replaces previous patch, apply after #8133


---

Attachment

Here's a new patch which produces output similar to the new `_repr_` but with the zeta's and mapsto arrows latexified.


---

Comment by davidloeffler created at 2010-04-05 13:19:39

Changing status from needs_work to needs_review.


---

Comment by wuthrich created at 2010-04-08 13:21:18

all tests pass on the new patch applied after #8133. Thanks.


---

Comment by wuthrich created at 2010-04-08 13:21:18

Changing status from needs_review to positive_review.


---

Comment by jhpalmieri created at 2010-04-15 23:40:24

Merged "trac_8584_new.patch" into 4.4.alpha0.


---

Comment by jhpalmieri created at 2010-04-15 23:40:24

Resolution: fixed
