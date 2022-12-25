# Issue 5553: allow vertical slopes in slope field plots

archive/issues_005553.json:
```json
{
    "body": "Assignee: @williamstein\n\n```\nplot_slope_field(x/y, (x,-2,2), (y,-2,2)).show(aspect_ratio=1)\n```\ncurrently won't show the vertical slopes at y=0, x nonzero, but there is no mathematical reason it shouldn't, so this should be fixed.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5553\n\n",
    "created_at": "2009-03-17T20:59:17Z",
    "labels": [
        "component: graphics",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "allow vertical slopes in slope field plots",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5553",
    "user": "https://github.com/kcrisman"
}
```
Assignee: @williamstein

```
plot_slope_field(x/y, (x,-2,2), (y,-2,2)).show(aspect_ratio=1)
```
currently won't show the vertical slopes at y=0, x nonzero, but there is no mathematical reason it shouldn't, so this should be fixed.

Issue created by migration from https://trac.sagemath.org/ticket/5553





---

archive/issue_comments_043110.json:
```json
{
    "body": "plot_vector_field is already fixed.  See #5259.",
    "created_at": "2009-03-18T07:04:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5553",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5553#issuecomment-43110",
    "user": "https://github.com/jasongrout"
}
```

plot_vector_field is already fixed.  See #5259.



---

archive/issue_comments_043111.json:
```json
{
    "body": "That said, it'd be great to fix plot_slope_field to detect when you have a vertical slope and have it change things accordingly.  I think this should be easy: just see what vectors have finite X, infinite Y, and set them to be zero X, one Y.",
    "created_at": "2009-03-18T07:07:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5553",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5553#issuecomment-43111",
    "user": "https://github.com/jasongrout"
}
```

That said, it'd be great to fix plot_slope_field to detect when you have a vertical slope and have it change things accordingly.  I think this should be easy: just see what vectors have finite X, infinite Y, and set them to be zero X, one Y.



---

archive/issue_comments_043112.json:
```json
{
    "body": "I see, I thought that there was also a question of allowing infinite vectors, which I thought was weird.  I didn't realize it didn't return a plot at *all* before!\n\nYes, so I will change the summary and description of this to fixing plot_slope_field.  The problem is that it will be a sort of messy hack, unless it's dealt with in the plot_vector_field code using a keyword (I attempted to start this), but then you are trying to catch something that looks like (1/inf,inf/inf=NaN), which is a little tricky.  But doing it in plot_slope_field means you might as well just do all the stuff in plot_vector_field there, since you'll have to catch individual vectors anyway - which is annoying, since it seems redundant.",
    "created_at": "2009-03-18T14:23:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5553",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5553#issuecomment-43112",
    "user": "https://github.com/kcrisman"
}
```

I see, I thought that there was also a question of allowing infinite vectors, which I thought was weird.  I didn't realize it didn't return a plot at *all* before!

Yes, so I will change the summary and description of this to fixing plot_slope_field.  The problem is that it will be a sort of messy hack, unless it's dealt with in the plot_vector_field code using a keyword (I attempted to start this), but then you are trying to catch something that looks like (1/inf,inf/inf=NaN), which is a little tricky.  But doing it in plot_slope_field means you might as well just do all the stuff in plot_vector_field there, since you'll have to catch individual vectors anyway - which is annoying, since it seems redundant.



---

archive/issue_comments_043113.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2010-03-17T05:28:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5553",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5553#issuecomment-43113",
    "user": "https://github.com/jasongrout"
}
```

Changing type from defect to enhancement.



---

archive/issue_events_013060.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5553",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5553#event-13060"
}
```



---

archive/issue_events_013061.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5553",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5553#event-13061"
}
```



---

archive/issue_events_013062.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5553",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5553#event-13062"
}
```



---

archive/issue_events_013063.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5553",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5553#event-13063"
}
```



---

archive/issue_events_013064.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5553",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5553#event-13064"
}
```



---

archive/issue_events_013065.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5553",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5553#event-13065"
}
```



---

archive/issue_events_013066.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5553",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5553#event-13066"
}
```
