# Issue 7570: default : list_plot of empty lists

archive/issues_007570.json:
```json
{
    "body": "Assignee: was\n\nCC:  jason ryan\n\nKeywords: list_plot\n\nlist_plot does not accept **empty** lists:\n\n\n```\nlist_plot([1],rgbcolor=(1,0,0))+list_plot([],rgbcolor=(0,0,1))\n\nIndexError: list index out of range\n```\n\n\ndoes not work, whereas\n\n\n```\nlist_plot([1],rgbcolor=(1,0,0))+list_plot([2],rgbcolor=(0,0,1))\n```\n\n\ndoes work. It would be nicer if list_plot of empty lists gives an empty graphics object.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7570\n\n",
    "created_at": "2009-12-01T14:16:10Z",
    "labels": [
        "graphics",
        "minor",
        "bug"
    ],
    "title": "default : list_plot of empty lists",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7570",
    "user": "chapoton"
}
```
Assignee: was

CC:  jason ryan

Keywords: list_plot

list_plot does not accept **empty** lists:


```
list_plot([1],rgbcolor=(1,0,0))+list_plot([],rgbcolor=(0,0,1))

IndexError: list index out of range
```


does not work, whereas


```
list_plot([1],rgbcolor=(1,0,0))+list_plot([2],rgbcolor=(0,0,1))
```


does work. It would be nicer if list_plot of empty lists gives an empty graphics object.

Issue created by migration from https://trac.sagemath.org/ticket/7570





---

archive/issue_comments_064407.json:
```json
{
    "body": "Incidentally, this is also true of things like point(), where an empty list of points yields an error (as far as I remember).  We should check ALL plot methods to ensure that empty input yields Graphics() or something like that, at least for the 2-d versions.  Changing summary appropriately.",
    "created_at": "2009-12-11T20:16:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7570",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7570#issuecomment-64407",
    "user": "kcrisman"
}
```

Incidentally, this is also true of things like point(), where an empty list of points yields an error (as far as I remember).  We should check ALL plot methods to ensure that empty input yields Graphics() or something like that, at least for the 2-d versions.  Changing summary appropriately.



---

archive/issue_comments_064408.json:
```json
{
    "body": "Changing keywords from \"list_plot\" to \"list_plot, beginner\".",
    "created_at": "2010-05-26T15:40:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7570",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7570#issuecomment-64408",
    "user": "jason"
}
```

Changing keywords from "list_plot" to "list_plot, beginner".



---

archive/issue_comments_064409.json:
```json
{
    "body": "Attachment\n\nmake list_plot() and point() accept empty lists and return empty Graphics() object",
    "created_at": "2010-08-21T13:40:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7570",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7570#issuecomment-64409",
    "user": "ryan"
}
```

Attachment

make list_plot() and point() accept empty lists and return empty Graphics() object



---

archive/issue_comments_064410.json:
```json
{
    "body": "Changing status from new to needs_work.",
    "created_at": "2010-08-21T13:42:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7570",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7570#issuecomment-64410",
    "user": "ryan"
}
```

Changing status from new to needs_work.



---

archive/issue_comments_064411.json:
```json
{
    "body": "The patch was made against sage-4.6.0\n\nIt handles empty lists as input to arrow, line, point, and plot.\n\nI'm not sure what other plotting functions would benefit from empty lists as input.",
    "created_at": "2011-01-08T19:15:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7570",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7570#issuecomment-64411",
    "user": "ryan"
}
```

The patch was made against sage-4.6.0

It handles empty lists as input to arrow, line, point, and plot.

I'm not sure what other plotting functions would benefit from empty lists as input.



---

archive/issue_comments_064412.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-01-08T19:15:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7570",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7570#issuecomment-64412",
    "user": "ryan"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_064413.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2011-01-08T20:06:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7570",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7570#issuecomment-64413",
    "user": "gagansekhon"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_064414.json:
