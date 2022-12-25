# Issue 8603: Partial sums are off for Fourier series of piecewise functions

archive/issues_008603.json:
```json
{
    "body": "Assignee: @burcin\n\nCC:  @wdjoyner @jasongrout @jondo @kcrisman @vbraun @slel @mkoeppe @eviatarbach @rwst @novoselt\n\nKeywords: sd31\n\nDoing\n\n```\nf = Piecewise([[(-pi, pi), x]])\nprint f.fourier_series_partial_sum(2, pi)\nprint f.fourier_series_partial_sum(3, pi)\n```\nwe get\n\n```\n2*sin(x)\n-sin(2*x) + 2*sin(x)\n```\nwhile according to the documentation we should get the second output with the first command.\n\nUpdate: Same output with the new `piecewise` from #14801. Does it agree with the documentation there?\n\nUPDATE: this is fixed in Sage 8.1 (see #23672):\n\n```\nsage: f = piecewise([[(-pi, pi), x]])\nsage: f.fourier_series_partial_sum(2, pi)\n-sin(2*x) + 2*sin(x)\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8603\n\n",
    "closed_at": "2017-12-12T08:23:33Z",
    "created_at": "2010-03-25T04:06:02Z",
    "labels": [
        "component: calculus",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Partial sums are off for Fourier series of piecewise functions",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8603",
    "user": "https://github.com/novoselt"
}
```
Assignee: @burcin

CC:  @wdjoyner @jasongrout @jondo @kcrisman @vbraun @slel @mkoeppe @eviatarbach @rwst @novoselt

Keywords: sd31

Doing

```
f = Piecewise([[(-pi, pi), x]])
print f.fourier_series_partial_sum(2, pi)
print f.fourier_series_partial_sum(3, pi)
```
we get

```
2*sin(x)
-sin(2*x) + 2*sin(x)
```
while according to the documentation we should get the second output with the first command.

Update: Same output with the new `piecewise` from #14801. Does it agree with the documentation there?

UPDATE: this is fixed in Sage 8.1 (see #23672):

```
sage: f = piecewise([[(-pi, pi), x]])
sage: f.fourier_series_partial_sum(2, pi)
-sin(2*x) + 2*sin(x)
```


Issue created by migration from https://trac.sagemath.org/ticket/8603





---

archive/issue_comments_077781.json:
```json
{
    "body": "Changing priority from major to minor.",
    "created_at": "2011-03-14T20:25:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8603",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8603#issuecomment-77781",
    "user": "https://github.com/kcrisman"
}
```

Changing priority from major to minor.



---

archive/issue_comments_077782.json:
```json
{
    "body": "This is still true, and syntax is also deprecated.\n\n```\n\nsage: f = Piecewise([[(-pi, pi), x]])\nsage: print f.fourier_series_partial_sum(2, pi)\n/Applications/MathApps/sage/local/lib/python2.6/site-packages/sage/functions/piecewise.py:1095: DeprecationWarning: Substitution using function-call syntax and unnamed arguments is deprecated and will be removed from a future release of Sage; you can use named arguments instead, like EXPR(x=..., y=...)\n  a0 = self.fourier_series_cosine_coefficient(0,L)\n/Applications/MathApps/sage/local/lib/python2.6/site-packages/sage/functions/piecewise.py:1099: DeprecationWarning: Substitution using function-call syntax and unnamed arguments is deprecated and will be removed from a future release of Sage; you can use named arguments instead, like EXPR(x=..., y=...)\n  for n in srange(1,N)])\n2*sin(x)\nsage: print f.fourier_series_partial_sum(3, pi)\n-sin(2*x) + 2*sin(x)\n```",
    "created_at": "2011-03-14T20:25:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8603",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8603#issuecomment-77782",
    "user": "https://github.com/kcrisman"
}
```

This is still true, and syntax is also deprecated.

```

sage: f = Piecewise([[(-pi, pi), x]])
sage: print f.fourier_series_partial_sum(2, pi)
/Applications/MathApps/sage/local/lib/python2.6/site-packages/sage/functions/piecewise.py:1095: DeprecationWarning: Substitution using function-call syntax and unnamed arguments is deprecated and will be removed from a future release of Sage; you can use named arguments instead, like EXPR(x=..., y=...)
  a0 = self.fourier_series_cosine_coefficient(0,L)
