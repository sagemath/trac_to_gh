# Issue 1569: solve() fails if one list element is True

archive/issues_001569.json:
```json
{
    "body": "Assignee: @williamstein\n\nAs reported by Brandon Barker at http://groups.google.com/group/sage-devel/browse_thread/thread/52683f508ccefb39#:\n\n```\nsage: solve([3==3, 1.00000000000000*x^3 == 0], x)\n[]\nsage: solve([1.00000000000000*x^3 == 0], x)\n[x == 0]\nsage: solve([1==3, 1.00000000000000*x^3 == 0], x)\n[]\n```\n\n\nThe first result is wrong; it should be the same as the second.\n\nNote that \"3==3\" will immediately evaluate to a Python boolean True; probably solve() should just strip list elements that are True.\n\nIssue created by migration from https://trac.sagemath.org/ticket/1569\n\n",
    "created_at": "2007-12-19T18:45:46Z",
    "labels": [
        "algebraic geometry",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.9.1",
    "title": "solve() fails if one list element is True",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1569",
    "user": "cwitty"
}
```
Assignee: @williamstein

As reported by Brandon Barker at http://groups.google.com/group/sage-devel/browse_thread/thread/52683f508ccefb39#:

```
sage: solve([3==3, 1.00000000000000*x^3 == 0], x)
[]
sage: solve([1.00000000000000*x^3 == 0], x)
[x == 0]
sage: solve([1==3, 1.00000000000000*x^3 == 0], x)
[]
```


The first result is wrong; it should be the same as the second.

Note that "3==3" will immediately evaluate to a Python boolean True; probably solve() should just strip list elements that are True.

Issue created by migration from https://trac.sagemath.org/ticket/1569





---

archive/issue_comments_009995.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-12-20T20:12:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1569",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1569#issuecomment-9995",
    "user": "@williamstein"
}
```

Changing status from new to assigned.



---

archive/issue_comments_009996.json:
```json
{
    "body": "Attachment [trac-1569.patch](tarball://root/attachments/some-uuid/ticket1569/trac-1569.patch) by @williamstein created at 2007-12-20 20:18:12",
    "created_at": "2007-12-20T20:18:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1569",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1569#issuecomment-9996",
    "user": "@williamstein"
}
```

Attachment [trac-1569.patch](tarball://root/attachments/some-uuid/ticket1569/trac-1569.patch) by @williamstein created at 2007-12-20 20:18:12



---

archive/issue_comments_009997.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-21T01:44:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1569",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1569#issuecomment-9997",
    "user": "@rlmill"
}
```

Resolution: fixed



---

archive/issue_comments_009998.json:
```json
{
    "body": "merged in 2.9.1 alpha2",
    "created_at": "2007-12-21T01:44:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1569",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1569#issuecomment-9998",
    "user": "@rlmill"
}
```

merged in 2.9.1 alpha2
