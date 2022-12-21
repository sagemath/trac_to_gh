# Issue 6615: Small bug in Graph.plot()

Issue created by migration from Trac.

Original creator: ncohen

Original creation time: 2009-07-24 18:00:05

Assignee: rlm

It may take only two lines, but I do not know which ones (I got a bit lost reading graph_plot.py) and it may take half a second to who wrote it in the first place.

g=graphs.PetersenGraph()
g.plot(edge_colors={"red":[(0,1)]})
g.plot(vertex_colors={"red":[1]})

When you plot a graph and want some edges to have a different color, the first plot is perfect. In the second case, though, I think it would be better to assign the others vertices a default color ;-)


---

Comment by ncohen created at 2009-08-02 11:33:31

The best way to do that may be to let vertex_colors (resp. edge_colors) in Graph.plot() accept any partition of the vertices ( resp. edges ), and let it deal with rainbow to pick the colors. Obviously, it does not mean Graph.plot() should not also be able to support the current dictionary of (color, list)


---

Comment by ncohen created at 2009-08-14 17:31:08

All the vertices are colored even if vertex_colors did not contain colors for all of them. The first unused color in ranbow() is taken.

There was a small mistake in rgbcolor() where the hexcadecimal values were divided by 256 instead of 255 which lead to "red"!=(1,0,0).

All the colors were wrong and nobody noticed !! :-)


---

Comment by ncohen created at 2009-08-24 11:30:46

* Graphfunctions-1 has no reason for being here, but I can not delete it
   * patchplot has been updated, I had forgotten to commit the change from 256 to 255 in rgbcolor()


---

Comment by jason created at 2009-09-15 04:32:50

The edge color plot in the description works great.

The vertex color plot doesn't.  The specified vertex is red; the others disappeared!

Also, it would be great to include those two examples in the docs.


---

Comment by ncohen created at 2009-10-27 05:56:51

Hello Jason !! I sent you an email about this patch some time ago, as I did not understand where this patch failed... Did you get it ? :-)


---

Comment by rlm created at 2009-12-16 18:55:55

Patch works fine for me.


---

Comment by rlm created at 2009-12-16 18:55:55

Changing status from needs_work to needs_review.


---

Comment by rlm created at 2009-12-16 18:56:02

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2009-12-19 19:54:37

There are test failures in sage/plot/colors.py


---

Comment by mhansen created at 2009-12-19 19:54:37

Changing status from positive_review to needs_work.


---

Attachment

depends: sage-4.3.1.alpha1 + #7634


---

Comment by rlm created at 2010-01-06 16:35:48

Changing status from needs_work to needs_review.


---

Comment by rlm created at 2010-01-06 16:35:57

Changing status from needs_review to positive_review.


---

Comment by rlm created at 2010-01-13 05:38:58

Resolution: fixed
