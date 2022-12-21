# Issue 9647: instructive example for mip.pyx

Issue created by migration from Trac.

Original creator: schilly

Original creation time: 2010-07-30 17:06:42

Assignee: jason, jkantor

CC:  kcrisman ncohen

Add an example from sage-support to the head of mip.pyx [see here](http://groups.google.com/group/sage-support/browse_thread/thread/e5ebaf0f6f657ab2).


---

Comment by schilly created at 2010-07-30 17:19:37

Changing status from new to needs_review.


---

Comment by kcrisman created at 2010-07-30 19:13:23

I can't comment on the correctness, obviously, but if the formatting works out right, this is exactly the kind of thing I was envisioning.  Great documentation and explanation - I hope someone reviews it soon!


---

Comment by schilly created at 2010-07-30 21:48:15

I've added a general introduction chapter, but suddenly the `:meth:~`Class.method`` references to methods no longer work. I don't know why.


---

Comment by schilly created at 2010-07-30 21:48:15

Changing status from needs_review to needs_work.


---

Comment by schilly created at 2010-07-31 12:11:31

Changing status from needs_work to needs_review.


---

Comment by ncohen created at 2010-07-31 14:28:41

Hello !!! Everything seems nice, but could you please add in the example one or two inequalities ? All the constraints in this case are equalities, which is a bit unusual with LP... Anyway people would understand that it is indeed possible to write an equality with two inequalities, while the opposite is not true... :-)

Nathann


---

Comment by schilly created at 2010-07-31 14:29:48

w_3 >= 1 is an inequality, but it's probably not explicit enough... wait a sec.


---

Comment by schilly created at 2010-07-31 14:34:26

How about now? I've intentionally avoided to set the lower bound of w_3 to 1 and instead used an inequality just because of that. I think that's ok now.


---

Comment by ncohen created at 2010-07-31 14:42:57

Hmmm.. I don't want an inequality "on principle"... I thought it would be nice for the users to see among your system of equalities some inequality... When they look at this system of equations they can think "ok, my own system fits". If they only see equalities and don't read the full text, they may not notice it is possible... Well, it's up to you ! If you don't this it sound, just say so, your ticket already dserves a positive review :-)

Nathann


---

Attachment

ok, you are probably right.


---

Comment by ncohen created at 2010-07-31 14:57:08

Sorryyyyyy !! I know it feels a bit artificial.... With a bit of luck we should have a proper tutorial for LP in Sage soon anyway... Thank you for your paaaaaatch !!! :-)

Nathann


---

Comment by ncohen created at 2010-07-31 14:57:08

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-08-09 09:40:18

Resolution: fixed
