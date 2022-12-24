# Issue 5885: #5567 should throw a deprecation warning

archive/issues_005885.json:
```json
{
    "body": "Assignee: burcin\n\nCC:  jason\n\n#5567 fixes a bug, but in doing so, avoids the deprecation warning that should happen when the user types in\n\n```\nregion_plot([y>0,x>0,x^2+y^2<3], (-3, 3), (-3,3),plot_points=100,incol='gray').show(aspect_ratio=1)\n```\n\n\nSee #5413 for details on the deprecation warning.  This deprecation warning should be triggered when the code in the doctest of #5567 is run.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5885\n\n",
    "created_at": "2009-04-24T01:20:37Z",
    "labels": [
        "calculus",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.2",
    "title": "#5567 should throw a deprecation warning",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5885",
    "user": "jason"
}
```
Assignee: burcin

CC:  jason

#5567 fixes a bug, but in doing so, avoids the deprecation warning that should happen when the user types in

```
region_plot([y>0,x>0,x^2+y^2<3], (-3, 3), (-3,3),plot_points=100,incol='gray').show(aspect_ratio=1)
```


See #5413 for details on the deprecation warning.  This deprecation warning should be triggered when the code in the doctest of #5567 is run.

Issue created by migration from https://trac.sagemath.org/ticket/5885





---

archive/issue_comments_046527.json:
```json
{
    "body": "What alternate syntax for a region of this kind would be appropriate, though?  Anything requiring a lambda construction or a previous function declaration seems awkward.\n\nPerhaps the fix is to require variable declaration (e.g.\n\n```\nregion_plot([y>0,x>0,x^2+y^2<3], (x,-3, 3), (y,-3,3),plot_points=100,incol='gray').show(aspect_ratio=1)\n```\n\nbut otherwise keep equify and friends.  In particular, the current doctest is too symmetric - better would be\n\n```\nregion_plot([y>0,x>0,x^2+y^2<3], (x,-3, 4), (y,-4,3),plot_points=100,incol='gray').show(aspect_ratio=1)\n```\n\nsince otherwise it isn't clear that the correct variables are associated with the correct input range otherwise.\n\nI'm also changing the milestone to 4.0, concurrent with the Pynac switch.    If anyone posts a patch they can change it back :)  I don't think it's a blocker either, but will accept Jason's categorization in those terms due to the switch.",
    "created_at": "2009-04-30T01:04:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5885",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5885#issuecomment-46527",
    "user": "kcrisman"
}
```

What alternate syntax for a region of this kind would be appropriate, though?  Anything requiring a lambda construction or a previous function declaration seems awkward.

