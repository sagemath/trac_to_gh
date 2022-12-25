# Issue 2392: [with patch, needs review] generic univariate polynomial has no discriminant function

archive/issues_002392.json:
```json
{
    "body": "Assignee: mabshoff\n\nCC:  @ncalexan\n\nKeywords: univariate polynomial discriminant\n\nAs it says: generic univariate polynomial has no discriminant function.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2392\n\n",
    "created_at": "2008-03-05T02:00:14Z",
    "labels": [
        "component: porting: cygwin",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.3",
    "title": "[with patch, needs review] generic univariate polynomial has no discriminant function",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2392",
    "user": "https://github.com/ncalexan"
}
```
Assignee: mabshoff

CC:  @ncalexan

Keywords: univariate polynomial discriminant

As it says: generic univariate polynomial has no discriminant function.

Issue created by migration from https://trac.sagemath.org/ticket/2392





---

archive/issue_comments_016099.json:
```json
{
    "body": "Attachment [2392-ncalexan-discriminant-1.patch](tarball://root/attachments/some-uuid/ticket2392/2392-ncalexan-discriminant-1.patch) by @malb created at 2008-03-05 11:30:28\n\n**Review**:\n* patch looks good, I say apply\n* shall we open a ticket for the mentioned Sage<->PARI issue?",
    "created_at": "2008-03-05T11:30:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2392",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2392#issuecomment-16099",
    "user": "https://github.com/malb"
}
```

Attachment [2392-ncalexan-discriminant-1.patch](tarball://root/attachments/some-uuid/ticket2392/2392-ncalexan-discriminant-1.patch) by @malb created at 2008-03-05 11:30:28

**Review**:
* patch looks good, I say apply
* shall we open a ticket for the mentioned Sage<->PARI issue?



---

archive/issue_comments_016100.json:
```json
{
    "body": "Replying to [comment:1 malb]:\n> **Review**:\n> * patch looks good, I say apply\n> * shall we open a ticket for the mentioned Sage<->PARI issue?\n\n\nHi malb,\n\nI assume you mean\n\n```\n+        Unfortunately SAGE does not handle PARI's variable ordering requirements\n+        gracefully, so the following fails:\n```\nin which case I would suggest that we open a ticket. Is that something that has been discussed before? I do not recall any currently open ticket that mentions pari and variable orderings.\n\nCheers,\n\nMichael",
    "created_at": "2008-03-05T13:28:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2392",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2392#issuecomment-16100",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Replying to [comment:1 malb]:
> **Review**:
> * patch looks good, I say apply
> * shall we open a ticket for the mentioned Sage<->PARI issue?


Hi malb,

I assume you mean

```
+        Unfortunately SAGE does not handle PARI's variable ordering requirements
+        gracefully, so the following fails:
```
in which case I would suggest that we open a ticket. Is that something that has been discussed before? I do not recall any currently open ticket that mentions pari and variable orderings.

Cheers,

Michael



---

archive/issue_comments_016101.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-05T13:29:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2392",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2392#issuecomment-16101",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_016102.json:
```json
{
    "body": "Merged in Sage 2.10.3.rc2",
    "created_at": "2008-03-05T13:29:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2392",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2392#issuecomment-16102",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.10.3.rc2



---

archive/issue_events_005644.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-03-05T13:29:27Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2392",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2392#event-5644"
}
```



---

archive/issue_comments_016103.json:
```json
{
    "body": "> Hi malb,\n> \n> I assume you mean\n> \n> ```\n> +        Unfortunately SAGE does not handle PARI's variable ordering requirements\n> +        gracefully, so the following fails:\n> ```\n> in which case I would suggest that we open a ticket. Is that something that has been discussed before? I do not recall any currently open ticket that mentions pari and variable orderings.\n\n\nJup.",
    "created_at": "2008-03-05T15:29:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2392",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2392#issuecomment-16103",
    "user": "https://github.com/malb"
}
```

> Hi malb,
> 
> I assume you mean
> 
> ```
> +        Unfortunately SAGE does not handle PARI's variable ordering requirements
> +        gracefully, so the following fails:
> ```
> in which case I would suggest that we open a ticket. Is that something that has been discussed before? I do not recall any currently open ticket that mentions pari and variable orderings.


Jup.
