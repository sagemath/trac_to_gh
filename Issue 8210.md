# Issue 8210: Problem in Displaying Graphs

Issue created by migration from Trac.

Original creator: pong

Original creation time: 2010-02-08 05:14:09

Assignee: rlm

Keywords: Graph

For example,

k=graphs.CompleteGraph(6)
show(k)

Shows K6 but the vertices are partially chopped off.

A work around would be 
show(k, axes_pad=.1)

But I hope this can be fixed once and for all.
There are some discussion about this problem in SAGE Support.
http://groups.google.com/group/sage-support/browse_thread/thread/85a797a886a6446f/4d58090a4c868200#4d58090a4c868200



---

Comment by jason created at 2010-02-09 15:42:12

This is a dup of #7299, and has been fixed in 4.3.2.


---

Comment by jason created at 2010-02-09 15:42:12

Resolution: duplicate