```json
{
    "body": "sage/plot/point.py fails. \n\nWhen I passed an empty list I got an error. \n\nsage: point([])\nERROR: An unexpected error occurred while tokenizing input\nThe following traceback may be corrupted or invalid\nThe error message is: ('EOF in multi-line statement', (273, 0))\n\n---------------------------------------------------------------------------\nValueError                                Traceback (most recent call last)\n\n/Applications/sage4.6/devel/sage-main/<ipython console> in <module>()\n\n/Applications/sage4.6/local/lib/python2.6/site-packages/IPython/Prompts.pyc in __call__(self, arg)\n    549 \n    550             # and now call a possibly user-defined print mechanism\n--> 551             manipulated_val = self.display(arg)\n    552             \n    553             # user display hooks can change the variable to be stored in\n\n/Applications/sage4.6/local/lib/python2.6/site-packages/IPython/Prompts.pyc in _display(self, arg)\n    575             return IPython.generics.result_display(arg)\n    576         except TryNext:            \n--> 577             return self.shell.hooks.result_display(arg)\n    578 \n    579     # Assign the default display method:\n\n/Applications/sage4.6/local/lib/python2.6/site-packages/IPython/hooks.pyc in __call__(self, *args, **kw)\n    139             #print \"prio\",prio,\"cmd\",cmd #dbg\n    140             try:\n--> 141                 ret = cmd(*args, **kw)\n    142                 return ret\n    143             except ipapi.TryNext, exc:\n\n/Applications/sage4.6/local/lib/python2.6/site-packages/sage/misc/displayhook.pyc in result_display(ip_self, obj)\n    148     # IPython's default result_display() uses the IPython.genutils.Term.cout stream.\n    149     # See also local/lib/python2.6/site-packages/IPython/hooks.py.\n--> 150     print_obj(IPython.genutils.Term.cout, obj)\n    151 \n    152 def displayhook(obj):\n\n/Applications/sage4.6/local/lib/python2.6/site-packages/sage/misc/displayhook.pyc in print_obj(out_stream, obj)\n    140             if _check_tall_list_and_print(out_stream, obj):\n    141                 return\n--> 142     print >>out_stream, `obj`\n    143 \n    144 def result_display(ip_self, obj):\n\n/Applications/sage4.6/local/lib/python2.6/site-packages/sage/structure/sage_object.so in sage.structure.sage_object.SageObject.__repr__ (sage/structure/sage_object.c:1341)()\n\n/Applications/sage4.6/local/lib/python2.6/site-packages/sage/plot/plot.pyc in _repr_(self)\n   1078         \"\"\"\n   1079         if SHOW_DEFAULT:\n-> 1080             self.show()\n   1081             return ''\n   1082         else:\n\n/Applications/sage4.6/local/lib/python2.6/site-packages/sage/plot/misc.pyc in wrapper(*args, **kwds)\n     82             kwds[self.name + \"options\"] = suboptions\n     83 \n---> 84             return func(*args, **kwds)\n     85 \n     86         from sage.misc.sageinspect import sage_getsource\n\n/Applications/sage4.6/local/lib/python2.6/site-packages/sage/plot/plot.pyc in show(self, **kwds)\n   1737             if options['filename'] is None:\n   1738                 options['filename'] = sage.misc.misc.tmp_filename() + '.png'\n-> 1739             self.save(**options)\n   1740             os.system('%s %s 2>/dev/null 1>/dev/null &' % \\\n   1741                 (sage.misc.viewer.browser(), options['filename']))\n\n/Applications/sage4.6/local/lib/python2.6/site-packages/sage/plot/plot.pyc in save(self, filename, dpi, savenow, *args, **kwds)\n   2386             options=dict()\n   2387             options['transparent']=kwds.pop('transparent',False)\n-> 2388             figure=self.matplotlib(*args, **kwds)\n   2389             # You can output in PNG, PS, EPS, PDF, or SVG format, depending on the file extension. \n   2390             # matplotlib looks at the file extension to see what the renderer should be.\n\n/Applications/sage4.6/local/lib/python2.6/site-packages/sage/plot/plot.pyc in matplotlib(self, filename, xmin, xmax, ymin, ymax, figsize, figure, sub, axes, axes_labels, fontsize, frame, verify, aspect_ratio, gridlines, gridlinesstyle, vgridlinesstyle, hgridlinesstyle, show_legend, legend_options, axes_pad, ticks_integer, tick_formatter, ticks)\n   1954         #add all the primitives to the subplot\n   1955         for g in self.__objects:\n-> 1956             g._render_on_subplot(subplot)\n   1957         \n   1958         #add the legend if requested\n\n/Applications/sage4.6/local/lib/python2.6/site-packages/sage/plot/point.pyc in _render_on_subplot(self, subplot)\n    271         scatteroptions={}\n    272         if not faceted: scatteroptions['edgecolors'] = 'none'\n--> 273         subplot.scatter(self.xdata, self.ydata, s=s, c=c, alpha=a, zorder=z, label=options['legend_label'], **scatteroptions)\n    274         \n    275 \n\n/Applications/sage4.6/local/lib/python2.6/site-packages/matplotlib/axes.pyc in scatter(self, x, y, s, c, marker, cmap, norm, vmin, vmax, alpha, linewidths, faceted, verts, **kwargs)\n   5811         temp_y = y\n   5812 \n-> 5813         minx = np.amin(temp_x)\n   5814         maxx = np.amax(temp_x)\n   5815         miny = np.amin(temp_y)\n\n/Applications/sage4.6/local/lib/python2.6/site-packages/numpy/core/fromnumeric.pyc in amin(a, axis, out)\n   1641     except AttributeError:\n   1642         return _wrapit(a, 'min', axis, out)\n-> 1643     return amin(axis, out)\n   1644 \n   1645 \n\nValueError: zero-size array to ufunc.reduce without identity",
    "created_at": "2011-01-08T20:06:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7570",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7570#issuecomment-64414",
    "user": "gagansekhon"
}
```

