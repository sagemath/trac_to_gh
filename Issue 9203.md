# Issue 9203: plot ellipses

Issue created by migration from https://trac.sagemath.org/ticket/9203

Original creator: vdelecroix

Original creation time: 2010-06-10 13:43:14

Assignee: vdelecroix

CC:  kcrisman jason

Keywords: plot, geometry, ellipse

Adding a primitive for plot ellipses that wraps the existing patch of matplotlib.

This is approximately the same stuff as the patch #9076 for plotting arcs (of circle and ellipse).


---

Comment by vdelecroix created at 2010-06-10 13:45:58

Changing status from new to needs_review.


---

Comment by kcrisman created at 2010-06-14 13:30:16

Changing status from needs_review to needs_work.


---

Comment by kcrisman created at 2010-06-14 13:30:16

This looks nice overall too, but again some things needed for best results.

* Class def examples for reference guide

* 'circle' still shows up a few times
 
* This `_repr_` method is better than the arc one!

* plot3d should open ticket or test `NotImplementedError`

* I like that options are given explicitly in arc(), as well as test of `NotImplementedError`

I'll try to work through the details of the `get_min_max_data` and test thoroughly on this and #9076 as soon as these things are addressed, because in general they're both good wraps and add much-needed functionality.  Good work!


---

Comment by vdelecroix created at 2010-06-14 16:32:16

Thank you for this careful review

> * Class def examples for reference guide

Done, if you mean examples in the docstring of the class Ellipse

> * 'circle' still shows up a few times

No more (I hope)

> * plot3d should open ticket or test `NotImplementedError`

I will. But as I really do not like the one it is implemented for circle for many different reasons I don't know how general should be the corresponding ticket...

> * I like that options are given explicitly in arc(), as well as test of `NotImplementedError`

Now there is. And I add a link from the sage.plot.plot

> I'll try to work through the details of the `get_min_max_data` and test thoroughly on this and #9076 as soon as these things are addressed, because in general they're both good wraps and add much-needed functionality.

The get_min_max_data for ellipse is just obtained by computing corresponding critical points. This is not the good way for arc but I will make an effort for it (as it is not too much complicate).


---

Comment by vdelecroix created at 2010-06-14 16:32:16

Changing status from needs_work to needs_review.


---

Comment by vdelecroix created at 2010-06-14 18:51:49

It appears that the get_min_max data is False. I'm working on it (post in few minutes)...


---

Comment by vdelecroix created at 2010-06-14 18:51:49

Changing status from needs_review to needs_work.


---

Comment by vdelecroix created at 2010-06-14 19:23:46

The bounding box seems to work now. I joined a worksheet that perform a lot of drawings.


---

Comment by vdelecroix created at 2010-06-14 19:23:46

Changing status from needs_work to needs_review.


---

Comment by kcrisman created at 2010-06-16 15:02:54

See #9076 for comments on bounding box and worksheet, though for this ticket I think it's ok.  Obviously the `fmod` function can be used here too, as well as already using math.pi since it's imported (I think this should work) and initializing the radii etc. as just the input numbers, waiting to float them until `_render...` and so forth.  Very nice work otherwise.

This patch also depends on #9076, for others who might test it.


---

Comment by kcrisman created at 2010-06-16 15:02:54

Changing status from needs_review to needs_work.


---

Attachment


---

Comment by vdelecroix created at 2010-06-26 14:09:22

worksheet that tests the bounding box of arcs and ellipses


---

Attachment

Replying to [comment:8 kcrisman]:
> See #9076 for comments on bounding box and worksheet, though for this ticket I think it's ok.  Obviously the `fmod` function can be used here too, as well as already using math.pi since it's imported (I think this should work) and initializing the radii etc. as just the input numbers, waiting to float them until `_render...` and so forth.  Very nice work otherwise.
> 
> This patch also depends on #9076, for others who might test it.


---

Comment by vdelecroix created at 2010-06-26 14:12:04

Changing status from needs_work to needs_review.


---

Comment by kcrisman created at 2010-08-10 15:06:34

Positive review!   This will be great.  

To release manager: very minor reviewer patch to be applied after `trac_9023-ellipse` patch.  This depends on #9076.


---

Comment by kcrisman created at 2010-08-10 15:06:34

Changing status from needs_review to positive_review.


---

Attachment

Apply after initial patch


---

Comment by kcrisman created at 2010-08-10 15:09:55

Also, see ticket #9719 for a followup to the awesome worksheet.


---

Comment by mpatel created at 2010-08-15 09:06:10

Changing status from positive_review to needs_work.


---

Comment by mpatel created at 2010-08-15 09:06:10

Please update [attachment:trac_9203-ellipse.patch] with a more descriptive commit string.


---

Comment by kcrisman created at 2010-08-16 12:46:36

Replying to [comment:13 mpatel]:
> Please update [attachment:trac_9203-ellipse.patch] with a more descriptive commit string.
The following patch is simply a hand-edited version to include a better commit message - it was not actually committed.  If that doesn't work/apply, we'll have to wait for the author to do this - but it would be really great to get this in!  Release manager can revert to positive review if this is satisfying.


---

Comment by kcrisman created at 2010-08-16 12:46:36

Changing status from needs_work to needs_review.


---

Comment by kcrisman created at 2010-08-16 12:47:04

With better commit message, otherwise same


---

Comment by mpatel created at 2010-08-16 21:17:40

Changing status from needs_review to positive_review.


---

Attachment


---

Comment by mpatel created at 2010-08-16 21:49:05

Replying to [comment:14 kcrisman]:
> Replying to [comment:13 mpatel]:
> > Please update [attachment:trac_9203-ellipse.patch] with a more descriptive commit string.
> The following patch is simply a hand-edited version to include a better commit message - it was not actually committed.  If that doesn't work/apply, we'll have to wait for the author to do this - but it would be really great to get this in!  Release manager can revert to positive review if this is satisfying.

Thanks for updating the patch.

Since the 4.5.3 series is now in feature freeze --- it's just open to blocker problems such as build errors, doctest fixes, etc. --- and we'll merge the PARI upgrade into 4.6.alpha0, it's very likely that merging this ticket and #9076 will have to wait until 4.6.alpha1, at least.


---

Comment by mpatel created at 2010-09-15 10:40:22

Resolution: fixed
