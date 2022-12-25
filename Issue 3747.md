# Issue 3747: incorrect power in modular arithmetic

archive/issues_003747.json:
```json
{
    "body": "Assignee: somebody\n\n\n```\nsage: R = Integers(17^5)\nsage: R(17)^5\n1419857\n```\n\n\nThe answer should be zero.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3747\n\n",
    "created_at": "2008-07-30T14:14:21Z",
    "labels": [
        "component: basic arithmetic",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1",
    "title": "incorrect power in modular arithmetic",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3747",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```
Assignee: somebody


```
sage: R = Integers(17^5)
sage: R(17)^5
1419857
```


The answer should be zero.


Issue created by migration from https://trac.sagemath.org/ticket/3747





---

archive/issue_comments_026557.json:
```json
{
    "body": "Attachment [3747.patch](tarball://root/attachments/some-uuid/ticket3747/3747.patch) by dmharvey created at 2008-07-30 14:28:37",
    "created_at": "2008-07-30T14:28:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3747",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3747#issuecomment-26557",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```

Attachment [3747.patch](tarball://root/attachments/some-uuid/ticket3747/3747.patch) by dmharvey created at 2008-07-30 14:28:37



---

archive/issue_comments_026558.json:
```json
{
    "body": "looks good!",
    "created_at": "2008-07-30T14:37:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3747",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3747#issuecomment-26558",
    "user": "https://github.com/williamstein"
}
```

looks good!



---

archive/issue_comments_026559.json:
```json
{
    "body": "Looks good to me too.  I note that only the 32-bit code had this bug, not the 64-bit code.",
    "created_at": "2008-07-30T23:13:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3747",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3747#issuecomment-26559",
    "user": "https://github.com/JohnCremona"
}
```

Looks good to me too.  I note that only the 32-bit code had this bug, not the 64-bit code.



---

archive/issue_comments_026560.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-07-30T23:15:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3747",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3747#issuecomment-26560",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_026561.json:
```json
{
    "body": "Merged in Sage 3.1.alpha0",
    "created_at": "2008-07-30T23:15:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3747",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3747#issuecomment-26561",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.1.alpha0



---

archive/issue_events_003969.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-07-30T23:15:51Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3747",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3747#event-3969"
}
```
