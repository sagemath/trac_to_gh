# Issue 9066: Improve documentation in shapes2.py

archive/issues_009066.json:
```json
{
    "body": "Assignee: mvngu\n\nCC:  jason mvngu robertwb\n\nplot.plot3d.shapes2.py was a mess, including having several weird helper functions that didn't really need doctests, such as\n\n```\n    def avg(a,b):\n        return (a+b)/2.0\n```\n\nThis cleans up the situation here.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9066\n\n",
    "created_at": "2010-05-27T15:03:33Z",
    "labels": [
        "documentation",
        "minor",
        "enhancement"
    ],
    "title": "Improve documentation in shapes2.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9066",
    "user": "kcrisman"
}
```
Assignee: mvngu

CC:  jason mvngu robertwb

plot.plot3d.shapes2.py was a mess, including having several weird helper functions that didn't really need doctests, such as

```
    def avg(a,b):
        return (a+b)/2.0
```

This cleans up the situation here.

Issue created by migration from https://trac.sagemath.org/ticket/9066





---

archive/issue_comments_084130.json:
```json
{
    "body": "Attachment [trac_9066-shapes2-doc.patch](tarball://root/attachments/some-uuid/ticket9066/trac_9066-shapes2-doc.patch) by kcrisman created at 2010-05-27 15:10:46\n\nBased on 4.4.2",
    "created_at": "2010-05-27T15:10:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9066",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9066#issuecomment-84130",
    "user": "kcrisman"
}
```

Attachment [trac_9066-shapes2-doc.patch](tarball://root/attachments/some-uuid/ticket9066/trac_9066-shapes2-doc.patch) by kcrisman created at 2010-05-27 15:10:46

Based on 4.4.2



---

archive/issue_comments_084131.json:
```json
{
    "body": "This also improves the copyright situation, for which reason I have added robertwb and was to this, in case they have any emendations to it.  I figured they were mostly responsible, though :)\n\nAlso, I'm not sure what purpose the ruler functions serve.  They were never documented before, and do not show up anywhere else in the HG repository than in this file!  So one could remove them if they were intended for something else that is now handled elsewhere; either way is fine.",
    "created_at": "2010-05-27T15:13:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9066",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9066#issuecomment-84131",
    "user": "kcrisman"
}
```

This also improves the copyright situation, for which reason I have added robertwb and was to this, in case they have any emendations to it.  I figured they were mostly responsible, though :)

Also, I'm not sure what purpose the ruler functions serve.  They were never documented before, and do not show up anywhere else in the HG repository than in this file!  So one could remove them if they were intended for something else that is now handled elsewhere; either way is fine.



---

archive/issue_comments_084132.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-05-27T15:13:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9066",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9066#issuecomment-84132",
    "user": "kcrisman"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_084133.json:
```json
{
    "body": "Attachment [trac_9066-reviewer.patch](tarball://root/attachments/some-uuid/ticket9066/trac_9066-reviewer.patch) by mvngu created at 2010-06-15 01:46:02",
    "created_at": "2010-06-15T01:46:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9066",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9066#issuecomment-84133",
    "user": "mvngu"
}
```

