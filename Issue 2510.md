# Issue 2510: Sage 2.10.4.a0: sage/graphs/graph_generators.py doctest failure related to #2473

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2008-03-13 20:55:12

Assignee: failure

The following pops up after merging #2473: 

```
sage -t -long devel/sage-main/sage/graphs/graph_generators.py
**********************************************************************
File "graph_generators.py", line 1946:
    sage: posdict_med.show()
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/release-cycle/sage-2.10.4.alpha0/local/lib/python2.5/doctest.py", line 1212, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_36[7]>", line 1, in <module>
        posdict_med.show()###line 1946:
    sage: posdict_med.show()
      File "/scratch/mabshoff/release-cycle/sage-2.10.4.alpha0/local/lib/python2.5/site-packages/sage/graphs/graph.py", line 4766, in show
        heights=heights).show(**kwds)
      File "/scratch/mabshoff/release-cycle/sage-2.10.4.alpha0/local/lib/python2.5/site-packages/sage/graphs/bipartite_graph.py", line 246, in plot
        l_len = len(self.left)
    AttributeError: 'BipartiteGraph' object has no attribute 'left'
**********************************************************************
File "graph_generators.py", line 1956:
    sage: for i in range(3):
       n = []
       for m in range(Integer(3)):
           n.append(g[Integer(3)*i + m].plot(vertex_size=Integer(50), vertex_labels=False))
       j.append(n)
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/release-cycle/sage-2.10.4.alpha0/local/lib/python2.5/doctest.py", line 1212, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_36[11]>", line 4, in <module>
        n.append(g[Integer(3)*i + m].plot(vertex_size=Integer(50), vertex_labels=False))
      File "/scratch/mabshoff/release-cycle/sage-2.10.4.alpha0/local/lib/python2.5/site-packages/sage/graphs/bipartite_graph.py", line 246, in plot
        l_len = len(self.left)
    AttributeError: 'BipartiteGraph' object has no attribute 'left'
**********************************************************************
1 items had failures:
   2 of  20 in __main__.example_36
***Test Failed*** 2 failures.
For whitespace errors, see the file .doctest_graph_generators.py
         [67.8 s]
exit code: 256
```


Cheers,

Michael


---

Comment by jason created at 2008-03-13 21:23:30

The breakage seems to occur in 2473-ref.patch from #2473


---

Attachment

Patch looks good to me. All doctests pass again with this patch applied.


---

Comment by mabshoff created at 2008-03-14 02:25:16

Resolution: fixed


---

Comment by mabshoff created at 2008-03-14 02:25:16

Merged in Sage 2.10.4.alpha0
