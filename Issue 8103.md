# Issue 8103: Published worksheets aren't inert

Issue created by migration from Trac.

Original creator: mpatel

Original creation time: 2010-01-28 03:54:24

Assignee: was

CC:  timdumol was

It's possible to modify published worksheets, by appending worksheet commands to their URLs.


---

Comment by mpatel created at 2010-01-28 04:04:11

Disable published worksheet commands other than 'alive'.  sagenb repo.


---

Comment by mpatel created at 2010-01-28 04:04:57

Changing status from new to needs_review.


---

Attachment

I've attached a patch for testing and review.


---

Comment by mpatel created at 2010-01-28 04:08:23

If/when we fix this, I can include the patch in SageNB 0.7.1 at #8051.


---

Comment by was created at 2010-01-28 05:51:33

Changing status from needs_review to positive_review.


---

Attachment

Less draconian restrictions.  Replaces previous.


---

Comment by mpatel created at 2010-01-28 07:10:15

Changing status from positive_review to needs_work.


---

Comment by mpatel created at 2010-01-28 07:10:24

Changing status from needs_work to needs_review.


---

Attachment

Closer to the truth.  Replaces previous.


---

Comment by mpatel created at 2010-01-28 07:26:04

I apologize for the sloppy patches.  I _should_ have looked at my patch for #6855 (not posted), which implements similar restrictions.


---

Comment by was created at 2010-01-29 03:53:46

This looks good.

It's a little annoying since the comment right above the code you added refers to the code *after* the code you added. If one reads that comment after your patch, it could be confusing.


---

Comment by was created at 2010-01-29 03:53:46

Changing status from needs_review to positive_review.


---

Comment by was created at 2010-01-29 04:03:18

I just tested this and it doesn't work anyways.


---

Comment by was created at 2010-01-29 04:03:18

Changing status from positive_review to needs_work.


---

Comment by was created at 2010-01-29 04:09:19

Actually it is fine.  I just had trouble because I had mis-applied your patch.


---

Comment by was created at 2010-01-29 04:09:19

Changing status from needs_work to needs_review.


---

Comment by was created at 2010-01-29 04:09:28

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-01-30 05:24:18

Resolution: fixed
