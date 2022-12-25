# Issue 1675: memleak in pAdicCappedRelativeElement._set_from_Rational

archive/issues_001675.json:
```json
{
    "body": "Assignee: mabshoff\n\nThe attached patch fixes a memleak in pAdicCappedRelativeElement._set_from_Rational\n\nIssue created by migration from https://trac.sagemath.org/ticket/1675\n\n",
    "created_at": "2008-01-03T21:28:48Z",
    "labels": [
        "component: memleak",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.9.2",
    "title": "memleak in pAdicCappedRelativeElement._set_from_Rational",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1675",
    "user": "https://github.com/wjp"
}
```
Assignee: mabshoff

The attached patch fixes a memleak in pAdicCappedRelativeElement._set_from_Rational

Issue created by migration from https://trac.sagemath.org/ticket/1675





---

archive/issue_comments_010601.json:
```json
{
    "body": "Attachment [7916.patch](tarball://root/attachments/some-uuid/ticket1675/7916.patch) by mabshoff created at 2008-01-03 22:20:51\n\nWith this and the patch from 1676 applied I get:\nBefore:\n\n```\n==6600== LEAK SUMMARY:\n==6600==    definitely lost: 264 bytes in 24 blocks.\n==6600==      possibly lost: 261,881 bytes in 713 blocks.\n==6600==    still reachable: 39,070,317 bytes in 19,102 blocks.\n==6600==         suppressed: 0 bytes in 0 blocks.\n```\n\nAfter:\n\n```\n==6600== LEAK SUMMARY:\n==6600==    definitely lost: 264 bytes in 24 blocks.\n==6600==      possibly lost: 261,881 bytes in 713 blocks.\n==6600==    still reachable: 39,070,317 bytes in 19,102 blocks.\n==6600==         suppressed: 0 bytes in 0 blocks.\n```\n\nPatch applied to Sage 2.9.2.rc0.\n\nCheers,\n\nMichael",
    "created_at": "2008-01-03T22:20:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1675",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1675#issuecomment-10601",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [7916.patch](tarball://root/attachments/some-uuid/ticket1675/7916.patch) by mabshoff created at 2008-01-03 22:20:51

With this and the patch from 1676 applied I get:
Before:

```
==6600== LEAK SUMMARY:
==6600==    definitely lost: 264 bytes in 24 blocks.
==6600==      possibly lost: 261,881 bytes in 713 blocks.
==6600==    still reachable: 39,070,317 bytes in 19,102 blocks.
==6600==         suppressed: 0 bytes in 0 blocks.
```

After:

```
==6600== LEAK SUMMARY:
==6600==    definitely lost: 264 bytes in 24 blocks.
==6600==      possibly lost: 261,881 bytes in 713 blocks.
==6600==    still reachable: 39,070,317 bytes in 19,102 blocks.
==6600==         suppressed: 0 bytes in 0 blocks.
```

Patch applied to Sage 2.9.2.rc0.

Cheers,

Michael



---

archive/issue_events_001834.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-01-03T22:20:51Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1675",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1675#event-1834"
}
```



---

archive/issue_comments_010602.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-03T22:20:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1675",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1675#issuecomment-10602",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_010603.json:
```json
{
    "body": "Oops:\n\nAfter:\n\n```\n==16192== LEAK SUMMARY:\n==16192==    definitely lost: 0 bytes in 0 blocks.\n==16192==      possibly lost: 261,881 bytes in 713 blocks.\n==16192==    still reachable: 39,070,317 bytes in 19,102 blocks.\n==16192==         suppressed: 0 bytes in 0 blocks.\n```\n",
    "created_at": "2008-01-03T22:21:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1675",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1675#issuecomment-10603",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Oops:

After:

```
==16192== LEAK SUMMARY:
==16192==    definitely lost: 0 bytes in 0 blocks.
==16192==      possibly lost: 261,881 bytes in 713 blocks.
==16192==    still reachable: 39,070,317 bytes in 19,102 blocks.
==16192==         suppressed: 0 bytes in 0 blocks.
```

