# Issue 5065: elliptic curve torsion subgroup doesn't know it's identity

archive/issues_005065.json:
```json
{
    "body": "Assignee: @williamstein\n\nThe torsion subgroup of an elliptic curve appears to be quite broken -- it barfs when trying to coerce in 0,\n\n```\nsage: E = EllipticCurve(1)\nsage: T = E.torsion_subgroup()\nsage: T(0)\n...\n...\nTypeError: Argument x (= 0) is of wrong type.\n```\n\nfurther, it returns a mysterious 1 when coercing in a 1\n\n```\nsage: a = T(1); a\n1\nsage: b = T.gens()[0]-T.gens()[0]; b\n(0 : 1 : 0)\nsage: a+b\nTypeError: unsupported operand parent(s) for '+': 'Abelian group of points on Elliptic Curve defined by y^2 + x*y + y = x^3 - 19*x + 26 over Rational Field' and 'Torsion Subgroup isomorphic to Multiplicative Abelian Group isomorphic to C6 x C2 associated to the Elliptic Curve defined by y^2 + x*y + y = x^3 - 19*x + 26 over Rational Field'\n```\n\nYet, it's all cool with the original curve.\n\n```\nsage: E(0)\n(0 : 1 : 0)\nsage: E(1)\n...\n...\nTypeError: v (=(1,)) must have 3 components\nsage: \n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5065\n\n",
    "created_at": "2009-01-23T08:29:47Z",
    "labels": [
        "component: number theory",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "elliptic curve torsion subgroup doesn't know it's identity",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5065",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```
Assignee: @williamstein

The torsion subgroup of an elliptic curve appears to be quite broken -- it barfs when trying to coerce in 0,

```
sage: E = EllipticCurve(1)
sage: T = E.torsion_subgroup()
sage: T(0)
...
...
TypeError: Argument x (= 0) is of wrong type.
```

further, it returns a mysterious 1 when coercing in a 1

```
sage: a = T(1); a
1
sage: b = T.gens()[0]-T.gens()[0]; b
(0 : 1 : 0)
sage: a+b
TypeError: unsupported operand parent(s) for '+': 'Abelian group of points on Elliptic Curve defined by y^2 + x*y + y = x^3 - 19*x + 26 over Rational Field' and 'Torsion Subgroup isomorphic to Multiplicative Abelian Group isomorphic to C6 x C2 associated to the Elliptic Curve defined by y^2 + x*y + y = x^3 - 19*x + 26 over Rational Field'
```

Yet, it's all cool with the original curve.

```
sage: E(0)
(0 : 1 : 0)
sage: E(1)
...
...
TypeError: v (=(1,)) must have 3 components
sage: 
```



Issue created by migration from https://trac.sagemath.org/ticket/5065





---

archive/issue_events_011679.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-04-23T08:04:24Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5065",
    "milestone": "sage-4.0",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5065#event-11679"
}
```



---

archive/issue_comments_038511.json:
```json
{
    "body": "Here is the reason.  the torsion subgroup class is derived from the Abelian group class, which in Sage is always a multiplicative group!  So it can coerce in 1 to give the identity 1, but not 0.\n\nI produced a lovely patch adding proper additive support to the AbelianGroup class months ago, motivated mainly by situations such as this, but nobody else was interested and it never got in.  (To be fair, the patch is on trac labelled \"not for review\" for some reason).\n\nOf course, for this specific group we could easily write a call() function to handle this, but the whole point of my Abeliangroup patch was that if you say that a group is additive on creation then that was all automatic.  Sigh.\n\nI see that this was reported 3 months ago.  Sorry, I never saw it until now!",
    "created_at": "2009-05-07T16:21:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5065",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5065#issuecomment-38511",
    "user": "https://github.com/JohnCremona"
}
```

Here is the reason.  the torsion subgroup class is derived from the Abelian group class, which in Sage is always a multiplicative group!  So it can coerce in 1 to give the identity 1, but not 0.

I produced a lovely patch adding proper additive support to the AbelianGroup class months ago, motivated mainly by situations such as this, but nobody else was interested and it never got in.  (To be fair, the patch is on trac labelled "not for review" for some reason).

Of course, for this specific group we could easily write a call() function to handle this, but the whole point of my Abeliangroup patch was that if you say that a group is additive on creation then that was all automatic.  Sigh.

I see that this was reported 3 months ago.  Sorry, I never saw it until now!



---

archive/issue_comments_038512.json:
```json
{
    "body": "Changing assignee from @williamstein to @loefflerd.",
    "created_at": "2009-07-20T20:23:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5065",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5065#issuecomment-38512",
    "user": "https://github.com/loefflerd"
}
```

Changing assignee from @williamstein to @loefflerd.



---

archive/issue_comments_038513.json:
```json
{
    "body": "Changing component from number theory to elliptic curves.",
    "created_at": "2009-07-20T20:23:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5065",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5065#issuecomment-38513",
    "user": "https://github.com/loefflerd"
}
```

Changing component from number theory to elliptic curves.



---

archive/issue_comments_038514.json:
```json
{
    "body": "Remove assignee @loefflerd.",
    "created_at": "2009-10-09T09:12:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5065",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5065#issuecomment-38514",
    "user": "https://github.com/loefflerd"
}
```

Remove assignee @loefflerd.



---

archive/issue_events_011680.json:
```json
{
    "actor": "https://github.com/JohnCremona",
    "created_at": "2010-08-14T16:47:11Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5065",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5065#event-11680"
}
```



---

archive/issue_comments_038515.json:
```json
{
    "body": "In 4.5.3.alpha3 this works fine:\n\n```\nsage: E = EllipticCurve(j=1)\nsage: T = E.torsion_subgroup()\nsage: T(0)\n(0 : 1 : 0)\n```\nthanks to the new Abelian Groups support.  So this ticket can be closed as fixed.",
    "created_at": "2010-08-14T16:47:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5065",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5065#issuecomment-38515",
    "user": "https://github.com/JohnCremona"
}
```

In 4.5.3.alpha3 this works fine:

```
sage: E = EllipticCurve(j=1)
sage: T = E.torsion_subgroup()
sage: T(0)
(0 : 1 : 0)
```
thanks to the new Abelian Groups support.  So this ticket can be closed as fixed.



---

archive/issue_comments_038516.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-08-14T16:47:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5065",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5065#issuecomment-38516",
    "user": "https://github.com/JohnCremona"
}
```

Resolution: fixed



---

archive/issue_events_011681.json:
```json
{
    "actor": "https://github.com/qed777",
    "created_at": "2010-08-14T21:01:56Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5065",
    "milestone": "sage-4.0",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5065#event-11681"
}
```



---

archive/issue_events_011682.json:
```json
{
    "actor": "https://github.com/qed777",
    "created_at": "2010-08-14T21:01:56Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5065",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5065#event-11682"
}
```



---

archive/issue_comments_038517.json:
```json
{
    "body": "I'm setting the resolution to \"duplicate\" and changing the milestone accordingly.",
    "created_at": "2010-08-14T21:01:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5065",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5065#issuecomment-38517",
    "user": "https://github.com/qed777"
}
```

I'm setting the resolution to "duplicate" and changing the milestone accordingly.



---

archive/issue_comments_038518.json:
```json
{
    "body": "Resolution changed from fixed to duplicate",
    "created_at": "2010-08-14T21:01:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5065",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5065#issuecomment-38518",
    "user": "https://github.com/qed777"
}
```

Resolution changed from fixed to duplicate
