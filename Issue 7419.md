# Issue 7419: implicit_plot ignores the z-range

archive/issues_007419.json:
```json
{
    "body": "Assignee: was\n\nCC:  wcauchois\n\nThis does not produce half of a sphere:\n\n\n```\nimplicit_plot3d((x^2)/2+(y^2)/2+(z^2)/2,(x,-5,5),(y,-5,5),(z,\n0,5),contour=2)\n```\n\n\nThe problem and solution were found in http://groups.google.com/group/sage-support/browse_thread/thread/69efe89a6aa97473\n\nReported by Micah (I don't see a last name on the email post reporting this)\n\nIssue created by migration from https://trac.sagemath.org/ticket/7419\n\n",
    "created_at": "2009-11-09T17:44:29Z",
    "labels": [
        "graphics",
        "major",
        "bug"
    ],
    "title": "implicit_plot ignores the z-range",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7419",
    "user": "jason"
}
```
Assignee: was

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

archive/issue_comments_062429.json:
```json
{
    "body": "Attachment [trac-7419-implicit-z-range.patch](tarball://root/attachments/some-uuid/ticket7419/trac-7419-implicit-z-range.patch) by jason created at 2009-11-09 17:47:53",
    "created_at": "2009-11-09T17:47:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7419",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7419#issuecomment-62429",
    "user": "jason"
}
```

Attachment [trac-7419-implicit-z-range.patch](tarball://root/attachments/some-uuid/ticket7419/trac-7419-implicit-z-range.patch) by jason created at 2009-11-09 17:47:53



---

archive/issue_comments_062430.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-11-09T17:47:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7419",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7419#issuecomment-62430",
    "user": "jason"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_062431.json:
```json
{
    "body": "This looks good.  I added a little extra explanation because the aspect_ratio needed to be set for the hemispheres to not look too weird.  I can't believe that little 1 was sitting there the whole time, wanting to be a 2!  Positive review, apply only reviewer patch.",
    "created_at": "2009-11-10T15:03:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7419",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7419#issuecomment-62431",
    "user": "kcrisman"
}
```

This looks good.  I added a little extra explanation because the aspect_ratio needed to be set for the hemispheres to not look too weird.  I can't believe that little 1 was sitting there the whole time, wanting to be a 2!  Positive review, apply only reviewer patch.



---

archive/issue_comments_062432.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-11-10T15:03:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7419",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7419#issuecomment-62432",
    "user": "kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_062433.json:
```json
{
    "body": "Based on 4.2.1.alpha0, apply only this patch.",
    "created_at": "2009-11-10T15:03:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7419",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7419#issuecomment-62433",
    "user": "kcrisman"
}
```

Based on 4.2.1.alpha0, apply only this patch.



---

archive/issue_comments_062434.json:
```json
{
    "body": "Attachment [trac-7419-implicit-z-range-review.patch](tarball://root/attachments/some-uuid/ticket7419/trac-7419-implicit-z-range-review.patch) by kcrisman created at 2009-11-10 15:04:02",
    "created_at": "2009-11-10T15:04:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7419",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7419#issuecomment-62434",
    "user": "kcrisman"
}
```

Attachment [trac-7419-implicit-z-range-review.patch](tarball://root/attachments/some-uuid/ticket7419/trac-7419-implicit-z-range-review.patch) by kcrisman created at 2009-11-10 15:04:02



---

archive/issue_comments_062435.json:
```json
{
    "body": "This must have been a simple copy-pasting error on my part. I'm glad we caught it!",
    "created_at": "2009-11-10T19:42:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7419",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7419#issuecomment-62435",
    "user": "wcauchois"
}
```

This must have been a simple copy-pasting error on my part. I'm glad we caught it!



---

archive/issue_comments_062436.json:
```json
{
    "body": "I'm pretty sure it's my fault from when I did the setup_eval_from_grid patch.",
    "created_at": "2009-11-10T20:03:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7419",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7419#issuecomment-62436",
    "user": "jason"
}
```

I'm pretty sure it's my fault from when I did the setup_eval_from_grid patch.



---

archive/issue_comments_062437.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-11-12T06:46:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7419",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7419#issuecomment-62437",
    "user": "mhansen"
}
```

Resolution: fixed
