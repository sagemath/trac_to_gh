# Issue 8395: degree() reports the degree of a self-loop vertex as contributing 1 to total degree

Issue created by migration from https://trac.sagemath.org/ticket/8395

Original creator: mvngu

Original creation time: 2010-02-28 14:52:11

Assignee: rlm

CC:  jason ncohen

From [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/42110dbb598d11d2):

```
[mvngu@sage mvngu]$ sage
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: G = Graph({1:[1]}); G
Looped graph on 1 vertex
sage: sum(G.degree())
1
sage: G.size()
0
sage: G = Graph({1:[1]}, loops=True); G
Looped graph on 1 vertex
sage: sum(G.degree())
1
sage: G.size()
0
sage: G = Graph({1:[1]}, loops=True, multiedges=True); G
Looped multi-graph on 1 vertex
sage: sum(G.degree())
1
sage: G.size()
0
| Sage Version 4.3.3, Release Date: 2010-02-21                       |
| Type notebook() for the GUI, and license() for information.        |
The size of G is 1 because there is one edge, i.e. the single
self-loop. As shown by the above session, Sage reports the size of G
as 0. I believe this is a bug. 
```



---

Attachment


---

Comment by mvngu created at 2010-12-03 13:59:16

Changing status from new to needs_review.


---

Attachment

apply after previous patch


---

Comment by rlm created at 2010-12-03 16:27:23

Minh,

Your patch looks good to me. If you approve of mine, please set this to positive review.

Thanks!


---

Comment by mvngu created at 2010-12-04 02:53:18

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2011-01-12 06:31:26

Resolution: fixed
