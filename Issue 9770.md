# Issue 9770: update instructions for reviewers, especially for new developers

Issue created by migration from https://trac.sagemath.org/ticket/9771

Original creator: niles

Original creation time: 2010-08-20 17:15:31

Assignee: mvngu

Keywords: doctests, reviewing

Update sections of developer guide about reviewing patches, as discussed at

http://ask.sagemath.org/question/31/should-i-_really_-review-trac-tickets




---

Comment by niles created at 2010-08-24 13:59:25

Changing status from new to needs_review.


---

Comment by niles created at 2010-08-24 13:59:25

forgot to set "needs review"!


---

Comment by mvngu created at 2010-09-07 06:21:24

Applies fine to Sage 4.5.3.rc0. No doctests were introduced, deleted, or modified so there is no need for me to run any doctests. I like the changes that cater to people new to Sage development. One could search for tickets needing review that have the priority "minor". We also have the priority "trivial". You could add that in with your current patch if you wish. Otherwise, you could open a new ticket to mention this point. In any case, I give the current patch a positive review.


---

Comment by mvngu created at 2010-09-07 06:21:24

Changing status from needs_review to positive_review.


---

Attachment

first version


---

Comment by niles created at 2010-09-07 19:56:54

Replying to [comment:2 mvngu]:

Thanks for the review!

> We also have the priority "trivial". 

I've added a mention of this now too.


---

Comment by mpatel created at 2010-09-15 11:38:16

Resolution: fixed
