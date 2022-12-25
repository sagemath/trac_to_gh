# Issue 8019: graphics_array messes up dimensions of plots

archive/issues_008019.json:
```json
{
    "body": "Assignee: @williamstein\n\nKeywords: graphics_array, scale\n\nThe following code should illustrate this, see picture below, everything gets scaled for no reason.\n\ngraph = circle((0,0),20)\ngraph.set_aspect_ratio(1)\ngraph2 = graphics_array([[graph]*4]*4)\ngraph2.show()\n\nIssue created by migration from https://trac.sagemath.org/ticket/8019\n\n",
    "created_at": "2010-01-21T00:31:30Z",
    "labels": [
        "component: graphics",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "graphics_array messes up dimensions of plots",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8019",
    "user": "https://trac.sagemath.org/admin/accounts/users/pdehaye"
}
```
Assignee: @williamstein

Keywords: graphics_array, scale

The following code should illustrate this, see picture below, everything gets scaled for no reason.

graph = circle((0,0),20)
graph.set_aspect_ratio(1)
graph2 = graphics_array([[graph]*4]*4)
graph2.show()

Issue created by migration from https://trac.sagemath.org/ticket/8019





---

archive/issue_comments_069953.json:
```json
{
    "body": "Attachment [circles.png](tarball://root/attachments/some-uuid/ticket8019/circles.png) by pdehaye created at 2010-01-21 00:32:45",
    "created_at": "2010-01-21T00:32:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8019",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8019#issuecomment-69953",
    "user": "https://trac.sagemath.org/admin/accounts/users/pdehaye"
}
```

Attachment [circles.png](tarball://root/attachments/some-uuid/ticket8019/circles.png) by pdehaye created at 2010-01-21 00:32:45



---

archive/issue_comments_069954.json:
```json
{
    "body": "Changing keywords from \"graphics_array, scale\" to \"axes_range, axes_pad\".",
    "created_at": "2010-01-21T08:56:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8019",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8019#issuecomment-69954",
    "user": "https://trac.sagemath.org/admin/accounts/users/pdehaye"
}
```

Changing keywords from "graphics_array, scale" to "axes_range, axes_pad".



---

archive/issue_comments_069955.json:
```json
{
    "body": "I think the problem is that in the save routine (actually, in the .matplotlib() method), the x and y limits are changed according to the axes_pad setting.  Instead, they should be temporarily changed and then changed back so that the graphic has the same x and y limits as it did when starting.",
    "created_at": "2010-09-29T21:44:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8019",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8019#issuecomment-69955",
    "user": "https://github.com/jasongrout"
}
```

I think the problem is that in the save routine (actually, in the .matplotlib() method), the x and y limits are changed according to the axes_pad setting.  Instead, they should be temporarily changed and then changed back so that the graphic has the same x and y limits as it did when starting.



---

archive/issue_events_008230.json:
```json
{
    "actor": "@mwhansen",
    "created_at": "2010-12-21T20:36:21Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8019",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8019#event-8230"
}
```



---

archive/issue_comments_069956.json:
```json
{
    "body": "This has been fixed by #10291.",
    "created_at": "2010-12-21T20:36:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8019",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8019#issuecomment-69956",
    "user": "https://github.com/mwhansen"
}
```

This has been fixed by #10291.



---

archive/issue_comments_069957.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2010-12-21T20:36:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8019",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8019#issuecomment-69957",
    "user": "https://github.com/mwhansen"
}
```

Resolution: invalid
