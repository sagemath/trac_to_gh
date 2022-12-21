# Issue 9750: Document that PARI no longer assumes more than GRH

Issue created by migration from Trac.

Original creator: jdemeyer

Original creation time: 2010-08-14 19:15:17

Assignee: mvngu

CC:  cremona

Earlier versions of PARI assumed something stronger than GRH (in Sage, this is referred to as GRH++).  As of PARI 2.4.0, "only" the GRH is assumed.


---

Comment by jdemeyer created at 2010-08-14 19:36:33

Changing status from new to needs_review.


---

Attachment

Looks good (apart from one Sphinx warning which my reviewer patch fixes).

Is there a good reference, say in the PARI reference manual, for the GRH assumptions?


---

Attachment

Apply after previous (and both depend on #9343)


---

Comment by cremona created at 2010-08-15 17:18:33

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2010-08-15 19:44:55

Replying to [comment:4 cremona]:
> Is there a good reference, say in the PARI reference manual, for the GRH assumptions?

Good point, I added a reference to the PARI/GP User's Guide in the bnfcertify() documentation.  The new patch replaces the previous two patches.  John, can you re-review?


---

Comment by jdemeyer created at 2010-08-15 19:44:55

Changing status from positive_review to needs_work.


---

Comment by jdemeyer created at 2010-08-15 19:45:05

Changing status from needs_work to needs_review.


---

Comment by cremona created at 2010-08-15 21:29:32

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2010-08-16 13:44:50

Includes previous 2 patches, adds reference to PARI's User's Guide


---

Comment by mpatel created at 2010-09-10 10:44:27

Resolution: fixed


---

Attachment
