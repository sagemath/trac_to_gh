# Issue 8603: Partial sums are off for Fourier series of piecewise functions

archive/issues_008603.json:
```json
{
    "body": "Assignee: @burcin\n\nCC:  @wdjoyner @jasongrout @jondo @kcrisman @vbraun @slel @mkoeppe @eviatarbach @rwst @novoselt\n\nDoing\n\n```\nf = Piecewise([[(-pi, pi), x]])\nprint f.fourier_series_partial_sum(2, pi)\nprint f.fourier_series_partial_sum(3, pi)\n```\n\nwe get\n\n```\n2*sin(x)\n-sin(2*x) + 2*sin(x)\n```\n\nwhile according to the documentation we should get the second output with the first command.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8603\n\n",
    "created_at": "2010-03-25T04:06:02Z",
    "labels": [
        "calculus",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Partial sums are off for Fourier series of piecewise functions",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8603",
    "user": "@novoselt"
}
```
Assignee: @burcin

CC:  @wdjoyner @jasongrout @jondo @kcrisman @vbraun @slel @mkoeppe @eviatarbach @rwst @novoselt

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

Issue created by migration from https://trac.sagemath.org/ticket/8603





---

archive/issue_comments_077909.json:
```json
{
    "body": "Changing priority from major to minor.",
    "created_at": "2011-03-14T20:25:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8603",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8603#issuecomment-77909",
    "user": "@kcrisman"
}
```

Changing priority from major to minor.



---