Perhaps the fix is to require variable declaration (e.g.

```
region_plot([y>0,x>0,x^2+y^2<3], (x,-3, 3), (y,-3,3),plot_points=100,incol='gray').show(aspect_ratio=1)
```

but otherwise keep equify and friends.  In particular, the current doctest is too symmetric - better would be

```
region_plot([y>0,x>0,x^2+y^2<3], (x,-3, 4), (y,-4,3),plot_points=100,incol='gray').show(aspect_ratio=1)
```

since otherwise it isn't clear that the correct variables are associated with the correct input range otherwise.

I'm also changing the milestone to 4.0, concurrent with the Pynac switch.    If anyone posts a patch they can change it back :)  I don't think it's a blocker either, but will accept Jason's categorization in those terms due to the switch.



---

archive/issue_comments_046528.json:
```json
{
    "body": "If we've released for 2 months without fixing this, it doesn't make sense to keep it as a blocker.",
    "created_at": "2009-06-15T23:26:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5885",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5885#issuecomment-46528",
    "user": "was"
}
```

If we've released for 2 months without fixing this, it doesn't make sense to keep it as a blocker.



---

archive/issue_comments_046529.json:
```json
{
    "body": "Changing priority from blocker to critical.",
    "created_at": "2009-06-15T23:26:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5885",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5885#issuecomment-46529",
    "user": "was"
}
```

Changing priority from blocker to critical.



---

archive/issue_comments_046530.json:
```json
{
    "body": "Given that #7809 has positive review and has changed this particular doctest, AND given that region_plot in this format has existed for close to a year with no complaints, and given that #7809 now makes clear what we *want* the behavior to be, I think it's time to close this ticket.  If jason or was concurs, then let's do it.",
    "created_at": "2010-01-08T16:23:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5885",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5885#issuecomment-46530",
    "user": "kcrisman"
}
```

Given that #7809 has positive review and has changed this particular doctest, AND given that region_plot in this format has existed for close to a year with no complaints, and given that #7809 now makes clear what we *want* the behavior to be, I think it's time to close this ticket.  If jason or was concurs, then let's do it.



---

archive/issue_comments_046531.json:
```json
{
    "body": "I concur, but for a totally different reason.  The deprecation warning is now thrown (probably because of the changes in #7809?):\n\n\n```\nsage: var('y')\ny\nsage: region_plot([y>0,x>0,x^2+y^2<3], (-3, 3), (-3,3),plot_points=100,incol='gray').show(aspect_ratio=1)\n/home/grout/sage/local/lib/python2.6/site-packages/sage/plot/contour_plot.py:565: DeprecationWarning: Unnamed ranges for more than one variable is deprecated and will be removed from a future release of Sage; you can used named ranges instead, like (x,0,2)\n  g, ranges = setup_for_eval_on_grid(f, [xrange, yrange], plot_points)\n\n\n```\n",
    "created_at": "2010-01-09T05:25:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5885",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5885#issuecomment-46531",
    "user": "jason"
}
```

I concur, but for a totally different reason.  The deprecation warning is now thrown (probably because of the changes in #7809?):


```
sage: var('y')
y
sage: region_plot([y>0,x>0,x^2+y^2<3], (-3, 3), (-3,3),plot_points=100,incol='gray').show(aspect_ratio=1)
/home/grout/sage/local/lib/python2.6/site-packages/sage/plot/contour_plot.py:565: DeprecationWarning: Unnamed ranges for more than one variable is deprecated and will be removed from a future release of Sage; you can used named ranges instead, like (x,0,2)
  g, ranges = setup_for_eval_on_grid(f, [xrange, yrange], plot_points)


```




---

archive/issue_comments_046532.json:
```json
{
    "body": "(to take care of a reviewer comment) -- I feel that we don't have to put in a DeprecationWarning doctest since the deprecation warning happens not in the region_plot function, but at a lower level, and it is already doctested there.\n\nI think this ticket can be closed as fixed once #7809 is merged.",
    "created_at": "2010-01-09T05:38:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5885",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5885#issuecomment-46532",
    "user": "jason"
}
```

(to take care of a reviewer comment) -- I feel that we don't have to put in a DeprecationWarning doctest since the deprecation warning happens not in the region_plot function, but at a lower level, and it is already doctested there.

I think this ticket can be closed as fixed once #7809 is merged.



---

archive/issue_comments_046533.json:
```json
{
    "body": "uh, I'll put this as \"needs review\", and maybe kcrisman can give it a positive review?",
    "created_at": "2010-01-09T05:38:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5885",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5885#issuecomment-46533",
    "user": "jason"
}
```

uh, I'll put this as "needs review", and maybe kcrisman can give it a positive review?



---

archive/issue_comments_046534.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-09T05:38:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5885",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5885#issuecomment-46534",
    "user": "jason"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_046535.json:
```json
{
    "body": "Sorry, I didn't see this recently.  Yes, we do get an appropriate deprecation warning.  I don't know that there is really an author or reviewer for this... just a closure.\n\nAlso, the plot is still one pixel off :)",
    "created_at": "2010-01-19T16:29:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5885",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5885#issuecomment-46535",
    "user": "kcrisman"
}
```

Sorry, I didn't see this recently.  Yes, we do get an appropriate deprecation warning.  I don't know that there is really an author or reviewer for this... just a closure.

Also, the plot is still one pixel off :)



---

archive/issue_comments_046536.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-19T16:29:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5885",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5885#issuecomment-46536",
    "user": "kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_046537.json:
```json
{
    "body": "Fixed due to #7809.",
    "created_at": "2010-01-22T21:42:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5885",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5885#issuecomment-46537",
    "user": "mvngu"
}
```

Fixed due to #7809.



---

archive/issue_comments_046538.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-22T21:42:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5885",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5885#issuecomment-46538",
    "user": "mvngu"
}
```

Resolution: fixed
