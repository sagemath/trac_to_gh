# Issue 292: Problems with stacked polynomial rings and vector

archive/issues_000292.json:
```json
{
    "body": "Assignee: somebody\n\nKeywords: polynomial rings vector\n\n\n```\nR1, (r0, r1, s1, s2) = QQ['r0', 'r1', 's1', 's2'].objgens()\nR2, z = R1['z'].objgen()\nR3, zb = R2.quo(z**3 + r1*z + r0, names='zb').objgen()\n\ns = s1*z + s2*z**2\n\nf1 = R3(s*1)\nf2 = R3(s*z)\nf3 = R3(s*z**2)\nprint vector(f1)\n```\n\n\nSpins off into 100% CPU land.\n\nIssue created by migration from https://trac.sagemath.org/ticket/292\n\n",
    "created_at": "2007-02-24T05:33:12Z",
    "labels": [
        "basic arithmetic",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.2",
    "title": "Problems with stacked polynomial rings and vector",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/292",
    "user": "@ncalexan"
}
```
Assignee: somebody

Keywords: polynomial rings vector


```
R1, (r0, r1, s1, s2) = QQ['r0', 'r1', 's1', 's2'].objgens()
R2, z = R1['z'].objgen()
R3, zb = R2.quo(z**3 + r1*z + r0, names='zb').objgen()

s = s1*z + s2*z**2

f1 = R3(s*1)
f2 = R3(s*z)
f3 = R3(s*z**2)
print vector(f1)
```


Spins off into 100% CPU land.

Issue created by migration from https://trac.sagemath.org/ticket/292





---

archive/issue_comments_001382.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-08-19T01:30:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/292",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/292#issuecomment-1382",
    "user": "@williamstein"
}
```

Resolution: fixed



---

archive/issue_comments_001383.json:
```json
{
    "body": "fixed for sage-2.8.2 by William",
    "created_at": "2007-08-19T01:30:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/292",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/292#issuecomment-1383",
    "user": "@williamstein"
}
```

fixed for sage-2.8.2 by William
