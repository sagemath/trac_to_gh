# Issue 8815: Misc elliptic curve typo fixes (easy review)

Issue created by migration from Trac.

Original creator: robertwb

Original creation time: 2010-04-29 04:24:30

Assignee: cremona

This code was clearly never actually tried out.


---

Comment by robertwb created at 2010-04-29 04:30:31

Changing status from new to needs_review.


---

Attachment

Note, `AttributeError` was the wrong thing to raise here, and got caught in odd places. The other logic was overly complicated, just let the TypeError get raised.


---

Comment by cremona created at 2010-04-29 08:53:00

Changing status from needs_review to needs_work.


---

Comment by cremona created at 2010-04-29 08:53:00

Patch applies to 4.4;  tests pass (I checked all sage/schemes/elliptic_curves).

In the first file patched, was there a reason for not changing the TypeError in lines 1093/4 to another ValueError?

In the second:  there are essentially identical blocks of code in lines 1052-1068 and 1360-1376.  But the typo (s to z) was only fixed in one place.  So the other needs fixing too.

In the "logic simplification" bit of the patch -- this is not correct now!  If z's parent is (say) QQ then after the patch, z will have been coerced into CC but C will be set to QQ.  So this now fails:

```
sage: E = EllipticCurve('14a1')
sage: L = E.period_lattice()
sage: L.coordinates(1)
```


Finally, your description is a little unkind!  I spent a long time trying this out -- though I do admit, of course, that I clearly did not test every line.  Perhaps we need to add some more doctests?


---

Comment by robertwb created at 2010-04-29 09:19:57

Sorry, my comment was not supposed to be derogatory about the code, it was supposed to be encouragement that the bug wasn't anything deep (but I can see how it was taken the wrong way). You're right about C--we need to set it if it's being used later. 

I typically raise a `TypeError` when I get something that's the wrong type (e.g. I expected a list, but got an integer, or something like that), and a `ValueError`when it's something about the value (e.g. it was supposed to be positive, or a prime). 

I'll fix the patch, including more doctests.


---

Attachment

No offence taken!  I'll review this again when ready.  #8820 wil take more work, so probably not today...


---

Comment by robertwb created at 2010-04-29 09:39:50

The file has some tabs in the docstring, so I'm hesitant to add any doctests until I've upgraded (there was a lot of detabification in the last release that bit me before). For the time being, I've reverted to the original logic, just fixing the typo. 

Thanks for looking at this barrage of tickets I've just posted!


---

Comment by cremona created at 2010-04-29 10:41:27

Changing status from needs_work to needs_review.


---

Comment by cremona created at 2010-04-29 10:41:27

Replying to [comment:5 robertwb]:
> The file has some tabs in the docstring, so I'm hesitant to add any doctests until I've upgraded (there was a lot of detabification in the last release that bit me before). For the time being, I've reverted to the original logic, just fixing the typo. 

I used to be one of the tab culprits but I have now properly configured emacs on all the machines I use not to use them!

> 
> Thanks for looking at this barrage of tickets I've just posted!

Well, I feel it's my duty to do so...

I am looking at the new patch now.


---

Comment by cremona created at 2010-04-29 10:51:57

Changing status from needs_review to positive_review.


---

Comment by cremona created at 2010-04-29 10:51:57

New patch fixes the issues I had with the first patch, applies fine to 4.4 and all tests in sage/schemes/elliptic_curves pass.

Positive review:  apply second patch only.


---

Comment by mvngu created at 2010-05-08 21:53:33

Resolution: fixed


---

Comment by mvngu created at 2010-05-08 21:53:33

Merged [8815-ec-fixes.2.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8815/8815-ec-fixes.2.patch).
