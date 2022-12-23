# Issue 4109: The complement of a graph shows as the original graph

Issue created by migration from https://trac.sagemath.org/ticket/4109

Original creator: jason

Original creation time: 2008-09-13 04:43:20

Assignee: rlm


```
g=graphs.PathGraph(6)
g.show()
h = g.complement()
h.show()
```

The last command shows the original P_6, not the complement.  However, calling `h.edges()` seems to return the right results.  Also, `Graph(h).show()` shows the correct thing, I think.




---

Comment by jason created at 2008-09-13 04:45:48

The possible problem:


```
[22:40] <rlm_> jason- the position dict of the path graph is set
[22:40] <rlm_> use layout='spring'
[22:41] *** rlm_ is now known as rlm|afk.
[22:42] <jason-> rlm_: okay, so the pos dict just needs to be cleared when creating the complement, I guess.
```



---

Comment by rlm created at 2008-09-13 07:30:52

This was actually a design decision -- if you take the complement, the vertices are in the same position, and you can see where the edges are and are not. Perhaps the path graph should have a more than one dimensional layout...


---

Comment by rlm created at 2008-09-13 18:45:06

Resolution: wontfix


---

Comment by rlm created at 2008-09-13 18:45:06

Since this is a design decision and not a bug, I'm invalidating the ticket. If you think it's a bad design decision, take it to the mailing list. If you think path graphs shouldn't layout in lines, make a new ticket.
