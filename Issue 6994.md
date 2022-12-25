# Issue 6994: [with spkg, needs review] upgrade matplotlib to 0.99.1

archive/issues_006994.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @kcrisman\n\nThe new matplotlib fixes *lots* of bugs, and incorporates some of our patches upstream too.  The new spkg is:\n\nhttp://sage.math.washington.edu/home/jason/matplotlib-0.99.1.spkg\n\nIssue created by migration from https://trac.sagemath.org/ticket/6994\n\n",
    "created_at": "2009-09-22T19:44:25Z",
    "labels": [
        "component: graphics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.2",
    "title": "[with spkg, needs review] upgrade matplotlib to 0.99.1",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6994",
    "user": "https://github.com/jasongrout"
}
```
Assignee: @williamstein

CC:  @kcrisman

The new matplotlib fixes *lots* of bugs, and incorporates some of our patches upstream too.  The new spkg is:

http://sage.math.washington.edu/home/jason/matplotlib-0.99.1.spkg

Issue created by migration from https://trac.sagemath.org/ticket/6994





---

archive/issue_comments_057739.json:
```json
{
    "body": "Apparently 0.99.1 has a special osx makefile, which I don't think we are using.  Should we use it?",
    "created_at": "2009-09-22T19:48:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6994",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6994#issuecomment-57739",
    "user": "https://github.com/jasongrout"
}
```

Apparently 0.99.1 has a special osx makefile, which I don't think we are using.  Should we use it?



---

archive/issue_comments_057740.json:
```json
{
    "body": "(if so, someone with osx ought to take a look at this)",
    "created_at": "2009-09-22T19:49:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6994",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6994#issuecomment-57740",
    "user": "https://github.com/jasongrout"
}
```

(if so, someone with osx ought to take a look at this)



---

archive/issue_comments_057741.json:
```json
{
    "body": "Hmm, well, it seems to be working fine on my copy of OSX.5.8.  Maybe someone else who knows something about makefiles should comment on this...\n\nMaybe this would be a good time to improve that documentation about things like\n\n```\nsage: plot(x^3,-10,-1)\n```\n\nwhich almost looks like they should intersect but they don't... that's already a ticket somewhere.\n\nAnyway, I don't have time to finish a review now, but so far everything looks fine, and as I said it built fine.",
    "created_at": "2009-09-22T20:00:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6994",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6994#issuecomment-57741",
    "user": "https://github.com/kcrisman"
}
```

Hmm, well, it seems to be working fine on my copy of OSX.5.8.  Maybe someone else who knows something about makefiles should comment on this...

Maybe this would be a good time to improve that documentation about things like

```
sage: plot(x^3,-10,-1)
```

which almost looks like they should intersect but they don't... that's already a ticket somewhere.

Anyway, I don't have time to finish a review now, but so far everything looks fine, and as I said it built fine.



---

archive/issue_comments_057742.json:
```json
{
    "body": "I get the following failure, probably due to a deprecated module...\n\n```\nsage -t  \"devel/sage/sage/plot/colors.py\"                   \n**********************************************************************\nFile \"/Users/.../sage-4.1.2.alpha2/devel/sage/sage/plot/colors.py\", line 193:\n    sage: graphs.DodecahedralGraph().show(vertex_colors=vertex_colors)\nException raised:\n    Traceback (most recent call last):\n<snip>\n      File \"/Users/.../sage-4.1.2.alpha2/local/lib/python/site-packages/matplotlib/backends/tkagg.py\", line 1, in <module>\n        import _tkagg\n    ImportError: No module named _tkagg\n*****************************************************************\n```\n\nSimilar ones in plot.py in lines 213 ff. and around line 1960, as well as in scatterplot.py. \n\nThere are also a couple failures in plot.py related to savefig and fig.  Otherwise everything seem okay.",
    "created_at": "2009-09-22T20:37:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6994",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6994#issuecomment-57742",
    "user": "https://github.com/kcrisman"
}
```

I get the following failure, probably due to a deprecated module...

```
sage -t  "devel/sage/sage/plot/colors.py"                   
**********************************************************************
File "/Users/.../sage-4.1.2.alpha2/devel/sage/sage/plot/colors.py", line 193:
    sage: graphs.DodecahedralGraph().show(vertex_colors=vertex_colors)
Exception raised:
    Traceback (most recent call last):
<snip>
      File "/Users/.../sage-4.1.2.alpha2/local/lib/python/site-packages/matplotlib/backends/tkagg.py", line 1, in <module>
        import _tkagg
    ImportError: No module named _tkagg
*****************************************************************
```

Similar ones in plot.py in lines 213 ff. and around line 1960, as well as in scatterplot.py. 

There are also a couple failures in plot.py related to savefig and fig.  Otherwise everything seem okay.



---

archive/issue_comments_057743.json:
```json
{
    "body": "Congratulations; you found a bug in the release of matplotlib.  They errantly included a config file that should have been deleted.\n\nI've updated the spkg, at the same URL as above.  Make sure you install it with \"sage -f\" to overwrite the previous one.",
    "created_at": "2009-09-22T22:44:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6994",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6994#issuecomment-57743",
    "user": "https://github.com/jasongrout"
}
```

Congratulations; you found a bug in the release of matplotlib.  They errantly included a config file that should have been deleted.

I've updated the spkg, at the same URL as above.  Make sure you install it with "sage -f" to overwrite the previous one.



---

archive/issue_comments_057744.json:
```json
{
    "body": "Okay, now all is well.  You may want to let Minh know about some of the bugfixes if they are notable for Sage, for the release tour.",
    "created_at": "2009-09-23T01:25:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6994",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6994#issuecomment-57744",
    "user": "https://github.com/kcrisman"
}
```

Okay, now all is well.  You may want to let Minh know about some of the bugfixes if they are notable for Sage, for the release tour.



---

archive/issue_comments_057745.json:
```json
{
    "body": "See #7022 for a port to OS X 10.6.",
    "created_at": "2009-09-27T04:05:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6994",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6994#issuecomment-57745",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

See #7022 for a port to OS X 10.6.



---

archive/issue_comments_057746.json:
```json
{
    "body": "I think that this should be closed now that #7022 is in.",
    "created_at": "2009-10-15T09:41:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6994",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6994#issuecomment-57746",
    "user": "https://github.com/mwhansen"
}
```

I think that this should be closed now that #7022 is in.



---

archive/issue_events_007218.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2009-10-15T09:41:56Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6994",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6994#event-7218"
}
```



---

archive/issue_comments_057747.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-10-15T09:41:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6994",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6994#issuecomment-57747",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed
