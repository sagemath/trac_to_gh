# Issue 6592: minimize_constrained only takes lambda functions as constraints

archive/issues_006592.json:
```json
{
    "body": "Assignee: jkantor\n\nCC:  @mforets\n\ne.g.:\n\n```\nsage: var('x y')\nsage: f = (100 - x) + (1000 - y)\nsage: c = x + y - 479 # > 0\nsage: minimize_constrained(f,[c],[100,300])\nTraceback (most recent call last):\n...\nUnboundLocalError: local variable 'min' referenced before assignment\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/6592\n\n",
    "created_at": "2009-07-22T15:31:31Z",
    "labels": [
        "component: numerical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-8.0",
    "title": "minimize_constrained only takes lambda functions as constraints",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6592",
    "user": "https://github.com/rlmill"
}
```
Assignee: jkantor

CC:  @mforets

e.g.:

```
sage: var('x y')
sage: f = (100 - x) + (1000 - y)
sage: c = x + y - 479 # > 0
sage: minimize_constrained(f,[c],[100,300])
Traceback (most recent call last):
...
UnboundLocalError: local variable 'min' referenced before assignment
```

Issue created by migration from https://trac.sagemath.org/ticket/6592





---

archive/issue_comments_053847.json:
```json
{
    "body": "More clearly, here's the \"bug\" part of this.  The documentation says that the function takes a symbolic function, but clearly does not:\n\n```\nsage: f(x,y) = (100 - x) + (1000 - y)\nsage: c = x + y - 479 \nsage: minimize_constrained(f,[c],[100,300])\n---------------------------------------------------------------------------\nUnboundLocalError                         Traceback (most recent call last)\n\n/home/grout/<ipython console> in <module>()\n\n/home/grout/sage/local/lib/python2.6/site-packages/sage/numerical/optimize.pyc in minimize_constrained(func, cons, x0, gradient, algorithm, **args)\n    408     elif isinstance(cons, function_type):\n    409         min= optimize.fmin_cobyla(f,x0,cons,iprint=0,**args)\n--> 410     return vector(RDF,min)\n    411 \n    412     \n\nUnboundLocalError: local variable 'min' referenced before assignment\n\n\n```",
    "created_at": "2010-03-17T05:12:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6592",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6592#issuecomment-53847",
    "user": "https://github.com/jasongrout"
}
```

More clearly, here's the "bug" part of this.  The documentation says that the function takes a symbolic function, but clearly does not:

```
sage: f(x,y) = (100 - x) + (1000 - y)
sage: c = x + y - 479 
sage: minimize_constrained(f,[c],[100,300])
---------------------------------------------------------------------------
UnboundLocalError                         Traceback (most recent call last)

/home/grout/<ipython console> in <module>()

/home/grout/sage/local/lib/python2.6/site-packages/sage/numerical/optimize.pyc in minimize_constrained(func, cons, x0, gradient, algorithm, **args)
    408     elif isinstance(cons, function_type):
    409         min= optimize.fmin_cobyla(f,x0,cons,iprint=0,**args)
--> 410     return vector(RDF,min)
    411 
    412     

UnboundLocalError: local variable 'min' referenced before assignment


```



---

archive/issue_events_015535.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6592",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6592#event-15535"
}
```



---

archive/issue_events_015536.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6592",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6592#event-15536"
}
```



---

archive/issue_events_015537.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6592",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6592#event-15537"
}
```



---

archive/issue_events_015538.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6592",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6592#event-15538"
}
```



---

archive/issue_events_015539.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6592",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6592#event-15539"
}
```



---

archive/issue_events_015540.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6592",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6592#event-15540"
}
```



---

archive/issue_events_015541.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6592",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6592#event-15541"
}
```



---

archive/issue_comments_053848.json:
```json
{
    "body": "New commits:",
    "created_at": "2017-05-28T05:34:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6592",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6592#issuecomment-53848",
    "user": "https://github.com/mforets"
}
```

New commits:



---

archive/issue_events_015542.json:
```json
{
    "actor": "https://github.com/mforets",
    "created_at": "2017-05-28T05:34:23Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6592",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6592#event-15542"
}
```



---

archive/issue_events_015543.json:
```json
{
    "actor": "https://github.com/mforets",
    "created_at": "2017-05-28T05:34:23Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6592",
    "milestone": "sage-8.0",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6592#event-15543"
}
```



---

archive/issue_comments_053849.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2017-05-28T05:34:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6592",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6592#issuecomment-53849",
    "user": "https://github.com/mforets"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_053850.json:
```json
{
    "body": "This patch adds code branches for the cases when the constraints are one or more symbolic expressions. There is also some cleanup (PEP-8).",
    "created_at": "2017-05-28T07:21:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6592",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6592#issuecomment-53850",
    "user": "https://github.com/mforets"
}
```

This patch adds code branches for the cases when the constraints are one or more symbolic expressions. There is also some cleanup (PEP-8).



---

archive/issue_comments_053851.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2017-07-11T03:53:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6592",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6592#issuecomment-53851",
    "user": "https://github.com/tscrim"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_053852.json:
```json
{
    "body": "The code make sense and fixes the error.",
    "created_at": "2017-07-11T03:53:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6592",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6592#issuecomment-53852",
    "user": "https://github.com/tscrim"
}
```

The code make sense and fixes the error.



---

archive/issue_comments_053853.json:
```json
{
    "body": "Replying to [comment:10 tscrim]:\n> The code make sense and fixes the error.\n\n\nthanks for reviewing :)",
    "created_at": "2017-07-11T06:13:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6592",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6592#issuecomment-53853",
    "user": "https://github.com/mforets"
}
```

Replying to [comment:10 tscrim]:
> The code make sense and fixes the error.


thanks for reviewing :)



---

archive/issue_comments_053854.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2017-07-26T22:13:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6592",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6592#issuecomment-53854",
    "user": "https://github.com/vbraun"
}
```

Resolution: fixed



---

archive/issue_events_015544.json:
```json
{
    "actor": "https://github.com/vbraun",
    "created_at": "2017-07-26T22:13:49Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6592",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6592#event-15544"
}
```
