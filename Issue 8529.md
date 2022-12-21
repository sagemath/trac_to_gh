# Issue 8529: default colors for plot and implicit_plot are not consistent

Issue created by migration from Trac.

Original creator: AlexGhitza

Original creation time: 2010-03-13 22:34:10

Assignee: was

CC:  kcrisman

Keywords: plot default color

When plotting a function using `plot`, the default color for the graph of the function is blue.  The default color for `implicit_plot` is black.  It would be preferable to have the same default color.


---

Comment by jason created at 2010-05-26 15:44:24

Changing keywords from "plot default color" to "plot default color beginner".


---

Comment by ryan created at 2010-07-27 23:39:08

the attached patch will change the default color of plot to black (so that it matches implicit_plot).


---

Comment by jason created at 2010-07-27 23:44:30

Changing status from new to needs_work.


---

Comment by jason created at 2010-07-27 23:44:30

Ryan!  Welcome to Trac!  Congratulations on your patch!

I think maybe it would be better to make the implicit plot default color be blue.  I like that a plot is a different color than the axes so that it's easier to distinguish the two.

Also, when a patch is ready for review, change the state below to "needs review".


---

Comment by jason created at 2010-07-27 23:55:34

See http://sagenb.org/home/jason3/230/ for how to plot implicit plots in a different color:


```
var('x,y')
implicit_plot(x^2-y^2==1, (x,-5,5), (y,-5,5), cmap=["red"])
```


I think it might be enough to give another argument to the `@`options decorator for implicit_plot: `cmap=["blue"]`


---

Comment by jason created at 2010-07-27 23:59:24

Even better, do `cmap=("blue")`, since then the tuple can not be modified by other things.


---

Comment by jason created at 2010-07-28 00:01:45

Replying to [comment:6 jason]:
> Even better, do `cmap=("blue")`, since then the tuple can not be modified by other things.

I mean `cmap=("blue",)`, so that it's a tuple, not just a string in parentheses.


---

Comment by kcrisman created at 2010-07-28 01:17:20

Replying to [comment:5 jason]:
> See http://sagenb.org/home/jason3/230/ for how to plot implicit plots in a different color:

If you published this, you didn't include the link.
> 
> {{{
> var('x,y')
> implicit_plot(x<sup>2-y</sup>2==1, (x,-5,5), (y,-5,5), cmap=["red"])
> }}}

So annoying that color='red' wouldn't work.  What happens with that?


---

Comment by kcrisman created at 2010-07-28 01:18:14

Replying to [comment:4 jason]:
> Ryan!  Welcome to Trac!  Congratulations on your patch!
> 

Yes!  You aren't by chance the famed little brother of Jason, are you?


---

Comment by jason created at 2010-07-28 08:00:54

Replying to [comment:8 kcrisman]:


> So annoying that color='red' wouldn't work.  What happens with that?

That would take one or two more lines of code to support.  Probably add it to `@`options, and then make a cmap=[<color>] argument that is passed to contour_plot.


---

Comment by ryan created at 2010-07-30 20:19:29

ok...here's the new patch.

One can now set the color of implicit_plot using cmap or the "new" color option (idea curtesy of kcrisman).  Note: syntax for cmap is still the same.  Syntax for color is ` color='blue' `

`@`kcrisman: Yeah, I'm Jason's little brother.  

Have fun with all those colorful plots :)


---

Comment by jason created at 2010-07-31 04:33:42

This is great.  Just one more thing: there should be some sort of doctest illustrating this (the question of how to change the color of an implicit plot has come up before, and it's bound to come up again, so it'd be nice to just point them to the documentation of the function).

Just take your favorite example and put it in the EXAMPLES section of the docstring of the function, following the format of the examples around it.


---

Comment by jason created at 2010-07-31 04:35:26

