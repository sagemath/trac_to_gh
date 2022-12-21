# Issue 9588: Extend is_prime_power to negative exponents

Issue created by migration from Trac.

Original creator: arminstraub

Original creation time: 2010-07-23 14:55:18

Assignee: AlexGhitza

Keywords: is_prime_power

Currently, is_prime_power only works on integers.  The attached simple patch will allow rational numbers as input as illustrated below.


```
sage: is_prime_power(1/2197)
True
sage: is_prime_power(1/100)
False
sage: is_prime_power(2/5)
False
```


This is also the behavior of Mathematica's PrimePowerQ function.


---

Attachment


---

Comment by arminstraub created at 2010-07-23 15:10:58

Changing status from new to needs_review.


---

Comment by cwitty created at 2010-07-24 20:52:04

Changing status from needs_review to needs_work.


---

Comment by cwitty created at 2010-07-24 20:52:04

Doesn't apply to sage-4.5.2.alpha0.  Could you update your patch?

By the way, you should look at the latest guidelines at http://groups.google.com/group/sage-release/browse_thread/thread/456f14fd92ee61a5 about commit messages and patch names.


---

Comment by arminstraub created at 2010-07-24 21:57:33

Changing status from needs_work to needs_review.


---

Comment by arminstraub created at 2010-07-24 22:00:42

Replying to [comment:2 cwitty]:

Thanks for the pointers.  Please let me know if I missed something else from the guidelines (it's my first patch).

> Doesn't apply to sage-4.5.2.alpha0.  Could you update your patch?

I downloaded the most recent available sage (4.5) and made a new patch.  Does this solve the issue?  If not, what can I do?


---

Comment by cwitty created at 2010-07-24 22:21:00

Unfortunately, your patch conflicts with the patch from #9206, which was newly added to sage-4.5.2.alpha0.  You could download and build that release (read sage-release http://groups.google.com/group/sage-release/browse_thread/thread/cc0b1929f66e0658?hl=en for a pointer to the source); or you could apply the patch from #9206 to your copy of Sage, and then redo your patch on top of that.

Sorry you're having such a difficult time with your first patch -- but you have to expect the occasional patch conflict when you work in the fast-changing field of testing for prime powers :)
(Just joking... the previous change to that code was in February 2009, so you're quite unlucky to have hit a time when somebody else was working on the same function.)


---

Comment by cwitty created at 2010-07-24 22:21:00

Changing status from needs_review to needs_work.


---

Comment by arminstraub created at 2010-07-24 23:47:06

apply only this one -- depends on #9206


---

Comment by arminstraub created at 2010-07-24 23:48:13

Changing status from needs_work to needs_review.


---

Attachment


---

Comment by arminstraub created at 2010-07-24 23:56:03

Replying to [comment:5 cwitty]:

Ok, thanks for the humorous explanation :)  I applied William's patch first, and adapted my patch---hopefully it works now!

I did two things of which I'm not quite sure if that was the proper way: (1) when uploading the new patch I replaced the old one, and (2) I just removed the "needs rebase" work issue in the hope that I addressed it.  Let me know if either of those is considered bad practice.


---

Comment by cwitty created at 2010-07-25 00:31:05

Changing status from needs_review to positive_review.


---

Comment by cwitty created at 2010-07-25 00:31:05

Code looks reasonable, doctests pass.  Positive review.

Armin, thanks for sticking with this!  To answer your questions:

(1) Opinions differ :) Sometimes it's nice to preserve the history of the patch, but it's also nice to make it easier for reviewers and the release manager by not having a whole sea of patches that they have to wade through to figure out which to apply.  In your case -- a simple rebase, where nobody will probably ever care about previous versions of the patch -- I'd say yes, replacing the old one is fine.

(2) Yes, if you think you've addressed the work issue you should remove it.

Release manager: apply only the second patch.


---

Comment by ddrake created at 2010-07-26 02:24:43

Resolution: fixed


---

Comment by ddrake created at 2010-07-26 02:24:43

9588_is_prime_power.patch merged in 4.5.2.alpha0. I did hand-edit the patch a tiny bit: with your patch, the documentation says "an integer rational number", and I changed it to "an integer or rational number".
