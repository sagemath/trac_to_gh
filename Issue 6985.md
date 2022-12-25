# Issue 6985: complex_plot needs to use fast_callable

archive/issues_006985.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @kcrisman\n\nTiming differences:\n\n\n```\n{{{\nsage: f(x) = x^2                   \nsage: %time P = complex_plot(f, (-10, 10), (-10, 10))\nCPU times: user 1.99 s, sys: 0.00 s, total: 2.00 s\nWall time: 2.02 s\nsage: g = fast_callable(f, domain=CC, vars='x')\nsage: %time Q = complex_plot(g, (-10, 10), (-10, 10))\nCPU times: user 0.54 s, sys: 0.01 s, total: 0.55 s\nWall time: 0.57 s\nsage: h = fast_callable(f, domain=CDF, vars='x')\nsage: %time R = complex_plot(h, (-10, 10), (-10, 10))\nCPU times: user 0.20 s, sys: 0.00 s, total: 0.20 s\nWall time: 0.21 s\n}}}\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6985\n\n",
    "created_at": "2009-09-22T14:32:34Z",
    "labels": [
        "component: graphics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.2",
    "title": "complex_plot needs to use fast_callable",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6985",
    "user": "https://github.com/jasongrout"
}
```
Assignee: @williamstein

CC:  @kcrisman

Timing differences:


