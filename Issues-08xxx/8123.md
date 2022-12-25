# Issue 8123: Notebook inclusion of SVG files

archive/issues_008123.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @mkoeppe\n\nIt seems that the notebook is close to serving \"SVG\" files in a way usable for SVG capable browser, but is not quite there:\nIf I try\n\n```\nsage: p = plot(x^2, -2, 2)\nsage: p.save('xsquared.svg')\n```\nin the notebook, Firefox 3.5.2 gives me a \"plugin needed\" message and where the picture is supposed to be, I only get a placeholder.\nIf I save `xsquared.svg` and point my browser directly to it, firefox displays the picture, so Firefox 3.5.2 can understand the SVG produced. HTML code that succeeds in displaying the picture:\n\n```\n<html>\n<body>\n<object data=\"xsquared.svg\">\n</body>\n</html>\n```\nSo, it may be that the notebook simply needs to generate different HTML for including SVG files it finds. Alternatively, it may be a matter of serving the SVG file with the appropriate MIME type.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8123\n\n",
    "closed_at": "2020-08-14T15:43:16Z",
    "created_at": "2010-01-29T19:24:04Z",
    "labels": [
        "component: notebook",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Notebook inclusion of SVG files",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8123",
    "user": "https://github.com/nbruin"
}
```
Assignee: @williamstein

CC:  @mkoeppe

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

archive/issue_comments_071287.json:
```json
{
    "body": "Try adding\n\n```\nimage/svg+xml   svg svgz\n```\nto `/etc/mime.times`, then restarting the notebook server and the browser.  This works for me in Firefox 3.5.6 on 64-bit Fedora 10 Linux.",
    "created_at": "2010-02-04T14:32:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8123",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8123#issuecomment-71287",
    "user": "https://github.com/qed777"
}
```

Try adding

```
image/svg+xml   svg svgz
```
to `/etc/mime.times`, then restarting the notebook server and the browser.  This works for me in Firefox 3.5.6 on 64-bit Fedora 10 Linux.



---

archive/issue_comments_071288.json:
```json
{
    "body": "That should be `/etc/mime.types.`",
    "created_at": "2010-02-04T14:35:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8123",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8123#issuecomment-71288",
    "user": "https://github.com/qed777"
}
```

That should be `/etc/mime.types.`



---

archive/issue_comments_071289.json:
```json
{
    "body": "Changing assignee from @williamstein to @qed777.",
    "created_at": "2010-02-04T14:47:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8123",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8123#issuecomment-71289",
    "user": "https://github.com/qed777"
}
```

Changing assignee from @williamstein to @qed777.



---

archive/issue_comments_071290.json:
```json
{
    "body": "We may need to add `height` and `width` attributes for Opera and WebKit browsers.",
    "created_at": "2010-02-04T14:47:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8123",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8123#issuecomment-71290",
    "user": "https://github.com/qed777"
}
```

We may need to add `height` and `width` attributes for Opera and WebKit browsers.



---

archive/issue_comments_071291.json:
```json
{
    "body": "Changing assignee from @qed777 to @williamstein.",
    "created_at": "2010-02-04T14:47:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8123",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8123#issuecomment-71291",
    "user": "https://github.com/qed777"
}
```

Changing assignee from @qed777 to @williamstein.



---

archive/issue_comments_071292.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2020-05-14T09:20:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8123",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8123#issuecomment-71292",
    "user": "https://github.com/fchapoton"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_071293.json:
```json
{
    "body": "maybe we can also close this ancient ticket about the deprecated sagenb ?",
    "created_at": "2020-05-14T09:20:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8123",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8123#issuecomment-71293",
    "user": "https://github.com/fchapoton"
}
```

maybe we can also close this ancient ticket about the deprecated sagenb ?



---

archive/issue_events_019456.json:
```json
{
    "actor": "https://github.com/fchapoton",
    "created_at": "2020-05-14T09:20:24Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8123",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8123#event-19456"
}
```



---

archive/issue_comments_071294.json:
```json
{
    "body": "Could be worth checking out whether this works in Jupyter first - most of the other sagenb ones are definitely sagenb specific, but could be worth seeing whether \n\n```\nsage: p = plot(x^2, -2, 2)\nsage: p.save('xsquared.svg')\n```\n\"works\" as expected in Jupyter.  (I would hope all browsers would now support this though!)",
    "created_at": "2020-05-18T17:47:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8123",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8123#issuecomment-71294",
    "user": "https://github.com/kcrisman"
}
```

Could be worth checking out whether this works in Jupyter first - most of the other sagenb ones are definitely sagenb specific, but could be worth seeing whether 

```
sage: p = plot(x^2, -2, 2)
sage: p.save('xsquared.svg')
```
"works" as expected in Jupyter.  (I would hope all browsers would now support this though!)



---

archive/issue_comments_071295.json:
```json
{
    "body": "It does work in jupyter. Closing.",
    "created_at": "2020-07-31T12:03:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8123",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8123#issuecomment-71295",
    "user": "https://github.com/dimpase"
}
```

It does work in jupyter. Closing.



---

archive/issue_comments_071296.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2020-07-31T12:03:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8123",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8123#issuecomment-71296",
    "user": "https://github.com/dimpase"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_019457.json:
```json
{
    "actor": "https://github.com/fchapoton",
    "created_at": "2020-08-14T15:43:16Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8123",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8123#event-19457"
}
```



---

archive/issue_comments_071297.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2020-08-14T15:43:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8123",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8123#issuecomment-71297",
    "user": "https://github.com/fchapoton"
}
```

Resolution: invalid
