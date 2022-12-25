# Issue 8578: method int_repr only works for small finite fields

archive/issues_008578.json:
```json
{
    "body": "Assignee: @aghitza\n\nFrom [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/f41d594281e843d9):\n\n```\nFor a finite field of, say 2^6 elements, an object representing an\nelement of such a field has a method called int_repr() that returns\nthe object's integer representation. However, if we are dealing with,\nsay GF(7^100), an object representing an element of such a field\ndoesn't have a corresponding int_repr() method. The report below\nincludes such a method, which is meant to work for a finite field of\nany order.\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8578\n\n",
    "created_at": "2010-03-22T12:00:54Z",
    "labels": [
        "component: algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "method int_repr only works for small finite fields",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8578",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```
Assignee: @aghitza

From [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/f41d594281e843d9):

```
For a finite field of, say 2^6 elements, an object representing an
element of such a field has a method called int_repr() that returns
the object's integer representation. However, if we are dealing with,
say GF(7^100), an object representing an element of such a field
doesn't have a corresponding int_repr() method. The report below
includes such a method, which is meant to work for a finite field of
any order.
```


Issue created by migration from https://trac.sagemath.org/ticket/8578





---

archive/issue_events_020704.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8578",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8578#event-20704"
}
```



---

archive/issue_events_020705.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8578",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8578#event-20705"
}
```



---

archive/issue_events_020706.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8578",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8578#event-20706"
}
```



---

archive/issue_events_020707.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8578",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8578#event-20707"
}
```



---

archive/issue_events_020708.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8578",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8578#event-20708"
}
```



---

archive/issue_events_020709.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8578",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8578#event-20709"
}
```



---

archive/issue_events_020710.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8578",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8578#event-20710"
}
```



---

archive/issue_comments_077564.json:
```json
{
    "body": "Apparently this is still an issue, see [this stack overflow question](http://stackoverflow.com/questions/36391931/how-do-i-get-the-int-representation-of-a-big-field-in-sage).",
    "created_at": "2016-04-04T14:53:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8578",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8578#issuecomment-77564",
    "user": "https://github.com/kcrisman"
}
```

Apparently this is still an issue, see [this stack overflow question](http://stackoverflow.com/questions/36391931/how-do-i-get-the-int-representation-of-a-big-field-in-sage).



---

archive/issue_comments_077565.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2021-04-05T01:27:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8578",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8578#issuecomment-77565",
    "user": "https://github.com/DaveWitteMorris"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_077566.json:
```json
{
    "body": "Changing priority from major to minor.",
    "created_at": "2021-04-05T01:27:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8578",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8578#issuecomment-77566",
    "user": "https://github.com/DaveWitteMorris"
}
```

Changing priority from major to minor.



---

archive/issue_comments_077567.json:
```json
{
    "body": "Duplicate of #31605.",
    "created_at": "2021-04-05T01:27:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8578",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8578#issuecomment-77567",
    "user": "https://github.com/DaveWitteMorris"
}
```

Duplicate of #31605.



---

archive/issue_events_020711.json:
```json
{
    "actor": "https://github.com/DaveWitteMorris",
    "created_at": "2021-04-05T01:27:27Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8578",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8578#event-20711"
}
```



---

archive/issue_events_020712.json:
```json
{
    "actor": "https://github.com/DaveWitteMorris",
    "created_at": "2021-04-05T01:27:27Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8578",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8578#event-20712"
}
```



---

archive/issue_comments_077568.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2021-04-11T23:05:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8578",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8578#issuecomment-77568",
    "user": "https://github.com/tscrim"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_020713.json:
```json
{
    "actor": "https://github.com/mkoeppe",
    "created_at": "2021-06-24T20:15:37Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8578",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8578#event-20713"
}
```



---

archive/issue_comments_077569.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2021-06-24T20:15:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8578",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8578#issuecomment-77569",
    "user": "https://github.com/mkoeppe"
}
```

Resolution: invalid
