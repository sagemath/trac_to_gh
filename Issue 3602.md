# Issue 3602: weird bug in group.pyx -- something about latexing a graph

archive/issues_003602.json:
```json
{
    "body": "Assignee: @rlmill\n\n\n```\nsage -t  devel/sage/sage/groups/group.pyx                   **********************************************************************\nFile \"/Users/was/build/sage-3.0.4.rc0/tmp/group.py\", line 139:\n    sage: show(G, color_by_label=True, edge_labels=True)\nException raised:\n    Traceback (most recent call last):\n      File \"/Users/was/build/sage-3.0.4.rc0/local/lib/python2.5/doctest.py\", line 1228, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_17[3]>\", line 1, in <module>\n        show(G, color_by_label=True, edge_labels=True)###line 139:\n    sage: show(G, color_by_label=True, edge_labels=True)\n      File \"/Users/was/build/sage-3.0.4.rc0/local/lib/python2.5/site-packages/sage/misc/functional.py\", line 916, in show\n        _do_show(x)\n      File \"/Users/was/build/sage-3.0.4.rc0/local/lib/python2.5/site-packages/sage/misc/functional.py\", line 923, in _do_show\n        return sage.misc.latex.latex(x)\n      File \"/Users/was/build/sage-3.0.4.rc0/local/lib/python2.5/site-packages/sage/misc/latex.py\", line 137, in latex\n        return LatexExpr(x._latex_())\n      File \"/Users/was/build/sage-3.0.4.rc0/local/lib/python2.5/site-packages/sage/graphs/graph.py\", line 497, in _latex_\n        raise NotImplementedError('To include a graph in LaTeX document, see function Graph.write_to_eps().')\n    NotImplementedError: To include a graph in LaTeX document, see function Graph.write_to_eps().\n**********************************************************************\n1 items had failures:\n   1 of   8 in __main__.example_17\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file /Users/was/build/sage-3.0.4.rc0/tmp/.doctest_group.py\n         [15.2 s]\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3602\n\n",
    "created_at": "2008-07-08T06:24:09Z",
    "labels": [
        "graph theory",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.4",
    "title": "weird bug in group.pyx -- something about latexing a graph",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3602",
    "user": "@williamstein"
}
```
Assignee: @rlmill


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


Issue created by migration from https://trac.sagemath.org/ticket/3602





---

archive/issue_comments_025461.json:
```json
{
    "body": "This is a weird heisenbug.  On exactly the same machine it doesn't happen anymore.  Very weird. \n\n```\nfermat:sage-3.0.4.rc0 was$ ./sage -t devel/sage/sage/groups/group.pyx\nsage -t  devel/sage/sage/groups/group.pyx                   \n\t [20.4 s]\n \n----------------------------------------------------------------------\nAll tests passed!\nTotal time for all tests: 20.4 seconds\nfermat:sage-3.0.4.rc0 was$ ./sage -t devel/sage/sage/groups/group.pyx\nsage -t  devel/sage/sage/groups/group.pyx                   \n\t [19.9 s]\n \n----------------------------------------------------------------------\nAll tests passed!\nTotal time for all tests: 19.9 seconds\n```\n",
    "created_at": "2008-07-08T06:39:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3602",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3602#issuecomment-25461",
    "user": "@williamstein"
}
```

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

archive/issue_comments_025462.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2008-07-08T06:39:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3602",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3602#issuecomment-25462",
    "user": "@williamstein"
}
```

Resolution: invalid
