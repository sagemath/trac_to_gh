# Issue 8640: Add BipartiteGraph to the documentation

Issue created by migration from Trac.

Original creator: ncohen

Original creation time: 2010-04-01 14:32:22

Assignee: mvngu

CC:  rhinton

For the moment, Sage's documentation does not include the BipartiteGraph class. 

For the moment, patches #8329 #8421 and #8425 are still to be merged, and waiting for them to be is a lazy way to avoid conflicts :-)

Nathann


---

Comment by mvngu created at 2010-04-30 21:02:30

Adding the bipartite graph class to the reference manual results in the following warnings:


```
/dev/shm/mvngu/sandbox/sage-4.4.1.alpha2-8640-bipartite/local/lib/python2.6/site-packages/sage/graphs/bipartite_graph.py:docstring of sage.graphs.bipartite_graph:3: (ERROR/3) Unexpected indentation.
/dev/shm/mvngu/sandbox/sage-4.4.1.alpha2-8640-bipartite/local/lib/python2.6/site-packages/sage/graphs/bipartite_graph.py:docstring of sage.graphs.bipartite_graph.BipartiteGraph:25: (WARNING/2) Literal block expected; none found.
/dev/shm/mvngu/sandbox/sage-4.4.1.alpha2-8640-bipartite/local/lib/python2.6/site-packages/sage/graphs/bipartite_graph.py:docstring of sage.graphs.bipartite_graph.BipartiteGraph.delete_vertex:7: (WARNING/2) Inline interpreted text or phrase reference start-string without end-string.
/dev/shm/mvngu/sandbox/sage-4.4.1.alpha2-8640-bipartite/local/lib/python2.6/site-packages/sage/graphs/bipartite_graph.py:docstring of sage.graphs.bipartite_graph:1: (ERROR/3) Unexpected indentation.
/dev/shm/mvngu/sandbox/sage-4.4.1.alpha2-8640-bipartite/local/lib/python2.6/site-packages/sage/graphs/bipartite_graph.py:docstring of sage.graphs.bipartite_graph.BipartiteGraph.load_afile:5: (WARNING/2) Block quote ends without a blank line; unexpected unindent.
/dev/shm/mvngu/sandbox/sage-4.4.1.alpha2-8640-bipartite/local/lib/python2.6/site-packages/sage/graphs/bipartite_graph.py:docstring of sage.graphs.bipartite_graph:8: (ERROR/3) Unexpected indentation.
/dev/shm/mvngu/sandbox/sage-4.4.1.alpha2-8640-bipartite/local/lib/python2.6/site-packages/sage/graphs/bipartite_graph.py:docstring of sage.graphs.bipartite_graph.BipartiteGraph.load_afile:14: (WARNING/2) Block quote ends without a blank line; unexpected unindent.
/dev/shm/mvngu/sandbox/sage-4.4.1.alpha2-8640-bipartite/local/lib/python2.6/site-packages/sage/graphs/bipartite_graph.py:docstring of sage.graphs.bipartite_graph:17: (ERROR/3) Unexpected indentation.
/dev/shm/mvngu/sandbox/sage-4.4.1.alpha2-8640-bipartite/local/lib/python2.6/site-packages/sage/graphs/bipartite_graph.py:docstring of sage.graphs.bipartite_graph.BipartiteGraph.reduced_adjacency_matrix:16: (WARNING/2) Definition list ends without a blank line; unexpected unindent.
/dev/shm/mvngu/sandbox/sage-4.4.1.alpha2-8640-bipartite/local/lib/python2.6/site-packages/sage/graphs/bipartite_graph.py:docstring of sage.graphs.bipartite_graph.BipartiteGraph:9: (ERROR/3) Unexpected indentation.
/dev/shm/mvngu/sandbox/sage-4.4.1.alpha2-8640-bipartite/local/lib/python2.6/site-packages/sage/graphs/bipartite_graph.py:docstring of sage.graphs.bipartite_graph.BipartiteGraph.save_afile:5: (WARNING/2) Definition list ends without a blank line; unexpected unindent.
/dev/shm/mvngu/sandbox/sage-4.4.1.alpha2-8640-bipartite/local/lib/python2.6/site-packages/sage/graphs/bipartite_graph.py:docstring of sage.graphs.bipartite_graph.BipartiteGraph.save_afile:10: (WARNING/2) Definition list ends without a blank line; unexpected unindent.
```


These warnings must be resolved before we could add the bipartite graph class to the reference manual.


---

Attachment


---

Comment by mvngu created at 2010-04-30 22:54:50

Changing status from new to needs_review.


---

Comment by mvngu created at 2010-04-30 22:57:20

Changes in the patch include:

 * Resolve all the warnings.
 * Clean-ups in accordance with [PEP 008](http://www.python.org/dev/peps/pep-0008/)


---

Comment by wdj created at 2010-05-11 15:25:22

Changing status from needs_review to positive_review.


---

Comment by wdj created at 2010-05-11 15:25:22

Applies to 4.4.2.a0 and build fine. Looks good to me.


---

Comment by mvngu created at 2010-05-12 22:47:52

Resolution: fixed
