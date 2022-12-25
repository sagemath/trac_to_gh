# Issue 1037: arithmetic with Schubert polynomials includes extra fixed points in the permutations

archive/issues_001037.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  sage-combinat\n\nFor example,\n\n\n```\nsage: X([3,2,1])*X([4,3,2,1])\nX[6, 4, 2, 1, 3, 5, 7]\n```\n\n\nshould be\n\n\n```\nsage: X([3,2,1])*X([4,3,2,1])\nX[6, 4, 2, 1, 3, 5]\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1037\n\n",
    "created_at": "2007-10-30T22:49:41Z",
    "labels": [
        "component: algebraic geometry",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.11",
    "title": "arithmetic with Schubert polynomials includes extra fixed points in the permutations",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1037",
    "user": "https://github.com/mwhansen"
}
```
Assignee: @williamstein

CC:  sage-combinat

For example,


```
sage: X([3,2,1])*X([4,3,2,1])
X[6, 4, 2, 1, 3, 5, 7]
```


should be


```
sage: X([3,2,1])*X([4,3,2,1])
X[6, 4, 2, 1, 3, 5]
```


Issue created by migration from https://trac.sagemath.org/ticket/1037





---

archive/issue_comments_006312.json:
```json
{
    "body": "Changing priority from major to minor.",
    "created_at": "2007-10-30T23:19:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1037",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1037#issuecomment-6312",
    "user": "https://github.com/mwhansen"
}
```

Changing priority from major to minor.



---

archive/issue_events_002829.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-10-31T01:58:00Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1037",
    "milestone": "sage-2.8.11",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1037#event-2829"
}
```



---

archive/issue_comments_006313.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-11-01T09:22:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1037",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1037#issuecomment-6313",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_006314.json:
```json
{
    "body": "Attachment [schubert.patch](tarball://root/attachments/some-uuid/ticket1037/schubert.patch) by mabshoff created at 2007-11-01 09:22:16\n\napplied to 2.8.11.alpha0",
    "created_at": "2007-11-01T09:22:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1037",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1037#issuecomment-6314",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [schubert.patch](tarball://root/attachments/some-uuid/ticket1037/schubert.patch) by mabshoff created at 2007-11-01 09:22:16

applied to 2.8.11.alpha0



---

archive/issue_events_002830.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-11-01T09:22:16Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1037",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1037#event-2830"
}
```



---

archive/issue_comments_006315.json:
```json
{
    "body": "Changing component from algebraic geometry to combinatorics.",
    "created_at": "2007-11-01T09:22:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1037",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1037#issuecomment-6315",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing component from algebraic geometry to combinatorics.
