# Issue 7322: SageNB: Upgrade jsMath to 3.6c

Issue created by migration from Trac.

Original creator: mpatel

Original creation time: 2009-10-27 17:22:19

Assignee: boothby

CC:  jhpalmieri

Version 3.6c of jsMath works around Firefox 3.5's single-origin policy for local files.  The policy can keep jsMath from loading its external components and functioning properly (cf. #6820).

Please see the [change log](http://www.math.union.edu/~dpvc/jsMath/changes.html) for other bug fixes. 


---

Attachment

Upgrade to jsMath 3.6c.


---

Comment by jhpalmieri created at 2009-10-29 20:09:59

I installed it and it seems to work well.  In particular, the patch at #6820 works with Firefox with this.

I skimmed the patch but I'm not going to proofread it carefully; I'm assuming that you just took the new source code for jsMath 3.6c and replaced the old source code for jsMath 3.6b.


---

Comment by jhpalmieri created at 2009-10-29 20:09:59

Changing status from new to needs_review.


---

Comment by jhpalmieri created at 2009-10-29 20:10:06

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2009-10-30 14:24:29

Replying to [comment:1 jhpalmieri]:
> I skimmed the patch but I'm not going to proofread it carefully; I'm assuming that you just took the new source code for jsMath 3.6c and replaced the old source code for jsMath 3.6b.

Indeed. That's all I did.


---

Comment by was created at 2009-11-11 22:14:59

Resolution: fixed


---

Comment by was created at 2009-11-11 22:14:59

merged into sagenb-0.4.2 (sage-4.2.1)
