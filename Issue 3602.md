# Issue 3602: weird bug in group.pyx -- something about latexing a graph

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-07-08 06:24:09

Assignee: rlm


```
sage -t  devel/sage/sage/groups/group.pyx                   **********************************************************************
File "/Users/was/build/sage-3.0.4.rc0/tmp/group.py", line 139:
    sage: show(G, color_by_label=True, edge_labels=True)
Exception raised:
    Traceback (most recent call last):
      File "/Users/was/build/sage-3.0.4.rc0/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_17[3]>", line 1, in <module>
        show(G, color_by_label=True, edge_labels=True)###line 139:
    sage: show(G, color_by_label=True, edge_labels=True)
      File "/Users/was/build/sage-3.0.4.rc0/local/lib/python2.5/site-packages/sage/misc/functional.py", line 916, in show
        _do_show(x)
      File "/Users/was/build/sage-3.0.4.rc0/local/lib/python2.5/site-packages/sage/misc/functional.py", line 923, in _do_show
        return sage.misc.latex.latex(x)
      File "/Users/was/build/sage-3.0.4.rc0/local/lib/python2.5/site-packages/sage/misc/latex.py", line 137, in latex
        return LatexExpr(x._latex_())
      File "/Users/was/build/sage-3.0.4.rc0/local/lib/python2.5/site-packages/sage/graphs/graph.py", line 497, in _latex_
        raise NotImplementedError('To include a graph in LaTeX document, see function Graph.write_to_eps().')
    NotImplementedError: To include a graph in LaTeX document, see function Graph.write_to_eps().
**********************************************************************
1 items had failures:
   1 of   8 in __main__.example_17
***Test Failed*** 1 failures.
For whitespace errors, see the file /Users/was/build/sage-3.0.4.rc0/tmp/.doctest_group.py
         [15.2 s]
```



---

Comment by was created at 2008-07-08 06:39:44

This is a weird heisenbug.  On exactly the same machine it doesn't happen anymore.  Very weird. 

```
fermat:sage-3.0.4.rc0 was$ ./sage -t devel/sage/sage/groups/group.pyx
sage -t  devel/sage/sage/groups/group.pyx                   
	 [20.4 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 20.4 seconds
fermat:sage-3.0.4.rc0 was$ ./sage -t devel/sage/sage/groups/group.pyx
sage -t  devel/sage/sage/groups/group.pyx                   
	 [19.9 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 19.9 seconds
```



---

Comment by was created at 2008-07-08 06:39:44

Resolution: invalid
