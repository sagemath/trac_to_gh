# Issue 1910: linear algebra -- doctesting for sage/matrix/matrix_field_dense.pyx is off for no good reason, and there are lots of problems when we turn it on.

archive/issues_001910.json:
```json
{
    "body": "Assignee: @williamstein\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1910\n\n",
    "created_at": "2008-01-24T15:17:11Z",
    "labels": [
        "component: linear algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "linear algebra -- doctesting for sage/matrix/matrix_field_dense.pyx is off for no good reason, and there are lots of problems when we turn it on.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1910",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein



Issue created by migration from https://trac.sagemath.org/ticket/1910





---

archive/issue_comments_012072.json:
```json
{
    "body": "This seems to be the reason: matrix_field_dense.pyx has matrix_pid_dense has its parent, but matrix_pid_dense doesn't even exist (yet)! Same for matrix_field_sparse and its counterpart, matrix_pid_sparse.",
    "created_at": "2008-03-04T17:07:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1910",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1910#issuecomment-12072",
    "user": "https://github.com/dfdeshom"
}
```

This seems to be the reason: matrix_field_dense.pyx has matrix_pid_dense has its parent, but matrix_pid_dense doesn't even exist (yet)! Same for matrix_field_sparse and its counterpart, matrix_pid_sparse.



---

archive/issue_comments_012073.json:
```json
{
    "body": "The file in question does not exist any more in Sage 3.2.2.alpha2, so I am closing this as wontfix:\n\n```\nsage-3.2.2.alpha2/devel/sage$ ls -al sage/matrix/matrix_dense*\n-rw-r--r-- 1 mabshoff 1090 264468 2008-12-10 06:41 sage/matrix/matrix_dense.c\n-rw-r--r-- 1 mabshoff 1090     66 2008-12-08 02:44 sage/matrix/matrix_dense.pxd\n-rw-r--r-- 1 mabshoff 1090  10782 2008-12-10 06:40 sage/matrix/matrix_dense.pyx\n```\n\nI also used find to locate the file elsewhere in the tree and it isn't there any more :)\n\nCheers,\n\nMichael",
    "created_at": "2008-12-11T16:00:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1910",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1910#issuecomment-12073",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

The file in question does not exist any more in Sage 3.2.2.alpha2, so I am closing this as wontfix:

```
sage-3.2.2.alpha2/devel/sage$ ls -al sage/matrix/matrix_dense*
-rw-r--r-- 1 mabshoff 1090 264468 2008-12-10 06:41 sage/matrix/matrix_dense.c
-rw-r--r-- 1 mabshoff 1090     66 2008-12-08 02:44 sage/matrix/matrix_dense.pxd
-rw-r--r-- 1 mabshoff 1090  10782 2008-12-10 06:40 sage/matrix/matrix_dense.pyx
```

I also used find to locate the file elsewhere in the tree and it isn't there any more :)

Cheers,

Michael



---

archive/issue_events_002066.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-12-11T16:00:57Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1910",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1910#event-2066"
}
```



---

archive/issue_comments_012074.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2008-12-11T16:00:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1910",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1910#issuecomment-12074",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: wontfix
