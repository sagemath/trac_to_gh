# Issue 3928: multiedge graphs create an edge for each character of a label

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2008-08-22 17:58:49

Assignee: rlm


```
Say, I want to define a multigraph with selfloops, and edge labels..
One way to do this is:

import networkx
G=networkx.XDiGraph(selfloops=True,multiedges=True)
for i in range(3): G.add_node(i)
for i in [(1,1,'hola'),(1,1,'hi'),(1,2,'two'),(1,2,'dos'),
(2,1,'one')]: G.add_edge(i)
G=DiGraph(G)

Now, I would be tempted to just do the following:
G=DiGraph({1:{1:'hola',1:'hi',2:'two',2:'dos'},2:{1:'one'}},
loops=True, multiedges=True)

or trying

import networkx
G=networkx.XDiGraph({1:{1:'hola',1:'hi',2:'two',2:'dos'},2:{1:'one'}},
selfloops=True, multiedges=True)

But in each case  I get:

G.edges()

(1, 1, 'h'), (1, 1, 'i'), (1, 2, 'd'), (1, 2, 'o'), (1, 2, 's'), (2,
1,
'o'), (2, 1, 'n'), (2, 1, 'e')]


Which is not as intended for two reasons:  One is that the labels are
wrong, and the other one is that it created three edges from 1 to 2.
```




---

Comment by rlm created at 2008-08-22 21:48:39

This is an error in input. I don't know how well the documentation explains this, but a dict-of-dicts representing a graph with multi-edges requires that the entries of the inner dicts be lists. That is the syntax. So if the documentation doesn't explain this carefully, it needs to.

The behavior you are getting is *exactly* as intended.


---

Comment by jason created at 2008-08-23 03:56:31

Resolution: invalid


---

Comment by jason created at 2008-08-23 03:56:31

Indeed, the following works:


```
sage: G=DiGraph({1:{1:['hola','hi'], 2:['two','dos']},2:{1:['one']}}, loops=True, multiedges=True)
sage: G.edges()
[(1, 1, 'hi'), (1, 1, 'hola'), (1, 2, 'dos'), (1, 2, 'two'), (2, 1, 'one')]

```



---

Comment by jason created at 2008-08-26 15:43:31

Changing priority from major to minor.


---

Comment by jason created at 2008-08-26 15:43:31

Changing status from closed to reopened.


---

Comment by jason created at 2008-08-26 15:43:31

Changing type from defect to enhancement.


---

Comment by jason created at 2008-08-26 15:43:31

As per Robert's comment and the suggestion on sage-devel to add documentation, I'm reopening this to add the following to the documentation:


```
For a digraph with multiple edges and labels, one must provide a list
within the dictionary:

sage: G=DiGraph({1:{1:['hola','hi'], 2:['two','dos']},2:{1:['one']}},
loops=True, multiedges=True)
sage: G.edges()
[(1, 1, 'hi'), (1, 1, 'hola'), (1, 2, 'dos'), (1, 2, 'two'), (2, 1,
'one')]
```



---

Comment by jason created at 2008-08-26 15:43:31

Resolution changed from invalid to 


---

Comment by mabshoff created at 2008-08-26 16:53:15

This is a *new* ticket - don't reopen closed tickets and reuse them for something related.

Cheers,

Michael


---

Comment by mabshoff created at 2008-08-26 16:53:15

Resolution: invalid
