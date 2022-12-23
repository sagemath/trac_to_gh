# Issue 1899: Calling graphs with a matrix and loops=True blows up

Issue created by migration from https://trac.sagemath.org/ticket/1899

Original creator: jason

Original creation time: 2008-01-23 22:19:40

Assignee: rlm


```
sage: Graph(matrix([[1,2],[3,4]]),loops=True)
---------------------------------------------------------------------------
<type 'exceptions.NameError'>             Traceback (most recent call last)

/home/jason/download/sage-2.10-Linux-i686-Linux/devel/sage-main/sage/combinat/<ipython console> in <module>()

/home/was/build/sage-2.10/local/lib/python2.5/site-packages/sage/graphs/graph.py in __init__(self, data, pos, loops, format, boundary, weighted, **kwds)

<type 'exceptions.NameError'>: global name 'multiedges' is not defined
```




---

Attachment


---

Comment by jason created at 2008-01-24 04:01:51

Looks good to me.


---

Comment by mabshoff created at 2008-01-24 04:04:40

Resolution: fixed


---

Comment by mabshoff created at 2008-01-24 04:04:40

Merged in Sage 2.10.1.alpha2
