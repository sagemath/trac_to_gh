# Issue 8921: Extend cross product to 7d

Issue created by migration from Trac.

Original creator: bwonderly

Original creation time: 2010-05-07 18:39:09

Assignee: jason, was

CC:  jason rbeezer

The cross product is defined for 7D, this patch allows for that functionality.


---

Attachment


---

Comment by rbeezer created at 2010-05-07 18:48:22

Jason,

I need to double-check the tests this afternoon, Billy is getting some known failures.

I'll post here when full tests pass.

Rob


---

Comment by rbeezer created at 2010-05-08 03:08:08

Replying to [comment:1 rbeezer]:
> I'll post here when full tests pass.

This passed all tests on my machine, so I think it is ready for a review.

Rob


---

Comment by rbeezer created at 2010-05-08 03:08:08

Changing status from new to needs_review.


---

Comment by jason created at 2010-05-11 05:02:57

Changing status from needs_review to positive_review.


---

Comment by jason created at 2010-05-11 05:02:57

tests pass on affected file, the formula checks out with wikipedia, and the properties are illustrated with the doctests.

Positive review!  Very nice!  Thanks for your work, Billy!


---

Comment by mhansen created at 2010-06-07 07:10:27

Resolution: fixed
