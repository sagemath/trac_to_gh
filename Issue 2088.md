# Issue 2088: Optional spkgs should be integrated into the automated cython building

archive/issues_002088.json:
```json
{
    "body": "Assignee: mabshoff\n\nThere should be a way of building optional cython interfaces for optional spkgs in a way that is very easy for the user.  For example, it would be nice to have optional spkg cython things automatically built in the sage -b process.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2088\n\n",
    "created_at": "2008-02-07T19:52:08Z",
    "labels": [
        "component: distribution"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Optional spkgs should be integrated into the automated cython building",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2088",
    "user": "https://github.com/jasongrout"
}
```
Assignee: mabshoff

There should be a way of building optional cython interfaces for optional spkgs in a way that is very easy for the user.  For example, it would be nice to have optional spkg cython things automatically built in the sage -b process.


Issue created by migration from https://trac.sagemath.org/ticket/2088





---

archive/issue_events_004998.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2088",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2088#event-4998"
}
```



---

archive/issue_comments_013482.json:
```json
{
    "body": "I guess this works now, using\n\n```\nif is_package_installed('some_package'):\n```\n\nin `module_list.py`.",
    "created_at": "2013-08-13T15:44:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2088",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2088#issuecomment-13482",
    "user": "https://github.com/jdemeyer"
}
```

I guess this works now, using

```
if is_package_installed('some_package'):
```

in `module_list.py`.



---

archive/issue_events_004999.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:44:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2088",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2088#event-4999"
}
```



---

archive/issue_events_005000.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:44:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2088",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2088#event-5000"
}
```



---

archive/issue_comments_013483.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2013-08-13T15:44:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2088",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2088#issuecomment-13483",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_013484.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2013-08-13T15:59:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2088",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2088#issuecomment-13484",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_005001.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-16T11:11:39Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2088",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2088#event-5001"
}
```



---

archive/issue_comments_013485.json:
```json
{
    "body": "Resolution: worksforme",
    "created_at": "2013-08-16T11:11:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2088",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2088#issuecomment-13485",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: worksforme
