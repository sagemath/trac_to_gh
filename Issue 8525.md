# Issue 8525: mistake in docstring for R=Zp(3)'s R.plot method.

archive/issues_008525.json:
```json
{
    "body": "Assignee: roed\n\nNote max_points versus point_count (in INPUT) below:\n\n\n```\nFile: /home/wstein/sage/local/lib/python2.6/site-packages/sage/rings/padics/padic_base_generic.py\n\nType: <type \u2018instancemethod\u2019>\n\nDefinition: k.plot(max_points=2500, **args)\n\nDocstring:\n\n    Creates a visualization of this p-adic ring as a fractal similar as a generalization of the the Sierpi\u2019nski triangle. The resulting image attempts to capture the algebraic and topological characteristics of \u2124p.\n\n    INPUT:\n\n        * point_count \u2013 the maximum number or points to plot, which controls the depth of recursion (default 2500)\n        * **args \u2013 color, size, etc. that are passed to the underlying point graphics objects\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8525\n\n",
    "created_at": "2010-03-13T17:22:55Z",
    "labels": [
        "padics",
        "minor",
        "bug"
    ],
    "title": "mistake in docstring for R=Zp(3)'s R.plot method.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8525",
    "user": "was"
}
```
Assignee: roed

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

archive/issue_comments_077048.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2011-11-09T03:48:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8525",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8525#issuecomment-77048",
    "user": "roed"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_077049.json:
```json
{
    "body": "Attachment",
    "created_at": "2011-11-09T03:48:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8525",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8525#issuecomment-77049",
    "user": "roed"
}
```

Attachment



---

archive/issue_comments_077050.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-12-01T09:51:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8525",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8525#issuecomment-77050",
    "user": "johanbosman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_077051.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-12-05T16:06:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8525",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8525#issuecomment-77051",
    "user": "jdemeyer"
}
```

Resolution: fixed
