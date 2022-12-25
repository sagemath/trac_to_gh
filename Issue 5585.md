# Issue 5585: [with patch, needs review]

archive/issues_005585.json:
```json
{
    "body": "Assignee: @malb\n\nCC:  @burcin rpw\n\nKeywords: crypto, aes\n\n**Before**:\n\n```\nsage: sr = mq.SR(4,4,4,8,gf2=True,polybori=True,allow_zero_inversions=True)\nsage: %time F,s = sr.polynomial_system()\nCPU times: user 23.46 s, sys: 0.07 s, total: 23.52 s\nWall time: 23.61 s\n```\n\n**After**:\n\n```\nsage: sr = mq.SR(4,4,4,8,gf2=True,polybori=True,allow_zero_inversions=True)\nsage: %time F,s = sr.polynomial_system()\nCPU times: user 3.58 s, sys: 0.04 s, total: 3.62 s\nWall time: 3.63 s\nsage: %time F,s = sr.polynomial_system()\nCPU times: user 2.05 s, sys: 0.00 s, total: 2.05 s\nWall time: 2.05 s\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/5585\n\n",
    "created_at": "2009-03-22T17:53:42Z",
    "labels": [
        "component: commutative algebra"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4.1",
    "title": "[with patch, needs review]",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5585",
    "user": "https://github.com/malb"
}
```
Assignee: @malb

CC:  @burcin rpw

Keywords: crypto, aes

**Before**:

```
sage: sr = mq.SR(4,4,4,8,gf2=True,polybori=True,allow_zero_inversions=True)
sage: %time F,s = sr.polynomial_system()
CPU times: user 23.46 s, sys: 0.07 s, total: 23.52 s
Wall time: 23.61 s
```

**After**:

```
sage: sr = mq.SR(4,4,4,8,gf2=True,polybori=True,allow_zero_inversions=True)
sage: %time F,s = sr.polynomial_system()
CPU times: user 3.58 s, sys: 0.04 s, total: 3.62 s
Wall time: 3.63 s
sage: %time F,s = sr.polynomial_system()
CPU times: user 2.05 s, sys: 0.00 s, total: 2.05 s
Wall time: 2.05 s
```

Issue created by migration from https://trac.sagemath.org/ticket/5585





---

archive/issue_comments_043447.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2009-03-22T20:09:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5585",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5585#issuecomment-43447",
    "user": "https://github.com/malb"
}
```

Resolution: duplicate



---

archive/issue_events_013156.json:
```json
{
    "actor": "https://github.com/malb",
    "created_at": "2009-03-22T20:09:28Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5585",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5585#event-13156"
}
```
