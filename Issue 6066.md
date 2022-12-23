# Issue 6066: constructing Sage graphs is slow compared to NetworkX graphs

Issue created by migration from https://trac.sagemath.org/ticket/6066

Original creator: mabshoff

Original creation time: 2009-05-18 07:45:45

Assignee: rlm

See https://groups.google.com/group/sage-devel/browse_thread/thread/802227fa22233d5/310379356a804e7f

```
I was playing with some big(10^6) graphs and noticed SAGE cannot
handle constructing them in good time. However, networkx does just
fine. Before I dive into the code, is this a feature (i.e. sage graph
object has richer data and methods available) or this is a bug?

sage: D={}
sage: for i in xrange(10^3):
    D[i]=[i+1,i-1]
....:
sage: timeit('g=Graph(D)')
5 loops, best of 3: 2.05 s per loop
sage: import networkx
sage: timeit('g=networkx.XGraph(D)')
25 loops, best of 3: 21.9 ms per loop

Rado 
```

Then

```
The bug is almost trivial. The code

verts = data.keys()
....
for u in data:
   verts.union([v for v in data[u] if v not in verts])

is slowing down because in python searching in lists is slow. If we
use "verts = set(data.keys())" the code speeds up tremendously.

sage: D={}
sage: for i in xrange(10^3):
....:     D[i]=[i+1,i-1]
....:
sage: timeit('g=Graph(D)')
5 loops, best of 3: 79.6 ms per loop

Before I submit a patch how do I run the the graph theory doctests to
make sure nothing else is broken by changing verts from list to set?

Rado 
```



---

Attachment


---

Comment by rlm created at 2009-05-18 18:16:16

Doctests pass in `graphs` and `combinat`, and long tests also pass in `graphs`. This needs to be tested on all of Sage before it gets merged, but pending that, I say merge the code!


---

Comment by mabshoff created at 2009-05-18 18:18:20

Doctests pass long globally, too.

Cheers,

Michael


---

Comment by mabshoff created at 2009-05-18 18:29:09

Merged in Sage 4.0.rc0.

Cheers,

Michael


---

Comment by mabshoff created at 2009-05-18 18:29:09

Resolution: fixed
