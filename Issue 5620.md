# Issue 5620: Digraph plotting bug

Issue created by migration from https://trac.sagemath.org/ticket/5620

Original creator: ekirkman

Original creation time: 2009-03-27 22:34:49

Assignee: ekirkman

Pointed out by rlm-- digraphs can have two paths between a pair of vertices without being multiple edged graphs.  So the graph

```
sage: G = DiGraph({1:{2: 'h'}, 2:{1:'g'}})
```

is drawn with only one straight-line arrow even though there are two edges.  Basically, this will just require a quick check for this case and then treating such a graph the same as a multidigraph.

Also, need to update multiple_edges and loops function calls in graph_plot.py to match the new function definitions has_multiple_edges and has_loops in graph.py

Pretty straightforward stuff... I should have a patch up in 3, 2, 1...


---

Comment by ekirkman created at 2009-03-27 23:05:32

I am also working on a straight-line alternative...  I'll put that one up shortly.


---

Comment by ekirkman created at 2009-03-28 02:16:54

So the straight line version turned out to be kind of hokey-looking, which is what I was afraid of.  But I was able to clean up the original fix so it's not so costly to run for large directed graphs.  So the patch that should be reviewed is trac5620_digraph_plotting.patch and the alternative option can be ignored.  I am leaving the alt patch up for now, to see if there's any feedback about whether it should be a non-default display option.  Also, I'm attaching pictures from executing

```
sage: G = DiGraph({1:{2: 'h', 4:'j'}, 2:{1:'g'}, 3:{1:'a', 2:'b'}, 4:{1:'f'}})
sage: G.show(color_by_label=True, edge_labels=True)
```

in each version.


---

Comment by ekirkman created at 2009-03-28 02:34:39

Changing assignee from ekirkman to rlm.


---

Comment by rlm created at 2009-03-31 23:14:29

Reviewer patch to original


---

Attachment


---

Comment by mabshoff created at 2009-04-01 00:46:13

Resolution: fixed


---

Comment by mabshoff created at 2009-04-01 00:46:13

Merged in Sage 3.4.1.rc0.

Cheers,

Michael
