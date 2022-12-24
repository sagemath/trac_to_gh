# Issue 7954: Defining affine curves in 3D space

archive/issues_007954.json:
```json
{
    "body": "Assignee: @aghitza\n\nCC:  @kwankyu\n\nReported by Ronald van Luijk:\n\nbecause the Curve constructor automatically interprets a homogeneous polynomial in 3 variables as a projective curve, the following doesn't work:\n\n\n```\nA.<x,y,z>=AffineSpace(QQ,3)\nC=Curve([x-y,x-z])\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7954\n\n",
    "created_at": "2010-01-16T18:15:19Z",
    "labels": [
        "algebraic geometry",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Defining affine curves in 3D space",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7954",
    "user": "@wjp"
}
```
Assignee: @aghitza

CC:  @kwankyu

Reported by Ronald van Luijk:

because the Curve constructor automatically interprets a homogeneous polynomial in 3 variables as a projective curve, the following doesn't work:


```
A.<x,y,z>=AffineSpace(QQ,3)
C=Curve([x-y,x-z])
```


Issue created by migration from https://trac.sagemath.org/ticket/7954





---

archive/issue_comments_069404.json:
```json
{
    "body": "Attachment [7954_curve_constructor.patch](tarball://root/attachments/some-uuid/ticket7954/7954_curve_constructor.patch) by @wjp created at 2010-01-17 03:52:22",
    "created_at": "2010-01-17T03:52:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7954",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7954#issuecomment-69404",
    "user": "@wjp"
}
```

Attachment [7954_curve_constructor.patch](tarball://root/attachments/some-uuid/ticket7954/7954_curve_constructor.patch) by @wjp created at 2010-01-17 03:52:22



---

archive/issue_comments_069405.json:
```json
{
    "body": "The attached patch adds an optional `space='affine'/'projective'` keyword argument to the Curve constructor.",
    "created_at": "2010-01-17T03:53:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7954",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7954#issuecomment-69405",
    "user": "@wjp"
}
```

The attached patch adds an optional `space='affine'/'projective'` keyword argument to the Curve constructor.



---

archive/issue_comments_069406.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-17T03:53:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7954",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7954#issuecomment-69406",
    "user": "@wjp"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_069407.json:
```json
{
    "body": "Attachment [trac_7954-part2.patch](tarball://root/attachments/some-uuid/ticket7954/trac_7954-part2.patch) by @williamstein created at 2010-01-17 09:38:23\n\nthe previous patch was part 1.  apply this after that one.",
    "created_at": "2010-01-17T09:38:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7954",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7954#issuecomment-69407",
    "user": "@williamstein"
}
```

Attachment [trac_7954-part2.patch](tarball://root/attachments/some-uuid/ticket7954/trac_7954-part2.patch) by @williamstein created at 2010-01-17 09:38:23

the previous patch was part 1.  apply this after that one.



---

archive/issue_comments_069408.json:
```json
{
    "body": "Hi,\n\nI made some important improvements to the patch while refereeing it.  However, it is clear after looking at this code for a bit that there is a *MAJOR* design flaw (which Willem pointed out to me in person).  The flaw is this in plane_curve/affine_curve.py:\n\n```\nclass AffineSpaceCurve_generic(Curve_generic, AlgebraicScheme_subscheme_affine):\n    def _repr_type(self):\n        return \"Affine Space\"\n```\n\nHowever, Curve_generic is very much a *plane* curve:\n\n```\nclass Curve_generic(AlgebraicScheme_subscheme):\n...\n    def defining_polynomial(self):\n        return self.defining_polynomials()[0]\n```\n\n\nThus the *isa* relationship that *must* be satisfied by derivation of objects is broken.\n\nThe space curve code must be completely moved out of this directory to the appropriate place.",
    "created_at": "2010-01-17T09:41:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7954",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7954#issuecomment-69408",
    "user": "@williamstein"
}
```

Hi,

I made some important improvements to the patch while refereeing it.  However, it is clear after looking at this code for a bit that there is a *MAJOR* design flaw (which Willem pointed out to me in person).  The flaw is this in plane_curve/affine_curve.py:

```
class AffineSpaceCurve_generic(Curve_generic, AlgebraicScheme_subscheme_affine):
    def _repr_type(self):
        return "Affine Space"
```

However, Curve_generic is very much a *plane* curve:

```
class Curve_generic(AlgebraicScheme_subscheme):
...
    def defining_polynomial(self):
        return self.defining_polynomials()[0]
```


Thus the *isa* relationship that *must* be satisfied by derivation of objects is broken.

The space curve code must be completely moved out of this directory to the appropriate place.



---

archive/issue_comments_069409.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-01-17T09:41:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7954",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7954#issuecomment-69409",
    "user": "@williamstein"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_069410.json:
```json
{
    "body": "I'm going to wait to talk to willem about this instead of just trying to do it myself.",
    "created_at": "2010-01-17T09:42:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7954",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7954#issuecomment-69410",
    "user": "@williamstein"
}
```

I'm going to wait to talk to willem about this instead of just trying to do it myself.



---

archive/issue_comments_069411.json:
```json
{
    "body": "The issue seems to have been solved now by adding `A`mbient space argument to the `Curve` constructor.\n\n\n```\nsage: A.<x,y,z>=AffineSpace(QQ,3)\nsage: C = Curve([x-y,y-z],A)\nsage: C\nAffine Curve over Rational Field defined by x - y, y - z\n```\n",
    "created_at": "2020-07-06T09:54:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7954",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7954#issuecomment-69411",
    "user": "@kwankyu"
}
```

The issue seems to have been solved now by adding `A`mbient space argument to the `Curve` constructor.


```
sage: A.<x,y,z>=AffineSpace(QQ,3)
sage: C = Curve([x-y,y-z],A)
sage: C
Affine Curve over Rational Field defined by x - y, y - z
```




---

archive/issue_comments_069412.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2020-07-06T09:57:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7954",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7954#issuecomment-69412",
    "user": "@kwankyu"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_069413.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2020-07-06T12:11:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7954",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7954#issuecomment-69413",
    "user": "@mkoeppe"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_069414.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2020-08-22T07:20:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7954",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7954#issuecomment-69414",
    "user": "@slel"
}
```

Resolution: fixed
