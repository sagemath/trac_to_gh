# Issue 5641: plotting of matrices with 0 rows or columns is broken in multiple ways

archive/issues_005641.json:
```json
{
    "body": "Assignee: @williamstein\n\n\n```\nsage: matrix(QQ,0).plot()\nTraceback (most recent call last):\n...\nIndexError: index out of bounds\n\nsage: matrix(QQ,0,5).plot()\nTraceback (most recent call last):\n...\nIndexError: index out of bounds\n\nsage: matrix(QQ,5,0).plot()\nTraceback (most recent call last):\n...\nValueError: zero-size array to ufunc.reduce without identity\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5641\n\n",
    "created_at": "2009-03-30T03:18:23Z",
    "labels": [
        "component: graphics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "plotting of matrices with 0 rows or columns is broken in multiple ways",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5641",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein


```
sage: matrix(QQ,0).plot()
Traceback (most recent call last):
...
IndexError: index out of bounds

sage: matrix(QQ,0,5).plot()
Traceback (most recent call last):
...
IndexError: index out of bounds

sage: matrix(QQ,5,0).plot()
Traceback (most recent call last):
...
ValueError: zero-size array to ufunc.reduce without identity
```


Issue created by migration from https://trac.sagemath.org/ticket/5641





---

archive/issue_comments_043979.json:
```json
{
    "body": "Still broken, though now all three have the latter error message.  I'm not sure I like this even being possible:\n\n```\nsage: A = matrix(QQ,5,0)\nsage: A.rows()\n[(), (), (), (), ()]\n```\n\nDoes this have meaning?\n\nAnyway, the error is raised while trying to acquire a colormap in matplotlib in imshow, and then Numpy doesn't like one of the inputs.  Having a Numpy or matplotlib-native version of this would be helpful - maybe the problem is upstream?  Or maybe we're just using it wrong and should have a special thing for plotting empty matrices... ??",
    "created_at": "2012-06-01T18:31:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5641",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5641#issuecomment-43979",
    "user": "https://github.com/kcrisman"
}
```

Still broken, though now all three have the latter error message.  I'm not sure I like this even being possible:

```
sage: A = matrix(QQ,5,0)
sage: A.rows()
[(), (), (), (), ()]
```

Does this have meaning?

Anyway, the error is raised while trying to acquire a colormap in matplotlib in imshow, and then Numpy doesn't like one of the inputs.  Having a Numpy or matplotlib-native version of this would be helpful - maybe the problem is upstream?  Or maybe we're just using it wrong and should have a special thing for plotting empty matrices... ??



---

archive/issue_events_013265.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5641",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5641#event-13265"
}
```



---

archive/issue_events_013266.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5641",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5641#event-13266"
}
```



---

archive/issue_events_013267.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5641",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5641#event-13267"
}
```



---

archive/issue_events_013268.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5641",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5641#event-13268"
}
```



---

archive/issue_events_013269.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5641",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5641#event-13269"
}
```



---

archive/issue_events_013270.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5641",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5641#event-13270"
}
```



---

archive/issue_events_013271.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5641",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5641#event-13271"
}
```
