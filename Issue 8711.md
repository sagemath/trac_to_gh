# Issue 8711: fix warnings when building the ref manual (4.4.alpha0)

Issue created by migration from https://trac.sagemath.org/ticket/8711

Original creator: jhpalmieri

Original creation time: 2010-04-18 04:45:17

Assignee: mvngu

Here is a patch to fix the warnings...


---

Comment by mvngu created at 2010-04-18 07:06:56

Changing status from new to needs_review.


---

Attachment


---

Comment by mvngu created at 2010-04-18 07:07:39

Changing status from needs_review to positive_review.


---

Comment by mvngu created at 2010-04-18 07:07:39

Building the reference manual of Sage 4.4.alpha0 results in the following warnings:

```
/dev/shm/mvngu/sandbox/sage-4.4.alpha0-8711-ref/local/lib/python2.6/site-packages/sage/graphs/generic_graph.py:docstring of sage.graphs.generic_graph.GenericGraph.add_cycle:5: (ERROR/3) Unexpected indentation.
/dev/shm/mvngu/sandbox/sage-4.4.alpha0-8711-ref/local/lib/python2.6/site-packages/sage/graphs/generic_graph.py:docstring of sage.graphs.generic_graph.GenericGraph.vertex_cover:26: (WARNING/2) Block quote ends without a blank line; unexpected unindent.
/dev/shm/mvngu/sandbox/sage-4.4.alpha0-8711-ref/local/lib/python2.6/site-packages/sage/symbolic/units.py:docstring of sage.symbolic.units.unitdocs:15: (WARNING/2) Block quote ends without a blank line; unexpected unindent.
/dev/shm/mvngu/sandbox/sage-4.4.alpha0-8711-ref/local/lib/python2.6/site-packages/sage/symbolic/units.py:docstring of sage.symbolic.units.unitdocs:18: (WARNING/2) Definition list ends without a blank line; unexpected unindent.
```

The attached patch resolves those warnings as claimed.


---

Comment by jhpalmieri created at 2010-04-19 05:18:58

Merged "trac_8711-reference44alpha0.patch" into 4.4.alpha1.


---

Comment by jhpalmieri created at 2010-04-19 05:18:58

Resolution: fixed
