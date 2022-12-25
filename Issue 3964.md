# Issue 3964: projective space homs do not check arguments sufficiently

archive/issues_003964.json:
```json
{
    "body": "Assignee: @williamstein\n\nKeywords: projective space morphism\n\nAlex Ghitsa reported:\n\n```\nI am fairly certain the following two things are bugs, but I want to\ndouble-check that I'm not doing something stupid before submitting a ticket:\n\nsage: R.<x,y> = QQ[]\nsage: P1 = ProjectiveSpace(R)\nsage: H = P1.Hom(P1)\nsage: f = H([x-y, x*y])\nsage: f\n\nScheme endomorphism of Projective Space of dimension 1 over Rational Field\n Defn: Defined on coordinates by sending (x : y) to\n       (x - y : x*y)\n\n\nThis is nonsense: there is no morphism from P1 to P1 given by those\nequations, since the two polynomials x-y and x*y are not homogeneous of\nthe same degree.  I think Sage should throw a ValueError here.\n\nThe second example:\n\nsage: R.<x,y> = QQ[]\nsage: P1 = ProjectiveSpace(R)\nsage: H = P1.Hom(P1)\nsage: f = H([x^2, x*y])\nsage: f\n\nScheme endomorphism of Projective Space of dimension 1 over Rational Field\n Defn: Defined on coordinates by sending (x : y) to\n       (x^2 : x*y)\n\n\nThis is also bad: the two polynomials are now homogeneous of degree 2,\nbut they are not relatively prime (and so this is not a morphism from P1\nto P1, but rather a rational map since it is not defined at (0 : y)).  I\nthink Sage should also throw a ValueError here.\n\n(Or maybe I'm doing things wrong, in which case I'd love to find out how\nto make this work.)\n```\n\n\nto which John Cremona added:\n\n```\nYou are definitely right.  The problem lies (as far as I can see) in\nsage.schemes.generic in the __init__ funtion of class\nSchemeMorphism_on_points_projective_space.  (I only found this out by\ntring to construct a morphism from P^1 to P^1 using 3 polynomials,\nwhich did raise an error in this very function.)\n\nIt appears that the only check this function does is that the number\nof polys is correct.  It does not check that they are actually polys,\nor have the right number of variables, let alone that they are coprime\nand homogeneous of the same degree:\n\nsage: S.<u,v,w> = QQ[]\nsage: f = H([u,v])\nsage: f = H([u*v*w,u+v+w])\nsage: f = H([exp(u),exp(v)])\nsage: f\n\nScheme endomorphism of Projective Space of dimension 1 over Rational Field\n Defn: Defined on coordinates by sending (x : y) to\n       (e^u : e^v)\n\nwith H as in your example.\n\nThis definitely deserves a ticket, which I will create. now.\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3964\n\n",
    "created_at": "2008-08-27T09:06:09Z",
    "labels": [
        "component: algebraic geometry",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.1",
    "title": "projective space homs do not check arguments sufficiently",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3964",
    "user": "https://github.com/JohnCremona"
}
```
Assignee: @williamstein

Keywords: projective space morphism

Alex Ghitsa reported:

```
I am fairly certain the following two things are bugs, but I want to
double-check that I'm not doing something stupid before submitting a ticket:

sage: R.<x,y> = QQ[]
sage: P1 = ProjectiveSpace(R)
sage: H = P1.Hom(P1)
sage: f = H([x-y, x*y])
sage: f

Scheme endomorphism of Projective Space of dimension 1 over Rational Field
 Defn: Defined on coordinates by sending (x : y) to
       (x - y : x*y)


This is nonsense: there is no morphism from P1 to P1 given by those
equations, since the two polynomials x-y and x*y are not homogeneous of
the same degree.  I think Sage should throw a ValueError here.

The second example:

sage: R.<x,y> = QQ[]
sage: P1 = ProjectiveSpace(R)
sage: H = P1.Hom(P1)
sage: f = H([x^2, x*y])
sage: f

Scheme endomorphism of Projective Space of dimension 1 over Rational Field
 Defn: Defined on coordinates by sending (x : y) to
       (x^2 : x*y)