/Applications/MathApps/sage/local/lib/python2.6/site-packages/sage/functions/piecewise.py:1099: DeprecationWarning: Substitution using function-call syntax and unnamed arguments is deprecated and will be removed from a future release of Sage; you can use named arguments instead, like EXPR(x=..., y=...)
  for n in srange(1,N)])
2*sin(x)
sage: print f.fourier_series_partial_sum(3, pi)
-sin(2*x) + 2*sin(x)
```



---

archive/issue_comments_077783.json:
```json
{
    "body": "Changing keywords from \"\" to \"sd31\".",
    "created_at": "2011-06-18T00:31:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8603",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8603#issuecomment-77783",
    "user": "https://github.com/novoselt"
}
```

Changing keywords from "" to "sd31".



---

archive/issue_comments_077784.json:
```json
{
    "body": "On a related note: what is the purpose of `plot` methods for Fourier partial sums? They don't do anything except for passing arguments to the usual global `plot` function, so they seem redundant to me and perhaps can be removed (after deprecation period).",
    "created_at": "2011-06-18T00:31:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8603",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8603#issuecomment-77784",
    "user": "https://github.com/novoselt"
}
```

On a related note: what is the purpose of `plot` methods for Fourier partial sums? They don't do anything except for passing arguments to the usual global `plot` function, so they seem redundant to me and perhaps can be removed (after deprecation period).



---

archive/issue_comments_077785.json:
```json
{
    "body": "You may be right.  I'd have to look at it.  Remember, these are all *really* old, so they probably at the time bypassed the non-existent 'plot' function, and then were subsequently changed, perhaps.",
    "created_at": "2011-06-18T00:41:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8603",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8603#issuecomment-77785",
    "user": "https://github.com/kcrisman"
}
```

You may be right.  I'd have to look at it.  Remember, these are all *really* old, so they probably at the time bypassed the non-existent 'plot' function, and then were subsequently changed, perhaps.



---

archive/issue_comments_077786.json:
```json
{
    "body": "one line change in docstring",
    "created_at": "2011-06-18T10:44:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8603",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8603#issuecomment-77786",
    "user": "https://github.com/wdjoyner"
}
```

one line change in docstring



---

archive/issue_comments_077787.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2011-06-18T10:46:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8603",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8603#issuecomment-77787",
    "user": "https://github.com/wdjoyner"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_077788.json:
```json
{
    "body": "Attachment [trac_8603-fourier-sum-docstring.patch](tarball://root/attachments/some-uuid/ticket8603/trac_8603-fourier-sum-docstring.patch) by @wdjoyner created at 2011-06-18 10:46:16\n\nThis fixes the documentation of fourier_series_partial_sum, replacing\n\n```\n f(x) \\sim \\frac{a_0}{2} + \\sum_{n=1}^N [a_n\\cos(\\frac{n\\pi x}{L}) +\nb_n\\sin(\\frac{n\\pi x}{L})],\n```\nby\n\n```\n f(x) \\sim \\frac{a_0}{2} + \\sum_{n=1}^{N-1} [a_n\\cos(\\frac{n\\pi x}{L})\n+ b_n\\sin(\\frac{n\\pi x}{L})],\n```",
    "created_at": "2011-06-18T10:46:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8603",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8603#issuecomment-77788",
    "user": "https://github.com/wdjoyner"
}
```

Attachment [trac_8603-fourier-sum-docstring.patch](tarball://root/attachments/some-uuid/ticket8603/trac_8603-fourier-sum-docstring.patch) by @wdjoyner created at 2011-06-18 10:46:16

This fixes the documentation of fourier_series_partial_sum, replacing

```
 f(x) \sim \frac{a_0}{2} + \sum_{n=1}^N [a_n\cos(\frac{n\pi x}{L}) +
b_n\sin(\frac{n\pi x}{L})],
```
by

```
 f(x) \sim \frac{a_0}{2} + \sum_{n=1}^{N-1} [a_n\cos(\frac{n\pi x}{L})
+ b_n\sin(\frac{n\pi x}{L})],
```



---

archive/issue_comments_077789.json:
```json
{
    "body": "Thanks, David; I don't have time to review this now, but appreciate it.  \n\nAndrey and I were discussing this at Sage Days 31, and thought that maybe changing the behavior instead to match Taylor series would be good, but if this was in fact what you had intended all along, then this solution is better.",
    "created_at": "2011-06-19T01:23:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8603",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8603#issuecomment-77789",
    "user": "https://github.com/kcrisman"
}
```

Thanks, David; I don't have time to review this now, but appreciate it.  

Andrey and I were discussing this at Sage Days 31, and thought that maybe changing the behavior instead to match Taylor series would be good, but if this was in fact what you had intended all along, then this solution is better.



---

archive/issue_comments_077790.json:
```json
{
    "body": "Replying to [comment:5 kcrisman]:\n> Thanks, David; I don't have time to review this now, but appreciate it.  \n> \n> Andrey and I were discussing this at Sage Days 31, and thought that maybe changing the behavior instead to match Taylor series would be good, but if this was in fact what you had intended all along, then this solution is better. \n\n\nThe `.series()` method of symbolic expressions cut off in a pythonic way, like David's change here. If `.taylor()` does something different we should change it.\n\nThis is a trivial change. I'd be happy to give a positive review if it passes all tests but the patch bot doesn't seem to be working for some reason.",
    "created_at": "2011-06-19T02:42:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8603",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8603#issuecomment-77790",
    "user": "https://github.com/burcin"
}
```

Replying to [comment:5 kcrisman]:
> Thanks, David; I don't have time to review this now, but appreciate it.  
> 
> Andrey and I were discussing this at Sage Days 31, and thought that maybe changing the behavior instead to match Taylor series would be good, but if this was in fact what you had intended all along, then this solution is better. 


The `.series()` method of symbolic expressions cut off in a pythonic way, like David's change here. If `.taylor()` does something different we should change it.

This is a trivial change. I'd be happy to give a positive review if it passes all tests but the patch bot doesn't seem to be working for some reason.



---

archive/issue_comments_077791.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2011-06-21T17:48:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8603",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8603#issuecomment-77791",
    "user": "https://github.com/novoselt"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_077792.json:
```json
{
    "body": "There are more instances of the same typo in other functions of this module, let's fix them all at once!-)\n\nDavid, do you agree that plot methods can be eliminated as they are not really doing anything?",
    "created_at": "2011-06-21T17:48:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8603",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8603#issuecomment-77792",
    "user": "https://github.com/novoselt"
}
```

There are more instances of the same typo in other functions of this module, let's fix them all at once!-)

David, do you agree that plot methods can be eliminated as they are not really doing anything?



---

archive/issue_comments_077793.json:
```json
{
    "body": "Replying to [comment:7 novoselt]:\n> There are more instances of the same typo in other functions of this module, let's fix them all at once!-)\n\nCan you be more specific?\n> David, do you agree that plot methods can be eliminated as they are not really doing anything?\n\nI think I looked at this at Sage Days 31, but now I forgot whether that statement is true.",
    "created_at": "2011-08-15T14:30:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8603",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8603#issuecomment-77793",
    "user": "https://github.com/kcrisman"
}
```

Replying to [comment:7 novoselt]:
> There are more instances of the same typo in other functions of this module, let's fix them all at once!-)

Can you be more specific?
> David, do you agree that plot methods can be eliminated as they are not really doing anything?

I think I looked at this at Sage Days 31, but now I forgot whether that statement is true.



---

archive/issue_events_020790.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8603",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8603#event-20790"
}
```



