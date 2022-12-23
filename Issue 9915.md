# Issue 9915: Change Shafarevich-Tate in BSD.py (also fixes doctests)

Issue created by migration from https://trac.sagemath.org/ticket/9916

Original creator: leif

Original creation time: 2010-09-16 09:41:21

Assignee: leif

CC:  cremona kcrisman mpatel wuthrich

Due to #9330, some doctests have to be adapted (and also the documentation).

I've *not* changed the name in the in the references' titles of course.


---

Comment by leif created at 2010-09-16 09:46:18

Apply to Sage library. Based on (not yet released) Sage 4.6.alpha1.


---

Comment by leif created at 2010-09-16 09:46:49

Changing status from new to needs_review.


---

Attachment

Patch is up.


---

Comment by mpatel created at 2010-09-16 21:49:12

Changing priority from major to blocker.


---

Comment by mpatel created at 2010-09-16 22:53:51

I can still merge this into 4.6.alpha1, while I wait for a response to a build error at #4000.


---

Comment by mpatel created at 2010-09-16 23:50:05

Are the stack size warnings expected here:

```python
sage -t -long  devel/sage/sage/schemes/elliptic_curves/ell_rational_field.py
  ***   Warning: new stack size = 1003360 (0.957 Mbytes).
  ***   Warning: new stack size = 1003360 (0.957 Mbytes).
**********************************************************************
File "/mnt/usb1/scratch/mpatel/tmp/sage-4.6.alpha1/devel/sage-main/sage/schemes/elliptic_curves/ell_rational_field.py", line 4805:
    sage: S
Expected:
    Shafarevich-Tate group for the Elliptic Curve defined by y^2 + y = x^3 - x over Rational Field
Got:
    Tate-Shafarevich group for the Elliptic Curve defined by y^2 + y = x^3 - x over Rational Field
```

?


---

Comment by leif created at 2010-09-17 00:48:33

Ooops, some kind of "recursive" doctest failure? I must have tested just those files that _previously_ failed.

I can upload a second patch for that, too, which in addition fixes one occurrence (documentation only) in `.../elliptic_curves/padic_lseries.py` as well.

Just let me know if you already fixed that elsewhere.

(I've seen those stack warnings before, but only when a doctest fails IIRC.)


---

Comment by mpatel created at 2010-09-17 00:51:00

By the way, the unofficial, trial 4.6.alpha1 is in `/home/release/sage-4.6.alpha1` on the Sage cluster.


---

Comment by mpatel created at 2010-09-17 00:53:42

Replying to [comment:7 leif]:
> I can upload a second patch for that, too, which in addition fixes one occurrence (documentation only) in `.../elliptic_curves/padic_lseries.py` as well.

Could you add the patch?  I haven't fixed this elsewhere.  Thanks for opening this ticket.


---

Comment by leif created at 2010-09-17 00:56:49

Replying to [comment:8 mpatel]:
> By the way, the unofficial, trial 4.6.alpha1 is in `/home/release/sage-4.6.alpha1` on the Sage cluster.

? What do you think mine came from? ;-) Or did you mean the *absent reviewers*?

(Cron ignores "README_first"...)

So I'll upload a second patch in a few seconds.


---

Attachment

Apply to Sage library. Based on (not yet released) Sage 4.6.alpha1.


---

Comment by leif created at 2010-09-17 01:14:01

Second patch is up; now passes _all_ doctests in `sage/schemes/elliptic_curves` (for me).

(Apply both.)


---

Comment by mpatel created at 2010-09-17 03:27:15

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-09-17 03:28:34

Resolution: fixed


---

Comment by wuthrich created at 2010-09-17 17:31:47

Apologies for my bad work on #9330 which caused all this to happen. Thanks for fixing it.

-- Chris.


---

Comment by leif created at 2010-09-17 18:49:16

Replying to [comment:16 wuthrich]:
> Apologies for my bad work on #9330 which caused all this to happen. Thanks for fixing it.

Never mind. If only all doctest failures (or bugs) were that trivial to fix...

I just cc'ed all of you to get this reviewed as quick as possible, not to blame anyone.


---

Comment by kcrisman created at 2010-09-17 19:28:41

Replying to [comment:17 leif]:
> Replying to [comment:16 wuthrich]:
> > Apologies for my bad work on #9330 which caused all this to happen. Thanks for fixing it.
> 
> Never mind. If only all doctest failures (or bugs) were that trivial to fix...

Hey, I reviewed that patch, and it was merged!  So there are at least three to blame :)

I wonder why it didn't cause any failures for me...  Anyway, thanks for looking into this so quickly.


---

Comment by mpatel created at 2010-09-17 23:02:11

For what it's worth: I was aware of the doctest errors here and that at #9924, when I merged their "parent" tickets into a trial 4.6.alpha1.  Were it not for the more serious build errors caused by #9733 and #4000, I would have announced this as alpha1 on sage-release with links to new tickets for known problems.
