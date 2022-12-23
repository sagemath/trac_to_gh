# Issue 9484: add demos for implicit_plot3d that show how to do CSG (constructive solid geometry)

archive/issues_009484.json:
```json
{
    "body": "Assignee: cwitty\n\nSee http://groups.google.com/group/sage-support/browse_thread/thread/e05229d90733c78d for an example of how to do CSG (intersections and unions of solid objects) with implicit_plot3d; I think the given example:\n\n```\nsage: var('x,y,z')\n(x, y, z)\nsage: implicit_plot3d(max_symbolic(min_symbolic(x*x+y*y-1, x*x+z*z-2), x-1.8, y-1.8, z-1.8, -x-1.8, -y-1.8, -z-1.8), (x, -2, 2), (y, -2, 2), (z, -2, 2), smooth=False)\n```\n\n(along with some explanation) should be added to the implicit_plot3d docstring.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9484\n\n",
    "created_at": "2010-07-12T17:34:19Z",
    "labels": [
        "graphics",
        "minor",
        "enhancement"
    ],
    "title": "add demos for implicit_plot3d that show how to do CSG (constructive solid geometry)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9484",
    "user": "cwitty"
}
```
Assignee: cwitty

See http://groups.google.com/group/sage-support/browse_thread/thread/e05229d90733c78d for an example of how to do CSG (intersections and unions of solid objects) with implicit_plot3d; I think the given example:

```
sage: var('x,y,z')
(x, y, z)
sage: implicit_plot3d(max_symbolic(min_symbolic(x*x+y*y-1, x*x+z*z-2), x-1.8, y-1.8, z-1.8, -x-1.8, -y-1.8, -z-1.8), (x, -2, 2), (y, -2, 2), (z, -2, 2), smooth=False)
```

(along with some explanation) should be added to the implicit_plot3d docstring.

Issue created by migration from https://trac.sagemath.org/ticket/9484





---

archive/issue_comments_091059.json:
```json
{
    "body": "Attachment\n\nI picked a slightly different example.",
    "created_at": "2010-07-18T02:54:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9484",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9484#issuecomment-91059",
    "user": "cwitty"
}
```

Attachment

I picked a slightly different example.



---

archive/issue_comments_091060.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-07-18T02:54:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9484",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9484#issuecomment-91060",
    "user": "cwitty"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_091061.json:
```json
{
    "body": "Probably depends on #9482 and #9483.",
    "created_at": "2010-08-05T20:46:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9484",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9484#issuecomment-91061",
    "user": "kcrisman"
}
```

Probably depends on #9482 and #9483.



---

archive/issue_comments_091062.json:
```json
{
    "body": "After #9483, I go from error message to no error message with this example as expected.  Can't test the actual view for some reason :(",
    "created_at": "2010-08-06T01:27:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9484",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9484#issuecomment-91062",
    "user": "kcrisman"
}
```

After #9483, I go from error message to no error message with this example as expected.  Can't test the actual view for some reason :(



---

archive/issue_comments_091063.json:
```json
{
    "body": "I apologize for not marking the dependency in my comment.\n\nBy the way, you could see a version of the plot by adding a viewer='tachyon' keyword argument to the implicit_plot3d call.",
    "created_at": "2010-08-06T02:45:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9484",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9484#issuecomment-91063",
    "user": "cwitty"
}
```

I apologize for not marking the dependency in my comment.

By the way, you could see a version of the plot by adding a viewer='tachyon' keyword argument to the implicit_plot3d call.



---

archive/issue_comments_091064.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-08-06T14:18:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9484",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9484#issuecomment-91064",
    "user": "kcrisman"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_091065.json:
```json
{
    "body": "This looks fine, except probably one should put commands like `implicit_plot3d` in double ticks like ```implicit_plot3d```, or in that case you might even be able to use `:meth:` or something like that.  Very interesting example!",
    "created_at": "2010-08-06T14:18:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9484",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9484#issuecomment-91065",
    "user": "kcrisman"
}
```

This looks fine, except probably one should put commands like `implicit_plot3d` in double ticks like ```implicit_plot3d```, or in that case you might even be able to use `:meth:` or something like that.  Very interesting example!
