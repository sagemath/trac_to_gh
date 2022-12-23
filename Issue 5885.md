# Issue 5885: #5567 should throw a deprecation warning

Issue created by migration from https://trac.sagemath.org/ticket/5885

Original creator: jason

Original creation time: 2009-04-24 01:20:37

Assignee: burcin

CC:  jason

#5567 fixes a bug, but in doing so, avoids the deprecation warning that should happen when the user types in

```
region_plot([y>0,x>0,x^2+y^2<3], (-3, 3), (-3,3),plot_points=100,incol='gray').show(aspect_ratio=1)
```


See #5413 for details on the deprecation warning.  This deprecation warning should be triggered when the code in the doctest of #5567 is run.


---

Comment by kcrisman created at 2009-04-30 01:04:14

What alternate syntax for a region of this kind would be appropriate, though?  Anything requiring a lambda construction or a previous function declaration seems awkward.

Perhaps the fix is to require variable declaration (e.g.

```
region_plot([y>0,x>0,x^2+y^2<3], (x,-3, 3), (y,-3,3),plot_points=100,incol='gray').show(aspect_ratio=1)
```

but otherwise keep equify and friends.  In particular, the current doctest is too symmetric - better would be

```
region_plot([y>0,x>0,x^2+y^2<3], (x,-3, 4), (y,-4,3),plot_points=100,incol='gray').show(aspect_ratio=1)
```

since otherwise it isn't clear that the correct variables are associated with the correct input range otherwise.

I'm also changing the milestone to 4.0, concurrent with the Pynac switch.    If anyone posts a patch they can change it back :)  I don't think it's a blocker either, but will accept Jason's categorization in those terms due to the switch.


---

Comment by was created at 2009-06-15 23:26:47

If we've released for 2 months without fixing this, it doesn't make sense to keep it as a blocker.


---

Comment by was created at 2009-06-15 23:26:47

Changing priority from blocker to critical.


---

Comment by kcrisman created at 2010-01-08 16:23:43

Given that #7809 has positive review and has changed this particular doctest, AND given that region_plot in this format has existed for close to a year with no complaints, and given that #7809 now makes clear what we _want_ the behavior to be, I think it's time to close this ticket.  If jason or was concurs, then let's do it.


---

Comment by jason created at 2010-01-09 05:25:48

I concur, but for a totally different reason.  The deprecation warning is now thrown (probably because of the changes in #7809?):


```
sage: var('y')
y
sage: region_plot([y>0,x>0,x^2+y^2<3], (-3, 3), (-3,3),plot_points=100,incol='gray').show(aspect_ratio=1)
/home/grout/sage/local/lib/python2.6/site-packages/sage/plot/contour_plot.py:565: DeprecationWarning: Unnamed ranges for more than one variable is deprecated and will be removed from a future release of Sage; you can used named ranges instead, like (x,0,2)
  g, ranges = setup_for_eval_on_grid(f, [xrange, yrange], plot_points)


```



---

Comment by jason created at 2010-01-09 05:38:24

(to take care of a reviewer comment) -- I feel that we don't have to put in a DeprecationWarning doctest since the deprecation warning happens not in the region_plot function, but at a lower level, and it is already doctested there.

I think this ticket can be closed as fixed once #7809 is merged.


---

Comment by jason created at 2010-01-09 05:38:58

uh, I'll put this as "needs review", and maybe kcrisman can give it a positive review?


---

Comment by jason created at 2010-01-09 05:38:58

Changing status from new to needs_review.


---

Comment by kcrisman created at 2010-01-19 16:29:28

Sorry, I didn't see this recently.  Yes, we do get an appropriate deprecation warning.  I don't know that there is really an author or reviewer for this... just a closure.

Also, the plot is still one pixel off :)


---

Comment by kcrisman created at 2010-01-19 16:29:28

Changing status from needs_review to positive_review.


---

Comment by mvngu created at 2010-01-22 21:42:02

Fixed due to #7809.


---

Comment by mvngu created at 2010-01-22 21:42:02

Resolution: fixed
