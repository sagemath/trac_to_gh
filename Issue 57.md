# Issue 57: certain p-adic coercions insanely slow

archive/issues_000057.json:
```json
{
    "body": "Assignee: somebody\n\nThe following calculation should be virtually instantaneous:\n\n\n```\nsage: x = 2**120000/3**100000\nsage: K = pAdicField(5, 5)\nsage: time y = K(x)\nCPU times: user 2.72 s, sys: 0.00 s, total: 2.72 s\nWall time: 2.72\n```\n\n\nIt should take about as long as just reducing numerator and denominator separately:\n\n```\nsage: time z = K(x.numerator())\nCPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s\nWall time: 0.00\n\nsage: time z = K(x.denominator())\nCPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s\nWall time: 0.00\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/57\n\n",
    "created_at": "2006-09-14T01:55:25Z",
    "labels": [
        "basic arithmetic",
        "major",
        "bug"
    ],
    "title": "certain p-adic coercions insanely slow",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/57",
    "user": "dmharvey"
}
```
Assignee: somebody

The following calculation should be virtually instantaneous:


```
sage: x = 2**120000/3**100000
sage: K = pAdicField(5, 5)
sage: time y = K(x)
CPU times: user 2.72 s, sys: 0.00 s, total: 2.72 s
Wall time: 2.72
```


It should take about as long as just reducing numerator and denominator separately:

```
sage: time z = K(x.numerator())
CPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s
Wall time: 0.00

sage: time z = K(x.denominator())
CPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s
Wall time: 0.00
```



Issue created by migration from https://trac.sagemath.org/ticket/57





---

archive/issue_comments_000302.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2006-09-16T05:04:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/57",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/57#issuecomment-302",
    "user": "dmharvey"
}
```

Resolution: fixed



---

archive/issue_comments_000303.json:
```json
{
    "body": "Fixed:\n\nThu Sep 14 19:17:11 PDT 2006  dmharvey`@`math.harvard.edu\n* padic.py -- fixes trac bug #57",
    "created_at": "2006-09-16T05:04:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/57",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/57#issuecomment-303",
    "user": "dmharvey"
}
```

Fixed:

Thu Sep 14 19:17:11 PDT 2006  dmharvey`@`math.harvard.edu
* padic.py -- fixes trac bug #57
