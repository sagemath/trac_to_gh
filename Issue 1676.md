# Issue 1676: memleak and unused variable in pAdicCappedAbsoluteElement

archive/issues_001676.json:
```json
{
    "body": "Assignee: mabshoff\n\nAttached patch fixes a memleak in pAdicCappedAbsoluteElement.multiplicate_order,\nand removes an unused variable in pAdicCappedAbsoluteElement.__pow__ .\n\nIssue created by migration from https://trac.sagemath.org/ticket/1676\n\n",
    "created_at": "2008-01-03T21:41:02Z",
    "labels": [
        "memleak",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.9.2",
    "title": "memleak and unused variable in pAdicCappedAbsoluteElement",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1676",
    "user": "wjp"
}
```
Assignee: mabshoff

Attached patch fixes a memleak in pAdicCappedAbsoluteElement.multiplicate_order,
and removes an unused variable in pAdicCappedAbsoluteElement.__pow__ .

Issue created by migration from https://trac.sagemath.org/ticket/1676





---

archive/issue_comments_010631.json:
```json
{
    "body": "Attachment [7917.patch](tarball://root/attachments/some-uuid/ticket1676/7917.patch) by wjp created at 2008-01-03 21:41:13",
    "created_at": "2008-01-03T21:41:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1676",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1676#issuecomment-10631",
    "user": "wjp"
}
```

Attachment [7917.patch](tarball://root/attachments/some-uuid/ticket1676/7917.patch) by wjp created at 2008-01-03 21:41:13



---

archive/issue_comments_010632.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-03T22:21:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1676",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1676#issuecomment-10632",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_010633.json:
```json
{
    "body": "With this and the patch from #1675 applied I get:\nBefore:\n\n```\n==6600== LEAK SUMMARY:\n==6600==    definitely lost: 264 bytes in 24 blocks.\n==6600==      possibly lost: 261,881 bytes in 713 blocks.\n==6600==    still reachable: 39,070,317 bytes in 19,102 blocks.\n==6600==         suppressed: 0 bytes in 0 blocks.\n```\n\nAfter:\n\n```\n==6600== LEAK SUMMARY:\n==6600==    definitely lost: 264 bytes in 24 blocks.\n==6600==      possibly lost: 261,881 bytes in 713 blocks.\n==6600==    still reachable: 39,070,317 bytes in 19,102 blocks.\n==6600==         suppressed: 0 bytes in 0 blocks.\n```\n\nPatch applied to Sage 2.9.2.rc0.\n\nCheers,\n\nMichael",
    "created_at": "2008-01-03T22:21:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1676",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1676#issuecomment-10633",
    "user": "mabshoff"
}
```

With this and the patch from #1675 applied I get:
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

archive/issue_comments_010634.json:
```json
{
    "body": "Oops:\n\nAfter:\n\n```\n==16192== LEAK SUMMARY:\n==16192==    definitely lost: 0 bytes in 0 blocks.\n==16192==      possibly lost: 261,881 bytes in 713 blocks.\n==16192==    still reachable: 39,070,317 bytes in 19,102 blocks.\n==16192==         suppressed: 0 bytes in 0 blocks.\n```\n",
    "created_at": "2008-01-03T22:21:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1676",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1676#issuecomment-10634",
    "user": "mabshoff"
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

