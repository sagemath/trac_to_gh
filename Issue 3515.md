# Issue 3515: Finance builds incorrectly with pbuild

archive/issues_003515.json:
```json
{
    "body": "Assignee: @garyfurnish\n\nFinance needs to be set up or pbuild configured to properly compile.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3515\n\n",
    "created_at": "2008-06-26T15:48:43Z",
    "labels": [
        "component: pbuild",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Finance builds incorrectly with pbuild",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3515",
    "user": "https://trac.sagemath.org/admin/accounts/users/ghtdak"
}
```
Assignee: @garyfurnish

Finance needs to be set up or pbuild configured to properly compile.

Issue created by migration from https://trac.sagemath.org/ticket/3515





---

archive/issue_comments_024725.json:
```json
{
    "body": "Glenn,\n\ncould you post some actual output from the failure?\n\nCheers,\n\nMichael",
    "created_at": "2008-06-26T19:01:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3515",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3515#issuecomment-24725",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Glenn,

could you post some actual output from the failure?

Cheers,

Michael



---

archive/issue_comments_024726.json:
```json
{
    "body": "We don't have output per se.  It just didn't work and william suggested trying it without pbuild and it was fine.  I've discussed with Gary and we didn't implement at the time as he was refactoring the pbuild code but is aware of the problem.\n\nMy understanding is that its a straightforward entry somewhere but I don't have any information as to how to configure pbuild.",
    "created_at": "2008-06-27T02:37:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3515",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3515#issuecomment-24726",
    "user": "https://trac.sagemath.org/admin/accounts/users/ghtdak"
}
```

We don't have output per se.  It just didn't work and william suggested trying it without pbuild and it was fine.  I've discussed with Gary and we didn't implement at the time as he was refactoring the pbuild code but is aware of the problem.

My understanding is that its a straightforward entry somewhere but I don't have any information as to how to configure pbuild.



---

archive/issue_comments_024727.json:
```json
{
    "body": "This should be easy to fix after #3399 is applied.  I included some documentation on how to correctly modify pbuild.",
    "created_at": "2008-07-01T17:15:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3515",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3515#issuecomment-24727",
    "user": "https://github.com/garyfurnish"
}
```

This should be easy to fix after #3399 is applied.  I included some documentation on how to correctly modify pbuild.



---

archive/issue_comments_024728.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2008-07-12T14:05:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3515",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3515#issuecomment-24728",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: invalid



---

archive/issue_events_003732.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-07-12T14:05:06Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3515",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3515#event-3732"
}
```



---

archive/issue_comments_024729.json:
```json
{
    "body": "This is a duplicate of #3614.\n\nGary, please check for existing tickets before opening new ones. This is a pbuild ticket owned by you, so you should know about this.\n\nCheers,\n\nMichael",
    "created_at": "2008-07-12T14:05:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3515",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3515#issuecomment-24729",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This is a duplicate of #3614.

Gary, please check for existing tickets before opening new ones. This is a pbuild ticket owned by you, so you should know about this.

Cheers,

Michael
