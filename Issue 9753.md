# Issue 9753: Simplify NumberFieldIdeal.gens_reduced()

Issue created by migration from https://trac.sagemath.org/ticket/9753

Original creator: jdemeyer

Original creation time: 2010-08-15 19:56:54

Assignee: davidloeffler

The function NumberFieldIdeal.gens_reduced() can be simplified quite a bit without essentially changing its functionality.


---

Comment by jdemeyer created at 2010-08-15 20:07:54

Changing status from new to needs_work.


---

Comment by jdemeyer created at 2010-08-15 20:07:54

I will wait to fix the doctests until after #9343 and #9400.


---

Comment by jdemeyer created at 2010-09-13 07:45:48

Changing status from needs_work to needs_review.


---

Attachment

Adds function gens_two(), rewrites gens_reduced() and fixes doctests


---

Comment by jdemeyer created at 2010-09-16 16:59:37

Changing type from defect to enhancement.


---

Comment by jdemeyer created at 2010-09-16 16:59:37

Changing keywords from "" to "number field ideal gens_two idealtwoelt".


---

Comment by davidloeffler created at 2010-09-23 10:58:22

Looks fine to me, and all tests pass on my machine.


---

Comment by davidloeffler created at 2010-09-23 10:58:22

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-09-28 09:34:37

Could someone update the patch commit string with a more descriptive first line (still including the ticket number) and restore the positive review?


---

Comment by mpatel created at 2010-09-28 09:34:37

Changing status from positive_review to needs_work.


---

Attachment

New version with better commit string


---

Comment by davidloeffler created at 2010-09-28 09:42:22

Changing status from needs_work to positive_review.


---

Comment by davidloeffler created at 2010-09-28 09:42:22

Done.


---

Comment by mpatel created at 2010-09-28 10:55:54

Resolution: fixed
