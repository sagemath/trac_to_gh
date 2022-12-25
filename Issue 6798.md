# Issue 6798: fix doctest timeout in modules/vector_double_dense.pyx

archive/issues_006798.json:
```json
{
    "body": "Assignee: tbd\n\nOn Solaris 10 update 7 (SPARC), the following tests timed out. Both ECL and Maxima were updated - ECL version 9.8.4 (see trac #6564); Maxima version 5.19.1 (see trac #6699). Updated spkgs can be found here. I'm not sure if this is new or not since updating Maxima + ECL, so it may or may not be related to that. \n\nhttp://sage.math.washington.edu/home/kirkby/Solaris-fixes/ecl-9.8.4/\n\nhttp://sage.math.washington.edu/home/kirkby/Solaris-fixes/maxima-5.19.1/\n\n\n```\n\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nThu Aug 20 20:02:37 BST 2009\ndsage-trial tmp directory doesn't exist - creating ...\nThis script will run the unit tests for DSage\n```\n\n| Sage Version 4.1.1, Release Date: 2009-08-14                       |\n| Type notebook() for the GUI, and license() for information.        |\n<SNIP>\n\n```\nsage -t  \"devel/sage/sage/modules/vector_double_dense.pyx\"\n         [71.4 s]\n\nsage -t  \"devel/sage/sage/lfunctions/sympow.py\"\n*** *** Error: TIMED OUT! PROCESS KILLED! *** ***\n*** *** Error: TIMED OUT! *** ***\n*** *** Error: TIMED OUT! *** ***\n         [361.1 s]\nsage -t  \"devel/sage/sage/lfunctions/all.py\"\n         [1.2 s]\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6798\n\n",
    "created_at": "2009-08-21T08:16:12Z",
    "labels": [
        "component: algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "fix doctest timeout in modules/vector_double_dense.pyx",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6798",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```
Assignee: tbd

On Solaris 10 update 7 (SPARC), the following tests timed out. Both ECL and Maxima were updated - ECL version 9.8.4 (see trac #6564); Maxima version 5.19.1 (see trac #6699). Updated spkgs can be found here. I'm not sure if this is new or not since updating Maxima + ECL, so it may or may not be related to that. 

http://sage.math.washington.edu/home/kirkby/Solaris-fixes/ecl-9.8.4/

http://sage.math.washington.edu/home/kirkby/Solaris-fixes/maxima-5.19.1/


```

----------------------------------------------------------------------
----------------------------------------------------------------------
Thu Aug 20 20:02:37 BST 2009
dsage-trial tmp directory doesn't exist - creating ...
This script will run the unit tests for DSage
```

| Sage Version 4.1.1, Release Date: 2009-08-14                       |
| Type notebook() for the GUI, and license() for information.        |
<SNIP>

```
sage -t  "devel/sage/sage/modules/vector_double_dense.pyx"
         [71.4 s]

sage -t  "devel/sage/sage/lfunctions/sympow.py"
*** *** Error: TIMED OUT! PROCESS KILLED! *** ***
*** *** Error: TIMED OUT! *** ***
*** *** Error: TIMED OUT! *** ***
         [361.1 s]
sage -t  "devel/sage/sage/lfunctions/all.py"
         [1.2 s]
```



Issue created by migration from https://trac.sagemath.org/ticket/6798





---

archive/issue_comments_055885.json:
```json
{
    "body": "Changing component from algebra to solaris.",
    "created_at": "2009-11-09T14:05:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6798",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6798#issuecomment-55885",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing component from algebra to solaris.



---

archive/issue_events_016012.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6798",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6798#event-16012"
}
```



---

archive/issue_comments_055886.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2013-12-02T20:52:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6798",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6798#issuecomment-55886",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from new to needs_review.



---

archive/issue_events_016013.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-12-02T20:52:09Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6798",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6798#event-16013"
}
```



---

archive/issue_events_016014.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-12-02T20:52:09Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6798",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6798#event-16014"
}
```



---

archive/issue_comments_055887.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2013-12-02T20:52:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6798",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6798#issuecomment-55887",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_016015.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-12-05T08:07:53Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6798",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6798#event-16015"
}
```



---

archive/issue_comments_055888.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2013-12-05T08:07:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6798",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6798#issuecomment-55888",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: invalid
