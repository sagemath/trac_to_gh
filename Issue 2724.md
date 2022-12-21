# Issue 2724: Graph.show3D should have default aspect ratio of [1,1,1]

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2008-03-29 19:37:19

Assignee: rlm

In the following:


```
sage: g=graphs.PetersenGraph()
sage: g.show3d()
```


the edges look messed up (some are darker and some are lighter and it changes as you rotate the graph).  Putting aspect_ratio=[1,1,1] fixes the problem:


```
sage: g=graphs.PetersenGraph()
sage: g.show3d(aspect_ratio=[1,1,1])
```




---

Comment by mabshoff created at 2008-03-29 19:50:32

Might this be a duplicate of #2477, i.e. show3d vs. plot3d? This also has some overlap with #2100.

Cheers,

Michael


---

Comment by rlm created at 2008-03-29 20:05:20

This is an exact duplicate of #2477. Make sure to check before posting tickets!


---

Comment by rlm created at 2008-03-29 20:05:20

Resolution: duplicate


---

Comment by jason created at 2008-03-29 20:06:39

You're right, it's a dup of #2477.  I tried searching for a ticket, but didn't find that one (I was looking for show3d).

I've posted a review for that patch.
