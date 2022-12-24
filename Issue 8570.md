# Issue 8570: Allow "marker" option to be passed to matplotlib on list_plot() and point()

archive/issues_008570.json:
```json
{
    "body": "Assignee: was\n\nCC:  jason kcrisman\n\nKeywords: plot marker\n\nCurrently, there's no obvious way to pass the marker option to matplotlib when plotting individual points, which would be mostly with this option.\n\nIt appears that plot() has deviated from other plot types, since it does allow the marker option, but apparently only for function plots.\n\nusing plot(points(point_list),marker='x') ignores the marker option\nusing list_plot(point_list,marker='x') or points(point_list,marker='x') gives a warning:\n  verbose 0 (136: primitive.py, options) WARNING: Ignoring option 'marker'=x\nbut displays the points nevertheless, though ignoring the marker option.\n\nAlso, setting plot.options['marker'] = 'x' or Graphics().SHOW_OPTIONS['marker'] = 'x' do not work.\n\nSomewhat related to #4529, #1431 and #5448, which seem to be related to not passing kwargs to matplotlib.\n\nSo far, I haven't been able to find a way to seamless join matplotlib's system with the sage.plot options.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8570\n\n",
    "created_at": "2010-03-21T15:17:23Z",
    "labels": [
        "graphics",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "Allow \"marker\" option to be passed to matplotlib on list_plot() and point()",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8570",
    "user": "ronanpaixao"
}
```
Assignee: was

CC:  jason kcrisman

Keywords: plot marker

Currently, there's no obvious way to pass the marker option to matplotlib when plotting individual points, which would be mostly with this option.

It appears that plot() has deviated from other plot types, since it does allow the marker option, but apparently only for function plots.

using plot(points(point_list),marker='x') ignores the marker option
using list_plot(point_list,marker='x') or points(point_list,marker='x') gives a warning:
  verbose 0 (136: primitive.py, options) WARNING: Ignoring option 'marker'=x
but displays the points nevertheless, though ignoring the marker option.

Also, setting plot.options['marker'] = 'x' or Graphics().SHOW_OPTIONS['marker'] = 'x' do not work.

Somewhat related to #4529, #1431 and #5448, which seem to be related to not passing kwargs to matplotlib.

So far, I haven't been able to find a way to seamless join matplotlib's system with the sage.plot options.


Issue created by migration from https://trac.sagemath.org/ticket/8570





---

archive/issue_comments_077623.json:
```json
{
    "body": "I think it would be a good design decision to just bundle the plotjoined=True features in with line() (i.e., eliminate the plotjoined=True features in listplot, and just make listplot about plotting points).",
    "created_at": "2010-06-04T04:34:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8570",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8570#issuecomment-77623",
    "user": "jason"
}
```

I think it would be a good design decision to just bundle the plotjoined=True features in with line() (i.e., eliminate the plotjoined=True features in listplot, and just make listplot about plotting points).



---

archive/issue_comments_077624.json:
```json
{
    "body": "In fact, I think a better design decision would be to completely deprecate list_plot.  Replace it with line() in the connected case, and scatter_plot in the disconnected case.  Each of those commands does better than list_plot.",
    "created_at": "2010-06-04T04:55:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8570",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8570#issuecomment-77624",
    "user": "jason"
}
```

In fact, I think a better design decision would be to completely deprecate list_plot.  Replace it with line() in the connected case, and scatter_plot in the disconnected case.  Each of those commands does better than list_plot.



---

archive/issue_comments_077625.json:
```json
{
    "body": "For that matter, the listplot3d should maybe be called surface_plot() instead, as it is clearer what it is plotting.",
    "created_at": "2010-06-04T05:06:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8570",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8570#issuecomment-77625",
    "user": "jason"
}
```

For that matter, the listplot3d should maybe be called surface_plot() instead, as it is clearer what it is plotting.



---

archive/issue_comments_077626.json:
```json
{
    "body": "Another reason for the deprecation: I think every other graphics command is named after the *output* (like \"line\"), not the *input* (like \"list_plot\")",
    "created_at": "2010-06-05T00:53:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8570",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8570#issuecomment-77626",
    "user": "jason"
}
```

Another reason for the deprecation: I think every other graphics command is named after the *output* (like "line"), not the *input* (like "list_plot")



---

archive/issue_comments_077627.json:
```json
{
    "body": "In fact, scatter_plot should be deprecated in favor of just points().  If we do that, then we need to make points() have more options (like edgecolor, markerstyle, etc.).",
    "created_at": "2010-06-05T19:48:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8570",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8570#issuecomment-77627",
    "user": "jason"
}
```

In fact, scatter_plot should be deprecated in favor of just points().  If we do that, then we need to make points() have more options (like edgecolor, markerstyle, etc.).



---

archive/issue_comments_077628.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2010-06-05T19:48:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8570",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8570#issuecomment-77628",
    "user": "jason"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_077629.json:
```json
{
    "body": "Just noting that this is still really unfortunate.  Here is a workaround in the meantime for getting markers.\n\n```\nline([(1,2),(2,3)],marker=7,linestyle='')\n```\n",
    "created_at": "2012-01-25T03:46:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8570",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8570#issuecomment-77629",
    "user": "kcrisman"
}
```

Just noting that this is still really unfortunate.  Here is a workaround in the meantime for getting markers.

```
line([(1,2),(2,3)],marker=7,linestyle='')
```




---

archive/issue_comments_077630.json:
```json
{
    "body": "Incidentally, I think the `list_plot` syntax in 2 and 3 dims is because Mma uses this, right?  We'd need a deprecation period or to keep the alias.\n\nSee also #13830.",
    "created_at": "2012-12-14T16:22:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8570",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8570#issuecomment-77630",
    "user": "kcrisman"
}
```

Incidentally, I think the `list_plot` syntax in 2 and 3 dims is because Mma uses this, right?  We'd need a deprecation period or to keep the alias.

See also #13830.
