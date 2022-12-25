# Issue 8570: Allow "marker" option to be passed to matplotlib on list_plot() and point()

archive/issues_008570.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @jasongrout @kcrisman\n\nKeywords: plot marker\n\nCurrently, there's no obvious way to pass the marker option to matplotlib when plotting individual points, which would be mostly with this option.\n\nIt appears that plot() has deviated from other plot types, since it does allow the marker option, but apparently only for function plots.\n\nusing plot(points(point_list),marker='x') ignores the marker option\nusing list_plot(point_list,marker='x') or points(point_list,marker='x') gives a warning:\n  verbose 0 (136: primitive.py, options) WARNING: Ignoring option 'marker'=x\nbut displays the points nevertheless, though ignoring the marker option.\n\nAlso, setting plot.options['marker'] = 'x' or Graphics().SHOW_OPTIONS['marker'] = 'x' do not work.\n\nSomewhat related to #4529, #1431 and #5448, which seem to be related to not passing kwargs to matplotlib.\n\nSo far, I haven't been able to find a way to seamless join matplotlib's system with the sage.plot options.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8570\n\n",
    "created_at": "2010-03-21T15:17:23Z",
    "labels": [
        "component: graphics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "Allow \"marker\" option to be passed to matplotlib on list_plot() and point()",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8570",
    "user": "https://trac.sagemath.org/admin/accounts/users/ronanpaixao"
}
```
Assignee: @williamstein

CC:  @jasongrout @kcrisman

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

archive/issue_comments_077495.json:
```json
{
    "body": "I think it would be a good design decision to just bundle the plotjoined=True features in with line() (i.e., eliminate the plotjoined=True features in listplot, and just make listplot about plotting points).",
    "created_at": "2010-06-04T04:34:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8570",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8570#issuecomment-77495",
    "user": "https://github.com/jasongrout"
}
```

I think it would be a good design decision to just bundle the plotjoined=True features in with line() (i.e., eliminate the plotjoined=True features in listplot, and just make listplot about plotting points).



---

archive/issue_comments_077496.json:
```json
{
    "body": "In fact, I think a better design decision would be to completely deprecate list_plot.  Replace it with line() in the connected case, and scatter_plot in the disconnected case.  Each of those commands does better than list_plot.",
    "created_at": "2010-06-04T04:55:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8570",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8570#issuecomment-77496",
    "user": "https://github.com/jasongrout"
}
```

In fact, I think a better design decision would be to completely deprecate list_plot.  Replace it with line() in the connected case, and scatter_plot in the disconnected case.  Each of those commands does better than list_plot.



---

archive/issue_comments_077497.json:
```json
{
    "body": "For that matter, the listplot3d should maybe be called surface_plot() instead, as it is clearer what it is plotting.",
    "created_at": "2010-06-04T05:06:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8570",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8570#issuecomment-77497",
    "user": "https://github.com/jasongrout"
}
```

For that matter, the listplot3d should maybe be called surface_plot() instead, as it is clearer what it is plotting.



---

archive/issue_comments_077498.json:
```json
{
    "body": "Another reason for the deprecation: I think every other graphics command is named after the *output* (like \"line\"), not the *input* (like \"list_plot\")",
    "created_at": "2010-06-05T00:53:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8570",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8570#issuecomment-77498",
    "user": "https://github.com/jasongrout"
}
```

Another reason for the deprecation: I think every other graphics command is named after the *output* (like "line"), not the *input* (like "list_plot")



---

archive/issue_comments_077499.json:
```json
{
    "body": "In fact, scatter_plot should be deprecated in favor of just points().  If we do that, then we need to make points() have more options (like edgecolor, markerstyle, etc.).",
    "created_at": "2010-06-05T19:48:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8570",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8570#issuecomment-77499",
    "user": "https://github.com/jasongrout"
}
```

In fact, scatter_plot should be deprecated in favor of just points().  If we do that, then we need to make points() have more options (like edgecolor, markerstyle, etc.).



---

archive/issue_comments_077500.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2010-06-05T19:48:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8570",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8570#issuecomment-77500",
    "user": "https://github.com/jasongrout"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_077501.json:
```json
{
    "body": "Just noting that this is still really unfortunate.  Here is a workaround in the meantime for getting markers.\n\n```\nline([(1,2),(2,3)],marker=7,linestyle='')\n```\n",
    "created_at": "2012-01-25T03:46:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8570",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8570#issuecomment-77501",
    "user": "https://github.com/kcrisman"
}
```

Just noting that this is still really unfortunate.  Here is a workaround in the meantime for getting markers.

```
line([(1,2),(2,3)],marker=7,linestyle='')
```




---

archive/issue_comments_077502.json:
```json
{
    "body": "Incidentally, I think the `list_plot` syntax in 2 and 3 dims is because Mma uses this, right?  We'd need a deprecation period or to keep the alias.\n\nSee also #13830.",
    "created_at": "2012-12-14T16:22:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8570",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8570#issuecomment-77502",
    "user": "https://github.com/kcrisman"
}
```

Incidentally, I think the `list_plot` syntax in 2 and 3 dims is because Mma uses this, right?  We'd need a deprecation period or to keep the alias.

See also #13830.



---

archive/issue_events_020680.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8570",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8570#event-20680"
}
```



---

archive/issue_events_020681.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8570",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8570#event-20681"
}
```



---

archive/issue_events_020682.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8570",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8570#event-20682"
}
```



---

archive/issue_events_020683.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8570",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8570#event-20683"
}
```



---

archive/issue_events_020684.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8570",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8570#event-20684"
}
```



---

archive/issue_events_020685.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8570",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8570#event-20685"
}
```



---

archive/issue_events_020686.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8570",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8570#event-20686"
}
```
