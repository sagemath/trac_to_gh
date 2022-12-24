# Issue 5938: graph plotting -- ploting of graphs (networks) is somehow messed up/scaled wrong/cropped wrong since it doesn't work with graphics_array

archive/issues_005938.json:
```json
{
    "body": "Assignee: rlm\n\nWant to see some truly hideous plotting output?  Try this:\n\n\n```\nQ = GraphQuery(display_cols=['graph6','num_vertices','degree_sequence'],num_edges=['<=',5],min_degree=1)\n\nv = Q.get_graphs_list(); v\n\ngraphics_array([g.plot() for g in v], 3, len(v)//3).show()\n```\n\n\nI guess the problem is maybe Networkx drawing the plots instead of Sage (??), hence the cropping/layout is wrong?  I don't know.  Why do we use networkx at all for any part of plotting?  It would be better to plot to native Sage primitives, wouldn't it?\n\nFix?  make it so the edges aren't cropped wrong.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5938\n\n",
    "created_at": "2009-04-29T16:11:45Z",
    "labels": [
        "graph theory",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "graph plotting -- ploting of graphs (networks) is somehow messed up/scaled wrong/cropped wrong since it doesn't work with graphics_array",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5938",
    "user": "was"
}
```
Assignee: rlm

Want to see some truly hideous plotting output?  Try this:


```
Q = GraphQuery(display_cols=['graph6','num_vertices','degree_sequence'],num_edges=['<=',5],min_degree=1)

v = Q.get_graphs_list(); v

graphics_array([g.plot() for g in v], 3, len(v)//3).show()
```


I guess the problem is maybe Networkx drawing the plots instead of Sage (??), hence the cropping/layout is wrong?  I don't know.  Why do we use networkx at all for any part of plotting?  It would be better to plot to native Sage primitives, wouldn't it?

Fix?  make it so the edges aren't cropped wrong.

Issue created by migration from https://trac.sagemath.org/ticket/5938





---

archive/issue_comments_046941.json:
```json
{
    "body": "Even this (following the above example), results in hideous mis-cropped plots, and it doesn't use graphics array at all:\n\n```\nfor g in v[:5]:\n    show(g,figsize=2)\n```\n",
    "created_at": "2009-04-29T16:13:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5938",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5938#issuecomment-46941",
    "user": "was"
}
```

Even this (following the above example), results in hideous mis-cropped plots, and it doesn't use graphics array at all:

```
for g in v[:5]:
    show(g,figsize=2)
```




---

archive/issue_comments_046942.json:
```json
{
    "body": "And even this results in bits being chopped off that shouldn't be!\n\n```\nfor g in v[:5]:\n    show(g)\n```\n",
    "created_at": "2009-04-29T16:14:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5938",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5938#issuecomment-46942",
    "user": "was"
}
```

And even this results in bits being chopped off that shouldn't be!

```
for g in v[:5]:
    show(g)
```




---

archive/issue_comments_046943.json:
```json
{
    "body": "I'm still working on this, but I have some updates.  It looks like the first problem is the buffer size on scatter_plot.  It's including the points, but not the vertex radius of the outermost points.  That should be simple enough to fix, but then I'll also look at some auto-scaling to make the graphics_array a little nicer.  I also feel like the graphs_list module had some nice parameters for graphics_arrays of graphs, but they might be outdated now that graph plotting is native in Sage.  I'll check into that too though.",
    "created_at": "2009-05-18T21:11:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5938",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5938#issuecomment-46943",
    "user": "ekirkman"
}
```

I'm still working on this, but I have some updates.  It looks like the first problem is the buffer size on scatter_plot.  It's including the points, but not the vertex radius of the outermost points.  That should be simple enough to fix, but then I'll also look at some auto-scaling to make the graphics_array a little nicer.  I also feel like the graphs_list module had some nice parameters for graphics_arrays of graphs, but they might be outdated now that graph plotting is native in Sage.  I'll check into that too though.



---

archive/issue_comments_046944.json:
```json
{
    "body": "See http://groups.google.com/group/sage-support/browse_thread/thread/274d540f783603e7/e43c031f36672d85",
    "created_at": "2009-11-03T02:55:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5938",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5938#issuecomment-46944",
    "user": "jason"
}
```

See http://groups.google.com/group/sage-support/browse_thread/thread/274d540f783603e7/e43c031f36672d85



---

archive/issue_comments_046945.json:
```json
{
    "body": "<vent>\nTHIS SUCKS!!!!!!!!!!!\n\nI can't believe how annoying it is that plotting graphs is still so totally and completely broken.  It is really, really horrible.  I don't know how anybody can stand this. \n\nFrickin' a.   Every single graph plot I try has the borders chopped off.  E.g.,\n\n\n```\nsage: Q = GraphQuery(display_cols=['graph6','num_vertices','degree_sequence'], num_edges=['<=',5],min_degree=1)\nsage: Q.show(with_picture=True)\n[[hideous pain]]\n```\n",
    "created_at": "2010-08-10T00:37:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5938",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5938#issuecomment-46945",
    "user": "was"
}
```

<vent>
THIS SUCKS!!!!!!!!!!!

I can't believe how annoying it is that plotting graphs is still so totally and completely broken.  It is really, really horrible.  I don't know how anybody can stand this. 

Frickin' a.   Every single graph plot I try has the borders chopped off.  E.g.,


```
sage: Q = GraphQuery(display_cols=['graph6','num_vertices','degree_sequence'], num_edges=['<=',5],min_degree=1)
sage: Q.show(with_picture=True)
[[hideous pain]]
```




---

archive/issue_comments_046946.json:
```json
{
    "body": "Fix it!",
    "created_at": "2010-08-10T00:44:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5938",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5938#issuecomment-46946",
    "user": "rlm"
}
```

Fix it!



---

archive/issue_comments_046947.json:
```json
{
    "body": "Warning- I've seen several \"fixes\" for this go in, and yet it's still borken",
    "created_at": "2010-08-10T00:44:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5938",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5938#issuecomment-46947",
    "user": "rlm"
}
```

Warning- I've seen several "fixes" for this go in, and yet it's still borken



---

archive/issue_comments_046948.json:
```json
{
    "body": "See #9211 for progress towards a fix.",
    "created_at": "2010-08-10T07:23:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5938",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5938#issuecomment-46948",
    "user": "jason"
}
```

See #9211 for progress towards a fix.



---

archive/issue_comments_046949.json:
```json
{
    "body": "Graph vertices are not cut off anymore.  The plot in the description has overlapping vertices, though.",
    "created_at": "2011-12-21T13:38:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5938",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5938#issuecomment-46949",
    "user": "jason"
}
```

Graph vertices are not cut off anymore.  The plot in the description has overlapping vertices, though.



---

archive/issue_comments_046950.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2011-12-21T13:38:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5938",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5938#issuecomment-46950",
    "user": "jason"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_046951.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-12-21T13:41:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5938",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5938#issuecomment-46951",
    "user": "jason"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_046952.json:
```json
{
    "body": "This is a dup of #9211.  Since the patch is there, and it is already merged, I'm calling this the duplicate.",
    "created_at": "2011-12-21T13:41:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5938",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5938#issuecomment-46952",
    "user": "jason"
}
```

This is a dup of #9211.  Since the patch is there, and it is already merged, I'm calling this the duplicate.



---

archive/issue_comments_046953.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2012-01-05T13:34:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5938",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5938#issuecomment-46953",
    "user": "jdemeyer"
}
```

Resolution: duplicate
