# Issue 3907: plot correctly up to asymptotes

Issue created by migration from Trac.

Original creator: kcrisman

Original creation time: 2008-08-20 01:21:12

Assignee: was

Assuming this is a bug, not a feature:

```
sage: plot(1/x,0,1)
<boom>

My feeling is this should plot okay, since there is only one "bad"
point and the plotting code handles that kind of thing.

As far as I can tell from the traceback (relevant appended), the
problem is in the axes, which convert (at least when using
_tasteful_ticks) the endpoints to integers, given a big enough range.

sage: plot(1/x,0,1)
---------------------------------------------------------------------------
OverflowError                             Traceback (most recent call
last)

/Applications/sage/local/lib/python2.5/site-packages/sage/plot/plot.py
in _repr_(self)
    738         """
    739         if SHOW_DEFAULT:
--> 740             self.show()
    741             return ''
    742         else:

/Applications/sage/local/lib/python2.5/site-packages/sage/plot/plot.py
in show(self, xmin, xmax, ymin, ymax, figsize, filename, dpi, axes,
axes_labels, frame, fontsize, aspect_ratio)
   1252                   axes_labels=axes_labels,
   1253                   frame=frame, fontsize=fontsize,
-> 1254                   aspect_ratio=aspect_ratio)
   1255         os.system('%s %s 2>/dev/null 1>/dev/null &'%
(sage.misc.viewer.browser(), filename))
   1256

/Applications/sage/local/lib/python2.5/site-packages/sage/plot/plot.py
in save(self, filename, xmin, xmax, ymin, ymax, figsize, figure, sub,
savenow, dpi, axes, axes_labels, fontsize, frame, verify,
aspect_ratio)
   1429                 xmin,xmax,ymin,ymax = self._prepare_axes(xmin,
xmax, ymin, ymax)
   1430
-> 1431                 xmin, xmax, ymin, ymax =
sage_axes.add_xy_axes(subplot, xmin, xmax, ymin, ymax)
   1432
   1433                 subplot.set_xlim(xmin, xmax)

/Applications/sage/local/lib/python2.5/site-packages/sage/plot/axes.py
in add_xy_axes(self, subplot, xmin, xmax, ymin, ymax, axes, ticks,
axesstyle, axes_labels)
    324
    325         #evalute find_axes for y values and x ticks
--> 326         x_axis_ypos, ystep, ytslminor, ytslmajor =
self._find_axes(ymin, ymax)
    327         xltheight = 0.015*yspan
    328         xstheight = 0.25*xltheight

/Applications/sage/local/lib/python2.5/site-packages/sage/plot/axes.py
in _find_axes(self, minval, maxval)
    240             tslmajor, oppaxis, step =
self._tasteless_ticks(minval, maxval, 10)
    241         else:
--> 242             tslmajor, oppaxis, step =
self._tasteful_ticks(minval, maxval)
    243         min = tslmajor[0] - step
    244         tslminor = sage.misc.misc.srange(min, maxval +
0.2*step, 0.2*step)

/Applications/sage/local/lib/python2.5/site-packages/sage/plot/axes.py
in _tasteful_ticks(self, minval, maxval)
    124             else:
    125                 if maxval >= 10:
--> 126                     sl = [s for s in str(int(absmax))]
    127                     d0 = eval(sl[0])
    128                     d1 = eval(sl[1])

OverflowError: cannot convert float infinity to long
```



---

Attachment


---

Comment by mhansen created at 2008-08-29 00:04:09

Changing assignee from was to mhansen.


---

Comment by mhansen created at 2008-08-29 00:04:09

I've attached a patch which fixes the big traceback you get and actually produces a plot.  This, however, does not fix the issue with the range on the y-axis being thrown of by asymptotes.  I think that should be a separate ticket.


---

Comment by mhansen created at 2008-08-29 00:04:09

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-08-29 02:43:20

Replying to [comment:1 mhansen]:
> I've attached a patch which fixes the big traceback you get and actually produces a plot.  This, however, does not fix the issue with the range on the y-axis being thrown of by asymptotes.  I think that should be a separate ticket.

kcrisman opened a ticket for that at #3985 - at least it seems very close to what you suggest.

Cheers,

Michael


---

Comment by robertwb created at 2008-09-02 08:36:34

Mostly looks good, but what about `-inf`?


---

Attachment

I've updated the patch to handle the -inf case.


---

Comment by rlm created at 2008-09-05 19:43:09

Apply only the second patch- applies cleanly to sage-3.1.2.alpha3 and passes tests in the files it touches.


---

Comment by mabshoff created at 2008-09-06 00:07:53

Resolution: fixed


---

Comment by mabshoff created at 2008-09-06 00:07:53

Merged in Sage 3.1.2.rc0
