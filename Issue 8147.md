# Issue 8147: Add mercurial queues information to Developer Walkthrough

Issue created by migration from Trac.

Original creator: rbeezer

Original creation time: 2010-02-02 03:05:26

Assignee: mvngu

CC:  mvngu rossk jpalmieri leif

This is a follow-on to #8108 expanding on basic use of Mercurial queues for Sage development.


---

Attachment


---

Comment by rbeezer created at 2010-02-02 06:29:29

Apply #8108 prior to applying this patch.


---

Comment by rbeezer created at 2010-02-02 06:29:29

Changing status from new to needs_review.


---

Attachment

apply on top of previous


---

Comment by mvngu created at 2010-02-02 20:25:29

The attachment [trac_8147_developer_doc_mq.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8147/trac_8147_developer_doc_mq.patch) is a valuable addition to the Developers' Guide. It's what many people have been asking for months now. I'm happy with the content. Obviously, there are not enough patches on this ticket, so I have attached a reviewer patch :-)  Only the attachment [trac_8147-reviewer.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8147/trac_8147-reviewer.patch) needs review.


---

Comment by rbeezer created at 2010-02-03 06:39:50

Changing status from needs_review to positive_review.


---

Comment by rbeezer created at 2010-02-03 06:39:50

Replying to [comment:4 mvngu]:
>
Thanks, Minh - those are some good additions, and I've learned a couple more fine-points.  And, as always, thanks for cleaning up my grammar. ;-)

The reviewer patch looks good to me, thankfully I had a guide to show me how to apply it.  I think I'm allowed to give such a thing a review, and if so, it's a positive review.

So it sounds like this is ready to go, and I'll mark it "positive review" - change it back if I missed something procedurally.

That was a nice collaboration - thanks for prodding me into action.

Rob


---

Comment by mvngu created at 2010-02-03 07:14:21

Merged in this order:

 1. [trac_8147_developer_doc_mq.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8147/trac_8147_developer_doc_mq.patch)
 1. [trac_8147-reviewer.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8147/trac_8147-reviewer.patch)


---

Comment by mvngu created at 2010-02-03 07:14:21

Resolution: fixed
