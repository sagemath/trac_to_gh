# Issue 8284: IntervalGraph generator and a bug in is_chordal

Issue created by migration from https://trac.sagemath.org/ticket/8284

Original creator: ncohen

Original creation time: 2010-02-16 18:11:03

Assignee: rlm

Hello !!!

This very small patch creates an independent generator for IntervalGraph, which is then called by the old RandomIntervalGraph function... The function is_chordal is fixed, as it was not exploring the whole graph when it was not connected.

Nathann


---

Comment by ncohen created at 2010-02-16 18:12:29

Changing status from new to needs_review.


---

Comment by ncohen created at 2010-02-16 18:15:18

Changing assignee from rlm to ncohen.


---

Comment by ncohen created at 2010-02-16 18:15:18

oh yes, and the lex_bfs method now admits an optional initial vertex ! :-)


---

Comment by rlm created at 2010-03-02 04:00:16

Can you please provide a doctest which shows a simple example of creating an `IntervalGraph` from intervals?


---

Comment by rlm created at 2010-03-02 04:00:16

Changing status from needs_review to needs_work.


---

Comment by ncohen created at 2010-03-02 09:13:59

Done ! :-)


---

Comment by ncohen created at 2010-03-02 09:13:59

Changing status from needs_work to needs_review.


---

Comment by rlm created at 2010-03-06 21:56:58

Changing status from needs_review to needs_work.


---

Comment by rlm created at 2010-03-06 21:56:58

Please add the following doctests:

1. An example of `is_chordal` for a non-connected graph.

2. Examples of the usage of each option to `lex_BFS`.

After this is done, I'll be happy with the patch. All tests pass.


---

Comment by rlm created at 2010-03-06 21:58:10

I forgot to mention, please also look over the attached patch. I believe this is a cleaner coding of the same thing.


---

Comment by ncohen created at 2010-03-07 13:02:26

The ``max`` instruction fails with this modification, as the --possibly last-- vertex in the list may have been removed before, thus max is trying to find the maximum of an empty list ...

I'll bring the other modifications as soon as possible... Thank you for your help ! :-)

Nathann


---

Comment by ncohen created at 2010-03-08 12:01:40

Changing status from needs_work to needs_review.


---

Comment by ncohen created at 2010-03-08 12:01:40

Here it is ! :-)


---

Comment by ncohen created at 2010-05-20 20:07:33

Changing priority from major to critical.


---

Comment by ncohen created at 2010-06-08 12:19:08

Patch updated ! And based on the brand new 4.4.4.alpha0. Apply only this one !

Nathann


---

Attachment

Looks good.


---

Comment by rlm created at 2010-06-08 17:31:42

Changing status from needs_review to positive_review.


---

Comment by edward.scheinerman created at 2010-06-13 22:53:07

This new graphs.IntervalGraph and the repaired graphs.RandomInterval work as advertised. Nicely done Nathann. 

However, I think graphs.Interval should allow repeated intervals, e.g., 
g = graphs.IntervalGraph( [(0,2), (0,2), (1,5), (3,7)] )
should create a graph with four vertices (not three as the method currently does).


---

Comment by ncohen created at 2010-06-14 06:42:33

you are right !!! I think the best way would be to create a RealInterval class in sage.sets, this way each vertex would be an immutable (hashable) object, and the graph could have two vertices representing the same interval.. I had the same problem when writing the recognition algorithm (#7563) : twin vertices were representing the same intervals, and the final graph was not isomorphic to the first as some vertices had disappeared..

I used a small trick to make it work, but this is definitely not a good answer :-)

Nathann


---

Comment by jason created at 2010-06-14 15:30:07

You might be able to get away with just creating a class that doesn't have a defined hash function, so that the default (the memory address) is used.  The problem with using a tuple is that the two hash values below are the same:


```
sage: a=(1,2)
sage: b=(1,2)
sage: hash(a)
3713081631934410656
sage: hash(b)
3713081631934410656
```


We can use a feature of user-defined classes, though:

"User-defined classes have __cmp__()  and __hash__()  methods by default; with them, all objects compare unequal (except with themselves) and x.__hash__()  returns id(x)."

This means we can get vertices which contain objects which normally would be considered equal in a dictionary to be stored as two different things in a dictionary:


```
sage: class Vertex(object):
....:     def __init__(self, value):
....:         self.__value=value
....:         
sage: a=Vertex((1,2))
sage: b=Vertex((1,2))
sage: a is b
False
sage: hash(a)
4528980944
sage: hash(b)
4528980816
sage: Graph({a: [b]})
Graph on 2 vertices
```


Does that address the problem?  It introduces a problem, in that now you can't do:

`g[Vertex((1,2))]`

to get the neighbors, since, of course, the element you are creating is not the same as any of the vertices of the graph.  Also, you have to use v.__value to get the interval (or better, make some accessors for the attribute (and if you want, try to disallow changing it).


---

Comment by ncohen created at 2010-06-14 15:37:40

Hmmmm.. Anyway creating a RealInterval class wouldn't be a solution as we would like RealInterval(1,2) == RealInterval(1,2) to be True, which can not hold if we want the vertices to be different in the Graph  :-/

In the end, perhaps the best idea is the one Ed mentionned in one of his emails : just labels the vertices with (id,(a.b)), and forget about unnecessary abstraction, which wouldn't add anything in this case...

But then the user creating an interval graph by giving a list of pairs (a,b) would not be able to guess the name of its vertices, as they would depend on the id given by IntervalGraph. Of course we can make it number them according to the order given by the list, but I don't like it very much either :-/

Any idea ? :-/

Nathann


---

Comment by rlm created at 2010-06-29 16:42:09

Resolution: fixed
