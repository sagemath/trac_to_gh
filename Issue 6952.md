# Issue 6952: follow-up to #6774: fix warnings and stylistic niceties

archive/issues_006952.json:
```json
{
    "body": "Assignee: tba\n\nCC:  @nathanncohen @jasongrout\n\nThis is a follow-up to ticket #6774.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6952\n\n",
    "created_at": "2009-09-17T23:02:29Z",
    "labels": [
        "component: documentation"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.2",
    "title": "follow-up to #6774: fix warnings and stylistic niceties",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6952",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```
Assignee: tba

CC:  @nathanncohen @jasongrout

This is a follow-up to ticket #6774.

Issue created by migration from https://trac.sagemath.org/ticket/6952





---

archive/issue_comments_057383.json:
```json
{
    "body": "There's a warning when building the tutorial with the two patches at #6774:\n\n```\nWARNING: /scratch/mvngu/release/sage-4.1.2.alpha1/devel/sage-main/doc/en/tutorial/tour_graphtheory.rst:91: (WARNING/2) Title underline too short.\n\nCompute maximum matchings\n^^^^^^^^^^^^^^^^^^^\n```\n\nThere are also some stylistic errors that I'll take care of.",
    "created_at": "2009-09-17T23:04:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6952",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6952#issuecomment-57383",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

There's a warning when building the tutorial with the two patches at #6774:

```
WARNING: /scratch/mvngu/release/sage-4.1.2.alpha1/devel/sage-main/doc/en/tutorial/tour_graphtheory.rst:91: (WARNING/2) Title underline too short.

Compute maximum matchings
^^^^^^^^^^^^^^^^^^^
```

There are also some stylistic errors that I'll take care of.



---

archive/issue_comments_057384.json:
```json
{
    "body": "Attachment [trac_6952-typo-fixes.patch](tarball://root/attachments/some-uuid/ticket6952/trac_6952-typo-fixes.patch) by mvngu created at 2009-09-17 23:57:21\n\ndepends on #6774",
    "created_at": "2009-09-17T23:57:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6952",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6952#issuecomment-57384",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Attachment [trac_6952-typo-fixes.patch](tarball://root/attachments/some-uuid/ticket6952/trac_6952-typo-fixes.patch) by mvngu created at 2009-09-17 23:57:21

depends on #6774



---

archive/issue_comments_057385.json:
```json
{
    "body": "Changing priority from major to minor.",
    "created_at": "2009-09-17T23:58:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6952",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6952#issuecomment-57385",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Changing priority from major to minor.



---

archive/issue_comments_057386.json:
```json
{
    "body": "Thanks! I learned a few things about writing in ReST from your patch.  I won't make those mistakes again (like enumerated lists).\n\nThis applied and looks fine.\n\nI assume you merged the necessary patches to make the functions in these examples work.  They did not work for me with a copy of 4.1.1.alpha1.  So doctests really ought to be run on this file just to make sure that the examples are correct.",
    "created_at": "2009-09-19T02:57:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6952",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6952#issuecomment-57386",
    "user": "https://github.com/jasongrout"
}
```

Thanks! I learned a few things about writing in ReST from your patch.  I won't make those mistakes again (like enumerated lists).

This applied and looks fine.

I assume you merged the necessary patches to make the functions in these examples work.  They did not work for me with a copy of 4.1.1.alpha1.  So doctests really ought to be run on this file just to make sure that the examples are correct.



---

archive/issue_comments_057387.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-09-19T19:34:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6952",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6952#issuecomment-57387",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_057388.json:
```json
{
    "body": "Replying to [comment:3 jason]:\n> I assume you merged the necessary patches to make the functions in these examples work. \nYes, I tried that.\n\n\n\n\n> So doctests really ought to be run on this file just to make sure that the examples are correct.\nWith other dependencies and this patch, all doctests in the tutorial pass.",
    "created_at": "2009-09-19T19:34:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6952",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6952#issuecomment-57388",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Replying to [comment:3 jason]:
> I assume you merged the necessary patches to make the functions in these examples work. 
Yes, I tried that.




> So doctests really ought to be run on this file just to make sure that the examples are correct.
With other dependencies and this patch, all doctests in the tutorial pass.



---

archive/issue_events_007176.json:
```json
{
    "actor": "mvngu",
    "created_at": "2009-09-19T19:34:08Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6952",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6952#event-7176"
}
```
