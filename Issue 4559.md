# Issue 4559: Merge commits from Jon Hanke's devel/sage/sage/quadratic_forms/genera/genus.py tree

archive/issues_004559.json:
```json
{
    "body": "Assignee: justin\n\nThere are a number of commits to devel/sage/sage/quadratic_forms/genera/genus.py\n\n```\nchangeset:   10632:8403d5ca95be\ntag:         tip\nuser:        Jonathan Hanke <jonhanke@gmail.com>\ndate:        Sun Nov 09 23:00:32 2008 -0800\nsummary:     Some changes to fix the segfault and add two interface routines.\n\nchangeset:   10628:05a3db2f6057\nuser:        Jonathan Hanke <jonhanke@gmail.com>\ndate:        Tue Apr 01 05:51:40 2008 +0200\nsummary:     Fixed signature name overloading bug in quadratic form genus routines, and also moved them to .pyx files.\n\nchangeset:   10626:dcad7b2c0a42\nuser:        Jonathan Hanke <jonhanke@gmail.com>\ndate:        Wed Mar 26 12:01:33 2008 +0100\nsummary:     Added a Hessian_matrix() routine for Quadratic forms, and added Nebe's correction of a typo in genus.py, and min\nor interface changes.\n\nchangeset:   10597:f220b913963e\nuser:        Jonathan Hanke <jonhanke@gmail.com>\ndate:        Mon Nov 12 23:17:00 2007 +0100\nsummary:     Added updated genus code from David Kohel and Gabrielle Nebe (received Sept 6th, 2007).\n\nchangeset:   10569:8fa815df5c0c\nuser:        Jonathan Hanke <jonhanke@gmail.com>\ndate:        Tue Sep 04 00:09:12 2007 +0200\nsummary:     Added simple interface to QuadraticForm for the genus routines in quadratic_form/genera.\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4559\n\n",
    "created_at": "2008-11-20T00:30:15Z",
    "labels": [
        "quadratic forms",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0.2",
    "title": "Merge commits from Jon Hanke's devel/sage/sage/quadratic_forms/genera/genus.py tree",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4559",
    "user": "mabshoff"
}
```
Assignee: justin

There are a number of commits to devel/sage/sage/quadratic_forms/genera/genus.py

```
changeset:   10632:8403d5ca95be
tag:         tip
user:        Jonathan Hanke <jonhanke@gmail.com>
date:        Sun Nov 09 23:00:32 2008 -0800
summary:     Some changes to fix the segfault and add two interface routines.

changeset:   10628:05a3db2f6057
user:        Jonathan Hanke <jonhanke@gmail.com>
date:        Tue Apr 01 05:51:40 2008 +0200
summary:     Fixed signature name overloading bug in quadratic form genus routines, and also moved them to .pyx files.

changeset:   10626:dcad7b2c0a42
user:        Jonathan Hanke <jonhanke@gmail.com>
date:        Wed Mar 26 12:01:33 2008 +0100
summary:     Added a Hessian_matrix() routine for Quadratic forms, and added Nebe's correction of a typo in genus.py, and min
or interface changes.

changeset:   10597:f220b913963e
user:        Jonathan Hanke <jonhanke@gmail.com>
date:        Mon Nov 12 23:17:00 2007 +0100
summary:     Added updated genus code from David Kohel and Gabrielle Nebe (received Sept 6th, 2007).

changeset:   10569:8fa815df5c0c
user:        Jonathan Hanke <jonhanke@gmail.com>
date:        Tue Sep 04 00:09:12 2007 +0200
summary:     Added simple interface to QuadraticForm for the genus routines in quadratic_form/genera.
```


Issue created by migration from https://trac.sagemath.org/ticket/4559





---

archive/issue_comments_034158.json:
```json
{
    "body": "This is fixed via #5954, isn't it?",
    "created_at": "2009-06-07T16:05:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4559",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4559#issuecomment-34158",
    "user": "davidloeffler"
}
```

This is fixed via #5954, isn't it?



---

archive/issue_comments_034159.json:
```json
{
    "body": "Verified as fixed in 4.0.2.rc0.",
    "created_at": "2009-06-15T15:52:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4559",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4559#issuecomment-34159",
    "user": "ncalexan"
}
```

Verified as fixed in 4.0.2.rc0.



---

archive/issue_comments_034160.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-06-15T15:52:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4559",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4559#issuecomment-34160",
    "user": "ncalexan"
}
```

Resolution: fixed
