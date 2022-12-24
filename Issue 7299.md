# Issue 7299: show() regression: Picture cropped too much

archive/issues_007299.json:
```json
{
    "body": "Assignee: was\n\nCC:  rlm rbeezer\n\nIn sage 4.1.2 and later, the show() function shows graphs so cropped that their vertices are partially missing.\n\nThis is a regression in 4.1.2 and later, Sage 4.1.1 is fine.\n\nAttaching the figures from\n\n```\nG=graphs.CycleGraph(3);G.show()\n```\n\nto show the issue.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7299\n\n",
    "created_at": "2009-10-25T18:26:25Z",
    "labels": [
        "graphics",
        "major",
        "bug"
    ],
    "title": "show() regression: Picture cropped too much",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7299",
    "user": "AJonsson"
}
```
Assignee: was

CC:  rlm rbeezer

In sage 4.1.2 and later, the show() function shows graphs so cropped that their vertices are partially missing.

This is a regression in 4.1.2 and later, Sage 4.1.1 is fine.

Attaching the figures from

```
G=graphs.CycleGraph(3);G.show()
```

to show the issue.

Issue created by migration from https://trac.sagemath.org/ticket/7299





---

archive/issue_comments_060836.json:
```json
{
    "body": "Attachment [Triangle-sage_4.1.1.png](tarball://root/attachments/some-uuid/ticket7299/Triangle-sage_4.1.1.png) by AJonsson created at 2009-10-25 18:27:11\n\nTriangle graph in 4.1.1",
    "created_at": "2009-10-25T18:27:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7299",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7299#issuecomment-60836",
    "user": "AJonsson"
}
```

Attachment [Triangle-sage_4.1.1.png](tarball://root/attachments/some-uuid/ticket7299/Triangle-sage_4.1.1.png) by AJonsson created at 2009-10-25 18:27:11

Triangle graph in 4.1.1



---

archive/issue_comments_060837.json:
```json
{
    "body": "Attachment [Triangle-Sage_4.1.2.png](tarball://root/attachments/some-uuid/ticket7299/Triangle-Sage_4.1.2.png) by AJonsson created at 2009-10-25 18:27:32\n\nTriangle graph in 4.1.2",
    "created_at": "2009-10-25T18:27:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7299",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7299#issuecomment-60837",
    "user": "AJonsson"
}
```

Attachment [Triangle-Sage_4.1.2.png](tarball://root/attachments/some-uuid/ticket7299/Triangle-Sage_4.1.2.png) by AJonsson created at 2009-10-25 18:27:32

Triangle graph in 4.1.2



---

archive/issue_comments_060838.json:
```json
{
    "body": "Attachment [trac-7299-graph-pad.patch](tarball://root/attachments/some-uuid/ticket7299/trac-7299-graph-pad.patch) by jason created at 2010-01-20 10:54:19",
    "created_at": "2010-01-20T10:54:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7299",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7299#issuecomment-60838",
    "user": "jason"
}
```

Attachment [trac-7299-graph-pad.patch](tarball://root/attachments/some-uuid/ticket7299/trac-7299-graph-pad.patch) by jason created at 2010-01-20 10:54:19



---

archive/issue_comments_060839.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-20T10:54:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7299",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7299#issuecomment-60839",
    "user": "jason"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_060840.json:
```json
{
    "body": "The attached patch is a one-line fix that makes graph vertices not be cut off now.",
    "created_at": "2010-01-20T10:54:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7299",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7299#issuecomment-60840",
    "user": "jason"
}
```

The attached patch is a one-line fix that makes graph vertices not be cut off now.



---

archive/issue_comments_060841.json:
```json
{
    "body": "LGTM. Such a small change for a big impact.",
    "created_at": "2010-01-20T10:58:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7299",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7299#issuecomment-60841",
    "user": "robertwb"
}
```

LGTM. Such a small change for a big impact.



---

archive/issue_comments_060842.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-20T10:58:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7299",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7299#issuecomment-60842",
    "user": "robertwb"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_060843.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-23T22:45:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7299",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7299#issuecomment-60843",
    "user": "mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_060844.json:
```json
{
    "body": "Merged [trac-7299-graph-pad.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7299/trac-7299-graph-pad.patch).",
    "created_at": "2010-01-23T22:45:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7299",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7299#issuecomment-60844",
    "user": "mvngu"
}
```

Merged [trac-7299-graph-pad.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7299/trac-7299-graph-pad.patch).
