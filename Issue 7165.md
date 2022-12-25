# Issue 7165: sage fails to plot a quarter circle when it should

archive/issues_007165.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @kcrisman\n\nI use sage 4.1.2alpha4. This plot is right with this version :\n\n`parametric_plot([real(exp(i*m)),imaginary(exp(i*m))],m,0,7)`\n\nI apply the patch 7122 by copy/paste in emacs and run sage -br.\nNow this plot is also right, it draw a half-circle :\n\n`parametric_plot([real(m+sqrt(m<sup>2-1)),imaginary(m+sqrt(m</sup>2-1))],m,-5,5)` \n\nI also get it by this function :\n\n```\ndef solve2pplot (eq) : return [real(eq.rhs()),imaginary(eq.rhs())]\nres = solve(z^2+2*m*z+1,z)\nparametric_plot (solve2pplot (res[0]), m, -5,5)\n```\n\nNow I solve this 4 degree equation. The solve is right with sqrt at 2 levels.\n\nBut I get an error in the parametric_plot :\n\n```\nres = solve(z^4+2*m*z^2+1,z)\nparametric_plot (solve2pplot (res[0]), m, -5,5)\n```\n\nThe local `solve2pplot(res[0])` generates a long formula.\n\nreal axe and imaginary axe are right. \n\nBut sage doesn't plot the quarter-circle between axes at position 1=(1,0) and i=(0,1) and claims `failed to evaluate function at 40 points`. So the plot is a line between the 2 axes.\n\n\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7165\n\n",
    "closed_at": "2020-01-09T23:44:40Z",
    "created_at": "2009-10-09T17:33:18Z",
    "labels": [
        "component: graphics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-9.1",
    "title": "sage fails to plot a quarter circle when it should",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7165",
    "user": "https://trac.sagemath.org/admin/accounts/users/fmaltey"
}
```
Assignee: @williamstein

CC:  @kcrisman

I use sage 4.1.2alpha4. This plot is right with this version :

`parametric_plot([real(exp(i*m)),imaginary(exp(i*m))],m,0,7)`

I apply the patch 7122 by copy/paste in emacs and run sage -br.
Now this plot is also right, it draw a half-circle :

`parametric_plot([real(m+sqrt(m<sup>2-1)),imaginary(m+sqrt(m</sup>2-1))],m,-5,5)` 

I also get it by this function :

```
def solve2pplot (eq) : return [real(eq.rhs()),imaginary(eq.rhs())]
res = solve(z^2+2*m*z+1,z)
parametric_plot (solve2pplot (res[0]), m, -5,5)
```

Now I solve this 4 degree equation. The solve is right with sqrt at 2 levels.

But I get an error in the parametric_plot :

```
res = solve(z^4+2*m*z^2+1,z)
parametric_plot (solve2pplot (res[0]), m, -5,5)
```

The local `solve2pplot(res[0])` generates a long formula.

real axe and imaginary axe are right. 

But sage doesn't plot the quarter-circle between axes at position 1=(1,0) and i=(0,1) and claims `failed to evaluate function at 40 points`. So the plot is a line between the 2 axes.





Issue created by migration from https://trac.sagemath.org/ticket/7165





---

archive/issue_comments_059282.json:
```json
{
    "body": "I browse the two previous expressions real(...) and imaginary(...), and test real(sqrt(...)).\n\nTheses calculus are right and remain real. \n\n```\nreal(sqrt(m)) ; real(sqrt(I*m)) ; real(sqrt(I*m+1)) # are right \n```\n\nBut this one is the shorter that contains complex expressions :\n\n```\nreal(sqrt(sqrt(m)+i+1))\n```\n\nThe outer sqrt(...) assume that the inner sqrt is obvious ; so sqrt(m)+i+1 remains, even if it's a complex expression.\nThen plot fails with this internal complex computation.\n\n```\nplot (real(sqrt(m)+i+1),m,-3,3) # fails with a system error\nplot (real(m+i+1),m,-3,3) # is a pretty line\n```",
    "created_at": "2009-10-25T12:10:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7165",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7165#issuecomment-59282",
    "user": "https://trac.sagemath.org/admin/accounts/users/fmaltey"
}
```

I browse the two previous expressions real(...) and imaginary(...), and test real(sqrt(...)).

Theses calculus are right and remain real. 

```
real(sqrt(m)) ; real(sqrt(I*m)) ; real(sqrt(I*m+1)) # are right 
```

But this one is the shorter that contains complex expressions :

```
real(sqrt(sqrt(m)+i+1))
```

The outer sqrt(...) assume that the inner sqrt is obvious ; so sqrt(m)+i+1 remains, even if it's a complex expression.
Then plot fails with this internal complex computation.

```
plot (real(sqrt(m)+i+1),m,-3,3) # fails with a system error
plot (real(m+i+1),m,-3,3) # is a pretty line
```



---

archive/issue_comments_059283.json:
```json
{
    "body": "The `plot (real(sqrt(m)+i+1),m,-3,3)` now works, probably as a result of #7614.  However, I don't think the original question is addressed.",
    "created_at": "2010-01-01T18:28:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7165",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7165#issuecomment-59283",
    "user": "https://github.com/jasongrout"
}
```

The `plot (real(sqrt(m)+i+1),m,-3,3)` now works, probably as a result of #7614.  However, I don't think the original question is addressed.



---

archive/issue_events_016940.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7165",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7165#event-16940"
}
```



