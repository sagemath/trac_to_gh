# Issue 9861: Reimplementation of IntervalGraph to handle repeated vertices.

Issue created by migration from https://trac.sagemath.org/ticket/9862

Original creator: edward.scheinerman

Original creation time: 2010-09-06 18:53:29

Assignee: jason, ncohen, rlm

Keywords: interval graph

This is a reimplementation of the `IntervalGraph()` constructor to allow repeated intervals in the list of intervals. The input is a list of intervals. The output is a graph whose vertices are numbered 0 through n-1 (where n is the length of the list). Vertices u and v are adjacent iff the u'th and v'th intervals in the input list intersect. The intervals associated with these vertices are saved with the graph using `set_vertex` and can be retrieved later using `get_vertex` or `get_vertices`.


---

Attachment


---

Comment by ncohen created at 2010-09-06 18:57:40

Changing status from new to needs_review.


---

Comment by ncohen created at 2010-09-06 19:24:51

Two short modifications in the docstring... One to use the ".. NOTE" environment, and another one to propagate the warnings to RandomInterval `:-)`

As usual, positive review to your patch ! It's left to you to judge mine `:-)`

Nathann


---

Attachment


---

Comment by edward.scheinerman created at 2010-09-06 19:59:13

Changing status from needs_review to positive_review.


---

Comment by edward.scheinerman created at 2010-09-06 19:59:13

Doc string changes are fine. Thanks, Nathann.


---

Comment by ncohen created at 2010-09-06 20:09:09

I'm glad to see this IntervalGraph issue settled at last.... and this easily :-)

Nathann


---

Comment by mpatel created at 2010-09-15 22:25:11

Remember to fill in the "Author(s)" and "Reviewer(s)" fields.  We use these to generate release notes.


---

Comment by mpatel created at 2010-09-15 22:52:34

Resolution: fixed
