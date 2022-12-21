# Issue 9746: documentation for plotting

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2010-08-14 14:15:00

Assignee: jason, was

CC:  kcrisman

I went through the "live" documentation for plots and found a number of places that computations should be split into separate cells, plots weren't displayed, etc.  This patch fixes these areas.


---

Comment by jason created at 2010-08-14 16:06:11

Depends on #9740, and possibly on #9221


---

Comment by jason created at 2010-08-14 16:06:17

Changing status from new to needs_review.


---

Comment by jason created at 2010-08-14 16:43:39

Changing type from defect to enhancement.


---

Comment by kcrisman created at 2010-09-21 20:03:47

There is a typo of 'primitve' in `plot/plot.py`.  Does this still apply to 4.6.alpha1?


---

Attachment

Replying to [comment:4 kcrisman]:
> There is a typo of 'primitve' in `plot/plot.py`.  Does this still apply to 4.6.alpha1?  

Yes.  I also refreshed the patch to correct the typo.  This depends on #9740.  Do you have time to review that and this patch?


---

Comment by kcrisman created at 2010-09-28 16:16:24

Changing status from needs_review to needs_work.


---

Comment by kcrisman created at 2010-09-28 16:16:24

Replying to [comment:5 jason]:
> Replying to [comment:4 kcrisman]:
> > There is a typo of 'primitve' in `plot/plot.py`.  Does this still apply to 4.6.alpha1?  
> 
> Yes.  I also refreshed the patch to correct the typo.  This depends on #9740.  Do you have time to review that and this patch?
Not totally at this time, though I see some of the things it is trying to fix.  I did take a look at some things while checking out the new matplotlib, and noticed that the example with `plot(1.5/(1+e^(-x))` is not correctly formatted in the documentation, and doesn't become a live cell.  I'm sorry to make this a long process.


---

Comment by kcrisman created at 2010-09-28 16:19:26

(Also, there are lots of places where there are many specific examples all together, such as in `point?`

```
point((1,2))
point((1,2,3))
point([(0,0), (1,1)])
point([(0,0,1), (1,1,1)]
```

but that should be a separate ticket.  I may be responsible for some of those, not realizing the live documentation needed these separate - or does it?)


---

Comment by jason created at 2010-09-28 16:34:59

