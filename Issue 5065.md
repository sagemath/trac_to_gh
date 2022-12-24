# Issue 5065: elliptic curve torsion subgroup doesn't know it's identity

archive/issues_005065.json:
```json
{
    "body": "Assignee: was\n\nThe torsion subgroup of an elliptic curve appears to be quite broken -- it barfs when trying to coerce in 0,\n\n\n```\nsage: E = EllipticCurve(1)\nsage: T = E.torsion_subgroup()\nsage: T(0)\n...\n...\nTypeError: Argument x (= 0) is of wrong type.\n```\n\n\nfurther, it returns a mysterious 1 when coercing in a 1\n\n\n```\nsage: a = T(1); a\n1\nsage: b = T.gens()[0]-T.gens()[0]; b\n(0 : 1 : 0)\nsage: a+b\nTypeError: unsupported operand parent(s) for '+': 'Abelian group of points on Elliptic Curve defined by y^2 + x*y + y = x^3 - 19*x + 26 over Rational Field' and 'Torsion Subgroup isomorphic to Multiplicative Abelian Group isomorphic to C6 x C2 associated to the Elliptic Curve defined by y^2 + x*y + y = x^3 - 19*x + 26 over Rational Field'\n```\n\n\nYet, it's all cool with the original curve.\n\n```\nsage: E(0)\n(0 : 1 : 0)\nsage: E(1)\n...\n...\nTypeError: v (=(1,)) must have 3 components\nsage: \n```\n\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5065\n\n",
    "created_at": "2009-01-23T08:29:47Z",
    "labels": [
        "number theory",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "elliptic curve torsion subgroup doesn't know it's identity",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5065",
    "user": "boothby"
}
```
Assignee: was

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

archive/issue_comments_038584.json:
```json
{
    "body": "Here is the reason.  the torsion subgroup class is derived from the Abelian group class, which in Sage is always a multiplicative group!  So it can coerce in 1 to give the identity 1, but not 0.\n\nI produced a lovely patch adding proper additive support to the AbelianGroup class months ago, motivated mainly by situations such as this, but nobody else was interested and it never got in.  (To be fair, the patch is on trac labelled \"not for review\" for some reason).\n\nOf course, for this specific group we could easily write a call() function to handle this, but the whole point of my Abeliangroup patch was that if you say that a group is additive on creation then that was all automatic.  Sigh.\n\nI see that this was reported 3 months ago.  Sorry, I never saw it until now!",
    "created_at": "2009-05-07T16:21:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5065",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5065#issuecomment-38584",
    "user": "cremona"
}
```

Here is the reason.  the torsion subgroup class is derived from the Abelian group class, which in Sage is always a multiplicative group!  So it can coerce in 1 to give the identity 1, but not 0.

I produced a lovely patch adding proper additive support to the AbelianGroup class months ago, motivated mainly by situations such as this, but nobody else was interested and it never got in.  (To be fair, the patch is on trac labelled "not for review" for some reason).

Of course, for this specific group we could easily write a call() function to handle this, but the whole point of my Abeliangroup patch was that if you say that a group is additive on creation then that was all automatic.  Sigh.

I see that this was reported 3 months ago.  Sorry, I never saw it until now!



---

archive/issue_comments_038585.json:
```json
{
    "body": "Changing assignee from was to davidloeffler.",
    "created_at": "2009-07-20T20:23:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5065",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5065#issuecomment-38585",
    "user": "davidloeffler"
}
```

Changing assignee from was to davidloeffler.



---

archive/issue_comments_038586.json:
```json
{
    "body": "Changing component from number theory to elliptic curves.",
    "created_at": "2009-07-20T20:23:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5065",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5065#issuecomment-38586",
    "user": "davidloeffler"
}
```

Changing component from number theory to elliptic curves.



---

archive/issue_comments_038587.json:
```json
{
    "body": "Remove assignee davidloeffler.",
    "created_at": "2009-10-09T09:12:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5065",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5065#issuecomment-38587",
    "user": "davidloeffler"
}
```

Remove assignee davidloeffler.



---

archive/issue_comments_038588.json:
```json
{
    "body": "In 4.5.3.alpha3 this works fine:\n\n```\nsage: E = EllipticCurve(j=1)\nsage: T = E.torsion_subgroup()\nsage: T(0)\n(0 : 1 : 0)\n```\n\nthanks to the new Abelian Groups support.  So this ticket can be closed as fixed.",
    "created_at": "2010-08-14T16:47:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5065",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5065#issuecomment-38588",
    "user": "cremona"
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

archive/issue_comments_038589.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-08-14T16:47:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5065",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5065#issuecomment-38589",
    "user": "cremona"
}
```

Resolution: fixed



---

archive/issue_comments_038590.json:
```json
{
    "body": "I'm setting the resolution to \"duplicate\" and changing the milestone accordingly.",
    "created_at": "2010-08-14T21:01:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5065",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5065#issuecomment-38590",
    "user": "mpatel"
}
```

I'm setting the resolution to "duplicate" and changing the milestone accordingly.



---

archive/issue_comments_038591.json:
```json
{
    "body": "Resolution changed from fixed to duplicate",
    "created_at": "2010-08-14T21:01:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5065",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5065#issuecomment-38591",
    "user": "mpatel"
}
```

Resolution changed from fixed to duplicate
