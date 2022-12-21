# Issue 5941: transitive_close returns a graph with the same name even though it is a totally different graph!

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-04-29 17:18:14

Assignee: rlm


```
sage: g = graphs.KrackhardtKiteGraph()
sage: h = g.transitive_closure()
sage: h       # oops -- h says it is Krackhardt Kite but it isn't
Krackhardt Kite Graph: Graph on 10 vertices
sage: h == g
False
sage: h.is_isomorphic(g)
False
```



---

Attachment


---

Comment by ekirkman created at 2009-07-18 23:49:59

Nice!


---

Comment by jason created at 2009-07-18 23:54:01

Looks like I simultaneously reviewed this.  Positive review from me too.


---

Comment by mvngu created at 2009-07-19 13:31:43

Resolution: fixed
