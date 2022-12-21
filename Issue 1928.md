# Issue 1928: Bundles of graphs

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2008-01-25 19:50:35

Assignee: rlm


#1306 laid some of the groundwork for finishing this request, but it's not finished yet, so I'm opening another ticket with the original request.


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

Comment by rlm created at 2008-01-26 19:40:28


```
[11:28am] rlm: given two graphs, and a surjection from one to the other (not necessarily a graph hom.), we can construct a bundle
[11:29am] rlm: further, all bundles arise in this way
[11:29am] rlm: so instead of a partition, give both graphs and a map
[11:29am] rlm: that allows for any bundle to be constructed, right?
[11:34am] jason: rlm: the first graph is the petersen graph, for example, and the second is K_2, right?
[11:34am] jason: Yes, I think you're right that every bundle can be described that way.
[11:35am] rlm: so at least we have one way of constructing, so that nothing can't be constructed
```



---

Comment by rlm created at 2008-01-26 20:07:54


```
[11:55am] rlm: ok, G1 is a 5-cycle
[11:55am] rlm: G2 is K(3,3)
[11:55am] rlm: G3 is empty on 3 vertices
[11:55am] rlm: there's an obvious bundle here, and it should be brainless to construct
[11:56am] rlm: like GraphBundle(base=G1, edge_lifts=G2, vertex_lifts=G3)
[11:56am] rlm: and it just works
[11:56am] rlm: no matter how you glue, you'll get the same thing
[11:57am] rlm: maybe instead of, if the vertices match up, just match them according to their orderings
[11:57am] jason: That's what Chris was saying when he said "(There is an implicit orientation here)"
```



---

Comment by rlm created at 2008-01-26 20:09:13

Also, there are several functions of generic graphs that should be overridden, especially things like add_vertex etc.


---

Comment by vbraun created at 2015-03-21 12:30:20

See #18028
