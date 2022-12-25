# Issue 8125: problem with "text"

archive/issues_008125.json:
```json
{
    "body": "Assignee: @williamstein\n\nIn Sage 4.3.2.alpha0:\n\n```\nsage: text(r\"$\\left(2 a=b\\right)$\", (2,3))   # works fine \nsage: text(r\"$(2 \\, a=b)$\", (2,3))   # works fine \nsage: text(r\"$\\left(2 \\, a=b\\right)$\", (2,3))   # error! \nTraceback (click to the left of this block for traceback) \n... \nAttributeError: 'Kern' object has no attribute 'height' \n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8125\n\n",
    "created_at": "2010-01-29T21:09:34Z",
    "labels": [
        "component: graphics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "problem with \"text\"",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8125",
    "user": "https://github.com/jhpalmieri"
}
```
Assignee: @williamstein

In Sage 4.3.2.alpha0:

```
sage: text(r"$\left(2 a=b\right)$", (2,3))   # works fine 
sage: text(r"$(2 \, a=b)$", (2,3))   # works fine 
sage: text(r"$\left(2 \, a=b\right)$", (2,3))   # error! 
Traceback (click to the left of this block for traceback) 
... 
AttributeError: 'Kern' object has no attribute 'height' 
```


Issue created by migration from https://trac.sagemath.org/ticket/8125





---

archive/issue_comments_071309.json:
```json
{
    "body": "This seems to be a bug in matplotlib; I just reported it to the matplotlib-devel mailing list, and I'll report any answers I get.\n\nMeanwhile, this arises in \"real life\" as follows:\n\n```\nsage: var(\"y R\") \nsage: a(y,R) = pi * (2*R - y) * y \nsage: latex(a(y,R))\n{\\left(2 \\, R - y\\right)} \\pi y\n```\nTherefore \n\n```\nsage: lbl = text(r\"$\\int \\  \" + latex(a(y,R)) + \"$\",(3,20)) \n```\nwon't work with matplotlib.  Should we get rid of the \"\\,\" in the latex output?",
    "created_at": "2010-01-30T01:25:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8125",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8125#issuecomment-71309",
    "user": "https://github.com/jhpalmieri"
}
```

This seems to be a bug in matplotlib; I just reported it to the matplotlib-devel mailing list, and I'll report any answers I get.

Meanwhile, this arises in "real life" as follows:

```
sage: var("y R") 
sage: a(y,R) = pi * (2*R - y) * y 
sage: latex(a(y,R))
{\left(2 \, R - y\right)} \pi y
```
Therefore 

```
sage: lbl = text(r"$\int \  " + latex(a(y,R)) + "$",(3,20)) 
```
won't work with matplotlib.  Should we get rid of the "\," in the latex output?



---

archive/issue_comments_071310.json:
```json
{
    "body": "Any response?",
    "created_at": "2010-07-27T17:35:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8125",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8125#issuecomment-71310",
    "user": "https://github.com/kcrisman"
}
```

Any response?



---

archive/issue_comments_071311.json:
```json
{
    "body": "No response at all.   From python:\n\n```\n>>> import pylab\n>>> pylab.text(0.2, 0.2, r\"$\\left(2a = b\\right)$\")\n<matplotlib.text.Text object at 0x1020aa450>\n>>> pylab.savefig('a.png')\n>>> pylab.text(0.2, 0.2, r\"$(2a \\, = b)$\")\n<matplotlib.text.Text object at 0x101e22a50>\n>>> pylab.savefig('b.png')\n>>> pylab.text(0.2, 0.2, r\"$\\left(2a \\, = b\\right)$\")\n<matplotlib.text.Text object at 0x1020b5750>\n>>> pylab.savefig('c.png')\nBOOM\n```\nCombining `\\left(`, `\\right)}]}, and {{{\\,` seems to lead to problems.  So now what?  Do we get rid of the `\\,`?",
    "created_at": "2010-07-27T17:45:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8125",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8125#issuecomment-71311",
    "user": "https://github.com/jhpalmieri"
}
```

No response at all.   From python:

```
>>> import pylab
>>> pylab.text(0.2, 0.2, r"$\left(2a = b\right)$")
<matplotlib.text.Text object at 0x1020aa450>
>>> pylab.savefig('a.png')
>>> pylab.text(0.2, 0.2, r"$(2a \, = b)$")
<matplotlib.text.Text object at 0x101e22a50>
>>> pylab.savefig('b.png')
>>> pylab.text(0.2, 0.2, r"$\left(2a \, = b\right)$")
<matplotlib.text.Text object at 0x1020b5750>
>>> pylab.savefig('c.png')
BOOM
```
Combining `\left(`, `\right)}]}, and {{{\,` seems to lead to problems.  So now what?  Do we get rid of the `\,`?



---

archive/issue_comments_071312.json:
```json
{
    "body": "Changing keywords from \"\" to \"matplotlib\".",
    "created_at": "2010-10-21T04:50:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8125",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8125#issuecomment-71312",
    "user": "https://github.com/jhpalmieri"
}
```

Changing keywords from "" to "matplotlib".



---

archive/issue_comments_071313.json:
```json
{
    "body": "This is still an issue in Sage 4.6.alpha3: it has not been fixed in matplotlib 1.0.0.",
    "created_at": "2010-10-21T04:50:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8125",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8125#issuecomment-71313",
    "user": "https://github.com/jhpalmieri"
}
```

This is still an issue in Sage 4.6.alpha3: it has not been fixed in matplotlib 1.0.0.



---

archive/issue_events_019459.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mdboom",
    "created_at": "2011-03-23T23:48:47Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8125",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8125#event-19459"
}
```



---

archive/issue_comments_071314.json:
```json
{
    "body": "Fixed by this pull request in matplotlib:\n\n[https://github.com/matplotlib/matplotlib/pull/52](https://github.com/matplotlib/matplotlib/pull/52)\n\nThis will make it into the next matplotlib bugfix release.",
    "created_at": "2011-03-23T23:48:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8125",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8125#issuecomment-71314",
    "user": "https://trac.sagemath.org/admin/accounts/users/mdboom"
}
```

Fixed by this pull request in matplotlib:

[https://github.com/matplotlib/matplotlib/pull/52](https://github.com/matplotlib/matplotlib/pull/52)

This will make it into the next matplotlib bugfix release.



---

archive/issue_comments_071315.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-03-23T23:48:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8125",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8125#issuecomment-71315",
    "user": "https://trac.sagemath.org/admin/accounts/users/mdboom"
}
```

Resolution: fixed



---

archive/issue_comments_071316.json:
```json
{
    "body": "Changing status from closed to new.",
    "created_at": "2011-03-24T00:19:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8125",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8125#issuecomment-71316",
    "user": "https://github.com/mwhansen"
}
```

Changing status from closed to new.



---

archive/issue_events_019460.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2011-03-24T00:19:03Z",
    "event": "reopened",
    "issue": "https://github.com/sagemath/sagetest/issues/8125",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8125#event-19460"
}
```



---

archive/issue_comments_071317.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2011-03-24T00:19:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8125",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8125#issuecomment-71317",
    "user": "https://github.com/mwhansen"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_071318.json:
```json
{
    "body": "We keep tickets open until the fix has actually gone into a Sage release.",
    "created_at": "2011-03-24T00:19:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8125",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8125#issuecomment-71318",
    "user": "https://github.com/mwhansen"
}
```

We keep tickets open until the fix has actually gone into a Sage release.



---

archive/issue_events_019461.json:
```json
{
    "actor": "https://github.com/jhpalmieri",
    "created_at": "2012-03-21T21:16:20Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8125",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8125#event-19461"
}
```



---

archive/issue_comments_071319.json:
```json
{
    "body": "This works now; it must be in matplotlib 1.1.0 (or earlier).  So this ticket can be closed.",
    "created_at": "2012-03-21T21:16:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8125",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8125#issuecomment-71319",
    "user": "https://github.com/jhpalmieri"
}
```

This works now; it must be in matplotlib 1.1.0 (or earlier).  So this ticket can be closed.



---

archive/issue_comments_071320.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2012-03-21T21:16:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8125",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8125#issuecomment-71320",
    "user": "https://github.com/jhpalmieri"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_071321.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2012-03-21T21:16:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8125",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8125#issuecomment-71321",
    "user": "https://github.com/jhpalmieri"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_071322.json:
```json
{
    "body": "Resolution: worksforme",
    "created_at": "2012-04-04T13:23:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8125",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8125#issuecomment-71322",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: worksforme



---

archive/issue_events_019462.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2012-04-04T13:23:16Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8125",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8125#event-19462"
}
```
