# Issue 9088: line3d does not take a tuple of points

archive/issues_009088.json:
```json
{
    "body": "Assignee: jason, was\n\nCC:  @kcrisman mhampton\n\nRight now, this fails:\n\n```\nline3d(( (0,0,0), (1,2,3) ))\n```\n\nsince the copy of the input data is not converted to a list.  This is an easy fix.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9088\n\n",
    "created_at": "2010-05-29T19:47:00Z",
    "labels": [
        "component: graphics",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5.2",
    "title": "line3d does not take a tuple of points",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9088",
    "user": "https://github.com/jasongrout"
}
```
Assignee: jason, was

CC:  @kcrisman mhampton

Right now, this fails:

```
line3d(( (0,0,0), (1,2,3) ))
```

since the copy of the input data is not converted to a list.  This is an easy fix.

Issue created by migration from https://trac.sagemath.org/ticket/9088





---

archive/issue_comments_084261.json:
```json
{
    "body": "Attachment [trac-9088-line3d-list-copy.2.patch](tarball://root/attachments/some-uuid/ticket9088/trac-9088-line3d-list-copy.2.patch) by @jasongrout created at 2010-05-29 19:52:11",
    "created_at": "2010-05-29T19:52:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9088",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9088#issuecomment-84261",
    "user": "https://github.com/jasongrout"
}
```

Attachment [trac-9088-line3d-list-copy.2.patch](tarball://root/attachments/some-uuid/ticket9088/trac-9088-line3d-list-copy.2.patch) by @jasongrout created at 2010-05-29 19:52:11



---

archive/issue_comments_084262.json:
```json
{
    "body": "Fix attached.  This should be a trivial review!",
    "created_at": "2010-05-29T19:53:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9088",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9088#issuecomment-84262",
    "user": "https://github.com/jasongrout"
}
```

Fix attached.  This should be a trivial review!



---

archive/issue_comments_084263.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-05-29T19:53:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9088",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9088#issuecomment-84263",
    "user": "https://github.com/jasongrout"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_084264.json:
```json
{
    "body": "Positive review.",
    "created_at": "2010-06-18T18:44:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9088",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9088#issuecomment-84264",
    "user": "https://github.com/kcrisman"
}
```

Positive review.



---

archive/issue_comments_084265.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-06-18T18:44:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9088",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9088#issuecomment-84265",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_084266.json:
```json
{
    "body": "This patch and #9066 seem to conflict -- if I apply both, I get a doctest failure:\n\n```\nsage -t  \"devel/sage-reviewing/sage/plot/plot3d/shapes2.py\"\n**********************************************************************\nFile \"/storage/masiao/sage-4.5.alpha1/devel/sage-reviewing/sage/plot/plot3d/shapes2.py\", line 700:\n    sage: P.tachyon_repr(P.default_render_params())\nExpected:\n    'Sphere center 1.0 2.0 3.0 Rad 0.015 texture84'\nGot:\n    'Sphere center 1.0 2.0 3.0 Rad 0.015 texture85'\n**********************************************************************\nFile \"/storage/masiao/sage-4.5.alpha1/devel/sage-reviewing/sage/plot/plot3d/shapes2.py\", line 717:\n    sage: P.obj_repr(P.default_render_params())[0][0:2]\nExpected:\n    ['g obj_1', 'usemtl texture86']\nGot:\n    ['g obj_1', 'usemtl texture87']\n**********************************************************************\nFile \"/storage/masiao/sage-4.5.alpha1/devel/sage-reviewing/sage/plot/plot3d/shapes2.py\", line 825:\n    sage: L.tachyon_repr(L.default_render_params())[0]\nExpected:\n    'FCylinder base 1.0 0.0 0.0 apex 0.999950000417 0.00999983333417 0.0001 rad 0.005 texture126'\nGot:\n    'FCylinder base 1.0 0.0 0.0 apex 0.999950000417 0.00999983333417 0.0001 rad 0.005 texture127'\n**********************************************************************\n3 items had failures:\n   1 of   4 in __main__.example_13\n   1 of   4 in __main__.example_14\n   1 of   4 in __main__.example_19\n***Test Failed*** 3 failures.\n```\n\nThis doesn't come up if I apply either one of the patches on its own.",
    "created_at": "2010-07-01T09:03:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9088",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9088#issuecomment-84266",
    "user": "https://github.com/loefflerd"
}
```

This patch and #9066 seem to conflict -- if I apply both, I get a doctest failure:

```
sage -t  "devel/sage-reviewing/sage/plot/plot3d/shapes2.py"
**********************************************************************
File "/storage/masiao/sage-4.5.alpha1/devel/sage-reviewing/sage/plot/plot3d/shapes2.py", line 700:
    sage: P.tachyon_repr(P.default_render_params())
Expected:
    'Sphere center 1.0 2.0 3.0 Rad 0.015 texture84'
Got:
    'Sphere center 1.0 2.0 3.0 Rad 0.015 texture85'
**********************************************************************
File "/storage/masiao/sage-4.5.alpha1/devel/sage-reviewing/sage/plot/plot3d/shapes2.py", line 717:
    sage: P.obj_repr(P.default_render_params())[0][0:2]
Expected:
    ['g obj_1', 'usemtl texture86']
Got:
    ['g obj_1', 'usemtl texture87']
**********************************************************************
File "/storage/masiao/sage-4.5.alpha1/devel/sage-reviewing/sage/plot/plot3d/shapes2.py", line 825:
    sage: L.tachyon_repr(L.default_render_params())[0]
Expected:
    'FCylinder base 1.0 0.0 0.0 apex 0.999950000417 0.00999983333417 0.0001 rad 0.005 texture126'
Got:
    'FCylinder base 1.0 0.0 0.0 apex 0.999950000417 0.00999983333417 0.0001 rad 0.005 texture127'
**********************************************************************
3 items had failures:
   1 of   4 in __main__.example_13
   1 of   4 in __main__.example_14
   1 of   4 in __main__.example_19
***Test Failed*** 3 failures.
```

This doesn't come up if I apply either one of the patches on its own.



---

archive/issue_comments_084267.json:
```json
{
    "body": "I'm not exactly sure how the texture numbers get decided, but I think there is some linear order involved with their names.  Anyway, this is easy enough to fix.  We should definitely apply #9088 first because it is much more annoying, and then it would be very simple to add a reviewer patch to fix these trivialities.\n\nI'll leave this as positive review until the release manager decides what order to merge these in, though - wouldn't want to overstep his prerogative :)  then he can mark whichever one needs work thus.",
    "created_at": "2010-07-01T13:47:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9088",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9088#issuecomment-84267",
    "user": "https://github.com/kcrisman"
}
```

I'm not exactly sure how the texture numbers get decided, but I think there is some linear order involved with their names.  Anyway, this is easy enough to fix.  We should definitely apply #9088 first because it is much more annoying, and then it would be very simple to add a reviewer patch to fix these trivialities.

I'll leave this as positive review until the release manager decides what order to merge these in, though - wouldn't want to overstep his prerogative :)  then he can mark whichever one needs work thus.



---

archive/issue_events_022288.json:
```json
{
    "actor": "https://github.com/qed777",
    "created_at": "2010-07-20T10:12:39Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9088",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9088#event-22288"
}
```



---

archive/issue_comments_084268.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-07-20T10:12:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9088",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9088#issuecomment-84268",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed
