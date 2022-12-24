# Issue 1704: [with patch] replace _DivPolyContext by _multiply_point

archive/issues_001704.json:
```json
{
    "body": "Assignee: was\n\nThis patch replaces the `_DivPolyContext` class with a new function `_multiply_point`. The main downside of the original `_DivPolyContext` is that it's very recursive, and I started overflowing python's stack for some large problems I needed to play with. The new function is not recursive, and also turns out to be slightly faster.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1704\n\n",
    "created_at": "2008-01-06T23:19:41Z",
    "labels": [
        "algebraic geometry",
        "major",
        "enhancement"
    ],
    "title": "[with patch] replace _DivPolyContext by _multiply_point",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1704",
    "user": "dmharvey"
}
```
Assignee: was

This patch replaces the `_DivPolyContext` class with a new function `_multiply_point`. The main downside of the original `_DivPolyContext` is that it's very recursive, and I started overflowing python's stack for some large problems I needed to play with. The new function is not recursive, and also turns out to be slightly faster.


Issue created by migration from https://trac.sagemath.org/ticket/1704





---

archive/issue_comments_010794.json:
```json
{
    "body": "Attachment [multiply_point.hg](tarball://root/attachments/some-uuid/ticket1704/multiply_point.hg) by dmharvey created at 2008-01-06 23:20:24",
    "created_at": "2008-01-06T23:20:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1704",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1704#issuecomment-10794",
    "user": "dmharvey"
}
```

Attachment [multiply_point.hg](tarball://root/attachments/some-uuid/ticket1704/multiply_point.hg) by dmharvey created at 2008-01-06 23:20:24



---

archive/issue_comments_010795.json:
```json
{
    "body": "I can't speak to mathematical correctness, but the patch looks good to me.  Apply.",
    "created_at": "2008-01-20T06:53:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1704",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1704#issuecomment-10795",
    "user": "ncalexan"
}
```

I can't speak to mathematical correctness, but the patch looks good to me.  Apply.



---

archive/issue_comments_010796.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-21T05:52:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1704",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1704#issuecomment-10796",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_010797.json:
```json
{
    "body": "Merged in Sage 2.10.1.alpha1",
    "created_at": "2008-01-21T05:52:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1704",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1704#issuecomment-10797",
    "user": "mabshoff"
}
```

Merged in Sage 2.10.1.alpha1