Attachment [trac_9066-reviewer.patch](tarball://root/attachments/some-uuid/ticket9066/trac_9066-reviewer.patch) by mvngu created at 2010-06-15 01:46:02



---

archive/issue_comments_084134.json:
```json
{
    "body": "I'm OK with kcrisman's patch, except for a few points which I have added in my reviewer patch. Changes in the reviewer patch include:\n\n* Use the new style of raising exceptions, e.g. use `TypeError` as if it's a function, not a statement. This new style is more consistent with Python 3.x. When it comes time to switch to using Python 3.x, there would be less work involved in making the transition to Python 3.x.\n* Put exception tests into a `TESTS` block.\n* Fix up docstring in `bezier3d` so it renders nicely in the reference manual.\n* Some miscellaneous typo fixes.\n\nIf my patch gets a positive review, the whole ticket is good to go.",
    "created_at": "2010-06-15T01:50:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9066",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9066#issuecomment-84134",
    "user": "mvngu"
}
```

I'm OK with kcrisman's patch, except for a few points which I have added in my reviewer patch. Changes in the reviewer patch include:

* Use the new style of raising exceptions, e.g. use `TypeError` as if it's a function, not a statement. This new style is more consistent with Python 3.x. When it comes time to switch to using Python 3.x, there would be less work involved in making the transition to Python 3.x.
* Put exception tests into a `TESTS` block.
* Fix up docstring in `bezier3d` so it renders nicely in the reference manual.
* Some miscellaneous typo fixes.

If my patch gets a positive review, the whole ticket is good to go.



---

archive/issue_comments_084135.json:
```json
{
    "body": ">  * Use the new style of raising exceptions, e.g. use `TypeError` as if it's a function, not a statement. This new style is more consistent with Python 3.x. When it comes time to switch to using Python 3.x, there would be less work involved in making the transition to Python 3.x.\nOkay, as long as this still works in Python 2.6 or whatever.\n>  * Put exception tests into a `TESTS` block.\nOk.\n>  * Fix up docstring in `bezier3d` so it renders nicely in the reference manual.\nI'm a minimalist about this sort of thing, as you know :)\n>  * Some miscellaneous typo fixes.\nSo did we say `3-D` and not `3D`?  I purposely put `3D` because I thought that was the default... I never know.",
    "created_at": "2010-06-15T13:21:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9066",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9066#issuecomment-84135",
    "user": "kcrisman"
}
```

>  * Use the new style of raising exceptions, e.g. use `TypeError` as if it's a function, not a statement. This new style is more consistent with Python 3.x. When it comes time to switch to using Python 3.x, there would be less work involved in making the transition to Python 3.x.
Okay, as long as this still works in Python 2.6 or whatever.
>  * Put exception tests into a `TESTS` block.
Ok.
>  * Fix up docstring in `bezier3d` so it renders nicely in the reference manual.
I'm a minimalist about this sort of thing, as you know :)
>  * Some miscellaneous typo fixes.
So did we say `3-D` and not `3D`?  I purposely put `3D` because I thought that was the default... I never know.



---

archive/issue_comments_084136.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-06-15T13:32:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9066",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9066#issuecomment-84136",
    "user": "kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_084137.json:
```json
{
    "body": "Docs look nice when built, passes tests.  Let's get this in!",
    "created_at": "2010-06-15T13:32:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9066",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9066#issuecomment-84137",
    "user": "kcrisman"
}
```

Docs look nice when built, passes tests.  Let's get this in!



---

archive/issue_comments_084138.json:
```json
{
    "body": "This patch and #9088 seem to conflict -- if I apply both, I get a doctest failure:\n\n```\nsage -t  \"devel/sage-reviewing/sage/plot/plot3d/shapes2.py\"\n**********************************************************************\nFile \"/storage/masiao/sage-4.5.alpha1/devel/sage-reviewing/sage/plot/plot3d/shapes2.py\", line 700:\n    sage: P.tachyon_repr(P.default_render_params())\nExpected:\n    'Sphere center 1.0 2.0 3.0 Rad 0.015 texture84'\nGot:\n    'Sphere center 1.0 2.0 3.0 Rad 0.015 texture85'\n**********************************************************************\nFile \"/storage/masiao/sage-4.5.alpha1/devel/sage-reviewing/sage/plot/plot3d/shapes2.py\", line 717:\n    sage: P.obj_repr(P.default_render_params())[0][0:2]\nExpected:\n    ['g obj_1', 'usemtl texture86']\nGot:\n    ['g obj_1', 'usemtl texture87']\n**********************************************************************\nFile \"/storage/masiao/sage-4.5.alpha1/devel/sage-reviewing/sage/plot/plot3d/shapes2.py\", line 825:\n    sage: L.tachyon_repr(L.default_render_params())[0]\nExpected:\n    'FCylinder base 1.0 0.0 0.0 apex 0.999950000417 0.00999983333417 0.0001 rad 0.005 texture126'\nGot:\n    'FCylinder base 1.0 0.0 0.0 apex 0.999950000417 0.00999983333417 0.0001 rad 0.005 texture127'\n**********************************************************************\n3 items had failures:\n   1 of   4 in __main__.example_13\n   1 of   4 in __main__.example_14\n   1 of   4 in __main__.example_19\n***Test Failed*** 3 failures.\n```\n\n\nThis doesn't come up if I apply either one of the patches on its own.",
    "created_at": "2010-07-01T09:03:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9066",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9066#issuecomment-84138",
    "user": "davidloeffler"
}
```

This patch and #9088 seem to conflict -- if I apply both, I get a doctest failure:

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

archive/issue_comments_084139.json:
```json
{
    "body": "I'm not exactly sure how the texture numbers get decided, but I think there is some linear order involved with their names.  Anyway, this is easy enough to fix.  We should definitely apply this one first because it is much more annoying, and then it would be very simple to add a reviewer patch to #9088 to fix these trivialities.",
    "created_at": "2010-07-01T13:46:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9066",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9066#issuecomment-84139",
    "user": "kcrisman"
}
```

I'm not exactly sure how the texture numbers get decided, but I think there is some linear order involved with their names.  Anyway, this is easy enough to fix.  We should definitely apply this one first because it is much more annoying, and then it would be very simple to add a reviewer patch to #9088 to fix these trivialities.



---

archive/issue_comments_084140.json:
```json
{
    "body": "Replying to [comment:6 kcrisman]:\n>  We should definitely apply this one first because it is much more annoying, and then it would be very simple to add a reviewer patch to #9088 to fix these trivialities.\n\nOops, it's now too late for that. Applying these patches to 4.5.2.alpha0, I get the doctest errors mentioned above. We've already merged #9088, so we'll need to fix the problem here.",
    "created_at": "2010-07-22T07:44:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9066",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9066#issuecomment-84140",
    "user": "ddrake"
}
```

Replying to [comment:6 kcrisman]:
>  We should definitely apply this one first because it is much more annoying, and then it would be very simple to add a reviewer patch to #9088 to fix these trivialities.

Oops, it's now too late for that. Applying these patches to 4.5.2.alpha0, I get the doctest errors mentioned above. We've already merged #9088, so we'll need to fix the problem here.



---

archive/issue_comments_084141.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-07-22T07:44:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9066",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9066#issuecomment-84141",
    "user": "ddrake"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_084142.json:
```json
{
    "body": "Unfortunately I am not a queueing expert, so in order to fix this I will have to add yet another doctest fix patch.  Is that okay with the release managers?",
    "created_at": "2010-07-22T12:39:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9066",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9066#issuecomment-84142",
    "user": "kcrisman"
}
```

Unfortunately I am not a queueing expert, so in order to fix this I will have to add yet another doctest fix patch.  Is that okay with the release managers?



---

archive/issue_comments_084143.json:
```json
{
    "body": "Replying to [comment:8 kcrisman]:\n> Unfortunately I am not a queueing expert, so in order to fix this I will have to add yet another doctest fix patch.  Is that okay with the release managers?\n\nThat's no problem at all.",
    "created_at": "2010-07-22T13:05:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9066",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9066#issuecomment-84143",
    "user": "ddrake"
}
```

Replying to [comment:8 kcrisman]:
> Unfortunately I am not a queueing expert, so in order to fix this I will have to add yet another doctest fix patch.  Is that okay with the release managers?

That's no problem at all.



---

archive/issue_comments_084144.json:
```json
{
    "body": "Attachment [trac_9066-doctest-fix.patch](tarball://root/attachments/some-uuid/ticket9066/trac_9066-doctest-fix.patch) by kcrisman created at 2010-07-22 13:30:38\n\nApply this last.",
    "created_at": "2010-07-22T13:30:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9066",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9066#issuecomment-84144",
    "user": "kcrisman"
}
```

Attachment [trac_9066-doctest-fix.patch](tarball://root/attachments/some-uuid/ticket9066/trac_9066-doctest-fix.patch) by kcrisman created at 2010-07-22 13:30:38

Apply this last.



---

archive/issue_comments_084145.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-07-22T13:32:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9066",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9066#issuecomment-84145",
    "user": "kcrisman"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_084146.json:
```json
{
    "body": "This should do it.  Hopefully a release manager can very easily review this.  Apply in order doc, reviewer, then doctest-fix.",
    "created_at": "2010-07-22T13:32:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9066",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9066#issuecomment-84146",
    "user": "kcrisman"
}
```

This should do it.  Hopefully a release manager can very easily review this.  Apply in order doc, reviewer, then doctest-fix.



---

archive/issue_comments_084147.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-07-23T00:10:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9066",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9066#issuecomment-84147",
    "user": "ddrake"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_084148.json:
```json
{
    "body": "Replying to [comment:10 kcrisman]:\n> This should do it.  Hopefully a release manager can very easily review this.  Apply in order doc, reviewer, then doctest-fix.\n\nLooks good.",
    "created_at": "2010-07-23T00:10:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9066",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9066#issuecomment-84148",
    "user": "ddrake"
}
```

Replying to [comment:10 kcrisman]:
> This should do it.  Hopefully a release manager can very easily review this.  Apply in order doc, reviewer, then doctest-fix.

Looks good.



---

archive/issue_comments_084149.json:
```json
{
    "body": "Merged all three patches in 4.5.2.alpha1.",
    "created_at": "2010-07-23T00:10:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9066",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9066#issuecomment-84149",
    "user": "ddrake"
}
```

Merged all three patches in 4.5.2.alpha1.



---

archive/issue_comments_084150.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-07-23T00:10:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9066",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9066#issuecomment-84150",
    "user": "ddrake"
}
```

Resolution: fixed
