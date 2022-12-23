# Issue 744: graphs: returning graph to allow chaining

Issue created by migration from https://trac.sagemath.org/ticket/744

Original creator: jason

Original creation time: 2007-09-24 18:22:33

Assignee: was

Keywords: graphs

Currently many functions which modify a graph return the value that was just set.  If instead the modified graph were returned, it would permit a very powerful chaining mechanism in programming.  This mechanism, for example, is one of the things that is best-loved about the jQuery javascript library and something that I personally like very much in Mathematica.

For example, if "name" and "add_vertex" both returned the modified graph, then the following code would make 10 copies of the graph g, labeling each appropriately, and add a new vertex that was hooked, successively, to the first 10 vertices of g.  Notice how nicely that chaining complements list comprehensions.


```
  sage: [g.copy().name(new="graph %d"%i).add_vertex('center').add_edge(('center',i)) for i in [1..10] ]
```


Is there something that would break if we make this change (e.g., is there some functionality that depends on receiving back the change that was just made in the graph)?



---

Comment by jason created at 2007-10-25 18:57:49

I understand python philosophy a little more now and am not so sure that this is a good idea any more.  As I understand it, methods which modify the state of an object generally don't return anything, like a.sort().  Someone (Robert Bradshaw?) said this made things nice since there isn't two copies of the same object floating about.

The example in the ticket is probably more clearly written as below.  It's definitely as compact, which may not be a bad thing.

```
sage: glist=[g.copy() for i in (1..10)]
sage: for i in (1..10):
sage:     h=glist[i]
sage:     h.name(new="graph %d"%i)
sage:     h.add_vertex('center')
sage:     h.add_edge(('center'),i))
```


Should there be a big performance difference between this code and the line given in the ticket?


---

Comment by jason created at 2007-10-25 18:58:35

(I meant, "it's definitely __not__ as compact")


---

Comment by jason created at 2007-10-25 21:02:58

Resolution: wontfix


---

Comment by jason created at 2007-10-25 21:02:58

I've tested a few cases and the performance for each of the above pieces of code (even when the list created is much bigger) is pretty much the same.  I'm closing the ticket since there is a "python way" that is just as fast and probably more readable.
