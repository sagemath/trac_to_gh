# Issue 8355: Fix hsv_to_rgb to take all 3 arguments

Issue created by migration from https://trac.sagemath.org/ticket/8355

Original creator: boothby

Original creation time: 2010-02-25 00:25:00

Assignee: was

CC:  kcrisman


```
sage: hue(.5,.5,.5)
Traceback (click to the left of this block for traceback)
...
TypeError: can't multiply sequence by non-int of type 'float'
```



---

Attachment


---

Comment by boothby created at 2010-04-02 00:31:57

Changing status from new to needs_review.


---

Comment by boothby created at 2010-04-02 00:35:02

Works for me.


---

Comment by boothby created at 2010-04-02 00:35:02

Changing status from needs_review to positive_review.


---

Comment by jhpalmieri created at 2010-04-15 22:16:11

This doesn't apply cleanly to me against 4.3.5.  Please rebase.


---

Comment by jhpalmieri created at 2010-04-15 22:16:11

Changing status from positive_review to needs_work.


---

Comment by jason created at 2010-05-26 15:41:40

Changing keywords from "" to "beginner".


---

Comment by ryan created at 2011-01-09 00:03:01

Changing status from needs_work to needs_review.


---

Comment by ryan created at 2011-01-09 00:03:01

I think this has been fixed already.  Works in sage-4.6.0


---

Comment by kcrisman created at 2011-01-09 02:56:16

Confirmed.  But should we add a patch that confirms this, as in the previous patch?  This is because we now use the Python version of this, afaict.


---

Comment by aly.deines created at 2011-01-09 22:41:44

I've created a patch that confirms

```
sage: hue(.5,.5,.5)
(0.25, 0.5, 0.5)
```

in the doctest of hue and applies to sage-4.6.1.rc1.


---

Comment by aly.deines created at 2011-01-09 22:42:23

hue doctest which applies to sage-4.6.1.rc1


---

Attachment

Looks good to me.


---

Comment by wjp created at 2011-01-09 23:15:11

Changing status from needs_review to positive_review.


---

Comment by kcrisman created at 2011-01-10 13:58:16

If these spellings of the author and reviewer aren't right, please correct them.


---

Comment by kcrisman created at 2011-01-11 17:42:37

Well, up to you guys.  It just seemed to me that since there wasn't anything left to patch, maybe the older ones weren't relevant - but you can give credit where you feel it's due!


---

Comment by jdemeyer created at 2011-01-17 20:52:41

Changing status from positive_review to needs_work.


---

Comment by jdemeyer created at 2011-01-17 20:52:41

Please add the *correct* ticket number to the commit message :-)


---

Comment by kcrisman created at 2011-01-17 21:00:26

Use only this patch


---

Attachment

This should fix this.  Apply only 8355-hue.2.2.patch


---

Comment by kcrisman created at 2011-01-17 21:01:16

Changing status from needs_work to needs_review.


---

Comment by kcrisman created at 2011-01-17 21:01:54

Changing status from needs_review to positive_review.


---

Comment by boothby created at 2011-01-17 21:17:21

I didn't have anything to do with the review of the patch going in... I think it's weird to get credit for this.


---

Comment by jdemeyer created at 2011-01-19 22:19:30

Resolution: fixed