```
{{{
sage: f(x) = x^2                   
sage: %time P = complex_plot(f, (-10, 10), (-10, 10))
CPU times: user 1.99 s, sys: 0.00 s, total: 2.00 s
Wall time: 2.02 s
sage: g = fast_callable(f, domain=CC, vars='x')
sage: %time Q = complex_plot(g, (-10, 10), (-10, 10))
CPU times: user 0.54 s, sys: 0.01 s, total: 0.55 s
Wall time: 0.57 s
sage: h = fast_callable(f, domain=CDF, vars='x')
sage: %time R = complex_plot(h, (-10, 10), (-10, 10))
CPU times: user 0.20 s, sys: 0.00 s, total: 0.20 s
Wall time: 0.21 s
}}}


Issue created by migration from https://trac.sagemath.org/ticket/6985





---

archive/issue_comments_057657.json:
```json
{
    "body": "Do this and/or #6947 address the issues with complex_plot not plotting some functions it should?  E.g. [http://groups.google.com/group/sage-support/browse_thread/thread/c2cfabe10550cffe](http://groups.google.com/group/sage-support/browse_thread/thread/c2cfabe10550cffe) or [http://groups.google.com/group/sage-devel/browse_thread/thread/a1a2b04747dbd0aa](http://groups.google.com/group/sage-devel/browse_thread/thread/a1a2b04747dbd0aa).",
    "created_at": "2009-09-22T16:55:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6985",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6985#issuecomment-57657",
    "user": "https://github.com/kcrisman"
}
```

Do this and/or #6947 address the issues with complex_plot not plotting some functions it should?  E.g. [http://groups.google.com/group/sage-support/browse_thread/thread/c2cfabe10550cffe](http://groups.google.com/group/sage-support/browse_thread/thread/c2cfabe10550cffe) or [http://groups.google.com/group/sage-devel/browse_thread/thread/a1a2b04747dbd0aa](http://groups.google.com/group/sage-devel/browse_thread/thread/a1a2b04747dbd0aa).



---

archive/issue_comments_057658.json:
```json
{
    "body": "Attachment [trac_6985.patch](tarball://root/attachments/some-uuid/ticket6985/trac_6985.patch) by @mwhansen created at 2009-09-24 06:41:19",
    "created_at": "2009-09-24T06:41:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6985",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6985#issuecomment-57658",
    "user": "https://github.com/mwhansen"
}
```

Attachment [trac_6985.patch](tarball://root/attachments/some-uuid/ticket6985/trac_6985.patch) by @mwhansen created at 2009-09-24 06:41:19



---

archive/issue_comments_057659.json:
```json
{
    "body": "Changing assignee from @williamstein to @mwhansen.",
    "created_at": "2009-09-24T06:44:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6985",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6985#issuecomment-57659",
    "user": "https://github.com/mwhansen"
}
```

Changing assignee from @williamstein to @mwhansen.



---

archive/issue_comments_057660.json:
```json
{
    "body": "It fixes those issues, but not directly.\n\nIn setup_for_eval_on_grid, we should check for not just types.FunctionType, but instead for (types.FunctionType, types.LambdaType, types.BuiltinFunctionType, types.BuiltinMethodType).  Also, everything should be converted from fast_float to fast_callable.  This would be a separate ticket.",
    "created_at": "2009-09-24T06:44:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6985",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6985#issuecomment-57660",
    "user": "https://github.com/mwhansen"
}
```

It fixes those issues, but not directly.

In setup_for_eval_on_grid, we should check for not just types.FunctionType, but instead for (types.FunctionType, types.LambdaType, types.BuiltinFunctionType, types.BuiltinMethodType).  Also, everything should be converted from fast_float to fast_callable.  This would be a separate ticket.



---

archive/issue_comments_057661.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-09-24T06:44:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6985",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6985#issuecomment-57661",
    "user": "https://github.com/mwhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_057662.json:
```json
{
    "body": "Replying to [comment:3 mhansen]:\n> It fixes those issues, but not directly.\n> \n> In setup_for_eval_on_grid, we should check for not just types.FunctionType, but instead for (types.FunctionType, types.LambdaType, types.BuiltinFunctionType, types.BuiltinMethodType).  Also, everything should be converted from fast_float to fast_callable.  This would be a separate ticket.\n\nCan you make another ticket for this?",
    "created_at": "2009-09-24T06:59:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6985",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6985#issuecomment-57662",
    "user": "https://github.com/jasongrout"
}
```

Replying to [comment:3 mhansen]:
> It fixes those issues, but not directly.
> 
> In setup_for_eval_on_grid, we should check for not just types.FunctionType, but instead for (types.FunctionType, types.LambdaType, types.BuiltinFunctionType, types.BuiltinMethodType).  Also, everything should be converted from fast_float to fast_callable.  This would be a separate ticket.

Can you make another ticket for this?



---

archive/issue_comments_057663.json:
```json
{
    "body": "There seems to be a regression: `%time complex_plot(exp(x)-sin(x), (-10, 10), (-10, 10))` takes 21 seconds before the patch, but 28 seconds after the patch for me.\n\nNote:\n\n\n```\nsage: f(x)=exp(x)-sin(x)\nsage: fcomplex=fast_callable(f, domain=complex, expect_one_var=True)sage: fCDF=fast_callable(f, domain=CDF, expect_one_var=True)\nsage: %timeit f(4j)\n100 loops, best of 3: 2.21 ms per loop\nsage: %timeit fcomplex(4j)\n100 loops, best of 3: 2.7 ms per loop\nsage: %timeit fCDF(4j)\n100000 loops, best of 3: 7.94 \u00b5s per loop\n```\n\n\nSo maybe the fast_callable in the patch should use domain CDF!\n\n(this seems really odd to me, but I can't argue with the timings above!)",
    "created_at": "2009-09-24T07:13:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6985",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6985#issuecomment-57663",
    "user": "https://github.com/jasongrout"
}
```

There seems to be a regression: `%time complex_plot(exp(x)-sin(x), (-10, 10), (-10, 10))` takes 21 seconds before the patch, but 28 seconds after the patch for me.

Note:


```
sage: f(x)=exp(x)-sin(x)
sage: fcomplex=fast_callable(f, domain=complex, expect_one_var=True)sage: fCDF=fast_callable(f, domain=CDF, expect_one_var=True)
sage: %timeit f(4j)
100 loops, best of 3: 2.21 ms per loop
sage: %timeit fcomplex(4j)
100 loops, best of 3: 2.7 ms per loop
sage: %timeit fCDF(4j)
100000 loops, best of 3: 7.94 µs per loop
```


So maybe the fast_callable in the patch should use domain CDF!

(this seems really odd to me, but I can't argue with the timings above!)



---

archive/issue_comments_057664.json:
```json
{
    "body": "In fact, we see the same sort of speedup just with exp(x):\n\n\n```\nsage: f(x)=exp(x)\nsage: fcomplex=fast_callable(f, domain=complex, expect_one_var=True)\nsage: fCDF=fast_callable(f, domain=CDF, expect_one_var=True)\nsage: %timeit f(4j)\n100 loops, best of 3: 2.12 ms per loop\nsage: %timeit fcomplex(4j)\n100 loops, best of 3: 2.39 ms per loop\nsage: %timeit fCDF(4j)\n100000 loops, best of 3: 7.32 \u00b5s per loop\n```\n",
    "created_at": "2009-09-24T07:15:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6985",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6985#issuecomment-57664",
    "user": "https://github.com/jasongrout"
}
```

In fact, we see the same sort of speedup just with exp(x):


```
sage: f(x)=exp(x)
sage: fcomplex=fast_callable(f, domain=complex, expect_one_var=True)
sage: fCDF=fast_callable(f, domain=CDF, expect_one_var=True)
sage: %timeit f(4j)
100 loops, best of 3: 2.12 ms per loop
sage: %timeit fcomplex(4j)
100 loops, best of 3: 2.39 ms per loop
sage: %timeit fCDF(4j)
100000 loops, best of 3: 7.32 µs per loop
```




---

archive/issue_comments_057665.json:
```json
{
    "body": "The fast_callable documentation mentions a special interpreter for float, which is the same as for RDF, and also a special interpreter for CDF.  It never mentions complex.  So maybe that's a bug/feature request for fast_callable...",
    "created_at": "2009-09-24T07:17:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6985",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6985#issuecomment-57665",
    "user": "https://github.com/jasongrout"
}
```

The fast_callable documentation mentions a special interpreter for float, which is the same as for RDF, and also a special interpreter for CDF.  It never mentions complex.  So maybe that's a bug/feature request for fast_callable...



---

archive/issue_comments_057666.json:
```json
{
    "body": "My simple patch to make the domain CDF should also maybe be reviewed.  All of the plots are even faster now than with domain=complex.",
    "created_at": "2009-09-24T07:24:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6985",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6985#issuecomment-57666",
    "user": "https://github.com/jasongrout"
}
```

My simple patch to make the domain CDF should also maybe be reviewed.  All of the plots are even faster now than with domain=complex.



---

archive/issue_comments_057667.json:
```json
{
    "body": "For the tour:\n\nBEFORE PATCH:\n\n\n```\nsage: %time complex_plot(exp(x)-sin(x), (-20, 20), (-20, 20))\n/home/jason/.sage/temp/littleone/4745/_home_jason__sage_init_sage_0.py:1: DeprecationWarning: Substitution using function-call syntax and unnamed arguments is deprecated and will be removed from a future release of Sage; you can use named arguments instead, like EXPR(x=..., y=...)\n  # -*- coding: utf-8 -*-\nCPU times: user 20.51 s, sys: 0.40 s, total: 20.91 s\nWall time: 21.09 s\n```\n\n\n\nAFTER PATCH:\n\n\n```\nsage: %time complex_plot(exp(x)-sin(x), (-20, 20), (-20, 20))\nCPU times: user 0.03 s, sys: 0.01 s, total: 0.04 s\nWall time: 0.05 s\n```\n",
    "created_at": "2009-09-24T07:26:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6985",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6985#issuecomment-57667",
    "user": "https://github.com/jasongrout"
}
```

For the tour:

BEFORE PATCH:


```
sage: %time complex_plot(exp(x)-sin(x), (-20, 20), (-20, 20))
/home/jason/.sage/temp/littleone/4745/_home_jason__sage_init_sage_0.py:1: DeprecationWarning: Substitution using function-call syntax and unnamed arguments is deprecated and will be removed from a future release of Sage; you can use named arguments instead, like EXPR(x=..., y=...)
  # -*- coding: utf-8 -*-
