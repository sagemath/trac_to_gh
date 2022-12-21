# Issue 5938: graph plotting -- ploting of graphs (networks) is somehow messed up/scaled wrong/cropped wrong since it doesn't work with graphics_array

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-04-29 16:11:45

Assignee: rlm

Want to see some truly hideous plotting output?  Try this:


```
Q = GraphQuery(display_cols=['graph6','num_vertices','degree_sequence'],num_edges=['<=',5],min_degree=1)

v = Q.get_graphs_list(); v

graphics_array([g.plot() for g in v], 3, len(v)//3).show()
```


I guess the problem is maybe Networkx drawing the plots instead of Sage (??), hence the cropping/layout is wrong?  I don't know.  Why do we use networkx at all for any part of plotting?  It would be better to plot to native Sage primitives, wouldn't it?

Fix?  make it so the edges aren't cropped wrong.


---

Comment by was created at 2009-04-29 16:13:39

Even this (following the above example), results in hideous mis-cropped plots, and it doesn't use graphics array at all:

```
for g in v[:5]:
    show(g,figsize=2)
```



---

Comment by was created at 2009-04-29 16:14:12

And even this results in bits being chopped off that shouldn't be!

```
for g in v[:5]:
    show(g)
```



---

Comment by ekirkman created at 2009-05-18 21:11:31

I'm still working on this, but I have some updates.  It looks like the first problem is the buffer size on scatter_plot.  It's including the points, but not the vertex radius of the outermost points.  That should be simple enough to fix, but then I'll also look at some auto-scaling to make the graphics_array a little nicer.  I also feel like the graphs_list module had some nice parameters for graphics_arrays of graphs, but they might be outdated now that graph plotting is native in Sage.  I'll check into that too though.


---

Comment by jason created at 2009-11-03 02:55:22

See http://groups.google.com/group/sage-support/browse_thread/thread/274d540f783603e7/e43c031f36672d85


---

Comment by was created at 2010-08-10 00:37:29

<vent>
THIS SUCKS!!!!!!!!!!!

I can't believe how annoying it is that plotting graphs is still so totally and completely broken.  It is really, really horrible.  I don't know how anybody can stand this. 

Frickin' a.   Every single graph plot I try has the borders chopped off.  E.g.,


```
sage: Q = GraphQuery(display_cols=['graph6','num_vertices','degree_sequence'], num_edges=['<=',5],min_degree=1)
sage: Q.show(with_picture=True)
[This is the Trac macro *hideous pain* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#hideous pain-macro)
```



---

Comment by rlm created at 2010-08-10 00:44:20

Fix it!


---

Comment by rlm created at 2010-08-10 00:44:52

Warning- I've seen several "fixes" for this go in, and yet it's still borken


---

Comment by jason created at 2010-08-10 07:23:46

See #9211 for progress towards a fix.


---

Comment by jason created at 2011-12-21 13:38:58

Graph vertices are not cut off anymore.  The plot in the description has overlapping vertices, though.


---

Comment by jason created at 2011-12-21 13:38:58

Changing status from new to needs_review.


---

Comment by jason created at 2011-12-21 13:41:14

Changing status from needs_review to positive_review.


---

Comment by jason created at 2011-12-21 13:41:14

This is a dup of #9211.  Since the patch is there, and it is already merged, I'm calling this the duplicate.


---

Comment by jdemeyer created at 2012-01-05 13:34:15

Resolution: duplicate
