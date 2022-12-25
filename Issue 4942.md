# Issue 4942: find_root() is broken when interval borders cannot be evaluated

archive/issues_004942.json:
```json
{
    "body": "Assignee: jkantor\n\nCC:  @kcrisman\n\nReported in http://groups.google.com/group/sage-support/browse_thread/thread/40da8039090c3e8a\n\n\n```\nHi, I'm trying out SAGE for the first time, so I entered what you \nsuggested (see above). \nNow, from the plot, it there seems to be no other roots between 0 and 2 \nso I entered \nsage: find_root(x^2*log(x,2)-1,0, 2) \nand got the root = 0.0 \nwhat am I missing here? \nTIA, \nAJG \n```\n\nBut note the following:\n\n```\nsage: find_root(1/(x-1)+1,0, 2) \n0.0 \nsage: find_root(1/(x-1)+1,0.00001, 2) \n1.0000000000011564 \n```\n\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/4942\n\n",
    "created_at": "2009-01-05T20:32:08Z",
    "labels": [
        "component: numerical",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-8.4",
    "title": "find_root() is broken when interval borders cannot be evaluated",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4942",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: jkantor

CC:  @kcrisman

Reported in http://groups.google.com/group/sage-support/browse_thread/thread/40da8039090c3e8a


```
Hi, I'm trying out SAGE for the first time, so I entered what you 
suggested (see above). 
Now, from the plot, it there seems to be no other roots between 0 and 2 
so I entered 
sage: find_root(x^2*log(x,2)-1,0, 2) 
and got the root = 0.0 
what am I missing here? 
TIA, 
AJG 
```

But note the following:

```
sage: find_root(1/(x-1)+1,0, 2) 
0.0 
sage: find_root(1/(x-1)+1,0.00001, 2) 
1.0000000000011564 
```


Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/4942





---

archive/issue_events_011394.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-01-12T02:27:29Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4942",
    "milestone": "sage-3.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4942#event-11394"
}
```



---

archive/issue_comments_037432.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-01-30T23:27:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4942",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4942#issuecomment-37432",
    "user": "https://github.com/mwhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_037433.json:
```json
{
    "body": "Changing assignee from jkantor to @mwhansen.",
    "created_at": "2009-01-30T23:27:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4942",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4942#issuecomment-37433",
    "user": "https://github.com/mwhansen"
}
```

Changing assignee from jkantor to @mwhansen.



---

archive/issue_comments_037434.json:
```json
{
    "body": "This is a critical bug and ought to be fixed in 3.3.\n\nNote that #3870 might be a dupe of this bug.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-08T06:41:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4942",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4942#issuecomment-37434",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This is a critical bug and ought to be fixed in 3.3.

Note that #3870 might be a dupe of this bug.

Cheers,

Michael



---

archive/issue_events_011395.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-02-08T06:41:17Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4942",
    "milestone": "sage-3.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4942#event-11395"
}
```



---

archive/issue_events_011396.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-02-08T06:41:17Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4942",
    "milestone": "sage-3.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4942#event-11396"
}
```



---

archive/issue_comments_037435.json:
```json
{
    "body": "It seems this is a problem with Scipy:\n\n\n```\nIn [16]: def f(x):         \n   ....:     return 1.0/(x-1.0)+1.0\n   ....: \n\nIn [17]: import scipy.optimize\n\nIn [18]: scipy.optimize.brentq(f, 0, 2)\nOut[18]: 0.0\n\nIn [19]: f(0.001)\nOut[19]: -0.0010010010010010895\n\nIn [20]: f(2)\nOut[20]: 2.0\n\nIn [21]: scipy.optimize.brentq(f, 0.001, 2)                                                   \nOut[21]: 1.0000000000007283\n\nIn [22]: f(1.0000000000007283)\nOut[22]: 1373048666882.2488\n```\n",
    "created_at": "2009-02-08T23:59:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4942",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4942#issuecomment-37435",
    "user": "https://github.com/mwhansen"
}
```

It seems this is a problem with Scipy:


```
In [16]: def f(x):         
   ....:     return 1.0/(x-1.0)+1.0
   ....: 

In [17]: import scipy.optimize

In [18]: scipy.optimize.brentq(f, 0, 2)
Out[18]: 0.0

In [19]: f(0.001)
Out[19]: -0.0010010010010010895

In [20]: f(2)
Out[20]: 2.0

In [21]: scipy.optimize.brentq(f, 0.001, 2)                                                   
Out[21]: 1.0000000000007283

In [22]: f(1.0000000000007283)
Out[22]: 1373048666882.2488
```




