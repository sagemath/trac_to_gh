# Issue 3495: [with patch, needs review] bug in cyclotomic charpoly for 1x1 matrices

archive/issues_003495.json:
```json
{
    "body": "Assignee: @craigcitro\n\nThe following will crash in sage:\n\n\n```\nsage: Matrix(CyclotomicField(3), 1, [0]).charpoly()\n```\n\n\nThe attached patch fixes it.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3495\n\n",
    "created_at": "2008-06-23T18:53:49Z",
    "labels": [
        "component: linear algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.4",
    "title": "[with patch, needs review] bug in cyclotomic charpoly for 1x1 matrices",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3495",
    "user": "https://github.com/craigcitro"
}
```
Assignee: @craigcitro

The following will crash in sage:


```
sage: Matrix(CyclotomicField(3), 1, [0]).charpoly()
```


The attached patch fixes it.

Issue created by migration from https://trac.sagemath.org/ticket/3495





---

archive/issue_comments_024562.json:
```json
{
    "body": "Attachment [trac-3495.patch](tarball://root/attachments/some-uuid/ticket3495/trac-3495.patch) by @craigcitro created at 2008-06-23 18:54:19",
    "created_at": "2008-06-23T18:54:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3495#issuecomment-24562",
    "user": "https://github.com/craigcitro"
}
```

Attachment [trac-3495.patch](tarball://root/attachments/some-uuid/ticket3495/trac-3495.patch) by @craigcitro created at 2008-06-23 18:54:19



---

archive/issue_comments_024563.json:
```json
{
    "body": "REFEREE REPORT:\n\n* +1; this works as advertised\n\nReminder -- need to also fix 0x0 as another ticket...",
    "created_at": "2008-06-23T19:17:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3495#issuecomment-24563",
    "user": "https://github.com/williamstein"
}
```

REFEREE REPORT:

* +1; this works as advertised

Reminder -- need to also fix 0x0 as another ticket...



---

archive/issue_comments_024564.json:
```json
{
    "body": "The 0x0 is #3496.",
    "created_at": "2008-06-23T19:22:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3495#issuecomment-24564",
    "user": "https://github.com/craigcitro"
}
```

The 0x0 is #3496.



---

archive/issue_comments_024565.json:
```json
{
    "body": "Merged in Sage 3.0.4.alpha1",
    "created_at": "2008-06-23T23:10:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3495#issuecomment-24565",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.0.4.alpha1



---

archive/issue_comments_024566.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-06-23T23:10:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3495#issuecomment-24566",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
