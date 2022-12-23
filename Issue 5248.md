# Issue 5248: edge_colors does not work on loops

Issue created by migration from https://trac.sagemath.org/ticket/5248

Original creator: mhampton

Original creation time: 2009-02-12 16:53:34

Assignee: rlm

Keywords: graphs

The following example illustrates the problem.  Loops are treated seperately, and not correctly colored (they are always black).


```
g = graphs.CompleteGraph(3)
g.loops(True)
g.add_edge(0,0)
c_dict = {"red":[(0,0)], "blue":[(0,1),(1,2),(0,2)]}
show(g.plot(edge_colors = c_dict))
```



---

Comment by rlm created at 2009-02-12 17:34:13

Ticket #3541 is going to contain an overhaul of the graph plotting code. Since I'm refereeing, I'll make sure that this is fixed in that patch.


---

Comment by mabshoff created at 2009-02-14 02:59:25

This ticket will be fixed by #3541, so let's move it to 3.3.

Cheers,

Michael


---

Comment by ekirkman created at 2009-02-14 03:48:19

This is now fixed by #3541.  Cheers.


---

Comment by ekirkman created at 2009-02-14 03:48:19

Resolution: duplicate
