# Issue 2160: leftovers from python to cython translation

archive/issues_002160.json:
```json
{
    "body": "Assignee: @williamstein\n\nIn matrix/matrix_integer_dense.pyx and matrix//matrix_rational_dense.pyx we delete the line:\n\ntmp = []\n\nbecause tmp is never used\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2160\n\n",
    "created_at": "2008-02-14T17:42:19Z",
    "labels": [
        "component: linear algebra",
        "trivial"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.2",
    "title": "leftovers from python to cython translation",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2160",
    "user": "https://github.com/jaapspies"
}
```
Assignee: @williamstein

In matrix/matrix_integer_dense.pyx and matrix//matrix_rational_dense.pyx we delete the line:

tmp = []

because tmp is never used



Issue created by migration from https://trac.sagemath.org/ticket/2160





---

archive/issue_comments_014156.json:
```json
{
    "body": "Attachment [trac_2160_leftovers.patch](tarball://root/attachments/some-uuid/ticket2160/trac_2160_leftovers.patch) by @jaapspies created at 2008-02-14 17:44:27",
    "created_at": "2008-02-14T17:44:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2160",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2160#issuecomment-14156",
    "user": "https://github.com/jaapspies"
}
```

Attachment [trac_2160_leftovers.patch](tarball://root/attachments/some-uuid/ticket2160/trac_2160_leftovers.patch) by @jaapspies created at 2008-02-14 17:44:27



---

archive/issue_comments_014157.json:
```json
{
    "body": "Patch looks good.\n\nCheers,\n\nMichael",
    "created_at": "2008-02-14T21:32:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2160",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2160#issuecomment-14157",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Patch looks good.

Cheers,

Michael



---

archive/issue_comments_014158.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-14T21:33:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2160",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2160#issuecomment-14158",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_014159.json:
```json
{
    "body": "Merged in Sage 2.10.2.alpha0",
    "created_at": "2008-02-14T21:33:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2160",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2160#issuecomment-14159",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.10.2.alpha0



---

archive/issue_events_002326.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-02-14T21:33:22Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2160",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2160#event-2326"
}
```
