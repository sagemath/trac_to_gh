# Issue 3089: removing an attached file doesn't work

archive/issues_003089.json:
```json
{
    "body": "Assignee: somebody\n\nThe help page given by attach? claims:\n\n```\n        Type attached_files() for a list of all currently attached files.\n        You can remove files from this list to stop them from being watched. \n```\n\nIn fact, this has no effect when I try it:\n\n```\nsage: version()\n'SAGE Version 2.10.1, Release Date: 2008-02-02'\nsage: attached_files()\n['/mit/price/tmp/hessian.sage']\nsage: attached_files().pop()\n'/mit/price/tmp/hessian.sage'\nsage: attached_files()\n['/mit/price/tmp/hessian.sage']\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3089\n\n",
    "created_at": "2008-05-03T06:51:25Z",
    "labels": [
        "component: basic arithmetic",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.1",
    "title": "removing an attached file doesn't work",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3089",
    "user": "https://trac.sagemath.org/admin/accounts/users/gnprice"
}
```
Assignee: somebody

The help page given by attach? claims:

```
        Type attached_files() for a list of all currently attached files.
        You can remove files from this list to stop them from being watched. 
```

In fact, this has no effect when I try it:

```
sage: version()
'SAGE Version 2.10.1, Release Date: 2008-02-02'
sage: attached_files()
['/mit/price/tmp/hessian.sage']
sage: attached_files().pop()
'/mit/price/tmp/hessian.sage'
sage: attached_files()
['/mit/price/tmp/hessian.sage']
```


Issue created by migration from https://trac.sagemath.org/ticket/3089





---

archive/issue_comments_021281.json:
```json
{
    "body": "Changing assignee from somebody to tba.",
    "created_at": "2008-05-03T07:02:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3089",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3089#issuecomment-21281",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing assignee from somebody to tba.



---

archive/issue_comments_021282.json:
```json
{
    "body": "Changing component from basic arithmetic to documentation.",
    "created_at": "2008-05-03T07:02:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3089",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3089#issuecomment-21282",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing component from basic arithmetic to documentation.



---

archive/issue_events_006972.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-05-03T07:02:43Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3089",
    "milestone": "sage-3.0.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3089#event-6972"
}
```



---

archive/issue_comments_021283.json:
```json
{
    "body": "This part of the documentation is plainly wrong and no longer valid.\n\nCheers,\n\nMichael",
    "created_at": "2008-05-03T07:02:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3089",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3089#issuecomment-21283",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This part of the documentation is plainly wrong and no longer valid.

Cheers,

Michael



---

archive/issue_comments_021284.json:
```json
{
    "body": "OK, that's one possible response.  I'd like to be able to make Sage stop watching a file, though; either in the admittedly hackish way the documentation describes, or by a \"detach\" or \"unattach\" command.\n\nThanks,\nGreg",
    "created_at": "2008-05-03T07:43:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3089",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3089#issuecomment-21284",
    "user": "https://trac.sagemath.org/admin/accounts/users/gnprice"
}
```

OK, that's one possible response.  I'd like to be able to make Sage stop watching a file, though; either in the admittedly hackish way the documentation describes, or by a "detach" or "unattach" command.

Thanks,
Greg



---

archive/issue_comments_021285.json:
```json
{
    "body": "Yes, I thought we had either a detach or unattach command, but I couldn't find either one. So it has either been discussed and never implemented or it isn't in the global namespace. Either way it should be fixed.\n\nCheers,\n\nMichael",
    "created_at": "2008-05-03T12:32:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3089",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3089#issuecomment-21285",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Yes, I thought we had either a detach or unattach command, but I couldn't find either one. So it has either been discussed and never implemented or it isn't in the global namespace. Either way it should be fixed.

Cheers,

Michael



---

archive/issue_comments_021286.json:
```json
{
    "body": "Cf. #7514.",
    "created_at": "2010-01-16T19:01:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3089",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3089#issuecomment-21286",
    "user": "https://github.com/qed777"
}
```

Cf. #7514.



---

archive/issue_comments_021287.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-17T14:13:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3089",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3089#issuecomment-21287",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_events_006973.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2010-01-17T14:13:17Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3089",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3089#event-6973"
}
```
