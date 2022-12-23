# Issue 9824: desolve_system unable to interpret Maxima's temporary variables

archive/issues_009824.json:
```json
{
    "body": "Assignee: burcin\n\nCC:  robert.marik\n\nKeywords: calculus, maxima, symbolics\n\ndesolve_system sometimes generates a Maxima result that includes temporary variables that Sage does not parse correctly.\n\n\n```\nsage: t = var('t')\nsage: x1 = function('x1', t)\nsage: x2 = function('x2', t)\nsage: de1 = (diff(x1,t) == -3*(x2^2-1))\nsage: de2 = (diff(x2,t) == 1)\nsage: desolve_system([de1, de2], [x1, x2], ivar=t)\n...\nTypeError: unable to make sense of Maxima expression 'x1(t)=ilt(-((3*laplace(x2(t)^2,t,?g1543)-x1(0))*?g1543-3)/?g1543^2,?g1543,t)' in Sage \n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9825\n\n",
    "created_at": "2010-08-27T16:44:47Z",
    "labels": [
        "calculus",
        "major",
        "bug"
    ],
    "title": "desolve_system unable to interpret Maxima's temporary variables",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9824",
    "user": "rhinton"
}
```
Assignee: burcin

CC:  robert.marik

Keywords: calculus, maxima, symbolics

desolve_system sometimes generates a Maxima result that includes temporary variables that Sage does not parse correctly.


```
sage: t = var('t')
sage: x1 = function('x1', t)
sage: x2 = function('x2', t)
sage: de1 = (diff(x1,t) == -3*(x2^2-1))
sage: de2 = (diff(x2,t) == 1)
sage: desolve_system([de1, de2], [x1, x2], ivar=t)
...
TypeError: unable to make sense of Maxima expression 'x1(t)=ilt(-((3*laplace(x2(t)^2,t,?g1543)-x1(0))*?g1543-3)/?g1543^2,?g1543,t)' in Sage 
```



Issue created by migration from https://trac.sagemath.org/ticket/9825





---

archive/issue_comments_096896.json:
```json
{
    "body": "On [ this Maxima list thread] we get the original system in Maxima notation - thanks to Stavros Macrackis:\n\n```\nde1: diff(x1(t),t)=-3*(x2(t)^2-1);\nde2: diff(x2(t),t)=1;\ndesolve([de1,de2],[x1(t),x2(t)]);\n```\n\nHe also provides a simpler example which does this:\n\n```\ndesolve([diff(f(x),x)=f(x^2)],[f(x)]);\n```\n\nThe suggestion is that the ilt should be replacing the `?g1234` type variables (which are indeed dummy variables, but native Lisp ones) by Maxima-type ones, so I am putting to reported upstream, developers acknowledge bug.  However, my feeling is that we should fix this by parsing these things as well, should they come up again.",
    "created_at": "2011-03-15T02:50:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9824",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9824#issuecomment-96896",
    "user": "kcrisman"
}
```

On [ this Maxima list thread] we get the original system in Maxima notation - thanks to Stavros Macrackis:

```
de1: diff(x1(t),t)=-3*(x2(t)^2-1);
de2: diff(x2(t),t)=1;
desolve([de1,de2],[x1(t),x2(t)]);
```

He also provides a simpler example which does this:

```
desolve([diff(f(x),x)=f(x^2)],[f(x)]);
```

The suggestion is that the ilt should be replacing the `?g1234` type variables (which are indeed dummy variables, but native Lisp ones) by Maxima-type ones, so I am putting to reported upstream, developers acknowledge bug.  However, my feeling is that we should fix this by parsing these things as well, should they come up again.



---

archive/issue_comments_096897.json:
```json
{
    "body": "Replying to [comment:1 kcrisman]:\n> On [ this Maxima list thread] we get the original system in Maxima notation - thanks to Stavros Macrackis:\n\nMeaning [this thread](http://www.math.utexas.edu/pipermail/maxima/2011/024573.html).",
    "created_at": "2011-03-15T02:52:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9824",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9824#issuecomment-96897",
    "user": "kcrisman"
}
```

Replying to [comment:1 kcrisman]:
> On [ this Maxima list thread] we get the original system in Maxima notation - thanks to Stavros Macrackis:

Meaning [this thread](http://www.math.utexas.edu/pipermail/maxima/2011/024573.html).



---

archive/issue_comments_096898.json:
```json
{
    "body": "I've followed up again at [this new thread](http://www.math.utexas.edu/pipermail/maxima/2012/028833.html) - apparently it never actually made it to their bug tracker?",
    "created_at": "2012-05-17T12:56:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9824",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9824#issuecomment-96898",
    "user": "kcrisman"
}
```

I've followed up again at [this new thread](http://www.math.utexas.edu/pipermail/maxima/2012/028833.html) - apparently it never actually made it to their bug tracker?



---

archive/issue_comments_096899.json:
```json
{
    "body": "See also [this ask.sagemath question](http://ask.sagemath.org/question/2039/desolve_system-error-unable-to-make-sense-of).",
    "created_at": "2012-11-30T14:01:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9824",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9824#issuecomment-96899",
    "user": "kcrisman"
}
```

See also [this ask.sagemath question](http://ask.sagemath.org/question/2039/desolve_system-error-unable-to-make-sense-of).



---

archive/issue_comments_096900.json:
```json
{
    "body": "And [this ask.sagemath question](http://ask.sagemath.org/question/2773/desolve_system-problem-with-expe), though here Maxima is actually asking a question about these variables!",
    "created_at": "2013-07-03T15:48:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9824",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9824#issuecomment-96900",
    "user": "kcrisman"
}
```

And [this ask.sagemath question](http://ask.sagemath.org/question/2773/desolve_system-problem-with-expe), though here Maxima is actually asking a question about these variables!



---

archive/issue_comments_096901.json:
```json
{
    "body": "Did you report it upstream to their bug tracker?  I never heard on either of these emails, so I think this is how it will have to be reported.",
    "created_at": "2014-06-30T13:18:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9824",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9824#issuecomment-96901",
    "user": "kcrisman"
}
```

Did you report it upstream to their bug tracker?  I never heard on either of these emails, so I think this is how it will have to be reported.



---

archive/issue_comments_096902.json:
```json
{
    "body": "I took your repeated mail to the list as report.",
    "created_at": "2014-06-30T14:03:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9824",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9824#issuecomment-96902",
    "user": "rws"
}
```

I took your repeated mail to the list as report.



---

archive/issue_comments_096903.json:
```json
{
    "body": "Sadly, that isn't always enough :(  Reported upstream [here](https://sourceforge.net/p/maxima/bugs/2774/), however, just now.  There was internal discussion in the original Maxima thread so I took it that the experts had several possible resolutions.",
    "created_at": "2014-06-30T14:14:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9824",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9824#issuecomment-96903",
    "user": "kcrisman"
}
```

Sadly, that isn't always enough :(  Reported upstream [here](https://sourceforge.net/p/maxima/bugs/2774/), however, just now.  There was internal discussion in the original Maxima thread so I took it that the experts had several possible resolutions.



---

archive/issue_comments_096904.json:
```json
{
    "body": "[Upstream](https://sourceforge.net/p/maxima/bugs/2774/#c37e) seems to have made a change that would do something about this.  Anyone want to give it a whirl?",
    "created_at": "2014-11-03T14:04:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9824",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9824#issuecomment-96904",
    "user": "kcrisman"
}
```

[Upstream](https://sourceforge.net/p/maxima/bugs/2774/#c37e) seems to have made a change that would do something about this.  Anyone want to give it a whirl?



---

archive/issue_comments_096905.json:
```json
{
    "body": "This now returns `[x1(t) == ilt(-(3*g3390*laplace(x2(t)^2, t, g3390) - g3390*x1(0) - 3)/g3390^2, g3390, t), x2(t) == t + x2(0)]` so it becomes an issue to fix our Maxima interface.",
    "created_at": "2015-02-01T10:25:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9824",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9824#issuecomment-96905",
    "user": "rws"
}
```

This now returns `[x1(t) == ilt(-(3*g3390*laplace(x2(t)^2, t, g3390) - g3390*x1(0) - 3)/g3390^2, g3390, t), x2(t) == t + x2(0)]` so it becomes an issue to fix our Maxima interface.



---

archive/issue_comments_096906.json:
```json
{
    "body": "Replying to [comment:15 rws]:\n> This now returns `[x1(t) == ilt(-(3*g3390*laplace(x2(t)^2, t, g3390) - g3390*x1(0) - 3)/g3390^2, g3390, t), x2(t) == t + x2(0)]` so it becomes an issue to fix our Maxima interface.\n\nAccording to the documentation of `inverse_laplace` this is probably more or less correct. We might want to do something about \"ilt\" so that it is more closely tied to `inverse_laplace`, though.",
    "created_at": "2015-02-01T17:39:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9824",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9824#issuecomment-96906",
    "user": "nbruin"
}
```

Replying to [comment:15 rws]:
> This now returns `[x1(t) == ilt(-(3*g3390*laplace(x2(t)^2, t, g3390) - g3390*x1(0) - 3)/g3390^2, g3390, t), x2(t) == t + x2(0)]` so it becomes an issue to fix our Maxima interface.

According to the documentation of `inverse_laplace` this is probably more or less correct. We might want to do something about "ilt" so that it is more closely tied to `inverse_laplace`, though.



---

archive/issue_comments_096907.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2021-03-13T13:18:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9824",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9824#issuecomment-96907",
    "user": "charpent"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_096908.json:
```json
{
    "body": "This is now fixed (probably due to upstream upgrade) :\n\n\n```\nsage: x1, x2=function(\"x1, x2\")\nsage: de1=x1(t).diff(t)==-3*(x2(t)-1)\nsage: de2=x2(t).diff(t)==1\nsage: Sol=desolve_system([de1, de2],[x1(t),x2(t)],ivar=t) ; Sol\n[x1(t) == -3/2*t^2 - 3*t*x2(0) + 3*t + x1(0), x2(t) == t + x2(0)]\n```\n\n\n==> invalidation of the bug and review query in order to get this bug closed.\n\nHTH,",
    "created_at": "2021-03-13T13:18:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9824",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9824#issuecomment-96908",
    "user": "charpent"
}
```

This is now fixed (probably due to upstream upgrade) :


```
sage: x1, x2=function("x1, x2")
sage: de1=x1(t).diff(t)==-3*(x2(t)-1)
sage: de2=x2(t).diff(t)==1
sage: Sol=desolve_system([de1, de2],[x1(t),x2(t)],ivar=t) ; Sol
[x1(t) == -3/2*t^2 - 3*t*x2(0) + 3*t + x1(0), x2(t) == t + x2(0)]
```


==> invalidation of the bug and review query in order to get this bug closed.

HTH,



---

archive/issue_comments_096909.json:
```json
{
    "body": "I guess as usual doctest needed?  Looks like it was a combination of their upstream fix and something we did to parse it right.",
    "created_at": "2021-03-13T13:26:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9824",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9824#issuecomment-96909",
    "user": "kcrisman"
}
```

I guess as usual doctest needed?  Looks like it was a combination of their upstream fix and something we did to parse it right.



---

archive/issue_comments_096910.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2021-03-13T13:26:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9824",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9824#issuecomment-96910",
    "user": "kcrisman"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_096911.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2021-03-14T10:26:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9824",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9824#issuecomment-96911",
    "user": "charpent"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_096912.json:
```json
{
    "body": "Doctest added.\n\nHTH,\n----\nNew commits:",
    "created_at": "2021-03-14T10:26:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9824",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9824#issuecomment-96912",
    "user": "charpent"
}
```

Doctest added.

HTH,
----
New commits:



---

archive/issue_comments_096913.json:
```json
{
    "body": "Thanks, this is great.  Despite patchbot not yet reporting and my own Sage install being too brittle to test, [Cell server](https://sagecell.sagemath.org/?z=eJwrTkxPtVIoSyzSUC9R1-TlKgbzKwx1FCqMbNNK85JLMvPzNJQgAkpwBSmphrYVhholmnopmWlpQNrWVtdYS6PCCMjUNURSZmQLFkMoM4TJBefn2KakFufnlKXGF1cWl6TmakQDjdUBaYrViQabrgPWHKuTCXSgbYmmgjVIFwBUFzUS&lang=sage&interacts=eJyLjgUAARUAuQ==) says it's fine so let's do it.",
    "created_at": "2021-03-17T14:38:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9824",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9824#issuecomment-96913",
    "user": "kcrisman"
}
```

Thanks, this is great.  Despite patchbot not yet reporting and my own Sage install being too brittle to test, [Cell server](https://sagecell.sagemath.org/?z=eJwrTkxPtVIoSyzSUC9R1-TlKgbzKwx1FCqMbNNK85JLMvPzNJQgAkpwBSmphrYVhholmnopmWlpQNrWVtdYS6PCCMjUNURSZmQLFkMoM4TJBefn2KakFufnlKXGF1cWl6TmakQDjdUBaYrViQabrgPWHKuTCXSgbYmmgjVIFwBUFzUS&lang=sage&interacts=eJyLjgUAARUAuQ==) says it's fine so let's do it.



---

archive/issue_comments_096914.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2021-03-17T14:38:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9824",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9824#issuecomment-96914",
    "user": "kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_096915.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2021-03-20T15:27:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9824",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9824#issuecomment-96915",
    "user": "vbraun"
}
```

Resolution: fixed
