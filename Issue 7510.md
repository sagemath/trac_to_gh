# Issue 7510: Primes is missing is_finite.

archive/issues_007510.json:
```json
{
    "body": "Assignee: @williamstein\n\nKeywords: Primes, is_finite\n\nPrimes has no methods `is_finite`. This breaks several thing including: \n\n```\nsage: contre_exemples = (p for p in Primes() and not is_prime(mersenne(p)))\n\n---------------------------------------------------------------------------\nAttributeError                            Traceback (most recent call last)\n\n/home/averell/.sage/temp/tomahawk/25868/_home_averell__sage_init_sage_0.py in <module>()\n\n/usr/local/sage/sage-4.2/local/lib/python2.6/site-packages/sage/structure/parent.so in sage.structure.parent.Set_generic.__nonzero__ (sage/structure/parent.c:14641)()\n\nAttributeError: 'Primes_with_category' object has no attribute 'is_finite'\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7510\n\n",
    "created_at": "2009-11-21T15:20:15Z",
    "labels": [
        "number theory",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3",
    "title": "Primes is missing is_finite.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7510",
    "user": "@hivert"
}
```
Assignee: @williamstein

Keywords: Primes, is_finite

Primes has no methods `is_finite`. This breaks several thing including: 

```
sage: contre_exemples = (p for p in Primes() and not is_prime(mersenne(p)))

---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)

/home/averell/.sage/temp/tomahawk/25868/_home_averell__sage_init_sage_0.py in <module>()

/usr/local/sage/sage-4.2/local/lib/python2.6/site-packages/sage/structure/parent.so in sage.structure.parent.Set_generic.__nonzero__ (sage/structure/parent.c:14641)()

AttributeError: 'Primes_with_category' object has no attribute 'is_finite'
```


Issue created by migration from https://trac.sagemath.org/ticket/7510





---

archive/issue_comments_063570.json:
```json
{
    "body": "Changing assignee from @williamstein to @hivert.",
    "created_at": "2009-11-21T15:20:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7510",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7510#issuecomment-63570",
    "user": "@hivert"
}
```

Changing assignee from @williamstein to @hivert.



---

archive/issue_comments_063571.json:
```json
{
    "body": "Changing component from number theory to categories.",
    "created_at": "2009-11-21T15:44:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7510",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7510#issuecomment-63571",
    "user": "@hivert"
}
```

Changing component from number theory to categories.



---

archive/issue_comments_063572.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-11-21T15:45:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7510",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7510#issuecomment-63572",
    "user": "@hivert"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_063573.json:
```json
{
    "body": "For the second example, don't you want an EnumeratedSet and not a FiniteEnumeratedSet?",
    "created_at": "2009-11-21T19:18:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7510",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7510#issuecomment-63573",
    "user": "@mwhansen"
}
```

For the second example, don't you want an EnumeratedSet and not a FiniteEnumeratedSet?



---

archive/issue_comments_063574.json:
```json
{
    "body": "Attachment [trac_7510-is_finite_categories.patch](tarball://root/attachments/some-uuid/ticket7510/trac_7510-is_finite_categories.patch) by @hivert created at 2009-11-21 22:43:31",
    "created_at": "2009-11-21T22:43:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7510",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7510#issuecomment-63574",
    "user": "@hivert"
}
```

Attachment [trac_7510-is_finite_categories.patch](tarball://root/attachments/some-uuid/ticket7510/trac_7510-is_finite_categories.patch) by @hivert created at 2009-11-21 22:43:31



---

archive/issue_comments_063575.json:
```json
{
    "body": "Replying to [comment:4 mhansen]:\n> For the second example, don't you want an EnumeratedSet and not a FiniteEnumeratedSet?\n\nSure ! The example didn't even pass the test... I forgot to re-export before uploading the patch... Thank for pointing this out and sorry for the trouble...",
    "created_at": "2009-11-21T22:45:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7510",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7510#issuecomment-63575",
    "user": "@hivert"
}
```

Replying to [comment:4 mhansen]:
> For the second example, don't you want an EnumeratedSet and not a FiniteEnumeratedSet?

Sure ! The example didn't even pass the test... I forgot to re-export before uploading the patch... Thank for pointing this out and sorry for the trouble...



---

archive/issue_comments_063576.json:
```json
{
    "body": "Looks good.",
    "created_at": "2009-12-01T05:30:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7510",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7510#issuecomment-63576",
    "user": "@mwhansen"
}
```

Looks good.



---

archive/issue_comments_063577.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-12-01T05:30:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7510",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7510#issuecomment-63577",
    "user": "@mwhansen"
}
```

Resolution: fixed
