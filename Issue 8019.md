# Issue 8019: graphics_array messes up dimensions of plots

archive/issues_008019.json:
```json
{
    "body": "Assignee: was\n\nKeywords: graphics_array, scale\n\nThe following code should illustrate this, see picture below, everything gets scaled for no reason.\n\ngraph = circle((0,0),20)\ngraph.set_aspect_ratio(1)\ngraph2 = graphics_array([[graph]*4]*4)\ngraph2.show()\n\nIssue created by migration from https://trac.sagemath.org/ticket/8019\n\n",
    "created_at": "2010-01-21T00:31:30Z",
    "labels": [
        "graphics",
        "minor",
        "bug"
    ],
    "title": "graphics_array messes up dimensions of plots",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8019",
    "user": "pdehaye"
}
```
Assignee: was

Keywords: graphics_array, scale

The following code should illustrate this, see picture below, everything gets scaled for no reason.

graph = circle((0,0),20)
graph.set_aspect_ratio(1)
graph2 = graphics_array([[graph]*4]*4)
graph2.show()

Issue created by migration from https://trac.sagemath.org/ticket/8019





---

archive/issue_comments_070073.json:
```json
{
    "body": "Attachment [circles.png](tarball://root/attachments/some-uuid/ticket8019/circles.png) by pdehaye created at 2010-01-21 00:32:45",
    "created_at": "2010-01-21T00:32:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8019",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8019#issuecomment-70073",
    "user": "pdehaye"
}
```

Attachment [circles.png](tarball://root/attachments/some-uuid/ticket8019/circles.png) by pdehaye created at 2010-01-21 00:32:45



---

archive/issue_comments_070074.json:
```json
{
    "body": "Changing keywords from \"graphics_array, scale\" to \"axes_range, axes_pad\".",
    "created_at": "2010-01-21T08:56:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8019",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8019#issuecomment-70074",
    "user": "pdehaye"
}
```

Changing keywords from "graphics_array, scale" to "axes_range, axes_pad".



---

archive/issue_comments_070075.json:
```json
{
    "body": "Changing priority from minor to major.",
    "created_at": "2010-01-21T08:56:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8019",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8019#issuecomment-70075",
    "user": "pdehaye"
}
```

Changing priority from minor to major.



---

archive/issue_comments_070076.json:
```json
{
    "body": "I think the problem is that in the save routine (actually, in the .matplotlib() method), the x and y limits are changed according to the axes_pad setting.  Instead, they should be temporarily changed and then changed back so that the graphic has the same x and y limits as it did when starting.",
    "created_at": "2010-09-29T21:44:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8019",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8019#issuecomment-70076",
    "user": "jason"
}
```

I think the problem is that in the save routine (actually, in the .matplotlib() method), the x and y limits are changed according to the axes_pad setting.  Instead, they should be temporarily changed and then changed back so that the graphic has the same x and y limits as it did when starting.



---

archive/issue_comments_070077.json:
```json
{
    "body": "This has been fixed by #10291.",
    "created_at": "2010-12-21T20:36:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8019",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8019#issuecomment-70077",
    "user": "mhansen"
}
```

This has been fixed by #10291.



---

archive/issue_comments_070078.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2010-12-21T20:36:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8019",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8019#issuecomment-70078",
    "user": "mhansen"
}
```

Resolution: invalid
