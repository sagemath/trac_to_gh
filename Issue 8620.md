# Issue 8620: Rogue minus sign in sage.modular.modsym.ambient.diamond_bracket_operator

Issue created by migration from https://trac.sagemath.org/ticket/8620

Original creator: davidloeffler

Original creation time: 2010-03-28 21:46:38

Assignee: craigcitro

Keywords: modular symbols

There is a minus sign in the code for diamond operators which shouldn't be there; what actually gets returned is the diamond operator times the star involution! In particular, ```< 1 >``` really ought to be the identity map. This patch corrects the error and adds a doctest to prove it. (This is needed for some code I wrote with Jared Weinstein at the 2010 Montreal conference, in which it's really vital to work with sign 0 symbols.)


---

Comment by davidloeffler created at 2010-03-28 21:53:14

patch against 4.3.4


---

Comment by davidloeffler created at 2010-03-28 22:02:20

Changing status from new to needs_review.


---

Attachment


---

Comment by was created at 2010-03-28 22:07:30

Changing status from needs_review to positive_review.


---

Comment by jhpalmieri created at 2010-04-16 18:53:30

Merged "trac_8620-diamond_operator_bug.patch" in 4.4.alpha0.


---

Comment by jhpalmieri created at 2010-04-16 18:53:30

Resolution: fixed
