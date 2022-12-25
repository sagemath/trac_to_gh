# Issue 8356: python is configured with an unreconised option

archive/issues_008356.json:
```json
{
    "body": "Assignee: tbd\n\nWhen python is configured, it is showing the following warning:\n\n\n```\nconfigure: WARNING: unrecognized options: --without-libpng\n```\n\n\nIt would be good if when people update packages, they actually check things like the options. R recently had --without-iconv, despite that was no longer an option. \n\n\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8356\n\n",
    "created_at": "2010-02-25T03:58:59Z",
    "labels": [
        "component: packages: standard",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.4",
    "title": "python is configured with an unreconised option",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8356",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```
Assignee: tbd

When python is configured, it is showing the following warning:


```
configure: WARNING: unrecognized options: --without-libpng
```


It would be good if when people update packages, they actually check things like the options. R recently had --without-iconv, despite that was no longer an option. 





Issue created by migration from https://trac.sagemath.org/ticket/8356





---

archive/issue_comments_074523.json:
```json
{
    "body": "If the issues at #7867 can be solved by some updates to python, which may be the case, then I'll fix this as part of the fixes for #7867. Otherwise, it will have to wait for someone else to do it. \n\nI'm dropping the priority of this, as the warning is harmless.",
    "created_at": "2010-02-25T04:10:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8356",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8356#issuecomment-74523",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

If the issues at #7867 can be solved by some updates to python, which may be the case, then I'll fix this as part of the fixes for #7867. Otherwise, it will have to wait for someone else to do it. 

I'm dropping the priority of this, as the warning is harmless.



---

archive/issue_comments_074524.json:
```json
{
    "body": "Changing priority from major to minor.",
    "created_at": "2010-02-25T04:10:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8356",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8356#issuecomment-74524",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing priority from major to minor.



---

archive/issue_events_008546.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2010-03-07T01:36:05Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8356",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8356#event-8546"
}
```



---

archive/issue_comments_074525.json:
```json
{
    "body": "Fixed by #8440.",
    "created_at": "2010-03-07T01:36:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8356",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8356#issuecomment-74525",
    "user": "https://github.com/mwhansen"
}
```

Fixed by #8440.



---

archive/issue_comments_074526.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-03-07T01:36:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8356",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8356#issuecomment-74526",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed
