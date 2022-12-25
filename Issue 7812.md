# Issue 7812: Compute Bell numbers using mpmath by default (instead of GAP)

archive/issues_007812.json:
```json
{
    "body": "Assignee: sage-combinat\n\nCC:  @jbandlow @nathanncohen\n\nKeywords: bell numbers\n\nFredrick Johansson discusses [here](http://fredrik-j.blogspot.com/2009/03/computing-generalized-bell-numbers.html) his implementation of generalized Bell numbers in mpmath. I've verified that this function is present in the version of mpmath shipped with sage 4.3. Benchmarks show it is faster than GAP (currently used by sage) and even mathematica.  This should be very easy to wrap.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7812\n\n",
    "closed_at": "2013-05-03T08:03:01Z",
    "created_at": "2010-01-02T02:41:55Z",
    "labels": [
        "component: combinatorics"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Compute Bell numbers using mpmath by default (instead of GAP)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7812",
    "user": "https://github.com/jbandlow"
}
```
Assignee: sage-combinat

CC:  @jbandlow @nathanncohen

Keywords: bell numbers

Fredrick Johansson discusses [here](http://fredrik-j.blogspot.com/2009/03/computing-generalized-bell-numbers.html) his implementation of generalized Bell numbers in mpmath. I've verified that this function is present in the version of mpmath shipped with sage 4.3. Benchmarks show it is faster than GAP (currently used by sage) and even mathematica.  This should be very easy to wrap.

Issue created by migration from https://trac.sagemath.org/ticket/7812





---

archive/issue_comments_067481.json:
```json
{
    "body": "I've exposed (wrapped) mpmath's `bell()` in #10170.",
    "created_at": "2013-03-28T21:39:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7812#issuecomment-67481",
    "user": "https://github.com/tscrim"
}
```

I've exposed (wrapped) mpmath's `bell()` in #10170.



---

archive/issue_events_018704.json:
```json
{
    "actor": "https://github.com/tscrim",
    "created_at": "2013-03-28T21:39:17Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7812",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7812#event-18704"
}
```



---

archive/issue_comments_067482.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2013-03-28T21:39:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7812#issuecomment-67482",
    "user": "https://github.com/tscrim"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_067483.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2013-05-01T19:39:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7812#issuecomment-67483",
    "user": "https://github.com/bsalisbury1"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_018705.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-05-03T08:03:01Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7812",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7812#event-18705"
}
```



---

archive/issue_comments_067484.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2013-05-03T08:03:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7812#issuecomment-67484",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: duplicate
