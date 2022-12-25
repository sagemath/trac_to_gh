# Issue 8640: Add BipartiteGraph to the documentation

archive/issues_008640.json:
```json
{
    "body": "Assignee: mvngu\n\nCC:  @rhinton\n\nFor the moment, Sage's documentation does not include the BipartiteGraph class. \n\nFor the moment, patches #8329 #8421 and #8425 are still to be merged, and waiting for them to be is a lazy way to avoid conflicts :-)\n\nNathann\n\nIssue created by migration from https://trac.sagemath.org/ticket/8640\n\n",
    "created_at": "2010-04-01T14:32:22Z",
    "labels": [
        "component: documentation",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4.2",
    "title": "Add BipartiteGraph to the documentation",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8640",
    "user": "https://github.com/nathanncohen"
}
```
Assignee: mvngu

CC:  @rhinton

For the moment, Sage's documentation does not include the BipartiteGraph class. 

For the moment, patches #8329 #8421 and #8425 are still to be merged, and waiting for them to be is a lazy way to avoid conflicts :-)

Nathann

Issue created by migration from https://trac.sagemath.org/ticket/8640





---

archive/issue_comments_078213.json:
```json
{
    "body": "Adding the bipartite graph class to the reference manual results in the following warnings:\n\n\n```\n/dev/shm/mvngu/sandbox/sage-4.4.1.alpha2-8640-bipartite/local/lib/python2.6/site-packages/sage/graphs/bipartite_graph.py:docstring of sage.graphs.bipartite_graph:3: (ERROR/3) Unexpected indentation.\n/dev/shm/mvngu/sandbox/sage-4.4.1.alpha2-8640-bipartite/local/lib/python2.6/site-packages/sage/graphs/bipartite_graph.py:docstring of sage.graphs.bipartite_graph.BipartiteGraph:25: (WARNING/2) Literal block expected; none found.\n/dev/shm/mvngu/sandbox/sage-4.4.1.alpha2-8640-bipartite/local/lib/python2.6/site-packages/sage/graphs/bipartite_graph.py:docstring of sage.graphs.bipartite_graph.BipartiteGraph.delete_vertex:7: (WARNING/2) Inline interpreted text or phrase reference start-string without end-string.\n/dev/shm/mvngu/sandbox/sage-4.4.1.alpha2-8640-bipartite/local/lib/python2.6/site-packages/sage/graphs/bipartite_graph.py:docstring of sage.graphs.bipartite_graph:1: (ERROR/3) Unexpected indentation.\n/dev/shm/mvngu/sandbox/sage-4.4.1.alpha2-8640-bipartite/local/lib/python2.6/site-packages/sage/graphs/bipartite_graph.py:docstring of sage.graphs.bipartite_graph.BipartiteGraph.load_afile:5: (WARNING/2) Block quote ends without a blank line; unexpected unindent.\n/dev/shm/mvngu/sandbox/sage-4.4.1.alpha2-8640-bipartite/local/lib/python2.6/site-packages/sage/graphs/bipartite_graph.py:docstring of sage.graphs.bipartite_graph:8: (ERROR/3) Unexpected indentation.\n/dev/shm/mvngu/sandbox/sage-4.4.1.alpha2-8640-bipartite/local/lib/python2.6/site-packages/sage/graphs/bipartite_graph.py:docstring of sage.graphs.bipartite_graph.BipartiteGraph.load_afile:14: (WARNING/2) Block quote ends without a blank line; unexpected unindent.\n/dev/shm/mvngu/sandbox/sage-4.4.1.alpha2-8640-bipartite/local/lib/python2.6/site-packages/sage/graphs/bipartite_graph.py:docstring of sage.graphs.bipartite_graph:17: (ERROR/3) Unexpected indentation.\n/dev/shm/mvngu/sandbox/sage-4.4.1.alpha2-8640-bipartite/local/lib/python2.6/site-packages/sage/graphs/bipartite_graph.py:docstring of sage.graphs.bipartite_graph.BipartiteGraph.reduced_adjacency_matrix:16: (WARNING/2) Definition list ends without a blank line; unexpected unindent.\n/dev/shm/mvngu/sandbox/sage-4.4.1.alpha2-8640-bipartite/local/lib/python2.6/site-packages/sage/graphs/bipartite_graph.py:docstring of sage.graphs.bipartite_graph.BipartiteGraph:9: (ERROR/3) Unexpected indentation.\n/dev/shm/mvngu/sandbox/sage-4.4.1.alpha2-8640-bipartite/local/lib/python2.6/site-packages/sage/graphs/bipartite_graph.py:docstring of sage.graphs.bipartite_graph.BipartiteGraph.save_afile:5: (WARNING/2) Definition list ends without a blank line; unexpected unindent.\n/dev/shm/mvngu/sandbox/sage-4.4.1.alpha2-8640-bipartite/local/lib/python2.6/site-packages/sage/graphs/bipartite_graph.py:docstring of sage.graphs.bipartite_graph.BipartiteGraph.save_afile:10: (WARNING/2) Definition list ends without a blank line; unexpected unindent.\n```\n\n\nThese warnings must be resolved before we could add the bipartite graph class to the reference manual.",
    "created_at": "2010-04-30T21:02:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8640",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8640#issuecomment-78213",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

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

archive/issue_comments_078214.json:
```json
{
    "body": "Attachment [trac_8640-bipartite.patch](tarball://root/attachments/some-uuid/ticket8640/trac_8640-bipartite.patch) by mvngu created at 2010-04-30 22:53:06",
    "created_at": "2010-04-30T22:53:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8640",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8640#issuecomment-78214",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Attachment [trac_8640-bipartite.patch](tarball://root/attachments/some-uuid/ticket8640/trac_8640-bipartite.patch) by mvngu created at 2010-04-30 22:53:06



---

archive/issue_comments_078215.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-04-30T22:54:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8640",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8640#issuecomment-78215",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_078216.json:
```json
{
    "body": "Changes in the patch include:\n\n* Resolve all the warnings.\n* Clean-ups in accordance with [PEP 008](http://www.python.org/dev/peps/pep-0008/)",
    "created_at": "2010-04-30T22:57:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8640",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8640#issuecomment-78216",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Changes in the patch include:

* Resolve all the warnings.
* Clean-ups in accordance with [PEP 008](http://www.python.org/dev/peps/pep-0008/)



---

archive/issue_comments_078217.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-05-11T15:25:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8640",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8640#issuecomment-78217",
    "user": "https://github.com/wdjoyner"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_078218.json:
```json
{
    "body": "Applies to 4.4.2.a0 and build fine. Looks good to me.",
    "created_at": "2010-05-11T15:25:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8640",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8640#issuecomment-78218",
    "user": "https://github.com/wdjoyner"
}
```

Applies to 4.4.2.a0 and build fine. Looks good to me.



---

archive/issue_comments_078219.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-05-12T22:47:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8640",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8640#issuecomment-78219",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed
