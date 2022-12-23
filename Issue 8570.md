# Issue 8570: Allow "marker" option to be passed to matplotlib on list_plot() and point()

Issue created by migration from https://trac.sagemath.org/ticket/8570

Original creator: ronanpaixao

Original creation time: 2010-03-21 15:17:23

Assignee: was

CC:  jason kcrisman

Keywords: plot marker

Currently, there's no obvious way to pass the marker option to matplotlib when plotting individual points, which would be mostly with this option.

It appears that plot() has deviated from other plot types, since it does allow the marker option, but apparently only for function plots.

using plot(points(point_list),marker='x') ignores the marker option
using list_plot(point_list,marker='x') or points(point_list,marker='x') gives a warning:
  verbose 0 (136: primitive.py, options) WARNING: Ignoring option 'marker'=x
but displays the points nevertheless, though ignoring the marker option.

Also, setting plot.options['marker'] = 'x' or Graphics().SHOW_OPTIONS['marker'] = 'x' do not work.

Somewhat related to #4529, #1431 and #5448, which seem to be related to not passing kwargs to matplotlib.

So far, I haven't been able to find a way to seamless join matplotlib's system with the sage.plot options.



---

Comment by jason created at 2010-06-04 04:34:53

I think it would be a good design decision to just bundle the plotjoined=True features in with line() (i.e., eliminate the plotjoined=True features in listplot, and just make listplot about plotting points).


---

Comment by jason created at 2010-06-04 04:55:46

In fact, I think a better design decision would be to completely deprecate list_plot.  Replace it with line() in the connected case, and scatter_plot in the disconnected case.  Each of those commands does better than list_plot.


---

Comment by jason created at 2010-06-04 05:06:56

For that matter, the listplot3d should maybe be called surface_plot() instead, as it is clearer what it is plotting.


---

Comment by jason created at 2010-06-05 00:53:00

Another reason for the deprecation: I think every other graphics command is named after the *output* (like "line"), not the *input* (like "list_plot")


---

Comment by jason created at 2010-06-05 19:48:26

In fact, scatter_plot should be deprecated in favor of just points().  If we do that, then we need to make points() have more options (like edgecolor, markerstyle, etc.).


---

Comment by jason created at 2010-06-05 19:48:41

Changing type from defect to enhancement.


---

Comment by kcrisman created at 2012-01-25 03:46:14

Just noting that this is still really unfortunate.  Here is a workaround in the meantime for getting markers.

```
line([(1,2),(2,3)],marker=7,linestyle='')
```



---

Comment by kcrisman created at 2012-12-14 16:22:33

Incidentally, I think the `list_plot` syntax in 2 and 3 dims is because Mma uses this, right?  We'd need a deprecation period or to keep the alias.

See also #13830.
