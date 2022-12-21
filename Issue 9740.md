# Issue 9740: matrix plot is upside down and should wrap more matplotlib options

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2010-08-13 08:14:04

Assignee: jason, was

CC:  rbeezer kcrisman

This patch:
  * flips the matrix so that it is right side up, and flips the y-axis to correctly label the rows, unless origin='lower' is specified.
  * Adds matplotlib's vmin and vmax parameters, which control the scaling
  * Adds matplotlib's norm parameter, which also controls the scaling




---

Comment by jason created at 2010-08-13 08:14:58

oh, and it also makes axes=False by default, since it looked really silly having axes

and this patch also shifts the matrix by 0.5 so it is centered in the plot.


---

Comment by jason created at 2010-08-13 08:42:41

Changing type from defect to enhancement.


---

Comment by jason created at 2010-08-13 08:42:41

CCing people that might be interested in reviewing this.


---

Comment by jason created at 2010-08-13 08:42:41

Changing status from new to needs_review.


---

Comment by kcrisman created at 2010-08-13 12:54:16

In what sense were the matrix plots wrong before?  I'm a little confused - the matrix plots I used in number theory seemed to be ok.  Also, what matrix plots have axes?  The ones I make only have frames, which look quite nice (except for being labeled wrong).   Anyway, posting a picture of "before" and "after" that is very clear would be helpful before one takes the time to wade through the mpl code :)

#2189 is related, though I don't know if this fixes all the issues mentioned there (i.e. labeling).


---

Comment by jason created at 2010-08-13 15:45:41

Before:

 * axes=True was the default, so typically there were lines on the far right and far bottom of the plot going through the first row and first column of the matrix

 * matrices were plotted upside-down, where the first row was on the bottom of the matrix.

You're right that #2189 is related, but that patch will have to be rewritten so much that it's probably easiest to write it from scratch.  Thanks for pointing out the patch, though.  You're also right that we are solving a different problem here.  This patch does not fix the issue there.


---

Comment by kcrisman created at 2010-08-13 15:56:03

Replying to [comment:4 jason]:
> Before:
> 
>  * axes=True was the default, so typically there were lines on the far right and far bottom of the plot going through the first row and first column of the matrix

I don't remember seeing that.

>  * matrices were plotted upside-down, where the first row was on the bottom of the matrix.

Huh, that is weird, because I definitely didn't have that experience.

Attached is a screenshot of what I get.  The top row is all the powers of 1 mod 7 (which are all 1), and the left row is all the 0th powers of a mod 7 (which are all 1).  The right row is Fermat's Little Theorem, that the 6th powers are also 1 mod 7.  The matrix itself is

```
sage: p=7
sage: matrix(p-1,[mod(a,p)^b for a in range(1,p) for b in srange(p)])
[1 1 1 1 1 1 1]
[1 2 4 1 2 4 1]
[1 3 2 6 4 5 1]
[1 4 2 1 4 2 1]
[1 5 4 6 2 3 1]
[1 6 1 6 1 6 1]
```

I feel like I must be missing something.


---

Comment by kcrisman created at 2010-08-13 15:56:31

The matrix in an interact for p=7


---

Attachment

Could you try the following two plots?

matrix_plot(identity_matrix(100))

matrix_plot(identity_matrix(100, sparse=True))


---

Comment by jason created at 2010-08-13 16:06:40

(that is *before* the patch, of course...)


---

Comment by kcrisman created at 2010-08-13 16:16:55

> matrix_plot(identity_matrix(100))
Looks fine, diagonal is from upper left to lower right, like the matrix. 0 (lowest input) is black, 1 (highest input) is white, I think this is as usual.  With cmap='jet' I get something I like :)  What do *you* get for this one?
> matrix_plot(identity_matrix(100, sparse=True))
Yikes!  Two issues.  First, it is definitely flipped.  Second, what's up with the colors?  I get white for the off-diagonal zeros and blue for the diagonal.  My diagnosis: something going on with all that special code for sparse matrices.

And now I see what you mean about the axes showing up.  I thought that was just part of the frame because my matrices tend to have blue or black around the edges, since the values are one!  Good catch with making axes=False in the future.


---

Comment by jason created at 2010-08-13 16:21:11

After the patch, the labels are corrected.  The issue of flipping the matrix is also affected by a matplotlibrc variable, so you might have the "correct" value of origin='upper'.  Of course, this is ignored for sparse matrices.  That patch corrects all this so that things are consistent.

For sparse matrices---the correct picture is whote for off-diagonal and blue for diagonal.  That uses spy underneath, which does not plot zero entries, which is exactly what you want for sparse matrices.


---

Comment by kcrisman created at 2010-08-13 16:46:29

Got it.  And sure enough, in my top directory (i.e., above my user account) there is one, probably placed there eons ago by some primitive Sage installation, with

```
image.origin : upper             # lower | upper
```

Is that it?

I hate to be picky, but I have another question.

