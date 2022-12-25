# Issue 4257: [with patch, needs review] support for Singular's  'intmat' and 'intvec'

archive/issues_004257.json:
```json
{
    "body": "Assignee: @malb\n\nCC:  singular\n\nThis now works:\n\n\n```\nsage: A = random_matrix(ZZ,3,3); A\n[ -8   2   0]\n[  0   1  -1]\n[  2   1 -95]\nsage: As = singular(A); As\n-8     2     0\n 0     1    -1\n 2     1   -95\nsage: As._sage_()\n[ -8   2   0]\n[  0   1  -1]\n[  2   1 -95]\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4257\n\n",
    "created_at": "2008-10-09T21:54:29Z",
    "labels": [
        "component: interfaces",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.3",
    "title": "[with patch, needs review] support for Singular's  'intmat' and 'intvec'",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4257",
    "user": "https://github.com/malb"
}
```
Assignee: @malb

CC:  singular

This now works:


```
sage: A = random_matrix(ZZ,3,3); A
[ -8   2   0]
[  0   1  -1]
[  2   1 -95]
sage: As = singular(A); As
-8     2     0
 0     1    -1
 2     1   -95
sage: As._sage_()
[ -8   2   0]
[  0   1  -1]
[  2   1 -95]
```


Issue created by migration from https://trac.sagemath.org/ticket/4257





---

archive/issue_comments_030921.json:
```json
{
    "body": "Attachment [singular_intmat.patch](tarball://root/attachments/some-uuid/ticket4257/singular_intmat.patch) by @malb created at 2008-10-10 08:46:24",
    "created_at": "2008-10-10T08:46:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4257",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4257#issuecomment-30921",
    "user": "https://github.com/malb"
}
```

Attachment [singular_intmat.patch](tarball://root/attachments/some-uuid/ticket4257/singular_intmat.patch) by @malb created at 2008-10-10 08:46:24



---

archive/issue_comments_030922.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2008-10-10T16:18:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4257",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4257#issuecomment-30922",
    "user": "https://github.com/mwhansen"
}
```

Looks good to me.



---

archive/issue_comments_030923.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-10-11T06:40:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4257",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4257#issuecomment-30923",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_004496.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-10-11T06:40:58Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4257",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4257#event-4496"
}
```



---

archive/issue_comments_030924.json:
```json
{
    "body": "Merged in Sage 3.1.3.rc0",
    "created_at": "2008-10-11T06:40:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4257",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4257#issuecomment-30924",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.1.3.rc0
