# Issue 6800: [with patch, needs review] formal/lazy/infinite powerseries

archive/issues_006800.json:
```json
{
    "body": "Assignee: burcin\n\nCC:  sage-combinat mantepse\n\nNew code that implements lazy power and Laurant series.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6800\n\n",
    "created_at": "2009-08-22T07:32:14Z",
    "labels": [
        "calculus",
        "major",
        "enhancement"
    ],
    "title": "[with patch, needs review] formal/lazy/infinite powerseries",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6800",
    "user": "Henryk.Trappmann"
}
```
Assignee: burcin

CC:  sage-combinat mantepse

New code that implements lazy power and Laurant series.

Issue created by migration from https://trac.sagemath.org/ticket/6800





---

archive/issue_comments_055993.json:
```json
{
    "body": "Attachment [12846.patch](tarball://root/attachments/some-uuid/ticket6800/12846.patch) by Henryk.Trappmann created at 2009-08-22 07:33:49\n\npatch adds the file formal_powerseries.py",
    "created_at": "2009-08-22T07:33:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6800#issuecomment-55993",
    "user": "Henryk.Trappmann"
}
```

Attachment [12846.patch](tarball://root/attachments/some-uuid/ticket6800/12846.patch) by Henryk.Trappmann created at 2009-08-22 07:33:49

patch adds the file formal_powerseries.py



---

archive/issue_comments_055994.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2009-12-08T10:03:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6800#issuecomment-55994",
    "user": "AlexGhitza"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_055995.json:
```json
{
    "body": "The documentation needs some serious reformatting to adhere to the ReST format.  I am cc-ing sage-combinat because a lot of people there would be interested in formal power and Laurent series.",
    "created_at": "2009-12-08T10:03:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6800#issuecomment-55995",
    "user": "AlexGhitza"
}
```

The documentation needs some serious reformatting to adhere to the ReST format.  I am cc-ing sage-combinat because a lot of people there would be interested in formal power and Laurent series.



---

archive/issue_comments_055996.json:
```json
{
    "body": "Changing component from calculus to algebra.",
    "created_at": "2009-12-08T10:03:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6800#issuecomment-55996",
    "user": "AlexGhitza"
}
```

Changing component from calculus to algebra.



---

archive/issue_comments_055997.json:
```json
{
    "body": "Changing keywords from \"\" to \"LazyPowerSeries\".",
    "created_at": "2014-01-10T20:48:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6800#issuecomment-55997",
    "user": "mantepse"
}
```

Changing keywords from "" to "LazyPowerSeries".



---

archive/issue_comments_055998.json:
```json
{
    "body": "I think although there is `combinat.species.series.LazyPowerSeries` this implementation would still be good to have, as the implementation in combinat misses many features included here. It is also needed for P-finite sequences. \n\nHowever, I don't think it's right to define all special functions anew: the ring or a static function should be able to create a series from a symbolic expression (interpreted as e.g.f.), and , in case of a rational polynomial, delegate to CFiniteSequence (#15714).\n\nThere were a few failures:\n\n```\n   1 of  39 in sage.rings.formal_powerseries.FormalPowerSeries\n   1 of   6 in sage.rings.formal_powerseries.FormalPowerSeries.nipow\n   1 of   6 in sage.rings.formal_powerseries.FormalPowerSeries.pow\n   3 of   8 in sage.rings.formal_powerseries.FormalPowerSeries0.abel\n   1 of   4 in sage.rings.formal_powerseries.decidable0\n```\n",
    "created_at": "2014-03-15T17:01:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6800#issuecomment-55998",
    "user": "rws"
}
```

I think although there is `combinat.species.series.LazyPowerSeries` this implementation would still be good to have, as the implementation in combinat misses many features included here. It is also needed for P-finite sequences. 

However, I don't think it's right to define all special functions anew: the ring or a static function should be able to create a series from a symbolic expression (interpreted as e.g.f.), and , in case of a rational polynomial, delegate to CFiniteSequence (#15714).

There were a few failures:

```
   1 of  39 in sage.rings.formal_powerseries.FormalPowerSeries
   1 of   6 in sage.rings.formal_powerseries.FormalPowerSeries.nipow
   1 of   6 in sage.rings.formal_powerseries.FormalPowerSeries.pow
   3 of   8 in sage.rings.formal_powerseries.FormalPowerSeries0.abel
   1 of   4 in sage.rings.formal_powerseries.decidable0
```




---

archive/issue_comments_055999.json:
```json
{
    "body": "This is subsumed by #32324.",
    "created_at": "2022-08-11T17:48:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6800#issuecomment-55999",
    "user": "mantepse"
}
```

This is subsumed by #32324.



---

archive/issue_comments_056000.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2022-08-11T17:49:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6800#issuecomment-56000",
    "user": "mantepse"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_056001.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2022-08-11T17:49:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6800#issuecomment-56001",
    "user": "mantepse"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_056002.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2022-09-01T02:30:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6800#issuecomment-56002",
    "user": "mkoeppe"
}
```

Resolution: invalid
