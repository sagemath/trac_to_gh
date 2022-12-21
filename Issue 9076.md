# Issue 9076: plot Arc of circle and ellipse

Issue created by migration from Trac.

Original creator: vdelecroix

Original creation time: 2010-05-28 20:12:41

Assignee: vdelecroix

CC:  sage-combinat kcrisman jason

Keywords: plot, arc, ellipse, circle

Implementation of arc plot 

This just wraps the matplotlib functionnality Arc
http://matplotlib.sourceforge.net/api/artist_api.html#matplotlib.patches.Arc

there is not yet fill capabilities (due to matplotlib).


---

Comment by vdelecroix created at 2010-06-05 11:40:37

Changing status from new to needs_review.


---

Comment by cremona created at 2010-06-05 15:09:08

I cannot review this as I know nothing about matplotlib (or graphics) and only learned 2 days ago how to draw a circle -- but what I really wanted was semicircles, so I will be happy when this is ready!


---

Comment by kcrisman created at 2010-06-10 00:49:02

Changing status from needs_review to needs_work.


---

Comment by kcrisman created at 2010-06-10 00:49:02

This patch is corrupt (in a sense) and has two copies of each changeset.   The second changeset seems to be a little more complete, so perhaps that is the correct one?    This will certainly be very easy to fix.


---

Comment by vdelecroix created at 2010-06-10 13:48:29

