# Issue 2266: give shortest_paths an optional endpoint

Issue created by migration from Trac.

Original creator: rlm

Original creation time: 2008-02-22 21:27:54

Assignee: rlm

CC:  jason mvngu brunellus

Implement an optional input, `v=None` to the function `shortest_paths`, which would then only return the shortest paths from `u` to `v`.


---

Comment by AlexGhitza created at 2009-01-22 18:26:38

Changing type from defect to enhancement.


---

Comment by mvngu created at 2009-06-27 00:50:58

CC'ing myself.


---

Comment by @akshat1136 created at 2020-01-30 11:43:53

I don't think we need to update `shortest_paths` as there already exists a method `shortest_path` which takes input `u` and `v` and outputs the single shortest path between them.


---

Comment by dcoudert created at 2022-05-01 08:13:22

If the question is to get all shortest paths from u to v, then:
- For unweighted graphs, we have `all_paths_iterator` and `all_simple_paths` that list paths by increasing length and that accept as input an optional list of starting / ending nodes.
- For weighted graphs without negative edge weights, we have `shortest_simple_paths` that yields shortest simple paths from u to v by increasing weights. Non-simple paths should be treated in #28076.
- For graphs with negative weight cycles, the problem of finding a path in NP-hard. We can use ILP. We can do better if we have negative weight edges but no negative weight cycles.
