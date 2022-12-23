# Issue 7378: Subdivide edges in a graph

Issue created by migration from https://trac.sagemath.org/ticket/7378

Original creator: ncohen

Original creation time: 2009-11-03 09:26:13

Assignee: rlm

It is often useful to subdivide the edges of a graph, so there should be a function in Sage for this.

When an edge e between u and v is subdivided in a DiGraph, perhaps the best thing to do would be to name the new vertices as (e, 0), (e, 1), (e, 2), etc ...

We are left with a similar problem concerning the Graphs and here I have to admit I do not know which name to use without inducing some orientation..

This being said, it has to be done ! :-)

Nathann


---

Comment by ncohen created at 2010-04-04 15:15:13

Changing status from new to needs_review.


---

Comment by ncohen created at 2010-04-04 15:15:13

Here it is !!!

Nathann


---

Comment by jason created at 2010-04-20 04:53:34

In the docs, you say that the following are valid forms:

G.add_edge( 1, 2, 8 )

G.add_edge( (1, 2), 8 )

However, reading the code seems to indicate that it should be subdivide_edge, not add_edge.


---

Comment by jason created at 2010-04-20 04:53:34

Changing assignee from rlm to jason.


---

Comment by ncohen created at 2010-04-20 07:32:23

Indeed. Fixed :-)

Nathann


---

Comment by ncohen created at 2010-04-23 11:43:24

I just applied this patch on top of #7608, and there was nothing wrong to report :-)


---

Comment by rlm created at 2010-06-17 20:50:55

Changing status from needs_review to needs_work.


---

Comment by rlm created at 2010-06-17 20:50:55

"If the given edge is labelled with `l`, all the edges created by the subdivision will have the same label."

... You should also specify what happens to labels when `l` is not given. In addition, you should have all these cases doctested.


---

Comment by rlm created at 2010-06-17 20:53:30

> ... You should also specify what happens to labels when `l` is not given. In addition, you should have all these cases doctested.

That said, all tests pass. So once the above is addressed, I'll probably be happy.


---

Comment by ncohen created at 2010-06-18 11:55:09

Changing status from needs_work to needs_review.


---

Comment by ncohen created at 2010-06-18 11:55:09

What about this ? :-)

Nathann


---

Comment by rlm created at 2010-06-18 15:20:58

Changing status from needs_review to needs_work.


---

Comment by rlm created at 2010-06-18 15:20:58

I don't think this quite works as advertised. If I have edge `(u, v, 1)` and I do `G.subdivide_edge((u, v, 2), 5)`, then the edge `(u, v, 1)` is never deleted.

Is the input label the new label, or the label of the existing edge?

Maybe there should be a `new_label` argument instead? I'm not sure the best way to approach this, and I'm interested in your opinion.


---

Comment by ncohen created at 2010-06-20 17:51:00

Oh... The behaviour I had in mind was rather to raise an ValueError excetion saying : edge(u,v,2) does not exist. I really think of this as a topological method, so the user is expected to relabel his edges later if there is any need of it. I really wanted the edge to be "split" into several parts, all bearing the same label. 

What would you think about it ? I'll update the patch to match this behaviour, just because it is easy to do so, though if you don't like it we can still remove it ! :-)

Nathann


---

Attachment


---

Comment by rlm created at 2010-06-21 17:38:31

Apply after trac_7378.patch


---

Comment by rlm created at 2010-06-21 17:40:17

Changing status from needs_work to needs_review.


---

Attachment

Replying to [comment:10 ncohen]:
> I really wanted the edge to be "split" into several parts, all bearing the same label. 

Thanks for clarifying. I've tried to make this clear in the documentation. If you approve of my referee patch, please set the ticket to positive review.


---

Comment by ncohen created at 2010-06-21 20:15:38

Changing status from needs_review to positive_review.


---

Comment by ncohen created at 2010-06-21 20:15:38

Thank youuuuuuuuuuu !!! :-)

Nathann


---

Comment by ncohen created at 2010-06-21 20:17:44

Changing status from positive_review to needs_work.


---

Comment by ncohen created at 2010-06-21 20:17:53

Changing status from needs_work to needs_review.


---

Comment by ncohen created at 2010-06-21 20:30:20

wrong alert, positive review ! :-)

Nathann


---

Comment by ncohen created at 2010-06-21 20:30:20

Changing status from needs_review to positive_review.


---

Comment by rlm created at 2010-06-29 16:43:03

Resolution: fixed
