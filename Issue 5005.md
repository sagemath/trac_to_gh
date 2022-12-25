# Issue 5005: polynomial_template __init__ from list horribly innefficient

archive/issues_005005.json:
```json
{
    "body": "Assignee: tbd\n\n\n```\n            for e in x:\n                # r += parent(e)*power\n                celement_pow(&monomial, &gen, deg, NULL, parent)\n                coeff = (<Polynomial_template>parent(e)).x\n                celement_mul(&monomial, &coeff, &monomial, parent)\n                celement_add(&self.x, &self.x, &monomial, parent)\n                deg += 1\n```\n\n\nThere should be a celement_set(self, x, i). \n\nIssue created by migration from https://trac.sagemath.org/ticket/5005\n\n",
    "created_at": "2009-01-17T23:58:30Z",
    "labels": [
        "component: algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "polynomial_template __init__ from list horribly innefficient",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5005",
    "user": "https://github.com/robertwb"
}
```
Assignee: tbd


```
            for e in x:
                # r += parent(e)*power
                celement_pow(&monomial, &gen, deg, NULL, parent)
                coeff = (<Polynomial_template>parent(e)).x
                celement_mul(&monomial, &coeff, &monomial, parent)
                celement_add(&self.x, &self.x, &monomial, parent)
                deg += 1
```


There should be a celement_set(self, x, i). 

Issue created by migration from https://trac.sagemath.org/ticket/5005





---

archive/issue_comments_038101.json:
```json
{
    "body": "The polynomial template framework has no c-level concept of elements of the basering, so there's not much that can be done here. Both ZZ[x] and Z/nZ[x] override `__init__` to be more efficient, so it's not really an issue, and so I'm closing this as won't fix.",
    "created_at": "2010-01-17T09:45:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5005",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5005#issuecomment-38101",
    "user": "https://github.com/robertwb"
}
```

The polynomial template framework has no c-level concept of elements of the basering, so there's not much that can be done here. Both ZZ[x] and Z/nZ[x] override `__init__` to be more efficient, so it's not really an issue, and so I'm closing this as won't fix.



---

archive/issue_comments_038102.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2010-01-17T09:45:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5005",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5005#issuecomment-38102",
    "user": "https://github.com/robertwb"
}
```

Resolution: wontfix
