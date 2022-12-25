# Issue 6657: EllipticCurve(..., j=...) shouldn't ignore field argument if given.

archive/issues_006657.json:
```json
{
    "body": "Assignee: @williamstein\n\n\n```\nI found the following to be rather unexpected:\n\nEllipticCurve(GF(144169),j=1728)\nElliptic Curve defined by y^2 = x^3 - x over Rational Field\n\n - Victor Miller\n\n[I understand that 1728 is considered an Integer, yet the first\nargument seems to be ignored]\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6657\n\n",
    "created_at": "2009-07-29T23:06:58Z",
    "labels": [
        "component: number theory",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.1",
    "title": "EllipticCurve(..., j=...) shouldn't ignore field argument if given.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6657",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein


```
I found the following to be rather unexpected:

EllipticCurve(GF(144169),j=1728)
Elliptic Curve defined by y^2 = x^3 - x over Rational Field

 - Victor Miller

[I understand that 1728 is considered an Integer, yet the first
argument seems to be ignored]
```


Issue created by migration from https://trac.sagemath.org/ticket/6657





---

archive/issue_comments_054545.json:
```json
{
    "body": "Easy to fix:  where EllipticCurve calls `EllipticCurve_from_j(j)` it should in fact coerce j into the parent of x (if x is not none).",
    "created_at": "2009-08-01T18:17:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6657",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6657#issuecomment-54545",
    "user": "https://github.com/JohnCremona"
}
```

Easy to fix:  where EllipticCurve calls `EllipticCurve_from_j(j)` it should in fact coerce j into the parent of x (if x is not none).



---

archive/issue_comments_054546.json:
```json
{
    "body": "This issue only appears in the deprecated function `EllipticCurve(..,j=..)`. The right function to call here is `EllipticCurve_from_j(GF(144169)(1728))`.\n\nMy proposal for a change is to finally eliminate the deprecated function.",
    "created_at": "2009-10-20T22:05:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6657",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6657#issuecomment-54546",
    "user": "https://github.com/categorie"
}
```

This issue only appears in the deprecated function `EllipticCurve(..,j=..)`. The right function to call here is `EllipticCurve_from_j(GF(144169)(1728))`.

My proposal for a change is to finally eliminate the deprecated function.



---

archive/issue_comments_054547.json:
```json
{
    "body": "Changing component from number theory to elliptic curves.",
    "created_at": "2010-01-12T14:49:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6657",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6657#issuecomment-54547",
    "user": "https://github.com/categorie"
}
```

Changing component from number theory to elliptic curves.



---

archive/issue_comments_054548.json:
```json
{
    "body": "Changing assignee from @williamstein to @JohnCremona.",
    "created_at": "2010-01-12T14:49:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6657",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6657#issuecomment-54548",
    "user": "https://github.com/categorie"
}
```

Changing assignee from @williamstein to @JohnCremona.



---

archive/issue_comments_054549.json:
```json
{
    "body": "Chris,\n\nYou are not quite right.  What is deprecated is EllipticCurve(j0), not EllipticCurve(j=j0):\n\n```\nsage: EllipticCurve(GF(101)(1728))\n/home/john/sage-4.3.1.alpha1/local/bin/sage-ipython:1: DeprecationWarning: 'EllipticCurve(j)' is deprecated; use 'EllipticCurve_from_j(j)' or 'EllipticCurve(j=j)' instead.\n  #!/usr/bin/env python\nElliptic Curve defined by y^2 = x^3 + x over Finite Field of size 101\nsage: EllipticCurve(j=GF(101)(1728))\nElliptic Curve defined by y^2 = x^3 + x over Finite Field of size 101\n```\n\nNow I cannot remember when that deprecation was put in, hence when it should be removed.\n\nAnyway, Victor's point is a valid one, and I'll put up a patch!",
    "created_at": "2010-01-12T20:19:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6657",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6657#issuecomment-54549",
    "user": "https://github.com/JohnCremona"
}
```

Chris,

You are not quite right.  What is deprecated is EllipticCurve(j0), not EllipticCurve(j=j0):

```
sage: EllipticCurve(GF(101)(1728))
/home/john/sage-4.3.1.alpha1/local/bin/sage-ipython:1: DeprecationWarning: 'EllipticCurve(j)' is deprecated; use 'EllipticCurve_from_j(j)' or 'EllipticCurve(j=j)' instead.
  #!/usr/bin/env python
Elliptic Curve defined by y^2 = x^3 + x over Finite Field of size 101
sage: EllipticCurve(j=GF(101)(1728))
Elliptic Curve defined by y^2 = x^3 + x over Finite Field of size 101
```

Now I cannot remember when that deprecation was put in, hence when it should be removed.

Anyway, Victor's point is a valid one, and I'll put up a patch!



---

archive/issue_comments_054550.json:
```json
{
    "body": "Applies to 4.3.1.alpha1",
    "created_at": "2010-01-12T20:52:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6657",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6657#issuecomment-54550",
    "user": "https://github.com/JohnCremona"
}
```

Applies to 4.3.1.alpha1



---

archive/issue_comments_054551.json:
```json
{
    "body": "Attachment [trac_6657-elliptic_curveconstructor.patch](tarball://root/attachments/some-uuid/ticket6657/trac_6657-elliptic_curveconstructor.patch) by @JohnCremona created at 2010-01-12 20:53:15\n\nThe attached patch sorts this out, with appropriate tests.",
    "created_at": "2010-01-12T20:53:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6657",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6657#issuecomment-54551",
    "user": "https://github.com/JohnCremona"
}
```

Attachment [trac_6657-elliptic_curveconstructor.patch](tarball://root/attachments/some-uuid/ticket6657/trac_6657-elliptic_curveconstructor.patch) by @JohnCremona created at 2010-01-12 20:53:15

The attached patch sorts this out, with appropriate tests.



---

archive/issue_comments_054552.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-12T20:53:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6657",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6657#issuecomment-54552",
    "user": "https://github.com/JohnCremona"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_054553.json:
```json
{
    "body": "Yes, that is fine. Thanks John.\n\nChris.",
    "created_at": "2010-01-15T16:43:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6657",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6657#issuecomment-54553",
    "user": "https://github.com/categorie"
}
```

Yes, that is fine. Thanks John.

Chris.



---

archive/issue_comments_054554.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-15T16:43:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6657",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6657#issuecomment-54554",
    "user": "https://github.com/categorie"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_015714.json:
```json
{
    "actor": "https://github.com/rlmill",
    "created_at": "2010-01-19T00:08:13Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6657",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6657#event-15714"
}
```



---

archive/issue_comments_054555.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-19T00:08:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6657",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6657#issuecomment-54555",
    "user": "https://github.com/rlmill"
}
```

Resolution: fixed
