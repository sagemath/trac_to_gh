# Issue 7678: shorten very long doctests in rings/arith.py

Issue created by migration from https://trac.sagemath.org/ticket/7678

Original creator: AlexGhitza

Original creation time: 2009-12-13 22:32:51

Assignee: tbd

On sage.math, before the patch:


```
sage -t -long "devel/sage-main/sage/rings/arith.py"         
         [162.6 s]
```


And after the patch:


```
sage -t -long "devel/sage-main/sage/rings/arith.py"         
         [50.2 s]
```


I'm putting the milestone as 4.3 only because this is almost certainly not going to break anything whatsoever.  Please change it to 4.3.1 if you think that's more appropriate.



---

Attachment


---

Comment by AlexGhitza created at 2009-12-13 22:34:31

Changing status from new to needs_review.


---

Comment by cremona created at 2009-12-14 15:00:45

I see what you did here: (1) you removed tha 'gap' algorithm from the test, presumably because it was slowest, and (2) instead of testing all i in each of the ranges 2 to 2255 and 2256 to  5000 you pick 500 random indices from those ranges and use those.

I don't think that strategy (2) is a good idea, since if this test ever fails it will be hard to find out exactly where (i.e. for which i).  The tests in our standard test suite should surely be deterministic.  What I did in a similar situation was to once and for all pick a random set of indices, and make the doctest test those indices only.  This does not prevent us from having a more strenuous test to do on occasion, I am only proposing limiting what happens every time the whole of Sage is tested.

For that reason (only) I have put this as "needs work", and will post to sage-devel so that others who commented on your observation can come and have their say.


---

Comment by cremona created at 2009-12-14 15:00:45

Changing status from needs_review to needs_work.


---

Comment by mhansen created at 2009-12-14 15:33:33

All of the random seeds are set at the beginning of the doctest, so it would be deterministic.


---

Comment by cremona created at 2009-12-14 16:49:44

In that case I'm changing this to "positive review".  Except that I can't, there is no such button below!


---

Comment by robertwb created at 2009-12-14 19:43:15

Changing status from needs_work to needs_review.


---

Comment by robertwb created at 2009-12-14 19:43:43

Can't give a positive review until it needs a review.


---

Comment by robertwb created at 2009-12-14 19:43:43

Changing status from needs_review to positive_review.


---

Comment by AlexGhitza created at 2009-12-14 21:25:06

Replying to [comment:2 cremona]:
> I see what you did here: (1) you removed tha 'gap' algorithm from the test, presumably because it was slowest

Actually, the splitting into range(2, 2255) including 'gap' and range(2256, 5000) excluding 'gap' was there before I touched this, and it was indeed because gap gets rather slow at doing this computation.  The only real change I made was to pick 500 integers in each range instead of testing the whole range.


---

Attachment


---

Comment by AlexGhitza created at 2009-12-14 21:33:35

I did something stupid in the first patch though, namely to remove `#long time` from two doctests that depend on previous long time computations.  This of course has no effect on `sage -t -long` but it breaks `sage -t`.  (Note to self: should test with and without -long in the future.)

Apply only the new patch, which fixes this.  And I guess this should technically be reviewed again.


---

Comment by AlexGhitza created at 2009-12-14 21:33:35

Changing status from positive_review to needs_work.


---

Comment by AlexGhitza created at 2009-12-14 21:33:46

Changing status from needs_work to needs_review.


---

Comment by cremona created at 2009-12-14 22:32:14

That's very odd since I definitely ran the test with and without -long.  I'll have to do it again.


---

Comment by cremona created at 2009-12-30 15:46:04

I did it again (eventually) and am now happy to give this a positive review.


---

Comment by cremona created at 2009-12-30 15:46:04

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2010-01-03 22:16:45

Resolution: fixed
