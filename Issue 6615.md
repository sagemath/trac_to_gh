# Issue 6615: Small bug in Graph.plot()

archive/issues_006615.json:
```json
{
    "body": "Assignee: @rlmill\n\nIt may take only two lines, but I do not know which ones (I got a bit lost reading graph_plot.py) and it may take half a second to who wrote it in the first place.\n\ng=graphs.PetersenGraph()\ng.plot(edge_colors={\"red\":[(0,1)]})\ng.plot(vertex_colors={\"red\":[1]})\n\nWhen you plot a graph and want some edges to have a different color, the first plot is perfect. In the second case, though, I think it would be better to assign the others vertices a default color ;-)\n\nIssue created by migration from https://trac.sagemath.org/ticket/6615\n\n",
    "created_at": "2009-07-24T18:00:05Z",
    "labels": [
        "component: graph theory",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.1",
    "title": "Small bug in Graph.plot()",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6615",
    "user": "https://github.com/nathanncohen"
}
```
Assignee: @rlmill

It may take only two lines, but I do not know which ones (I got a bit lost reading graph_plot.py) and it may take half a second to who wrote it in the first place.

g=graphs.PetersenGraph()
g.plot(edge_colors={"red":[(0,1)]})
g.plot(vertex_colors={"red":[1]})

When you plot a graph and want some edges to have a different color, the first plot is perfect. In the second case, though, I think it would be better to assign the others vertices a default color ;-)

Issue created by migration from https://trac.sagemath.org/ticket/6615





---

archive/issue_comments_054060.json:
```json
{
    "body": "The best way to do that may be to let vertex_colors (resp. edge_colors) in Graph.plot() accept any partition of the vertices ( resp. edges ), and let it deal with rainbow to pick the colors. Obviously, it does not mean Graph.plot() should not also be able to support the current dictionary of (color, list)",
    "created_at": "2009-08-02T11:33:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6615",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6615#issuecomment-54060",
    "user": "https://github.com/nathanncohen"
}
```

The best way to do that may be to let vertex_colors (resp. edge_colors) in Graph.plot() accept any partition of the vertices ( resp. edges ), and let it deal with rainbow to pick the colors. Obviously, it does not mean Graph.plot() should not also be able to support the current dictionary of (color, list)



---

archive/issue_comments_054061.json:
```json
{
    "body": "All the vertices are colored even if vertex_colors did not contain colors for all of them. The first unused color in ranbow() is taken.\n\nThere was a small mistake in rgbcolor() where the hexcadecimal values were divided by 256 instead of 255 which lead to \"red\"!=(1,0,0).\n\nAll the colors were wrong and nobody noticed !! :-)",
    "created_at": "2009-08-14T17:31:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6615",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6615#issuecomment-54061",
    "user": "https://github.com/nathanncohen"
}
```

All the vertices are colored even if vertex_colors did not contain colors for all of them. The first unused color in ranbow() is taken.

There was a small mistake in rgbcolor() where the hexcadecimal values were divided by 256 instead of 255 which lead to "red"!=(1,0,0).

All the colors were wrong and nobody noticed !! :-)



---

archive/issue_comments_054062.json:
```json
{
    "body": "* Graphfunctions-1 has no reason for being here, but I can not delete it\n   * patchplot has been updated, I had forgotten to commit the change from 256 to 255 in rgbcolor()",
    "created_at": "2009-08-24T11:30:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6615",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6615#issuecomment-54062",
    "user": "https://github.com/nathanncohen"
}
```

* Graphfunctions-1 has no reason for being here, but I can not delete it
   * patchplot has been updated, I had forgotten to commit the change from 256 to 255 in rgbcolor()



---

archive/issue_comments_054063.json:
```json
{
    "body": "The edge color plot in the description works great.\n\nThe vertex color plot doesn't.  The specified vertex is red; the others disappeared!\n\nAlso, it would be great to include those two examples in the docs.",
    "created_at": "2009-09-15T04:32:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6615",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6615#issuecomment-54063",
    "user": "https://github.com/jasongrout"
}
```

The edge color plot in the description works great.

The vertex color plot doesn't.  The specified vertex is red; the others disappeared!

Also, it would be great to include those two examples in the docs.



---

archive/issue_comments_054064.json:
```json
{
    "body": "Hello Jason !! I sent you an email about this patch some time ago, as I did not understand where this patch failed... Did you get it ? :-)",
    "created_at": "2009-10-27T05:56:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6615",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6615#issuecomment-54064",
    "user": "https://github.com/nathanncohen"
}
```

Hello Jason !! I sent you an email about this patch some time ago, as I did not understand where this patch failed... Did you get it ? :-)



---

archive/issue_comments_054065.json:
```json
{
    "body": "Patch works fine for me.",
    "created_at": "2009-12-16T18:55:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6615",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6615#issuecomment-54065",
    "user": "https://github.com/rlmill"
}
```

Patch works fine for me.



---

archive/issue_comments_054066.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-12-16T18:55:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6615",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6615#issuecomment-54066",
    "user": "https://github.com/rlmill"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_054067.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-12-16T18:56:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6615",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6615#issuecomment-54067",
    "user": "https://github.com/rlmill"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_054068.json:
```json
{
    "body": "There are test failures in sage/plot/colors.py",
    "created_at": "2009-12-19T19:54:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6615",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6615#issuecomment-54068",
    "user": "https://github.com/mwhansen"
}
```

There are test failures in sage/plot/colors.py



---

archive/issue_comments_054069.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2009-12-19T19:54:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6615",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6615#issuecomment-54069",
    "user": "https://github.com/mwhansen"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_054070.json:
```json
{
    "body": "Attachment [trac_6615-ref.patch](tarball://root/attachments/some-uuid/ticket6615/trac_6615-ref.patch) by @rlmill created at 2010-01-06 16:34:54\n\ndepends: sage-4.3.1.alpha1 + #7634",
    "created_at": "2010-01-06T16:34:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6615",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6615#issuecomment-54070",
    "user": "https://github.com/rlmill"
}
```

Attachment [trac_6615-ref.patch](tarball://root/attachments/some-uuid/ticket6615/trac_6615-ref.patch) by @rlmill created at 2010-01-06 16:34:54

depends: sage-4.3.1.alpha1 + #7634



---

archive/issue_comments_054071.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-01-06T16:35:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6615",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6615#issuecomment-54071",
    "user": "https://github.com/rlmill"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_054072.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-06T16:35:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6615",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6615#issuecomment-54072",
    "user": "https://github.com/rlmill"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_006855.json:
```json
{
    "actor": "https://github.com/rlmill",
    "created_at": "2010-01-13T05:38:58Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6615",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6615#event-6855"
}
```



---

archive/issue_comments_054073.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-13T05:38:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6615",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6615#issuecomment-54073",
    "user": "https://github.com/rlmill"
}
```

Resolution: fixed
