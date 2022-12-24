# Issue 1095: [with patch] silly annoyance in sage -coverage

archive/issues_001095.json:
```json
{
    "body": "Assignee: @craigcitro\n\nI made a silly mistake when I was editing sage-coverage -- it will always tell you that a function is \"possibly wrong\" (i.e. function name doesn't occur in doctest) when there is no doctest; this is pretty obvious. This patch fixes it, so that now things only appear in the \"possibly wrong\" list if they *don't* appear in either of the other lists (missing documentation or missing doctests).\n\nIssue created by migration from https://trac.sagemath.org/ticket/1095\n\n",
    "created_at": "2007-11-04T01:15:24Z",
    "labels": [
        "doctest coverage",
        "trivial",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.12",
    "title": "[with patch] silly annoyance in sage -coverage",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1095",
    "user": "@craigcitro"
}
```
Assignee: @craigcitro

I made a silly mistake when I was editing sage-coverage -- it will always tell you that a function is "possibly wrong" (i.e. function name doesn't occur in doctest) when there is no doctest; this is pretty obvious. This patch fixes it, so that now things only appear in the "possibly wrong" list if they *don't* appear in either of the other lists (missing documentation or missing doctests).

Issue created by migration from https://trac.sagemath.org/ticket/1095





---

archive/issue_comments_006629.json:
```json
{
    "body": "Attachment [trac_1095.hg](tarball://root/attachments/some-uuid/ticket1095/trac_1095.hg) by @craigcitro created at 2007-11-04 01:16:06\n\nbundle for $SAGE_ROOT/local/bin",
    "created_at": "2007-11-04T01:16:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1095",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1095#issuecomment-6629",
    "user": "@craigcitro"
}
```

Attachment [trac_1095.hg](tarball://root/attachments/some-uuid/ticket1095/trac_1095.hg) by @craigcitro created at 2007-11-04 01:16:06

bundle for $SAGE_ROOT/local/bin



---

archive/issue_comments_006630.json:
```json
{
    "body": "applied to 2.8.12.rc0",
    "created_at": "2007-11-06T22:33:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1095",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1095#issuecomment-6630",
    "user": "mabshoff"
}
```

applied to 2.8.12.rc0



---

archive/issue_comments_006631.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-11-06T22:33:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1095",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1095#issuecomment-6631",
    "user": "mabshoff"
}
```

Resolution: fixed
