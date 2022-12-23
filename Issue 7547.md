# Issue 7547: improve has_multiple_edges

Issue created by migration from https://trac.sagemath.org/ticket/7547

Original creator: ylchapuy

Original creation time: 2009-11-28 02:14:34

Assignee: rlm

CC:  ncohen

It seems to be the main bottleneck in graph plotting!
This patch cuts down by 30% the time for `sage -t graph.py` on my machine... (and doctests of course still pass)


---

Comment by ylchapuy created at 2009-11-28 03:01:45

For the record:

```
sage: P = graphs.PetersenGraph()
sage: D = graphs.DodecahedralGraph()
sage: L = D.lexicographic_product(P) 
sage: L.allow_multiple_edges(True)
sage: time L.has_multiple_edges()
```


Before: Wall time: 39.56 s

After: Wall time: 19.32 s

I hope I did no mistake, it's 4 a.m here...


---

Comment by ylchapuy created at 2009-11-28 03:01:45

Changing status from new to needs_review.


---

Comment by rlm created at 2009-11-28 05:36:20

Changing status from needs_review to positive_review.


---

Comment by rlm created at 2009-11-28 05:36:20

Nice work!


---

Comment by ncohen created at 2009-11-28 08:52:05

Well done !! :-)

Nathann


---

Comment by ylchapuy created at 2009-11-28 10:15:01

Sorry to give myself a "needs work" but my ideas are much clearer this morning.
New patch to come in a few minutes!


---

Comment by ylchapuy created at 2009-11-28 10:15:01

Changing status from positive_review to needs_work.


---

Comment by ylchapuy created at 2009-11-28 10:20:53

based on 4.3.alpha0


---

Comment by ylchapuy created at 2009-11-28 10:22:31

Changing status from needs_work to needs_review.


---

Attachment

New timing for the same test: 1.22s. It's useful to sleep!


---

Comment by rlm created at 2009-11-28 19:13:44

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2009-11-29 06:02:01

Resolution: fixed
