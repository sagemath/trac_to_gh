# Issue 6573: fix docstring from #5651

archive/issues_006573.json:
```json
{
    "body": "Assignee: tba\n\nCC:  wcauchois davidloeffler\n\nThat rebased patch at #5651 contains doctrings that doesn't conform with conventions for formatting docstrings. In particular, in sage/plot/bar_chart.py:\n\n```\n131\t    Extra options will get passed on to show(), as long as they are valid:\n```\n\nIn sage/plot/bezier_path.py:\n\n```\n171\t    Extra options will get passed on to show(), as long as they are valid:\n```\n\nIn sage/plot/matrix_plot.py:\n\n```\n58\t    Extra options will get passed on to show(), as long as they are valid:\n62\t    Extra options will get passed on to show(), as long as they are valid:\n```\n\nIn sage/plot/polygon.py:\n\n```\n255\t    Extra options will get passed on to show(), as long as they are valid:\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6573\n\n",
    "created_at": "2009-07-20T20:55:23Z",
    "labels": [
        "documentation",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.1",
    "title": "fix docstring from #5651",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6573",
    "user": "mvngu"
}
```
Assignee: tba

CC:  wcauchois davidloeffler

That rebased patch at #5651 contains doctrings that doesn't conform with conventions for formatting docstrings. In particular, in sage/plot/bar_chart.py:

```
131	    Extra options will get passed on to show(), as long as they are valid:
```

In sage/plot/bezier_path.py:

```
171	    Extra options will get passed on to show(), as long as they are valid:
```

In sage/plot/matrix_plot.py:

```
58	    Extra options will get passed on to show(), as long as they are valid:
62	    Extra options will get passed on to show(), as long as they are valid:
```

In sage/plot/polygon.py:

```
255	    Extra options will get passed on to show(), as long as they are valid:
```


Issue created by migration from https://trac.sagemath.org/ticket/6573





---

archive/issue_comments_053676.json:
```json
{
    "body": "based on Sage 4.1.1.alpha0",
    "created_at": "2009-07-21T14:26:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6573",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6573#issuecomment-53676",
    "user": "mvngu"
}
```

based on Sage 4.1.1.alpha0



---

archive/issue_comments_053677.json:
```json
{
    "body": "Attachment [trac_6573-docstring-fix.patch](tarball://root/attachments/some-uuid/ticket6573/trac_6573-docstring-fix.patch) by mvngu created at 2009-07-21 14:28:47\n\nDavid: Can I ask you to review this?",
    "created_at": "2009-07-21T14:28:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6573",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6573#issuecomment-53677",
    "user": "mvngu"
}
```

Attachment [trac_6573-docstring-fix.patch](tarball://root/attachments/some-uuid/ticket6573/trac_6573-docstring-fix.patch) by mvngu created at 2009-07-21 14:28:47

David: Can I ask you to review this?



---

archive/issue_comments_053678.json:
```json
{
    "body": "Attachment [trac_6573-review.patch](tarball://root/attachments/some-uuid/ticket6573/trac_6573-review.patch) by davidloeffler created at 2009-07-21 14:59:11",
    "created_at": "2009-07-21T14:59:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6573",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6573#issuecomment-53678",
    "user": "davidloeffler"
}
```

Attachment [trac_6573-review.patch](tarball://root/attachments/some-uuid/ticket6573/trac_6573-review.patch) by davidloeffler created at 2009-07-21 14:59:11



---

archive/issue_comments_053679.json:
```json
{
    "body": "Looks fine to me; but it looks like the Bezier paths module isn't in the reference manual. I've uploaded a tiny patch that fixes this.",
    "created_at": "2009-07-21T15:01:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6573",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6573#issuecomment-53679",
    "user": "davidloeffler"
}
```

Looks fine to me; but it looks like the Bezier paths module isn't in the reference manual. I've uploaded a tiny patch that fixes this.



---

archive/issue_comments_053680.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-07-23T05:09:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6573",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6573#issuecomment-53680",
    "user": "mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_053681.json:
```json
{
    "body": "Merged both patches.",
    "created_at": "2009-07-23T05:09:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6573",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6573#issuecomment-53681",
    "user": "mvngu"
}
```

Merged both patches.
