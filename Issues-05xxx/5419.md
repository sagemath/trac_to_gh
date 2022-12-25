# Issue 5419: moving fraction field to new coercion broke old pickles

archive/issues_005419.json:
```json
{
    "body": "Assignee: @craigcitro\n\nCC:  @burcin\n\nAt some point, fraction fields were moved over to the new coercion model, which is good -- except that it broke all the old pickles. This thread on `sage-support` is about someone having a problem with them: http://groups.google.com/group/sage-support/browse_thread/thread/b5519db45a141819\n\nThe problem is that the old pickles don't have `_element_class` or `_element_constructor` fields, and there was no factory function in place -- so unpickling tries to directly create the object, which totally fails. Putting the old `__call__` method back in place is an ugly hack to get these to load, but it's not a good permanent solution. \n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5419\n\n",
    "created_at": "2009-03-02T06:40:28Z",
    "labels": [
        "component: misc",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "moving fraction field to new coercion broke old pickles",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5419",
    "user": "https://github.com/craigcitro"
}
```
Assignee: @craigcitro

CC:  @burcin

At some point, fraction fields were moved over to the new coercion model, which is good -- except that it broke all the old pickles. This thread on `sage-support` is about someone having a problem with them: http://groups.google.com/group/sage-support/browse_thread/thread/b5519db45a141819

The problem is that the old pickles don't have `_element_class` or `_element_constructor` fields, and there was no factory function in place -- so unpickling tries to directly create the object, which totally fails. Putting the old `__call__` method back in place is an ugly hack to get these to load, but it's not a good permanent solution. 



Issue created by migration from https://trac.sagemath.org/ticket/5419





---

archive/issue_comments_041848.json:
```json
{
    "body": "Hmm,\n\nhow did this escape the pickle jar doctest?\n\nCheers,\n\nMichael",
    "created_at": "2009-03-02T07:00:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5419",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5419#issuecomment-41848",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Hmm,

how did this escape the pickle jar doctest?

Cheers,

Michael



---

archive/issue_comments_041849.json:
```json
{
    "body": "Changing component from algebra to misc.",
    "created_at": "2009-03-02T07:00:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5419",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5419#issuecomment-41849",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing component from algebra to misc.



---

archive/issue_events_012625.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-03-02T07:00:10Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5419",
    "milestone": "sage-3.4.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5419#event-12625"
}
```



---

archive/issue_events_012626.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5419",
    "milestone": "sage-3.4.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5419#event-12626"
}
```



---

archive/issue_events_012627.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5419",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5419#event-12627"
}
```



---

archive/issue_events_012628.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5419",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5419#event-12628"
}
```



---

archive/issue_events_012629.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5419",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5419#event-12629"
}
```



---

archive/issue_events_012630.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5419",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5419#event-12630"
}
```



---

archive/issue_events_012631.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5419",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5419#event-12631"
}
```



---

archive/issue_events_012632.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5419",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5419#event-12632"
}
```



---

archive/issue_events_012633.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5419",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5419#event-12633"
}
```
