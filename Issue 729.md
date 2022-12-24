# Issue 729: graphs: Implement __eq__ and __neq__ rather than __cmp__

archive/issues_000729.json:
```json
{
    "body": "Assignee: @williamstein\n\nKeywords: graphs\n\nThe rich comparison operators __eq__ and __neq__ are preferred in Python.  See [http://docs.python.org/ref/customization.html](http://docs.python.org/ref/customization.html)\n\nIssue created by migration from https://trac.sagemath.org/ticket/729\n\n",
    "created_at": "2007-09-21T17:56:12Z",
    "labels": [
        "combinatorics",
        "trivial",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.9",
    "title": "graphs: Implement __eq__ and __neq__ rather than __cmp__",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/729",
    "user": "@jasongrout"
}
```
Assignee: @williamstein

Keywords: graphs

The rich comparison operators __eq__ and __neq__ are preferred in Python.  See [http://docs.python.org/ref/customization.html](http://docs.python.org/ref/customization.html)

Issue created by migration from https://trac.sagemath.org/ticket/729





---

archive/issue_comments_004278.json:
```json
{
    "body": "This is actually crucial in the graph_isom code: there, not just equality comparison, but actually finding which graph is smaller is important. There is a specific enumeration of graphs coded, and under that enumeration, __cmp__ gives exactly what it means. This method cannot be removed.",
    "created_at": "2007-10-22T01:36:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/729",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/729#issuecomment-4278",
    "user": "@rlmill"
}
```

This is actually crucial in the graph_isom code: there, not just equality comparison, but actually finding which graph is smaller is important. There is a specific enumeration of graphs coded, and under that enumeration, __cmp__ gives exactly what it means. This method cannot be removed.



---

archive/issue_comments_004279.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2007-10-22T01:36:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/729",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/729#issuecomment-4279",
    "user": "@rlmill"
}
```

Resolution: invalid



---

archive/issue_comments_004280.json:
```json
{
    "body": "Please do not close tickets unless explicitly asked to do so. You can recommend to close a ticket.\n\nCheers,\n\nMichael",
    "created_at": "2007-10-22T07:03:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/729",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/729#issuecomment-4280",
    "user": "mabshoff"
}
```

Please do not close tickets unless explicitly asked to do so. You can recommend to close a ticket.

Cheers,

Michael



---

archive/issue_comments_004281.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2007-10-22T07:03:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/729",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/729#issuecomment-4281",
    "user": "mabshoff"
}
```

Changing status from closed to reopened.



---

archive/issue_comments_004282.json:
```json
{
    "body": "Resolution changed from invalid to ",
    "created_at": "2007-10-22T07:03:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/729",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/729#issuecomment-4282",
    "user": "mabshoff"
}
```

Resolution changed from invalid to 



---

archive/issue_comments_004283.json:
```json
{
    "body": "Actually, I was wrong on two counts - count 1, the graph_isom code actually re-implements the enumeration, so it doesn't actually depend on __cmp__, and count 2, you're right about rich comparison, but instead of just __eq__ and __neq__, there should also be __lt__, __le__, etc. However, this would all be part of an overhaul on how graph enumeration is done in general, so this could be part of ticket #749.",
    "created_at": "2007-10-22T16:30:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/729",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/729#issuecomment-4283",
    "user": "@rlmill"
}
```

Actually, I was wrong on two counts - count 1, the graph_isom code actually re-implements the enumeration, so it doesn't actually depend on __cmp__, and count 2, you're right about rich comparison, but instead of just __eq__ and __neq__, there should also be __lt__, __le__, etc. However, this would all be part of an overhaul on how graph enumeration is done in general, so this could be part of ticket #749.



---

archive/issue_comments_004284.json:
```json
{
    "body": "This is duplicate because #749 takes care of it.",
    "created_at": "2007-10-23T18:01:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/729",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/729#issuecomment-4284",
    "user": "@malb"
}
```

This is duplicate because #749 takes care of it.



---

archive/issue_comments_004285.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2007-10-23T18:01:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/729",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/729#issuecomment-4285",
    "user": "@malb"
}
```

Resolution: duplicate