CPU times: user 20.51 s, sys: 0.40 s, total: 20.91 s
Wall time: 21.09 s
```



AFTER PATCH:


```
sage: %time complex_plot(exp(x)-sin(x), (-20, 20), (-20, 20))
CPU times: user 0.03 s, sys: 0.01 s, total: 0.04 s
Wall time: 0.05 s
```




---

archive/issue_comments_057668.json:
```json
{
    "body": "(oh, and positive review to mhansen's patch.  My patch should still be reviewed.)",
    "created_at": "2009-09-24T07:28:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6985",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6985#issuecomment-57668",
    "user": "https://github.com/jasongrout"
}
```

(oh, and positive review to mhansen's patch.  My patch should still be reviewed.)



---

archive/issue_comments_057669.json:
```json
{
    "body": "These don't apply for me properly - I don't have the stuff after the Riemann Zeta function and options, but before the actual code, e.g.\n\n```\nsage: P = complex_plot(f, (-10, 10), (-10, 10)) \nsage: Q = complex_plot(g, (-10, 10), (-10, 10)) \nsage: R = complex_plot(h, (-10, 10), (-10, 10)) \n```\n\nIs that in some other patch, or was it removed before 4.1.2.alpha2?",
    "created_at": "2009-09-24T13:16:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6985",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6985#issuecomment-57669",
    "user": "https://github.com/kcrisman"
}
```

These don't apply for me properly - I don't have the stuff after the Riemann Zeta function and options, but before the actual code, e.g.

```
sage: P = complex_plot(f, (-10, 10), (-10, 10)) 
sage: Q = complex_plot(g, (-10, 10), (-10, 10)) 
sage: R = complex_plot(h, (-10, 10), (-10, 10)) 
```

Is that in some other patch, or was it removed before 4.1.2.alpha2?



---

archive/issue_comments_057670.json:
```json
{
    "body": "Oh, and I think there should still be at least one example of the type\n\n```\nsage: complex_plot(sqrt, (-5, 5), (-5, 5))\n```\n\nto show that it is still possible.",
    "created_at": "2009-09-24T13:17:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6985",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6985#issuecomment-57670",
    "user": "https://github.com/kcrisman"
}
```

Oh, and I think there should still be at least one example of the type

```
sage: complex_plot(sqrt, (-5, 5), (-5, 5))
```

to show that it is still possible.



---

archive/issue_comments_057671.json:
```json
{
    "body": "Oh, this patch depends on #6947.",
    "created_at": "2009-09-24T18:48:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6985",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6985#issuecomment-57671",
    "user": "https://github.com/jasongrout"
}
```

Oh, this patch depends on #6947.



---

archive/issue_comments_057672.json:
```json
{
    "body": "Some work needs to be done on fast_callable to make it be able to replace fast_float: see #5572.",
    "created_at": "2009-09-24T19:37:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6985",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6985#issuecomment-57672",
    "user": "https://github.com/jasongrout"
}
```

Some work needs to be done on fast_callable to make it be able to replace fast_float: see #5572.



---

archive/issue_comments_057673.json:
```json
{
    "body": "Does this mean this patch is not ready for review?  \n\nI was going to try to review it (after applying #6947) later on... unfortunately, my main computer is on the fritz so it's back to 1 GB of memory and recompiling 4.1.2.alpha2 from scratch.",
    "created_at": "2009-09-24T19:41:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6985",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6985#issuecomment-57673",
    "user": "https://github.com/kcrisman"
}
```

Does this mean this patch is not ready for review?  

I was going to try to review it (after applying #6947) later on... unfortunately, my main computer is on the fritz so it's back to 1 GB of memory and recompiling 4.1.2.alpha2 from scratch.



---

archive/issue_comments_057674.json:
```json
{
    "body": "Nope, this patch is ready to go in (maybe after you add a patch with the doctest you like :).",
    "created_at": "2009-09-24T19:47:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6985",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6985#issuecomment-57674",
    "user": "https://github.com/jasongrout"
}
```

Nope, this patch is ready to go in (maybe after you add a patch with the doctest you like :).



---

archive/issue_comments_057675.json:
```json
{
    "body": "Attachment [trac-6985-CDF-domain.patch](tarball://root/attachments/some-uuid/ticket6985/trac-6985-CDF-domain.patch) by @jasongrout created at 2009-09-25 06:06:28\n\napply on top of previous patch",
    "created_at": "2009-09-25T06:06:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6985",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6985#issuecomment-57675",
    "user": "https://github.com/jasongrout"
}
```

Attachment [trac-6985-CDF-domain.patch](tarball://root/attachments/some-uuid/ticket6985/trac-6985-CDF-domain.patch) by @jasongrout created at 2009-09-25 06:06:28

apply on top of previous patch



---

archive/issue_comments_057676.json:
```json
{
    "body": "I just updated the patch to have your example there too.",
    "created_at": "2009-09-25T06:07:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6985",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6985#issuecomment-57676",
    "user": "https://github.com/jasongrout"
}
```

I just updated the patch to have your example there too.



---

archive/issue_comments_057677.json:
```json
{
    "body": "Apply on top of first patch, instead of other CDF patch",
    "created_at": "2009-09-25T13:31:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6985",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6985#issuecomment-57677",
    "user": "https://github.com/kcrisman"
}
```

Apply on top of first patch, instead of other CDF patch



---

archive/issue_comments_057678.json:
```json
{
    "body": "Attachment [trac_6985-CDF_and_reviewer.patch](tarball://root/attachments/some-uuid/ticket6985/trac_6985-CDF_and_reviewer.patch) by @kcrisman created at 2009-09-25 13:32:32\n\nOkay, positive review.  I put the example I wanted under tests instead, because it's really noticeably slower.",
    "created_at": "2009-09-25T13:32:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6985",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6985#issuecomment-57678",
    "user": "https://github.com/kcrisman"
}
```

Attachment [trac_6985-CDF_and_reviewer.patch](tarball://root/attachments/some-uuid/ticket6985/trac_6985-CDF_and_reviewer.patch) by @kcrisman created at 2009-09-25 13:32:32

Okay, positive review.  I put the example I wanted under tests instead, because it's really noticeably slower.



---

archive/issue_comments_057679.json:
```json
{
    "body": "Of course, this will unfortunately necessitate a one-line change in the patch for #7008 so it applies properly.",
    "created_at": "2009-09-25T13:34:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6985",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6985#issuecomment-57679",
    "user": "https://github.com/kcrisman"
}
```

Of course, this will unfortunately necessitate a one-line change in the patch for #7008 so it applies properly.



---

archive/issue_comments_057680.json:
```json
{
    "body": "Merged patches in this order:\n\n1. `trac_6985.patch`\n2. `trac_6985-CDF_and_reviewer.patch`",
    "created_at": "2009-09-25T15:06:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6985",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6985#issuecomment-57680",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Merged patches in this order:

1. `trac_6985.patch`
2. `trac_6985-CDF_and_reviewer.patch`



---

archive/issue_comments_057681.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-09-25T15:06:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6985",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6985#issuecomment-57681",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed



---

archive/issue_events_016404.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2009-09-25T15:06:41Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6985",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6985#event-16404"
}
```



---

archive/issue_comments_057682.json:
```json
{
    "body": "There is no 4.1.2.alpha3. Sage 4.1.2.alpha3 was William Stein's release for working on making the notebook a standalone package.",
    "created_at": "2009-09-27T10:36:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6985",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6985#issuecomment-57682",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

There is no 4.1.2.alpha3. Sage 4.1.2.alpha3 was William Stein's release for working on making the notebook a standalone package.
