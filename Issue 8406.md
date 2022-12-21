# Issue 8406: problem with duck typing in c_graph

Issue created by migration from Trac.

Original creator: ylchapuy

Original creation time: 2010-03-01 08:28:27

Assignee: rlm

two examples:

```
sage: G=Graph()
sage: R.<a>=GF(3^3)
sage: G.add_vertex(a^2)
sage: G.vertices()
[9]
```

This should be `[a]`, but `int(a)=9`

```
sage: R.<x>=GF(3^3,'a')[]
sage: G.add_vertex(x)
ValueError
```

This should work as `x` is hashable.

`int(x)` return a `ValueError`, but the code only tests for `TypeError`.


---

Comment by ylchapuy created at 2010-03-01 08:31:55

line 638 of c_graph.pyx, we find:


```
try:
    u_int = u
except TypeError:
    return -1
```


I think we should instead do an explicit test:

```
if isinstance(u,(int,long,Integer))
```

to avoid coercions.

Thoughts?


---

Comment by rlm created at 2010-03-02 07:06:26

The only thing I could think of was that maybe this would effect the speed. To benchmark, I tried `g = graphs.CubeGraph(n)` for various `n`, since that calls the relevant function `2^n` times. There was no noticable change at all, so I say we definitely switch. Not to steal author credit, but here's what I tested:


```
-    try:
+    
+    if isinstance(u,(int,long,Integer)):
         u_int = u
-    except TypeError:
+    else:
         return -1
-    if u_int < 0 or u_int >= G.active_vertices.size:
-        return -1
-    if u_int in vertex_labels:
+    if u_int < 0 or u_int >= G.active_vertices.size or u_int in vertex_labels:
```



---

Comment by ylchapuy created at 2010-03-02 08:53:27

Changing status from new to needs_review.


---

Attachment


---

Comment by rlm created at 2010-03-06 21:26:22

Every patch fixing a bug should include a doctest illustrating that bug. Can you make doctests for the two bugs you noted at the top of the page?


---

Comment by rlm created at 2010-03-06 21:26:22

Changing status from needs_review to needs_work.


---

Comment by ylchapuy created at 2010-03-09 15:08:28

Changing status from needs_work to needs_review.


---

Attachment

apply both patches in order.


---

Comment by rlm created at 2010-03-09 16:11:14

Thank you!


---

Comment by rlm created at 2010-03-09 16:11:14

Changing status from needs_review to positive_review.


---

Comment by mvngu created at 2010-03-11 04:44:27

Resolution: fixed


---

Comment by mvngu created at 2010-03-11 04:44:27

Merged in this order:

 1. [trac_8406.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8406/trac_8406.patch)
 1. [trac_8406-doctests.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8406/trac_8406-doctests.patch)


---

Comment by rlm created at 2010-07-27 12:16:22

see #9610
