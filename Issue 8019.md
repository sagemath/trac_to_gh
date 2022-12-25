# Issue 8019: rendering a plot changes its dimensions [was: graphics_array messes up dimensions of plots]

archive/issues_008019.json:
```json
{
    "body": "Assignee: @williamstein\n\nKeywords: axes_range, axes_pad\n\nThe following code should illustrate this, see picture below, everything gets scaled for no reason.\n\n```\ngraph = circle((0,0),20)\ngraph.set_aspect_ratio(1)\ngraph2 = graphics_array([[graph]*4]*4)\ngraph2.show()\n```\n\nThe real reason is that axes_pad<>0 will affect the same picture every time it's rendered (to be saved or displayed), and change its dimensions by 2% each time by default. I can understand the need for axes_pad, but don't think this should happen:\n\n```\ngraph = circle((0,0),20)\ngraph.show()\nprint graph.get_axes_range()\ngraph.save('test.png')\ngraph.save('test.png')\ngraph.save('test.png')\ngraph.save('test.png')\ngraph.save('test.png')\nprint graph.get_axes_range()\ngraph.show()\n```\nand compare with\n\n```\ngraph = circle((0,0),20)\ngraph.show(axes_pad=0)\nprint graph.get_axes_range()\ngraph.save('test.png',axes_pad=0)\ngraph.save('test.png',axes_pad=0)\ngraph.save('test.png',axes_pad=0)\ngraph.save('test.png',axes_pad=0)\ngraph.save('test.png',axes_pad=0)\nprint graph.get_axes_range()\ngraph.show(axes_pad=0)\n```\n\n\n\n\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8019\n\n",
    "closed_at": "2010-12-21T20:36:21Z",
    "created_at": "2010-01-21T00:31:30Z",
    "labels": [
        "component: graphics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "rendering a plot changes its dimensions [was: graphics_array messes up dimensions of plots]",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8019",
    "user": "https://trac.sagemath.org/admin/accounts/users/pdehaye"
}
```
Assignee: @williamstein

Keywords: axes_range, axes_pad

The following code should illustrate this, see picture below, everything gets scaled for no reason.

```
graph = circle((0,0),20)
graph.set_aspect_ratio(1)
graph2 = graphics_array([[graph]*4]*4)
graph2.show()
```

The real reason is that axes_pad<>0 will affect the same picture every time it's rendered (to be saved or displayed), and change its dimensions by 2% each time by default. I can understand the need for axes_pad, but don't think this should happen:

```
graph = circle((0,0),20)
graph.show()
print graph.get_axes_range()
graph.save('test.png')
graph.save('test.png')
graph.save('test.png')
graph.save('test.png')
graph.save('test.png')
print graph.get_axes_range()
graph.show()
```
and compare with

```
graph = circle((0,0),20)
graph.show(axes_pad=0)
print graph.get_axes_range()
graph.save('test.png',axes_pad=0)
graph.save('test.png',axes_pad=0)
graph.save('test.png',axes_pad=0)
graph.save('test.png',axes_pad=0)
graph.save('test.png',axes_pad=0)
print graph.get_axes_range()
graph.show(axes_pad=0)
```







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

archive/issue_events_019214.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2010-12-21T20:36:21Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8019",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8019#event-19214"
}
```



---

archive/issue_events_019215.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2010-12-21T20:36:21Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8019",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8019#event-19215"
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