(and it's more than nice; patches are required to have doctests if they fix a bug or add new features these days...)

After you add a doctest, then you can run:


```
sage -b
```


to rebuild, and then 


```
sage -t contour_plot.py
```


to run the tests.


---

Comment by ryan created at 2010-08-01 01:21:16

(Patch + Documentation) Change color of implicit plot.


---

Attachment

ok...updated patch (with documentation).

Thanks jason for the reminder add the documentation.  This patch passed the doctests.


---

Comment by ryan created at 2010-08-03 06:38:52

Changing status from needs_work to needs_review.


---

Comment by kcrisman created at 2010-08-10 16:06:44

Changing status from needs_review to positive_review.


---

Comment by kcrisman created at 2010-08-10 16:06:44

This is nice - positive review.  

I fixed some minor doc issues added a really cool example I stumbled upon while testing it (picture attached), and also updated some other minor doc issues which became apparent with this - all of which are basically related to the color or are just typos.

To release manager: Apply `trac_8529-color-implicit-plot` and then `trac-8529-reviewer`.


---

Comment by kcrisman created at 2010-08-10 16:07:03

Apply after initial patch


---

Attachment

Super-cool example picture of this patch working


---

Attachment

This solves #9654 too.


---

Comment by jason created at 2010-08-14 14:47:03

please apply my reviewer-reviewer patch on top of everything else; it simplifies the doc source a little.


---

Comment by kcrisman created at 2010-08-16 12:31:10

Replying to [comment:18 jason]:
> please apply my reviewer-reviewer patch on top of everything else; it simplifies the doc source a little.
Thanks, I didn't know about this `~` notation.


---

Comment by kcrisman created at 2010-08-16 12:54:28

Just FYI, the (essentially) positively reviewed #9203 and #9076 add functions with the same `~` not being used, and won't apply properly with this one.  I recommend that those be applied first, then this one applied to see what would need to be updated, and then this one updated - since those implement actual new functionality.  Or we can split this one up into a different ticket for updating the plot doc, or add that in with #9746.


---

Comment by mpatel created at 2010-09-18 07:37:33

With the other tickets merged into 4.6.alpha1, I get

```
[...]
$ hg qpush
applying trac-8529-reviewer-reviewer.patch
patching file sage/plot/plot.py
Hunk #1 FAILED at 6
1 out of 3 hunks FAILED -- saving rejects to file sage/plot/plot.py.rej
patch failed, unable to continue (try -v)
patch failed, rejects left in working dir
errors during apply, please fix and refresh trac-8529-reviewer-reviewer.patch
```

The .rej file:

```diff
--- plot.py
+++ plot.py
`@``@` -7,20 +7,20 `@``@`
 The following graphics primitives are supported:
 
 
--  :func:`arrow() <sage.plot.arrow.arrow>` - an arrow from a min point to a max point.
-
--  :func:`circle() <sage.plot.circle.circle>` - a circle with given radius
-
--  :func:`disk() <sage.plot.disk.disk>` - a filled disk (i.e. a sector or wedge of a circle)
-
--  :func:`line() <sage.plot.line.line>` - a line determined by a sequence of points (this need not
+-  :func:`~sage.plot.arrow.arrow` - an arrow from a min point to a max point.
+
+-  :func:`~sage.plot.circle.circle` - a circle with given radius
+
+-  :func:`~sage.plot.disk.disk` - a filled disk (i.e. a sector or wedge of a circle)
+
+-  :func:`~sage.plot.line.line` - a line determined by a sequence of points (this need not
    be straight!)
 
--  :func:`point() <sage.plot.point.point>` - a point
-
--  :func:`text() <sage.plot.text.text>` - some text
-
--  :func:`polygon() <sage.plot.polygon.polygon>` - a filled polygon
+-  :func:`~sage.plot.point.point` - a point
+
+-  :func:`~sage.plot.text.text` - some text
+
+-  :func:`~sage.plot.polygon.polygon` - a filled polygon
 
 
 The following plotting functions are supported:
```

Could someone rebase the "reviewer-reviewer" patch when 4.6.alpha1 is out?


---

Comment by mpatel created at 2010-09-18 07:37:33

Changing status from positive_review to needs_work.


---

Comment by jason created at 2010-10-19 06:12:48

apply on top of previous patches


---

Attachment

I rebased the reviewer-reviewer patch for 4.6.alpha3.  In fact, that reviewer-reviewer patch was so picky, it probably would have been okay to just ignore it anyway.


---

Comment by jason created at 2010-10-19 06:26:26

Changing status from needs_work to positive_review.


---

Comment by jdemeyer created at 2010-11-01 10:05:49

Resolution: fixed
