# Issue 3132: [PATCH] Add computation of multinomial coefficients

Issue created by migration from Trac.

Original creator: gebner

Original creation time: 2008-05-08 13:16:47

Assignee: somebody

CC:  sage-combinat

The attached code computes multinomial coefficients using products of binomial coefficients, which is reasonably fast even for large inputs.

(However, MMA is about 3-4x times faster on my machine.)


---

Attachment


---

Comment by cwitty created at 2008-05-10 20:08:14

Code looks good, but the doctest fails on a 32-bit platform (due to #3134).  Either the doctest needs to be changed to use smaller numbers, or #3134 needs to be fixed.


---

Attachment

fix doctest not to hit #3134


---

Comment by craigcitro created at 2008-06-20 04:23:16

Changing keywords from "" to "editor_cwitty".


---

Comment by cwitty created at 2008-06-20 07:25:11

Looks good.  Thanks for fixing the doctest, and sorry it took so long to re-review.

Apply only the second patch.


---

Comment by mabshoff created at 2008-06-23 06:43:04

Resolution: fixed


---

Comment by mabshoff created at 2008-06-23 06:43:04

Merged in Sage 3.0.4.alpha0

Gabriel,

please post hg patches and not diffs in the future, i.e. hg export instead of hg diff. I committed the patch in your name in this case.

Cheers,

Michael
