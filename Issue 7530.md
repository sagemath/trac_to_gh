# Issue 7530: corrects simple Laurent-polynomial bug

Issue created by migration from Trac.

Original creator: fwclarke

Original creation time: 2009-11-25 13:14:29

Assignee: AlexGhitza

Keywords: Laurent Polynomial

It is not possible to form a polynomial ring over a Laurent polynomial ring.  This is because the function `is_integral_domain` for Laurent polynomial rings lacks the optional parameter `proof=True` (unlike every other instance of `is_integral_domain`).  The patch corrects this omission, which solves the problem.



---

Comment by fwclarke created at 2009-11-25 13:16:14

Changing status from new to needs_review.


---

Attachment


---

Comment by cremona created at 2009-12-17 18:01:24

Patch applies to 4.3.rc0, but:

    1. The function does not use the new parameter!
    2. No examples or doctests are given.

so -- needs work!


---

Comment by cremona created at 2009-12-17 18:01:24

Changing status from needs_review to needs_work.


---

Comment by fwclarke created at 2009-12-18 09:13:36

Changing status from needs_work to needs_review.


---

Comment by fwclarke created at 2009-12-18 09:13:36

Thanks, John.  

You're right; the `proof` parameter needs to be passed on to the base ring, which I've done in a replacement patch.  I've included an example verifying that the problem I had with constructing a polynomial ring over a Laurent polynomial ring is solved by the patch.

As it happens, the Laurent polynomial constructor currently restricts the base ring to be an integral domain.  Of course this isn't (mathematically) necessary, but the current code for taking negative powers of Laurent polynomial generators uses the fraction field of the base ring (producing some bizarre errors in the process).  I'll raise another ticket about this issue.


---

Attachment

replaces previous patch


---

Comment by cremona created at 2009-12-18 15:52:56

This looks better!  Second patch applies to 4.3.rc0, and tests pass.


---

Comment by cremona created at 2009-12-18 15:52:56

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2009-12-19 21:02:25

Resolution: fixed
