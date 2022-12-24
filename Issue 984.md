# Issue 984: sage-2.8.9.rc1: sage-banner is empty

archive/issues_000984.json:
```json
{
    "body": "Assignee: was\n\nsage is missing its startup message in 2.8.9.rc1:\n\n```\ncwitty@magnetar:~/sage-2.8.9.rc1$ ./sage\n\nsage: \n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/984\n\n",
    "created_at": "2007-10-25T00:50:42Z",
    "labels": [
        "user interface",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.9",
    "title": "sage-2.8.9.rc1: sage-banner is empty",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/984",
    "user": "cwitty"
}
```
Assignee: was

sage is missing its startup message in 2.8.9.rc1:

```
cwitty@magnetar:~/sage-2.8.9.rc1$ ./sage

sage: 
```



Issue created by migration from https://trac.sagemath.org/ticket/984





---

archive/issue_comments_006018.json:
```json
{
    "body": "When I do sage -sdist even using that binary I get that a banner\nis created.  I banner certainly gets created when I do -sdist from\nmy sage install.  So it will be in the released version.",
    "created_at": "2007-10-25T07:56:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/984",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/984#issuecomment-6018",
    "user": "was"
}
```

When I do sage -sdist even using that binary I get that a banner
is created.  I banner certainly gets created when I do -sdist from
my sage install.  So it will be in the released version.



---

archive/issue_comments_006019.json:
```json
{
    "body": "So this ought to be close against 2.8.9 then.\n\nMichael",
    "created_at": "2007-10-25T10:48:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/984",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/984#issuecomment-6019",
    "user": "mabshoff"
}
```

So this ought to be close against 2.8.9 then.

Michael



---

archive/issue_comments_006020.json:
```json
{
    "body": "Fixed in final 2.8.9 and verified with local build.\n\nCheers,\n\nMichael",
    "created_at": "2007-10-27T05:17:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/984",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/984#issuecomment-6020",
    "user": "mabshoff"
}
```

Fixed in final 2.8.9 and verified with local build.

Cheers,

Michael



---

archive/issue_comments_006021.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-10-27T05:17:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/984",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/984#issuecomment-6021",
    "user": "mabshoff"
}
```

Resolution: fixed
