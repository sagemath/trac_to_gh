# Issue 7157: [with patch, needs review] neighbors_out/in instead of predecessor/successor in DiGraph

Issue created by migration from Trac.

Original creator: ncohen

Original creation time: 2009-10-08 16:31:05

Assignee: rlm

CC:  jason rlm nthiery

As the title says, and following the discussion on Sage-devel :
http://groups.google.com/group/sage-devel/browse_thread/thread/bfeb9b1828a04350/10681dbb1f189b2f


---

Comment by ncohen created at 2009-10-08 16:32:18

On my side, it passes -testall without any (related) failure.


---

Comment by ncohen created at 2009-10-08 16:32:18

Changing status from new to needs_review.


---

Comment by rlm created at 2009-10-08 16:34:26

You shouldn't just remove the successor/predecessor terminology. A lot of people (e.g. Chris Godsil) might have to do a lot of work to change all their personal scripts etc. to reflect this change. This patch breaks backwards compatibility.


---

Comment by rlm created at 2009-10-08 16:34:26

Changing status from needs_review to needs_work.


---

Comment by ncohen created at 2009-10-08 16:37:28

Should I just add aliases and let the old functions exist ? Should we keep two copies of the same functions ?


---

Comment by rlm created at 2009-10-08 16:39:06

Replying to [comment:3 ncohen]:
> Should I just add aliases and let the old functions exist ? Should we keep two copies of the same functions ?

I think aliases would be okay, but people have mentioned before that aliases are bad. Please bring this up on the sage-devel thread, and do what the consensus is there.


---

Comment by ncohen created at 2009-10-09 12:17:15

Changing status from needs_work to needs_review.


---

Comment by ncohen created at 2009-10-09 12:17:15

Should be better now :-)

The new functions are defined, old functions are marked "Deprecated".


---

Comment by hivert created at 2009-11-22 19:05:46

Hi there,

Just a short remark: If you wan't to shorten the patch: see #7515.


---

Comment by ncohen created at 2009-11-22 19:10:58

Thank you very much !!! :-)


---

Comment by ncohen created at 2009-11-24 15:57:46

Updated !


---

Attachment

Replying to [comment:8 ncohen]:
> Updated !

It was decided on sage-devel only to put the version and not the date in the message of deprecation aliases. I just uploaded a patch witch does that. Please review. Aside from that

You have a Positive review on trac_7157.patch. You can change the status as soon as you had an eye on my trivial review patch. 

Cheers,

Florent

By the way a review on #7515 is welcome ;-)


---

Comment by ncohen created at 2009-11-30 11:11:16

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2009-12-01 04:37:12

Resolution: fixed


---

Attachment

I've added a new trac_7157_review.patch patch with two function calls that were missed.


---

Comment by ncohen created at 2009-12-01 05:48:51

Thank you ! :-)
