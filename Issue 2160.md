# Issue 2160: leftovers from python to cython translation

archive/issues_002160.json:
```json
{
    "body": "Assignee: @williamstein\n\nIn matrix/matrix_integer_dense.pyx and matrix//matrix_rational_dense.pyx we delete the line:\n\ntmp = []\n\nbecause tmp is never used\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2160\n\n",
    "created_at": "2008-02-14T17:42:19Z",
    "labels": [
        "linear algebra",
        "trivial",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.2",
    "title": "leftovers from python to cython translation",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2160",
    "user": "@jaapspies"
}
```
Assignee: @williamstein

In matrix/matrix_integer_dense.pyx and matrix//matrix_rational_dense.pyx we delete the line:

tmp = []

because tmp is never used



Issue created by migration from https://trac.sagemath.org/ticket/2160





---

archive/issue_comments_014187.json:
```json
{
    "body": "Attachment [trac_2160_leftovers.patch](tarball://root/attachments/some-uuid/ticket2160/trac_2160_leftovers.patch) by @jaapspies created at 2008-02-14 17:44:27",
    "created_at": "2008-02-14T17:44:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2160",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2160#issuecomment-14187",
    "user": "@jaapspies"
}
```

Attachment [trac_2160_leftovers.patch](tarball://root/attachments/some-uuid/ticket2160/trac_2160_leftovers.patch) by @jaapspies created at 2008-02-14 17:44:27



---

archive/issue_comments_014188.json:
```json
{
    "body": "Patch looks good.\n\nCheers,\n\nMichael",
    "created_at": "2008-02-14T21:32:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2160",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2160#issuecomment-14188",
    "user": "mabshoff"
}
```

Patch looks good.

Cheers,

Michael



---

archive/issue_comments_014189.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-14T21:33:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2160",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2160#issuecomment-14189",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_014190.json:
```json
{
    "body": "Merged in Sage 2.10.2.alpha0",
    "created_at": "2008-02-14T21:33:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2160",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2160#issuecomment-14190",
    "user": "mabshoff"
}
```

Merged in Sage 2.10.2.alpha0
