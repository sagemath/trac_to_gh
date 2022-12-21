# Issue 6546: Fully implement edge thickness in plots of graphs

Issue created by migration from Trac.

Original creator: rbeezer

Original creation time: 2009-07-17 04:59:38

Assignee: rlm

CC:  slelievre

Keywords: plot graph edge width thickness

There is an option for specifying the thickness/width of an edge in a graph ("thickness").  For a graph `G`

`G.plot(thickness=10)`

works as expected, but

`show(G, thickness=10)`

raises an error about the option name being unrecognized.

Also, I couldn't find any mention of this parameter in the documentation anywhere.


---

Comment by rbeezer created at 2013-11-01 04:33:03

It would seem this has gone backwards.  Now `.plot()` complains about not understanding `thickness`.  Drawing a (graphics primitive) `line` understands `thickness`.  So it should be a matter of making `thickness` a valid option of a graph plot and passing it to `matplotlib` in `graphs/graph_plot.py` when drawing (straight) edges.  Maybe curved edges would be just as easy?


---

Comment by ppurka created at 2014-06-22 14:49:30

A preliminary patch is attached. Just wanted to get an implementation out there, so that others can look at it or enhance it.
----
New commits:


---

Comment by slelievre created at 2018-04-20 15:35:22

See also #20035, #21540.
