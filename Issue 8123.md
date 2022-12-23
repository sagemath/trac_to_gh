# Issue 8123: Notebook inclusion of SVG files

archive/issues_008123.json:
```json
{
    "body": "Assignee: was\n\nCC:  mkoeppe\n\nIt seems that the notebook is close to serving \"SVG\" files in a way usable for SVG capable browser, but is not quite there:\nIf I try\n\n```\nsage: p = plot(x^2, -2, 2)\nsage: p.save('xsquared.svg')\n```\n\nin the notebook, Firefox 3.5.2 gives me a \"plugin needed\" message and where the picture is supposed to be, I only get a placeholder.\nIf I save `xsquared.svg` and point my browser directly to it, firefox displays the picture, so Firefox 3.5.2 can understand the SVG produced. HTML code that succeeds in displaying the picture:\n\n```\n<html>\n<body>\n<object data=\"xsquared.svg\">\n</body>\n</html>\n```\n\nSo, it may be that the notebook simply needs to generate different HTML for including SVG files it finds. Alternatively, it may be a matter of serving the SVG file with the appropriate MIME type.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8123\n\n",
    "created_at": "2010-01-29T19:24:04Z",
    "labels": [
        "notebook",
        "minor",
        "bug"
    ],
    "title": "Notebook inclusion of SVG files",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8123",
    "user": "nbruin"
}
```
Assignee: was

CC:  mkoeppe

It seems that the notebook is close to serving "SVG" files in a way usable for SVG capable browser, but is not quite there:
If I try

```
sage: p = plot(x^2, -2, 2)
sage: p.save('xsquared.svg')
```

in the notebook, Firefox 3.5.2 gives me a "plugin needed" message and where the picture is supposed to be, I only get a placeholder.
If I save `xsquared.svg` and point my browser directly to it, firefox displays the picture, so Firefox 3.5.2 can understand the SVG produced. HTML code that succeeds in displaying the picture:

```
<html>
<body>
<object data="xsquared.svg">
</body>
</html>
```

So, it may be that the notebook simply needs to generate different HTML for including SVG files it finds. Alternatively, it may be a matter of serving the SVG file with the appropriate MIME type.

Issue created by migration from https://trac.sagemath.org/ticket/8123





---

archive/issue_comments_071408.json:
```json
{
    "body": "Try adding\n\n```\nimage/svg+xml   svg svgz\n```\n\nto `/etc/mime.times`, then restarting the notebook server and the browser.  This works for me in Firefox 3.5.6 on 64-bit Fedora 10 Linux.",
    "created_at": "2010-02-04T14:32:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8123",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8123#issuecomment-71408",
    "user": "mpatel"
}
```

Try adding

```
image/svg+xml   svg svgz
```

to `/etc/mime.times`, then restarting the notebook server and the browser.  This works for me in Firefox 3.5.6 on 64-bit Fedora 10 Linux.



---

archive/issue_comments_071409.json:
```json
{
    "body": "That should be `/etc/mime.types.`",
    "created_at": "2010-02-04T14:35:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8123",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8123#issuecomment-71409",
    "user": "mpatel"
}
```

That should be `/etc/mime.types.`



---

archive/issue_comments_071410.json:
```json
{
    "body": "Changing assignee from was to mpatel.",
    "created_at": "2010-02-04T14:47:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8123",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8123#issuecomment-71410",
    "user": "mpatel"
}
```

Changing assignee from was to mpatel.



---

archive/issue_comments_071411.json:
```json
{
    "body": "We may need to add `height` and `width` attributes for Opera and WebKit browsers.",
    "created_at": "2010-02-04T14:47:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8123",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8123#issuecomment-71411",
    "user": "mpatel"
}
```

We may need to add `height` and `width` attributes for Opera and WebKit browsers.



---

archive/issue_comments_071412.json:
```json
{
    "body": "Changing assignee from mpatel to was.",
    "created_at": "2010-02-04T14:47:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8123",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8123#issuecomment-71412",
    "user": "mpatel"
}
```

Changing assignee from mpatel to was.



---

archive/issue_comments_071413.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2020-05-14T09:20:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8123",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8123#issuecomment-71413",
    "user": "chapoton"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_071414.json:
```json
{
    "body": "maybe we can also close this ancient ticket about the deprecated sagenb ?",
    "created_at": "2020-05-14T09:20:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8123",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8123#issuecomment-71414",
    "user": "chapoton"
}
```

maybe we can also close this ancient ticket about the deprecated sagenb ?



---

archive/issue_comments_071415.json:
```json
{
    "body": "Could be worth checking out whether this works in Jupyter first - most of the other sagenb ones are definitely sagenb specific, but could be worth seeing whether \n\n```\nsage: p = plot(x^2, -2, 2)\nsage: p.save('xsquared.svg')\n```\n\n\"works\" as expected in Jupyter.  (I would hope all browsers would now support this though!)",
    "created_at": "2020-05-18T17:47:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8123",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8123#issuecomment-71415",
    "user": "kcrisman"
}
```

Could be worth checking out whether this works in Jupyter first - most of the other sagenb ones are definitely sagenb specific, but could be worth seeing whether 

```
sage: p = plot(x^2, -2, 2)
sage: p.save('xsquared.svg')
```

"works" as expected in Jupyter.  (I would hope all browsers would now support this though!)



---

archive/issue_comments_071416.json:
```json
{
    "body": "It does work in jupyter. Closing.",
    "created_at": "2020-07-31T12:03:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8123",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8123#issuecomment-71416",
    "user": "dimpase"
}
```

It does work in jupyter. Closing.



---

archive/issue_comments_071417.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2020-07-31T12:03:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8123",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8123#issuecomment-71417",
    "user": "dimpase"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_071418.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2020-08-14T15:43:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8123",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8123#issuecomment-71418",
    "user": "chapoton"
}
```

Resolution: invalid
