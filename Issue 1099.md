# Issue 1099: graphs: consolidating delete functionality

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2007-11-04 03:30:51

Assignee: mhansen

Keywords: graphs

Currently there are four different functions to delete things from a graph: delete_edge, delete_edges, delete_vertex, and delete_vertices.  How about we consolidate these into one function, "delete", that looks like this:

delete(vertices=list_of_vertices, edges=list_of_edges) deletes the vertices specified, then the edges specified.

So:

 * delete_vertex(v) == delete(vertices=[v])

 * delete_vertices(list) == delete(vertices=list)

 * delete_edge(e) == delete(edges=[e])

 * delete_edges(list) == delete(edges=list)

 * deleting vertices and edges is accomplished by passing both parameters in.

This idea may be completely irrational, but I thought I'd throw it out in an effort to consolidate functions and make the interface simpler to remember.  What do you think?

(I'm ignoring delete_multiedge here, though we could probably include that in as an option to delete).



---

Comment by rlm created at 2007-12-17 15:11:14

Changing assignee from mhansen to rlm.


---

Comment by rlm created at 2007-12-17 15:11:14

Changing component from combinatorics to graph theory.


---

Comment by rlm created at 2007-12-17 15:11:14

Changing keywords from "graphs" to "".


---

Attachment

Defines the delete function, but does not remove any other functions


---

Comment by rlm created at 2008-01-27 03:12:28

We still need to figure out what to do with delete_multiedge (perhaps just keep it). Also, is there any loss of functionality going from the other functions to this one?


---

Comment by rlm created at 2008-01-27 03:19:15

Also note the somewhat arbitrary choice to support delete(edges=e) and delete(vertices=v) for vertex v and edge e. Should this stay?


---

Comment by boothby created at 2008-01-28 15:50:26

I support removing all other delete methods -- tab completion on a graph produces a formidable list, and having a bunch of redundant functions adds to the clutter.  That said, there are some strange things about this patch that I could do without:


```
G.delete(1)       #deletes a node
G.delete(1,2)     #deletes an edge
G.delete(1,2,3)   #deletes three nodes
G.delete(1,2,3,4) #deletes four nodes
```


one of these is not like the other... maybe you could balance it out, so if they pass in an even number of arguments, it removes the edges between successive pairs; odd number of arguments deletes nodes?


---

Comment by rlm created at 2008-01-28 17:58:49

I propose the following:

 1. Add an option, `multiple_edges`, to `delete()`, which is a boolean. If True, for every edge given, it deletes all edges on those vertices.
 1. Make it so that `delete(arg)` deletes vertex `arg`, or fails silently if it is not there. Make it so that `delete(arg1, arg2)` deletes the edge `(arg1, arg2)` if it is there, or fails silently if it is not there. Due to edges being 3-tuples (two vertices and a label), also make it so that `delete(arg1, arg2, arg3)` deletes the edge `(arg1, arg2, arg3)` if it is there, or fails silently if it is not.
 1. Make it so that calling `delete` with more than 3 arguments is not supported.
 1. Make it so that only iterable containers can be passed in for `delete(vertices=[v])` and `delete(edges=[e])`, so that `delete(edges=e)` and `delete(vertices=v)` is also not supported.


---

Attachment

On top of delete.patch


---

Attachment

On top of delete-2.patch


---

Attachment

on top of delete-3.patch


---

Comment by jason created at 2008-01-28 21:03:58

delete-4.patch should be applied on top of delete-3.patch.  It adds the following:

  1. extends the syntax so that delete((u,v)) or delete((u,v,label)) deletes an edge; this is so that we can do something like for e in g.edges(): g.delete(e)

  2. enhances the doctests for delete and also adds a doctest in another function that should have shown errors from the change we've made.

  3. Fix the errors from calling the old functions.  Robert, can you specifically look at the change in graph_generators?


---

Comment by jason created at 2008-01-28 21:52:43

I've run out of time today to work on this, but rlm and I agree that we should consolidate to two functions: delete_vertices and delete_edges, with a single non-list argument deleting a single vertex or edge.

That patch should be much simpler and should make much more sense in the long run.


---

Comment by rlm created at 2008-01-29 00:39:01

> with a single non-list argument deleting a single vertex or edge.

To clarify, if there is only one argument, and it is either a list or of type types.GeneratorType...


---

Comment by mabshoff created at 2008-04-08 15:59:41

What is the status of this ticket? I am afraid this code has/will bitrot.

Cheers,

Michael


---

Comment by rlm created at 2008-04-09 13:19:27

None of the patches for this ticket are or ever were quite ready. I also have to say that I still disagree with the ticket in general. It is much simpler to specify what you are deleting (especially if you happen to do a lot of actual coding with graphs, like me!).


---

Comment by mabshoff created at 2008-08-13 02:08:02

Jason,

what is the status of this work? It this something you are working on? Did those patches rot in the meantime?

Cheers,

Michael


---

Comment by rlm created at 2008-08-30 21:50:29

Resolution: wontfix
