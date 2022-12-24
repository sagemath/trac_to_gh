# Issue 8563: R interpreter starts (seemingly) without reason

archive/issues_008563.json:
```json
{
    "body": "Assignee: @burcin\n\nCC:  @mwhansen\n\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nsage: var('r')\nr\nsage: simplify((r-1)^3 *r)\n(r - 1)^3*r\nsage: quit\nExiting SAGE (CPU time 0m0.08s, Wall time 0m32.87s).\nExiting spawned R Interpreter process.\nExiting spawned Maxima process.\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8563\n\n",
    "created_at": "2010-03-20T01:48:46Z",
    "labels": [
        "symbolics",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "R interpreter starts (seemingly) without reason",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8563",
    "user": "@rishikesha"
}
```
Assignee: @burcin

CC:  @mwhansen


```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: var('r')
r
sage: simplify((r-1)^3 *r)
(r - 1)^3*r
sage: quit
Exiting SAGE (CPU time 0m0.08s, Wall time 0m32.87s).
Exiting spawned R Interpreter process.
Exiting spawned Maxima process.
```


Issue created by migration from https://trac.sagemath.org/ticket/8563





---

archive/issue_comments_077533.json:
```json
{
    "body": "This is a duplicate of #7661. After applying the patch attached to that ticket we get the response from `simplify()` faster and there is no R interpreter on exit.",
    "created_at": "2010-04-05T18:27:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8563",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8563#issuecomment-77533",
    "user": "@burcin"
}
```

This is a duplicate of #7661. After applying the patch attached to that ticket we get the response from `simplify()` faster and there is no R interpreter on exit.



---

archive/issue_comments_077534.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2010-04-05T18:27:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8563",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8563#issuecomment-77534",
    "user": "@burcin"
}
```

Resolution: duplicate
