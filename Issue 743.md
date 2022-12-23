# Issue 743: graphs: simplify interface for accessing vertex objects

Issue created by migration from https://trac.sagemath.org/ticket/743

Original creator: jason

Original creation time: 2007-09-24 18:12:25

Assignee: was

Keywords: graphs

The functionality for associating any vertex of a graph with an arbitrary object is very nice.  However, it seems like the implementation could be simplified.  Can we implement an interface that does the following?

 * Makes it easy to assign an object to a single vertex, multiple vertices, or all vertices.  (Currently, you must assign the entire graph at once).

 * Makes it easy to retrieve an object associated with a vertex or multiple objects associated with multiple vertices (currently we can only retrieve one vertex at a time).

 * Has symmetry in the get/set functions (currently there is an "associate" and a "obj" function).

It seems that the simplest way to deal with multiple vertices is to use a dictionary, as is currently done, to associate a set of vertices with their corresponding objects.

Here's an example of a possible idea:


```
  sage: g=Graph();
  sage: g.add_vertices(10);
  sage: g.set_vertices({0: 'vertex0', 1: 'vertex1'})
  sage: g.set_vertex({3: 'vertex3'})
  sage: g.set_vertex(4,'vertex4')
  sage: g.get_vertices()
  {0: 'vertex0', 1: 'vertex1', 3: 'vertex3', 4: 'vertex4'}
  sage: g.get_vertex(0)
  'vertex0'
  sage: g.get_vertices([0,1])
  {0: 'vertex0', 1: 'vertex1'}
```


Of course, in the above example, the strings could have been replaced with any objects.


---

Comment by jason created at 2007-11-28 19:47:24

Additional comments, stemming from Chris Godsil's wishlist:


```
>>> (c) Edge-colored graphs: A graph and functions from its edges to an index
>>> set, and vice versa. These could also be represented as a set of
>>> matchings,
>>> and this data structure can be used to represent maps on surfaces.
>> I think we should make a nice system for attaching arbitrary metadata to
>> vertices and edges of a graph. Something like an attribute dictionary
>> for each vertex and edge.
> There is an existing trac ticket for improving the vertex association
> setup- most likely these comments should just go on that ticket. Any
> object at all can be the label for an edge, so I don't think there is
> too much to do here.
```



---

Comment by rlm created at 2007-12-02 04:49:58

Changing status from new to assigned.


---

Comment by rlm created at 2007-12-02 04:49:58

Changing assignee from was to rlm.


---

Comment by rlm created at 2007-12-17 15:08:10

Changing keywords from "graphs" to "".


---

Comment by rlm created at 2007-12-17 15:08:10

Changing component from combinatorics to graph theory.


---

Comment by jason created at 2008-01-19 06:18:52

See the recent discussion on the networkx mailing list at:

http://groups.google.com/group/networkx-discuss/browse_thread/thread/3fdfe1956c6e915?hl=en

for some comments on labels for vertices.


---

Attachment


---

Comment by rlm created at 2008-01-27 02:08:14

I don't know why the first two diffs on the patch are necessary, but the relevant changes are in the last two.


---

Comment by cwitty created at 2008-01-27 02:44:14

Code looks good; doctests pass.


---

Comment by mabshoff created at 2008-01-27 02:47:38

Merged in Sage 2.10.1.rc1


---

Comment by mabshoff created at 2008-01-27 02:47:38

Resolution: fixed


---

Attachment


---

Comment by cwitty created at 2008-01-27 04:15:31

Changing status from closed to reopened.


---

Comment by cwitty created at 2008-01-27 04:15:31

The attached trac-743-fix.patch fixes the fallout from this patch in ell_rational_field.py .


---

Comment by cwitty created at 2008-01-27 04:15:31

Resolution changed from fixed to 


---

Comment by mabshoff created at 2008-01-27 04:20:08

trac-743-fix.patch looks good to me. Merged in Sage 2.10.1.rc1.

Cheers,

Michael


---

Comment by mabshoff created at 2008-01-27 04:20:08

Resolution: fixed
