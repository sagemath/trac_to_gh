# Issue 810: [with patch] gens_reduced for general ideals

archive/issues_000810.json:
```json
{
    "body": "Assignee: was\n\nIt's annoying that number field ideals have a `gens_reduced()` method, but ideals of ZZ do not. This patch fixes this by adding a `gens_reduced()` method to the base ideal class, whose default implementation just calls `gens()`.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/810\n\n",
    "created_at": "2007-10-03T16:39:57Z",
    "labels": [
        "algebraic geometry",
        "major",
        "bug"
    ],
    "title": "[with patch] gens_reduced for general ideals",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/810",
    "user": "dmharvey"
}
```
Assignee: was

It's annoying that number field ideals have a `gens_reduced()` method, but ideals of ZZ do not. This patch fixes this by adding a `gens_reduced()` method to the base ideal class, whose default implementation just calls `gens()`.


Issue created by migration from https://trac.sagemath.org/ticket/810





---

archive/issue_comments_004903.json:
```json
{
    "body": "Attachment [gens-reduced.hg](tarball://root/attachments/some-uuid/ticket810/gens-reduced.hg) by dmharvey created at 2007-10-03 16:40:10",
    "created_at": "2007-10-03T16:40:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/810",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/810#issuecomment-4903",
    "user": "dmharvey"
}
```

Attachment [gens-reduced.hg](tarball://root/attachments/some-uuid/ticket810/gens-reduced.hg) by dmharvey created at 2007-10-03 16:40:10



---

archive/issue_comments_004904.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-10-04T15:15:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/810",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/810#issuecomment-4904",
    "user": "was"
}
```

Resolution: fixed