This is also bad: the two polynomials are now homogeneous of degree 2,
but they are not relatively prime (and so this is not a morphism from P1
to P1, but rather a rational map since it is not defined at (0 : y)).  I
think Sage should also throw a ValueError here.

(Or maybe I'm doing things wrong, in which case I'd love to find out how
to make this work.)
```


to which John Cremona added:

```
You are definitely right.  The problem lies (as far as I can see) in
sage.schemes.generic in the __init__ funtion of class
SchemeMorphism_on_points_projective_space.  (I only found this out by
tring to construct a morphism from P^1 to P^1 using 3 polynomials,
which did raise an error in this very function.)

It appears that the only check this function does is that the number
of polys is correct.  It does not check that they are actually polys,
or have the right number of variables, let alone that they are coprime
and homogeneous of the same degree:

sage: S.<u,v,w> = QQ[]
sage: f = H([u,v])
sage: f = H([u*v*w,u+v+w])
sage: f = H([exp(u),exp(v)])
sage: f

Scheme endomorphism of Projective Space of dimension 1 over Rational Field
 Defn: Defined on coordinates by sending (x : y) to
       (e^u : e^v)

with H as in your example.

This definitely deserves a ticket, which I will create. now.
```


Issue created by migration from https://trac.sagemath.org/ticket/3964





---

archive/issue_comments_028416.json:
```json
{
    "body": "I finally got around to fixing this.  The attached patch fixes the issues reported above (by John and myself), and adds some doctests.",
    "created_at": "2008-12-21T10:26:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3964",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3964#issuecomment-28416",
    "user": "https://github.com/aghitza"
}
```

I finally got around to fixing this.  The attached patch fixes the issues reported above (by John and myself), and adds some doctests.



---

archive/issue_comments_028417.json:
```json
{
    "body": "Attachment [trac_3964.patch](tarball://root/attachments/some-uuid/ticket3964/trac_3964.patch) by @aghitza created at 2008-12-21 10:27:59",
    "created_at": "2008-12-21T10:27:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3964",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3964#issuecomment-28417",
    "user": "https://github.com/aghitza"
}
```

Attachment [trac_3964.patch](tarball://root/attachments/some-uuid/ticket3964/trac_3964.patch) by @aghitza created at 2008-12-21 10:27:59



---

archive/issue_comments_028418.json:
```json
{
    "body": "This looks pretty good (I have not actually tested it yet though).  Alex, can we not check that the polys define a map to the correct space by checking that the defining polys of the target (if any) vanish when evaluated at the tuple of polys defining the map?  If that works it would be worthwhile adding it.",
    "created_at": "2008-12-21T13:25:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3964",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3964#issuecomment-28418",
    "user": "https://github.com/JohnCremona"
}
```

This looks pretty good (I have not actually tested it yet though).  Alex, can we not check that the polys define a map to the correct space by checking that the defining polys of the target (if any) vanish when evaluated at the tuple of polys defining the map?  If that works it would be worthwhile adding it.



---

archive/issue_comments_028419.json:
```json
{
    "body": "Good point.  I will implement this and submit a new patch.  I also just realized that I misread a docstring and implemented some things the wrong way around, so I will get that fixed.",
    "created_at": "2008-12-21T15:55:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3964",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3964#issuecomment-28419",
    "user": "https://github.com/aghitza"
}
```

Good point.  I will implement this and submit a new patch.  I also just realized that I misread a docstring and implemented some things the wrong way around, so I will get that fixed.



---

archive/issue_comments_028420.json:
```json
{
    "body": "Changing assignee from @williamstein to @aghitza.",
    "created_at": "2009-03-29T08:18:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3964",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3964#issuecomment-28420",
    "user": "https://github.com/aghitza"
}
```

Changing assignee from @williamstein to @aghitza.



---

archive/issue_comments_028421.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-03-29T08:18:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3964",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3964#issuecomment-28421",
    "user": "https://github.com/aghitza"
}
```

Changing status from new to assigned.



---