Replying to [comment:7 kcrisman]:
> (Also, there are lots of places where there are many specific examples all together, such as in `point?`
> {{{
> point((1,2))
> point((1,2,3))
> point([(0,0), (1,1)])
> point([(0,0,1), (1,1,1)]
> }}}
> but that should be a separate ticket.  I may be responsible for some of those, not realizing the live documentation needed these separate - or does it?)

Those are fixed in my version (after #9740, #9746, and #4342).


---

Comment by kcrisman created at 2010-09-28 16:40:27

Hilarious - I didn't make it far enough down to see that this exact one is on this ticket!  Well, like I said, I don't have time to check it all the way... I feel like there were other similar places, though.


---

Comment by jason created at 2010-09-28 16:45:03

I've attached a patch which takes care of the error pointed out above, and corrects two or three more things in the docs.


---

Comment by jason created at 2010-09-28 16:45:03

Changing status from needs_work to needs_review.


---

Comment by jason created at 2010-09-28 16:58:22

apply on top of previous patches


---

Attachment

ptestlong in 4.6.alpha1 (Ubuntu 10.04 64-bit) passes with the following tickets applied in order: #9221 (and new spkg), #9740, #9746, #4342.


---

Comment by kcrisman created at 2010-09-29 03:31:06

Changing status from needs_review to needs_work.


---

Comment by kcrisman created at 2010-09-29 03:31:06

Okay, here are comments.  A lot of them are very similar in style, but I tried to be exhaustive within the files you modified.  I am too tired to look for problems in the other files, though they are likely there and I likely introduced them :)  But overall this is good, I just found more of the same for most (a few other errors, though).  Here we go! 

In scatterplot, there is another one of those 'these are equivalent' things, but they're not separated out.  Also, I get code{scatter_plot.options} instead of the actual code.  Should it be show() or `show()`?

In sage.plot.polygon.polygon we have something similar in the examples - somehow you only got some of them.  Again with the extra options guy, too.

Same with the equivalent in point.py, in both `point` and `points`.

In the `plot_field.py` file, why did you once add the x,y variable declaration and once not?  It doesn't really matter to me, but I wonder if there is something I'm missing.  Again with the `show()` or show(), and the equivalent.  It's not so important to me with the equivalent showing two things, but I feel like maybe you changed that one place - or maybe not.

In plot.py, ironically, just above the place where you fixed the `1.5/(1+e^(-x))` thing, there are a bunch of plots I didn't separate in my custom ticks patch.  My apologies - but there they are!  I also still get an error 'ellipsis object not callable' or something in 'add grid lines at specific positions (using lists/tuples)'.  There's an ellipsis that got stuck in there still somehow - I think you got a different one of these.

In line.py, after the cool cat there are a couple things as in the previous files - one nonseparated, one equivalent issue/show() issue.

In disk.py, maybe the disk that is parallel to the `xy`-plane should be plotted, not just its type?  Same equiv/show question.

I don't know what happened in density plot, but I think a tick is missing in the `DensityPlot` documentation - likely my fault?  This is in 'Examples'.

In contour plot, the very last example under `region_plot` should have two plots, but has one.  But they are different.

The circles also has the parallel to the `xy`-plane issue when it comes to giving the type, but not the plot.


---

Comment by jason created at 2010-09-29 04:08:29

So, since a lot of tickets depend on this one, why don't we make all of these a separate ticket?  That's a great list for improving docs!


---

Comment by jason created at 2010-09-29 04:08:29

Changing status from needs_work to needs_review.


---

Comment by kcrisman created at 2010-09-29 18:00:11

Okay, I'll cave in.  I don't know that 'a lot' of tickets depend on this (if #4342 counts as 'a lot') but a ticket with 'even more plot documentation improvements' sounds okay.  This is now #10032.

Positive review to this patch, but noting that #10032 addresses more issues of a similar nature.


---

Comment by kcrisman created at 2010-09-29 18:00:11

Changing status from needs_review to positive_review.


---

Comment by jason created at 2010-09-29 18:12:11

Replying to [comment:15 kcrisman]:
> Okay, I'll cave in.  I don't know that 'a lot' of tickets depend on this (if #4342 counts as 'a lot') but a ticket with 'even more plot documentation improvements' sounds okay.  This is now #10032.


I knew it was in the stack of patches I had applied, and other patches depended on it.  How about "an important patch that has been waiting a very long time depends on this"? :)

My purpose is to just narrow the scope of this ticket to exactly the improvements actually done in the patch.  Thanks for agreeing and opening up another ticket for more improvements.


---

Comment by kcrisman created at 2010-09-29 18:26:32

Replying to [comment:16 jason]:
> Replying to [comment:15 kcrisman]:
> > Okay, I'll cave in.  I don't know that 'a lot' of tickets depend on this (if #4342 counts as 'a lot') but a ticket with 'even more plot documentation improvements' sounds okay.  This is now #10032.
> 
> 
> I knew it was in the stack of patches I had applied, and other patches depended on it.  How about "an important patch that has been waiting a very long time depends on this"? :)
I agree with that!
> My purpose is to just narrow the scope of this ticket to exactly the improvements actually done in the patch.  Thanks for agreeing and opening up another ticket for more improvements.
No problem - although not using queues made this a little harder for me to test.


---

Comment by kcrisman created at 2010-09-29 18:40:34

This one

```
 I also still get an error 'ellipsis object not callable' or something in 'add grid lines at specific positions (using lists/tuples)'. There's an ellipsis that got stuck in there still somehow - I think you got a different one of these.
```

in particular is aggravating, and should be fixed quickly, if possible.


---

Comment by mpatel created at 2010-10-03 06:35:58

Resolution: fixed
