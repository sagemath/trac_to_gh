# Issue 6800: formal/lazy/infinite powerseries

archive/issues_006800.json:
```json
{
    "body": "Assignee: @burcin\n\nCC:  sage-combinat @mantepse\n\nKeywords: LazyPowerSeries\n\nNew code that implements lazy power and Laurent series.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6800\n\n",
    "closed_at": "2022-09-01T02:30:35Z",
    "created_at": "2009-08-22T07:32:14Z",
    "labels": [
        "component: algebra"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "formal/lazy/infinite powerseries",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6800",
    "user": "https://trac.sagemath.org/admin/accounts/users/Henryk.Trappmann"
}
```
Assignee: @burcin

CC:  sage-combinat @mantepse

Keywords: LazyPowerSeries

New code that implements lazy power and Laurent series.

Issue created by migration from https://trac.sagemath.org/ticket/6800





---

archive/issue_comments_055891.json:
```json
{
    "body": "Attachment [12846.patch](tarball://root/attachments/some-uuid/ticket6800/12846.patch) by Henryk.Trappmann created at 2009-08-22 07:33:49\n\npatch adds the file formal_powerseries.py",
    "created_at": "2009-08-22T07:33:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6800#issuecomment-55891",
    "user": "https://trac.sagemath.org/admin/accounts/users/Henryk.Trappmann"
}
```

Attachment [12846.patch](tarball://root/attachments/some-uuid/ticket6800/12846.patch) by Henryk.Trappmann created at 2009-08-22 07:33:49

patch adds the file formal_powerseries.py



---

archive/issue_comments_055892.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2009-12-08T10:03:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6800#issuecomment-55892",
    "user": "https://github.com/aghitza"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_055893.json:
```json
{
    "body": "The documentation needs some serious reformatting to adhere to the ReST format.  I am cc-ing sage-combinat because a lot of people there would be interested in formal power and Laurent series.",
    "created_at": "2009-12-08T10:03:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6800#issuecomment-55893",
    "user": "https://github.com/aghitza"
}
```

The documentation needs some serious reformatting to adhere to the ReST format.  I am cc-ing sage-combinat because a lot of people there would be interested in formal power and Laurent series.



---

archive/issue_comments_055894.json:
```json
{
    "body": "Changing component from calculus to algebra.",
    "created_at": "2009-12-08T10:03:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6800#issuecomment-55894",
    "user": "https://github.com/aghitza"
}
```

Changing component from calculus to algebra.



---

archive/issue_events_016018.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6800",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6800#event-16018"
}
```



---

archive/issue_comments_055895.json:
```json
{
    "body": "Changing keywords from \"\" to \"LazyPowerSeries\".",
    "created_at": "2014-01-10T20:48:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6800#issuecomment-55895",
    "user": "https://github.com/mantepse"
}
```

Changing keywords from "" to "LazyPowerSeries".



---

archive/issue_events_016019.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6800",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6800#event-16019"
}
```



---

archive/issue_events_016020.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6800",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6800#event-16020"
}
```



---

archive/issue_comments_055896.json:
```json
{
    "body": "I think although there is `combinat.species.series.LazyPowerSeries` this implementation would still be good to have, as the implementation in combinat misses many features included here. It is also needed for P-finite sequences. \n\nHowever, I don't think it's right to define all special functions anew: the ring or a static function should be able to create a series from a symbolic expression (interpreted as e.g.f.), and , in case of a rational polynomial, delegate to CFiniteSequence (#15714).\n\nThere were a few failures:\n\n```\n   1 of  39 in sage.rings.formal_powerseries.FormalPowerSeries\n   1 of   6 in sage.rings.formal_powerseries.FormalPowerSeries.nipow\n   1 of   6 in sage.rings.formal_powerseries.FormalPowerSeries.pow\n   3 of   8 in sage.rings.formal_powerseries.FormalPowerSeries0.abel\n   1 of   4 in sage.rings.formal_powerseries.decidable0\n```",
    "created_at": "2014-03-15T17:01:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6800#issuecomment-55896",
    "user": "https://github.com/rwst"
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

archive/issue_events_016021.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6800",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6800#event-16021"
}
```



---

archive/issue_events_016022.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6800",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6800#event-16022"
}
```



---

archive/issue_events_016023.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6800",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6800#event-16023"
}
```



---

archive/issue_events_016024.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6800",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6800#event-16024"
}
```



---

archive/issue_comments_055897.json:
```json
{
    "body": "This is subsumed by #32324.",
    "created_at": "2022-08-11T17:48:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6800#issuecomment-55897",
    "user": "https://github.com/mantepse"
}
```

This is subsumed by #32324.



---

archive/issue_comments_055898.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2022-08-11T17:49:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6800#issuecomment-55898",
    "user": "https://github.com/mantepse"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_events_016025.json:
```json
{
    "actor": "https://github.com/mantepse",
    "created_at": "2022-08-11T17:49:25Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6800",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6800#event-16025"
}
```



---

archive/issue_events_016026.json:
```json
{
    "actor": "https://github.com/mantepse",
    "created_at": "2022-08-11T17:49:25Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6800",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6800#event-16026"
}
```



---

archive/issue_comments_055899.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2022-08-11T17:49:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6800#issuecomment-55899",
    "user": "https://github.com/mantepse"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_016027.json:
```json
{
    "actor": "https://github.com/mkoeppe",
    "created_at": "2022-09-01T02:30:35Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6800",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6800#event-16027"
}
```



---

archive/issue_comments_055900.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2022-09-01T02:30:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6800#issuecomment-55900",
    "user": "https://github.com/mkoeppe"
}
```

Resolution: invalid