---

archive/issue_events_020791.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8603",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8603#event-20791"
}
```



---

archive/issue_events_020792.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8603",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8603#event-20792"
}
```



---

archive/issue_events_020793.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8603",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8603#event-20793"
}
```



---

archive/issue_events_020794.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8603",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8603#event-20794"
}
```



---

archive/issue_events_020795.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8603",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8603#event-20795"
}
```



---

archive/issue_events_020796.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8603",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8603#event-20796"
}
```



---

archive/issue_events_020797.json:
```json
{
    "actor": "https://github.com/mkoeppe",
    "created_at": "2016-06-27T03:31:36Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8603",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8603#event-20797"
}
```



---

archive/issue_events_020798.json:
```json
{
    "actor": "https://github.com/mkoeppe",
    "created_at": "2016-06-27T03:31:36Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8603",
    "milestone": "sage-7.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8603#event-20798"
}
```



---

archive/issue_comments_077794.json:
```json
{
    "body": "Updated with information regarding the new `piecewise` implementation from #14801.",
    "created_at": "2016-06-27T03:31:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8603",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8603#issuecomment-77794",
    "user": "https://github.com/mkoeppe"
}
```

Updated with information regarding the new `piecewise` implementation from #14801.



---

archive/issue_comments_077795.json:
```json
{
    "body": "Changing status from needs_work to needs_info.",
    "created_at": "2016-06-27T03:31:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8603",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8603#issuecomment-77795",
    "user": "https://github.com/mkoeppe"
}
```

