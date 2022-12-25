# Issue 180: -s option to sage issues

archive/issues_000180.json:
```json
{
    "body": "Assignee: @williamstein\n\n\n```\n[justin]: Hmmm...it's actually \"-s -i\".  The 'sage' command seems to care about the order of switches; \"-f -i\" works, while \"-i -f\" doesn't.  \"-i -s\" does not save the results, while '-s -i' does.  Is that intentional?\n[11:54am] was389: it's a bug.\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/180\n\n",
    "created_at": "2006-12-10T19:59:06Z",
    "labels": [
        "component: packages: standard",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "-s option to sage issues",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/180",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein


```
[justin]: Hmmm...it's actually "-s -i".  The 'sage' command seems to care about the order of switches; "-f -i" works, while "-i -f" doesn't.  "-i -s" does not save the results, while '-s -i' does.  Is that intentional?
[11:54am] was389: it's a bug.
```


Issue created by migration from https://trac.sagemath.org/ticket/180





---

archive/issue_comments_000822.json:
```json
{
    "body": "Hmmm again: \n$ sage -s -i gd-2.0.33.p1\nUnknown option: -s\nusage: sage [options]\nTry 'sage -h' for more information.\n\nWorks when used as \"sage -f -s -i gd-2.0.33.p1\"",
    "created_at": "2006-12-11T01:27:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/180",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/180#issuecomment-822",
    "user": "https://trac.sagemath.org/admin/accounts/users/justin"
}
```

Hmmm again: 
$ sage -s -i gd-2.0.33.p1
Unknown option: -s
usage: sage [options]
Try 'sage -h' for more information.

Works when used as "sage -f -s -i gd-2.0.33.p1"



---

archive/issue_comments_000823.json:
```json
{
    "body": "And just to continue filling out forms:\n\nsage -i -s gd-2.0.33.p1\n\nworks.  Yeesh....",
    "created_at": "2006-12-11T01:29:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/180",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/180#issuecomment-823",
    "user": "https://trac.sagemath.org/admin/accounts/users/justin"
}
```

And just to continue filling out forms:

sage -i -s gd-2.0.33.p1

works.  Yeesh....



---

archive/issue_comments_000824.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2007-01-13T02:40:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/180",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/180#issuecomment-824",
    "user": "https://github.com/williamstein"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_000825.json:
```json
{
    "body": "change to enhancement, i.e., sage currently doesn't support complicated command\nline switches and doesn't claim to!",
    "created_at": "2007-01-13T02:40:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/180",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/180#issuecomment-825",
    "user": "https://github.com/williamstein"
}
```

change to enhancement, i.e., sage currently doesn't support complicated command
line switches and doesn't claim to!



---

archive/issue_events_000340.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-08-24T22:53:13Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/180",
    "milestone": "sage-2.9",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/180#event-340"
}
```



---

archive/issue_comments_000826.json:
```json
{
    "body": "This ticket is the same issue as #21, so I am closing this as a dupe and adding a comment to #21 to also check these issues.\n\nCheers,\n\nMichael",
    "created_at": "2008-09-24T02:58:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/180",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/180#issuecomment-826",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This ticket is the same issue as #21, so I am closing this as a dupe and adding a comment to #21 to also check these issues.

Cheers,

Michael



---

archive/issue_comments_000827.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2008-09-24T02:58:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/180",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/180#issuecomment-827",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: duplicate



---

archive/issue_events_000341.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-09-24T02:58:55Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/180",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/180#event-341"
}
```



---

archive/issue_events_000342.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-09-24T02:58:55Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/180",
    "milestone": "sage-2.9",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/180#event-342"
}
```
