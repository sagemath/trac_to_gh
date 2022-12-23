# Issue 6522: replace .copy() with .__copy__() in graphs/graph.py

Issue created by migration from https://trac.sagemath.org/ticket/6522

Original creator: AlexGhitza

Original creation time: 2009-07-13 10:22:27

Assignee: was

CC:  sage-combinat was mvngu alexghitza

See also #111, where this originates.



---

Comment by AlexGhitza created at 2009-07-13 10:25:49

Note that this has consequences for several files in combinat/.


---

Comment by kcrisman created at 2009-09-15 15:19:51

Note that we will likely need deprecation warnings.  See discussion at #6521.


---

Comment by kcrisman created at 2009-11-18 15:18:04

There is one small problem with this.  Doing the naive change - 

```
    def __copy__(self, implementation='networkx', sparse=None):
```

yields:

```
sage: g=Graph({0:[0,1,1,2]})
sage: copy(g)
Looped multi-graph on 3 vertices
sage: g.__copy__(sparse=True)
Looped multi-graph on 3 vertices
sage: copy(g,sparse=True)
---------------------------------------------------------------------------
TypeError: copy() got an unexpected keyword argument 'sparse'
```

It's not clear to me how to deal with this; changing the global 'copy' to handle keywords seems ill-advised.  On the other hand, there definitely is code (elsewhere) that uses the keywords implementation and sparse, at least in graph_generators.py.


---

Comment by kcrisman created at 2009-11-18 17:04:06

Changing status from new to needs_review.


---

Comment by kcrisman created at 2009-11-18 17:04:06

I resolved this as best I could.  Attached patch *should* catch all remaining instances of .copy() that don't belong to Python objects that require it (i.e. dicts have only copy, not '__copy__'!)


---

Comment by kcrisman created at 2009-11-18 17:04:33

Based on 4.2.1


---

Attachment

Hello !!! Could you use the new methods defined in #7515 for the functions you deprecate ? It would ease the work in #7559 :-)


---

Comment by ncohen created at 2009-12-08 17:13:08

Changing status from needs_review to needs_work.


---

Comment by rlm created at 2009-12-15 21:58:40

I can't say that I agree with the point of this ticket.

Certainly there should be a `__copy__` defined for graphs, so that

```
sage: G = copy(Graph())
```

works. However, the main use case of the `copy` method for graphs (for me, at least) is when I want to change underlying implementations. What was

```
sage: G = graphs.PetersenGraph()
sage: C = G.copy(implementation='c_graph', sparse=False)
```

won't work as

```
sage: G = graphs.PetersenGraph()
sage: copy(G, implementation='c_graph', sparse=False)
```

but instead we now need to do:

```
sage: G = graphs.PetersenGraph()
sage: C = G.__copy__(implementation='c_graph', sparse=False)
```


Which is an ugly, pointless change in API. Why don't we just define `__copy__`, and acknowledge that in some cases, it makes sense for objects to have a `copy` method?


---

Comment by kcrisman created at 2009-12-16 03:18:06

I think that is fine (despite the time it took to do this), because that point makes tons of sense!  But perhaps the people who originated this idea in #111 should weigh in before we just add a __copy__ and don't remove copy - I am cc:ing a few of them.


---

Comment by ncohen created at 2009-12-16 12:00:31

Ok, let's forget about #7515 and #7559 for this patch, if you are short on time it is not worth making this patch wait :-)

Besides, taking care of #7559 will be a huge work, with of without 10 modifications more !

Nathann


---

Comment by rlm created at 2009-12-16 18:52:04

Changing the component to graph theory so I can track this:

see http://groups.google.com/group/sage-devel/browse_thread/thread/70aacbd1dcc83497


---

Comment by rlm created at 2009-12-16 18:52:04

Changing component from user interface to graph theory.


---

Comment by kcrisman created at 2009-12-17 21:50:31

Based on 4.3.alpha1


---

Attachment

Okay, here is how I dealt with these issues.

1. We can't use the generic deprecation thing from #7515 here, because it would say to use copy instead of copy!  Unfortunately.  On the plus side, that's one less for #7559. 

2. I have not deprecated copy() from the generic graph class, only the yang-baxter one.  There is now a __copy__ for generic graphs.  In order to deal with a tricky thing on Dynkin diagrams, I had to define a __copy__ method for them, which however is EXACTLY the same as the generic Python copy from the copy module.

I really, really worked hard to make sure I caught every possible place where this causes problems, and it passes all doctests, but please think hard where it would make a difference.  I also hope I won't have to rebase it again :)


---

Comment by kcrisman created at 2009-12-17 21:54:05

Changing status from needs_work to needs_review.


---

Comment by rlm created at 2009-12-17 22:45:02

Changing status from needs_review to positive_review.


---

Comment by rlm created at 2009-12-17 22:45:02

Ran tests in sage/graphs and sage/combinat. Looks good to me (I think some of those imports are unnecessary, but not a showstopper)


---

Comment by mhansen created at 2009-12-20 07:19:08

Resolution: fixed
