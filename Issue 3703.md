# Issue 3703: [with patch, needs review] bug in set_edge_label

Issue created by migration from https://trac.sagemath.org/ticket/3703

Original creator: rlm

Original creation time: 2008-07-22 00:17:40

Assignee: rlm


```
sage: G = Graph({0:{1:1}}, implementation='c_graph')
sage: G.num_edges()
1
sage: G.set_edge_label(0,1,1)
sage: G.num_edges()
2
```



---

Attachment

Positive review.  Good catch!

Passes doctests in graphs/*.py, graphs/*.pyx, and graphs/base/*.pyx


---

Comment by rlm created at 2008-07-22 16:36:37

I spent most of a day hunting for this one; I wasn't expecting to find it where I did. I was writing new code, so I was convinced it was there...


---

Comment by jason created at 2008-07-25 15:00:48

That's a nice blog post you have talking about finding this bug:

http://rlmill.blogspot.com/2008/07/adinkras.html


---

Comment by rlm created at 2008-07-30 20:07:19

This has been sitting positively reviewed for several release cycles now. What's going on??


---

Comment by mabshoff created at 2008-07-30 22:30:24

Replying to [comment:5 rlm]:
> This has been sitting positively reviewed for several release cycles now. What's going on??

3.0.5 was supposed to be ultra stable, but one bug introduced mandated another 3.0.6 stable release. So this patch fell by the side. It will be merged in 3.1.alpha0 in a couple minutes provided the doctests pass.

Cheers,

Michael


---

Comment by mabshoff created at 2008-07-30 22:31:39

Resolution: fixed


---

Comment by mabshoff created at 2008-07-30 22:31:39

Merged in Sage 3.1.alpha0
