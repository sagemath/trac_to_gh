# Issue 8417: improve CubeGraph and HyperStarGraph generation

Issue created by migration from Trac.

Original creator: ylchapuy

Original creation time: 2010-03-02 11:00:37

Assignee: rlm

see the title...


---

Attachment


---

Comment by ylchapuy created at 2010-03-02 11:03:47

the provided patch does also some 'cosmetic' changes, replacing 
`range(2*n)[n:]`with `range(n,2*n)`.


---

Comment by ylchapuy created at 2010-03-02 11:03:47

Changing status from new to needs_review.


---

Comment by rlm created at 2010-03-09 16:56:27

Apply both patches in order.


---

Comment by rlm created at 2010-03-09 16:56:27

Changing status from needs_review to positive_review.


---

Comment by ylchapuy created at 2010-03-09 18:14:50

Beware, with your patch applied I get:

```
sage: %timeit graphs.CubeGraph(12)
5 loops, best of 3: 2.95 s per loop
sage: time g = graphs.CubeGraph(14)
CPU times: user 72.66 s, sys: 0.42 s, total: 73.08 s
```

whereas with mine only I have:

```
sage: %timeit graphs.CubeGraph(12)
5 loops, best of 3: 653 ms per loop
sage: time g = graphs.CubeGraph(14)
CPU times: user 3.10 s, sys: 0.06 s, total: 3.16 s
```


This is mainly because using the construction `Graph(d, ...)` add
some checks I avoid setting vertices and edges myself.


---

Comment by rlm created at 2010-03-09 18:21:57

apply on top of other patch


---

Attachment

Replying to [comment:3 ylchapuy]:
> Beware, with your patch applied I get:

Thank you for pointing this out. I've reverted that part of the patch.

Can you see any way to make the overhead from checking in this case any better? Also, what do you think about a check=False option in graph construction, more generally?


---

Comment by jhpalmieri created at 2010-04-15 23:49:14

Merged into 4.4.alpha0:
 - trac_8417.patch
 - trac_8417-ref.patch


---

Comment by jhpalmieri created at 2010-04-15 23:49:14

Resolution: fixed
