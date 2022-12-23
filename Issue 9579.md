# Issue 9579: Raise an exception when arguments to add_constraint are not admissible

Issue created by migration from https://trac.sagemath.org/ticket/9579

Original creator: ncohen

Original creation time: 2010-07-23 02:37:16

Assignee: jason, jkantor

Because of the error reported on :

http://groups.google.com/group/sage-support/browse_thread/thread/b953192f3554337f

It may be good to save an user several hours of trouble because a wrong argument is silently accepted.

Done in this patch ! :-)

Nathann


---

Comment by ncohen created at 2010-07-23 02:38:28

Changing status from new to needs_review.


---

Comment by schilly created at 2010-07-23 09:00:44

I don't know if testing with RR is the best way to do this, but should work. What's missing is a test for max b/c you only tested for min.


---

Comment by schilly created at 2010-07-23 09:01:45

test both arguments, not only one of them


---

Attachment

Replying to [comment:2 schilly]:
> I don't know if testing with RR is the best way to do this, but should work. What's missing is a test for max b/c you only tested for min.

You do not begin to know how I *HATE* this RR... Is there any way to check whether a value is numerical without having to import RINGS ? :-D

Even a Python method is fine !!! The most esoteric thing that could be found there is a rational number !

Nathann


---

Attachment

I just updated my patch so that instead of ugly "try/except", a "if" is enough, thanks to Harald's suggestion. By the way, your patch still applies on top of mine, so if you are ok with these changes, let's say this ticket is positively reviewed :-)

Nathann


---

Comment by schilly created at 2010-07-23 09:19:55

there is still this hurdle to run all tests, i'll start them right now.


---

Comment by schilly created at 2010-07-23 10:17:51

Changing status from needs_review to positive_review.


---

Comment by schilly created at 2010-07-23 10:17:51

dear release manager, first merge trac_9579.patch and then trac_9579_review.patch


---

Comment by ddrake created at 2010-07-26 02:37:43

Replying to [comment:6 schilly]:
> dear release manager, first merge trac_9579.patch and then trac_9579_review.patch

Merged in 4.5.2.alpha1.


---

Comment by ddrake created at 2010-07-26 02:37:43

Resolution: fixed


---

Comment by ncohen created at 2010-08-06 02:06:08

My 'n' !! I hadn't noticed it !! Thank you :-)

Nathann
