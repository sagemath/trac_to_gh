# Issue 8108: Expand the Sage Developer Guide for newcomers

Issue created by migration from Trac.

Original creator: rbeezer

Original creation time: 2010-01-28 05:46:50

Assignee: mvngu

CC:  mvngu leif

Newcomers to Sage development could use more comprehensive guidance on getting started.

A rough draft of possible new content is attached to this ticket.


---

Attachment


---

Comment by mvngu created at 2010-01-30 23:16:10

based on Sage 4.3.2.alpha0


---

Attachment

I have attached a patch that includes information from [how-to-develop.txt](http://trac.sagemath.org/sage_trac/attachment/ticket/8108/how-to-develop.txt). I also added more stuff, which means I can no longer review Rob's work. What's missing is a section on patch management using Mercurial queue. That could be for a separate ticket if necessary.


---

Comment by mvngu created at 2010-01-30 23:22:58

Changing status from new to needs_review.


---

Comment by leif created at 2010-01-31 21:39:59

Thanks (also for disclosing Gauss' e-mail address).


---

Comment by rossk created at 2010-02-01 15:49:41

Changing status from needs_review to positive_review.


---

Comment by rossk created at 2010-02-01 15:49:41

This will save newbie developers (and reviewers) hours of work (includes me! :-) For what its worth, Ive read it and it has answered a dozen questions. Thanks. We should remember that any other info can be included over time. Given this stuff is so valuable IMHO and Ive already tried much of what Ive read (but now it makes sense ;-) Im going to give this a positive review, if I may, even if you guys want to finesse it before including it. AGAIN THANKS!


---

Comment by jhpalmieri created at 2010-02-01 18:18:45

Here's a little patch to fix a few typos.


---

Comment by jhpalmieri created at 2010-02-01 18:19:04

apply on top of other patch


---

Attachment

John - thanks for the fixes (and the once-over).

John's fixes look good to me.  Minh handled the formatting (and lots more), so hopefully this will pass for a review of John's changes.  ;-)

Rob


---

Comment by rbeezer created at 2010-02-02 03:08:42

Ross,

Thanks for the enthusiastic review!  I've included you as a cc on #8147 that will expand the material on Mercurial queues at the end.

Rob

Replying to [comment:4 rossk]:
> This will save newbie developers (and reviewers) hours of work (includes me! :-) For what its worth, Ive read it and it has answered a dozen questions. Thanks. We should remember that any other info can be included over time. Given this stuff is so valuable IMHO and Ive already tried much of what Ive read (but now it makes sense ;-) Im going to give this a positive review, if I may, even if you guys want to finesse it before including it. AGAIN THANKS!


---

Comment by mvngu created at 2010-02-02 04:23:31

Resolution: fixed


---

Comment by mvngu created at 2010-02-02 04:23:31

Merged in this order:

 1. [trac_8108-beginner-guide.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8108/trac_8108-beginner-guide.patch)
 1. [trac_8108-typos.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8108/trac_8108-typos.patch)


---

Comment by rossk created at 2010-02-02 10:14:07

Replying to [comment:7 rbeezer]:
> Ross,
> 
> Thanks for the enthusiastic review!  I've included you as a cc on #8147 that will expand the material on Mercurial queues at the end.
> 
> Rob
> 
No probs Rob :-)


---

Comment by pdehaye created at 2011-05-31 15:25:51

Thanks to all for this and subsequent patches. It's a great improvement from what was there before. I know because I sweat hard a long time ago, which put me off from more sage development for a while. I just tried my hand at it again and it now makes _much_ more sense.


---

Comment by rbeezer created at 2011-06-01 06:31:08

Replying to [comment:10 pdehaye]:
> Thanks to all for this and subsequent patches.

pdehaye - thanks for the feedback.  I'm sitting on a pile of further suggestions for refinements, which I should whip into shape soon.

Rob