Changing status from needs_work to needs_info.



---

archive/issue_comments_077796.json:
```json
{
    "body": "This is fixed by #23672.\n\nRegarding the example in the ticket description, in Sage 8.1.beta4, we have now\n\n```\nsage: f = piecewise([[(-pi, pi), x]])\nsage: f.fourier_series_partial_sum(2, pi)\n-sin(2*x) + 2*sin(x)\n```\nWe even have, since the half-period is now a default argument,\n\n```\nsage: f.fourier_series_partial_sum(2)\n-sin(2*x) + 2*sin(x)\n```",
    "created_at": "2017-09-07T12:01:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8603",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8603#issuecomment-77796",
    "user": "https://github.com/egourgoulhon"
}
```

This is fixed by #23672.

Regarding the example in the ticket description, in Sage 8.1.beta4, we have now

```
sage: f = piecewise([[(-pi, pi), x]])
sage: f.fourier_series_partial_sum(2, pi)
-sin(2*x) + 2*sin(x)
```
We even have, since the half-period is now a default argument,

```
sage: f.fourier_series_partial_sum(2)
-sin(2*x) + 2*sin(x)
```



---

archive/issue_comments_077797.json:
```json
{
    "body": "Changing status from needs_info to positive_review.",
    "created_at": "2017-09-07T12:01:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8603",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8603#issuecomment-77797",
    "user": "https://github.com/egourgoulhon"
}
```

Changing status from needs_info to positive_review.



---

archive/issue_events_020799.json:
```json
{
    "actor": "https://github.com/egourgoulhon",
    "created_at": "2017-09-07T12:01:47Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8603",
    "milestone": "sage-7.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8603#event-20799"
}
```



---

archive/issue_events_020800.json:
```json
{
    "actor": "https://github.com/egourgoulhon",
    "created_at": "2017-09-07T12:01:47Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8603",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8603#event-20800"
}
```



---

archive/issue_comments_077798.json:
```json
{
    "body": "Excellent.  Is this documented via a test?",
    "created_at": "2017-09-07T14:33:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8603",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8603#issuecomment-77798",
    "user": "https://github.com/kcrisman"
}
```

Excellent.  Is this documented via a test?



---

archive/issue_comments_077799.json:
```json
{
    "body": "Changing status from positive_review to needs_info.",
    "created_at": "2017-09-07T14:33:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8603",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8603#issuecomment-77799",
    "user": "https://github.com/kcrisman"
}
```

Changing status from positive_review to needs_info.



---

archive/issue_comments_077800.json:
```json
{
    "body": "Replying to [comment:16 kcrisman]:\n> Excellent.  Is this documented via a test?\n\n\nYes this is documented, both in [Sage Reference Manual](http://doc.sagemath.org/html/en/reference/) and in [Sage Constructions](http://doc.sagemath.org/html/en/constructions/), see [here](https://git.sagemath.org/sage.git/commit?id=ddeef52c783ef2f87c21b4b26e4410ace5007f02).",
    "created_at": "2017-09-07T14:41:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8603",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8603#issuecomment-77800",
    "user": "https://github.com/egourgoulhon"
}
```

Replying to [comment:16 kcrisman]:
> Excellent.  Is this documented via a test?


