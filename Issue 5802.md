# Issue 5802: use tuples rather than copying lists for immutable data

Issue created by migration from Trac.

Original creator: robertwb

Original creation time: 2009-04-16 07:21:10

Assignee: cwitty

An example came up at #5756 where one returns the list `__im_gens` but for fear that it be mutated, a copy is created. I've seen this same thing elsewhere in the library. It would be better to just return a tuple. 


---

Comment by kedlaya created at 2016-08-17 00:59:13

A similar issue arose at #20743.
