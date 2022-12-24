# Issue 6540: [with patch, needs review] g.add_edge((u,v), label=l) syntax unsupported for C graphs

archive/issues_006540.json:
```json
{
    "body": "Assignee: @rlmill\n\nCC:  @jasongrout\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6540\n\n",
    "created_at": "2009-07-16T00:53:02Z",
    "labels": [
        "graph theory",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.1",
    "title": "[with patch, needs review] g.add_edge((u,v), label=l) syntax unsupported for C graphs",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6540",
    "user": "@rlmill"
}
```
Assignee: @rlmill

CC:  @jasongrout



Issue created by migration from https://trac.sagemath.org/ticket/6540





---

archive/issue_comments_053321.json:
```json
{
    "body": "Attachment [trac_6540-edge_syntax.patch](tarball://root/attachments/some-uuid/ticket6540/trac_6540-edge_syntax.patch) by @jasongrout created at 2009-07-17 19:19:10",
    "created_at": "2009-07-17T19:19:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6540",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6540#issuecomment-53321",
    "user": "@jasongrout"
}
```

Attachment [trac_6540-edge_syntax.patch](tarball://root/attachments/some-uuid/ticket6540/trac_6540-edge_syntax.patch) by @jasongrout created at 2009-07-17 19:19:10



---

archive/issue_comments_053322.json:
```json
{
    "body": "This looks good and passes tests in graph.py.\n\nThe function has a blanket except: statement, which should instead trap the specific error it is expecting.  But that is not this issue.\n\nAs a side note, I think there are too many syntax choices for creating edges, which not only creates obscure corner cases and parsing code like this, but also leads to code that goes against the python philosophy that there should be one way to do things (\"http://trac.sagemath.org/sage_trac/raw-attachment/ticket/6540/trac_6540-edge_syntax.patch\").  I don't have time to do anything about it, so this is just a hollow complaint now :).",
    "created_at": "2009-07-18T22:09:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6540",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6540#issuecomment-53322",
    "user": "@jasongrout"
}
```

This looks good and passes tests in graph.py.

The function has a blanket except: statement, which should instead trap the specific error it is expecting.  But that is not this issue.

As a side note, I think there are too many syntax choices for creating edges, which not only creates obscure corner cases and parsing code like this, but also leads to code that goes against the python philosophy that there should be one way to do things ("http://trac.sagemath.org/sage_trac/raw-attachment/ticket/6540/trac_6540-edge_syntax.patch").  I don't have time to do anything about it, so this is just a hollow complaint now :).



---

archive/issue_comments_053323.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-07-19T14:04:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6540",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6540#issuecomment-53323",
    "user": "mvngu"
}
```

Resolution: fixed
