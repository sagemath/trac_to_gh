# Issue 8632: .save ignores ymin etc.

Issue created by migration from https://trac.sagemath.org/ticket/8632

Original creator: damm

Original creation time: 2010-03-30 17:12:08

Assignee: was

CC:  kcrisman

a sage (4.3.3) notebook shows the correct picture of


```
plot(x^2-5,(x,0,5),ymin=0)
```



The save method ignores the ymin parameter:


```
plot(x^2-5,(x,0,5),ymin=0).save("/tmp/test.png")
```



---

Comment by novoselt created at 2010-11-19 03:55:47

See also #7981.


---

Comment by novoselt created at 2011-01-13 05:47:30

With the current patch at #7981 this problem is gone. The graph goes a bit below ymin=0, but it happens in both cases in the same way, so save does not ignore the parameter anymore.


---

Comment by novoselt created at 2011-01-13 05:47:30

Changing status from new to needs_review.


---

Comment by novoselt created at 2011-01-13 05:52:33

Easy review with #7981 applied ;-)


---

Comment by kcrisman created at 2011-01-13 15:00:28

Except we need a patch :-)  It could go in the TESTS section; it would need to use the usual temp directory for Sage.


---

Comment by kcrisman created at 2011-01-13 15:00:28

Changing status from needs_review to needs_work.


---

Comment by novoselt created at 2011-01-13 16:36:35

Could you please remind me what is the usual temp directory for Sage?

Also, what exactly should the test do? How do I verify that images from `show` and `save` are the same? It seems like a waste of time on tests if it is only checked that these commands don't raise an exception - they were working before as well, just not as they should.


---

Comment by kcrisman created at 2011-01-13 17:05:34

Replying to [comment:5 novoselt]:
> Could you please remind me what is the usual temp directory for Sage?
See line 1732 of your patch for #7981 ;-)  - `kwds.setdefault('filename', sage.misc.misc.tmp_filename() + '.png') `
> Also, what exactly should the test do? How do I verify that images from `show` and `save` are the same? It seems like a waste of time on tests if it is only checked that these commands don't raise an exception - they were working before as well, just not as they should.
Sadly, we can't do that yet.  (Matplotlib apparently does do this with Nose, but we don't have the capability yet.)   Partly this could be useful for the future day when we CAN check things like this...

But for now the point is that at least someone can visually verify that there is a different min than $y=-5$ if they care to look.  We want to document that we have done something about the particular one. 

Alternately, you could try to ask a release manager to close this as a duplicate of #7981.  Personally, I think it would be worth adding an example to the save documentation that one can choose to either put the commands in `.save(foo=bar)` or to pass it one from `plot(f,foo=bar)`; that could be useful for a complete newbie to the code to see, so that they don't have to follow code around.


---

Attachment


---

Comment by novoselt created at 2011-01-13 17:40:12

Changing status from needs_work to needs_review.


---

Comment by novoselt created at 2011-01-13 17:40:12

Thank you! How about this patch?


---

Comment by kcrisman created at 2011-01-13 17:59:14

I assume the patch depends on #7981, correct?


---

Comment by novoselt created at 2011-01-13 18:04:02

Yes!


---

Comment by kcrisman created at 2011-01-14 02:30:28

Changing status from needs_review to positive_review.


---

Comment by kcrisman created at 2011-01-14 02:30:28

Positive review.  

To buildbot: depends on #7981, apply trac_8632_save_ignores_options_from_plot.patch


---

Comment by kcrisman created at 2011-01-14 02:37:26

Scratch that.  Need to change the patch a bit so documentation looks ok - a missing colon.


---

Attachment

reviewer patch


---

Comment by kcrisman created at 2011-01-14 02:42:06

Okay, now all is well.  

to buildbot: depends on #7981, apply trac_8632_save_ignores_options_from_plot.patch and trac_8632-reviewer.patch


---

Comment by novoselt created at 2011-01-14 03:21:15

Thanks for the corrections, sorry for sloppiness!


---

Comment by kcrisman created at 2011-01-15 03:21:22

Just FYI - still applies fine on 4.6.2.alpha0.


---

Comment by jdemeyer created at 2011-01-19 01:42:58

Replying to [comment:14 kcrisman]:
> Just FYI - still applies fine on 4.6.2.alpha0.

Actually, it doesn't:

```
patching file sage/plot/plot.py
Hunk #1 FAILED at 2394.
1 out of 1 hunk FAILED -- saving rejects to file sage/plot/plot.py.rej
```



---

Comment by jdemeyer created at 2011-01-19 01:42:58

Changing status from positive_review to needs_work.


---

Comment by jdemeyer created at 2011-01-19 01:45:25

Changing status from needs_work to positive_review.


---

Comment by jdemeyer created at 2011-01-19 01:45:25

Sorry, I missed the dependency on #7981.


---

Comment by jdemeyer created at 2011-01-25 08:14:11

Resolution: fixed
