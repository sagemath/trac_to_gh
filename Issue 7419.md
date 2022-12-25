# Issue 7419: implicit_plot ignores the z-range

archive/issues_007419.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  wcauchois\n\nThis does not produce half of a sphere:\n\n\n```\nimplicit_plot3d((x^2)/2+(y^2)/2+(z^2)/2,(x,-5,5),(y,-5,5),(z,\n0,5),contour=2)\n```\n\n\nThe problem and solution were found in http://groups.google.com/group/sage-support/browse_thread/thread/69efe89a6aa97473\n\nReported by Micah (I don't see a last name on the email post reporting this)\n\nIssue created by migration from https://trac.sagemath.org/ticket/7419\n\n",
    "created_at": "2009-11-09T17:44:29Z",
    "labels": [
        "component: graphics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.2.1",
    "title": "implicit_plot ignores the z-range",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7419",
    "user": "https://github.com/jasongrout"
}
```
Assignee: @williamstein

CC:  wcauchois

This does not produce half of a sphere:


```
implicit_plot3d((x^2)/2+(y^2)/2+(z^2)/2,(x,-5,5),(y,-5,5),(z,
0,5),contour=2)
```


The problem and solution were found in http://groups.google.com/group/sage-support/browse_thread/thread/69efe89a6aa97473

Reported by Micah (I don't see a last name on the email post reporting this)

Issue created by migration from https://trac.sagemath.org/ticket/7419





---

archive/issue_comments_062314.json:
```json
{
    "body": "Attachment [trac-7419-implicit-z-range.patch](tarball://root/attachments/some-uuid/ticket7419/trac-7419-implicit-z-range.patch) by @jasongrout created at 2009-11-09 17:47:53",
    "created_at": "2009-11-09T17:47:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7419",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7419#issuecomment-62314",
    "user": "https://github.com/jasongrout"
}
```

Attachment [trac-7419-implicit-z-range.patch](tarball://root/attachments/some-uuid/ticket7419/trac-7419-implicit-z-range.patch) by @jasongrout created at 2009-11-09 17:47:53



---

archive/issue_comments_062315.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-11-09T17:47:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7419",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7419#issuecomment-62315",
    "user": "https://github.com/jasongrout"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_062316.json:
```json
{
    "body": "This looks good.  I added a little extra explanation because the aspect_ratio needed to be set for the hemispheres to not look too weird.  I can't believe that little 1 was sitting there the whole time, wanting to be a 2!  Positive review, apply only reviewer patch.",
    "created_at": "2009-11-10T15:03:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7419",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7419#issuecomment-62316",
    "user": "https://github.com/kcrisman"
}
```

This looks good.  I added a little extra explanation because the aspect_ratio needed to be set for the hemispheres to not look too weird.  I can't believe that little 1 was sitting there the whole time, wanting to be a 2!  Positive review, apply only reviewer patch.



---

archive/issue_comments_062317.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-11-10T15:03:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7419",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7419#issuecomment-62317",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_062318.json:
```json
{
    "body": "Based on 4.2.1.alpha0, apply only this patch.",
    "created_at": "2009-11-10T15:03:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7419",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7419#issuecomment-62318",
    "user": "https://github.com/kcrisman"
}
```

Based on 4.2.1.alpha0, apply only this patch.



---

archive/issue_comments_062319.json:
```json
{
    "body": "Attachment [trac-7419-implicit-z-range-review.patch](tarball://root/attachments/some-uuid/ticket7419/trac-7419-implicit-z-range-review.patch) by @kcrisman created at 2009-11-10 15:04:02",
    "created_at": "2009-11-10T15:04:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7419",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7419#issuecomment-62319",
    "user": "https://github.com/kcrisman"
}
```

Attachment [trac-7419-implicit-z-range-review.patch](tarball://root/attachments/some-uuid/ticket7419/trac-7419-implicit-z-range-review.patch) by @kcrisman created at 2009-11-10 15:04:02



---

archive/issue_comments_062320.json:
```json
{
    "body": "This must have been a simple copy-pasting error on my part. I'm glad we caught it!",
    "created_at": "2009-11-10T19:42:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7419",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7419#issuecomment-62320",
    "user": "https://trac.sagemath.org/admin/accounts/users/wcauchois"
}
```

This must have been a simple copy-pasting error on my part. I'm glad we caught it!



---

archive/issue_comments_062321.json:
```json
{
    "body": "I'm pretty sure it's my fault from when I did the setup_eval_from_grid patch.",
    "created_at": "2009-11-10T20:03:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7419",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7419#issuecomment-62321",
    "user": "https://github.com/jasongrout"
}
```

I'm pretty sure it's my fault from when I did the setup_eval_from_grid patch.



---

archive/issue_comments_062322.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-11-12T06:46:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7419",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7419#issuecomment-62322",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed
