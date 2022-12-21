# Issue 1869: Implement show(list(graphs(n))) et al

Issue created by migration from Trac.

Original creator: rlm

Original creation time: 2008-01-20 20:35:34

Assignee: rlm

`show` is in `sage/misc/functional.py`. It should be easy to get graphs_list functionality in there, if it applies.


---

Comment by rlm created at 2008-01-20 20:35:41

Changing status from new to assigned.


---

Attachment


---

Comment by jason created at 2008-01-23 23:05:44

Very nice functionality!

Three things:

  * Could we pass the width and height of the grid as parameters?  something like {{{
sage: show(graphs(5),width=3,height=3)
# Displays 3x3 pages of the graphs
}}}
  * Why limit this to graphs?  Why not have a list trigger a default rendering as a rectangular array, where each item is drawn with "show(list[i])"  Hmmm...then nested lists would even work and display nicely.
  * `show(graphs(1))` gives an image with space for 4 graphs, but only the one result is displayed.  Can we make the image narrower?

I think this patch is a great start.


---

Comment by mabshoff created at 2008-01-24 00:08:48

Resolution: fixed


---

Comment by mabshoff created at 2008-01-24 00:08:48

Merged in Sage 2.10.1.alpha2
