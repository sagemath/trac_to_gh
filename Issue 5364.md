# Issue 5364: unused maxima builtin functions for matrices over SR

archive/issues_005364.json:
```json
{
    "body": "Assignee: @williamstein\n\nsome functions are not wraped which makes e.g. identity_matrix or transpose awfully slow for matrices over SR.\n(we do not use maxime.ident nor maxima.transpose)\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5364\n\n",
    "created_at": "2009-02-24T23:42:26Z",
    "labels": [
        "linear algebra",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "unused maxima builtin functions for matrices over SR",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5364",
    "user": "ylchapuy"
}
```
Assignee: @williamstein

some functions are not wraped which makes e.g. identity_matrix or transpose awfully slow for matrices over SR.
(we do not use maxime.ident nor maxima.transpose)



Issue created by migration from https://trac.sagemath.org/ticket/5364





---

archive/issue_comments_041327.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2009-06-05T01:35:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5364",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5364#issuecomment-41327",
    "user": "@mwhansen"
}
```

Resolution: invalid



---

archive/issue_comments_041328.json:
```json
{
    "body": "This was fixed by converting symbolic matrices to use Sage's generic dense matrix backend:\n\n\n```\nsage: m = MatrixSpace(SR, 1000, 1000)\nsage: %time a = m.identity_matrix()\nCPU times: user 0.04 s, sys: 0.00 s, total: 0.04 s\nWall time: 0.04 s\nsage: %time b = a.transpose()\nCPU times: user 0.05 s, sys: 0.01 s, total: 0.06 s\nWall time: 0.06 s\n```\n",
    "created_at": "2009-06-05T01:35:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5364",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5364#issuecomment-41328",
    "user": "@mwhansen"
}
```

This was fixed by converting symbolic matrices to use Sage's generic dense matrix backend:


```
sage: m = MatrixSpace(SR, 1000, 1000)
sage: %time a = m.identity_matrix()
CPU times: user 0.04 s, sys: 0.00 s, total: 0.04 s
Wall time: 0.04 s
sage: %time b = a.transpose()
CPU times: user 0.05 s, sys: 0.01 s, total: 0.06 s
Wall time: 0.06 s
```

