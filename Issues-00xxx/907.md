# Issue 907: [with patch] fix small memory leak in modn_sparse_lift

archive/issues_000907.json:
```json
{
    "body": "Assignee: mabshoff\n\nRunning\n\n```\nfor n in range(10,100):\n   a=ModularSymbols(n,sign=1).decomposition(); print n, get_memory_usage()\n```\nBefore (with the other memleak patches tagged for 2.8.8):\n\n```\n==15147== LEAK SUMMARY:\n==15147==    definitely lost: 1,072,216 bytes in 96,412 blocks.\n==15147==    indirectly lost: 419,120 bytes in 7,205 blocks.\n==15147==      possibly lost: 376,558 bytes in 1,194 blocks.\n==15147==    still reachable: 92,977,412 bytes in 1,342,343 blocks.\n==15147==         suppressed: 0 bytes in 0 blocks.\n```\nWith the patch:\n\n```\n==22935== LEAK SUMMARY:\n==22935==    definitely lost: 1,071,084 bytes in 88,923 blocks.\n==22935==    indirectly lost: 408,752 bytes in 7,166 blocks.\n==22935==      possibly lost: 379,454 bytes in 1,197 blocks.\n==22935==    still reachable: 92,968,751 bytes in 1,342,412 blocks.\n==22935==         suppressed: 0 bytes in 0 blocks.\n```\n\nEvery byte counts!\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/907\n\n",
    "closed_at": "2007-10-20T19:18:48Z",
    "created_at": "2007-10-16T04:55:03Z",
    "labels": [
        "component: memleak",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.8",
    "title": "[with patch] fix small memory leak in modn_sparse_lift",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/907",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff

Running

```
for n in range(10,100):
   a=ModularSymbols(n,sign=1).decomposition(); print n, get_memory_usage()
```
Before (with the other memleak patches tagged for 2.8.8):

```
==15147== LEAK SUMMARY:
==15147==    definitely lost: 1,072,216 bytes in 96,412 blocks.
==15147==    indirectly lost: 419,120 bytes in 7,205 blocks.
==15147==      possibly lost: 376,558 bytes in 1,194 blocks.
==15147==    still reachable: 92,977,412 bytes in 1,342,343 blocks.
==15147==         suppressed: 0 bytes in 0 blocks.
```
With the patch:

```
==22935== LEAK SUMMARY:
==22935==    definitely lost: 1,071,084 bytes in 88,923 blocks.
==22935==    indirectly lost: 408,752 bytes in 7,166 blocks.
==22935==      possibly lost: 379,454 bytes in 1,197 blocks.
==22935==    still reachable: 92,968,751 bytes in 1,342,412 blocks.
==22935==         suppressed: 0 bytes in 0 blocks.
```

Every byte counts!

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/907





---

archive/issue_comments_005562.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-10-16T04:55:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/907",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/907#issuecomment-5562",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_005563.json:
```json
{
    "body": "Attachment [sage-2.8.7.rc1-fix-small-memleaks-in_modn_sparse_lift.patch](tarball://root/attachments/some-uuid/ticket907/sage-2.8.7.rc1-fix-small-memleaks-in_modn_sparse_lift.patch) by mabshoff created at 2007-10-16 04:55:44",
    "created_at": "2007-10-16T04:55:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/907",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/907#issuecomment-5563",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [sage-2.8.7.rc1-fix-small-memleaks-in_modn_sparse_lift.patch](tarball://root/attachments/some-uuid/ticket907/sage-2.8.7.rc1-fix-small-memleaks-in_modn_sparse_lift.patch) by mabshoff created at 2007-10-16 04:55:44



---

archive/issue_events_002507.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-10-20T19:18:48Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/907",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/907#event-2507"
}
```



---

archive/issue_comments_005564.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-10-20T19:18:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/907",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/907#issuecomment-5564",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed
