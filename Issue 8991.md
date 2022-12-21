# Issue 8991: Adjust developer walkthrough for two changes to mercurial queues syntax

Issue created by migration from Trac.

Original creator: rbeezer

Original creation time: 2010-05-19 00:09:26

Assignee: mvngu

CC:  alubovsky


```
hg qinit
hg -f qnew
```


are deprecated in newer versions of Mercurial (1.5) which some may be using (ie not using the version distributed with Sage).  This patch includes text to transition to the new state of the syntax without abandoning the old.


---

Attachment


---

Comment by alubovsky created at 2010-05-19 01:33:17

Changing status from new to needs_review.


---

Comment by alubovsky created at 2010-05-19 01:34:16

Changing status from needs_review to positive_review.


---

Comment by rbeezer created at 2010-05-19 04:00:50

alubovsky -

Thanks for the quick review.  Probably best to give the release manager (who makes the final decision about adding this into "official" Sage) some idea of what testing you did.  Such as something about building the developers manual without warnings, output looks fine, mq changes are accurately reported, etc.

Also, please put your real name into the "Reviewer" field and you'll get credit in the release tour and the Trac reports.  ;-)

cc me when you submit that patch of typos you are collecting!

Rob


---

Comment by alubovsky created at 2010-05-19 04:41:32

Patch output looks fine, no warnings building with
sage -docbuild developer html

patch applied just fine, (not sure what mq changes are accurately reported means.)


---

Comment by alubovsky created at 2010-05-19 04:53:39

I should add, i applied the patch to the latest version of sage-combinat repository, instead of sage-main, hopefully it makes no difference.


---

Comment by rbeezer created at 2010-05-19 05:32:34

Replying to [comment:4 alubovsky]:
> (not sure what mq changes are accurately reported means.)

I was just suggesting you might note the *content* of the changes was correct.  I don't have Mercurial 1.5 installed anywhere, so was working off documantation I could find online (which wsn't always helpful).

In this case, I think the sage-combinat repo is probably OK.


---

Comment by mvngu created at 2010-05-19 07:49:57

Resolution: fixed