Yes this is documented, both in [Sage Reference Manual](http://doc.sagemath.org/html/en/reference/) and in [Sage Constructions](http://doc.sagemath.org/html/en/constructions/), see [here](https://git.sagemath.org/sage.git/commit?id=ddeef52c783ef2f87c21b4b26e4410ace5007f02).



---

archive/issue_comments_077801.json:
```json
{
    "body": "Sweet.  Strange that it didn't cause any doctest errors then?  If it didn't, we should make sure to include at least two of the examples on the ticket in the doc *somewhere*.",
    "created_at": "2017-09-07T17:30:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8603",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8603#issuecomment-77801",
    "user": "https://github.com/kcrisman"
}
```

Sweet.  Strange that it didn't cause any doctest errors then?  If it didn't, we should make sure to include at least two of the examples on the ticket in the doc *somewhere*.



---

archive/issue_comments_077802.json:
```json
{
    "body": "Changing status from needs_info to positive_review.",
    "created_at": "2017-09-07T17:30:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8603",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8603#issuecomment-77802",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_info to positive_review.



---

archive/issue_comments_077803.json:
```json
{
    "body": "Replying to [comment:19 kcrisman]:\n> Sweet.  Strange that it didn't cause any doctest errors then?  If it didn't, we should make sure to include at least two of the examples on the ticket in the doc *somewhere*.\n\n\nI am not sure to understand what you mean. In the current version, as integrated in Sage 8.1.beta4, there are doctests like\n\n```\nsage: f = piecewise([((-1,0), -1), ((0,1), 1)])\nsage: f.fourier_series_partial_sum(5)\n4/5*sin(5*pi*x)/pi + 4/3*sin(3*pi*x)/pi + 4*sin(pi*x)/pi\n```\nIn Sage <= 8.0, this would have returned (*)\n\n```\n4/3*sin(3*pi*x)/pi + 4*sin(pi*x)/pi\n```\n\n(*) with the half-period added as the second argument, i.e. `f.fourier_series_partial_sum(5, 1)`)",
    "created_at": "2017-09-07T19:30:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8603",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8603#issuecomment-77803",
    "user": "https://github.com/egourgoulhon"
}
```

Replying to [comment:19 kcrisman]:
> Sweet.  Strange that it didn't cause any doctest errors then?  If it didn't, we should make sure to include at least two of the examples on the ticket in the doc *somewhere*.


I am not sure to understand what you mean. In the current version, as integrated in Sage 8.1.beta4, there are doctests like

```
sage: f = piecewise([((-1,0), -1), ((0,1), 1)])
sage: f.fourier_series_partial_sum(5)
4/5*sin(5*pi*x)/pi + 4/3*sin(3*pi*x)/pi + 4*sin(pi*x)/pi
```
In Sage <= 8.0, this would have returned (*)

```
4/3*sin(3*pi*x)/pi + 4*sin(pi*x)/pi
```

(*) with the half-period added as the second argument, i.e. `f.fourier_series_partial_sum(5, 1)`)



---

archive/issue_comments_077804.json:
```json
{
    "body": "My concern was just that the *correct* nature was doctested, not the wrong one, and that we really did have that to test against regression at some point.  Good!",
    "created_at": "2017-09-07T21:34:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8603",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8603#issuecomment-77804",
    "user": "https://github.com/kcrisman"
}
```

My concern was just that the *correct* nature was doctested, not the wrong one, and that we really did have that to test against regression at some point.  Good!



---

archive/issue_events_020801.json:
```json
{
    "actor": "https://github.com/embray",
    "created_at": "2017-12-12T08:23:33Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8603",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8603#event-20801"
}
```



---

archive/issue_comments_077805.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2017-12-12T08:23:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8603",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8603#issuecomment-77805",
    "user": "https://github.com/embray"
}
```

Resolution: wontfix



---

archive/issue_comments_077806.json:
```json
{
    "body": "I wonder why \"wontfix\" since the issue is fixed in 8.1.beta4.\nPaul",
    "created_at": "2017-12-12T13:27:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8603",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8603#issuecomment-77806",
    "user": "https://github.com/zimmermann6"
}
```

I wonder why "wontfix" since the issue is fixed in 8.1.beta4.
Paul



---

archive/issue_comments_077807.json:
```json
{
    "body": "Replying to [comment:23 zimmerma]:\n> I wonder why \"wontfix\" since the issue is fixed in 8.1.beta4.\n> Paul\n\nActually, as said in comment:15, the issue is fixed in another ticket: #23672, hence the \"sage-duplicate/invalid/wontfix\" milestone for the current one and the \"wonfix\" resolution.",
    "created_at": "2017-12-12T13:41:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8603",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8603#issuecomment-77807",
    "user": "https://github.com/egourgoulhon"
}
```

Replying to [comment:23 zimmerma]:
> I wonder why "wontfix" since the issue is fixed in 8.1.beta4.
> Paul

Actually, as said in comment:15, the issue is fixed in another ticket: #23672, hence the "sage-duplicate/invalid/wontfix" milestone for the current one and the "wonfix" resolution.



---

archive/issue_comments_077808.json:
```json
{
    "body": "Hey, do non-release managers get to mark \"closed\"?  That would be a change in protocol.\n\nAlso, maybe the resolution should be \"fixed\" or \"duplicate\" if it is indeed fixed in another ticket?",
    "created_at": "2017-12-12T15:18:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8603",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8603#issuecomment-77808",
    "user": "https://github.com/kcrisman"
}
```

Hey, do non-release managers get to mark "closed"?  That would be a change in protocol.

Also, maybe the resolution should be "fixed" or "duplicate" if it is indeed fixed in another ticket?



---

archive/issue_comments_077809.json:
```json
{
    "body": "Resolution changed from wontfix to duplicate",
    "created_at": "2017-12-12T15:18:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8603",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8603#issuecomment-77809",
    "user": "https://github.com/kcrisman"
}
```

Resolution changed from wontfix to duplicate



---

archive/issue_comments_077810.json:
```json
{
    "body": "Replying to [comment:26 kcrisman]:\n> Hey, do non-release managers get to mark \"closed\"?  That would be a change in protocol.\n> \n\n\nThis was announced in https://groups.google.com/d/msg/sage-release/4bIUu1NECwY/we3BMdkeAAAJ with apparently the approval of the release manager.\n\n> Also, maybe the resolution should be \"fixed\" or \"duplicate\" if it is indeed fixed in another ticket?\n\n\nAh yes, you are right (I thought this was automatically set to \"wontfix\"  while closing \"sage-duplicate/invalid/wontfix\" tickets).",
    "created_at": "2017-12-12T15:27:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8603",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8603#issuecomment-77810",
    "user": "https://github.com/egourgoulhon"
}
```

Replying to [comment:26 kcrisman]:
> Hey, do non-release managers get to mark "closed"?  That would be a change in protocol.
> 


This was announced in https://groups.google.com/d/msg/sage-release/4bIUu1NECwY/we3BMdkeAAAJ with apparently the approval of the release manager.

> Also, maybe the resolution should be "fixed" or "duplicate" if it is indeed fixed in another ticket?


Ah yes, you are right (I thought this was automatically set to "wontfix"  while closing "sage-duplicate/invalid/wontfix" tickets).



---

archive/issue_comments_077811.json:
```json
{
    "body": "Replying to [comment:27 egourgoulhon]:\n> Replying to [comment:26 kcrisman]:\n> > Hey, do non-release managers get to mark \"closed\"?  That would be a change in protocol.\n> > \n\n> \n> This was announced in https://groups.google.com/d/msg/sage-release/4bIUu1NECwY/we3BMdkeAAAJ with apparently the approval of the release manager.\n> \n\n\n10 hours ago :-) but this will be welcome for obvious dupes etc.\n\n> > Also, maybe the resolution should be \"fixed\" or \"duplicate\" if it is indeed fixed in another ticket?\n\n> \n> Ah yes, you are right (I thought this was automatically set to \"wontfix\"  while closing \"sage-duplicate/invalid/wontfix\" tickets).\n\n\nYeah, that might be the default, but typically we try to be precise on this. Nice.",
    "created_at": "2017-12-12T19:15:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8603",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8603#issuecomment-77811",
    "user": "https://github.com/kcrisman"
}
```

Replying to [comment:27 egourgoulhon]:
> Replying to [comment:26 kcrisman]:
> > Hey, do non-release managers get to mark "closed"?  That would be a change in protocol.
> > 

> 
> This was announced in https://groups.google.com/d/msg/sage-release/4bIUu1NECwY/we3BMdkeAAAJ with apparently the approval of the release manager.
> 


10 hours ago :-) but this will be welcome for obvious dupes etc.

> > Also, maybe the resolution should be "fixed" or "duplicate" if it is indeed fixed in another ticket?

> 
> Ah yes, you are right (I thought this was automatically set to "wontfix"  while closing "sage-duplicate/invalid/wontfix" tickets).


Yeah, that might be the default, but typically we try to be precise on this. Nice.
