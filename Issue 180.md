# Issue 180: -s option to sage issues

archive/issues_000180.json:
```json
{
    "body": "Assignee: @williamstein\n\n\n```\n[justin]: Hmmm...it's actually \"-s -i\".  The 'sage' command seems to care about the order of switches; \"-f -i\" works, while \"-i -f\" doesn't.  \"-i -s\" does not save the results, while '-s -i' does.  Is that intentional?\n[11:54am] was389: it's a bug.\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/180\n\n",
    "created_at": "2006-12-10T19:59:06Z",
    "labels": [
        "packages: standard",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "-s option to sage issues",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/180",
    "user": "@williamstein"
}
```
Assignee: @williamstein


```
[justin]: Hmmm...it's actually "-s -i".  The 'sage' command seems to care about the order of switches; "-f -i" works, while "-i -f" doesn't.  "-i -s" does not save the results, while '-s -i' does.  Is that intentional?
[11:54am] was389: it's a bug.
```


Issue created by migration from https://trac.sagemath.org/ticket/180





---

archive/issue_comments_000825.json:
```json
{
    "body": "Hmmm again: \n$ sage -s -i gd-2.0.33.p1\nUnknown option: -s\nusage: sage [options]\nTry 'sage -h' for more information.\n\nWorks when used as \"sage -f -s -i gd-2.0.33.p1\"",
    "created_at": "2006-12-11T01:27:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/180",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/180#issuecomment-825",
    "user": "justin"
}
```

Hmmm again: 
$ sage -s -i gd-2.0.33.p1
Unknown option: -s
usage: sage [options]
Try 'sage -h' for more information.

Works when used as "sage -f -s -i gd-2.0.33.p1"



---

archive/issue_comments_000826.json:
```json
{
    "body": "And just to continue filling out forms:\n\nsage -i -s gd-2.0.33.p1\n\nworks.  Yeesh....",
    "created_at": "2006-12-11T01:29:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/180",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/180#issuecomment-826",
    "user": "justin"
}
```

And just to continue filling out forms:

sage -i -s gd-2.0.33.p1

works.  Yeesh....



---

archive/issue_comments_000827.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2007-01-13T02:40:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/180",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/180#issuecomment-827",
    "user": "@williamstein"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_000828.json:
```json
{
    "body": "change to enhancement, i.e., sage currently doesn't support complicated command\nline switches and doesn't claim to!",
    "created_at": "2007-01-13T02:40:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/180",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/180#issuecomment-828",
    "user": "@williamstein"
}
```

change to enhancement, i.e., sage currently doesn't support complicated command
line switches and doesn't claim to!



---

archive/issue_comments_000829.json:
```json
{
    "body": "This ticket is the same issue as #21, so I am closing this as a dupe and adding a comment to #21 to also check these issues.\n\nCheers,\n\nMichael",
    "created_at": "2008-09-24T02:58:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/180",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/180#issuecomment-829",
    "user": "mabshoff"
}
```

This ticket is the same issue as #21, so I am closing this as a dupe and adding a comment to #21 to also check these issues.

Cheers,

Michael



---

archive/issue_comments_000830.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2008-09-24T02:58:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/180",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/180#issuecomment-830",
    "user": "mabshoff"
}
```

Resolution: duplicate
