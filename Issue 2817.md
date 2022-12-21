# Issue 2817: specify options for parts of graphs

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2008-04-05 22:37:11

Assignee: rlm

CC:  ncohen

See the post at:

http://groups.google.com/group/sage-support/browse_thread/thread/64b76550609c1019

One way to handle setting display options for different vertices/edges is to have the following conventions:

 * If edge_style is the dictionary **edge_style, pass **edge_style into the arrow() commands
 * If edge_style is a list, then we want to create (possibly different) edge_style dictionaries for each edge.  For each item in the list:
    * if the item is a dictionary d, then update all edge_style dictionaries with the dictionary d.
    * if the item is a list L with L[0]=list of edges, L[1]=dictionary d, then for each edge in L[0], update its edge_style with d.

Optimize this so that we create a dictionary for an edge iff it has a different edge style than other edges.  In other words, first have only one edge_style dictionary.  If a list is edges is then specified, then take those out of the default edge_list and update their dictionary, etc.  is there a data structure which efficiently partitions objects (maybe Sage partitions!?)


---

Comment by rlm created at 2008-09-10 03:01:52

Changing assignee from rlm to jason.


---

Comment by jmantysalo created at 2016-01-04 19:33:30

Nathann, I think this is a duplicate of #13827. If you agree, please put on positive_review.


---

Comment by jmantysalo created at 2016-01-04 19:33:30

Changing status from new to needs_review.


---

Comment by ncohen created at 2016-01-04 21:55:03

Do you consider #13827 as a ticket which aims at making all options of `Graph.plot` able to take [edge/vertex]-specific instructions? If so, could you update its description before setting this one to `positive_review`? Right now all the description of #13827 says is that it should be possible to provide an alternative text to the vertices' name.

Nathann


---

Comment by jmantysalo created at 2016-01-05 05:20:48

Changing status from needs_review to positive_review.


---

Comment by jmantysalo created at 2016-01-05 05:20:48

Replying to [comment:4 ncohen]:
> Do you consider #13827 as a ticket which aims at making all options of `Graph.plot` able to take [edge/vertex]-specific instructions? If so, could you update its description before setting this one to `positive_review`? Right now all the description of #13827 says is that it should be possible to provide an alternative text to the vertices' name.

Done that.

(For now that ticket is kind of waiting for someone to decide if my suggestions are good or not. ​Punarbasu Purkayastha suggested other kind of interface.)


---

Comment by vbraun created at 2016-01-06 00:01:41

Resolution: duplicate
