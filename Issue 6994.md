# Issue 6994: [with spkg, needs review] upgrade matplotlib to 0.99.1

Issue created by migration from https://trac.sagemath.org/ticket/6994

Original creator: jason

Original creation time: 2009-09-22 19:44:25

Assignee: was

CC:  kcrisman

The new matplotlib fixes *lots* of bugs, and incorporates some of our patches upstream too.  The new spkg is:

http://sage.math.washington.edu/home/jason/matplotlib-0.99.1.spkg


---

Comment by jason created at 2009-09-22 19:48:57

Apparently 0.99.1 has a special osx makefile, which I don't think we are using.  Should we use it?


---

Comment by jason created at 2009-09-22 19:49:13

(if so, someone with osx ought to take a look at this)


---

Comment by kcrisman created at 2009-09-22 20:00:49

Hmm, well, it seems to be working fine on my copy of OSX.5.8.  Maybe someone else who knows something about makefiles should comment on this...

Maybe this would be a good time to improve that documentation about things like

```
sage: plot(x^3,-10,-1)
```

which almost looks like they should intersect but they don't... that's already a ticket somewhere.

Anyway, I don't have time to finish a review now, but so far everything looks fine, and as I said it built fine.


---

Comment by kcrisman created at 2009-09-22 20:37:21

I get the following failure, probably due to a deprecated module...

```
sage -t  "devel/sage/sage/plot/colors.py"                   
**********************************************************************
File "/Users/.../sage-4.1.2.alpha2/devel/sage/sage/plot/colors.py", line 193:
    sage: graphs.DodecahedralGraph().show(vertex_colors=vertex_colors)
Exception raised:
    Traceback (most recent call last):
<snip>
      File "/Users/.../sage-4.1.2.alpha2/local/lib/python/site-packages/matplotlib/backends/tkagg.py", line 1, in <module>
        import _tkagg
    ImportError: No module named _tkagg
*****************************************************************
```

Similar ones in plot.py in lines 213 ff. and around line 1960, as well as in scatterplot.py. 

There are also a couple failures in plot.py related to savefig and fig.  Otherwise everything seem okay.


---

Comment by jason created at 2009-09-22 22:44:50

Congratulations; you found a bug in the release of matplotlib.  They errantly included a config file that should have been deleted.

I've updated the spkg, at the same URL as above.  Make sure you install it with "sage -f" to overwrite the previous one.


---

Comment by kcrisman created at 2009-09-23 01:25:19

Okay, now all is well.  You may want to let Minh know about some of the bugfixes if they are notable for Sage, for the release tour.


---

Comment by mvngu created at 2009-09-27 04:05:03

See #7022 for a port to OS X 10.6.


---

Comment by mhansen created at 2009-10-15 09:41:56

I think that this should be closed now that #7022 is in.


---

Comment by mhansen created at 2009-10-15 09:41:56

Resolution: fixed
