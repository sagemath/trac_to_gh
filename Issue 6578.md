# Issue 6578: fast subgraphs by building the graph instead of deleting things

Issue created by migration from https://trac.sagemath.org/ticket/6578

Original creator: jason

Original creation time: 2009-07-21 11:08:27

Assignee: rlm

CC:  rlm

Currently, to create a subgraph, Sage copies the graph and then deletes everything not specified.  This is very slow if you just want a small part of a large graph.


---

Comment by jason created at 2009-07-21 11:17:09

This patch refactors the subgraph code into two functions, and then tries to intelligently choose between building the graph from scratch and deleting vertices and edges from a copy of the graph.


---

Attachment

Timing comparison:


```
sage: g=graphs.PathGraph(100000)                     
sage: %time g.subgraph(range(20), algorithm='add')   
CPU times: user 0.61 s, sys: 0.01 s, total: 0.62 s
Wall time: 0.68 s
Subgraph of (Path Graph): Graph on 20 vertices
sage: %time g.subgraph(range(20), algorithm='delete') # the old algorithm
CPU times: user 3.96 s, sys: 0.04 s, total: 4.00 s
Wall time: 4.15 s
Subgraph of (Path Graph): Graph on 20 vertices
```



---

Comment by rlm created at 2009-07-21 21:08:27

Jason,

Do you have any examples where `delete` is actually faster than `add`? I ask because what this does is add every edge, and then delete a bunch of them. I doubt it's ever faster.


---

Comment by jason created at 2009-07-22 02:13:06

Most of the time delete is faster than add; that's why I set the factor so that if we want more than 5% of the vertices, it does delete.

I think delete copies the graph, which doesn't *add* every edge, but probably just copies the edge dictionary, which should be *way* faster.

The tests I was taking my data from was doing


```
sage: g=graphs.PathGraph(1000)
```


and then doing `g.subgraph(range(i)` using each of the algorithms.  The breakeven point seemed to be between 50 and 100.  I also did this with the complete graph, and got similar results.


---

Comment by rlm created at 2009-07-22 02:45:35

Replying to [comment:4 jason]:
> I think delete copies the graph, which doesn't *add* every edge, but probably just copies the edge dictionary, which should be *way* faster.

What is this opinion based on? If it's not an inplace subgraph then it creates a copy, which calls networkx_graph, which calls NX's copy, which has the following lines:

```
        for e in self.edges_iter():
            H.add_edge(e)
```


So we're definitely not using the adjacency dictionary there. The crossover between add and delete you observed above is most likely due to overhead from the fact that calling Sage's add_edge is using several layers of Python functions.

I expect this to change drastically once the graph backends are optimized. This may be a while in the future, but you should keep this in mind for when that does eventually happen. In general, this patch is an improvement, since it provides both options, but thinking in terms of optimization at this stage is going to result in wasted effort, since the floor is about to drop out from underneath any current timings.

Anyway, everything looks good here (especially, applies to 4.1.1.alpha0 and passes tests), so let's go ahead and merge it!


---

Comment by jason created at 2009-07-22 06:24:43

The opinion was based on thinking of the most logical way to implement it (hence the "I think") :).  Thanks for looking into the code.

I'm dreaming of the day that this optimization and choice is obsolete!  It would be *so* nice!


---

Comment by mvngu created at 2009-07-23 05:22:42

referee patch


---

Attachment

The patch `trac_6578-referee.patch` adds a missing double colon "::". It also deletes two sets of redundant double colons.


---

Comment by mvngu created at 2009-07-23 05:38:08

Resolution: fixed
