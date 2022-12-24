# Issue 4852: graph plotting using @option and @suboption

archive/issues_004852.json:
```json
{
    "body": "Assignee: rlm\n\nCC:  ekirkman\n\nWe really probably ought to use the very nice `@`option and `@`suboption functionality for doing plots of graphs. That would make it easier to specify edge/vertex options, for example, and to retrieve existing defaults, etc.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4852\n\n",
    "created_at": "2008-12-22T18:37:25Z",
    "labels": [
        "graph theory",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "graph plotting using @option and @suboption",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4852",
    "user": "jason"
}
```
Assignee: rlm

CC:  ekirkman

We really probably ought to use the very nice `@`option and `@`suboption functionality for doing plots of graphs. That would make it easier to specify edge/vertex options, for example, and to retrieve existing defaults, etc.


Issue created by migration from https://trac.sagemath.org/ticket/4852





---

archive/issue_comments_036785.json:
```json
{
    "body": "Changing assignee from rlm to jason.",
    "created_at": "2008-12-22T18:40:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4852",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4852#issuecomment-36785",
    "user": "jason"
}
```

Changing assignee from rlm to jason.



---

archive/issue_comments_036786.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-12-22T18:40:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4852",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4852#issuecomment-36786",
    "user": "jason"
}
```

Changing status from new to assigned.



---

archive/issue_comments_036787.json:
```json
{
    "body": "Emily was working on this at one point. I don't know where that code is now...",
    "created_at": "2008-12-22T19:06:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4852",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4852#issuecomment-36787",
    "user": "rlm"
}
```

Emily was working on this at one point. I don't know where that code is now...



---

archive/issue_comments_036788.json:
```json
{
    "body": "This is related a little to #2817.\n\nEmily, were you working on using `@`option and `@`suboption to plot graphs?",
    "created_at": "2008-12-23T03:00:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4852",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4852#issuecomment-36788",
    "user": "jason"
}
```

This is related a little to #2817.

Emily, were you working on using `@`option and `@`suboption to plot graphs?



---

archive/issue_comments_036789.json:
```json
{
    "body": "Graph plots currently use `@`option. See `sage/graphs/graph_plot.py`\n\n\n...invalid?",
    "created_at": "2009-07-13T21:34:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4852",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4852#issuecomment-36789",
    "user": "rlm"
}
```

Graph plots currently use `@`option. See `sage/graphs/graph_plot.py`


...invalid?



---

archive/issue_comments_036790.json:
```json
{
    "body": "> Graph plots currently use `@`option. See `sage/graphs/graph_plot.py`\n\nOr at least see `sage.graphs.generic_graph.py`, in particular (in Sage 5.0) [http://hg.sagemath.org/sage-main/file/9ab4ab6e12d0/sage/graphs/generic_graph.py#l13907](http://hg.sagemath.org/sage-main/file/9ab4ab6e12d0/sage/graphs/generic_graph.py#l13907)\n\n> \n> ...invalid?\n\nProbably it could be improved somehow, but we'd want a more specific ticket for this.  Jason, I'm recommending closing this - speak now!",
    "created_at": "2012-06-01T18:55:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4852",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4852#issuecomment-36790",
    "user": "kcrisman"
}
```

> Graph plots currently use `@`option. See `sage/graphs/graph_plot.py`

Or at least see `sage.graphs.generic_graph.py`, in particular (in Sage 5.0) [http://hg.sagemath.org/sage-main/file/9ab4ab6e12d0/sage/graphs/generic_graph.py#l13907](http://hg.sagemath.org/sage-main/file/9ab4ab6e12d0/sage/graphs/generic_graph.py#l13907)

> 
> ...invalid?

Probably it could be improved somehow, but we'd want a more specific ticket for this.  Jason, I'm recommending closing this - speak now!



---

archive/issue_comments_036791.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2012-06-01T18:55:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4852",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4852#issuecomment-36791",
    "user": "kcrisman"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_036792.json:
```json
{
    "body": "+1 to closing this vague ticket that seems to be minimally satisfied.",
    "created_at": "2012-06-01T18:58:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4852",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4852#issuecomment-36792",
    "user": "jason"
}
```

+1 to closing this vague ticket that seems to be minimally satisfied.



---

archive/issue_comments_036793.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2012-06-01T19:00:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4852",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4852#issuecomment-36793",
    "user": "kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_036794.json:
```json
{
    "body": "Great.",
    "created_at": "2012-06-01T19:00:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4852",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4852#issuecomment-36794",
    "user": "kcrisman"
}
```

Great.



---

archive/issue_comments_036795.json:
```json
{
    "body": "Resolution: worksforme",
    "created_at": "2012-06-02T12:33:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4852",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4852#issuecomment-36795",
    "user": "jdemeyer"
}
```

Resolution: worksforme
