# Issue 5937: graph theory -- showing the result of a database query with_picture=True is totally broken

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-04-29 16:05:22

Assignee: rlm

Here is *yet another* example of non-tested code being totally broken.  Try this in the notebook.


```
Q = GraphQuery(display_cols=['graph6','num_vertices','degree_sequence'],
   num_edges=['<=',5],min_degree=1)

Q.show(with_picture=True)
```


this silently outputs absolutely nothing. 

The doctests don't test this -- they only test that this fails (with a message) on the command line. 

Shorterm fix: completely remove this option from the documentation and code.

Lonterm fix: actually track down and fix the bug -- this would be nice, since I know the output looks good (I've seen Emily demo it).




---

Comment by ekirkman created at 2009-05-21 21:54:48

I am unable to duplicate this bug.  I'm using a clean branch of 4.0alpha0.  Can someone else give this a try?


---

Comment by rlm created at 2009-05-21 22:02:32

I have the same result. Everything looks fine for me.

William -- Could you try reproducing this? If you can, can we get what machine/version it is on?


---

Comment by rlm created at 2009-07-13 21:40:46

Resolution: invalid


---

Comment by rlm created at 2009-07-13 21:40:46

This has been open for 8 weeks with zero comment, so I'm assuming this is no longer valid.
