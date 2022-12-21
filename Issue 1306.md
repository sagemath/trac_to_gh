# Issue 1306: [graphs] Bundles of graphs

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2007-11-28 19:53:26

Assignee: mhansen

Keywords: graphs

From Chris Godsil's wishlist (reply by Jason Grout, second reply by Robert Miller)


```
>>> (e) Bundles: Start with a base graph G with vertices {1, . . . , n}.
>>> For each
>>> vertex i we are given a graph Ci . For each edge ij we are given a
>>> bipartite
>>> graph joining V (Ci ) to V (Cj ). (There is an implicit orientation here.)
>>> Some examples:
>>> (i) The Petersen graph: n = 2, C1 is the 5-cycle, C2 is its complement
>>> and the bipartite graph is a 5-matching.
>>> (ii) The Hoffman-Singleton graph can be constructed with n = 2, where
>>> C1 is an independent set on 15 vertices, C2 is a nice distance regular
>>> graph on 35 vertices,. . .
>>> (iii) Covering graphs. Here the graphs Ci are empty on r vertices, and
>>> each bipartite graphs is either an r-matching or is empty.
>> Huh, I used this idea extensively in my dissertation and a research
>> paper. I used the "blowup graph" terminology, though, from extremal
>> graph theory. Is anyone working on this? If not, I'll make a trac ticket.
> Nobody I know of. If you did this type of stuff in your dissertation,
> then I nominate you! Create a ticket.
```



---

Comment by rlm created at 2007-12-17 15:13:40

Changing component from combinatorics to graph theory.


---

Comment by rlm created at 2007-12-17 15:13:40

Changing keywords from "graphs" to "".


---

Comment by rlm created at 2007-12-17 15:13:40

Changing assignee from mhansen to rlm.


---

Attachment


---

Comment by rlm created at 2008-01-21 03:57:45

Changing status from new to assigned.


---

Comment by rlm created at 2008-01-21 03:57:45

Depends on #1874.


---

Comment by mhansen created at 2008-01-21 04:00:48

Applies and passes for me after 1874.


---

Comment by mabshoff created at 2008-01-21 04:06:16

Merged in Sage 2.10.1.alpha1


---

Comment by mabshoff created at 2008-01-21 04:06:16

Resolution: fixed
