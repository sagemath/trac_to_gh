# Issue 6860: dimensions of modular forms spaces for Gamma(N) is busted / not implemented

archive/issues_006860.json:
```json
{
    "body": "Assignee: @williamstein\n\n\n```\nsage: dimension_cusp_forms(Gamma(11))\n[hangs forever]\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6860\n\n",
    "created_at": "2009-09-02T02:22:05Z",
    "labels": [
        "component: number theory",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "dimensions of modular forms spaces for Gamma(N) is busted / not implemented",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6860",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein


```
sage: dimension_cusp_forms(Gamma(11))
[hangs forever]
```


Issue created by migration from https://trac.sagemath.org/ticket/6860





---

archive/issue_comments_056475.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2009-09-02T13:05:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6860",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6860#issuecomment-56475",
    "user": "https://github.com/williamstein"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_056476.json:
```json
{
    "body": "Wait, I'm just impatient, since:\n\n```\nsage: dimension_cusp_forms(Gamma(11))\n26\n```\n\n\nSo I'm changing this to an enhancement, since I think this should be fast.",
    "created_at": "2009-09-02T13:05:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6860",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6860#issuecomment-56476",
    "user": "https://github.com/williamstein"
}
```

Wait, I'm just impatient, since:

```
sage: dimension_cusp_forms(Gamma(11))
26
```


So I'm changing this to an enhancement, since I think this should be fast.



---

archive/issue_comments_056477.json:
```json
{
    "body": "Changing component from number theory to modular forms.",
    "created_at": "2013-07-22T15:22:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6860",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6860#issuecomment-56477",
    "user": "https://github.com/loefflerd"
}
```

Changing component from number theory to modular forms.



---

archive/issue_comments_056478.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2013-07-22T15:22:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6860",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6860#issuecomment-56478",
    "user": "https://github.com/loefflerd"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_056479.json:
```json
{
    "body": "This has now been fastified:\n\n```python\nsage: %time dimension_cusp_forms(Gamma(10^28+731))                             \nCPU times: user 0.04 s, sys: 0.02 s, total: 0.06 s\nWall time: 1.54 s\n36274370885528165103530592700784546931709800073501194539717685491542679896172544001\n```\n\n(and most of that is the time taken to factor the level). I propose closing this as fixed.",
    "created_at": "2013-07-22T15:22:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6860",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6860#issuecomment-56479",
    "user": "https://github.com/loefflerd"
}
```

This has now been fastified:

```python
sage: %time dimension_cusp_forms(Gamma(10^28+731))                             
CPU times: user 0.04 s, sys: 0.02 s, total: 0.06 s
Wall time: 1.54 s
36274370885528165103530592700784546931709800073501194539717685491542679896172544001
```

(and most of that is the time taken to factor the level). I propose closing this as fixed.



---

archive/issue_comments_056480.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2013-07-22T16:41:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6860",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6860#issuecomment-56480",
    "user": "https://github.com/aghitza"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_056481.json:
```json
{
    "body": "Agreed.",
    "created_at": "2013-07-22T16:41:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6860",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6860#issuecomment-56481",
    "user": "https://github.com/aghitza"
}
```

Agreed.



---

archive/issue_comments_056482.json:
```json
{
    "body": "Changing type from enhancement to defect.",
    "created_at": "2013-07-22T16:41:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6860",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6860#issuecomment-56482",
    "user": "https://github.com/aghitza"
}
```

Changing type from enhancement to defect.



---

archive/issue_comments_056483.json:
```json
{
    "body": "Changing keywords from \"\" to \"sd51\".",
    "created_at": "2013-07-22T16:46:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6860",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6860#issuecomment-56483",
    "user": "https://github.com/aghitza"
}
```

Changing keywords from "" to "sd51".



---

archive/issue_comments_056484.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2013-08-13T08:46:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6860",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6860#issuecomment-56484",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: duplicate
