# Issue 3985: Asymptote plotting

archive/issues_003985.json:
```json
{
    "body": "Assignee: @williamstein\n\nPlotting functions like 1/x, tan, etc. have asymptotes essentially plotted in Sage at this point.  This is okay, except that the scale is way out of whack, so things look very odd.  Sage should either remove the asymptote piece of these plots somehow (how is not obvious) or fix the ymin and ymax in show so that it just looks like the asymptotes are plotted.  \nE.g.\n\n```\nsage: plot(tan,-20,20).show(ymin=-5, ymax=5) \n```\n\nexcept automatic detection of the ymin and ymax.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3985\n\n",
    "created_at": "2008-08-29T02:28:48Z",
    "labels": [
        "component: graphics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "Asymptote plotting",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3985",
    "user": "https://github.com/kcrisman"
}
```
Assignee: @williamstein

Plotting functions like 1/x, tan, etc. have asymptotes essentially plotted in Sage at this point.  This is okay, except that the scale is way out of whack, so things look very odd.  Sage should either remove the asymptote piece of these plots somehow (how is not obvious) or fix the ymin and ymax in show so that it just looks like the asymptotes are plotted.  
E.g.

```
sage: plot(tan,-20,20).show(ymin=-5, ymax=5) 
```

except automatic detection of the ymin and ymax.

Issue created by migration from https://trac.sagemath.org/ticket/3985





---

archive/issue_comments_028605.json:
```json
{
    "body": "Hmm, I am wondering if #3907 fixed this issue?\n\nCheers,\n\nMichael",
    "created_at": "2008-09-09T04:53:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3985",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3985#issuecomment-28605",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Hmm, I am wondering if #3907 fixed this issue?

Cheers,

Michael



---

archive/issue_comments_028606.json:
```json
{
    "body": "I doubt it, because e.g. the tangent example above usually won't get 'inf' or '-inf' as something in ydata; it just has weird things happen near asymptotes because of the adaptive plotting, and also will occasionally get random points that are really far from y=0.   I'll try it when 3.1.2 comes out, though.\n\nIt's actually kind of fun to evaluate the above command again and again, seeing what you get each time... If you try a few times you can get a ydata point that is 10000 or even more, which requires only that plot \"guesses\" a number within 10<sup>-5</sup> of pi/2 for the xdata...",
    "created_at": "2008-09-09T19:20:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3985",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3985#issuecomment-28606",
    "user": "https://github.com/kcrisman"
}
```

I doubt it, because e.g. the tangent example above usually won't get 'inf' or '-inf' as something in ydata; it just has weird things happen near asymptotes because of the adaptive plotting, and also will occasionally get random points that are really far from y=0.   I'll try it when 3.1.2 comes out, though.

It's actually kind of fun to evaluate the above command again and again, seeing what you get each time... If you try a few times you can get a ydata point that is 10000 or even more, which requires only that plot "guesses" a number within 10<sup>-5</sup> of pi/2 for the xdata...



---

archive/issue_comments_028607.json:
```json
{
    "body": "Just FYI, #6035 partially resolves this.  \n\nHowever, \n\n```\nsage: plot(tan,-20,20, detect_poles='show')\nsage: plot(tan,-20,20, detect_poles=True)\n```\n\nshows that 'show' still keeps the \"missing\" points (which include not just the asymptote but also the high slopes on either side) and that True doesn't create a uniform height as one might desire in the Description.  \n\nDescription changed to indicate this successful partial resolution, however!",
    "created_at": "2009-05-21T18:50:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3985",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3985#issuecomment-28607",
    "user": "https://github.com/kcrisman"
}
```

Just FYI, #6035 partially resolves this.  

However, 

```
sage: plot(tan,-20,20, detect_poles='show')
sage: plot(tan,-20,20, detect_poles=True)
```

shows that 'show' still keeps the "missing" points (which include not just the asymptote but also the high slopes on either side) and that True doesn't create a uniform height as one might desire in the Description.  

Description changed to indicate this successful partial resolution, however!



---

archive/issue_comments_028608.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2010-03-17T05:19:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3985",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3985#issuecomment-28608",
    "user": "https://github.com/jasongrout"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_028609.json:
```json
{
    "body": "See also #8341.",
    "created_at": "2013-01-14T15:42:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3985",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3985#issuecomment-28609",
    "user": "https://github.com/kcrisman"
}
```

See also #8341.