---

archive/issue_comments_037436.json:
```json
{
    "body": "There are at least a couple of issues here.  First, brentq is a variant of a bisection-based solver; if you use any bisection-based solver to find a zero of 1/(x-1) between 0 and 2, it will narrow down and return something very close to 1.  So if we don't like that, we should use a different solver (or at least try to check the output; for instance, a simple check that f(x) is \"small\" would detect this particular problem).\n\nSecond, find_root tries to verify that the function evaluates to different signs at the endpoints of the interval (as required by brentq); but it doesn't check the function evaluation results for NaN.  In the original test case, fast_float(f)(0) gives NaN.",
    "created_at": "2009-02-15T03:15:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4942",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4942#issuecomment-37436",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

There are at least a couple of issues here.  First, brentq is a variant of a bisection-based solver; if you use any bisection-based solver to find a zero of 1/(x-1) between 0 and 2, it will narrow down and return something very close to 1.  So if we don't like that, we should use a different solver (or at least try to check the output; for instance, a simple check that f(x) is "small" would detect this particular problem).

Second, find_root tries to verify that the function evaluates to different signs at the endpoints of the interval (as required by brentq); but it doesn't check the function evaluation results for NaN.  In the original test case, fast_float(f)(0) gives NaN.



---

archive/issue_events_011397.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-03-01T02:30:48Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4942",
    "milestone": "sage-3.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4942#event-11397"
}
```



---

archive/issue_events_011398.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-03-01T02:30:48Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4942",
    "milestone": "sage-3.4.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4942#event-11398"
}
```



---

archive/issue_comments_037437.json:
```json
{
    "body": "Better luck in 3.4.1. Unfortunately this either requires testing of the result of scipy or some deeper surgery in Scipy.\n\nCheers,\n\nMichael",
    "created_at": "2009-03-01T02:30:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4942",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4942#issuecomment-37437",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Better luck in 3.4.1. Unfortunately this either requires testing of the result of scipy or some deeper surgery in Scipy.

Cheers,

Michael



---

archive/issue_comments_037438.json:
```json
{
    "body": "Changing priority from blocker to critical.",
    "created_at": "2009-06-15T23:23:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4942",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4942#issuecomment-37438",
    "user": "https://github.com/williamstein"
}
```

Changing priority from blocker to critical.



---

archive/issue_comments_037439.json:
```json
{
    "body": "If we've released for months and months without fixing this, it doesn't make sense to keep it as a blocker.",
    "created_at": "2009-06-15T23:23:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4942",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4942#issuecomment-37439",
    "user": "https://github.com/williamstein"
}
```

If we've released for months and months without fixing this, it doesn't make sense to keep it as a blocker.



---

archive/issue_events_011399.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:34:36Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4942",
    "milestone": "sage-3.4.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4942#event-11399"
}
```



---

archive/issue_events_011400.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:34:36Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4942",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4942#event-11400"
}
```



---

archive/issue_events_011401.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4942",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4942#event-11401"
}
```



---

archive/issue_events_011402.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4942",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4942#event-11402"
}
```



---

archive/issue_events_011403.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:19:32Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4942",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4942#event-11403"
}
```



---

archive/issue_events_011404.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:19:32Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4942",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4942#event-11404"
}
```



---

archive/issue_events_011405.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4942",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4942#event-11405"
}
```



---

archive/issue_events_011406.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4942",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4942#event-11406"
}
```



---

archive/issue_comments_037440.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2018-09-04T11:23:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4942",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4942#issuecomment-37440",
    "user": "https://github.com/assaferan"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_037441.json:
```json
{
    "body": "Hi, added two small validity checks:\n1. If one of the endpoints is evaluated to NaN we seek a nearby point in the interval which can be evaluated.\n2. If the value of the function at the root found is \"large\", raise an error that we could not find it.\n----\nNew commits:",
    "created_at": "2018-09-04T11:23:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4942",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4942#issuecomment-37441",
    "user": "https://github.com/assaferan"
}
```

Hi, added two small validity checks:
1. If one of the endpoints is evaluated to NaN we seek a nearby point in the interval which can be evaluated.
2. If the value of the function at the root found is "large", raise an error that we could not find it.
----
New commits:



---

archive/issue_comments_037442.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2018-09-06T09:21:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4942",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4942#issuecomment-37442",
    "user": "https://github.com/assaferan"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_037443.json:
