# Issue 7540: Speed up shortest_path_all_pairs() and update distance_graph

Issue created by migration from https://trac.sagemath.org/ticket/7540

Original creator: ncohen

Original creation time: 2009-11-27 12:16:45

Assignee: rlm

CC:  rbeezer

As mentionned in #7533 by Rob Beezer, the function shortest_path_all_pairs() is much slower than computing independently all the distances, which is a bit worrying. Easy explanation ( at least it is an explanation for me, though there may be a deeper one ), distance() is a function from NetworkX while the Floyd-Marshall algorithm is directly written in Python, hence the slowness.

This function is very fundamental and should be improved ! The difference is amazing :


```
sage: g=graphs.RandomGNP(200,.1)
sage: time e=g.shortest_path_all_pairs()
CPU times: user 16.51 s, sys: 0.06 s, total: 16.57 s
Wall time: 16.60 s
sage: time a=[g.distance(i,j) for (i,j) in Subsets(g,2)]
CPU times: user 1.06 s, sys: 0.00 s, total: 1.06 s
Wall time: 1.06 s
```



---

Comment by ylchapuy created at 2009-11-27 14:13:01

then... use networkx. More precisely,
`networkx.all_pairs_shortest_path` and `networkx.all_pairs_shortest_path_length`.

They are not based on Floyd-Marshall (it is also in networkx but way slower)


---

Comment by ncohen created at 2010-01-19 06:22:37

Resolution: duplicate


---

Comment by ncohen created at 2010-01-19 06:22:37

Done in #7966
