# Issue 9036: Graph.canonical_label(certify=True, edge_labels=True) returns a name error

Issue created by migration from Trac.

Original creator: stumpc5

Original creation time: 2010-05-24 14:29:39

Assignee: jason, ncohen, rlm

Keywords: labelled graph isomorphism

The method canonical_label() for Graph and DiGraph does not take the parameters 'certify=True' and 'edge_labels=True' at the same time:


```
sage: g = Graph()                                      
sage: g.canonical_label()
Graph on 0 vertices
sage: g.canonical_label(certify=True)
(Graph on 0 vertices, {})
sage: g.canonical_label(edge_labels=True)
Graph on 0 vertices
sage: g.canonical_label(certify=True, edge_labels=True)

...

NameError: global name 'relabeling' is not defined
}}


---

Comment by stumpc5 created at 2010-06-02 00:47:23

Changing status from new to needs_review.


---

Comment by ncohen created at 2010-06-13 18:18:18

Changing status from needs_review to needs_info.


---

Comment by ncohen created at 2010-06-13 18:18:18

Hmmm... I am reaallyyyyy sorry but I do not have the slightest idea of what the function "canonical_label" exactly does... Could I ask that your patch also improves its documentation ? :-/

Nathann


---

Comment by stumpc5 created at 2010-06-15 13:26:18

fixed bug in GenericGraph.canonical_label() and updated documentation


---

Attachment

Done... I hope it is more understandable now.

Christian


---

Comment by stumpc5 created at 2010-06-15 13:30:19

Changing status from needs_info to needs_review.


---

Comment by ncohen created at 2010-06-15 14:14:35

Changing status from needs_review to positive_review.


---

Comment by ncohen created at 2010-06-15 14:14:35

Positive review ! I can now see it was a natural thing to do, but I really didn't feel safe without understanding the function's purpose... :-)

Thank you again !

Nathann


---

Comment by rlm created at 2010-06-29 16:47:57

Resolution: fixed
