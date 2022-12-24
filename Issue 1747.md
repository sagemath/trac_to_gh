# Issue 1747: [with patch, needs review] speed improvement for mq.SR.polynomial_system

archive/issues_001747.json:
```json
{
    "body": "Assignee: malb\n\nSee attached patch.\n\nIssue created by migration from https://trac.sagemath.org/ticket/1747\n\n",
    "created_at": "2008-01-10T15:14:18Z",
    "labels": [
        "misc",
        "minor",
        "enhancement"
    ],
    "title": "[with patch, needs review] speed improvement for mq.SR.polynomial_system",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1747",
    "user": "malb"
}
```
Assignee: malb

See attached patch.

Issue created by migration from https://trac.sagemath.org/ticket/1747





---

archive/issue_comments_011033.json:
```json
{
    "body": "Attachment [sr_speedup.patch](tarball://root/attachments/some-uuid/ticket1747/sr_speedup.patch) by malb created at 2008-01-10 15:14:31",
    "created_at": "2008-01-10T15:14:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1747",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1747#issuecomment-11033",
    "user": "malb"
}
```

Attachment [sr_speedup.patch](tarball://root/attachments/some-uuid/ticket1747/sr_speedup.patch) by malb created at 2008-01-10 15:14:31



---

archive/issue_comments_011034.json:
```json
{
    "body": "Looks good to me. I would be curious how much a difference it does make.\n\nCheers,\n\nMichael",
    "created_at": "2008-01-16T15:55:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1747",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1747#issuecomment-11034",
    "user": "mabshoff"
}
```

Looks good to me. I would be curious how much a difference it does make.

Cheers,

Michael



---

archive/issue_comments_011035.json:
```json
{
    "body": "malb commented on the performance issue in IRC:\n\n```\n[16:46] <mabshoff> Did you run benchmarks? I.e. does it make a difference?\n[16:46] <malb> a LOT\n[16:46] <malb> from unfeasible to < 1s\n[16:46] <malb> the preparser is slow slow slow\n```\n",
    "created_at": "2008-01-16T15:59:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1747",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1747#issuecomment-11035",
    "user": "mabshoff"
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

archive/issue_comments_011036.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-16T15:59:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1747",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1747#issuecomment-11036",
    "user": "mabshoff"
}
```

Resolution: fixed
