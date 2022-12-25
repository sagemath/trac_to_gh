# Issue 3907: plot correctly up to asymptotes

archive/issues_003907.json:
```json
{
    "body": "Assignee: @williamstein\n\nAssuming this is a bug, not a feature:\n\n```\nsage: plot(1/x,0,1)\n<boom>\n\nMy feeling is this should plot okay, since there is only one \"bad\"\npoint and the plotting code handles that kind of thing.\n\nAs far as I can tell from the traceback (relevant appended), the\nproblem is in the axes, which convert (at least when using\n_tasteful_ticks) the endpoints to integers, given a big enough range.\n\nsage: plot(1/x,0,1)\n---------------------------------------------------------------------------\nOverflowError                             Traceback (most recent call\nlast)\n\n/Applications/sage/local/lib/python2.5/site-packages/sage/plot/plot.py\nin _repr_(self)\n    738         \"\"\"\n    739         if SHOW_DEFAULT:\n--> 740             self.show()\n    741             return ''\n    742         else:\n\n/Applications/sage/local/lib/python2.5/site-packages/sage/plot/plot.py\nin show(self, xmin, xmax, ymin, ymax, figsize, filename, dpi, axes,\naxes_labels, frame, fontsize, aspect_ratio)\n   1252                   axes_labels=axes_labels,\n   1253                   frame=frame, fontsize=fontsize,\n-> 1254                   aspect_ratio=aspect_ratio)\n   1255         os.system('%s %s 2>/dev/null 1>/dev/null &'%\n(sage.misc.viewer.browser(), filename))\n   1256\n\n/Applications/sage/local/lib/python2.5/site-packages/sage/plot/plot.py\nin save(self, filename, xmin, xmax, ymin, ymax, figsize, figure, sub,\nsavenow, dpi, axes, axes_labels, fontsize, frame, verify,\naspect_ratio)\n   1429                 xmin,xmax,ymin,ymax = self._prepare_axes(xmin,\nxmax, ymin, ymax)\n   1430\n-> 1431                 xmin, xmax, ymin, ymax =\nsage_axes.add_xy_axes(subplot, xmin, xmax, ymin, ymax)\n   1432\n   1433                 subplot.set_xlim(xmin, xmax)\n\n/Applications/sage/local/lib/python2.5/site-packages/sage/plot/axes.py\nin add_xy_axes(self, subplot, xmin, xmax, ymin, ymax, axes, ticks,\naxesstyle, axes_labels)\n    324\n    325         #evalute find_axes for y values and x ticks\n--> 326         x_axis_ypos, ystep, ytslminor, ytslmajor =\nself._find_axes(ymin, ymax)\n    327         xltheight = 0.015*yspan\n    328         xstheight = 0.25*xltheight\n\n/Applications/sage/local/lib/python2.5/site-packages/sage/plot/axes.py\nin _find_axes(self, minval, maxval)\n    240             tslmajor, oppaxis, step =\nself._tasteless_ticks(minval, maxval, 10)\n    241         else:\n--> 242             tslmajor, oppaxis, step =\nself._tasteful_ticks(minval, maxval)\n    243         min = tslmajor[0] - step\n    244         tslminor = sage.misc.misc.srange(min, maxval +\n0.2*step, 0.2*step)\n\n/Applications/sage/local/lib/python2.5/site-packages/sage/plot/axes.py\nin _tasteful_ticks(self, minval, maxval)\n    124             else:\n    125                 if maxval >= 10:\n--> 126                     sl = [s for s in str(int(absmax))]\n    127                     d0 = eval(sl[0])\n    128                     d1 = eval(sl[1])\n\nOverflowError: cannot convert float infinity to long\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3907\n\n",
    "created_at": "2008-08-20T01:21:12Z",
    "labels": [
        "component: graphics",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.2",
    "title": "plot correctly up to asymptotes",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3907",
    "user": "https://github.com/kcrisman"
}
```
Assignee: @williamstein

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


Issue created by migration from https://trac.sagemath.org/ticket/3907





---

archive/issue_comments_027890.json:
```json
{
    "body": "Attachment [trac_3907.patch](tarball://root/attachments/some-uuid/ticket3907/trac_3907.patch) by @mwhansen created at 2008-08-29 00:02:54",
    "created_at": "2008-08-29T00:02:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3907",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3907#issuecomment-27890",
    "user": "https://github.com/mwhansen"
}
```

Attachment [trac_3907.patch](tarball://root/attachments/some-uuid/ticket3907/trac_3907.patch) by @mwhansen created at 2008-08-29 00:02:54



---

archive/issue_comments_027891.json:
```json
{
    "body": "Changing assignee from @williamstein to @mwhansen.",
    "created_at": "2008-08-29T00:04:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3907",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3907#issuecomment-27891",
    "user": "https://github.com/mwhansen"
}
```

Changing assignee from @williamstein to @mwhansen.



---

archive/issue_comments_027892.json:
```json
{
    "body": "I've attached a patch which fixes the big traceback you get and actually produces a plot.  This, however, does not fix the issue with the range on the y-axis being thrown of by asymptotes.  I think that should be a separate ticket.",
    "created_at": "2008-08-29T00:04:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3907",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3907#issuecomment-27892",
    "user": "https://github.com/mwhansen"
}
```

I've attached a patch which fixes the big traceback you get and actually produces a plot.  This, however, does not fix the issue with the range on the y-axis being thrown of by asymptotes.  I think that should be a separate ticket.



---

archive/issue_comments_027893.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-08-29T00:04:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3907",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3907#issuecomment-27893",
    "user": "https://github.com/mwhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_027894.json:
```json
{
    "body": "Replying to [comment:1 mhansen]:\n> I've attached a patch which fixes the big traceback you get and actually produces a plot.  This, however, does not fix the issue with the range on the y-axis being thrown of by asymptotes.  I think that should be a separate ticket.\n\nkcrisman opened a ticket for that at #3985 - at least it seems very close to what you suggest.\n\nCheers,\n\nMichael",
    "created_at": "2008-08-29T02:43:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3907",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3907#issuecomment-27894",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Replying to [comment:1 mhansen]:
> I've attached a patch which fixes the big traceback you get and actually produces a plot.  This, however, does not fix the issue with the range on the y-axis being thrown of by asymptotes.  I think that should be a separate ticket.

kcrisman opened a ticket for that at #3985 - at least it seems very close to what you suggest.

Cheers,

Michael



---

archive/issue_comments_027895.json:
```json
{
    "body": "Mostly looks good, but what about `-inf`?",
    "created_at": "2008-09-02T08:36:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3907",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3907#issuecomment-27895",
    "user": "https://github.com/robertwb"
}
```

Mostly looks good, but what about `-inf`?



---

archive/issue_comments_027896.json:
```json
{
    "body": "Attachment [trac_3907.2.patch](tarball://root/attachments/some-uuid/ticket3907/trac_3907.2.patch) by @mwhansen created at 2008-09-05 19:37:53\n\nI've updated the patch to handle the -inf case.",
    "created_at": "2008-09-05T19:37:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3907",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3907#issuecomment-27896",
    "user": "https://github.com/mwhansen"
}
```

Attachment [trac_3907.2.patch](tarball://root/attachments/some-uuid/ticket3907/trac_3907.2.patch) by @mwhansen created at 2008-09-05 19:37:53

I've updated the patch to handle the -inf case.



---

archive/issue_comments_027897.json:
```json
{
    "body": "Apply only the second patch- applies cleanly to sage-3.1.2.alpha3 and passes tests in the files it touches.",
    "created_at": "2008-09-05T19:43:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3907",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3907#issuecomment-27897",
    "user": "https://github.com/rlmill"
}
```

Apply only the second patch- applies cleanly to sage-3.1.2.alpha3 and passes tests in the files it touches.



---

archive/issue_comments_027898.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-09-06T00:07:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3907",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3907#issuecomment-27898",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_004134.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-09-06T00:07:53Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3907",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3907#event-4134"
}
```



---

archive/issue_comments_027899.json:
```json
{
    "body": "Merged in Sage 3.1.2.rc0",
    "created_at": "2008-09-06T00:07:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3907",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3907#issuecomment-27899",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.1.2.rc0
