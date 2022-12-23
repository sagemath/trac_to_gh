# Issue 2510: Sage 2.10.4.a0: sage/graphs/graph_generators.py doctest failure related to #2473

archive/issues_002510.json:
```json
{
    "body": "Assignee: failure\n\nThe following pops up after merging #2473: \n\n```\nsage -t -long devel/sage-main/sage/graphs/graph_generators.py\n**********************************************************************\nFile \"graph_generators.py\", line 1946:\n    sage: posdict_med.show()\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/mabshoff/release-cycle/sage-2.10.4.alpha0/local/lib/python2.5/doctest.py\", line 1212, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_36[7]>\", line 1, in <module>\n        posdict_med.show()###line 1946:\n    sage: posdict_med.show()\n      File \"/scratch/mabshoff/release-cycle/sage-2.10.4.alpha0/local/lib/python2.5/site-packages/sage/graphs/graph.py\", line 4766, in show\n        heights=heights).show(**kwds)\n      File \"/scratch/mabshoff/release-cycle/sage-2.10.4.alpha0/local/lib/python2.5/site-packages/sage/graphs/bipartite_graph.py\", line 246, in plot\n        l_len = len(self.left)\n    AttributeError: 'BipartiteGraph' object has no attribute 'left'\n**********************************************************************\nFile \"graph_generators.py\", line 1956:\n    sage: for i in range(3):\n       n = []\n       for m in range(Integer(3)):\n           n.append(g[Integer(3)*i + m].plot(vertex_size=Integer(50), vertex_labels=False))\n       j.append(n)\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/mabshoff/release-cycle/sage-2.10.4.alpha0/local/lib/python2.5/doctest.py\", line 1212, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_36[11]>\", line 4, in <module>\n        n.append(g[Integer(3)*i + m].plot(vertex_size=Integer(50), vertex_labels=False))\n      File \"/scratch/mabshoff/release-cycle/sage-2.10.4.alpha0/local/lib/python2.5/site-packages/sage/graphs/bipartite_graph.py\", line 246, in plot\n        l_len = len(self.left)\n    AttributeError: 'BipartiteGraph' object has no attribute 'left'\n**********************************************************************\n1 items had failures:\n   2 of  20 in __main__.example_36\n***Test Failed*** 2 failures.\nFor whitespace errors, see the file .doctest_graph_generators.py\n         [67.8 s]\nexit code: 256\n```\n\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/2510\n\n",
    "created_at": "2008-03-13T20:55:12Z",
    "labels": [
        "doctest coverage",
        "blocker",
        "bug"
    ],
    "title": "Sage 2.10.4.a0: sage/graphs/graph_generators.py doctest failure related to #2473",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2510",
    "user": "mabshoff"
}
```
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

Issue created by migration from https://trac.sagemath.org/ticket/2510





---

archive/issue_comments_017025.json:
```json
{
    "body": "The breakage seems to occur in 2473-ref.patch from #2473",
    "created_at": "2008-03-13T21:23:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2510",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2510#issuecomment-17025",
    "user": "jason"
}
```

The breakage seems to occur in 2473-ref.patch from #2473



---

archive/issue_comments_017026.json:
```json
{
    "body": "Attachment\n\nPatch looks good to me. All doctests pass again with this patch applied.",
    "created_at": "2008-03-14T02:24:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2510",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2510#issuecomment-17026",
    "user": "mabshoff"
}
```

Attachment

Patch looks good to me. All doctests pass again with this patch applied.



---

archive/issue_comments_017027.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-14T02:25:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2510",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2510#issuecomment-17027",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_017028.json:
```json
{
    "body": "Merged in Sage 2.10.4.alpha0",
    "created_at": "2008-03-14T02:25:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2510",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2510#issuecomment-17028",
    "user": "mabshoff"
}
```

Merged in Sage 2.10.4.alpha0
