# Issue 1088: [with patch] graphs: minimum spanning tree function

archive/issues_001088.json:
```json
{
    "body": "Assignee: mhansen\n\nKeywords: graphs\n\nHere's an implementation of a minimum spanning tree function.  Well, actually 3 implementations, defaulting to Kruskal's algorithm.\n\nIssue created by migration from https://trac.sagemath.org/ticket/1088\n\n",
    "created_at": "2007-11-03T20:45:05Z",
    "labels": [
        "combinatorics",
        "major",
        "enhancement"
    ],
    "title": "[with patch] graphs: minimum spanning tree function",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1088",
    "user": "jason"
}
```
Assignee: mhansen

Keywords: graphs

Here's an implementation of a minimum spanning tree function.  Well, actually 3 implementations, defaulting to Kruskal's algorithm.

Issue created by migration from https://trac.sagemath.org/ticket/1088





---

archive/issue_comments_006584.json:
```json
{
    "body": "Attachment [minspantree.patch](tarball://root/attachments/some-uuid/ticket1088/minspantree.patch) by jason created at 2007-11-03 20:45:18",
    "created_at": "2007-11-03T20:45:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1088",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1088#issuecomment-6584",
    "user": "jason"
}
```

Attachment [minspantree.patch](tarball://root/attachments/some-uuid/ticket1088/minspantree.patch) by jason created at 2007-11-03 20:45:18



---

archive/issue_comments_006585.json:
```json
{
    "body": "Attachment [doc_1088.patch](tarball://root/attachments/some-uuid/ticket1088/doc_1088.patch) by rlm created at 2007-11-03 23:20:23",
    "created_at": "2007-11-03T23:20:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1088",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1088#issuecomment-6585",
    "user": "rlm"
}
```

Attachment [doc_1088.patch](tarball://root/attachments/some-uuid/ticket1088/doc_1088.patch) by rlm created at 2007-11-03 23:20:23



---

archive/issue_comments_006586.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-11-03T23:38:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1088",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1088#issuecomment-6586",
    "user": "was"
}
```

Resolution: fixed



---

archive/issue_comments_006587.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2007-11-06T22:36:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1088",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1088#issuecomment-6587",
    "user": "jason"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_006588.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2007-11-06T22:36:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1088",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1088#issuecomment-6588",
    "user": "jason"
}
```

Changing status from closed to reopened.



---

archive/issue_comments_006589.json:
```json
{
    "body": "I believe there is a bug in the code change of the doc_1088 patch above.  The third patch (1088-correct-bugs-improve-doctests.patch) reverses this change, reimplements the doctests, and makes the code faster by sorting using key instead of cmp.\n\nThe third doctest should be applied after the first two doctests.",
    "created_at": "2007-11-06T22:36:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1088",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1088#issuecomment-6589",
    "user": "jason"
}
```

I believe there is a bug in the code change of the doc_1088 patch above.  The third patch (1088-correct-bugs-improve-doctests.patch) reverses this change, reimplements the doctests, and makes the code faster by sorting using key instead of cmp.

The third doctest should be applied after the first two doctests.



---

archive/issue_comments_006590.json:
```json
{
    "body": "Attachment [1088-correct-bugs-improve-doctests.patch](tarball://root/attachments/some-uuid/ticket1088/1088-correct-bugs-improve-doctests.patch) by jason created at 2007-11-06 22:37:16",
    "created_at": "2007-11-06T22:37:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1088",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1088#issuecomment-6590",
    "user": "jason"
}
```

Attachment [1088-correct-bugs-improve-doctests.patch](tarball://root/attachments/some-uuid/ticket1088/1088-correct-bugs-improve-doctests.patch) by jason created at 2007-11-06 22:37:16



---

archive/issue_comments_006591.json:
```json
{
    "body": "The third patch above also corrects a bug in the original code.",
    "created_at": "2007-11-06T22:38:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1088",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1088#issuecomment-6591",
    "user": "jason"
}
```

The third patch above also corrects a bug in the original code.



---

archive/issue_comments_006592.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-11-06T23:54:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1088",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1088#issuecomment-6592",
    "user": "mabshoff"
}
```

Resolution: fixed
