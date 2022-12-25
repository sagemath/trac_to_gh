# Issue 7958: Conversion of rationals into the fraction field of integer polynomials

archive/issues_007958.json:
```json
{
    "body": "Assignee: @aghitza\n\n```\nsage: F = Frac(PolynomialRing(ZZ, 't'))\nsage: F(1/2)\n...\nTypeError: no conversion of this rational to integer\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/7958\n\n",
    "created_at": "2010-01-16T19:28:41Z",
    "labels": [
        "component: algebra",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.2",
    "title": "Conversion of rationals into the fraction field of integer polynomials",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7958",
    "user": "https://trac.sagemath.org/admin/accounts/users/spancratz"
}
```
Assignee: @aghitza

```
sage: F = Frac(PolynomialRing(ZZ, 't'))
sage: F(1/2)
...
TypeError: no conversion of this rational to integer
```

Issue created by migration from https://trac.sagemath.org/ticket/7958





---

archive/issue_comments_069320.json:
```json
{
    "body": "Changing assignee from @aghitza to @robertwb.",
    "created_at": "2010-01-16T19:29:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7958",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7958#issuecomment-69320",
    "user": "https://trac.sagemath.org/admin/accounts/users/spancratz"
}
```

Changing assignee from @aghitza to @robertwb.



---

archive/issue_comments_069321.json:
```json
{
    "body": "Changing component from algebra to coercion.",
    "created_at": "2010-01-16T19:29:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7958",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7958#issuecomment-69321",
    "user": "https://trac.sagemath.org/admin/accounts/users/spancratz"
}
```

Changing component from algebra to coercion.



---

archive/issue_comments_069322.json:
```json
{
    "body": "Attachment [trac7958.patch](tarball://root/attachments/some-uuid/ticket7958/trac7958.patch) by spancratz created at 2010-01-16 21:00:19",
    "created_at": "2010-01-16T21:00:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7958",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7958#issuecomment-69322",
    "user": "https://trac.sagemath.org/admin/accounts/users/spancratz"
}
```

Attachment [trac7958.patch](tarball://root/attachments/some-uuid/ticket7958/trac7958.patch) by spancratz created at 2010-01-16 21:00:19



---

archive/issue_comments_069323.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-16T21:30:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7958",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7958#issuecomment-69323",
    "user": "https://trac.sagemath.org/admin/accounts/users/spancratz"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_069324.json:
```json
{
    "body": "Your fix does work great for QQ, but this is actually a more general issue than just QQ:\n\n```\nsage: _.<x> = ZZ[]\nsage: K.<a> = NumberField(x^2-2)\nsage: R.<b> = K.ring_of_integers()\nsage: S.<y> = R[]\nsage: F = FractionField(S)\nsage: F(1)/F(a)\n1/a\nsage: F(1/a)\n*boom*\n```\n\nAnd a minor issue: I think the comment about QQ should be a code comment rather than in the doctest, since it might now confuse users (who might think they need to handle QQ specially themselves).",
    "created_at": "2010-01-17T17:50:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7958",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7958#issuecomment-69324",
    "user": "https://github.com/wjp"
}
```

Your fix does work great for QQ, but this is actually a more general issue than just QQ:

```
sage: _.<x> = ZZ[]
sage: K.<a> = NumberField(x^2-2)
sage: R.<b> = K.ring_of_integers()
sage: S.<y> = R[]
sage: F = FractionField(S)
sage: F(1)/F(a)
1/a
sage: F(1/a)
*boom*
```

And a minor issue: I think the comment about QQ should be a code comment rather than in the doctest, since it might now confuse users (who might think they need to handle QQ specially themselves).



---

archive/issue_comments_069325.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-01-17T17:50:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7958",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7958#issuecomment-69325",
    "user": "https://github.com/wjp"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_069326.json:
```json
{
    "body": "Attachment [trac7958_c.patch](tarball://root/attachments/some-uuid/ticket7958/trac7958_c.patch) by spancratz created at 2010-01-17 21:29:16",
    "created_at": "2010-01-17T21:29:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7958",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7958#issuecomment-69326",
    "user": "https://trac.sagemath.org/admin/accounts/users/spancratz"
}
```

Attachment [trac7958_c.patch](tarball://root/attachments/some-uuid/ticket7958/trac7958_c.patch) by spancratz created at 2010-01-17 21:29:16



---

archive/issue_comments_069327.json:
```json
{
    "body": "To see that this issue is now resolved (for rationals and number fields), consider\n\n```\nsage: _.<x> = ZZ[]\nsage: K.<a> = NumberField(x^5-3*x^4+2424*x^3+2*x-232)\nsage: R.<b> = K.ring_of_integers()\nsage: S.<y> = R[]\nsage: F = Frac(S)\nsage: F(1/a)\na^4 - 3*a^3 + 2424*a^2 + 2/232\nsage: F(1/a).numerator()\na^4 - 3*a^3 + 2424*a^2 + 2\nsage: F(1/a).denominator()\n232\n```\n\nBut the last three lines highlight a bug in the printing routines.",
    "created_at": "2010-01-17T21:45:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7958",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7958#issuecomment-69327",
    "user": "https://trac.sagemath.org/admin/accounts/users/spancratz"
}
```

To see that this issue is now resolved (for rationals and number fields), consider

```
sage: _.<x> = ZZ[]
sage: K.<a> = NumberField(x^5-3*x^4+2424*x^3+2*x-232)
sage: R.<b> = K.ring_of_integers()
sage: S.<y> = R[]
sage: F = Frac(S)
sage: F(1/a)
a^4 - 3*a^3 + 2424*a^2 + 2/232
sage: F(1/a).numerator()
a^4 - 3*a^3 + 2424*a^2 + 2
sage: F(1/a).denominator()
232
```

But the last three lines highlight a bug in the printing routines.



---

archive/issue_comments_069328.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-01-17T21:45:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7958",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7958#issuecomment-69328",
    "user": "https://trac.sagemath.org/admin/accounts/users/spancratz"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_069329.json:
```json
{
    "body": "Attachment [trac7958_d.patch](tarball://root/attachments/some-uuid/ticket7958/trac7958_d.patch) by @mwhansen created at 2010-01-20 04:16:42\n\n```\n\nsage: _.<x> = ZZ[]\nsage: K.<a> = NumberField(x^5-3*x^4+2424*x^3+2*x-232)\nsage: R.<b> = K.ring_of_integers()\nsage: S.<y> = R[]\nsage: F = Frac(S)\nsage: F(1/a)\na^4 - 3*a^3 + 2424*a^2 + 2/232\nsage: F(1/a).numerator()\na^4 - 3*a^3 + 2424*a^2 + 2\nsage: F(1/a).denominator()\n232\n\n```",
    "created_at": "2010-01-20T04:16:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7958",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7958#issuecomment-69329",
    "user": "https://github.com/mwhansen"
}
```

Attachment [trac7958_d.patch](tarball://root/attachments/some-uuid/ticket7958/trac7958_d.patch) by @mwhansen created at 2010-01-20 04:16:42

```

