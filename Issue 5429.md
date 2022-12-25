# Issue 5429: Change the QuadraticForm base_ring to only define the equivalence, but not the ring for coefficients/values

archive/issues_005429.json:
```json
{
    "body": "Assignee: tbd\n\nIt is sometimes inconvenient to require that all quadratic_forms take values in their ring of equivalence.  This should be separated out into two parts, a coefficient_ring and an equivalence_ring.  \n\nPerhaps for ease of tab-completion these should be called ring_* instead of *_ring?  Also, coefficient_ring could equally well be called value_ring, though that may be more confusing to find for the average user.\n\nCalls to the base_ring() method should almost everywhere be replaced by calls to equivalence_ring(), with the notable exception of the constructor.\n\nThe default constructor would take only one ring, which would be the equivalence ring, and the inferred coefficient ring would be the fraction field/object of the given ring.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5429\n\n",
    "created_at": "2009-03-03T13:37:46Z",
    "labels": [
        "component: algebra"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "Change the QuadraticForm base_ring to only define the equivalence, but not the ring for coefficients/values",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5429",
    "user": "https://github.com/jonhanke"
}
```
Assignee: tbd

It is sometimes inconvenient to require that all quadratic_forms take values in their ring of equivalence.  This should be separated out into two parts, a coefficient_ring and an equivalence_ring.  

Perhaps for ease of tab-completion these should be called ring_* instead of *_ring?  Also, coefficient_ring could equally well be called value_ring, though that may be more confusing to find for the average user.

Calls to the base_ring() method should almost everywhere be replaced by calls to equivalence_ring(), with the notable exception of the constructor.

The default constructor would take only one ring, which would be the equivalence ring, and the inferred coefficient ring would be the fraction field/object of the given ring.

Issue created by migration from https://trac.sagemath.org/ticket/5429





---

archive/issue_comments_041930.json:
```json
{
    "body": "Changing component from algebra to quadratic forms.",
    "created_at": "2010-01-01T23:09:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5429",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5429#issuecomment-41930",
    "user": "https://github.com/aghitza"
}
```

Changing component from algebra to quadratic forms.



---

archive/issue_events_012667.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5429",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5429#event-12667"
}
```



---

archive/issue_events_012668.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5429",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5429#event-12668"
}
```



---

archive/issue_events_012669.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5429",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5429#event-12669"
}
```



---

archive/issue_events_012670.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5429",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5429#event-12670"
}
```



---

archive/issue_events_012671.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5429",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5429#event-12671"
}
```



---

archive/issue_events_012672.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5429",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5429#event-12672"
}
```



---

archive/issue_events_012673.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5429",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5429#event-12673"
}
```
