# Issue 7452: Make it easier to diagnose build problems by allowing copy-paste

Issue created by migration from Trac.

Original creator: iandrus

Original creation time: 2009-11-13 17:27:07

Assignee: tbd

In case of build problems the message telling you what to do cannot be easily copied as one command to run.


---

Attachment

Make debugging instructions copy/pastable


---

Comment by iandrus created at 2009-11-13 17:29:10

Changing status from new to needs_review.


---

Comment by mvngu created at 2009-12-08 17:43:54

I couldn't successfully apply the patch `trac7452.patch` to Sage 4.3.alpha1. So I have attached the reviewer patch `trac_7452-rebased.patch` which is a rebase of iandrus' patch. This newer patch is based on Sage 4.3.alpha1 and contains some rewording, but the essential ideas are those of iandrus' so I kept his name on the newer patch. I'm OK with iandrus' original patch; only my rebased patch needs to be reviewed and applied. Essentially, anyone besides me are welcome to review `trac_7452-rebased.patch`.


---

Comment by iandrus created at 2009-12-08 21:19:17

If I am allowed to review the rebased patch, I give it a positive review.  The only nit that I have it is uses tabs, but there are other tabs in this file as well.


---

Comment by iandrus created at 2009-12-08 21:19:17

Changing status from needs_review to positive_review.


---

Attachment

based on Sage 4.3.alpha1


---

Comment by mvngu created at 2009-12-08 22:13:14

Replying to [comment:4 iandrus]:
> If I am allowed to review the rebased patch, I give it a positive review. 

Yes, I think you are allowed to review my rebased patch. Essentially, I'm happy with your original patch and I would give it a positive review. But I can't successfully apply your patch to Sage 4.3.alpha1 so I had to rebase your patch. What you are doing is reviewing the modification I made to your patch.





> The only nit that I have it is uses tabs, but there are other tabs in this file as well.

My apology about introducing the tabs. I have attached a new patch which shouldn't have any tabs in it. Only that newer patch needs reviewing.


---

Comment by mvngu created at 2009-12-08 22:13:14

Changing status from positive_review to needs_work.


---

Comment by mvngu created at 2009-12-08 22:13:20

Changing status from needs_work to needs_review.


---

Comment by mhansen created at 2009-12-09 08:28:21

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2009-12-14 15:53:44

Resolution: fixed
