# Issue 2516: generalized hypergeometric functions should be implemented

archive/issues_002516.json:
```json
{
    "body": "Assignee: cwitty\n\nCC:  burcin fstan kcrisman ktkohl benjaminfjones dsm eviatarbach mmezzarobba\n\nSage should have support for [generalized hypergeometric functions](http://mathworld.wolfram.com/GeneralizedHypergeometricFunction.html). They are an important class of special functions. They show up everywhere from differential equations to binomial coefficient identities.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2516\n\n",
    "created_at": "2008-03-14T09:55:34Z",
    "labels": [
        "misc",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.3",
    "title": "generalized hypergeometric functions should be implemented",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2516",
    "user": "ddrake"
}
```
Assignee: cwitty

CC:  burcin fstan kcrisman ktkohl benjaminfjones dsm eviatarbach mmezzarobba

Sage should have support for [generalized hypergeometric functions](http://mathworld.wolfram.com/GeneralizedHypergeometricFunction.html). They are an important class of special functions. They show up everywhere from differential equations to binomial coefficient identities.

Issue created by migration from https://trac.sagemath.org/ticket/2516





---

archive/issue_comments_017088.json:
```json
{
    "body": "Attachment [hyper.patch](tarball://root/attachments/some-uuid/ticket2516/hyper.patch) by fredrik.johansson created at 2010-07-26 03:17:42\n\ntentative implementation of generalized hypergeometric functions",
    "created_at": "2010-07-26T03:17:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2516",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2516#issuecomment-17088",
    "user": "fredrik.johansson"
}
```

Attachment [hyper.patch](tarball://root/attachments/some-uuid/ticket2516/hyper.patch) by fredrik.johansson created at 2010-07-26 03:17:42

tentative implementation of generalized hypergeometric functions



---

archive/issue_comments_017089.json:
```json
{
    "body": "Changing status from new to needs_work.",
    "created_at": "2010-07-26T03:35:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2516",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2516#issuecomment-17089",
    "user": "fredrik.johansson"
}
```

Changing status from new to needs_work.



---

archive/issue_comments_017090.json:
```json
{
    "body": "I've attached essentially the code I wrote during with Sage Days 24 with some additions. Features include:\n\n* Representation of PFQs as symbolic functions (with automatic simplification) and in always-unevaluated form\n\n* Numerical evaluation (wrapping mpmath)\n\n* Evaluation in terms of elementary functions in some simple cases\n\nImportant missing features include:\n\n* Rewriting symbolic sums as PFQs\n\n* Evaluation in terms of polygamma functions\n\n* Various transformations permitting closed-form evaluation in special cases\n\nThe patch includes symbolic versions of Bessel functions, which can be expanded as PFQs. This obviously needs to be merged with the existing Bessel function classes.\n\nThe main remaining issue is to handle multivariate symbolic functions properly (the current approach in Function_PFQ is something of a hack). Also, in the present patch, there are two PFQ classes. This is partially due to limitations/awkwardness of the symbolic function class, but regardless of whether necessary, it may be desirable to have a separate \"backend\" representation for hypergeometric functions that doesn't need to be concerned with automatic evaluation, numerical conversions, etc. I'm not sure what's the best way to organize it all.",
    "created_at": "2010-07-26T03:35:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2516",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2516#issuecomment-17090",
    "user": "fredrik.johansson"
}
```

I've attached essentially the code I wrote during with Sage Days 24 with some additions. Features include:

* Representation of PFQs as symbolic functions (with automatic simplification) and in always-unevaluated form

* Numerical evaluation (wrapping mpmath)

* Evaluation in terms of elementary functions in some simple cases

Important missing features include:

* Rewriting symbolic sums as PFQs

* Evaluation in terms of polygamma functions

* Various transformations permitting closed-form evaluation in special cases

The patch includes symbolic versions of Bessel functions, which can be expanded as PFQs. This obviously needs to be merged with the existing Bessel function classes.

The main remaining issue is to handle multivariate symbolic functions properly (the current approach in Function_PFQ is something of a hack). Also, in the present patch, there are two PFQ classes. This is partially due to limitations/awkwardness of the symbolic function class, but regardless of whether necessary, it may be desirable to have a separate "backend" representation for hypergeometric functions that doesn't need to be concerned with automatic evaluation, numerical conversions, etc. I'm not sure what's the best way to organize it all.



---

archive/issue_comments_017091.json:
```json
{
    "body": "See also #9908, which is at least related (we need to translate Maxima hg functions).\n\nAlso, I think that we already have a lot of Bessel functions implemented, though they are not yet symbolic.",
    "created_at": "2011-02-17T01:52:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2516",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2516#issuecomment-17091",
    "user": "kcrisman"
}
```

See also #9908, which is at least related (we need to translate Maxima hg functions).

Also, I think that we already have a lot of Bessel functions implemented, though they are not yet symbolic.



---

archive/issue_comments_017092.json:
```json
{
    "body": "Changing component.  But this is a really nice start, hopefully can be combined with some of the currently existing bessel stuff etc.",
    "created_at": "2012-05-26T19:14:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2516",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2516#issuecomment-17092",
    "user": "kcrisman"
}
```

Changing component.  But this is a really nice start, hopefully can be combined with some of the currently existing bessel stuff etc.



---

archive/issue_comments_017093.json:
```json
{
    "body": "Changing component from misc to symbolics.",
    "created_at": "2012-05-26T19:14:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2516",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2516#issuecomment-17093",
    "user": "kcrisman"
}
```

Changing component from misc to symbolics.



---

archive/issue_comments_017094.json:
```json
{
    "body": "Okay, I'm going to see what can be done to get this merged.",
    "created_at": "2012-05-26T19:59:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2516",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2516#issuecomment-17094",
    "user": "dsm"
}
```

Okay, I'm going to see what can be done to get this merged.



---

archive/issue_comments_017095.json:
```json
{
    "body": "Having played around with this some, I think it'll be pretty straightforward to get in.. *after* we have Burcin's ticket allowing numerical_approx to take more general kwargs.  If it weren't for the need to maintain backward compatibility with the algorithm kwarg for the old bessel functions, life would be easier.\n\nI have a half-functional wrapper which monkeypatches things to sort of get them to work, but once that patch gets in it becomes much simpler.  So I think this should stay in a holding pattern until we get that one in.",
    "created_at": "2012-05-26T22:55:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2516",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2516#issuecomment-17095",
    "user": "dsm"
}
```

Having played around with this some, I think it'll be pretty straightforward to get in.. *after* we have Burcin's ticket allowing numerical_approx to take more general kwargs.  If it weren't for the need to maintain backward compatibility with the algorithm kwarg for the old bessel functions, life would be easier.

I have a half-functional wrapper which monkeypatches things to sort of get them to work, but once that patch gets in it becomes much simpler.  So I think this should stay in a holding pattern until we get that one in.



---

archive/issue_comments_017096.json:
```json
{
    "body": "> If it weren't for the need to maintain backward compatibility with the algorithm kwarg for the old bessel functions, life would be easier.\nSince #4102 is nearly finished, and has at least sort of dealt with this issue, perhaps one can just ignore that part of the Bessel issue.  Instead, one could just add the `_expand_hyper` methods to the stuff there.  I do like the idea here and it would be a shame for it to bit rot further...",
    "created_at": "2013-04-25T02:21:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2516",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2516#issuecomment-17096",
    "user": "kcrisman"
}
```

> If it weren't for the need to maintain backward compatibility with the algorithm kwarg for the old bessel functions, life would be easier.
Since #4102 is nearly finished, and has at least sort of dealt with this issue, perhaps one can just ignore that part of the Bessel issue.  Instead, one could just add the `_expand_hyper` methods to the stuff there.  I do like the idea here and it would be a shame for it to bit rot further...



---

archive/issue_comments_017097.json:
```json
{
    "body": "Here is an initial version of an updated patch. It needs some work because it's failing a few tests, but I just wanted to post for comments.",
    "created_at": "2013-07-05T11:19:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2516",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2516#issuecomment-17097",
    "user": "eviatarbach"
}
```

Here is an initial version of an updated patch. It needs some work because it's failing a few tests, but I just wanted to post for comments.



---

archive/issue_comments_017098.json:
```json
{
    "body": "Attachment [hyper3.patch](tarball://root/attachments/some-uuid/ticket2516/hyper3.patch) by eviatarbach created at 2013-07-05 11:20:13",
    "created_at": "2013-07-05T11:20:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2516",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2516#issuecomment-17098",
    "user": "eviatarbach"
}
```

Attachment [hyper3.patch](tarball://root/attachments/some-uuid/ticket2516/hyper3.patch) by eviatarbach created at 2013-07-05 11:20:13



---

archive/issue_comments_017099.json:
```json
{
    "body": "Two of the failing doctests are caused by #14858.",
    "created_at": "2013-07-05T20:07:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2516",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2516#issuecomment-17099",
    "user": "eviatarbach"
}
```

Two of the failing doctests are caused by #14858.



---

archive/issue_comments_017100.json:
```json
{
    "body": "Changing status from needs_work to needs_info.",
    "created_at": "2013-07-14T02:48:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2516",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2516#issuecomment-17100",
    "user": "eviatarbach"
}
```

Changing status from needs_work to needs_info.



---

archive/issue_comments_017101.json:
```json
{
    "body": "Plotting is now working fine (with the approach from #14801, thanks Volker!), except for getting deprecation warnings about using unnamed function parameters, which I have not been able to debug. Does anyone know how to fix this?\n\nAnother strange doctest failure is the one in `_fast_callable_`; when I run it from interactive mode I get `{CommutativeRings.element_class}(v_0)`, but the doctest returns `{Fields.element_class}(v_0)`. Why is that?\n\nOther than that the patch should be ready for review.",
    "created_at": "2013-07-14T02:48:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2516",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2516#issuecomment-17101",
    "user": "eviatarbach"
}
```

Plotting is now working fine (with the approach from #14801, thanks Volker!), except for getting deprecation warnings about using unnamed function parameters, which I have not been able to debug. Does anyone know how to fix this?

Another strange doctest failure is the one in `_fast_callable_`; when I run it from interactive mode I get `{CommutativeRings.element_class}(v_0)`, but the doctest returns `{Fields.element_class}(v_0)`. Why is that?

Other than that the patch should be ready for review.



---

archive/issue_comments_017102.json:
```json
{
    "body": "Attachment [trac_2516.patch](tarball://root/attachments/some-uuid/ticket2516/trac_2516.patch) by eviatarbach created at 2013-07-14 02:49:22",
    "created_at": "2013-07-14T02:49:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2516",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2516#issuecomment-17102",
    "user": "eviatarbach"
}
```

Attachment [trac_2516.patch](tarball://root/attachments/some-uuid/ticket2516/trac_2516.patch) by eviatarbach created at 2013-07-14 02:49:22



---

archive/issue_comments_017103.json:
```json
{
    "body": "New patch fixes a circular import issue which caused a problem with numerical evaluation; see #13028.",
    "created_at": "2013-07-15T03:07:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2516",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2516#issuecomment-17103",
    "user": "eviatarbach"
}
```

New patch fixes a circular import issue which caused a problem with numerical evaluation; see #13028.



---

archive/issue_comments_017104.json:
```json
{
    "body": "Attachment [trac_2516_2.patch](tarball://root/attachments/some-uuid/ticket2516/trac_2516_2.patch) by eviatarbach created at 2013-07-15 03:08:20",
    "created_at": "2013-07-15T03:08:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2516",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2516#issuecomment-17104",
    "user": "eviatarbach"
}
```

Attachment [trac_2516_2.patch](tarball://root/attachments/some-uuid/ticket2516/trac_2516_2.patch) by eviatarbach created at 2013-07-15 03:08:20



---

archive/issue_comments_017105.json:
```json
{
    "body": "Changing keywords from \"\" to \"hypergeometric\".",
    "created_at": "2014-03-06T17:09:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2516",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2516#issuecomment-17105",
    "user": "chapoton"
}
```

Changing keywords from "" to "hypergeometric".



---

archive/issue_comments_017106.json:
```json
{
    "body": "Rebased on 6.2.beta7. The branch includes the (already merged) #14802. I fixed some but not all doctests.\n----\nNew commits:",
    "created_at": "2014-04-10T12:54:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2516",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2516#issuecomment-17106",
    "user": "rws"
}
```

Rebased on 6.2.beta7. The branch includes the (already merged) #14802. I fixed some but not all doctests.
----
New commits:



---

archive/issue_comments_017107.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2014-04-10T12:54:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2516",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2516#issuecomment-17107",
    "user": "rws"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_017108.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2014-04-10T12:54:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2516",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2516#issuecomment-17108",
    "user": "rws"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_017109.json:
```json
{
    "body": "Three of the remaining doctest errors come from:\n\n```\nsage: f=fast_callable(hypergeometric([x], [], 2),domain=CDF,expect_one_var=True)\nsage: f(8)\n/home/ralf/sage/local/lib/python2.7/site-packages/IPython/core/interactiveshell.py:2834: DeprecationWarning: Substitution using function-call syntax and unnamed arguments is deprecated and will be removed from a future release of Sage; you can use named arguments instead, like EXPR(x=..., y=...)\nSee http://trac.sagemath.org/5930 for details.\n  exec code_obj in self.user_global_ns, self.user_ns\n1.0\nsage: f(x=8)\n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n<ipython-input-3-499d03e2f57c> in <module>()\n----> 1 f(x=Integer(8))\n\nTypeError: __call__() got an unexpected keyword argument 'x'\n```\n\nThe deprecation warning is triggered in `plot()` and `complex_plot()` with hypergeometric argument. I'm unsure where exactly the problem is. At the least `fast_callable()` should behave consistently when given a named parameter, and if there is a problem in `hypergeometric`, `fast_callable()` should give the right warning. So, maybe a separate ticket for this is necessary.",
    "created_at": "2014-04-11T08:55:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2516",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2516#issuecomment-17109",
    "user": "rws"
}
```

Three of the remaining doctest errors come from:

```
sage: f=fast_callable(hypergeometric([x], [], 2),domain=CDF,expect_one_var=True)
sage: f(8)
/home/ralf/sage/local/lib/python2.7/site-packages/IPython/core/interactiveshell.py:2834: DeprecationWarning: Substitution using function-call syntax and unnamed arguments is deprecated and will be removed from a future release of Sage; you can use named arguments instead, like EXPR(x=..., y=...)
See http://trac.sagemath.org/5930 for details.
  exec code_obj in self.user_global_ns, self.user_ns
1.0
sage: f(x=8)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-3-499d03e2f57c> in <module>()
----> 1 f(x=Integer(8))

TypeError: __call__() got an unexpected keyword argument 'x'
```

The deprecation warning is triggered in `plot()` and `complex_plot()` with hypergeometric argument. I'm unsure where exactly the problem is. At the least `fast_callable()` should behave consistently when given a named parameter, and if there is a problem in `hypergeometric`, `fast_callable()` should give the right warning. So, maybe a separate ticket for this is necessary.



---

archive/issue_comments_017110.json:
```json
{
    "body": "Thanks for working on this!\n\nI believe you set the incorrect authors though.",
    "created_at": "2014-04-11T09:02:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2516",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2516#issuecomment-17110",
    "user": "eviatarbach"
}
```

Thanks for working on this!

I believe you set the incorrect authors though.



---

archive/issue_comments_017111.json:
```json
{
    "body": "I got the plotting problem before too, see comment 17. It's something in the `fast_callable` implementation if I recall correctly, but I couldn't figure out how to fix it at the time.",
    "created_at": "2014-04-11T09:08:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2516",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2516#issuecomment-17111",
    "user": "eviatarbach"
}
```

I got the plotting problem before too, see comment 17. It's something in the `fast_callable` implementation if I recall correctly, but I couldn't figure out how to fix it at the time.



---

archive/issue_comments_017112.json:
```json
{
    "body": "Replying to [comment:26 eviatarbach]:\n> I believe you set the incorrect authors though.\nOops, sorry.\n> I got the plotting problem before too, see comment 17. It's something in the `fast_callable` implementation if I recall correctly, but I couldn't figure out how to fix it at the time.\n`exp_integral_e()` is a `BuiltinFunction` too, and needs two parameters but\n\n```\nsage: f=fast_callable(exp_integral_e(x,1),domain=CDF,expect_one_var=True)\nsage: f(8)\n0.0452114820619\nsage: f=fast_callable(hypergeometric([x], [], y),domain=CDF,vars=[x,y])\nsage: f(8,9)\n5.96046447754e-08\nsage: f=fast_callable(hypergeometric([x], [], 2),domain=CDF,vars=[x])\nsage: f(8)\n1.0\n```\n\nso I changed \n\n```\n        f = fast_callable(f, domain=CDF, expect_one_var=TRUE)\n```\n\nto\n\n```\n        f = fast_callable(f, domain=CDF, vars=[x])\n```\n\nin `complex_plot()`. Now the one var case works but not the two etc. So it seems the handling of `expect_one_var` in `fast_callable()` is wrong, as I already said.",
    "created_at": "2014-04-11T09:38:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2516",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2516#issuecomment-17112",
    "user": "rws"
}
```

Replying to [comment:26 eviatarbach]:
> I believe you set the incorrect authors though.
Oops, sorry.
> I got the plotting problem before too, see comment 17. It's something in the `fast_callable` implementation if I recall correctly, but I couldn't figure out how to fix it at the time.
`exp_integral_e()` is a `BuiltinFunction` too, and needs two parameters but

```
sage: f=fast_callable(exp_integral_e(x,1),domain=CDF,expect_one_var=True)
sage: f(8)
0.0452114820619
sage: f=fast_callable(hypergeometric([x], [], y),domain=CDF,vars=[x,y])
sage: f(8,9)
5.96046447754e-08
sage: f=fast_callable(hypergeometric([x], [], 2),domain=CDF,vars=[x])
sage: f(8)
1.0
```

so I changed 

```
        f = fast_callable(f, domain=CDF, expect_one_var=TRUE)
```

to

```
        f = fast_callable(f, domain=CDF, vars=[x])
```

in `complex_plot()`. Now the one var case works but not the two etc. So it seems the handling of `expect_one_var` in `fast_callable()` is wrong, as I already said.



---

archive/issue_comments_017113.json:
```json
{
    "body": "Forget all what I wrote. The deprecation warning is only printed once per session, which makes my conclusions arbitrary.",
    "created_at": "2014-04-11T14:57:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2516",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2516#issuecomment-17113",
    "user": "rws"
}
```

Forget all what I wrote. The deprecation warning is only printed once per session, which makes my conclusions arbitrary.



---

archive/issue_comments_017114.json:
```json
{
    "body": "Replying to [comment:17 eviatarbach]:\n> It's something in the `fast_callable` implementation if I recall correctly, but I couldn't figure out how to fix it at the time.\nWhat's certain is that `Wrapper_cdf.__call__()` gets the same arguments as with other working examples but that `SR._call_element_()` gets called where the deprecation warning happens while with `exp_integral_e(x,1)` its `_eval_()` is called directly.\n> Another strange doctest failure is the one in `_fast_callable_`; when I run it from interactive mode I get `{CommutativeRings.element_class}(v_0)`, but the doctest returns `{Fields.element_class}(v_0)`. Why is that?\nInterestingly if use `h=exp_integral_e(x,1)` in the same doctest, I get\n\n```\nsage: h._fast_callable_(etb)\n{exp_integral_e}(v_0, 1)\n```\n\nSo why is it not `hypergeometric(None, None, v_0)` or similar in the doctest?",
    "created_at": "2014-04-12T09:15:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2516",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2516#issuecomment-17114",
    "user": "rws"
}
```

Replying to [comment:17 eviatarbach]:
> It's something in the `fast_callable` implementation if I recall correctly, but I couldn't figure out how to fix it at the time.
What's certain is that `Wrapper_cdf.__call__()` gets the same arguments as with other working examples but that `SR._call_element_()` gets called where the deprecation warning happens while with `exp_integral_e(x,1)` its `_eval_()` is called directly.
> Another strange doctest failure is the one in `_fast_callable_`; when I run it from interactive mode I get `{CommutativeRings.element_class}(v_0)`, but the doctest returns `{Fields.element_class}(v_0)`. Why is that?
Interestingly if use `h=exp_integral_e(x,1)` in the same doctest, I get

```
sage: h._fast_callable_(etb)
{exp_integral_e}(v_0, 1)
```

So why is it not `hypergeometric(None, None, v_0)` or similar in the doctest?



---

archive/issue_comments_017115.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2014-04-12T15:38:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2516",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2516#issuecomment-17115",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_017116.json:
```json
{
    "body": "This fixes all except the one in `_fast_callable_` and two others I haven't looked closely at. Specifically, I resolved the deprecation warning by excluding dynamic classes from this warning.",
    "created_at": "2014-04-12T15:41:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2516",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2516#issuecomment-17116",
    "user": "rws"
}
```

This fixes all except the one in `_fast_callable_` and two others I haven't looked closely at. Specifically, I resolved the deprecation warning by excluding dynamic classes from this warning.



---

archive/issue_comments_017117.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2014-04-13T14:41:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2516",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2516#issuecomment-17117",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_017118.json:
```json
{
    "body": "Fixed all doctests. Please review. I had to exclude the hypergeometric function from random symbolic tests as that code blindly applies real numbers as parameters, and I didn't want to add `try: ... except ValueError: pass` there.",
    "created_at": "2014-04-13T14:45:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2516",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2516#issuecomment-17118",
    "user": "rws"
}
```

Fixed all doctests. Please review. I had to exclude the hypergeometric function from random symbolic tests as that code blindly applies real numbers as parameters, and I didn't want to add `try: ... except ValueError: pass` there.



---

archive/issue_comments_017119.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2014-04-13T14:45:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2516",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2516#issuecomment-17119",
    "user": "rws"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_017120.json:
```json
{
    "body": "Excellent work! I wasn't able to checkout the branch here for testing, but I noticed one thing for the maxima_lib interfacing:\n- You are installing an extra rule in `mqapply_to_sage`, which I assume is correct. This rule registered in the special_max_to_sage dictionary: Great! that's what you're supposed to do\n- However, for conversion back, there should be a corresponding entry in special_sage_to_max as well, and you're not adding that. You'd have to test, but from the rule in the other direction, I'd guess it should be something like:\n\n```\nsage.functions.hypergeometric.hypergeometric : lambda A, B, X : [[mqapply],[[max_hyper, max_array],lisp_length(A)-1,lisp_length(B)-1],A,B,X]\n```\n\nwhere\n\n```\nlisp_length=EclObject('length')\n```\n\n\nIf you don't put this rule in place, you'll find that things like \"limit\", \"integral\" and \"sum\" (which use `sr_to_max`) will probably not work correctly with hypergeometric function. (in fact, I'm not so sure maxima has much support for them anyway, but at least we should make sure that the functions can survive a round-trip)\n\nAnother bit: the addition to `sr_to_max`\n\n```\n+ elif op == tuple:\n+     return maxima(expr.operands()).ecl()\n```\n\nshould read\n\n```\n+ elif op == tuple:\n+     return EclObject( ([mlist],(sr_to_max(op) for op in expr.operands())) )\n```\n\nif a \"symbolic tuple\" should indeed be translated into a maxima list.\n\n(the branch attached to this ticket currently doesn't build to a usable executable for me. I'm having some libntl conflict)",
    "created_at": "2014-04-13T19:57:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2516",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2516#issuecomment-17120",
    "user": "nbruin"
}
```

Excellent work! I wasn't able to checkout the branch here for testing, but I noticed one thing for the maxima_lib interfacing:
- You are installing an extra rule in `mqapply_to_sage`, which I assume is correct. This rule registered in the special_max_to_sage dictionary: Great! that's what you're supposed to do
- However, for conversion back, there should be a corresponding entry in special_sage_to_max as well, and you're not adding that. You'd have to test, but from the rule in the other direction, I'd guess it should be something like:

```
sage.functions.hypergeometric.hypergeometric : lambda A, B, X : [[mqapply],[[max_hyper, max_array],lisp_length(A)-1,lisp_length(B)-1],A,B,X]
```

where

```
lisp_length=EclObject('length')
```


If you don't put this rule in place, you'll find that things like "limit", "integral" and "sum" (which use `sr_to_max`) will probably not work correctly with hypergeometric function. (in fact, I'm not so sure maxima has much support for them anyway, but at least we should make sure that the functions can survive a round-trip)

Another bit: the addition to `sr_to_max`

```
+ elif op == tuple:
+     return maxima(expr.operands()).ecl()
```

should read

```
+ elif op == tuple:
+     return EclObject( ([mlist],(sr_to_max(op) for op in expr.operands())) )
```

if a "symbolic tuple" should indeed be translated into a maxima list.

(the branch attached to this ticket currently doesn't build to a usable executable for me. I'm having some libntl conflict)



---

archive/issue_comments_017121.json:
```json
{
    "body": "I found this suspicious (it's in the implementation of the `_fast_callable_` method\n\n```\n+ self.__name__ = self.__repr__() # was clobbered by category mechanics\n+ return etb.call(self, *map(etb.var, etb._vars))\n```\n\nOne shouldn't touch the `__name__` attribute, and certainly not during arbitrary executing code! Is it clear what code depends on the `__name__` being identical to `__repr__`? Can we solve this issue (cheaply) during `__init__`, or perhaps avoid the clobbering altogether?",
    "created_at": "2014-04-14T02:10:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2516",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2516#issuecomment-17121",
    "user": "nbruin"
}
```

I found this suspicious (it's in the implementation of the `_fast_callable_` method

```
+ self.__name__ = self.__repr__() # was clobbered by category mechanics
+ return etb.call(self, *map(etb.var, etb._vars))
```

One shouldn't touch the `__name__` attribute, and certainly not during arbitrary executing code! Is it clear what code depends on the `__name__` being identical to `__repr__`? Can we solve this issue (cheaply) during `__init__`, or perhaps avoid the clobbering altogether?



---

archive/issue_comments_017122.json:
```json
{
    "body": "Replying to [comment:36 nbruin]:\n> One shouldn't touch the `__name__` attribute, and certainly not during arbitrary executing code!\nDo you have a reference for that?\n> Is it clear what code depends on the `__name__` being identical to `__repr__`?\nIt fixes the issue mentioned above where the doctest gets different output than interactive Sage. The first doctest in `_fast_callable_`.\n> Can we solve this issue (cheaply) during `__init__`.\nNope it happens after `__init__`\n> or perhaps avoid the clobbering altogether?\nIt is a consequence of `hypergeometric` being a SE with tuples as parameter. In the`Expression` constructor the class gets changed using `dynamic_class()` and this appears to be responsible.\n\nOverall, all long tests pass and I see no reason to hold this old ticket any longer.",
    "created_at": "2014-04-14T03:39:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2516",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2516#issuecomment-17122",
    "user": "rws"
}
```

Replying to [comment:36 nbruin]:
> One shouldn't touch the `__name__` attribute, and certainly not during arbitrary executing code!
Do you have a reference for that?
> Is it clear what code depends on the `__name__` being identical to `__repr__`?
It fixes the issue mentioned above where the doctest gets different output than interactive Sage. The first doctest in `_fast_callable_`.
> Can we solve this issue (cheaply) during `__init__`.
Nope it happens after `__init__`
> or perhaps avoid the clobbering altogether?
It is a consequence of `hypergeometric` being a SE with tuples as parameter. In the`Expression` constructor the class gets changed using `dynamic_class()` and this appears to be responsible.

Overall, all long tests pass and I see no reason to hold this old ticket any longer.



---

archive/issue_comments_017123.json:
```json
{
    "body": "Replying to [comment:37 rws]:\n> Replying to [comment:36 nbruin]:\n> > One shouldn't touch the `__name__` attribute, and certainly not during arbitrary executing code!\n> Do you have a reference for that?\n\nWell, you can look it up. Python uses `__name__` for any \"named\" object (e.g., defined by a `def` or a `class` or modules). These things aren't supposed to change (they are used for introspection). The fact that it does (and that that matters!) points to either a flaw in the category system or in the way it is used here.\n\n> It is a consequence of `hypergeometric` being a SE with tuples as parameter. In the`Expression` constructor the class gets changed using `dynamic_class()` and this appears to be responsible.\n\n> Overall, all long tests pass and I see no reason to hold this old ticket any longer.\n\nThe issues around `sr_to_max` should be fixed (and that's straightforward).",
    "created_at": "2014-04-14T05:34:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2516",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2516#issuecomment-17123",
    "user": "nbruin"
}
```

Replying to [comment:37 rws]:
> Replying to [comment:36 nbruin]:
> > One shouldn't touch the `__name__` attribute, and certainly not during arbitrary executing code!
> Do you have a reference for that?

Well, you can look it up. Python uses `__name__` for any "named" object (e.g., defined by a `def` or a `class` or modules). These things aren't supposed to change (they are used for introspection). The fact that it does (and that that matters!) points to either a flaw in the category system or in the way it is used here.

> It is a consequence of `hypergeometric` being a SE with tuples as parameter. In the`Expression` constructor the class gets changed using `dynamic_class()` and this appears to be responsible.

> Overall, all long tests pass and I see no reason to hold this old ticket any longer.

The issues around `sr_to_max` should be fixed (and that's straightforward).



---

archive/issue_comments_017124.json:
```json
{
    "body": "OK, the problem is in `ext.fast_callable.function_name`, which gets called by `sage.ext.fast_callable.ExpressionCall.__repr__`. with as argument the \"function\" component of the ExpressionCall. The problem is: an expression doesn't have a `__name__`. So you end up finding a `__name__` somewhere higher in the inheritance. You just end up putting an extraneous attribute on the expression. To illustrate the nasty side-effect:\n\n```\nsage: h =  hypergeometric([],[],x)\nsage: h.__name__\n'CommutativeRings.element_class'\nsage: from sage.ext.fast_callable import ExpressionTreeBuilder\nsage: etb = ExpressionTreeBuilder(vars=['x'])\nsage: _ = h._fast_callable_(etb)\nsage: h.__name__\n'hypergeometric((), (), x)'\n```\n\nAs you see, `_fast_callable_` now has a side-effect on `h`! \n\nA better solution would be to adapt the routine `ext.fast_callable.function_name` (or the way it gets used). It's clear you're now feeding it things it wasn't designed for.",
    "created_at": "2014-04-14T06:34:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2516",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2516#issuecomment-17124",
    "user": "nbruin"
}
```

OK, the problem is in `ext.fast_callable.function_name`, which gets called by `sage.ext.fast_callable.ExpressionCall.__repr__`. with as argument the "function" component of the ExpressionCall. The problem is: an expression doesn't have a `__name__`. So you end up finding a `__name__` somewhere higher in the inheritance. You just end up putting an extraneous attribute on the expression. To illustrate the nasty side-effect:

```
sage: h =  hypergeometric([],[],x)
sage: h.__name__
'CommutativeRings.element_class'
sage: from sage.ext.fast_callable import ExpressionTreeBuilder
sage: etb = ExpressionTreeBuilder(vars=['x'])
sage: _ = h._fast_callable_(etb)
sage: h.__name__
'hypergeometric((), (), x)'
```

As you see, `_fast_callable_` now has a side-effect on `h`! 

A better solution would be to adapt the routine `ext.fast_callable.function_name` (or the way it gets used). It's clear you're now feeding it things it wasn't designed for.



---

archive/issue_comments_017125.json:
```json
{
    "body": "This should at least solve the maxima_lib translation problems.",
    "created_at": "2014-04-14T06:49:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2516",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2516#issuecomment-17125",
    "user": "nbruin"
}
```

This should at least solve the maxima_lib translation problems.



---

archive/issue_comments_017126.json:
```json
{
    "body": "Replying to [comment:40 nbruin]:\n> A better solution would be to adapt the routine `ext.fast_callable.function_name` (or the way it gets used). It's clear you're now feeding it things it wasn't designed for.\nYes but how to distinguish such a 'dynamical' expression from `Expression`? The type displayed (`sage.functions.hypergeometric.Expression_with_dynamic_methods`) cannot be tested for directly. To do it right it should not be hypergeometric-specific either.\n----\nNew commits:",
    "created_at": "2014-04-14T08:35:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2516",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2516#issuecomment-17126",
    "user": "rws"
}
```

Replying to [comment:40 nbruin]:
> A better solution would be to adapt the routine `ext.fast_callable.function_name` (or the way it gets used). It's clear you're now feeding it things it wasn't designed for.
Yes but how to distinguish such a 'dynamical' expression from `Expression`? The type displayed (`sage.functions.hypergeometric.Expression_with_dynamic_methods`) cannot be tested for directly. To do it right it should not be hypergeometric-specific either.
----
New commits:



---

archive/issue_comments_017127.json:
```json
{
    "body": "What about\n\n```\n+ if isinstance(fn, Expression) and str(type(fn)).find('Expression_with_dynamic_methods') >= 0:\n+     return \"{%r}\" % fn\n```\n\nAlternatively this seems to work too:\n\n```\n+ if isinstance(type(h),sage.structure.dynamic_class.DynamicMetaclass)\n+     return \"{%r}\" % fn\n```\n\nWouldn't one of these be safe enough?",
    "created_at": "2014-04-14T08:45:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2516",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2516#issuecomment-17127",
    "user": "rws"
}
```

What about

```
+ if isinstance(fn, Expression) and str(type(fn)).find('Expression_with_dynamic_methods') >= 0:
+     return "{%r}" % fn
```

Alternatively this seems to work too:

```
+ if isinstance(type(h),sage.structure.dynamic_class.DynamicMetaclass)
+     return "{%r}" % fn
```

Wouldn't one of these be safe enough?



---

archive/issue_comments_017128.json:
```json
{
    "body": "Replying to [comment:43 rws]:\n> Alternatively this seems to work too:\n> {{{\n> + if isinstance(type(h),sage.structure.dynamic_class.DynamicMetaclass)\n> +     return \"{%r}\" % fn\n> }}}\n> Wouldn't one of these be safe enough?\n\nI think the distinction should be easier to make. I don't think `__name__` is reasonable on any expression. Compare:\n\n\n```\nsage: h = hypergeometric([], [], x)\nsage: s = sin(x)\nsage: from sage.ext.fast_callable import ExpressionTreeBuilder\nsage: etb = ExpressionTreeBuilder(vars=['x'])\nsage: v = h._fast_callable_(etb)\nsage: w = s._fast_callable_(etb)\nsage: type(v.function())\n<class 'sage.functions.hypergeometric.Expression_with_dynamic_methods'>\nsage: type(w.function())\n<class 'sage.functions.trig.Function_sin'>\n```\n\nAs you can see, with more traditional functions, there's a rather more dedicated object in the function slot, for which the `__name__` can be expected to be quite descriptive. For an expression, the `__name__` attribute, if there's something there at all (and that there is seems a side-effect of the dynamic classes. Normally, `__name__` doesn't descend to class instances), can't really be descriptive. Looking at how to tell them apart:\n\n```\nsage: type(v.function()).mro()\n[sage.functions.hypergeometric.Expression_with_dynamic_methods,\n sage.symbolic.expression.Expression,\n sage.structure.element.CommutativeRingElement,\n sage.structure.element.RingElement,\n sage.structure.element.ModuleElement,\n sage.structure.element.Element,\n sage.structure.sage_object.SageObject,\n object]\nsage: type(w.function()).mro()\n[sage.functions.trig.Function_sin,\n sage.symbolic.function.GinacFunction,\n sage.symbolic.function.BuiltinFunction,\n sage.symbolic.function.Function,\n sage.structure.sage_object.SageObject,\n object]\n```\n\nSo my guess is that you only need `isinstance(type(h), sage.symbolic.expression.Expression)`, no need to check for substrings. On the other hand, your `sage.structure.dynamic_class.DynamicMetaclass` seems to work too, even though that class doesn't show up in the mro!\n\nI think we're running into a break-down of ducktyping here: the code as written previously assumed that if a `__name__` attribute is present, then it's meaningful. This is apparently not true for some dynamic classes and makes me think that maybe this `__name__` attribute shouldn't be provided (wherever that happens).",
    "created_at": "2014-04-14T15:29:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2516",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2516#issuecomment-17128",
    "user": "nbruin"
}
```

Replying to [comment:43 rws]:
> Alternatively this seems to work too:
> {{{
> + if isinstance(type(h),sage.structure.dynamic_class.DynamicMetaclass)
> +     return "{%r}" % fn
> }}}
> Wouldn't one of these be safe enough?

I think the distinction should be easier to make. I don't think `__name__` is reasonable on any expression. Compare:


```
sage: h = hypergeometric([], [], x)
sage: s = sin(x)
sage: from sage.ext.fast_callable import ExpressionTreeBuilder
sage: etb = ExpressionTreeBuilder(vars=['x'])
sage: v = h._fast_callable_(etb)
sage: w = s._fast_callable_(etb)
sage: type(v.function())
<class 'sage.functions.hypergeometric.Expression_with_dynamic_methods'>
sage: type(w.function())
<class 'sage.functions.trig.Function_sin'>
```

As you can see, with more traditional functions, there's a rather more dedicated object in the function slot, for which the `__name__` can be expected to be quite descriptive. For an expression, the `__name__` attribute, if there's something there at all (and that there is seems a side-effect of the dynamic classes. Normally, `__name__` doesn't descend to class instances), can't really be descriptive. Looking at how to tell them apart:

```
sage: type(v.function()).mro()
[sage.functions.hypergeometric.Expression_with_dynamic_methods,
 sage.symbolic.expression.Expression,
 sage.structure.element.CommutativeRingElement,
 sage.structure.element.RingElement,
 sage.structure.element.ModuleElement,
 sage.structure.element.Element,
 sage.structure.sage_object.SageObject,
 object]
sage: type(w.function()).mro()
[sage.functions.trig.Function_sin,
 sage.symbolic.function.GinacFunction,
 sage.symbolic.function.BuiltinFunction,
 sage.symbolic.function.Function,
 sage.structure.sage_object.SageObject,
 object]
```

So my guess is that you only need `isinstance(type(h), sage.symbolic.expression.Expression)`, no need to check for substrings. On the other hand, your `sage.structure.dynamic_class.DynamicMetaclass` seems to work too, even though that class doesn't show up in the mro!

I think we're running into a break-down of ducktyping here: the code as written previously assumed that if a `__name__` attribute is present, then it's meaningful. This is apparently not true for some dynamic classes and makes me think that maybe this `__name__` attribute shouldn't be provided (wherever that happens).



---

archive/issue_comments_017129.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2014-04-15T01:31:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2516",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2516#issuecomment-17129",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_017130.json:
```json
{
    "body": "Please rebase/merge.",
    "created_at": "2014-04-15T06:22:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2516",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2516#issuecomment-17130",
    "user": "rws"
}
```

Please rebase/merge.



---

archive/issue_comments_017131.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2014-04-15T15:22:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2516",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2516#issuecomment-17131",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_017132.json:
```json
{
    "body": "Rebased on 6.2.beta8. I also included the test for `Expression` in `fast_callable`.\n\nReplying to [comment:35 nbruin]:\n>  - You are installing an extra rule in `mqapply_to_sage`, which I assume is correct. This rule registered in the special_max_to_sage dictionary: Great! that's what you're supposed to do\n>  - However, for conversion back, there should be a corresponding entry in special_sage_to_max as well, and you're not adding that. You'd have to test, but from the rule in the other direction, I'd guess it should be something like:\n> {{{\n> sage.functions.hypergeometric.hypergeometric : lambda A, B, X : [[mqapply],[[max_hyper, max_array],lisp_length(A)-1,lisp_length(B)-1],A,B,X]\n> }}}\n> where\n> {{{\n> lisp_length=EclObject('length')\n> }}}\n> \n> If you don't put this rule in place, you'll find that things like \"limit\", \"integral\" and \"sum\" (which use `sr_to_max`) will probably not work correctly with hypergeometric function. (in fact, I'm not so sure maxima has much support for them anyway, but at least we should make sure that the functions can survive a round-trip)\nI'm afraid offhand I have no idea what this is about. Will try.\n----\nNew commits:",
    "created_at": "2014-04-16T15:00:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2516",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2516#issuecomment-17132",
    "user": "rws"
}
```

Rebased on 6.2.beta8. I also included the test for `Expression` in `fast_callable`.

Replying to [comment:35 nbruin]:
>  - You are installing an extra rule in `mqapply_to_sage`, which I assume is correct. This rule registered in the special_max_to_sage dictionary: Great! that's what you're supposed to do
>  - However, for conversion back, there should be a corresponding entry in special_sage_to_max as well, and you're not adding that. You'd have to test, but from the rule in the other direction, I'd guess it should be something like:
> {{{
> sage.functions.hypergeometric.hypergeometric : lambda A, B, X : [[mqapply],[[max_hyper, max_array],lisp_length(A)-1,lisp_length(B)-1],A,B,X]
> }}}
> where
> {{{
> lisp_length=EclObject('length')
> }}}
> 
> If you don't put this rule in place, you'll find that things like "limit", "integral" and "sum" (which use `sr_to_max`) will probably not work correctly with hypergeometric function. (in fact, I'm not so sure maxima has much support for them anyway, but at least we should make sure that the functions can survive a round-trip)
I'm afraid offhand I have no idea what this is about. Will try.
----
New commits:



---

archive/issue_comments_017133.json:
```json
{
    "body": "Replying to [comment:35 nbruin]:\n> {{{\n> sage.functions.hypergeometric.hypergeometric : lambda A, B, X : [[mqapply],[[max_hyper, max_array],lisp_length(A)-1,lisp_length(B)-1],A,B,X]\n> }}}\nIt's already included, as far as I can see.\n\nAre there any issues left?",
    "created_at": "2014-04-17T13:15:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2516",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2516#issuecomment-17133",
    "user": "rws"
}
```

Replying to [comment:35 nbruin]:
> {{{
> sage.functions.hypergeometric.hypergeometric : lambda A, B, X : [[mqapply],[[max_hyper, max_array],lisp_length(A)-1,lisp_length(B)-1],A,B,X]
> }}}
It's already included, as far as I can see.

Are there any issues left?



---

archive/issue_comments_017134.json:
```json
{
    "body": "Replying to [comment:50 rws]:\n> It's already included, as far as I can see.\nYep, I figured out later how to get your branch to compile, so I provided the change\n\n> Are there any issues left?\nIt should be safe to delete the line\n`self.__name__ = self.__repr__()`\nnow.\n\nI haven't looked into much of the details of this; I mainly checked to see that translation to/from maxima_lib was done properly (and I think it is now).",
    "created_at": "2014-04-17T15:34:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2516",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2516#issuecomment-17134",
    "user": "nbruin"
}
```

Replying to [comment:50 rws]:
> It's already included, as far as I can see.
Yep, I figured out later how to get your branch to compile, so I provided the change

> Are there any issues left?
It should be safe to delete the line
`self.__name__ = self.__repr__()`
now.

I haven't looked into much of the details of this; I mainly checked to see that translation to/from maxima_lib was done properly (and I think it is now).



---

archive/issue_comments_017135.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2014-04-18T17:08:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2516",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2516#issuecomment-17135",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_017136.json:
```json
{
    "body": "Replying to [comment:51 nbruin]:\n> It should be safe to delete the line\n> `self.__name__ = self.__repr__()`\n> now.\nThanks. I also noticed that only the check for `DynamicMetaclass` will make all resp. doctests pass.\n> I haven't looked into much of the details of this; I mainly checked to see that translation to/from maxima_lib was done properly (and I think it is now).\nPlease add your name as reviewer anyway. If you cannot give positive I will then ask in sage-devel.",
    "created_at": "2014-04-18T17:09:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2516",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2516#issuecomment-17136",
    "user": "rws"
}
```

Replying to [comment:51 nbruin]:
> It should be safe to delete the line
> `self.__name__ = self.__repr__()`
> now.
Thanks. I also noticed that only the check for `DynamicMetaclass` will make all resp. doctests pass.
> I haven't looked into much of the details of this; I mainly checked to see that translation to/from maxima_lib was done properly (and I think it is now).
Please add your name as reviewer anyway. If you cannot give positive I will then ask in sage-devel.



---

archive/issue_comments_017137.json:
```json
{
    "body": "I can't vouch for the mathematical correctness here, but the translation to/from maxima seems sound.",
    "created_at": "2014-04-24T18:25:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2516",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2516#issuecomment-17137",
    "user": "nbruin"
}
```

I can't vouch for the mathematical correctness here, but the translation to/from maxima seems sound.



---

archive/issue_comments_017138.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2014-05-10T06:27:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2516",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2516#issuecomment-17138",
    "user": "chapoton"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_017139.json:
```json
{
    "body": "Some of the new functions needs to be doctested",
    "created_at": "2014-05-10T06:27:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2516",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2516#issuecomment-17139",
    "user": "chapoton"
}
```

Some of the new functions needs to be doctested



---

archive/issue_comments_017140.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2014-05-10T08:50:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2516",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2516#issuecomment-17140",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_017141.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2014-05-10T08:51:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2516",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2516#issuecomment-17141",
    "user": "rws"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_017142.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2014-05-11T07:35:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2516",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2516#issuecomment-17142",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_017143.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2014-06-21T12:34:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2516",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2516#issuecomment-17143",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_017144.json:
```json
{
    "body": "Changing keywords from \"hypergeometric\" to \"hypergeometric, special\".",
    "created_at": "2014-06-21T12:35:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2516",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2516#issuecomment-17144",
    "user": "rws"
}
```

Changing keywords from "hypergeometric" to "hypergeometric, special".



---

archive/issue_comments_017145.json:
```json
{
    "body": "The lazy import in the last commit causes this:\n\n```\n[calculus ] loading cross citations...\n[calculus ] /home/ralf/sage/src/doc/en/reference/calculus/sage/calculus/calculus.rst:11: WARNING: error while formatting signature for sage.calculus.calculus.symbolic_expression_from_maxima_string: 'module' object has no attribute 'hypergeometric'\n[categorie] reading sources... [ 76%] sage/categories/modules_with_basis\nError building the documentation.\nTraceback (most recent call last):\n  File \"/home/ralf/sage/src/doc/common/builder.py\", line 1490, in <module>\n    getattr(get_builder(name), type)()\n  File \"/home/ralf/sage/src/doc/common/builder.py\", line 291, in _wrapper\n    getattr(get_builder(document), 'inventory')(*args, **kwds)\n  File \"/home/ralf/sage/src/doc/common/builder.py\", line 502, in _wrapper\n    x.get(99999)\n  File \"/home/ralf/sage/local/lib/python/multiprocessing/pool.py\", line 558, in get\n    raise self._value\nOSError: [calculus ] /home/ralf/sage/src/doc/en/reference/calculus/sage/calculus/calculus.rst:11: WARNING: error while formatting signature for sage.calculus.calculus.symbolic_expression_from_maxima_string: 'module' object has no attribute 'hypergeometric'\n```\n\nI have no idea why. There appears to be no circular import. It can also be triggered with\n\n```\nsage: from sage.calculus.calculus import symbolic_expression_from_maxima_string\nsage: symbolic_expression_from_maxima_string('hypergeometric')\n```\n\nbut that specific instance goes away when I import non-lazily at function level. Local import does not resolve the docbuild error.\n\nSo, back as global non-lazy import into `functions/all.py`?",
    "created_at": "2014-06-22T15:07:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2516",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2516#issuecomment-17145",
    "user": "rws"
}
```

The lazy import in the last commit causes this:

```
[calculus ] loading cross citations...
[calculus ] /home/ralf/sage/src/doc/en/reference/calculus/sage/calculus/calculus.rst:11: WARNING: error while formatting signature for sage.calculus.calculus.symbolic_expression_from_maxima_string: 'module' object has no attribute 'hypergeometric'
[categorie] reading sources... [ 76%] sage/categories/modules_with_basis
Error building the documentation.
Traceback (most recent call last):
  File "/home/ralf/sage/src/doc/common/builder.py", line 1490, in <module>
    getattr(get_builder(name), type)()
  File "/home/ralf/sage/src/doc/common/builder.py", line 291, in _wrapper
    getattr(get_builder(document), 'inventory')(*args, **kwds)
  File "/home/ralf/sage/src/doc/common/builder.py", line 502, in _wrapper
    x.get(99999)
  File "/home/ralf/sage/local/lib/python/multiprocessing/pool.py", line 558, in get
    raise self._value
OSError: [calculus ] /home/ralf/sage/src/doc/en/reference/calculus/sage/calculus/calculus.rst:11: WARNING: error while formatting signature for sage.calculus.calculus.symbolic_expression_from_maxima_string: 'module' object has no attribute 'hypergeometric'
```

I have no idea why. There appears to be no circular import. It can also be triggered with

```
sage: from sage.calculus.calculus import symbolic_expression_from_maxima_string
sage: symbolic_expression_from_maxima_string('hypergeometric')
```

but that specific instance goes away when I import non-lazily at function level. Local import does not resolve the docbuild error.

So, back as global non-lazy import into `functions/all.py`?



---

archive/issue_comments_017146.json:
```json
{
    "body": "Looks like there are circular imports in `maxima_lib`. But is it the cause?",
    "created_at": "2014-06-22T16:25:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2516",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2516#issuecomment-17146",
    "user": "rws"
}
```

Looks like there are circular imports in `maxima_lib`. But is it the cause?



---

archive/issue_comments_017147.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2014-06-23T16:16:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2516",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2516#issuecomment-17147",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_017148.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2014-06-23T16:18:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2516",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2516#issuecomment-17148",
    "user": "rws"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_017149.json:
```json
{
    "body": "Now that the lazy import no longer causes a docbuild error a doctest fail appears:\n\n```\nsage -t --long src/sage/functions/hypergeometric.py  # 1 doctest failed\n```\n",
    "created_at": "2014-06-23T16:18:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2516",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2516#issuecomment-17149",
    "user": "rws"
}
```

Now that the lazy import no longer causes a docbuild error a doctest fail appears:

```
sage -t --long src/sage/functions/hypergeometric.py  # 1 doctest failed
```




---

archive/issue_comments_017150.json:
```json
{
    "body": "I noticed this:\n\n```\n+lazy_import(\"sage.functions.hypergeometric\", \"hypergeometric\")\n...\n special_sage_to_max={\n+ hypergeometric : lambda A, B, X : [[mqapply],[[max_hyper, max_array],lisp_length(A.cdr()),lisp_length(B.cdr())],A,B,X]\n}\n```\n\nThis can't do what I think it is meant to do. Either the reference to \"hypergeometric\" as a dictionary key leads to resolving the lazy import (this is the most likely, because we'll need `hypergeometric.__hash__()` to set the dict entry), in which case there's no point in doing a lazy import, or some lazy proxy makes it into the dictionary as a key, which is then out of reach of the lazy import resolver to substitute with the real thing, leaving the proxy (and its slowdown) in place indefinitely.\n\nI suspect that just importing `hypergeometric` normally will lead to acceptable performance.",
    "created_at": "2014-06-23T23:10:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2516",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2516#issuecomment-17150",
    "user": "nbruin"
}
```

I noticed this:

```
+lazy_import("sage.functions.hypergeometric", "hypergeometric")
...
 special_sage_to_max={
+ hypergeometric : lambda A, B, X : [[mqapply],[[max_hyper, max_array],lisp_length(A.cdr()),lisp_length(B.cdr())],A,B,X]
}
```

This can't do what I think it is meant to do. Either the reference to "hypergeometric" as a dictionary key leads to resolving the lazy import (this is the most likely, because we'll need `hypergeometric.__hash__()` to set the dict entry), in which case there's no point in doing a lazy import, or some lazy proxy makes it into the dictionary as a key, which is then out of reach of the lazy import resolver to substitute with the real thing, leaving the proxy (and its slowdown) in place indefinitely.

I suspect that just importing `hypergeometric` normally will lead to acceptable performance.



---

archive/issue_comments_017151.json:
```json
{
    "body": "Reset to before lazy import. Reviewers will just have to ignore the `PluginFailed` from patchbot.\n\nI'll grab the occasion and announce that I will not run after every upgrade merge fail from now, but simply upload a patch that reviewers/other authors should apply at merge conflict. If that patch goes stale as well, too bad.",
    "created_at": "2014-06-24T08:54:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2516",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2516#issuecomment-17151",
    "user": "rws"
}
```

Reset to before lazy import. Reviewers will just have to ignore the `PluginFailed` from patchbot.

I'll grab the occasion and announce that I will not run after every upgrade merge fail from now, but simply upload a patch that reviewers/other authors should apply at merge conflict. If that patch goes stale as well, too bad.



---

archive/issue_comments_017152.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2014-06-24T08:54:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2516",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2516#issuecomment-17152",
    "user": "rws"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_017153.json:
```json
{
    "body": "Now that the lazy import experiment was abandoned, is there anything amiss?",
    "created_at": "2014-06-29T14:05:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2516",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2516#issuecomment-17153",
    "user": "rws"
}
```

Now that the lazy import experiment was abandoned, is there anything amiss?



---

archive/issue_comments_017154.json:
```json
{
    "body": "Looks good to me but merge conflict with #16007. Either merge that branch in or wait until the next beta.",
    "created_at": "2014-07-08T13:08:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2516",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2516#issuecomment-17154",
    "user": "vbraun"
}
```

Looks good to me but merge conflict with #16007. Either merge that branch in or wait until the next beta.



---

archive/issue_comments_017155.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. Last 10 new commits:",
    "created_at": "2014-07-08T14:35:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2516",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2516#issuecomment-17155",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. Last 10 new commits:



---

archive/issue_comments_017156.json:
```json
{
    "body": "Thanks to all other authors and reviewers.",
    "created_at": "2014-07-08T14:36:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2516",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2516#issuecomment-17156",
    "user": "rws"
}
```

Thanks to all other authors and reviewers.



---

archive/issue_comments_017157.json:
```json
{
    "body": "> Thanks to all other authors and reviewers.\nThanks for sticking with it to make this a reality!\n\nDoes this fix either of the two remaining examples at #9908 (see [comment:11:ticket:9908 here])?  No worries about putting them here, but if so then we can mark that as an easy-to-fix ticket.",
    "created_at": "2014-07-08T15:22:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2516",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2516#issuecomment-17157",
    "user": "kcrisman"
}
```

> Thanks to all other authors and reviewers.
Thanks for sticking with it to make this a reality!

Does this fix either of the two remaining examples at #9908 (see [comment:11:ticket:9908 here])?  No worries about putting them here, but if so then we can mark that as an easy-to-fix ticket.



---

archive/issue_comments_017158.json:
```json
{
    "body": "Replying to [comment:73 kcrisman]:\n> Does this fix either of the two remaining examples at #9908 (see [comment:11:ticket:9908 here])?  No worries about putting them here, but if so then we can mark that as an easy-to-fix ticket.\nAnswered there.",
    "created_at": "2014-07-08T15:56:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2516",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2516#issuecomment-17158",
    "user": "rws"
}
```

Replying to [comment:73 kcrisman]:
> Does this fix either of the two remaining examples at #9908 (see [comment:11:ticket:9908 here])?  No worries about putting them here, but if so then we can mark that as an easy-to-fix ticket.
Answered there.



---

archive/issue_comments_017159.json:
```json
{
    "body": "I understand Volker's final remark as 'conditionally positive', and now the condition is fulfilled.",
    "created_at": "2014-07-08T17:35:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2516",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2516#issuecomment-17159",
    "user": "rws"
}
```

I understand Volker's final remark as 'conditionally positive', and now the condition is fulfilled.



---

archive/issue_comments_017160.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2014-07-08T17:35:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2516",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2516#issuecomment-17160",
    "user": "rws"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_017161.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2014-07-08T18:51:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2516",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2516#issuecomment-17161",
    "user": "vbraun"
}
```

Resolution: fixed



---

archive/issue_comments_017162.json:
```json
{
    "body": "See #16752 for a followup with some code/doc tweaks.",
    "created_at": "2014-08-02T23:26:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2516",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2516#issuecomment-17162",
    "user": "tscrim"
}
```

See #16752 for a followup with some code/doc tweaks.



---

archive/issue_comments_017163.json:
```json
{
    "body": "Does anybody remember why this `inspect.ismethod` condition was added here to the deprecation from #5930? I mean, either something is deprecated or not. It shouldn't depend on some very subtle condition like the type of the `_fast_callable_` attribute.\n\n```python\n            import inspect\n            if not hasattr(_the_element,'_fast_callable_') or not inspect.ismethod(_the_element._fast_callable_):\n                # only warn if _the_element is not dynamic\n                from sage.misc.superseded import deprecation\n                deprecation(5930, \"Substitution using function-call syntax and unnamed arguments is deprecated and will be removed from a future release of Sage; you can use named arguments instead, like EXPR(x=..., y=...)\")\n```\n",
    "created_at": "2017-06-07T12:59:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2516",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2516#issuecomment-17163",
    "user": "jdemeyer"
}
```

Does anybody remember why this `inspect.ismethod` condition was added here to the deprecation from #5930? I mean, either something is deprecated or not. It shouldn't depend on some very subtle condition like the type of the `_fast_callable_` attribute.

```python
            import inspect
            if not hasattr(_the_element,'_fast_callable_') or not inspect.ismethod(_the_element._fast_callable_):
                # only warn if _the_element is not dynamic
                from sage.misc.superseded import deprecation
                deprecation(5930, "Substitution using function-call syntax and unnamed arguments is deprecated and will be removed from a future release of Sage; you can use named arguments instead, like EXPR(x=..., y=...)")
```




---

archive/issue_comments_017164.json:
```json
{
    "body": "Follow-up at #23159.",
    "created_at": "2017-06-07T13:27:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2516",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2516#issuecomment-17164",
    "user": "jdemeyer"
}
```

Follow-up at #23159.
