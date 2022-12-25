# Issue 5317: DeprecationWarning in pickle_jar is not pre-determined

archive/issues_005317.json:
```json
{
    "body": "Assignee: mabshoff\n\nThe output of deprecation warnings can vary:\n\n```\nsage -t -long devel/sage/sage/structure/sage_object.pyx\n**********************************************************************\nFile \"/scratch/mabshoff/sage-3.3.rc3/devel/sage-main/sage/structure/sage_object.pyx\", line 682:\n    sage: sage.structure.sage_object.unpickle_all(std)\nExpected:\n    doctest:...: DeprecationWarning: Your data is stored in an old format. Please use the save() function to store your data in a more recent format.\n    doctest:...: DeprecationWarning: RQDF is deprecated; use RealField(212) instead.\n    Successfully unpickled ... objects.\n    Failed to unpickle 0 objects.\nGot:\n    doctest:1172: DeprecationWarning: RQDF is deprecated; use RealField(212) instead.\n    doctest:1172: DeprecationWarning: Your data is stored in an old format. Please use the save() function to store your data in a more recent format.\n    Successfully unpickled 448 objects.\n    Failed to unpickle 0 objects.\n**********************************************************************\n```\n\nI have hit this once for literally thousands of doctest runs so far, so I don't think this will be a big problem.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/5317\n\n",
    "created_at": "2009-02-20T06:38:39Z",
    "labels": [
        "component: doctest coverage",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "DeprecationWarning in pickle_jar is not pre-determined",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5317",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff

The output of deprecation warnings can vary:

```
sage -t -long devel/sage/sage/structure/sage_object.pyx
**********************************************************************
File "/scratch/mabshoff/sage-3.3.rc3/devel/sage-main/sage/structure/sage_object.pyx", line 682:
    sage: sage.structure.sage_object.unpickle_all(std)
Expected:
    doctest:...: DeprecationWarning: Your data is stored in an old format. Please use the save() function to store your data in a more recent format.
    doctest:...: DeprecationWarning: RQDF is deprecated; use RealField(212) instead.
    Successfully unpickled ... objects.
    Failed to unpickle 0 objects.
Got:
    doctest:1172: DeprecationWarning: RQDF is deprecated; use RealField(212) instead.
    doctest:1172: DeprecationWarning: Your data is stored in an old format. Please use the save() function to store your data in a more recent format.
    Successfully unpickled 448 objects.
    Failed to unpickle 0 objects.
**********************************************************************
```

I have hit this once for literally thousands of doctest runs so far, so I don't think this will be a big problem.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/5317





---

archive/issue_events_012382.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5317",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5317#event-12382"
}
```



---

archive/issue_events_012383.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5317",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5317#event-12383"
}
```



---

archive/issue_events_012384.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5317",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5317#event-12384"
}
```



---

archive/issue_events_012385.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5317",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5317#event-12385"
}
```



---

archive/issue_events_012386.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5317",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5317#event-12386"
}
```



---

archive/issue_comments_040868.json:
```json
{
    "body": "This was fixed at some point.",
    "created_at": "2014-08-07T00:54:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5317",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5317#issuecomment-40868",
    "user": "https://github.com/tscrim"
}
```

This was fixed at some point.



---

archive/issue_comments_040869.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2014-08-07T00:54:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5317",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5317#issuecomment-40869",
    "user": "https://github.com/tscrim"
}
```

Changing status from new to needs_review.



---

archive/issue_events_012387.json:
```json
{
    "actor": "https://github.com/tscrim",
    "created_at": "2014-08-07T00:54:56Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5317",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5317#event-12387"
}
```



---

archive/issue_events_012388.json:
```json
{
    "actor": "https://github.com/tscrim",
    "created_at": "2014-08-07T00:54:56Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5317",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5317#event-12388"
}
```



---

archive/issue_comments_040870.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2014-08-10T20:20:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5317",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5317#issuecomment-40870",
    "user": "https://github.com/a-andre"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_040871.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2014-08-20T20:32:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5317",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5317#issuecomment-40871",
    "user": "https://github.com/vbraun"
}
```

Resolution: fixed



---

archive/issue_events_012389.json:
```json
{
    "actor": "https://github.com/vbraun",
    "created_at": "2014-08-20T20:32:54Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5317",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5317#event-12389"
}
```