---

archive/issue_events_016941.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7165",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7165#event-16941"
}
```



---

archive/issue_events_016942.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7165",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7165#event-16942"
}
```



---

archive/issue_events_016943.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7165",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7165#event-16943"
}
```



---

archive/issue_events_016944.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7165",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7165#event-16944"
}
```



---

archive/issue_events_016945.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7165",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7165#event-16945"
}
```



---

archive/issue_events_016946.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7165",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7165#event-16946"
}
```



---

archive/issue_comments_059284.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2019-04-19T09:15:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7165",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7165#issuecomment-59284",
    "user": "https://github.com/videlec"
}
```

Changing status from new to needs_review.



---

archive/issue_events_016947.json:
```json
{
    "actor": "https://github.com/videlec",
    "created_at": "2019-04-19T09:15:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7165",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7165#event-16947"
}
```



---

archive/issue_events_016948.json:
```json
{
    "actor": "https://github.com/videlec",
    "created_at": "2019-04-19T09:15:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7165",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7165#event-16948"
}
```



---

archive/issue_comments_059285.json:
```json
{
    "body": "Now this does work\n\n```\nm = SR.var('m')\nparametric_plot([real(exp(i*m)),imaginary(exp(i*m))], (m,0,7))\n```",
    "created_at": "2019-04-19T09:15:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7165",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7165#issuecomment-59285",
    "user": "https://github.com/videlec"
}
```

Now this does work

```
m = SR.var('m')
parametric_plot([real(exp(i*m)),imaginary(exp(i*m))], (m,0,7))
```



---

archive/issue_comments_059286.json:
```json
{
    "body": "This needs a doctest.",
    "created_at": "2019-04-24T11:50:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7165",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7165#issuecomment-59286",
    "user": "https://github.com/fchapoton"
}
```

This needs a doctest.



---

archive/issue_comments_059287.json:
```json
{
    "body": "Here is a tiny doctest. After that, I think one can close this old ticket.\n\n---\nNew commits:",
    "created_at": "2020-01-04T20:13:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7165",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7165#issuecomment-59287",
    "user": "https://github.com/fchapoton"
}
```

Here is a tiny doctest. After that, I think one can close this old ticket.

---
New commits:



---

archive/issue_events_016949.json:
```json
{
    "actor": "https://github.com/fchapoton",
    "created_at": "2020-01-04T20:13:18Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7165",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7165#event-16949"
}
```



---

archive/issue_events_016950.json:
```json
{
    "actor": "https://github.com/fchapoton",
    "created_at": "2020-01-04T20:13:18Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7165",
    "milestone": "sage-9.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7165#event-16950"
}
```



---

archive/issue_comments_059288.json:
```json
{
    "body": "LGTM.",
    "created_at": "2020-01-04T21:02:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7165",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7165#issuecomment-59288",
    "user": "https://github.com/tscrim"
}
```

LGTM.



---

archive/issue_comments_059289.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2020-01-04T21:02:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7165",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7165#issuecomment-59289",
    "user": "https://github.com/tscrim"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_016951.json:
```json
{
    "actor": "https://github.com/vbraun",
    "created_at": "2020-01-09T23:44:40Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7165",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7165#event-16951"
}
```



---

archive/issue_comments_059290.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2020-01-09T23:44:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7165",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7165#issuecomment-59290",
    "user": "https://github.com/vbraun"
}
```

Resolution: fixed