I fixed the patch (and I created another one #9203 for plotting ellipse).


---

Comment by vdelecroix created at 2010-06-10 13:48:29

Changing status from needs_work to needs_review.


---

Comment by kcrisman created at 2010-06-14 13:23:32

Changing status from needs_review to needs_work.


---

Comment by kcrisman created at 2010-06-14 13:23:32

In general, I like this.  Here are some specific suggestions to make it tip-top.

* line 26 - "an arc", not just "arc"

* There should be some examples for the class def, since that is in reference

* allowed options docs has circle a couple times rather than arc

* The '_repr_' method should have an explanation of radius, maybe even to the point of checking whether it is a circle or an ellipse (and then returning an appropriate string)

* Should be a plot3d method, or open a ticket to add one - though really one could just ape circle.py with x+r*cos(t*dt) and y+r*sin(t*dt) changed appropriately - and if not, then we should test the `NotImplementedError` raised in the base class.

* in arc(), we should have a few changes.  First, a few more of the options should be shown in the examples.  Second, I think a 2-uple is a 2-tuple (?).  Third, clearly the radii don't need to be floats, thought presumably they should be nonnegative.  Next, the sector should be clearly pointed out to be a 2-tuple in the input.  Finally, of the two examples shown, the red one isn't!  It would be good to give an explicit example of how angle (as opposed to sector) works, perhaps similarly to the one in get_min_max_data.  One should test the `NotImplementedError` at the end (under TESTS::, I guess)


---

Comment by kcrisman created at 2010-06-14 13:23:45

Changing component from geometry to graphics.


---

Comment by vdelecroix created at 2010-06-14 19:25:28

Changing status from needs_work to needs_review.


---

Comment by vdelecroix created at 2010-06-14 19:28:42

I get two problems in arc/ellipse:
  
   * there is an uncompatiblity of option names between disk and arc/ellipse. The function disk uses *angle* as the angle of the sector to draw as arc/ellipse uses angle but arc uses *sector*. Moreover the word *angle* is reserved for the angle between the horizontal and the angle of the first axis

    * I did not find any function that allows to make some calculus modulo 2pi. I created a dummy function mod2pi that does the reduction.


---

Comment by jason created at 2010-06-14 19:32:26

Replying to [comment:10 vdelecroix]:
> 
>     * I did not find any function that allows to make some calculus modulo 2pi. I created a dummy function mod2pi that does the reduction.


```
sage: math.fmod(10,2*pi)
3.7168146928204138
```


See http://docs.python.org/library/math.html#math.fmod


---

Comment by kcrisman created at 2010-06-16 14:59:41

I am sorry for the following laundry list.  I want to reiterate that in general this is very nice, but the hope is that this will be the best possible!  Thanks for your patience.

 * I think that the current algorithm for the bounding box is not the same as that in the worksheet, which seems to be pretty good.  The ellipse part works; I did find one example where the arc one didn't quite work:

```
my_arc=arc((1,-2),2,5,-pi/5,(3*pi/2,pi/4),thickness=2)
my_d=my_arc[0].get_minmax_data()
my_arc+polygon([(my_d['xmin'],my_d['ymin']),
          (my_d['xmin'],my_d['ymax']),
          (my_d['xmax'],my_d['ymax']),
          (my_d['xmax'],my_d['ymin'])],rgbcolor='red')
```


```
my_arc=arc((0,0),2,5,-pi/5,(3*pi/2,pi/4),thickness=2)
my_xmin,my_ymin,my_xmax,my_ymax=arc_bounding_box(2,5,-pi/5,3*pi/2,pi/4)
my_arc+polygon([(my_xmin,my_ymin),
          (my_xmin,my_ymax),
          (my_xmax,my_ymax),
          (my_xmax,my_ymin)],rgbcolor='red')
```

Maybe the part of the algorithm that checks whether to use the sector endpoints is too lax?

 * The worksheet is REALLY COOL, by the way; I strongly encourage you to add more commentary, turn the graphics into interacts, and advertise it as a great way to use Sage to demonstrate basic uses of parametric calculus!

 * With respect to `fmod` - yes, this makes sense to use.  (Otherwise we'd have to document the dummy function!)

 * I'd also point out that since you already imported pi from math, there should be no need to float it (? I think?); this happens a lot in this code.

```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: from math import pi
sage: pi
3.1415926535897931
sage: float(pi)
3.1415926535897931
```

| Sage Version 4.4.2, Release Date: 2010-05-19                       |
| Type notebook() for the GUI, and license() for information.        |
 * On a related point, the constructor should be as minimal as possible; why not wait to float the radii etc. until `_render_on_subplot_()` and `get_minmax_data()`?  That would also make the representation string much easier on the eyes (and intelligible).

 * Space missing in the sage/plot/plot.py reference

 * My sense is that the point of having ``@`rename_keyword(color='rgbcolor')` is so that 

```
sage: arc((0,0), 2, 1, 0, (0,pi/2), color="red") 
```

would work, which is more natural to the user (though I may be misunderstanding the documentation for sage.plot.misc.rename_keyword).   I realize that circle.py doesn't really take advantage of this... and really an rgbcolor should be a 3-tuple, morally speaking... That example doesn't have linestyle='--', incidentally.

 * Center should still be 2-tuple, not 2-uple
 
 * One may want to point out that alpha refers to transparency.

 * Minh will surely point out that we wish uniformity on 2-d, 2D, 2-D, or whatever.  I think the current convention is 2-D, though some docs have 2d or 2D.  But at any rate within a file it should be consistent.

 * Again, in the docs for `arc()`, the radii do NOT have to be floats.

 * should there be a check for negative radii, like in the patch for ellipse.py?  `arc((1,1),1,-1,pi,(pi/2,pi))` is logically correct but maybe would allow bugs in code of people using `arc` to slip through.

But again all of this takes nothing away from what is in general a great contribution.


---

Comment by kcrisman created at 2010-06-16 14:59:41

Changing status from needs_review to needs_work.


---

Attachment


---

Comment by vdelecroix created at 2010-06-26 14:06:30

>  * I think that the current algorithm for the bounding box is not the same as that in the worksheet, which seems to be pretty good.  The ellipse part works; I did find one example where the arc one didn't quite work:

There was a mistake... this now works on a lot (all?) examples.

>  * The worksheet is REALLY COOL, by the way; I strongly encourage you to add more commentary, turn the graphics into interacts, and advertise it as a great way to use Sage to demonstrate basic uses of parametric calculus!

I tried to enhanced the worksheet. I do not know what I can do more.
 
>  * On a related point, the constructor should be as minimal as possible; why not wait to float the radii etc. until `_render_on_subplot_()` and `get_minmax_data()`?  That would also make the representation string much easier on the eyes (and intelligible).

Here, I disagree because all plotting functions convert in the constructor. I do not know why, but for consistency I find it better to do this way. An other argument for this option is to get an error as soon as possible if the constructor is called with wrong argument.

I corrected all the other points in the way you suggested.


---

Comment by vdelecroix created at 2010-06-26 14:06:30

Changing status from needs_work to needs_review.


---

Comment by kcrisman created at 2010-08-10 14:47:57

Changing status from needs_review to positive_review.


---

Comment by kcrisman created at 2010-08-10 14:47:57

Okay, the constructor is not so important anyway.  If we get reports that the representation string is annoying, though, I'll open another ticket.  

Otherwise ENTHUSIASTIC positive review for a great addition.  Very minor changes (including putting a helper function somewhere it won't hurt doctest coverage, and a few typesetting things) attached in a reviewer patch.  Documentation now looks great, passes tests.


---

Attachment

Apply after initial patch


---

Comment by kcrisman created at 2010-08-10 14:49:40

To release manager - this should apply fine to 4.5.2.  Apply `arc` patch first, then `arc-reviewer` patch.


---

Comment by mpatel created at 2010-08-15 09:10:45

Changing status from positive_review to needs_work.


---

Comment by mpatel created at 2010-08-15 09:10:45

Please update [attachment:trac_9076-arc.patch] with a more descriptive commit string.


---

Comment by kcrisman created at 2010-08-16 12:50:27

Replying to [comment:16 mpatel]:
> Please update [attachment:trac_9076-arc.patch] with a more descriptive commit string.
This should get in, so here is a hand-edited version.  If this doesn't apply, we'll have to wait for the original author to do it, since I can never get an actual created patch to have someone else's information.  Release manager can revert to positive review if this works.


---

Comment by kcrisman created at 2010-08-16 12:50:27

Changing status from needs_work to needs_review.


---

Comment by kcrisman created at 2010-08-16 12:50:52

Same as other one, but better commit message


---

Attachment


---

Comment by mpatel created at 2010-08-16 21:16:42

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-09-15 10:40:26

Resolution: fixed
