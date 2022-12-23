# Issue 8722: S-units sometimes broken and sometimes just plain wrong for relative fields

archive/issues_008722.json:
```json
{
    "body": "Assignee: davidloeffler\n\n\n```\nsage: L.<a,b> = NumberField([x^2 + 1, x^2 - 5])\nsage: p = L.ideal((-1/2*b - 1/2)*a + 1/2*b - 1/2)\nsage: p.absolute_norm()\n9\nsage: p.is_prime()\nTrue\nsage: W = L.S_units([p]); W\n[1/2*a + 7/4, a, 1/2*b - 1/2]\nsage: W[0].valuation(L.primes_above(2)[0])\n-4\n```\n\nSo the first element of the list of S-units isn't actually an S-unit! In other examples the code just blows up, because it calls `residue_field` and that dies because of #8721:\n\n```\nsage: L.<a, b> = NumberField([polygen(QQ)^2 - 3, polygen(QQ)^2 - 5])\nsage: L.S_units([L.ideal(a)])\n```\n\nThis is arguably less bad: raising an error is far better than silently a wrong answer.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8722\n\n",
    "created_at": "2010-04-20T09:09:57Z",
    "labels": [
        "number fields",
        "major",
        "bug"
    ],
    "title": "S-units sometimes broken and sometimes just plain wrong for relative fields",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8722",
    "user": "davidloeffler"
}
```
Assignee: davidloeffler


```
sage: L.<a,b> = NumberField([x^2 + 1, x^2 - 5])
sage: p = L.ideal((-1/2*b - 1/2)*a + 1/2*b - 1/2)
sage: p.absolute_norm()
9
sage: p.is_prime()
True
sage: W = L.S_units([p]); W
[1/2*a + 7/4, a, 1/2*b - 1/2]
sage: W[0].valuation(L.primes_above(2)[0])
-4
```

So the first element of the list of S-units isn't actually an S-unit! In other examples the code just blows up, because it calls `residue_field` and that dies because of #8721:

```
sage: L.<a, b> = NumberField([polygen(QQ)^2 - 3, polygen(QQ)^2 - 5])
sage: L.S_units([L.ideal(a)])
```

This is arguably less bad: raising an error is far better than silently a wrong answer.

Issue created by migration from https://trac.sagemath.org/ticket/8722





---

archive/issue_comments_079650.json:
```json
{
    "body": "Here's a patch. Turns out that the code was using `K.gen` and the correct answer is to call `K.absolute_generator`, which isn't the same in the above example. This fixes the first example; the second is an instance of #8721.",
    "created_at": "2010-04-20T09:52:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8722",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8722#issuecomment-79650",
    "user": "davidloeffler"
}
```

Here's a patch. Turns out that the code was using `K.gen` and the correct answer is to call `K.absolute_generator`, which isn't the same in the above example. This fixes the first example; the second is an instance of #8721.



---

archive/issue_comments_079651.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-04-20T09:52:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8722",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8722#issuecomment-79651",
    "user": "davidloeffler"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_079652.json:
```json
{
    "body": "Attachment\n\napply over patches at #8446",
    "created_at": "2010-04-20T09:56:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8722",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8722#issuecomment-79652",
    "user": "davidloeffler"
}
```

Attachment

apply over patches at #8446



---

archive/issue_comments_079653.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-04-21T08:36:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8722",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8722#issuecomment-79653",
    "user": "cremona"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_079654.json:
```json
{
    "body": "Looks good, applied fine to 4.4.alpha0 + #8446 patches, and all tests in sage/rings/number_field pass.\n\nPositive review!",
    "created_at": "2010-04-21T08:36:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8722",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8722#issuecomment-79654",
    "user": "cremona"
}
```

Looks good, applied fine to 4.4.alpha0 + #8446 patches, and all tests in sage/rings/number_field pass.

Positive review!



---

archive/issue_comments_079655.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-04-23T17:09:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8722",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8722#issuecomment-79655",
    "user": "jhpalmieri"
}
```

Resolution: fixed



---

archive/issue_comments_079656.json:
```json
{
    "body": "Merged into 4.4.alpha2.",
    "created_at": "2010-04-23T17:09:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8722",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8722#issuecomment-79656",
    "user": "jhpalmieri"
}
```

Merged into 4.4.alpha2.
