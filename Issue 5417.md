# Issue 5417: Fix some more deepcopy/caching issues in the quadratic forms code (followup to #5403)

archive/issues_005417.json:
```json
{
    "body": "Assignee: justin\n\nGonzalo found some problem in the QF code when working on #5403. These problems are related to deepcopy.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/5417\n\n",
    "created_at": "2009-03-02T03:52:41Z",
    "labels": [
        "component: quadratic forms",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "Fix some more deepcopy/caching issues in the quadratic forms code (followup to #5403)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5417",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: justin

Gonzalo found some problem in the QF code when working on #5403. These problems are related to deepcopy.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/5417





---

archive/issue_comments_041844.json:
```json
{
    "body": "The patch in #5403 fixes the function `scale_by_factor` in `quadratic_form__variable_substitutions.py`, by replacing the use of `copy.deepcopy` + `__init__` by a call to the constructor.\n\nThe issue with this is that the caches for some functions are copied, hence the results may be incorrect. There seem to be more instances of this bug in the quadratic_forms code, hence this ticket, but that one is the only one currently triggered by the following doctest (this only happens *after* applying the `import *` fix in #5403 without the `deepcopy` fix):\n\n```\n        sage: Q = QuadraticForm(ZZ, 3, [2, -2, 0, 3, -5, 4])\n        sage: Q.jordan_blocks_in_unimodular_list_by_scale_power(2)\n        Traceback (most recent call last):\n        ...\n        TypeError: Oops!  The given quadratic form has a Jordan component with a negative scale exponent!\n        This routine requires an integer-matrix quadratic form for the output indexing to work properly!\n\n        sage: Q.scale_by_factor(2).jordan_blocks_in_unimodular_list_by_scale_power(2)\n        [Quadratic form in 2 variables over Integer Ring with coefficients: \n        [ 0 2 ]\n        [ * 0 ]\n        ,\n        Quadratic form in 0 variables over Integer Ring with coefficients: \n        ,\n        Quadratic form in 1 variables over Integer Ring with coefficients: \n        [ 345 ]\n        ]\n```\nIn this example, after the first call to `jordan_blocks_in_unimodular_list_by_scale_power`, the result is cached, and the function `scale_by_factor` copies this cached result, so that the second call returns the answer for the original quadratic form.",
    "created_at": "2009-03-02T04:21:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5417",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5417#issuecomment-41844",
    "user": "https://github.com/tornaria"
}
```

The patch in #5403 fixes the function `scale_by_factor` in `quadratic_form__variable_substitutions.py`, by replacing the use of `copy.deepcopy` + `__init__` by a call to the constructor.

The issue with this is that the caches for some functions are copied, hence the results may be incorrect. There seem to be more instances of this bug in the quadratic_forms code, hence this ticket, but that one is the only one currently triggered by the following doctest (this only happens *after* applying the `import *` fix in #5403 without the `deepcopy` fix):

```
        sage: Q = QuadraticForm(ZZ, 3, [2, -2, 0, 3, -5, 4])
        sage: Q.jordan_blocks_in_unimodular_list_by_scale_power(2)
        Traceback (most recent call last):
        ...
        TypeError: Oops!  The given quadratic form has a Jordan component with a negative scale exponent!
        This routine requires an integer-matrix quadratic form for the output indexing to work properly!

        sage: Q.scale_by_factor(2).jordan_blocks_in_unimodular_list_by_scale_power(2)
        [Quadratic form in 2 variables over Integer Ring with coefficients: 
        [ 0 2 ]
        [ * 0 ]
        ,
        Quadratic form in 0 variables over Integer Ring with coefficients: 
        ,
        Quadratic form in 1 variables over Integer Ring with coefficients: 
        [ 345 ]
        ]
```
In this example, after the first call to `jordan_blocks_in_unimodular_list_by_scale_power`, the result is cached, and the function `scale_by_factor` copies this cached result, so that the second call returns the answer for the original quadratic form.



---

archive/issue_events_012616.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5417",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5417#event-12616"
}
```



---

archive/issue_events_012617.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5417",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5417#event-12617"
}
```



---

archive/issue_events_012618.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5417",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5417#event-12618"
}
```



---

archive/issue_events_012619.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5417",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5417#event-12619"
}
```



---

archive/issue_events_012620.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5417",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5417#event-12620"
}
```



---

archive/issue_events_012621.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5417",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5417#event-12621"
}
```



---

archive/issue_events_012622.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5417",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5417#event-12622"
}
```



---

archive/issue_comments_041845.json:
```json
{
    "body": "Exactly what is the problem here? The description is very vague...",
    "created_at": "2015-08-28T09:58:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5417",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5417#issuecomment-41845",
    "user": "https://github.com/jdemeyer"
}
```

Exactly what is the problem here? The description is very vague...
