# Issue 6039: [with patch, needs review] Change name of pari's sum function when imported

archive/issues_006039.json:
```json
{
    "body": "Assignee: @craigcitro\n\nWhen we include Pari's `sum` function via `libs/pari/decl.pxi`, it takes precedence over the default Python one. This causes some rather confusing compiler errors -- see, e.g., this thread:\n\nhttp://groups.google.com/group/sage-devel/browse_thread/thread/68a7bd7e99ef22e6#\n\nThe attached patch uses string replace magic to rename it to `pari_sum`. \n\nIssue created by migration from https://trac.sagemath.org/ticket/6039\n\n",
    "created_at": "2009-05-14T16:49:37Z",
    "labels": [
        "interfaces",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0",
    "title": "[with patch, needs review] Change name of pari's sum function when imported",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6039",
    "user": "@craigcitro"
}
```
Assignee: @craigcitro

When we include Pari's `sum` function via `libs/pari/decl.pxi`, it takes precedence over the default Python one. This causes some rather confusing compiler errors -- see, e.g., this thread:

http://groups.google.com/group/sage-devel/browse_thread/thread/68a7bd7e99ef22e6#

The attached patch uses string replace magic to rename it to `pari_sum`. 

Issue created by migration from https://trac.sagemath.org/ticket/6039





---

archive/issue_comments_048086.json:
```json
{
    "body": "Attachment [trac-6039.patch](tarball://root/attachments/some-uuid/ticket6039/trac-6039.patch) by @craigcitro created at 2009-05-14 16:50:15",
    "created_at": "2009-05-14T16:50:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6039",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6039#issuecomment-48086",
    "user": "@craigcitro"
}
```

Attachment [trac-6039.patch](tarball://root/attachments/some-uuid/ticket6039/trac-6039.patch) by @craigcitro created at 2009-05-14 16:50:15



---

archive/issue_comments_048087.json:
```json
{
    "body": "It is never a good idea to touch sage/libs/pari/decl.pxi :). Positive review.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-14T17:15:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6039",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6039#issuecomment-48087",
    "user": "mabshoff"
}
```

It is never a good idea to touch sage/libs/pari/decl.pxi :). Positive review.

Cheers,

Michael



---

archive/issue_comments_048088.json:
```json
{
    "body": "Merged in Sage 4.0.alpha0.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-14T17:33:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6039",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6039#issuecomment-48088",
    "user": "mabshoff"
}
```

Merged in Sage 4.0.alpha0.

Cheers,

Michael



---

archive/issue_comments_048089.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-05-14T17:33:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6039",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6039#issuecomment-48089",
    "user": "mabshoff"
}
```

Resolution: fixed
