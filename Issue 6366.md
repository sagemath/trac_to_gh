# Issue 6366: lift method on elements of residue class field is broken / not implemented as it should be

archive/issues_006366.json:
```json
{
    "body": "Assignee: was\n\n\n```\nsage: K.<a> = NumberField(x^2 + 3)\nsage: P = K.factor(5)[0][0]; P\nFractional ideal (5)\nsage: F = P.residue_field()\nsage: z = F.gen() + 2; z\nabar + 2\nsage: F.lift(z)\n6*a + 2\nsage: z.lift()\nTraceback (most recent call last):\n...\nAttributeError: 'sage.rings.finite_field_givaro.FiniteField_givaroE' object has no attribute 'lift'\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6366\n\n",
    "created_at": "2009-06-20T15:14:45Z",
    "labels": [
        "number theory",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "lift method on elements of residue class field is broken / not implemented as it should be",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6366",
    "user": "was"
}
```
Assignee: was


```
sage: K.<a> = NumberField(x^2 + 3)
sage: P = K.factor(5)[0][0]; P
Fractional ideal (5)
sage: F = P.residue_field()
sage: z = F.gen() + 2; z
abar + 2
sage: F.lift(z)
6*a + 2
sage: z.lift()
Traceback (most recent call last):
...
AttributeError: 'sage.rings.finite_field_givaro.FiniteField_givaroE' object has no attribute 'lift'
```


Issue created by migration from https://trac.sagemath.org/ticket/6366





---

archive/issue_comments_050927.json:
```json
{
    "body": "Changing component from number theory to number fields.",
    "created_at": "2009-07-21T08:20:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6366",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6366#issuecomment-50927",
    "user": "davidloeffler"
}
```

Changing component from number theory to number fields.



---

archive/issue_comments_050928.json:
```json
{
    "body": "Changing assignee from was to davidloeffler.",
    "created_at": "2009-07-21T08:20:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6366",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6366#issuecomment-50928",
    "user": "davidloeffler"
}
```

Changing assignee from was to davidloeffler.
