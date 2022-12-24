# Issue 8031: make graph_editor also available as a *method* on graphs

archive/issues_008031.json:
```json
{
    "body": "Assignee: @rlmill\n\nCC:  @fchapoton\n\nThis is nice:\n\n\n```\ng = graphs.CompleteGraph(5)\ngraph_editor(g)\n```\n\n\nbut this would be even better:\n\n```\ng = graphs.CompleteGraph(5)\ng.edit()\n```\n\n\nIt could also fit into a framework where we have \"edit\" methods for all kinds of objects in Sage, including matrices, elliptic curves, etc.,.   These could be implemented using `@`interact in many cases. \n\nIssue created by migration from https://trac.sagemath.org/ticket/8031\n\n",
    "created_at": "2010-01-21T20:05:00Z",
    "labels": [
        "graph theory",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "make graph_editor also available as a *method* on graphs",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8031",
    "user": "@williamstein"
}
```
Assignee: @rlmill

CC:  @fchapoton

This is nice:


```
g = graphs.CompleteGraph(5)
graph_editor(g)
```


but this would be even better:

```
g = graphs.CompleteGraph(5)
g.edit()
```


It could also fit into a framework where we have "edit" methods for all kinds of objects in Sage, including matrices, elliptic curves, etc.,.   These could be implemented using `@`interact in many cases. 

Issue created by migration from https://trac.sagemath.org/ticket/8031





---

archive/issue_comments_070156.json:
```json
{
    "body": "Changing component from graph theory to notebook.",
    "created_at": "2014-10-16T08:32:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8031",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8031#issuecomment-70156",
    "user": "@jdemeyer"
}
```

Changing component from graph theory to notebook.



---

archive/issue_comments_070157.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2020-08-18T00:36:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8031",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8031#issuecomment-70157",
    "user": "@mkoeppe"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_070158.json:
```json
{
    "body": "Proposing to close all sagenb tickets as outdated, so that all remaining open tickets in the notebook component are about the Jupyter notebook.",
    "created_at": "2020-08-18T00:36:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8031",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8031#issuecomment-70158",
    "user": "@mkoeppe"
}
```

Proposing to close all sagenb tickets as outdated, so that all remaining open tickets in the notebook component are about the Jupyter notebook.



---

archive/issue_comments_070159.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2020-08-25T09:36:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8031",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8031#issuecomment-70159",
    "user": "@dimpase"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_070160.json:
```json
{
    "body": "Changing keywords from \"\" to \"graph_editor\".",
    "created_at": "2020-09-30T09:19:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8031",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8031#issuecomment-70160",
    "user": "@fchapoton"
}
```

Changing keywords from "" to "graph_editor".



---

archive/issue_comments_070161.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2021-01-01T14:23:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8031",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8031#issuecomment-70161",
    "user": "@fchapoton"
}
```

Resolution: invalid
