# Issue 9463: Integer factorization should handle perfect powers efficiently

archive/issues_009463.json:
```json
{
    "body": "Assignee: @aghitza\n\nCC:  @jdemeyer\n\nfactor() is extremely slow at factoring large perfect powers (with a nontrivial base).\n\n```\nsage: %time factor(next_prime(10^20)^150)\nCPU times: user 0.75 s, sys: 0.00 s, total: 0.75 s\nWall time: 0.75 s\n100000000000000000039^150\nsage: %time factor(next_prime(10^20)^250)\nCPU times: user 2.68 s, sys: 0.00 s, total: 2.68 s\nWall time: 2.69 s\n100000000000000000039^250\nsage: %time factor(next_prime(10^20)^500)\nCPU times: user 13.19 s, sys: 0.00 s, total: 13.19 s\nWall time: 13.20 s\n100000000000000000039^500\n```\nFor comparison, SymPy handles such numbers in an instant:\n\n```\nsage: from sympy import factorint\nsage: %time factorint(next_prime(10^20)^150)\nCPU times: user 0.01 s, sys: 0.00 s, total: 0.01 s\nWall time: 0.01 s\n{100000000000000000039L: 150}\nsage: %time factorint(next_prime(10^20)^250)\nCPU times: user 0.01 s, sys: 0.00 s, total: 0.01 s\nWall time: 0.01 s\n{100000000000000000039L: 250}\nsage: %time factorint(next_prime(10^20)^500)\nCPU times: user 0.02 s, sys: 0.00 s, total: 0.02 s\nWall time: 0.02 s\n{100000000000000000039L: 500}\n```\nPerfect power testing is very cheap, so it should be attempted early on for large numbers.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9463\n\n",
    "created_at": "2010-07-09T09:03:28Z",
    "labels": [
        "component: basic arithmetic",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Integer factorization should handle perfect powers efficiently",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9463",
    "user": "https://github.com/fredrik-johansson"
}
```
Assignee: @aghitza

CC:  @jdemeyer

factor() is extremely slow at factoring large perfect powers (with a nontrivial base).

```
sage: %time factor(next_prime(10^20)^150)
CPU times: user 0.75 s, sys: 0.00 s, total: 0.75 s
Wall time: 0.75 s
100000000000000000039^150
sage: %time factor(next_prime(10^20)^250)
CPU times: user 2.68 s, sys: 0.00 s, total: 2.68 s
Wall time: 2.69 s
100000000000000000039^250
sage: %time factor(next_prime(10^20)^500)
CPU times: user 13.19 s, sys: 0.00 s, total: 13.19 s
Wall time: 13.20 s
100000000000000000039^500
```
For comparison, SymPy handles such numbers in an instant:

```
sage: from sympy import factorint
sage: %time factorint(next_prime(10^20)^150)
CPU times: user 0.01 s, sys: 0.00 s, total: 0.01 s
Wall time: 0.01 s
{100000000000000000039L: 150}
sage: %time factorint(next_prime(10^20)^250)
CPU times: user 0.01 s, sys: 0.00 s, total: 0.01 s
Wall time: 0.01 s
{100000000000000000039L: 250}
sage: %time factorint(next_prime(10^20)^500)
CPU times: user 0.02 s, sys: 0.00 s, total: 0.02 s
Wall time: 0.02 s
{100000000000000000039L: 500}
```
Perfect power testing is very cheap, so it should be attempted early on for large numbers.

Issue created by migration from https://trac.sagemath.org/ticket/9463





---

archive/issue_comments_090597.json:
```json
{
    "body": "Changing assignee from @aghitza to tbd.",
    "created_at": "2010-07-11T08:03:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9463",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9463#issuecomment-90597",
    "user": "https://github.com/jdemeyer"
}
```

Changing assignee from @aghitza to tbd.



---

archive/issue_comments_090598.json:
```json
{
    "body": "This is because of the way PARI factors number (first trial division, then perfect power checking).  See http://pari.math.u-bordeaux.fr/cgi-bin/bugreport.cgi?bug=1074",
    "created_at": "2010-07-11T08:03:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9463",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9463#issuecomment-90598",
    "user": "https://github.com/jdemeyer"
}
```

This is because of the way PARI factors number (first trial division, then perfect power checking).  See http://pari.math.u-bordeaux.fr/cgi-bin/bugreport.cgi?bug=1074



---

archive/issue_comments_090599.json:
```json
{
    "body": "Changing component from basic arithmetic to factorization.",
    "created_at": "2010-07-11T08:03:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9463",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9463#issuecomment-90599",
    "user": "https://github.com/jdemeyer"
}
```

Changing component from basic arithmetic to factorization.



---

archive/issue_comments_090600.json:
```json
{
    "body": "Examples take milliseconds now even on old computer, so I guess this has been fixed and can be closed.",
    "created_at": "2016-08-20T05:51:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9463",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9463#issuecomment-90600",
    "user": "https://github.com/jm58660"
}
```

Examples take milliseconds now even on old computer, so I guess this has been fixed and can be closed.



---

archive/issue_events_023441.json:
```json
{
    "actor": "https://github.com/jm58660",
    "created_at": "2016-08-20T05:51:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9463",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9463#event-23441"
}
```



---

archive/issue_comments_090601.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2016-08-20T05:51:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9463",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9463#issuecomment-90601",
    "user": "https://github.com/jm58660"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_090602.json:
```json
{
    "body": "I agree!",
    "created_at": "2016-08-21T14:57:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9463",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9463#issuecomment-90602",
    "user": "https://github.com/bgrenet"
}
```

I agree!



---

archive/issue_comments_090603.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2016-08-21T14:57:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9463",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9463#issuecomment-90603",
    "user": "https://github.com/bgrenet"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_023442.json:
```json
{
    "actor": "https://github.com/embray",
    "created_at": "2016-08-30T13:32:25Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9463",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9463#event-23442"
}
```



---

archive/issue_comments_090604.json:
```json
{
    "body": "Determined to be invalid/duplicate/wontfix (closing as \"wontfix\" as a catch-all resolution).",
    "created_at": "2016-08-30T13:32:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9463",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9463#issuecomment-90604",
    "user": "https://github.com/embray"
}
```

Determined to be invalid/duplicate/wontfix (closing as "wontfix" as a catch-all resolution).



---

archive/issue_comments_090605.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2016-08-30T13:32:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9463",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9463#issuecomment-90605",
    "user": "https://github.com/embray"
}
```

Resolution: wontfix
