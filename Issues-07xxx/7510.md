# Issue 7510: is_finite method in categories (was Primes is missing is_finite)

archive/issues_007510.json:
```json
{
    "body": "Assignee: @hivert\n\nKeywords: Primes, is_finite\n\nI found that Primes has no methods `is_finite`. This is actually not a problem of `Prime` but should be dealt in categories. I put a small patch here though i'm not sure we want to do this. Isn't this redundent with categories ? \n\nCheers,\n\nFlorent\n \n\nIssue created by migration from https://trac.sagemath.org/ticket/7510\n\n",
    "closed_at": "2009-12-01T05:30:54Z",
    "created_at": "2009-11-21T15:20:15Z",
    "labels": [
        "component: categories",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3",
    "title": "is_finite method in categories (was Primes is missing is_finite)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7510",
    "user": "https://github.com/hivert"
}
```
Assignee: @hivert

Keywords: Primes, is_finite

I found that Primes has no methods `is_finite`. This is actually not a problem of `Prime` but should be dealt in categories. I put a small patch here though i'm not sure we want to do this. Isn't this redundent with categories ? 

Cheers,

Florent
 

Issue created by migration from https://trac.sagemath.org/ticket/7510





---

archive/issue_comments_063454.json:
```json
{
    "body": "Changing assignee from @williamstein to @hivert.",
    "created_at": "2009-11-21T15:20:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7510",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7510#issuecomment-63454",
    "user": "https://github.com/hivert"
}
```

Changing assignee from @williamstein to @hivert.



---

archive/issue_comments_063455.json:
```json
{
    "body": "Changing component from number theory to categories.",
    "created_at": "2009-11-21T15:44:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7510",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7510#issuecomment-63455",
    "user": "https://github.com/hivert"
}
```

Changing component from number theory to categories.



---

archive/issue_comments_063456.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-11-21T15:45:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7510",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7510#issuecomment-63456",
    "user": "https://github.com/hivert"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_063457.json:
```json
{
    "body": "For the second example, don't you want an EnumeratedSet and not a FiniteEnumeratedSet?",
    "created_at": "2009-11-21T19:18:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7510",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7510#issuecomment-63457",
    "user": "https://github.com/mwhansen"
}
```

For the second example, don't you want an EnumeratedSet and not a FiniteEnumeratedSet?



---

archive/issue_comments_063458.json:
```json
{
    "body": "Attachment [trac_7510-is_finite_categories.patch](tarball://root/attachments/some-uuid/ticket7510/trac_7510-is_finite_categories.patch) by @hivert created at 2009-11-21 22:43:31",
    "created_at": "2009-11-21T22:43:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7510",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7510#issuecomment-63458",
    "user": "https://github.com/hivert"
}
```

Attachment [trac_7510-is_finite_categories.patch](tarball://root/attachments/some-uuid/ticket7510/trac_7510-is_finite_categories.patch) by @hivert created at 2009-11-21 22:43:31



---

archive/issue_comments_063459.json:
```json
{
    "body": "Replying to [comment:4 mhansen]:\n> For the second example, don't you want an EnumeratedSet and not a FiniteEnumeratedSet?\n\n\nSure ! The example didn't even pass the test... I forgot to re-export before uploading the patch... Thank for pointing this out and sorry for the trouble...",
    "created_at": "2009-11-21T22:45:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7510",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7510#issuecomment-63459",
    "user": "https://github.com/hivert"
}
```

Replying to [comment:4 mhansen]:
> For the second example, don't you want an EnumeratedSet and not a FiniteEnumeratedSet?


Sure ! The example didn't even pass the test... I forgot to re-export before uploading the patch... Thank for pointing this out and sorry for the trouble...



---

archive/issue_comments_063460.json:
```json
{
    "body": "Looks good.",
    "created_at": "2009-12-01T05:30:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7510",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7510#issuecomment-63460",
    "user": "https://github.com/mwhansen"
}
```

Looks good.



---

archive/issue_events_017803.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2009-12-01T05:30:54Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7510",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7510#event-17803"
}
```



---

archive/issue_comments_063461.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-12-01T05:30:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7510",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7510#issuecomment-63461",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed
