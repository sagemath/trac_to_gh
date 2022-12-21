# Issue 5914: default edge color is *invisible*

Issue created by migration from Trac.

Original creator: rlm

Original creation time: 2009-04-27 19:06:21

Assignee: rlm

If you do

sage: G = graphs.CompleteGraph(5)
sage: G.show(edge_colors={'red':(0,1)})

what you get is one red edge...

The default color should be black.


---

Comment by jason created at 2009-04-27 19:08:19

vertex_colors might also suffer from the same problem...


---

Attachment

Quick remark: If you do 

```
sage: G = graphs.CompleteGraph(5)
sage: G.show(edge_colors={'red':(0,1)})
```

as you put in the ticket description, you get an error.  The proper input is:

```
sage: G = graphs.CompleteGraph(5)
sage: G.show(edge_colors={'red':[(0,1)]})
```


This patch works fine.


---

Comment by mabshoff created at 2009-04-30 02:40:15

Resolution: fixed


---

Comment by mabshoff created at 2009-04-30 02:40:15

Merged in Sage 3.4.2.rc0.

Cheers,

Michael