```json
{
    "body": "I am not sure 1 is necessarily the best solution to this because what if you get a function that always evaluates to NaN as you increase/decrease the endpoints? For instance\n\n```\nsage: f(x) = 0.0 / max(0, x)\n```\n\nwill be NaN for infinitely many values. So your current test means this runs forever:\n\n```\nsage: find_root(f, -1, 0)\n```\n\n(before it simply gave a wrong value).\n\nAlso, I think for 2 you should raise a `NotImplementedError` as I think that more accurately reflects the situation.",
    "created_at": "2018-09-06T22:32:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4942",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4942#issuecomment-37443",
    "user": "https://github.com/tscrim"
}
```

I am not sure 1 is necessarily the best solution to this because what if you get a function that always evaluates to NaN as you increase/decrease the endpoints? For instance

```
sage: f(x) = 0.0 / max(0, x)
```

will be NaN for infinitely many values. So your current test means this runs forever:

```
sage: find_root(f, -1, 0)
```

(before it simply gave a wrong value).

Also, I think for 2 you should raise a `NotImplementedError` as I think that more accurately reflects the situation.



---

archive/issue_comments_037444.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2018-09-07T10:11:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4942",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4942#issuecomment-37444",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_037445.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2018-09-07T12:01:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4942",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4942#issuecomment-37445",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_037446.json:
```json
{
    "body": "Fixed the bugs and changed behaviour in both cases, as suggested by tscrim",
    "created_at": "2018-09-07T13:20:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4942",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4942#issuecomment-37446",
    "user": "https://github.com/assaferan"
}
```

Fixed the bugs and changed behaviour in both cases, as suggested by tscrim



---

archive/issue_comments_037447.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2018-09-07T13:20:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4942",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4942#issuecomment-37447",
    "user": "https://github.com/assaferan"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_037448.json:
```json
{
    "body": "Thanks. Looks better now. A few more little things:\n\n- `ticket 4942` -> `:trac:`4942`` in the documentation.\n- Could you add the test from comment:17.\n- This change:\n  {{{#!diff\n        Traceback (most recent call last):\n-           ...\n+       ...\n        NotImplementedError: Brent's method failed to find a zero for f on the interval\n  }}}\n- Instead of using `...` for imprecision, it would be better to use `# abs tol` (or a `# rel tol`).\n- `if` statements do not need outer parentheses in Python, so remove them from `if (full_output):` and the outermost pair from the other `if` statement 4 lines down.",
    "created_at": "2018-09-07T23:24:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4942",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4942#issuecomment-37448",
    "user": "https://github.com/tscrim"
}
```

Thanks. Looks better now. A few more little things:

- `ticket 4942` -> `:trac:`4942`` in the documentation.
- Could you add the test from comment:17.
- This change:
  {{{#!diff
        Traceback (most recent call last):
-           ...
+       ...
        NotImplementedError: Brent's method failed to find a zero for f on the interval
  }}}
- Instead of using `...` for imprecision, it would be better to use `# abs tol` (or a `# rel tol`).
- `if` statements do not need outer parentheses in Python, so remove them from `if (full_output):` and the outermost pair from the other `if` statement 4 lines down.



---

archive/issue_comments_037449.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2018-09-10T08:39:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4942",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4942#issuecomment-37449",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_037450.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2018-09-17T06:28:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4942",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4942#issuecomment-37450",
    "user": "https://github.com/tscrim"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_011407.json:
```json
{
    "actor": "https://github.com/tscrim",
    "created_at": "2018-09-17T06:28:47Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4942",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4942#event-11407"
}
```



---

archive/issue_events_011408.json:
```json
{
    "actor": "https://github.com/tscrim",
    "created_at": "2018-09-17T06:28:47Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4942",
    "milestone": "sage-8.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4942#event-11408"
}
```



---

archive/issue_comments_037451.json:
```json
{
    "body": "Thank you. LGTM.",
    "created_at": "2018-09-17T06:28:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4942",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4942#issuecomment-37451",
    "user": "https://github.com/tscrim"
}
```

Thank you. LGTM.



---

archive/issue_events_011409.json:
```json
{
    "actor": "https://github.com/vbraun",
    "created_at": "2018-09-19T08:09:26Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4942",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4942#event-11409"
}
```



---

archive/issue_comments_037452.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2018-09-19T08:09:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4942",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4942#issuecomment-37452",
    "user": "https://github.com/vbraun"
}
```

Resolution: fixed