archive/issue_comments_028422.json:
```json
{
    "body": "apply this (not the previous one).",
    "created_at": "2010-01-17T08:59:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3964",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3964#issuecomment-28422",
    "user": "https://github.com/williamstein"
}
```

apply this (not the previous one).



---

archive/issue_comments_028423.json:
```json
{
    "body": "Attachment [trac_3964-rebased_and_extended.patch](tarball://root/attachments/some-uuid/ticket3964/trac_3964-rebased_and_extended.patch) by @williamstein created at 2010-01-17 08:59:26",
    "created_at": "2010-01-17T08:59:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3964",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3964#issuecomment-28423",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac_3964-rebased_and_extended.patch](tarball://root/attachments/some-uuid/ticket3964/trac_3964-rebased_and_extended.patch) by @williamstein created at 2010-01-17 08:59:26



---

archive/issue_comments_028424.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-01-17T08:59:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3964",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3964#issuecomment-28424",
    "user": "https://github.com/williamstein"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_028425.json:
```json
{
    "body": "Hi,\n\nI took Alex's patch, added a bunch of doctests, changed it some, and read it.  I think this should go in if it looks ok to John or Alex.  It's a clear improvement, though arbitrarily much works remains!",
    "created_at": "2010-01-17T09:00:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3964",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3964#issuecomment-28425",
    "user": "https://github.com/williamstein"
}
```

Hi,

I took Alex's patch, added a bunch of doctests, changed it some, and read it.  I think this should go in if it looks ok to John or Alex.  It's a clear improvement, though arbitrarily much works remains!



---

archive/issue_comments_028426.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-17T11:16:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3964",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3964#issuecomment-28426",
    "user": "https://github.com/JohnCremona"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_028427.json:
```json
{
    "body": "Patch applies fine to 4.3.1.rc0 and tests pass.  So I'll give this a positive review despite the fact that (as was said) there's a lot more needing to be done, for example:\n\n\n```\nsage: S.<u,v,w> = QQ[]\nsage: C = Curve(u^2+v^2-w^2); C\nProjective Curve over Rational Field defined by u^2 + v^2 - w^2\nsage: H = C.Hom(C); H\nSet of points of Projective Curve over Rational Field defined by u^2 + v^2 - w^2 defined over Quotient of Multivariate Polynomial Ring in u, v, w over Rational Field by the ideal (u^2 + v^2 - w^2)\nsage: \nsage: H([u,v,w])\n---------------------------------------------------------------------------\nAttributeError                            Traceback (most recent call last)\n...\nAttributeError: 'QuotientRingElement' object has no attribute 'degree'\n```\n",
    "created_at": "2010-01-17T11:16:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3964",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3964#issuecomment-28427",
    "user": "https://github.com/JohnCremona"
}
```

Patch applies fine to 4.3.1.rc0 and tests pass.  So I'll give this a positive review despite the fact that (as was said) there's a lot more needing to be done, for example:


```
sage: S.<u,v,w> = QQ[]
sage: C = Curve(u^2+v^2-w^2); C
Projective Curve over Rational Field defined by u^2 + v^2 - w^2
sage: H = C.Hom(C); H
Set of points of Projective Curve over Rational Field defined by u^2 + v^2 - w^2 defined over Quotient of Multivariate Polynomial Ring in u, v, w over Rational Field by the ideal (u^2 + v^2 - w^2)
sage: 
sage: H([u,v,w])
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
...
AttributeError: 'QuotientRingElement' object has no attribute 'degree'
```




---

archive/issue_events_004192.json:
```json
{
    "actor": "@rlmill",
    "created_at": "2010-01-18T23:44:40Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3964",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3964#event-4192"
}
```



---

archive/issue_comments_028428.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-18T23:44:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3964",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3964#issuecomment-28428",
    "user": "https://github.com/rlmill"
}
```

Resolution: fixed



---

archive/issue_comments_028429.json:
```json
{
    "body": "See #10297 for the next step in this direction.",
    "created_at": "2010-11-21T16:50:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3964",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3964#issuecomment-28429",
    "user": "https://github.com/JohnCremona"
}
```

See #10297 for the next step in this direction.
