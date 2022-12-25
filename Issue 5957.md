# Issue 5957: 3.4.2.rc0: Maxima related doctest failure in matrix/matrix_symbolic_dense.pyx

archive/issues_005957.json:
```json
{
    "body": "Assignee: mabshoff\n\nThis happens with gcc 4.3.3 on iras and cicero:\n\n```\nsage -t -long \"devel/sage/sage/matrix/matrix_symbolic_dense.pyx\"\n**********************************************************************\nFile \"/home/mabshoff/build-3.4.2.rc0/sage-3.4.2.rc0-ciero-gcc-4.3.3/\ndevel/sage/sage/matrix/matrix_symbolic_dense.pyx\", line 413:\n   sage: M.determinant()\nExpected:\n   4*x - 6\nGot:\n   determinant(sage513)\n**********************************************************************\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5957\n\n",
    "created_at": "2009-05-01T13:34:36Z",
    "labels": [
        "component: doctest coverage",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4.2",
    "title": "3.4.2.rc0: Maxima related doctest failure in matrix/matrix_symbolic_dense.pyx",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5957",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff

This happens with gcc 4.3.3 on iras and cicero:

```
sage -t -long "devel/sage/sage/matrix/matrix_symbolic_dense.pyx"
**********************************************************************
File "/home/mabshoff/build-3.4.2.rc0/sage-3.4.2.rc0-ciero-gcc-4.3.3/
devel/sage/sage/matrix/matrix_symbolic_dense.pyx", line 413:
   sage: M.determinant()
Expected:
   4*x - 6
Got:
   determinant(sage513)
**********************************************************************
```


Issue created by migration from https://trac.sagemath.org/ticket/5957





---

archive/issue_comments_047069.json:
```json
{
    "body": "Maybe it is good to mention I had this failure already in sage-3.4.2.alpha0.\n\nBoth with Fedora 9 and 10, 32 bit.\n\ngcc version 4.3.0, resp. 4.3.2\n\nJaap",
    "created_at": "2009-05-03T22:36:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5957#issuecomment-47069",
    "user": "https://github.com/jaapspies"
}
```

Maybe it is good to mention I had this failure already in sage-3.4.2.alpha0.

Both with Fedora 9 and 10, 32 bit.

gcc version 4.3.0, resp. 4.3.2

Jaap



---

archive/issue_comments_047070.json:
```json
{
    "body": "Attachment [trac_5957.patch](tarball://root/attachments/some-uuid/ticket5957/trac_5957.patch) by mabshoff created at 2009-05-04 04:54:04",
    "created_at": "2009-05-04T04:54:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5957#issuecomment-47070",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [trac_5957.patch](tarball://root/attachments/some-uuid/ticket5957/trac_5957.patch) by mabshoff created at 2009-05-04 04:54:04



---

archive/issue_comments_047071.json:
```json
{
    "body": "This is William's patch, so I can review it :)\n\nCheers,\n\nMichael",
    "created_at": "2009-05-04T04:54:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5957#issuecomment-47071",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This is William's patch, so I can review it :)

Cheers,

Michael



---

archive/issue_comments_047072.json:
```json
{
    "body": "Positive review.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-04T05:02:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5957#issuecomment-47072",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Positive review.

Cheers,

Michael



---

archive/issue_events_013970.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-05-04T05:02:58Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5957",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5957#event-13970"
}
```



---

archive/issue_comments_047073.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-05-04T05:02:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5957#issuecomment-47073",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_047074.json:
```json
{
    "body": "Merged in Sage 3.4.2.final.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-04T05:02:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5957#issuecomment-47074",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.4.2.final.

Cheers,

Michael
