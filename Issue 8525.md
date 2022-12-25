# Issue 8525: mistake in docstring for R=Zp(3)'s R.plot method.

archive/issues_008525.json:
```json
{
    "body": "Assignee: @roed314\n\nNote max_points versus point_count (in INPUT) below:\n\n\n```\nFile: /home/wstein/sage/local/lib/python2.6/site-packages/sage/rings/padics/padic_base_generic.py\n\nType: <type \u2018instancemethod\u2019>\n\nDefinition: k.plot(max_points=2500, **args)\n\nDocstring:\n\n    Creates a visualization of this p-adic ring as a fractal similar as a generalization of the the Sierpi\u2019nski triangle. The resulting image attempts to capture the algebraic and topological characteristics of \u2124p.\n\n    INPUT:\n\n        * point_count \u2013 the maximum number or points to plot, which controls the depth of recursion (default 2500)\n        * **args \u2013 color, size, etc. that are passed to the underlying point graphics objects\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8525\n\n",
    "created_at": "2010-03-13T17:22:55Z",
    "labels": [
        "component: padics",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.8",
    "title": "mistake in docstring for R=Zp(3)'s R.plot method.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8525",
    "user": "https://github.com/williamstein"
}
```
Assignee: @roed314

Note max_points versus point_count (in INPUT) below:


```
File: /home/wstein/sage/local/lib/python2.6/site-packages/sage/rings/padics/padic_base_generic.py

Type: <type ‘instancemethod’>

Definition: k.plot(max_points=2500, **args)

Docstring:

    Creates a visualization of this p-adic ring as a fractal similar as a generalization of the the Sierpi’nski triangle. The resulting image attempts to capture the algebraic and topological characteristics of ℤp.

    INPUT:

        * point_count – the maximum number or points to plot, which controls the depth of recursion (default 2500)
        * **args – color, size, etc. that are passed to the underlying point graphics objects
```


Issue created by migration from https://trac.sagemath.org/ticket/8525





---

archive/issue_comments_076921.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2011-11-09T03:48:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8525",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8525#issuecomment-76921",
    "user": "https://github.com/roed314"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_076922.json:
```json
{
    "body": "Attachment [8525.patch](tarball://root/attachments/some-uuid/ticket8525/8525.patch) by @roed314 created at 2011-11-09 03:48:14",
    "created_at": "2011-11-09T03:48:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8525",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8525#issuecomment-76922",
    "user": "https://github.com/roed314"
}
```

Attachment [8525.patch](tarball://root/attachments/some-uuid/ticket8525/8525.patch) by @roed314 created at 2011-11-09 03:48:14



---

archive/issue_comments_076923.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-12-01T09:51:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8525",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8525#issuecomment-76923",
    "user": "https://trac.sagemath.org/admin/accounts/users/johanbosman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_008705.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2011-12-05T16:06:24Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8525",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8525#event-8705"
}
```



---

archive/issue_comments_076924.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-12-05T16:06:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8525",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8525#issuecomment-76924",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed
