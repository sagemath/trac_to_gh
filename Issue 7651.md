# Issue 7651: c_graph backends should include a "reversed" copy for digraphs in the sparse case

Issue created by migration from Trac.

Original creator: rlm

Original creation time: 2009-12-10 06:17:45

Assignee: rlm

CC:  ncohen jason

This is because the data structure for sparse graphs is itself directed, and in_neighbors is a slow function, as it needs to check each node.


---

Comment by rlm created at 2009-12-14 23:28:50

Changing status from new to needs_review.


---

Comment by ylchapuy created at 2009-12-15 00:32:56

line 945 in `c_graphs.pyx`, shouldn't it be `in_neighbors` ?


---

Comment by rlm created at 2009-12-15 00:56:30

Changing status from needs_review to needs_work.


---

Comment by rlm created at 2009-12-15 00:56:30

Yes! Good catch!


---

Attachment

apply to sage-4.3.rc0 + #7640 + #7674 + #7673


---

Comment by rlm created at 2009-12-15 01:02:40

Changing status from needs_work to needs_review.


---

Comment by ncohen created at 2009-12-15 11:15:02

I saw you replaced 

```
for w in (self._cg.out_neighbors(v) if side == 1 else self._cg.in_neighbors(v)): 
```

with

```
if side == 1: 
   neighbors = self._cg.out_neighbors(v) 
elif self._cg_rev is not None: # Sparse 
   neighbors = self._cg_rev.out_neighbors(v) 
else: # Dense 
   neighbors = self._cg.in_neighbors(v) 
```

I understand what you mean, but wouldn't it easier for developpers to define a function "in_neighbors" or "out_neighbors" doing this stuff to avoid dealing with the implementation of graphs when in the c_graph.pyx file ( where the algorithm are more graph-theoretic and a bit further from the implementation ) ?

This kind of thing is bound to reappear very often as we write algorithms in Cython... :-)

Nathann


---

Comment by ncohen created at 2009-12-15 14:50:52

Changing status from needs_review to needs_info.


---

Comment by rlm created at 2009-12-15 15:14:56

Changing status from needs_info to needs_review.


---

Comment by rlm created at 2009-12-15 15:14:56

Replying to [comment:7 ncohen]:
> I saw you replaced 
> ...
> with
> ...
> I understand what you mean, but wouldn't it easier for developpers to define a function "in_neighbors" or "out_neighbors" doing this stuff to avoid dealing with the implementation of graphs when in the c_graph.pyx file ( where the algorithm are more graph-theoretic and a bit further from the implementation ) ?

On the level of c_graphs, there is no way to avoid the implementation of graphs. You're using ints as vertices which may not line up with the actual labels, and since you're calling methods of self._cg, there's no way around it. If you want to write on a more friendly level, you need to sacrifice some speed, since on the level of (mostly Python) backends, the vertex labels are honest, and 'in_neighbors' is the appropriate function there.

> This kind of thing is bound to reappear very often as we write algorithms in Cython... :-)

This is only relevant to very low-level functions. In which case you *are* implementing graphs :)


---

Comment by rlm created at 2009-12-15 16:04:41

I should have pointed out that `self._cg.in_neighbors(v)` would still work in the case you point out. It's just that using `self._cg_rev.out_neighbors(v)` is faster when it's available. The point is that you only have to worry about these things when you're writing a function in the GraphBackends.

I'm more and more becoming convinced that #7634 is the appropriate place to break up `graph.py`. It will already be an invasive change to sage/graphs, and this will encourage people to get their pet patches merged before the switch. When I break up the file, part of the result will be a Cython layer, which sits "above" the graph backends. That way, when people are writing more advanced graph theory functions in Cython, they can do it there, safely away from the implementation-level stuff you're talking about.


---

Comment by ncohen created at 2009-12-15 16:22:18

Got it :-)

D you think there could be a *nice* way, though, to prevent people from using in_neighbors on sparse graphs having a reversed version of themselves ?


---

Comment by ncohen created at 2009-12-15 16:26:01

Positive review for this patch ! Applies fine, pass tests, and as far as I could I found nothing wrong inside... :-)


---

Comment by ncohen created at 2009-12-15 16:26:01

Changing status from needs_review to positive_review.


---

Comment by rlm created at 2009-12-15 16:44:04

Replying to [comment:11 ncohen]:
> Got it :-)
> 
> D you think there could be a *nice* way, though, to prevent people from using in_neighbors on sparse graphs having a reversed version of themselves ?

SparseGraphs will never have a reversed version. CGraphBackends may have a reversed version (i.e. two SparseGraphs), in which case in_neighbors will call it. I don't think we need to worry too much about lots of people implementing functions for the backends.


---

Comment by mhansen created at 2009-12-15 17:23:20

Resolution: fixed
