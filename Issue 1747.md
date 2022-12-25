# Issue 1747: [with patch, needs review] speed improvement for mq.SR.polynomial_system

archive/issues_001747.json:
```json
{
    "body": "Assignee: @malb\n\nSee attached patch.\n\nIssue created by migration from https://trac.sagemath.org/ticket/1747\n\n",
    "created_at": "2008-01-10T15:14:18Z",
    "labels": [
        "component: misc",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10",
    "title": "[with patch, needs review] speed improvement for mq.SR.polynomial_system",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1747",
    "user": "https://github.com/malb"
}
```
Assignee: @malb

See attached patch.

Issue created by migration from https://trac.sagemath.org/ticket/1747





---

archive/issue_comments_011006.json:
```json
{
    "body": "Attachment [sr_speedup.patch](tarball://root/attachments/some-uuid/ticket1747/sr_speedup.patch) by @malb created at 2008-01-10 15:14:31",
    "created_at": "2008-01-10T15:14:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1747",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1747#issuecomment-11006",
    "user": "https://github.com/malb"
}
```

Attachment [sr_speedup.patch](tarball://root/attachments/some-uuid/ticket1747/sr_speedup.patch) by @malb created at 2008-01-10 15:14:31



---

archive/issue_comments_011007.json:
```json
{
    "body": "Looks good to me. I would be curious how much a difference it does make.\n\nCheers,\n\nMichael",
    "created_at": "2008-01-16T15:55:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1747",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1747#issuecomment-11007",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Looks good to me. I would be curious how much a difference it does make.

Cheers,

Michael



---

archive/issue_comments_011008.json:
```json
{
    "body": "malb commented on the performance issue in IRC:\n\n```\n[16:46] <mabshoff> Did you run benchmarks? I.e. does it make a difference?\n[16:46] <malb> a LOT\n[16:46] <malb> from unfeasible to < 1s\n[16:46] <malb> the preparser is slow slow slow\n```\n",
    "created_at": "2008-01-16T15:59:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1747",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1747#issuecomment-11008",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

malb commented on the performance issue in IRC:

```
[16:46] <mabshoff> Did you run benchmarks? I.e. does it make a difference?
[16:46] <malb> a LOT
[16:46] <malb> from unfeasible to < 1s
[16:46] <malb> the preparser is slow slow slow
```




---

archive/issue_comments_011009.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-16T15:59:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1747",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1747#issuecomment-11009",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
