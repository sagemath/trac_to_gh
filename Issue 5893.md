# Issue 5893: Norm Form for Number Fields and Orders

archive/issues_005893.json:
```json
{
    "body": "Assignee: @roed314\n\nOften if one is doing computations with number fields and orders by hand, it's useful to have the norm form with respect to a given basis.  For example:\n\n\n```\nsage: K.<sqrt2> = NumberField(x^2 - 2); T.<a, b> = QQ[]\nsage: K.power_basis()\n[1, sqrt2]\nsage: K.norm_form([a, b])\na^2 - 2*b^2\nsage: K.norm_form([1, b])\n1 - 2*b^2\nsage: OK = NumberField(x^2-5, names='sqrt5').maximal_order(); T.<a, b> = ZZ[]\nsage: OK.basis()\n[1/2*sqrt5 + 1/2, sqrt5]\nsage: OK.norm_form([a, b])\n-a^2 - 5*a*b - 5*b^2\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5893\n\n",
    "created_at": "2009-04-25T09:43:11Z",
    "labels": [
        "number theory",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-feature",
    "title": "Norm Form for Number Fields and Orders",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5893",
    "user": "@roed314"
}
```
Assignee: @roed314

Often if one is doing computations with number fields and orders by hand, it's useful to have the norm form with respect to a given basis.  For example:


```
sage: K.<sqrt2> = NumberField(x^2 - 2); T.<a, b> = QQ[]
sage: K.power_basis()
[1, sqrt2]
sage: K.norm_form([a, b])
a^2 - 2*b^2
sage: K.norm_form([1, b])
1 - 2*b^2
sage: OK = NumberField(x^2-5, names='sqrt5').maximal_order(); T.<a, b> = ZZ[]
sage: OK.basis()
[1/2*sqrt5 + 1/2, sqrt5]
sage: OK.norm_form([a, b])
-a^2 - 5*a*b - 5*b^2
```



Issue created by migration from https://trac.sagemath.org/ticket/5893





---

archive/issue_comments_046604.json:
```json
{
    "body": "Changing component from number theory to number fields.",
    "created_at": "2009-07-21T08:19:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5893",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5893#issuecomment-46604",
    "user": "@loefflerd"
}
```

Changing component from number theory to number fields.