```
Generally matrices are plotted with the (0,0) entry in the upper 
right.  However, sometimes if we are plotting an image, we'd like 
the (0,0) entry to be in the lower left. 
```

Should the first word in the second line be 'left'?  And if not, please explain.


---

Comment by jason created at 2010-08-13 16:59:12

Yep, that's it.  And yes, you're right about the doc correction.  New patch coming up.


---

Comment by jason created at 2010-08-13 17:06:03

I should have made that a separate patch; sorry.  The only change is that one word 'right'->'left'


---

Comment by jason created at 2010-08-14 16:25:38

A new version of the patch that:

  * makes it possible to plot dense matrices upside-down
  * ensures tick labels are integrs.


---

Comment by jason created at 2010-09-07 03:29:46

Just one more enhancement to bring sparse plotting in line with dense plotting: we were automatically converting to floating point numbers in the dense case, which allowed plotting matrices over finite fields, for example.  The coerce-float patch enables this for sparse matrices as well.


---

Comment by jason created at 2010-09-28 16:02:02

I'm rebasing this for 4.6.alpha1 momentarily...


---

Comment by jason created at 2010-09-28 16:04:32

I've rebased to 4.6.alpha1 and combined the two patches.  kcrisman: can you review this?


---

Attachment

apply only this patch; rebased to 4.6.alpha1


---

Comment by jason created at 2010-09-28 19:08:22

ptestlong in 4.6.alpha1 (Ubuntu 10.04 64-bit) passes with the following tickets applied in order: #9221 (and new spkg), #9740, #9746, #4342.


---

Comment by kcrisman created at 2010-09-28 19:33:49

Explain `axes_integer`.  Also, the options for the locators weren't always

```
locator_options=dict(nbins=9,steps=[1,2,5,10],integer=axes_integer)
```

in all cases - will this make anything different, particularly the `steps` addition?  That stuff should have been a separate ticket, or maybe on #9221 ;)

Explain

```
limits[k]-=0.5
```

I assume this makes it so that the matrix has `0,1,2,3` as opposed to putting entries between `0-1`, `1-2`, etc.  I can't check this because the branch I'm making for this decided to rebuild documentation, which takes a while... sigh.

Good catch on the complex guys.

Just point of information to other readers; very minor doc issues are corrected in #9746.


---

Comment by kcrisman created at 2010-09-28 20:00:03

Replying to [comment:18 kcrisman]:
> Explain `axes_integer`.  
> Explain
> {{{
> limits[k]-=0.5
> }}}
> I assume this makes it so that the matrix has `0,1,2,3` as opposed to putting entries between `0-1`, `1-2`, etc.  I can't check this because the branch I'm making for this decided to rebuild documentation, which takes a while... sigh.

