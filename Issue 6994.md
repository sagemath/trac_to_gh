# Issue 6994: [with spkg, needs review] upgrade matplotlib to 0.99.1

archive/issues_006994.json:
```json
{
    "body": "Assignee: was\n\nCC:  kcrisman\n\nThe new matplotlib fixes *lots* of bugs, and incorporates some of our patches upstream too.  The new spkg is:\n\nhttp://sage.math.washington.edu/home/jason/matplotlib-0.99.1.spkg\n\nIssue created by migration from https://trac.sagemath.org/ticket/6994\n\n",
    "created_at": "2009-09-22T19:44:25Z",
    "labels": [
        "graphics",
        "major",
        "bug"
    ],
    "title": "[with spkg, needs review] upgrade matplotlib to 0.99.1",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6994",
    "user": "jason"
}
```
Assignee: was

CC:  kcrisman

The new matplotlib fixes *lots* of bugs, and incorporates some of our patches upstream too.  The new spkg is:

http://sage.math.washington.edu/home/jason/matplotlib-0.99.1.spkg

Issue created by migration from https://trac.sagemath.org/ticket/6994





---

archive/issue_comments_057847.json:
```json
{
    "body": "Apparently 0.99.1 has a special osx makefile, which I don't think we are using.  Should we use it?",
    "created_at": "2009-09-22T19:48:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6994",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6994#issuecomment-57847",
    "user": "jason"
}
```

Apparently 0.99.1 has a special osx makefile, which I don't think we are using.  Should we use it?



---

archive/issue_comments_057848.json:
```json
{
    "body": "(if so, someone with osx ought to take a look at this)",
    "created_at": "2009-09-22T19:49:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6994",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6994#issuecomment-57848",
    "user": "jason"
}
```

(if so, someone with osx ought to take a look at this)



---

archive/issue_comments_057849.json:
```json
{
    "body": "Hmm, well, it seems to be working fine on my copy of OSX.5.8.  Maybe someone else who knows something about makefiles should comment on this...\n\nMaybe this would be a good time to improve that documentation about things like\n\n```\nsage: plot(x^3,-10,-1)\n```\n\nwhich almost looks like they should intersect but they don't... that's already a ticket somewhere.\n\nAnyway, I don't have time to finish a review now, but so far everything looks fine, and as I said it built fine.",
    "created_at": "2009-09-22T20:00:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6994",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6994#issuecomment-57849",
    "user": "kcrisman"
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

archive/issue_comments_057850.json:
```json
{
    "body": "I get the following failure, probably due to a deprecated module...\n\n```\nsage -t  \"devel/sage/sage/plot/colors.py\"                   \n**********************************************************************\nFile \"/Users/.../sage-4.1.2.alpha2/devel/sage/sage/plot/colors.py\", line 193:\n    sage: graphs.DodecahedralGraph().show(vertex_colors=vertex_colors)\nException raised:\n    Traceback (most recent call last):\n<snip>\n      File \"/Users/.../sage-4.1.2.alpha2/local/lib/python/site-packages/matplotlib/backends/tkagg.py\", line 1, in <module>\n        import _tkagg\n    ImportError: No module named _tkagg\n*****************************************************************\n```\n\nSimilar ones in plot.py in lines 213 ff. and around line 1960, as well as in scatterplot.py. \n\nThere are also a couple failures in plot.py related to savefig and fig.  Otherwise everything seem okay.",
    "created_at": "2009-09-22T20:37:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6994",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6994#issuecomment-57850",
    "user": "kcrisman"
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

archive/issue_comments_057851.json:
```json
{
    "body": "Congratulations; you found a bug in the release of matplotlib.  They errantly included a config file that should have been deleted.\n\nI've updated the spkg, at the same URL as above.  Make sure you install it with \"sage -f\" to overwrite the previous one.",
    "created_at": "2009-09-22T22:44:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6994",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6994#issuecomment-57851",
    "user": "jason"
}
```

Congratulations; you found a bug in the release of matplotlib.  They errantly included a config file that should have been deleted.

I've updated the spkg, at the same URL as above.  Make sure you install it with "sage -f" to overwrite the previous one.



---

archive/issue_comments_057852.json:
```json
{
    "body": "Okay, now all is well.  You may want to let Minh know about some of the bugfixes if they are notable for Sage, for the release tour.",
    "created_at": "2009-09-23T01:25:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6994",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6994#issuecomment-57852",
    "user": "kcrisman"
}
```

Okay, now all is well.  You may want to let Minh know about some of the bugfixes if they are notable for Sage, for the release tour.



---

archive/issue_comments_057853.json:
```json
{
    "body": "See #7022 for a port to OS X 10.6.",
    "created_at": "2009-09-27T04:05:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6994",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6994#issuecomment-57853",
    "user": "mvngu"
}
```

See #7022 for a port to OS X 10.6.



---

archive/issue_comments_057854.json:
```json
{
    "body": "I think that this should be closed now that #7022 is in.",
    "created_at": "2009-10-15T09:41:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6994",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6994#issuecomment-57854",
    "user": "mhansen"
}
```

I think that this should be closed now that #7022 is in.



---

archive/issue_comments_057855.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-10-15T09:41:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6994",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6994#issuecomment-57855",
    "user": "mhansen"
}
```

Resolution: fixed
