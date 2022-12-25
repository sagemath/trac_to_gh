# Issue 3701: [with spkg, needs review] Solaris: fix polybori build due to bashism

archive/issues_003701.json:
```json
{
    "body": "Assignee: mabshoff\n\nPolybori.spkg contains some bashism that cause trouble on Solaris. So change the shebang to use \"#1/usr/bin/env bash\". That is the only change in the spkg at\n\nhttp://sage.math.washington.edu/home/mabshoff/release-cycles-3.0.6/alpha1/polybori-0.3.1.p4.spkg\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/3701\n\n",
    "created_at": "2008-07-21T21:55:21Z",
    "labels": [
        "component: porting: solaris",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.6",
    "title": "[with spkg, needs review] Solaris: fix polybori build due to bashism",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3701",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff

Polybori.spkg contains some bashism that cause trouble on Solaris. So change the shebang to use "#1/usr/bin/env bash". That is the only change in the spkg at

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.0.6/alpha1/polybori-0.3.1.p4.spkg

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/3701





---

archive/issue_comments_026199.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-07-21T21:55:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3701",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3701#issuecomment-26199",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_026200.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-07-21T22:12:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3701",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3701#issuecomment-26200",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_026201.json:
```json
{
    "body": "Merged in Sage 3.0.6.rc0",
    "created_at": "2008-07-21T22:12:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3701",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3701#issuecomment-26201",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.0.6.rc0