Okay, I think that these two things combine to make this happen, after reading [this](http://matplotlib.sourceforge.net/api/ticker_api.html#matplotlib.ticker.MaxNLocator) again.

I still don't know if I like sparse and dense matrices looking so different.  So the idea is that the little circle points indicate sparse, while the boxes indicate dense?  I'm thinking of 

```
sage: b=random_matrix(GF(2),12,sparse=True,density=0.99)
sage: matrix_plot(b)

sage: b=random_matrix(GF(2),12,density=0.99)
sage: matrix_plot(b)
```


Also, my favorite use case doesn't work yet, though to be fair it didn't work before, so this shouldn't hold things up (and is a currently open ticket).  But just in case, is there a quick way to get this now?  After all, one might want the first row to be labeled 1 sometimes!

```
sage: M = matrix(ZZ,[[1,2,3,4],[1,4,9,16],[1,8,27,64]])
sage: matrix_plot(M)
sage: matrix_plot(M,ticks=[1,2,3,4])
ERROR: An unexpected error occurred while tokenizing input
<snip>
   1992 
   1993             from matplotlib.ticker import OldScalarFormatter, MaxNLocator, MultipleLocator, FixedLocator, NullLocator, Locator
-> 1994             x_locator, y_locator = ticks
   1995             if x_locator is None:
   1996                 x_locator = MaxNLocator(**locator_options)

ValueError: too many values to unpack
```


I should be able to finish reviewing this later on today.


---

Comment by jason created at 2010-09-28 20:02:30

I fixed the issues you mentioned.  I also changed the option name to `ticks_integer` to be more consistent with the new ticks options.

Yes, the defaults may change slightly with the steps option.  I don't know why I didn't put in those steps defaults before; they look better, and this will provide consistency to have the same steps options for different calls.  Possibly it should have gone on another ticket, but I already had to consolidate things for the integer option.


---

Comment by jason created at 2010-09-28 20:10:17

I didn't fix the issues you mentioned in http://trac.sagemath.org/sage_trac/ticket/9740#comment:19, though.


---

Comment by jason created at 2010-09-28 20:13:26

Replying to [comment:19 kcrisman]:
> Replying to [comment:18 kcrisman]:
> > Explain `axes_integer`.  
> > Explain
> > {{{
> > limits[k]-=0.5
> > }}}
> > I assume this makes it so that the matrix has `0,1,2,3` as opposed to putting entries between `0-1`, `1-2`, etc.  I can't check this because the branch I'm making for this decided to rebuild documentation, which takes a while... sigh.
> 
> Okay, I think that these two things combine to make this happen, after reading [this](http://matplotlib.sourceforge.net/api/ticker_api.html#matplotlib.ticker.MaxNLocator) again.
> 
> I still don't know if I like sparse and dense matrices looking so different.  So the idea is that the little circle points indicate sparse, while the boxes indicate dense?  I'm thinking of 
> {{{
> sage: b=random_matrix(GF(2),12,sparse=True,density=0.99)
> sage: matrix_plot(b)
> 
> sage: b=random_matrix(GF(2),12,density=0.99)
> sage: matrix_plot(b)
> }}}

Yes; you can choose the marker used in sparse matrices.  Aside from the fact that this is a fundamental difference in matplotlib, it does also make sense.  In dense matrices, most entries are nonzero, so you color every pixel/square.  In sparse matrices, most entries are zero, so you only put a marker where there is a nonzero.


> 
> Also, my favorite use case doesn't work yet, though to be fair it didn't work before, so this shouldn't hold things up (and is a currently open ticket).  But just in case, is there a quick way to get this now?  After all, one might want the first row to be labeled 1 sometimes!
> {{{
> sage: M = matrix(ZZ,[[1,2,3,4],[1,4,9,16],[1,8,27,64]])
> sage: matrix_plot(M)
> sage: matrix_plot(M,ticks=[1,2,3,4])
> ERROR: An unexpected error occurred while tokenizing input
> <snip>
>    1992 
>    1993             from matplotlib.ticker import OldScalarFormatter, MaxNLocator, MultipleLocator, FixedLocator, NullLocator, Locator
> -> 1994             x_locator, y_locator = ticks
>    1995             if x_locator is None:
>    1996                 x_locator = MaxNLocator(**locator_options)
> 
> ValueError: too many values to unpack
> }}}

Yes, definitely another ticket.


---

Comment by jason created at 2010-09-28 20:15:08

of course, your ticks example above does *not* label the first row 1; it would only put a tick on the *second* row (if it worked).  You probably want to change the tick_formatter argument to relabel things.


---

Comment by kcrisman created at 2010-09-28 20:17:44

Replying to [comment:21 jason]:
> I didn't fix the issues you mentioned in http://trac.sagemath.org/sage_trac/ticket/9740#comment:19, though.
That's okay, they are preexisting behavior and still similar, so can be discussed elsewhere.

You beat me to realizing the rebase needed now in #4342.  Luckily I could just roll that back... someday I'll use queues.


---

Comment by kcrisman created at 2010-09-29 03:10:37

Okay, in general this is great!  I love the live documentation for testing, by the way - don't know why I never thought of that before.

Two things, which perhaps should still be addressed - what do you think?

First, the error message with the `matrix_plot(A,marker=',')` is not very helpful when you choose a different marker (for instance, '<' works (and is cool with small matrices) but ';' doesn't).  I realize this isn't part of the ticket per se, so maybe this should be a followup.

Second, there are two instances of 

```
Extra options will get passed on to show(), as long as they are valid:
```

in the documentation for `MatrixPlot`.  Again, maybe this is better addressed on a followup ticket.

I like that the error message for when `vmin` and `vmax` clash is actually helpful, even though it's an mpl error.

I also just noticed that the doc for `matrix_plot` doesn't mention that the default for `norm` is `None`, though it is.  This can probably be fixed very easily.


---

Comment by kcrisman created at 2010-09-29 03:32:43

Changing status from needs_review to needs_work.


---

Comment by kcrisman created at 2010-09-29 03:32:43

> Second, there are two instances of 
> {{{
> Extra options will get passed on to show(), as long as they are valid:
> }}}
> in the documentation for `MatrixPlot`.  Again, maybe this is better addressed on a followup ticket.
Or in #9746?

> I also just noticed that the doc for `matrix_plot` doesn't mention that the default for `norm` is `None`, though it is.  This can probably be fixed very easily.
After thinking about it, since the ticket says to wrap more mpl options, this should be addressed on this ticket.


---

Comment by jason created at 2010-09-29 04:21:35

apply on top of previous patches


---

Comment by jason created at 2010-09-29 04:22:44

Changing status from needs_work to needs_review.


---

Attachment

I updated the review-fixes patch to take care of the issues you brought up.  I also polished two more references in the docs.


---

Comment by kcrisman created at 2010-09-29 17:53:23

Changing status from needs_review to positive_review.


---

Comment by kcrisman created at 2010-09-29 17:53:23

Thanks a ton - the only other thing I saw is fixed in #9746, so all is well, other than stuff above that can go in another ticket.

Positive review.


---

Comment by mpatel created at 2010-10-03 06:36:03

Resolution: fixed
