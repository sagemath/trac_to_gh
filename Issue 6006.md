# Issue 6006: Bring plot/point.py to 100% coverage

archive/issues_006006.json:
```json
{
    "body": "Assignee: tba\n\nBring plot/point.py to 100% coverage.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6006\n\n",
    "created_at": "2009-05-08T05:09:27Z",
    "labels": [
        "documentation",
        "minor",
        "enhancement"
    ],
    "title": "Bring plot/point.py to 100% coverage",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6006",
    "user": "kcrisman"
}
```
Assignee: tba

Bring plot/point.py to 100% coverage.

Issue created by migration from https://trac.sagemath.org/ticket/6006





---

archive/issue_comments_047781.json:
```json
{
    "body": "Changing assignee from tba to kcrisman.",
    "created_at": "2009-05-08T05:13:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6006",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6006#issuecomment-47781",
    "user": "kcrisman"
}
```

Changing assignee from tba to kcrisman.



---

archive/issue_comments_047782.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-05-08T05:13:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6006",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6006#issuecomment-47782",
    "user": "kcrisman"
}
```

Changing status from new to assigned.



---

archive/issue_comments_047783.json:
```json
{
    "body": "Attachment [trac_6006.patch](tarball://root/attachments/some-uuid/ticket6006/trac_6006.patch) by kcrisman created at 2009-05-08 05:13:20\n\nThis patch also actually implements the height option for the plot3d method of the Point class that the old doctest was actually using through a 3D graphics object.",
    "created_at": "2009-05-08T05:13:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6006",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6006#issuecomment-47783",
    "user": "kcrisman"
}
```

Attachment [trac_6006.patch](tarball://root/attachments/some-uuid/ticket6006/trac_6006.patch) by kcrisman created at 2009-05-08 05:13:20

This patch also actually implements the height option for the plot3d method of the Point class that the old doctest was actually using through a 3D graphics object.



---

archive/issue_comments_047784.json:
```json
{
    "body": "I should also point out that I could not find a way to test for _allowed_options for the keywords in Point.plot3d, so I put something about that in the TODO but also pointed it out in the documentation, lest one confuse pointsize and size (et al.).",
    "created_at": "2009-05-08T05:15:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6006",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6006#issuecomment-47784",
    "user": "kcrisman"
}
```

I should also point out that I could not find a way to test for _allowed_options for the keywords in Point.plot3d, so I put something about that in the TODO but also pointed it out in the documentation, lest one confuse pointsize and size (et al.).



---

archive/issue_comments_047785.json:
```json
{
    "body": "See [http://groups.google.com/group/sage-devel/browse_thread/thread/1adac4035031b140/c36f1f8a7c8a9b43#c36f1f8a7c8a9b43](http://groups.google.com/group/sage-devel/browse_thread/thread/1adac4035031b140/c36f1f8a7c8a9b43#c36f1f8a7c8a9b43) for explanation of why there is no loads(dumps()) test.",
    "created_at": "2009-05-08T16:46:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6006",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6006#issuecomment-47785",
    "user": "kcrisman"
}
```

See [http://groups.google.com/group/sage-devel/browse_thread/thread/1adac4035031b140/c36f1f8a7c8a9b43#c36f1f8a7c8a9b43](http://groups.google.com/group/sage-devel/browse_thread/thread/1adac4035031b140/c36f1f8a7c8a9b43#c36f1f8a7c8a9b43) for explanation of why there is no loads(dumps()) test.



---

archive/issue_comments_047786.json:
```json
{
    "body": "On line 43, the constructor for `Point(GraphicPrimitive_xydata)` is\n\n```\n43\t    def __init__(self, xdata, ydata, options)\n```\n\nCurrently with Sphinx, any docstring of `__init__` will not be shown in the documentation for `Point(GraphicPrimitive_xydata)`. The situation is the same for every class. So one issue to fix is to copy the examples in `__init__(self, xdata, ydata, options)` and paste them within the docstring for `Point(GraphicPrimitive_xydata)` after line 32. Another issue is, the constructor arguments `xdata, ydata, options` on line 43 are not documented in the docstring for `Point(GraphicPrimitive_xydata)`. Constructor arguments must be documented to explain what they are, and how to properly use them.",
    "created_at": "2009-05-13T04:36:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6006",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6006#issuecomment-47786",
    "user": "mvngu"
}
```

On line 43, the constructor for `Point(GraphicPrimitive_xydata)` is

```
43	    def __init__(self, xdata, ydata, options)
```

Currently with Sphinx, any docstring of `__init__` will not be shown in the documentation for `Point(GraphicPrimitive_xydata)`. The situation is the same for every class. So one issue to fix is to copy the examples in `__init__(self, xdata, ydata, options)` and paste them within the docstring for `Point(GraphicPrimitive_xydata)` after line 32. Another issue is, the constructor arguments `xdata, ydata, options` on line 43 are not documented in the docstring for `Point(GraphicPrimitive_xydata)`. Constructor arguments must be documented to explain what they are, and how to properly use them.



---

archive/issue_comments_047787.json:
```json
{
    "body": "I was not aware of this.  I would be happy to improve this, and copying examples is easy.  However, could you point me to a file with a correctly documented set of constructor arguments?  I am uncertain how to proceed with that, particularly because I modeled my own documentation after other examples in plot/; the xdata and ydata, for instance, come from the function getxydata or something like that, which is called when a point (as opposed to Point) is made.   Also, what *should* be in the docstring for __init__, if not what is currently there?  Thanks for any ideas or model files to look at!",
    "created_at": "2009-05-13T13:35:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6006",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6006#issuecomment-47787",
    "user": "kcrisman"
}
```

I was not aware of this.  I would be happy to improve this, and copying examples is easy.  However, could you point me to a file with a correctly documented set of constructor arguments?  I am uncertain how to proceed with that, particularly because I modeled my own documentation after other examples in plot/; the xdata and ydata, for instance, come from the function getxydata or something like that, which is called when a point (as opposed to Point) is made.   Also, what *should* be in the docstring for __init__, if not what is currently there?  Thanks for any ideas or model files to look at!



---

archive/issue_comments_047788.json:
```json
{
    "body": "Replying to [comment:4 mvngu]:\n}\n> Currently with Sphinx, any docstring of `__init__` will not be shown in the documentation for `Point(GraphicPrimitive_xydata)`. The situation is the same for every class. So one issue to fix is to copy the examples in `__init__(self, xdata, ydata, options)` and paste them within the docstring for `Point(GraphicPrimitive_xydata)` after line 32.\n\nNo, do not do this. It will be fixed in the future. This is still \"needs work\" due to the other issue.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-13T17:18:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6006",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6006#issuecomment-47788",
    "user": "mabshoff"
}
```

Replying to [comment:4 mvngu]:
}
> Currently with Sphinx, any docstring of `__init__` will not be shown in the documentation for `Point(GraphicPrimitive_xydata)`. The situation is the same for every class. So one issue to fix is to copy the examples in `__init__(self, xdata, ydata, options)` and paste them within the docstring for `Point(GraphicPrimitive_xydata)` after line 32.

No, do not do this. It will be fixed in the future. This is still "needs work" due to the other issue.

Cheers,

Michael



---

archive/issue_comments_047789.json:
```json
{
    "body": "Attachment [trac_6006-fix.patch](tarball://root/attachments/some-uuid/ticket6006/trac_6006-fix.patch) by kcrisman created at 2009-05-14 16:14:45",
    "created_at": "2009-05-14T16:14:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6006",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6006#issuecomment-47789",
    "user": "kcrisman"
}
```

Attachment [trac_6006-fix.patch](tarball://root/attachments/some-uuid/ticket6006/trac_6006-fix.patch) by kcrisman created at 2009-05-14 16:14:45



---

archive/issue_comments_047790.json:
```json
{
    "body": "reviewer patch",
    "created_at": "2009-05-15T07:20:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6006",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6006#issuecomment-47790",
    "user": "mvngu"
}
```

reviewer patch



---

archive/issue_comments_047791.json:
```json
{
    "body": "Attachment [trac_6006-reviewer.patch](tarball://root/attachments/some-uuid/ticket6006/trac_6006-reviewer.patch) by mvngu created at 2009-05-15 07:22:16\n\nPositive review! Apply patches in the following order:\n1. `trac_6006.patch`\n2. `trac_6006-fix.patch`\n3. `trac_6006-reviewer.patch` -- this fixes two trivial typos introduced in `trac_6006.patch`",
    "created_at": "2009-05-15T07:22:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6006",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6006#issuecomment-47791",
    "user": "mvngu"
}
```

Attachment [trac_6006-reviewer.patch](tarball://root/attachments/some-uuid/ticket6006/trac_6006-reviewer.patch) by mvngu created at 2009-05-15 07:22:16

Positive review! Apply patches in the following order:
1. `trac_6006.patch`
2. `trac_6006-fix.patch`
3. `trac_6006-reviewer.patch` -- this fixes two trivial typos introduced in `trac_6006.patch`



---

archive/issue_comments_047792.json:
```json
{
    "body": "Merged all three patches in Sage 4.0.alpha0.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-15T07:54:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6006",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6006#issuecomment-47792",
    "user": "mabshoff"
}
```

Merged all three patches in Sage 4.0.alpha0.

Cheers,

Michael



---

archive/issue_comments_047793.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-05-15T07:54:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6006",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6006#issuecomment-47793",
    "user": "mabshoff"
}
```

Resolution: fixed
