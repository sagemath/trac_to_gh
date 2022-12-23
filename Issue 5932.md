# Issue 5932: graphs.RandomRegular(3,10) often returns a graph on 0 vertices

Issue created by migration from https://trac.sagemath.org/ticket/5932

Original creator: was

Original creation time: 2009-04-29 05:21:23

Assignee: rlm

The docstring for graphs.RandomRegular says

```
Returns a random d-regular graph on n vertices, or returns False on
failure.
```


However, try calling it a few times with input 3,10 and with probability about 25% you'll get back an empty graph!:

```
sage: graphs.RandomRegular(3,10)
Graph on 0 vertices

sage: [len(graphs.RandomRegular(3,10)) for _ in range(1000)].count(0)
232
```




---

Comment by rlm created at 2009-04-29 16:09:31

This is a bug in NetworkX. Their docstring says:


```
Definition:     networkx.random_regular_graph(d, n, seed=None)
Source:
def random_regular_graph(d, n, seed=None):
    """Return a random regular graph of n nodes each with degree d, G_{n,d}.
    Return False if unsuccessful.
```



---

Attachment


---

Comment by jason created at 2009-07-18 23:35:14

The fix looks correct, the file passes doctests, and everything looks great!


---

Comment by mvngu created at 2009-07-19 12:02:06

Resolution: fixed