archive/issue_comments_077910.json:
```json
{
    "body": "This is still true, and syntax is also deprecated.\n\n```\n\nsage: f = Piecewise([[(-pi, pi), x]])\nsage: print f.fourier_series_partial_sum(2, pi)\n/Applications/MathApps/sage/local/lib/python2.6/site-packages/sage/functions/piecewise.py:1095: DeprecationWarning: Substitution using function-call syntax and unnamed arguments is deprecated and will be removed from a future release of Sage; you can use named arguments instead, like EXPR(x=..., y=...)\n  a0 = self.fourier_series_cosine_coefficient(0,L)\n/Applications/MathApps/sage/local/lib/python2.6/site-packages/sage/functions/piecewise.py:1099: DeprecationWarning: Substitution using function-call syntax and unnamed arguments is deprecated and will be removed from a future release of Sage; you can use named arguments instead, like EXPR(x=..., y=...)\n  for n in srange(1,N)])\n2*sin(x)\nsage: print f.fourier_series_partial_sum(3, pi)\n-sin(2*x) + 2*sin(x)\n```\n",
    "created_at": "2011-03-14T20:25:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8603",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8603#issuecomment-77910",
    "user": "@kcrisman"
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

archive/issue_comments_077911.json:
```json
{
    "body": "Changing keywords from \"\" to \"sd31\".",
    "created_at": "2011-06-18T00:31:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8603",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8603#issuecomment-77911",
    "user": "@novoselt"
}
```

Changing keywords from "" to "sd31".



---

archive/issue_comments_077912.json:
```json
{
    "body": "On a related note: what is the purpose of `plot` methods for Fourier partial sums? They don't do anything except for passing arguments to the usual global `plot` function, so they seem redundant to me and perhaps can be removed (after deprecation period).",
    "created_at": "2011-06-18T00:31:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8603",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8603#issuecomment-77912",
    "user": "@novoselt"
}
```

On a related note: what is the purpose of `plot` methods for Fourier partial sums? They don't do anything except for passing arguments to the usual global `plot` function, so they seem redundant to me and perhaps can be removed (after deprecation period).



---

archive/issue_comments_077913.json:
```json
{
    "body": "You may be right.  I'd have to look at it.  Remember, these are all *really* old, so they probably at the time bypassed the non-existent 'plot' function, and then were subsequently changed, perhaps.",
    "created_at": "2011-06-18T00:41:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8603",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8603#issuecomment-77913",
    "user": "@kcrisman"
}
```

You may be right.  I'd have to look at it.  Remember, these are all *really* old, so they probably at the time bypassed the non-existent 'plot' function, and then were subsequently changed, perhaps.



---

archive/issue_comments_077914.json:
```json
{
    "body": "one line change in docstring",
    "created_at": "2011-06-18T10:44:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8603",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8603#issuecomment-77914",
    "user": "@wdjoyner"
}
```

one line change in docstring



---

archive/issue_comments_077915.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2011-06-18T10:46:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8603",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8603#issuecomment-77915",
    "user": "@wdjoyner"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_077916.json:
```json
{
    "body": "Attachment [trac_8603-fourier-sum-docstring.patch](tarball://root/attachments/some-uuid/ticket8603/trac_8603-fourier-sum-docstring.patch) by @wdjoyner created at 2011-06-18 10:46:16\n\nThis fixes the documentation of fourier_series_partial_sum, replacing\n\n```\n f(x) \\sim \\frac{a_0}{2} + \\sum_{n=1}^N [a_n\\cos(\\frac{n\\pi x}{L}) +\nb_n\\sin(\\frac{n\\pi x}{L})],\n```\n\nby\n\n```\n f(x) \\sim \\frac{a_0}{2} + \\sum_{n=1}^{N-1} [a_n\\cos(\\frac{n\\pi x}{L})\n+ b_n\\sin(\\frac{n\\pi x}{L})],\n```\n",
    "created_at": "2011-06-18T10:46:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8603",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8603#issuecomment-77916",
    "user": "@wdjoyner"
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

archive/issue_comments_077917.json:
```json
{
    "body": "Thanks, David; I don't have time to review this now, but appreciate it.  \n\nAndrey and I were discussing this at Sage Days 31, and thought that maybe changing the behavior instead to match Taylor series would be good, but if this was in fact what you had intended all along, then this solution is better.",
    "created_at": "2011-06-19T01:23:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8603",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8603#issuecomment-77917",
    "user": "@kcrisman"
}
```

Thanks, David; I don't have time to review this now, but appreciate it.  

Andrey and I were discussing this at Sage Days 31, and thought that maybe changing the behavior instead to match Taylor series would be good, but if this was in fact what you had intended all along, then this solution is better.



---

archive/issue_comments_077918.json:
```json
{
    "body": "Replying to [comment:5 kcrisman]:\n> Thanks, David; I don't have time to review this now, but appreciate it.  \n> \n> Andrey and I were discussing this at Sage Days 31, and thought that maybe changing the behavior instead to match Taylor series would be good, but if this was in fact what you had intended all along, then this solution is better. \n\nThe `.series()` method of symbolic expressions cut off in a pythonic way, like David's change here. If `.taylor()` does something different we should change it.\n\nThis is a trivial change. I'd be happy to give a positive review if it passes all tests but the patch bot doesn't seem to be working for some reason.",
    "created_at": "2011-06-19T02:42:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8603",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8603#issuecomment-77918",
    "user": "@burcin"
}
```

Replying to [comment:5 kcrisman]:
> Thanks, David; I don't have time to review this now, but appreciate it.  
> 
> Andrey and I were discussing this at Sage Days 31, and thought that maybe changing the behavior instead to match Taylor series would be good, but if this was in fact what you had intended all along, then this solution is better. 

The `.series()` method of symbolic expressions cut off in a pythonic way, like David's change here. If `.taylor()` does something different we should change it.

This is a trivial change. I'd be happy to give a positive review if it passes all tests but the patch bot doesn't seem to be working for some reason.



---

archive/issue_comments_077919.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2011-06-21T17:48:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8603",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8603#issuecomment-77919",
    "user": "@novoselt"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_077920.json:
```json
{
    "body": "There are more instances of the same typo in other functions of this module, let's fix them all at once!-)\n\nDavid, do you agree that plot methods can be eliminated as they are not really doing anything?",
    "created_at": "2011-06-21T17:48:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8603",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8603#issuecomment-77920",
    "user": "@novoselt"
}
```

There are more instances of the same typo in other functions of this module, let's fix them all at once!-)

David, do you agree that plot methods can be eliminated as they are not really doing anything?



---

archive/issue_comments_077921.json:
```json
{
    "body": "Replying to [comment:7 novoselt]:\n> There are more instances of the same typo in other functions of this module, let's fix them all at once!-)\nCan you be more specific?\n> David, do you agree that plot methods can be eliminated as they are not really doing anything?\nI think I looked at this at Sage Days 31, but now I forgot whether that statement is true.",
    "created_at": "2011-08-15T14:30:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8603",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8603#issuecomment-77921",
    "user": "@kcrisman"
}
```

Replying to [comment:7 novoselt]:
> There are more instances of the same typo in other functions of this module, let's fix them all at once!-)
Can you be more specific?
> David, do you agree that plot methods can be eliminated as they are not really doing anything?
I think I looked at this at Sage Days 31, but now I forgot whether that statement is true.



---

archive/issue_comments_077922.json:
```json
{
    "body": "Updated with information regarding the new `piecewise` implementation from #14801.",
    "created_at": "2016-06-27T03:31:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8603",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8603#issuecomment-77922",
    "user": "@mkoeppe"
}
```

Updated with information regarding the new `piecewise` implementation from #14801.



---

archive/issue_comments_077923.json:
```json
{
    "body": "Changing status from needs_work to needs_info.",
    "created_at": "2016-06-27T03:31:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8603",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8603#issuecomment-77923",
    "user": "@mkoeppe"
}
```

Changing status from needs_work to needs_info.



---

archive/issue_comments_077924.json:
```json
{
    "body": "This is fixed by #23672.\n\nRegarding the example in the ticket description, in Sage 8.1.beta4, we have now\n\n```\nsage: f = piecewise([[(-pi, pi), x]])\nsage: f.fourier_series_partial_sum(2, pi)\n-sin(2*x) + 2*sin(x)\n```\n\nWe even have, since the half-period is now a default argument,\n\n```\nsage: f.fourier_series_partial_sum(2)\n-sin(2*x) + 2*sin(x)\n```\n",
    "created_at": "2017-09-07T12:01:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8603",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8603#issuecomment-77924",
    "user": "@egourgoulhon"
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

archive/issue_comments_077925.json:
```json
{
    "body": "Changing status from needs_info to positive_review.",
    "created_at": "2017-09-07T12:01:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8603",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8603#issuecomment-77925",
    "user": "@egourgoulhon"
}
```

Changing status from needs_info to positive_review.



---

archive/issue_comments_077926.json:
```json
{
    "body": "Excellent.  Is this documented via a test?",
    "created_at": "2017-09-07T14:33:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8603",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8603#issuecomment-77926",
    "user": "@kcrisman"
}
```

Excellent.  Is this documented via a test?



---

archive/issue_comments_077927.json:
```json
{
    "body": "Changing status from positive_review to needs_info.",
    "created_at": "2017-09-07T14:33:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8603",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8603#issuecomment-77927",
    "user": "@kcrisman"
}
```

Changing status from positive_review to needs_info.



---

archive/issue_comments_077928.json:
```json
{
    "body": "Replying to [comment:16 kcrisman]:\n> Excellent.  Is this documented via a test?\n\nYes this is documented, both in [Sage Reference Manual](http://doc.sagemath.org/html/en/reference/) and in [Sage Constructions](http://doc.sagemath.org/html/en/constructions/), see [here](https://git.sagemath.org/sage.git/commit?id=ddeef52c783ef2f87c21b4b26e4410ace5007f02).",
    "created_at": "2017-09-07T14:41:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8603",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8603#issuecomment-77928",
    "user": "@egourgoulhon"
}
```

Replying to [comment:16 kcrisman]:
> Excellent.  Is this documented via a test?

Yes this is documented, both in [Sage Reference Manual](http://doc.sagemath.org/html/en/reference/) and in [Sage Constructions](http://doc.sagemath.org/html/en/constructions/), see [here](https://git.sagemath.org/sage.git/commit?id=ddeef52c783ef2f87c21b4b26e4410ace5007f02).



---

archive/issue_comments_077929.json:
```json
{
    "body": "Sweet.  Strange that it didn't cause any doctest errors then?  If it didn't, we should make sure to include at least two of the examples on the ticket in the doc *somewhere*.",
    "created_at": "2017-09-07T17:30:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8603",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8603#issuecomment-77929",
    "user": "@kcrisman"
}
```

Sweet.  Strange that it didn't cause any doctest errors then?  If it didn't, we should make sure to include at least two of the examples on the ticket in the doc *somewhere*.



---

archive/issue_comments_077930.json:
```json
{
    "body": "Changing status from needs_info to positive_review.",
    "created_at": "2017-09-07T17:30:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8603",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8603#issuecomment-77930",
    "user": "@kcrisman"
}
```

Changing status from needs_info to positive_review.



---

archive/issue_comments_077931.json:
```json
{
    "body": "Replying to [comment:19 kcrisman]:\n> Sweet.  Strange that it didn't cause any doctest errors then?  If it didn't, we should make sure to include at least two of the examples on the ticket in the doc *somewhere*.\n\nI am not sure to understand what you mean. In the current version, as integrated in Sage 8.1.beta4, there are doctests like\n\n```\nsage: f = piecewise([((-1,0), -1), ((0,1), 1)])\nsage: f.fourier_series_partial_sum(5)\n4/5*sin(5*pi*x)/pi + 4/3*sin(3*pi*x)/pi + 4*sin(pi*x)/pi\n```\n\nIn Sage <= 8.0, this would have returned (*)\n\n```\n4/3*sin(3*pi*x)/pi + 4*sin(pi*x)/pi\n```\n\n\n(*) with the half-period added as the second argument, i.e. `f.fourier_series_partial_sum(5, 1)`)",
    "created_at": "2017-09-07T19:30:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8603",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8603#issuecomment-77931",
    "user": "@egourgoulhon"
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

archive/issue_comments_077932.json:
```json
{
    "body": "My concern was just that the *correct* nature was doctested, not the wrong one, and that we really did have that to test against regression at some point.  Good!",
    "created_at": "2017-09-07T21:34:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8603",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8603#issuecomment-77932",
    "user": "@kcrisman"
}
```

My concern was just that the *correct* nature was doctested, not the wrong one, and that we really did have that to test against regression at some point.  Good!



---

archive/issue_comments_077933.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2017-12-12T08:23:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8603",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8603#issuecomment-77933",
    "user": "@embray"
}
```

Resolution: wontfix



---

archive/issue_comments_077934.json:
```json
{
    "body": "I wonder why \"wontfix\" since the issue is fixed in 8.1.beta4.\nPaul",
    "created_at": "2017-12-12T13:27:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8603",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8603#issuecomment-77934",
    "user": "@zimmermann6"
}
```

I wonder why "wontfix" since the issue is fixed in 8.1.beta4.
Paul



---

archive/issue_comments_077935.json:
```json
{
    "body": "Replying to [comment:23 zimmerma]:\n> I wonder why \"wontfix\" since the issue is fixed in 8.1.beta4.\n> Paul\nActually, as said in comment:15, the issue is fixed in another ticket: #23672, hence the \"sage-duplicate/invalid/wontfix\" milestone for the current one and the \"wonfix\" resolution.",
    "created_at": "2017-12-12T13:41:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8603",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8603#issuecomment-77935",
    "user": "@egourgoulhon"
}
```

Replying to [comment:23 zimmerma]:
> I wonder why "wontfix" since the issue is fixed in 8.1.beta4.
> Paul
Actually, as said in comment:15, the issue is fixed in another ticket: #23672, hence the "sage-duplicate/invalid/wontfix" milestone for the current one and the "wonfix" resolution.



---

archive/issue_comments_077936.json:
```json
{
    "body": "Hey, do non-release managers get to mark \"closed\"?  That would be a change in protocol.\n\nAlso, maybe the resolution should be \"fixed\" or \"duplicate\" if it is indeed fixed in another ticket?",
    "created_at": "2017-12-12T15:18:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8603",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8603#issuecomment-77936",
    "user": "@kcrisman"
}
```

Hey, do non-release managers get to mark "closed"?  That would be a change in protocol.

Also, maybe the resolution should be "fixed" or "duplicate" if it is indeed fixed in another ticket?



---

archive/issue_comments_077937.json:
```json
{
    "body": "Resolution changed from wontfix to duplicate",
    "created_at": "2017-12-12T15:18:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8603",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8603#issuecomment-77937",
    "user": "@kcrisman"
}
```

Resolution changed from wontfix to duplicate



---

archive/issue_comments_077938.json:
```json
{
    "body": "Replying to [comment:26 kcrisman]:\n> Hey, do non-release managers get to mark \"closed\"?  That would be a change in protocol.\n> \n\nThis was announced in https://groups.google.com/d/msg/sage-release/4bIUu1NECwY/we3BMdkeAAAJ with apparently the approval of the release manager.\n\n> Also, maybe the resolution should be \"fixed\" or \"duplicate\" if it is indeed fixed in another ticket?\n\nAh yes, you are right (I thought this was automatically set to \"wontfix\"  while closing \"sage-duplicate/invalid/wontfix\" tickets).",
    "created_at": "2017-12-12T15:27:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8603",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8603#issuecomment-77938",
    "user": "@egourgoulhon"
}
```

Replying to [comment:26 kcrisman]:
> Hey, do non-release managers get to mark "closed"?  That would be a change in protocol.
> 

This was announced in https://groups.google.com/d/msg/sage-release/4bIUu1NECwY/we3BMdkeAAAJ with apparently the approval of the release manager.

> Also, maybe the resolution should be "fixed" or "duplicate" if it is indeed fixed in another ticket?

Ah yes, you are right (I thought this was automatically set to "wontfix"  while closing "sage-duplicate/invalid/wontfix" tickets).



---

archive/issue_comments_077939.json:
```json
{
    "body": "Replying to [comment:27 egourgoulhon]:\n> Replying to [comment:26 kcrisman]:\n> > Hey, do non-release managers get to mark \"closed\"?  That would be a change in protocol.\n> > \n> \n> This was announced in https://groups.google.com/d/msg/sage-release/4bIUu1NECwY/we3BMdkeAAAJ with apparently the approval of the release manager.\n> \n\n10 hours ago :-) but this will be welcome for obvious dupes etc.\n\n> > Also, maybe the resolution should be \"fixed\" or \"duplicate\" if it is indeed fixed in another ticket?\n> \n> Ah yes, you are right (I thought this was automatically set to \"wontfix\"  while closing \"sage-duplicate/invalid/wontfix\" tickets).\n\nYeah, that might be the default, but typically we try to be precise on this. Nice.",
    "created_at": "2017-12-12T19:15:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8603",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8603#issuecomment-77939",
    "user": "@kcrisman"
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
