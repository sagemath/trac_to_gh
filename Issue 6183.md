# Issue 6183: [with patch, needs work] Quaternion algebra latexification

archive/issues_006183.json:
```json
{
    "body": "Assignee: @aghitza\n\nKeywords: quaternion latex\n\nQuaternion algebra elements don't have a nice latexification. This should be easy for someone to add. \n\nIssue created by migration from https://trac.sagemath.org/ticket/6183\n\n",
    "created_at": "2009-06-02T07:28:18Z",
    "labels": [
        "component: algebra",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "[with patch, needs work] Quaternion algebra latexification",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6183",
    "user": "https://github.com/robertwb"
}
```
Assignee: @aghitza

Keywords: quaternion latex

Quaternion algebra elements don't have a nice latexification. This should be easy for someone to add. 

Issue created by migration from https://trac.sagemath.org/ticket/6183





---

archive/issue_comments_049267.json:
```json
{
    "body": "Changing assignee from tbd to @aghitza.",
    "created_at": "2009-07-11T13:12:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6183",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6183#issuecomment-49267",
    "user": "https://github.com/aghitza"
}
```

Changing assignee from tbd to @aghitza.



---

archive/issue_comments_049268.json:
```json
{
    "body": "Changing keywords from \"\" to \"quaternion latex\".",
    "created_at": "2009-07-11T13:12:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6183",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6183#issuecomment-49268",
    "user": "https://github.com/aghitza"
}
```

Changing keywords from "" to "quaternion latex".



---

archive/issue_comments_049269.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2009-07-11T13:12:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6183",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6183#issuecomment-49269",
    "user": "https://github.com/aghitza"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_049270.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-07-11T13:12:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6183",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6183#issuecomment-49270",
    "user": "https://github.com/aghitza"
}
```

Changing status from new to assigned.



---

archive/issue_events_014514.json:
```json
{
    "actor": "https://github.com/aghitza",
    "created_at": "2009-07-11T13:12:02Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6183",
    "milestone": "sage-4.1.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6183#event-14514"
}
```



---

archive/issue_comments_049271.json:
```json
{
    "body": "See attached patch.",
    "created_at": "2009-07-11T13:12:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6183",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6183#issuecomment-49271",
    "user": "https://github.com/aghitza"
}
```

See attached patch.



---

archive/issue_comments_049272.json:
```json
{
    "body": "Attachment [trac_6183.patch](tarball://root/attachments/some-uuid/ticket6183/trac_6183.patch) by @aghitza created at 2009-07-11 13:12:23",
    "created_at": "2009-07-11T13:12:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6183",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6183#issuecomment-49272",
    "user": "https://github.com/aghitza"
}
```

Attachment [trac_6183.patch](tarball://root/attachments/some-uuid/ticket6183/trac_6183.patch) by @aghitza created at 2009-07-11 13:12:23



---

archive/issue_comments_049273.json:
```json
{
    "body": "```\nsage: B.<i, j, k> = QuaternionAlgebra(RR, -1, -1) \nsage: latex(i + 1 - k) \n1.00000000000000 + i - k\n```\n\nWith all due respect, this is hideous :-) I know you only did it for consistency with the `repr` method, of course; but what would you say to the suggestion that we change `repr`, and `latex`, so they return something like `1.00000000000000 + 1.00000000000000*i - 1.00000000000000*k`? This is consistent with our conventions for other algebras over inexact rings (e.g. polynomials and power series).",
    "created_at": "2009-07-13T19:16:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6183",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6183#issuecomment-49273",
    "user": "https://github.com/loefflerd"
}
```

```
sage: B.<i, j, k> = QuaternionAlgebra(RR, -1, -1) 
sage: latex(i + 1 - k) 
1.00000000000000 + i - k
```

With all due respect, this is hideous :-) I know you only did it for consistency with the `repr` method, of course; but what would you say to the suggestion that we change `repr`, and `latex`, so they return something like `1.00000000000000 + 1.00000000000000*i - 1.00000000000000*k`? This is consistent with our conventions for other algebras over inexact rings (e.g. polynomials and power series).



---

archive/issue_comments_049274.json:
```json
{
    "body": "Point taken.\n\nI'm changing this to \"needs work\".  I'll try to find an elegant way of using the printing code for polynomials so that things are consistent (and stay that way).",
    "created_at": "2009-07-14T07:05:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6183",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6183#issuecomment-49274",
    "user": "https://github.com/aghitza"
}
```

Point taken.

I'm changing this to "needs work".  I'll try to find an elegant way of using the printing code for polynomials so that things are consistent (and stay that way).



---

archive/issue_comments_049275.json:
```json
{
    "body": "Actually, note that printing of polynomials is *not* consistent, in that multivariable polynomials have \"hideous\" printing, whereas univariate ones have \"pretty\" printing:\n\n```\nsage: R.<i, j, k> = RR[]\nsage: i + 1 - k\ni - k + 1.00000000000000\nsage: R.<i> = RR[[]]\nsage: i+1\n1.00000000000000 + 1.00000000000000*i\n```\n\nSo this needs fixing.",
    "created_at": "2009-07-14T07:41:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6183",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6183#issuecomment-49275",
    "user": "https://github.com/aghitza"
}
```

Actually, note that printing of polynomials is *not* consistent, in that multivariable polynomials have "hideous" printing, whereas univariate ones have "pretty" printing:

```
sage: R.<i, j, k> = RR[]
sage: i + 1 - k
i - k + 1.00000000000000
sage: R.<i> = RR[[]]
sage: i+1
1.00000000000000 + 1.00000000000000*i
```

So this needs fixing.



---

archive/issue_events_014515.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6183",
    "milestone": "sage-4.1.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6183#event-14515"
}
```



---

archive/issue_events_014516.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6183",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6183#event-14516"
}
```



---

archive/issue_events_014517.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6183",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6183#event-14517"
}
```



---

archive/issue_events_014518.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6183",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6183#event-14518"
}
```



---

archive/issue_events_014519.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6183",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6183#event-14519"
}
```



---

archive/issue_events_014520.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6183",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6183#event-14520"
}
```



---

archive/issue_events_014521.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6183",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6183#event-14521"
}
```



---

archive/issue_events_014522.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6183",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6183#event-14522"
}
```
