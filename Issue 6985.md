# Issue 6985: complex_plot needs to use fast_callable

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2009-09-22 14:32:34

Assignee: was

CC:  kcrisman

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



---

Comment by kcrisman created at 2009-09-22 16:55:31

Do this and/or #6947 address the issues with complex_plot not plotting some functions it should?  E.g. [http://groups.google.com/group/sage-support/browse_thread/thread/c2cfabe10550cffe](http://groups.google.com/group/sage-support/browse_thread/thread/c2cfabe10550cffe) or [http://groups.google.com/group/sage-devel/browse_thread/thread/a1a2b04747dbd0aa](http://groups.google.com/group/sage-devel/browse_thread/thread/a1a2b04747dbd0aa).


---

Attachment


---

Comment by mhansen created at 2009-09-24 06:44:38

Changing assignee from was to mhansen.


---

Comment by mhansen created at 2009-09-24 06:44:38

It fixes those issues, but not directly.

In setup_for_eval_on_grid, we should check for not just types.FunctionType, but instead for (types.FunctionType, types.LambdaType, types.BuiltinFunctionType, types.BuiltinMethodType).  Also, everything should be converted from fast_float to fast_callable.  This would be a separate ticket.


---

Comment by mhansen created at 2009-09-24 06:44:38

Changing status from new to assigned.


---

Comment by jason created at 2009-09-24 06:59:34

Replying to [comment:3 mhansen]:
> It fixes those issues, but not directly.
> 
> In setup_for_eval_on_grid, we should check for not just types.FunctionType, but instead for (types.FunctionType, types.LambdaType, types.BuiltinFunctionType, types.BuiltinMethodType).  Also, everything should be converted from fast_float to fast_callable.  This would be a separate ticket.

Can you make another ticket for this?


---

Comment by jason created at 2009-09-24 07:13:47

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

Comment by jason created at 2009-09-24 07:15:19

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

Comment by jason created at 2009-09-24 07:17:04

The fast_callable documentation mentions a special interpreter for float, which is the same as for RDF, and also a special interpreter for CDF.  It never mentions complex.  So maybe that's a bug/feature request for fast_callable...


---

Comment by jason created at 2009-09-24 07:24:46

My simple patch to make the domain CDF should also maybe be reviewed.  All of the plots are even faster now than with domain=complex.


---

Comment by jason created at 2009-09-24 07:26:59

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

Comment by jason created at 2009-09-24 07:28:14

(oh, and positive review to mhansen's patch.  My patch should still be reviewed.)


---

Comment by kcrisman created at 2009-09-24 13:16:31

These don't apply for me properly - I don't have the stuff after the Riemann Zeta function and options, but before the actual code, e.g.

```
sage: P = complex_plot(f, (-10, 10), (-10, 10)) 
sage: Q = complex_plot(g, (-10, 10), (-10, 10)) 
sage: R = complex_plot(h, (-10, 10), (-10, 10)) 
```

Is that in some other patch, or was it removed before 4.1.2.alpha2?


---

Comment by kcrisman created at 2009-09-24 13:17:43

Oh, and I think there should still be at least one example of the type

```
sage: complex_plot(sqrt, (-5, 5), (-5, 5))
```

to show that it is still possible.


---

Comment by jason created at 2009-09-24 18:48:57

Oh, this patch depends on #6947.


---

Comment by jason created at 2009-09-24 19:37:27

Some work needs to be done on fast_callable to make it be able to replace fast_float: see #5572.


---

Comment by kcrisman created at 2009-09-24 19:41:19

Does this mean this patch is not ready for review?  

I was going to try to review it (after applying #6947) later on... unfortunately, my main computer is on the fritz so it's back to 1 GB of memory and recompiling 4.1.2.alpha2 from scratch.


---

Comment by jason created at 2009-09-24 19:47:03

Nope, this patch is ready to go in (maybe after you add a patch with the doctest you like :).


---

Attachment

apply on top of previous patch


---

Comment by jason created at 2009-09-25 06:07:46

I just updated the patch to have your example there too.


---

Comment by kcrisman created at 2009-09-25 13:31:17

Apply on top of first patch, instead of other CDF patch


---

Attachment

Okay, positive review.  I put the example I wanted under tests instead, because it's really noticeably slower.


---

Comment by kcrisman created at 2009-09-25 13:34:30

Of course, this will unfortunately necessitate a one-line change in the patch for #7008 so it applies properly.


---

Comment by mvngu created at 2009-09-25 15:06:41

Merged patches in this order:

 1. `trac_6985.patch`
 1. `trac_6985-CDF_and_reviewer.patch`


---

Comment by mvngu created at 2009-09-25 15:06:41

Resolution: fixed


---

Comment by mvngu created at 2009-09-27 10:36:09

There is no 4.1.2.alpha3. Sage 4.1.2.alpha3 was William Stein's release for working on making the notebook a standalone package.