sage/plot/point.py fails. 

When I passed an empty list I got an error. 

sage: point([])
ERROR: An unexpected error occurred while tokenizing input
The following traceback may be corrupted or invalid
The error message is: ('EOF in multi-line statement', (273, 0))

---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)

/Applications/sage4.6/devel/sage-main/<ipython console> in <module>()

/Applications/sage4.6/local/lib/python2.6/site-packages/IPython/Prompts.pyc in __call__(self, arg)
    549 
    550             # and now call a possibly user-defined print mechanism
--> 551             manipulated_val = self.display(arg)
    552             
    553             # user display hooks can change the variable to be stored in

/Applications/sage4.6/local/lib/python2.6/site-packages/IPython/Prompts.pyc in _display(self, arg)
    575             return IPython.generics.result_display(arg)
    576         except TryNext:            
--> 577             return self.shell.hooks.result_display(arg)
    578 
    579     # Assign the default display method:

/Applications/sage4.6/local/lib/python2.6/site-packages/IPython/hooks.pyc in __call__(self, *args, **kw)
    139             #print "prio",prio,"cmd",cmd #dbg
    140             try:
--> 141                 ret = cmd(*args, **kw)
    142                 return ret
    143             except ipapi.TryNext, exc:

/Applications/sage4.6/local/lib/python2.6/site-packages/sage/misc/displayhook.pyc in result_display(ip_self, obj)
    148     # IPython's default result_display() uses the IPython.genutils.Term.cout stream.
    149     # See also local/lib/python2.6/site-packages/IPython/hooks.py.
--> 150     print_obj(IPython.genutils.Term.cout, obj)
    151 
    152 def displayhook(obj):

/Applications/sage4.6/local/lib/python2.6/site-packages/sage/misc/displayhook.pyc in print_obj(out_stream, obj)
    140             if _check_tall_list_and_print(out_stream, obj):
    141                 return
--> 142     print >>out_stream, `obj`
    143 
    144 def result_display(ip_self, obj):

/Applications/sage4.6/local/lib/python2.6/site-packages/sage/structure/sage_object.so in sage.structure.sage_object.SageObject.__repr__ (sage/structure/sage_object.c:1341)()

