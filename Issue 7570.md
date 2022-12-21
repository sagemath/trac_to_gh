# Issue 7570: default : list_plot of empty lists

Issue created by migration from Trac.

Original creator: chapoton

Original creation time: 2009-12-01 14:16:10

Assignee: was

CC:  jason ryan

Keywords: list_plot

list_plot does not accept *empty* lists:


```
list_plot([1],rgbcolor=(1,0,0))+list_plot([],rgbcolor=(0,0,1))

IndexError: list index out of range
```


does not work, whereas


```
list_plot([1],rgbcolor=(1,0,0))+list_plot([2],rgbcolor=(0,0,1))
```


does work. It would be nicer if list_plot of empty lists gives an empty graphics object.


---

Comment by kcrisman created at 2009-12-11 20:16:01

Incidentally, this is also true of things like point(), where an empty list of points yields an error (as far as I remember).  We should check ALL plot methods to ensure that empty input yields Graphics() or something like that, at least for the 2-d versions.  Changing summary appropriately.


---

Comment by jason created at 2010-05-26 15:40:56

Changing keywords from "list_plot" to "list_plot, beginner".


---

Attachment

make list_plot() and point() accept empty lists and return empty Graphics() object


---

Comment by ryan created at 2010-08-21 13:42:16

Changing status from new to needs_work.


---

Comment by ryan created at 2011-01-08 19:15:17

The patch was made against sage-4.6.0

It handles empty lists as input to arrow, line, point, and plot.

I'm not sure what other plotting functions would benefit from empty lists as input.


---

Comment by ryan created at 2011-01-08 19:15:17

Changing status from needs_work to needs_review.


---

Comment by gagansekhon created at 2011-01-08 20:06:21

Changing status from needs_review to needs_work.


---

Comment by gagansekhon created at 2011-01-08 20:06:21

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

Comment by jason created at 2011-01-08 22:34:34

Thanks for working on polishing these things!

One quick comment from just glancing at the patch: there is a typo that occurs twice in the patch: "returns and empty plot" (where "and" should be "an").


---

Comment by ryan created at 2011-01-08 23:29:03

funny...I can't reproduce this error on my local sage install.  However, on a remote sage install (i.e., sage.math), I get the error.  However, the error is triggered (I think) because the remote installation can't display graphics.

Try:
[[[
a = point([])
type(a)
]]]
a is of type sage.plot.plot.Graphics()


---

Comment by ryan created at 2011-01-08 23:30:05

Try: ` a = point([]) type(a) ` a is of type sage.plot.plot.Graphics


---

Comment by ryan created at 2011-01-08 23:48:56

1. fixed the typos
2. changed arrow2d a bit.


---

Comment by ryan created at 2011-01-08 23:48:56

Changing status from needs_work to needs_review.


---

Comment by ryan created at 2011-01-09 06:05:23

This latest patch now fixes the bug _actually_ described in the ticket :)


---

Comment by ryan created at 2011-01-09 06:12:47

added documentation


---

Attachment

The only test that didn't pass was ./sage -t devel/sage/sage/plot/arrow.py and I think it's only because you have line 412 in:

```
sage: arrow2d(headpoint=None, tailpoint) 
```



If you delete that line, the tests pass and everything looks good.


---

Comment by aly.deines created at 2011-01-09 20:25:29

This fixes the doctest.


---

Attachment


---

Comment by gagansekhon created at 2011-01-10 04:47:09

Changing status from needs_review to positive_review.


---

Comment by kcrisman created at 2011-01-10 14:00:23

Positive reviewer, can you add your (real) name to the reviewer list?


---

Comment by jdemeyer created at 2011-01-25 16:32:23

Please specify which patches have to be applied.


---

Comment by jdemeyer created at 2011-01-25 16:32:23

Changing status from positive_review to needs_info.


---

Comment by jdemeyer created at 2011-01-27 17:35:04

Changing status from needs_info to needs_review.


---

Comment by jdemeyer created at 2011-01-27 17:35:22

Changing status from needs_review to positive_review.


---

Comment by kcrisman created at 2011-01-27 17:40:59

I hate to do this, because I *really* want this in - just yesterday had to write all sorts of dumb if/then clauses to get around this.  But the commit message on the most recent patch is totally uninformative, and unfortunately I don't have time to fix that now.


---

Comment by kcrisman created at 2011-01-27 17:40:59

Changing status from positive_review to needs_work.


---

Comment by jdemeyer created at 2011-01-28 08:36:29

There is also a Sphinx error:

```
/mnt/usb1/scratch/jdemeyer/merger/sage-4.6.2.alpha3/local/lib/python2.6/site-packages/sage/plot/plot.py:docstring of sage.plot.plot:157: (ERROR/3) Unexpected indentation.
```



---

Comment by jdemeyer created at 2011-02-07 08:49:14

Can somebody please fix the trivial issues with this ticket?


---

Attachment

Use this patch only


---

Comment by kcrisman created at 2011-02-07 15:54:14

I think this fixes both issues, as well as corrects several 'emtpy' occurrences.


---

Comment by kcrisman created at 2011-02-07 15:54:14

Changing status from needs_work to needs_review.


---

Comment by kcrisman created at 2011-02-07 15:54:23

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2011-02-16 08:49:38

Resolution: fixed


---

Comment by jason created at 2011-09-11 03:08:15

There is a problem with the code on the final merged patch: why wasn't len()==0 used as a test?  The problem is illustrated here: http://groups.google.com/group/sage-support/browse_thread/thread/fb53b9d908acfb4

I've opened #11787 to correct this.
