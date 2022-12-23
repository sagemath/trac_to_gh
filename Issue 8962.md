# Issue 8962: Change realfield latex representation to include precision/rounding information

Issue created by migration from https://trac.sagemath.org/ticket/8962

Original creator: jason

Original creation time: 2010-05-14 15:29:35

Assignee: AlexGhitza

CC:  robertwb

This patch changes the RealField latex representation to be RR_{precision}_^{0 or + or -}^ (for RNDZ, RNDU, or RNDD)


---

Attachment

Ready for review now.


---

Comment by jason created at 2010-05-14 15:52:19

Changing status from new to needs_review.


---

Comment by kcrisman created at 2010-05-26 18:09:33

Looks nice, including in the notebook with nice typesetting.  Maybe should have some documentation as to what this rep is?  Is it even standard notation (esp. the Z thing)?   This could be in the latex method or in the RealField? output.


---

Comment by kcrisman created at 2010-05-26 18:09:33

Changing status from needs_review to needs_work.


---

Comment by jason created at 2010-05-26 18:16:45

I completely made up the notation :).  I have no idea if it is standard, but it was nice to see in a numerical analysis class.
