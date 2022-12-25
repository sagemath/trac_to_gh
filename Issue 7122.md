# Issue 7122: plot real part and imaginary part of function sqrt.

archive/issues_007122.json:
```json
{
    "body": "Assignee: @williamstein\n\nI try to plot a half-circle with the \n\n\n```\nvar('m')\nparametric_plot ([real(m+sqrt(1-m^2)), imaginary(m+sqrt(1-m^2))],m,-1,1)\n```\n \n\nand get a severe error.\n\nTheses plots are right :\n\n```\nplot([sqrt(m2+1)],m,0,6)\nplot(real (sqrt(m2+1)),m,0,6)\n```\n\n\nBut this one with AND real(...) or imaginary(...) AND list AND sqrt(...)  fails :\n\n\n```\nplot([real (sqrt(m2+1))],m,0,6)\n```\n\n\nOn devel-support kcrisman proposes :\n\n\nAfter looking at the traceback about an extra argument, I have a\nsneaky suspicion this is because sqrt takes an extra keyword prec,\nwhich perhaps is getting caught up in fast_float somehow.  What's\ninteresting is that the problem also only shows up for a list, so\nagain fast_float([]) is what's getting concerned.  Those who know how fast_float and the expression trees work will hopefully check this out as they get an opportunity.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7122\n\n",
    "created_at": "2009-10-05T15:15:11Z",
    "labels": [
        "component: graphics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.2",
    "title": "plot real part and imaginary part of function sqrt.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7122",
    "user": "https://trac.sagemath.org/admin/accounts/users/fmaltey"
}
```
Assignee: @williamstein

I try to plot a half-circle with the 


```
var('m')
parametric_plot ([real(m+sqrt(1-m^2)), imaginary(m+sqrt(1-m^2))],m,-1,1)
```
 

and get a severe error.

Theses plots are right :

```
plot([sqrt(m2+1)],m,0,6)
plot(real (sqrt(m2+1)),m,0,6)
```


But this one with AND real(...) or imaginary(...) AND list AND sqrt(...)  fails :


```
plot([real (sqrt(m2+1))],m,0,6)
```


On devel-support kcrisman proposes :


After looking at the traceback about an extra argument, I have a
sneaky suspicion this is because sqrt takes an extra keyword prec,
which perhaps is getting caught up in fast_float somehow.  What's
interesting is that the problem also only shows up for a list, so
again fast_float([]) is what's getting concerned.  Those who know how fast_float and the expression trees work will hopefully check this out as they get an opportunity.


Issue created by migration from https://trac.sagemath.org/ticket/7122





---

archive/issue_comments_058922.json:
```json
{
    "body": "I've attached a patch which fixes the error you get.  However, I don't think that's the right equation to draw a half circle since sqrt(1-m^2) is always going to be real for -1 <= m <= 1.",
    "created_at": "2009-10-05T17:27:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7122",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7122#issuecomment-58922",
    "user": "https://github.com/mwhansen"
}
```

I've attached a patch which fixes the error you get.  However, I don't think that's the right equation to draw a half circle since sqrt(1-m^2) is always going to be real for -1 <= m <= 1.



---

archive/issue_comments_058923.json:
```json
{
    "body": "Attachment [trac_7122.patch](tarball://root/attachments/some-uuid/ticket7122/trac_7122.patch) by @mwhansen created at 2009-10-05 17:27:49",
    "created_at": "2009-10-05T17:27:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7122",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7122#issuecomment-58923",
    "user": "https://github.com/mwhansen"
}
```

Attachment [trac_7122.patch](tarball://root/attachments/some-uuid/ticket7122/trac_7122.patch) by @mwhansen created at 2009-10-05 17:27:49



---

archive/issue_comments_058924.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-10-20T06:49:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7122",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7122#issuecomment-58924",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_058925.json:
```json
{
    "body": "Looks good, passes all the tests I can think of. \n\nIf it's significant enough that \n\n```\nsage: plot([real (sqrt(m^2-1))],m,0,6)\n```\n\nnow works, maybe there should be a doctest in plot/plot.py?\n\nOtherwise positive review.",
    "created_at": "2009-10-20T06:49:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7122",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7122#issuecomment-58925",
    "user": "https://github.com/kcrisman"
}
```

Looks good, passes all the tests I can think of. 

If it's significant enough that 

```
sage: plot([real (sqrt(m^2-1))],m,0,6)
```

now works, maybe there should be a doctest in plot/plot.py?

Otherwise positive review.



---

archive/issue_events_016834.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2009-10-21T04:04:19Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7122",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7122#event-16834"
}
```



---

archive/issue_comments_058926.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-10-21T04:04:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7122",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7122#issuecomment-58926",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed
