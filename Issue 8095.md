# Issue 8095: is_primitive of WordMorphism is broken

archive/issues_008095.json:
```json
{
    "body": "Assignee: slabbe\n\nCC:  abmasse\n\nLet us define the following morphism over 3 letters:\n\n```\nsage: substitution=WordMorphism('a->b,b->ac,c->a')\n```\n\nThen we get\n\n```\nsage: substitution.is_primitive()\nFalse\n```\n\nbut also\n\n```\nsage: (substitution^2).is_primitive()\nTrue\n```\n\n\n------\n\nexpected behaviour:\n\nSee the description of \".is_primitive()\":\nReturns True if self is primitive.\nA morphism \u03d5 is primitive if there exists an positive integer k such\nthat for all \u03b1\u2208\u03a3, \u03d5k(\u03b1) contains all the letters of \u03a3.\n\nSo, if a morphism is primitive, so are all its powers. And if there is\na power which is primitive, so is the morphism itself. In the example\nabove, both outputs should be \"True\".\n\nIssue created by migration from https://trac.sagemath.org/ticket/8095\n\n",
    "created_at": "2010-01-27T13:59:46Z",
    "labels": [
        "combinatorics",
        "major",
        "bug"
    ],
    "title": "is_primitive of WordMorphism is broken",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8095",
    "user": "slabbe"
}
```
Assignee: slabbe

CC:  abmasse

Let us define the following morphism over 3 letters:

```
sage: substitution=WordMorphism('a->b,b->ac,c->a')
```

Then we get

```
sage: substitution.is_primitive()
False
```

but also

```
sage: (substitution^2).is_primitive()
True
```


------

expected behaviour:

See the description of ".is_primitive()":
Returns True if self is primitive.
A morphism ϕ is primitive if there exists an positive integer k such
that for all α∈Σ, ϕk(α) contains all the letters of Σ.

So, if a morphism is primitive, so are all its powers. And if there is
a power which is primitive, so is the morphism itself. In the example
above, both outputs should be "True".

Issue created by migration from https://trac.sagemath.org/ticket/8095





---

archive/issue_comments_070964.json:
```json
{
    "body": "I just posted a patch which solves the described problem. The solution uses the following algorithm:\n\n\n```\nALGORITHM: \n \n   Let `m` be the incidence matrix of a endomorphism on a monoid  \n   of `d` letters. The endomorphism is primitive if and only if \n   there exists `k` such that `1 \\leq k \\leq (d-1)^2+1` and `m^k`  \n   contains no zero. \n```\n\n\nAre we sure this is true? Is there a proof of that somewhere?",
    "created_at": "2010-01-27T15:22:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8095",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8095#issuecomment-70964",
    "user": "slabbe"
}
```

I just posted a patch which solves the described problem. The solution uses the following algorithm:


```
ALGORITHM: 
 
   Let `m` be the incidence matrix of a endomorphism on a monoid  
   of `d` letters. The endomorphism is primitive if and only if 
   there exists `k` such that `1 \leq k \leq (d-1)^2+1` and `m^k`  
   contains no zero. 
```


Are we sure this is true? Is there a proof of that somewhere?



---

archive/issue_comments_070965.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-27T15:22:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8095",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8095#issuecomment-70965",
    "user": "slabbe"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_070966.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-01-28T16:41:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8095",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8095#issuecomment-70966",
    "user": "slabbe"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_070967.json:
```json
{
    "body": "Attachment [trac_8095_wordmorph_is_primitive-sl.patch](tarball://root/attachments/some-uuid/ticket8095/trac_8095_wordmorph_is_primitive-sl.patch) by slabbe created at 2010-01-29 14:23:05\n\ntested on sage-4.3.1",
    "created_at": "2010-01-29T14:23:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8095",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8095#issuecomment-70967",
    "user": "slabbe"
}
```

Attachment [trac_8095_wordmorph_is_primitive-sl.patch](tarball://root/attachments/some-uuid/ticket8095/trac_8095_wordmorph_is_primitive-sl.patch) by slabbe created at 2010-01-29 14:23:05

tested on sage-4.3.1



---

archive/issue_comments_070968.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-01-29T14:24:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8095",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8095#issuecomment-70968",
    "user": "slabbe"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_070969.json:
```json
{
    "body": "I found a reference for the above statement (Automatic sequences of Allouche and Shallit).",
    "created_at": "2010-01-29T14:24:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8095",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8095#issuecomment-70969",
    "user": "slabbe"
}
```

I found a reference for the above statement (Automatic sequences of Allouche and Shallit).



---

archive/issue_comments_070970.json:
```json
{
    "body": "Tested on sage-4.3.1 as well and it works.\nIt fixes the reported problem as well.\nAll tests passed when running ``sage -t morphism.py\".\nPositive review.",
    "created_at": "2010-01-29T14:44:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8095",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8095#issuecomment-70970",
    "user": "abmasse"
}
```

Tested on sage-4.3.1 as well and it works.
It fixes the reported problem as well.
All tests passed when running ``sage -t morphism.py".
Positive review.



---

archive/issue_comments_070971.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-29T14:44:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8095",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8095#issuecomment-70971",
    "user": "abmasse"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_070972.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-30T23:41:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8095",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8095#issuecomment-70972",
    "user": "mvngu"
}
```

Resolution: fixed
