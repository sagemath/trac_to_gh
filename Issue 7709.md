# Issue 7709: Graph constructor : Graph(edges=[ ... ] )

Issue created by migration from https://trac.sagemath.org/ticket/7709

Original creator: ncohen

Original creation time: 2009-12-16 11:55:26

Assignee: rlm

CC:  nthiery rlm

I often need to create graphs defined by a set of edges, and it should not be hard to add a new constructor of this shape :

```
g = Graph(edges=[ ... ] )
```


Nathann


---

Comment by ncohen created at 2010-06-06 11:00:53

Changing status from new to needs_work.


---

Comment by ncohen created at 2010-08-02 11:10:47

Here is a patch to update graph.py. I have been sitting a while, trying to find a efficient way to write this, and found none, so I ended up converting it all to a dict_of_lists of dict_of_dicts... As it took some time to write, I would gladly ask for your advice before rewriting it all for digraphs.py (if you agree). Otherwise, let's try to find a better solution together :-)

Nathann


---

Comment by ncohen created at 2010-08-02 11:10:47

Changing status from needs_work to needs_info.


---

Comment by ncohen created at 2010-08-02 11:11:52

Oh, by the way... This is no a new feature, as it was already possible to create a Graph by giving as an argument a list of edges, but until now it was forwarded to NetworkX..

Nathann


---

Comment by schilly created at 2010-08-02 12:13:30

I think `data.setdefault(u, [])` instead of `if not u in data: data[u] = []` could make it a litte bit faster  ;-)


---

Comment by ncohen created at 2010-08-02 14:42:54

Actually, I wondered... Faster to write, of course, but do you think it is also more efficient ? I had no idea, so I stuck to the most basic tools :-)

Nathann


---

Comment by schilly created at 2010-08-02 16:22:22

sorry, forget my comment, data.setdefault(...[]).append(u) is slower than your solution.


---

Comment by rlm created at 2010-08-04 01:59:05

I would change the ValueError message to something much shorter and more comprehensive, such as "Edges input must all be of the same format" or length or something...


---

Comment by rlm created at 2010-08-04 01:59:41

Replying to [comment:9 rlm]:
> I would change the ValueError message to something much shorter and more comprehensive, such as "Edges input must all be of the same format" or length or something...

Also, the doctests don't expose this error.


---

Comment by ncohen created at 2010-08-04 03:30:23

I just updated the ticket to fix it ! Do you think this method is acceptable and I can now do the same for DiGraphs ?

Nathann


---

Comment by rlm created at 2010-08-06 14:39:46

Replying to [comment:11 ncohen]:
> I just updated the ticket to fix it ! Do you think this method is acceptable and I can now do the same for DiGraphs ?

Nathann,

This looks good (maybe in the multiedges=False test you can show the list of edges afterward to demonstrate what actually happens). Please implement this in the DiGraph case as well!


---

Comment by ncohen created at 2010-08-08 11:05:20

Here it is ! Actually, the constructor raises an exception when the same edge receives different labels with multiedges = False. I had forgotten to fill the doctests, as it was just a preview !`:-)`

Nathann


---

Comment by ncohen created at 2010-08-08 11:05:20

Changing status from needs_info to needs_review.


---

Comment by rlm created at 2010-11-10 13:53:54

Changing status from needs_review to positive_review.


---

Attachment


---

Comment by jdemeyer created at 2010-11-11 13:01:50

Resolution: fixed