/Applications/sage4.6/local/lib/python2.6/site-packages/sage/plot/plot.pyc in _repr_(self)
   1078         """
   1079         if SHOW_DEFAULT:
-> 1080             self.show()
   1081             return ''
   1082         else:

/Applications/sage4.6/local/lib/python2.6/site-packages/sage/plot/misc.pyc in wrapper(*args, **kwds)
     82             kwds[self.name + "options"] = suboptions
     83 
---> 84             return func(*args, **kwds)
     85 
     86         from sage.misc.sageinspect import sage_getsource

/Applications/sage4.6/local/lib/python2.6/site-packages/sage/plot/plot.pyc in show(self, **kwds)
   1737             if options['filename'] is None:
   1738                 options['filename'] = sage.misc.misc.tmp_filename() + '.png'
-> 1739             self.save(**options)
   1740             os.system('%s %s 2>/dev/null 1>/dev/null &' % \
   1741                 (sage.misc.viewer.browser(), options['filename']))

/Applications/sage4.6/local/lib/python2.6/site-packages/sage/plot/plot.pyc in save(self, filename, dpi, savenow, *args, **kwds)
   2386             options=dict()
   2387             options['transparent']=kwds.pop('transparent',False)
-> 2388             figure=self.matplotlib(*args, **kwds)
   2389             # You can output in PNG, PS, EPS, PDF, or SVG format, depending on the file extension. 
   2390             # matplotlib looks at the file extension to see what the renderer should be.

/Applications/sage4.6/local/lib/python2.6/site-packages/sage/plot/plot.pyc in matplotlib(self, filename, xmin, xmax, ymin, ymax, figsize, figure, sub, axes, axes_labels, fontsize, frame, verify, aspect_ratio, gridlines, gridlinesstyle, vgridlinesstyle, hgridlinesstyle, show_legend, legend_options, axes_pad, ticks_integer, tick_formatter, ticks)
   1954         #add all the primitives to the subplot
   1955         for g in self.__objects:
-> 1956             g._render_on_subplot(subplot)
   1957         
   1958         #add the legend if requested

/Applications/sage4.6/local/lib/python2.6/site-packages/sage/plot/point.pyc in _render_on_subplot(self, subplot)
    271         scatteroptions={}
    272         if not faceted: scatteroptions['edgecolors'] = 'none'
--> 273         subplot.scatter(self.xdata, self.ydata, s=s, c=c, alpha=a, zorder=z, label=options['legend_label'], **scatteroptions)
    274         
    275 

/Applications/sage4.6/local/lib/python2.6/site-packages/matplotlib/axes.pyc in scatter(self, x, y, s, c, marker, cmap, norm, vmin, vmax, alpha, linewidths, faceted, verts, **kwargs)
   5811         temp_y = y
   5812 
-> 5813         minx = np.amin(temp_x)
   5814         maxx = np.amax(temp_x)
   5815         miny = np.amin(temp_y)

/Applications/sage4.6/local/lib/python2.6/site-packages/numpy/core/fromnumeric.pyc in amin(a, axis, out)
   1641     except AttributeError:
   1642         return _wrapit(a, 'min', axis, out)
-> 1643     return amin(axis, out)
   1644 
   1645 

ValueError: zero-size array to ufunc.reduce without identity



---

archive/issue_comments_064415.json:
```json
{
    "body": "Thanks for working on polishing these things!\n\nOne quick comment from just glancing at the patch: there is a typo that occurs twice in the patch: \"returns and empty plot\" (where \"and\" should be \"an\").",
    "created_at": "2011-01-08T22:34:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7570",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7570#issuecomment-64415",
    "user": "jason"
}
```

Thanks for working on polishing these things!

One quick comment from just glancing at the patch: there is a typo that occurs twice in the patch: "returns and empty plot" (where "and" should be "an").



---

archive/issue_comments_064416.json:
```json
{
    "body": "funny...I can't reproduce this error on my local sage install.  However, on a remote sage install (i.e., sage.math), I get the error.  However, the error is triggered (I think) because the remote installation can't display graphics.\n\nTry:\n[[[\na = point([])\ntype(a)\n]]]\na is of type sage.plot.plot.Graphics()",
    "created_at": "2011-01-08T23:29:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7570",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7570#issuecomment-64416",
    "user": "ryan"
}
```

funny...I can't reproduce this error on my local sage install.  However, on a remote sage install (i.e., sage.math), I get the error.  However, the error is triggered (I think) because the remote installation can't display graphics.

Try:
[[[
a = point([])
type(a)
]]]
a is of type sage.plot.plot.Graphics()



---

archive/issue_comments_064417.json:
```json
{
    "body": "Try: ` a = point([]) type(a) ` a is of type sage.plot.plot.Graphics",
    "created_at": "2011-01-08T23:30:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7570",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7570#issuecomment-64417",
    "user": "ryan"
}
```

Try: ` a = point([]) type(a) ` a is of type sage.plot.plot.Graphics



---

archive/issue_comments_064418.json:
```json
{
    "body": "1. fixed the typos\n2. changed arrow2d a bit.",
    "created_at": "2011-01-08T23:48:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7570",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7570#issuecomment-64418",
    "user": "ryan"
}
```

1. fixed the typos
2. changed arrow2d a bit.



---

archive/issue_comments_064419.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-01-08T23:48:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7570",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7570#issuecomment-64419",
    "user": "ryan"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_064420.json:
```json
{
    "body": "This latest patch now fixes the bug _actually_ described in the ticket :)",
    "created_at": "2011-01-09T06:05:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7570",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7570#issuecomment-64420",
    "user": "ryan"
}
```

This latest patch now fixes the bug _actually_ described in the ticket :)



---

archive/issue_comments_064421.json:
```json
{
    "body": "added documentation",
    "created_at": "2011-01-09T06:12:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7570",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7570#issuecomment-64421",
    "user": "ryan"
}
```

added documentation



---

archive/issue_comments_064422.json:
```json
{
    "body": "Attachment\n\nThe only test that didn't pass was ./sage -t devel/sage/sage/plot/arrow.py and I think it's only because you have line 412 in:\n\n```\nsage: arrow2d(headpoint=None, tailpoint) \n```\n\n\n\nIf you delete that line, the tests pass and everything looks good.",
    "created_at": "2011-01-09T20:19:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7570",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7570#issuecomment-64422",
    "user": "aly.deines"
}
```

Attachment

The only test that didn't pass was ./sage -t devel/sage/sage/plot/arrow.py and I think it's only because you have line 412 in:

```
sage: arrow2d(headpoint=None, tailpoint) 
```



If you delete that line, the tests pass and everything looks good.



---

archive/issue_comments_064423.json:
```json
{
    "body": "This fixes the doctest.",
    "created_at": "2011-01-09T20:25:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7570",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7570#issuecomment-64423",
    "user": "aly.deines"
}
```

This fixes the doctest.



---

archive/issue_comments_064424.json:
```json
{
    "body": "Attachment",
    "created_at": "2011-01-10T04:47:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7570",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7570#issuecomment-64424",
    "user": "gagansekhon"
}
```

Attachment



---

archive/issue_comments_064425.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-01-10T04:47:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7570",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7570#issuecomment-64425",
    "user": "gagansekhon"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_064426.json:
```json
{
    "body": "Positive reviewer, can you add your (real) name to the reviewer list?",
    "created_at": "2011-01-10T14:00:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7570",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7570#issuecomment-64426",
    "user": "kcrisman"
}
```

Positive reviewer, can you add your (real) name to the reviewer list?



---

archive/issue_comments_064427.json:
```json
{
    "body": "Please specify which patches have to be applied.",
    "created_at": "2011-01-25T16:32:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7570",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7570#issuecomment-64427",
    "user": "jdemeyer"
}
```

Please specify which patches have to be applied.



---

archive/issue_comments_064428.json:
```json
{
    "body": "Changing status from positive_review to needs_info.",
    "created_at": "2011-01-25T16:32:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7570",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7570#issuecomment-64428",
    "user": "jdemeyer"
}
```

Changing status from positive_review to needs_info.



---

archive/issue_comments_064429.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2011-01-27T17:35:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7570",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7570#issuecomment-64429",
    "user": "jdemeyer"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_064430.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-01-27T17:35:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7570",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7570#issuecomment-64430",
    "user": "jdemeyer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_064431.json:
```json
{
    "body": "I hate to do this, because I *really* want this in - just yesterday had to write all sorts of dumb if/then clauses to get around this.  But the commit message on the most recent patch is totally uninformative, and unfortunately I don't have time to fix that now.",
    "created_at": "2011-01-27T17:40:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7570",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7570#issuecomment-64431",
    "user": "kcrisman"
}
```

I hate to do this, because I *really* want this in - just yesterday had to write all sorts of dumb if/then clauses to get around this.  But the commit message on the most recent patch is totally uninformative, and unfortunately I don't have time to fix that now.



---

archive/issue_comments_064432.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2011-01-27T17:40:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7570",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7570#issuecomment-64432",
    "user": "kcrisman"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_064433.json:
```json
{
    "body": "There is also a Sphinx error:\n\n```\n/mnt/usb1/scratch/jdemeyer/merger/sage-4.6.2.alpha3/local/lib/python2.6/site-packages/sage/plot/plot.py:docstring of sage.plot.plot:157: (ERROR/3) Unexpected indentation.\n```\n",
    "created_at": "2011-01-28T08:36:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7570",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7570#issuecomment-64433",
    "user": "jdemeyer"
}
```

There is also a Sphinx error:

```
/mnt/usb1/scratch/jdemeyer/merger/sage-4.6.2.alpha3/local/lib/python2.6/site-packages/sage/plot/plot.py:docstring of sage.plot.plot:157: (ERROR/3) Unexpected indentation.
```




---

archive/issue_comments_064434.json:
```json
{
    "body": "Can somebody please fix the trivial issues with this ticket?",
    "created_at": "2011-02-07T08:49:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7570",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7570#issuecomment-64434",
    "user": "jdemeyer"
}
```

Can somebody please fix the trivial issues with this ticket?



---

archive/issue_comments_064435.json:
```json
{
    "body": "Attachment\n\nUse this patch only",
    "created_at": "2011-02-07T15:53:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7570",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7570#issuecomment-64435",
    "user": "kcrisman"
}
```

Attachment

Use this patch only



---

archive/issue_comments_064436.json:
```json
{
    "body": "I think this fixes both issues, as well as corrects several 'emtpy' occurrences.",
    "created_at": "2011-02-07T15:54:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7570",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7570#issuecomment-64436",
    "user": "kcrisman"
}
```

I think this fixes both issues, as well as corrects several 'emtpy' occurrences.



---

archive/issue_comments_064437.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-02-07T15:54:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7570",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7570#issuecomment-64437",
    "user": "kcrisman"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_064438.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-02-07T15:54:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7570",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7570#issuecomment-64438",
    "user": "kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_064439.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-02-16T08:49:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7570",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7570#issuecomment-64439",
    "user": "jdemeyer"
}
```

Resolution: fixed



---

archive/issue_comments_064440.json:
```json
{
    "body": "There is a problem with the code on the final merged patch: why wasn't len()==0 used as a test?  The problem is illustrated here: http://groups.google.com/group/sage-support/browse_thread/thread/fb53b9d908acfb4\n\nI've opened #11787 to correct this.",
    "created_at": "2011-09-11T03:08:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7570",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7570#issuecomment-64440",
    "user": "jason"
}
```

There is a problem with the code on the final merged patch: why wasn't len()==0 used as a test?  The problem is illustrated here: http://groups.google.com/group/sage-support/browse_thread/thread/fb53b9d908acfb4

I've opened #11787 to correct this.
