# Issue 1674: memleak in pAdicCappedRelativeElement.__pow__

archive/issues_001674.json:
```json
{
    "body": "Assignee: mabshoff\n\nThe attached patch plugs a small memleak in pAdicCappedRelativeElement.__pow__ .\n\nIssue created by migration from https://trac.sagemath.org/ticket/1674\n\n",
    "created_at": "2008-01-03T21:07:41Z",
    "labels": [
        "memleak",
        "minor",
        "bug"
    ],
    "title": "memleak in pAdicCappedRelativeElement.__pow__",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1674",
    "user": "wjp"
}
```
Assignee: mabshoff

The attached patch plugs a small memleak in pAdicCappedRelativeElement.__pow__ .

Issue created by migration from https://trac.sagemath.org/ticket/1674





---

archive/issue_comments_010624.json:
```json
{
    "body": "Attachment [7915.patch](tarball://root/attachments/some-uuid/ticket1674/7915.patch) by wjp created at 2008-01-03 21:08:09",
    "created_at": "2008-01-03T21:08:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1674",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1674#issuecomment-10624",
    "user": "wjp"
}
```

Attachment [7915.patch](tarball://root/attachments/some-uuid/ticket1674/7915.patch) by wjp created at 2008-01-03 21:08:09



---

archive/issue_comments_010625.json:
```json
{
    "body": "Merged in 2.9.2.rc0.\n\nCheers,\n\nMichael",
    "created_at": "2008-01-03T21:18:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1674",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1674#issuecomment-10625",
    "user": "mabshoff"
}
```

Merged in 2.9.2.rc0.

Cheers,

Michael



---

archive/issue_comments_010626.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-03T21:18:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1674",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1674#issuecomment-10626",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_010627.json:
```json
{
    "body": "Some statistics on running memcheck on `padic_capped_relative_element.py`:\nBefore:\n\n```\n==6186== LEAK SUMMARY:\n==6186==    definitely lost: 312 bytes in 30 blocks.\n==6186==      possibly lost: 261,425 bytes in 712 blocks.\n==6186==    still reachable: 39,070,789 bytes in 19,104 blocks.\n==6186==         suppressed: 0 bytes in 0 blocks.\n```\n\nAfter:\n\n```\n==6600== LEAK SUMMARY:\n==6600==    definitely lost: 264 bytes in 24 blocks.\n==6600==      possibly lost: 261,881 bytes in 713 blocks.\n==6600==    still reachable: 39,070,317 bytes in 19,102 blocks.\n==6600==         suppressed: 0 bytes in 0 blocks.\n```\n\n6 blocks with 48 bytes, but those leaks should add up quickly.\n\nCheers,\n\nMichael",
    "created_at": "2008-01-03T21:25:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1674",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1674#issuecomment-10627",
    "user": "mabshoff"
}
```

Some statistics on running memcheck on `padic_capped_relative_element.py`:
Before:

```
==6186== LEAK SUMMARY:
==6186==    definitely lost: 312 bytes in 30 blocks.
==6186==      possibly lost: 261,425 bytes in 712 blocks.
==6186==    still reachable: 39,070,789 bytes in 19,104 blocks.
==6186==         suppressed: 0 bytes in 0 blocks.
```

After:

```
==6600== LEAK SUMMARY:
==6600==    definitely lost: 264 bytes in 24 blocks.
==6600==      possibly lost: 261,881 bytes in 713 blocks.
==6600==    still reachable: 39,070,317 bytes in 19,102 blocks.
==6600==         suppressed: 0 bytes in 0 blocks.
```

6 blocks with 48 bytes, but those leaks should add up quickly.

Cheers,

Michael
