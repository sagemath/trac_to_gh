# Issue 2700: scaling y-axis of plots to fit the data

archive/issues_002700.json:
```json
{
    "body": "Assignee: @williamstein\n\n```\n>>  I have tried to plot a graphic in the notebook with a small scale (<1)\n>>  and it end up by showing up nothing:\n>>    sage: var('x')\n>>    sage: plot(sin(x), 0, 0.01)\n>>\n> \n> Try this:\n> \n> sage: plot(sin(x), 0, 0.01).show(0,0.01, 0, 0.01)\n> \n> The problem is plot's default scale isn't good enough.  using show you can force\n> something more useful.\n\n\n(turning this into a dev discussion :)\n\nYou know, we do evaluate the function for lots of points in the interval, so we ought to have a pretty intelligent idea of the max and min of the function.  This ought to let us get a pretty good guess at a ymin and ymax.  If we really wanted to get fancy, we could do a small statistical analysis to throw out outliers too.\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/2700\n\n",
    "created_at": "2008-03-28T17:13:40Z",
    "labels": [
        "component: graphics",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1",
    "title": "scaling y-axis of plots to fit the data",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2700",
    "user": "https://github.com/jasongrout"
}
```
Assignee: @williamstein

```
>>  I have tried to plot a graphic in the notebook with a small scale (<1)
>>  and it end up by showing up nothing:
>>    sage: var('x')
>>    sage: plot(sin(x), 0, 0.01)
>>
> 
> Try this:
> 
> sage: plot(sin(x), 0, 0.01).show(0,0.01, 0, 0.01)
> 
> The problem is plot's default scale isn't good enough.  using show you can force
> something more useful.


(turning this into a dev discussion :)

You know, we do evaluate the function for lots of points in the interval, so we ought to have a pretty intelligent idea of the max and min of the function.  This ought to let us get a pretty good guess at a ymin and ymax.  If we really wanted to get fancy, we could do a small statistical analysis to throw out outliers too.
```

Issue created by migration from https://trac.sagemath.org/ticket/2700





---

archive/issue_comments_018584.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-09-02T19:49:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2700",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2700#issuecomment-18584",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed



---

archive/issue_events_006311.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2008-09-02T19:49:18Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2700",
    "milestone": "sage-3.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2700#event-6311"
}
```



---

archive/issue_events_006312.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2008-09-02T19:49:18Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2700",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2700#event-6312"
}
```



---

archive/issue_comments_018585.json:
```json
{
    "body": "This was fixed by #3806.",
    "created_at": "2008-09-02T19:49:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2700",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2700#issuecomment-18585",
    "user": "https://github.com/mwhansen"
}
```

This was fixed by #3806.
