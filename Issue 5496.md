# Issue 5496: fix bugs in is_prime  (EASY)

archive/issues_005496.json:
```json
{
    "body": "Assignee: was\n\nThis is not good:\n\n```\nsage: is_prime(GF(5)(3))\nTrue\nsage: is_prime(GF(5)(4))\nFalse\n```\n\n\nThe fix is to totally 100% rewrite is_prime in arith.py so that it first calls x.is_prime() and if that isn't defined, then in some special cases (e.g., python ints) converts to Integer and calls is_prime.  Otherwise, it raises a NotImplementedError. \n\nIssue created by migration from https://trac.sagemath.org/ticket/5496\n\n",
    "created_at": "2009-03-12T02:55:11Z",
    "labels": [
        "number theory",
        "major",
        "bug"
    ],
    "title": "fix bugs in is_prime  (EASY)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5496",
    "user": "was"
}
```
Assignee: was

This is not good:

```
sage: is_prime(GF(5)(3))
True
sage: is_prime(GF(5)(4))
False
```


The fix is to totally 100% rewrite is_prime in arith.py so that it first calls x.is_prime() and if that isn't defined, then in some special cases (e.g., python ints) converts to Integer and calls is_prime.  Otherwise, it raises a NotImplementedError. 

Issue created by migration from https://trac.sagemath.org/ticket/5496





---

archive/issue_comments_042683.json:
```json
{
    "body": "Right now finite fields don't seem to have an is_prime function, so I believe that currently, is_prime(GF(5)(3)) should raise NotImplementedError.  I'm going to try to fix is_prime so that it raises NotImplementedError for is_prime(GF(5)(3)).\n\n\nKevin Stueve",
    "created_at": "2010-01-17T21:08:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5496",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5496#issuecomment-42683",
    "user": "kevin.stueve"
}
```

Right now finite fields don't seem to have an is_prime function, so I believe that currently, is_prime(GF(5)(3)) should raise NotImplementedError.  I'm going to try to fix is_prime so that it raises NotImplementedError for is_prime(GF(5)(3)).


Kevin Stueve



---

archive/issue_comments_042684.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-17T21:49:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5496",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5496#issuecomment-42684",
    "user": "kevin.stueve"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_042685.json:
```json
{
    "body": "Attachment\n\nchanged delegation of is_prime calculation to n.is_prime()",
    "created_at": "2010-01-17T22:11:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5496",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5496#issuecomment-42685",
    "user": "kevin.stueve"
}
```

Attachment

changed delegation of is_prime calculation to n.is_prime()



---

archive/issue_comments_042686.json:
```json
{
    "body": "Attachment",
    "created_at": "2010-01-17T23:19:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5496",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5496#issuecomment-42686",
    "user": "kevin.stueve"
}
```

Attachment



---

archive/issue_comments_042687.json:
```json
{
    "body": "Apply only 5496.2.patch.",
    "created_at": "2010-01-17T23:22:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5496",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5496#issuecomment-42687",
    "user": "kevin.stueve"
}
```

Apply only 5496.2.patch.



---

archive/issue_comments_042688.json:
```json
{
    "body": "Three small changes throughout the Sage library",
    "created_at": "2010-01-18T01:03:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5496",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5496#issuecomment-42688",
    "user": "spancratz"
}
```

Three small changes throughout the Sage library



---

archive/issue_comments_042689.json:
```json
{
    "body": "Attachment\n\nSecond addendum, for symbolic expressions",
    "created_at": "2010-01-18T04:51:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5496",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5496#issuecomment-42689",
    "user": "spancratz"
}
```

Attachment

Second addendum, for symbolic expressions



---

archive/issue_comments_042690.json:
```json
{
    "body": "Applying Kevin's second patch ``5496.2.patch`` and the two small changes I added, this now passes all doctests done with ``sage -t devel/sage/sage``, and can get a positive review.",
    "created_at": "2010-01-18T04:53:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5496",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5496#issuecomment-42690",
    "user": "spancratz"
}
```

Applying Kevin's second patch ``5496.2.patch`` and the two small changes I added, this now passes all doctests done with ``sage -t devel/sage/sage``, and can get a positive review.



---

archive/issue_comments_042691.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-18T04:53:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5496",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5496#issuecomment-42691",
    "user": "spancratz"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_042692.json:
```json
{
    "body": "\n```\nif type(n) == int or type(n)==long: \n```\n\nshould be\n\n```\nif isinstance(n, (int, long)):\n```\n",
    "created_at": "2010-01-18T05:36:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5496",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5496#issuecomment-42692",
    "user": "was"
}
```


```
if type(n) == int or type(n)==long: 
```

should be

```
if isinstance(n, (int, long)):
```




---

archive/issue_comments_042693.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-01-18T05:36:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5496",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5496#issuecomment-42693",
    "user": "was"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_042694.json:
```json
{
    "body": "Also, use `obj.pyobject()` in some cases for symbolics...",
    "created_at": "2010-01-18T05:37:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5496",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5496#issuecomment-42694",
    "user": "was"
}
```

Also, use `obj.pyobject()` in some cases for symbolics...



---

archive/issue_comments_042695.json:
```json
{
    "body": "Third addendum, for one character change for lucas numbers",
    "created_at": "2010-01-18T05:38:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5496",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5496#issuecomment-42695",
    "user": "spancratz"
}
```

Third addendum, for one character change for lucas numbers



---

archive/issue_comments_042696.json:
```json
{
    "body": "Attachment\n\nI've now incorporated the handling of symbolic expressions as suggested by Burcin.  The sequence of patches should be applied in the order\n\n- 5496.2.patch\n- trac5496_rationals_to_int.patch\n- trac5496_symbolic_expressions.patch\n- trac5496_lucas.patch\n- trac5496_symbolic_expressions2.patch\n\nI am running doctests now, but if they pass this should get positive review again.",
    "created_at": "2010-01-18T06:01:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5496",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5496#issuecomment-42696",
    "user": "spancratz"
}
```

Attachment

I've now incorporated the handling of symbolic expressions as suggested by Burcin.  The sequence of patches should be applied in the order

- 5496.2.patch
- trac5496_rationals_to_int.patch
- trac5496_symbolic_expressions.patch
- trac5496_lucas.patch
- trac5496_symbolic_expressions2.patch

I am running doctests now, but if they pass this should get positive review again.



---

archive/issue_comments_042697.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-01-18T06:01:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5496",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5496#issuecomment-42697",
    "user": "spancratz"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_042698.json:
```json
{
    "body": "Attachment\n\nFourth addendum, for symbolic expressions",
    "created_at": "2010-01-18T06:06:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5496",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5496#issuecomment-42698",
    "user": "spancratz"
}
```

Attachment

Fourth addendum, for symbolic expressions



---

archive/issue_comments_042699.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-18T06:24:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5496",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5496#issuecomment-42699",
    "user": "spancratz"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_042700.json:
```json
{
    "body": "This is to confirm that all doctests have been passed, checked with \"./sage -t devel/sage/sage\".",
    "created_at": "2010-01-18T06:24:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5496",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5496#issuecomment-42700",
    "user": "spancratz"
}
```

This is to confirm that all doctests have been passed, checked with "./sage -t devel/sage/sage".



---

archive/issue_comments_042701.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-19T01:15:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5496",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5496#issuecomment-42701",
    "user": "rlm"
}
```

Resolution: fixed