sage: _.<x> = ZZ[]
sage: K.<a> = NumberField(x^5-3*x^4+2424*x^3+2*x-232)
sage: R.<b> = K.ring_of_integers()
sage: S.<y> = R[]
sage: F = Frac(S)
sage: F(1/a)
a^4 - 3*a^3 + 2424*a^2 + 2/232
sage: F(1/a).numerator()
a^4 - 3*a^3 + 2424*a^2 + 2
sage: F(1/a).denominator()
232

```



---

archive/issue_comments_069330.json:
```json
{
    "body": "Combined version of the above patches.",
    "created_at": "2010-01-20T04:28:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7958",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7958#issuecomment-69330",
    "user": "https://github.com/mwhansen"
}
```

Combined version of the above patches.



---

archive/issue_comments_069331.json:
```json
{
    "body": "Attachment [trac_7958-atomic.patch](tarball://root/attachments/some-uuid/ticket7958/trac_7958-atomic.patch) by @mwhansen created at 2010-01-20 05:50:41",
    "created_at": "2010-01-20T05:50:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7958",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7958#issuecomment-69331",
    "user": "https://github.com/mwhansen"
}
```

Attachment [trac_7958-atomic.patch](tarball://root/attachments/some-uuid/ticket7958/trac_7958-atomic.patch) by @mwhansen created at 2010-01-20 05:50:41



---

archive/issue_comments_069332.json:
```json
{
    "body": "Applying the two patches\n\n- trac7958.2.patch\n- trac_7958-atomic.patch\n\nthis applies cleanly and passes all doctests.",
    "created_at": "2010-01-20T07:19:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7958",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7958#issuecomment-69332",
    "user": "https://trac.sagemath.org/admin/accounts/users/spancratz"
}
```

Applying the two patches

- trac7958.2.patch
- trac_7958-atomic.patch

this applies cleanly and passes all doctests.



---

archive/issue_comments_069333.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-20T07:19:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7958",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7958#issuecomment-69333",
    "user": "https://trac.sagemath.org/admin/accounts/users/spancratz"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_069334.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-23T07:47:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7958",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7958#issuecomment-69334",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed



---

archive/issue_events_019045.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2010-01-23T07:47:55Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7958",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7958#event-19045"
}
```



---

archive/issue_comments_069335.json:
```json
{
    "body": "Merged patches in this order:\n\n1. [trac7958.2.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7958/trac7958.2.patch)\n2. [trac_7958-atomic.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7958/trac_7958-atomic.patch)",
    "created_at": "2010-01-23T07:47:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7958",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7958#issuecomment-69335",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Merged patches in this order:

1. [trac7958.2.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7958/trac7958.2.patch)
2. [trac_7958-atomic.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7958/trac_7958-atomic.patch)
