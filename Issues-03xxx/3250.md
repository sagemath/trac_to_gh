# Issue 3250: Parent does not have a cdef class default hash

archive/issues_003250.json:
```json
{
    "body": "Assignee: @robertwb\n\nCC:  @robertwb\n\nParent does has a default hash for python classes, but not for cython classes.  This leads to very subtle bugs where converting a python class to a cython class can result in coercion failing mysteriously.  Either coercion should be more descriptive with its error messages resulting from lack of a hash function or Parent should get a default cdef hash function.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3250\n\n",
    "closed_at": "2018-03-08T10:05:34Z",
    "created_at": "2008-05-18T02:33:23Z",
    "labels": [
        "component: coercion",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Parent does not have a cdef class default hash",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3250",
    "user": "https://github.com/garyfurnish"
}
```
Assignee: @robertwb

CC:  @robertwb

Parent does has a default hash for python classes, but not for cython classes.  This leads to very subtle bugs where converting a python class to a cython class can result in coercion failing mysteriously.  Either coercion should be more descriptive with its error messages resulting from lack of a hash function or Parent should get a default cdef hash function.

Issue created by migration from https://trac.sagemath.org/ticket/3250





---

archive/issue_comments_022440.json:
```json
{
    "body": "Changing assignee from @rlmill to @robertwb.",
    "created_at": "2008-05-18T02:33:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3250",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3250#issuecomment-22440",
    "user": "https://github.com/garyfurnish"
}
```

Changing assignee from @rlmill to @robertwb.



---

archive/issue_comments_022441.json:
```json
{
    "body": "Changing component from coding theory to coercion.",
    "created_at": "2008-05-18T02:33:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3250",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3250#issuecomment-22441",
    "user": "https://github.com/garyfurnish"
}
```

Changing component from coding theory to coercion.



---

archive/issue_comments_022442.json:
```json
{
    "body": "Hashing/comparison is being addressed in the new coercion model.",
    "created_at": "2008-06-12T23:44:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3250",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3250#issuecomment-22442",
    "user": "https://github.com/robertwb"
}
```

Hashing/comparison is being addressed in the new coercion model.



---

archive/issue_comments_022443.json:
```json
{
    "body": "Hi Robert,\n\nI assume this has been addressed by now? If so please close this ticket as fixed.\n\nCheers,\n\nMichael",
    "created_at": "2008-12-10T13:47:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3250",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3250#issuecomment-22443",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Hi Robert,

I assume this has been addressed by now? If so please close this ticket as fixed.

Cheers,

Michael



---

archive/issue_comments_022444.json:
```json
{
    "body": "We didn't do as many changes to the comparison/hashing model as we had intended starting out, mainly because it just got to be too much on top of everything else... \n\nHowever, short of a specific example, this ticket is rather vague, and I have never run into this.",
    "created_at": "2008-12-11T07:42:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3250",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3250#issuecomment-22444",
    "user": "https://github.com/robertwb"
}
```

We didn't do as many changes to the comparison/hashing model as we had intended starting out, mainly because it just got to be too much on top of everything else... 

However, short of a specific example, this ticket is rather vague, and I have never run into this.



---

archive/issue_events_007296.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3250",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3250#event-7296"
}
```



---

archive/issue_events_007297.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3250",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3250#event-7297"
}
```



---

archive/issue_events_007298.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3250",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3250#event-7298"
}
```



---

archive/issue_events_007299.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3250",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3250#event-7299"
}
```



---

archive/issue_events_007300.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3250",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3250#event-7300"
}
```



---

archive/issue_events_007301.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3250",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3250#event-7301"
}
```



---

archive/issue_events_007302.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3250",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3250#event-7302"
}
```



---

archive/issue_events_007303.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2018-03-08T10:05:34Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3250",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3250#event-7303"
}
```



---

archive/issue_events_007304.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2018-03-08T10:05:34Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3250",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3250#event-7304"
}
```



---

archive/issue_events_007305.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2018-03-08T10:05:34Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3250",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3250#event-7305"
}
```



---

archive/issue_comments_022445.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2018-03-08T10:05:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3250",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3250#issuecomment-22445",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: invalid
