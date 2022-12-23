# Issue 2516: generalized hypergeometric functions should be implemented

Issue created by migration from https://trac.sagemath.org/ticket/2516

Original creator: ddrake

Original creation time: 2008-03-14 09:55:34

Assignee: cwitty

CC:  burcin fstan kcrisman ktkohl benjaminfjones dsm eviatarbach mmezzarobba

Sage should have support for [generalized hypergeometric functions](http://mathworld.wolfram.com/GeneralizedHypergeometricFunction.html). They are an important class of special functions. They show up everywhere from differential equations to binomial coefficient identities.


---

Attachment

tentative implementation of generalized hypergeometric functions


---

Comment by fredrik.johansson created at 2010-07-26 03:35:32

Changing status from new to needs_work.


---

Comment by fredrik.johansson created at 2010-07-26 03:35:32

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

Comment by kcrisman created at 2011-02-17 01:52:45

See also #9908, which is at least related (we need to translate Maxima hg functions).

Also, I think that we already have a lot of Bessel functions implemented, though they are not yet symbolic.


---

Comment by kcrisman created at 2012-05-26 19:14:15

Changing component.  But this is a really nice start, hopefully can be combined with some of the currently existing bessel stuff etc.


---

Comment by kcrisman created at 2012-05-26 19:14:15

Changing component from misc to symbolics.


---

Comment by dsm created at 2012-05-26 19:59:52

Okay, I'm going to see what can be done to get this merged.


---

Comment by dsm created at 2012-05-26 22:55:04

Having played around with this some, I think it'll be pretty straightforward to get in.. *after* we have Burcin's ticket allowing numerical_approx to take more general kwargs.  If it weren't for the need to maintain backward compatibility with the algorithm kwarg for the old bessel functions, life would be easier.

I have a half-functional wrapper which monkeypatches things to sort of get them to work, but once that patch gets in it becomes much simpler.  So I think this should stay in a holding pattern until we get that one in.


---

Comment by kcrisman created at 2013-04-25 02:21:24

> If it weren't for the need to maintain backward compatibility with the algorithm kwarg for the old bessel functions, life would be easier.
Since #4102 is nearly finished, and has at least sort of dealt with this issue, perhaps one can just ignore that part of the Bessel issue.  Instead, one could just add the `_expand_hyper` methods to the stuff there.  I do like the idea here and it would be a shame for it to bit rot further...


---

Comment by eviatarbach created at 2013-07-05 11:19:42

Here is an initial version of an updated patch. It needs some work because it's failing a few tests, but I just wanted to post for comments.


---

Attachment


---

Comment by eviatarbach created at 2013-07-05 20:07:08

Two of the failing doctests are caused by #14858.


---

Comment by eviatarbach created at 2013-07-14 02:48:01

Changing status from needs_work to needs_info.


---

Comment by eviatarbach created at 2013-07-14 02:48:01

Plotting is now working fine (with the approach from #14801, thanks Volker!), except for getting deprecation warnings about using unnamed function parameters, which I have not been able to debug. Does anyone know how to fix this?

Another strange doctest failure is the one in `_fast_callable_`; when I run it from interactive mode I get `{CommutativeRings.element_class}(v_0)`, but the doctest returns `{Fields.element_class}(v_0)`. Why is that?

Other than that the patch should be ready for review.


---

Attachment


---

Comment by eviatarbach created at 2013-07-15 03:07:20

New patch fixes a circular import issue which caused a problem with numerical evaluation; see #13028.


---

Attachment


---

Comment by chapoton created at 2014-03-06 17:09:33

Changing keywords from "" to "hypergeometric".


---

Comment by rws created at 2014-04-10 12:54:00

Rebased on 6.2.beta7. The branch includes the (already merged) #14802. I fixed some but not all doctests.
----
New commits:


---

Comment by rws created at 2014-04-10 12:54:00

Changing status from needs_info to needs_review.


---

Comment by rws created at 2014-04-10 12:54:52

Changing status from needs_review to needs_work.


---

Comment by rws created at 2014-04-11 08:55:02

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

Comment by eviatarbach created at 2014-04-11 09:02:23

Thanks for working on this!

I believe you set the incorrect authors though.


---

Comment by eviatarbach created at 2014-04-11 09:08:02

I got the plotting problem before too, see comment 17. It's something in the `fast_callable` implementation if I recall correctly, but I couldn't figure out how to fix it at the time.


---

Comment by rws created at 2014-04-11 09:38:43

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

Comment by rws created at 2014-04-11 14:57:23

Forget all what I wrote. The deprecation warning is only printed once per session, which makes my conclusions arbitrary.


---

Comment by rws created at 2014-04-12 09:15:28

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

Comment by git created at 2014-04-12 15:38:47

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by rws created at 2014-04-12 15:41:28

This fixes all except the one in `_fast_callable_` and two others I haven't looked closely at. Specifically, I resolved the deprecation warning by excluding dynamic classes from this warning.


---

Comment by git created at 2014-04-13 14:41:20

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by rws created at 2014-04-13 14:45:16

Fixed all doctests. Please review. I had to exclude the hypergeometric function from random symbolic tests as that code blindly applies real numbers as parameters, and I didn't want to add `try: ... except ValueError: pass` there.


---

Comment by rws created at 2014-04-13 14:45:16

Changing status from needs_work to needs_review.


---

Comment by nbruin created at 2014-04-13 19:57:15

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

Comment by nbruin created at 2014-04-14 02:10:37

I found this suspicious (it's in the implementation of the `_fast_callable_` method

```
+ self.__name__ = self.__repr__() # was clobbered by category mechanics
+ return etb.call(self, *map(etb.var, etb._vars))
```

One shouldn't touch the `__name__` attribute, and certainly not during arbitrary executing code! Is it clear what code depends on the `__name__` being identical to `__repr__`? Can we solve this issue (cheaply) during `__init__`, or perhaps avoid the clobbering altogether?


---

Comment by rws created at 2014-04-14 03:39:06

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

Comment by nbruin created at 2014-04-14 05:34:22

Replying to [comment:37 rws]:
> Replying to [comment:36 nbruin]:
> > One shouldn't touch the `__name__` attribute, and certainly not during arbitrary executing code!
> Do you have a reference for that?

Well, you can look it up. Python uses `__name__` for any "named" object (e.g., defined by a `def` or a `class` or modules). These things aren't supposed to change (they are used for introspection). The fact that it does (and that that matters!) points to either a flaw in the category system or in the way it is used here.

> It is a consequence of `hypergeometric` being a SE with tuples as parameter. In the`Expression` constructor the class gets changed using `dynamic_class()` and this appears to be responsible.

> Overall, all long tests pass and I see no reason to hold this old ticket any longer.

The issues around `sr_to_max` should be fixed (and that's straightforward).


---

Comment by nbruin created at 2014-04-14 06:34:41

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

Comment by nbruin created at 2014-04-14 06:49:03

This should at least solve the maxima_lib translation problems.


---

Comment by rws created at 2014-04-14 08:35:22

Replying to [comment:40 nbruin]:
> A better solution would be to adapt the routine `ext.fast_callable.function_name` (or the way it gets used). It's clear you're now feeding it things it wasn't designed for.
Yes but how to distinguish such a 'dynamical' expression from `Expression`? The type displayed (`sage.functions.hypergeometric.Expression_with_dynamic_methods`) cannot be tested for directly. To do it right it should not be hypergeometric-specific either.
----
New commits:


---

Comment by rws created at 2014-04-14 08:45:33

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

Comment by nbruin created at 2014-04-14 15:29:10

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

Comment by git created at 2014-04-15 01:31:25

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by rws created at 2014-04-15 06:22:29

Please rebase/merge.


---

Comment by git created at 2014-04-15 15:22:52

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by rws created at 2014-04-16 15:00:34

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

Comment by rws created at 2014-04-17 13:15:38

Replying to [comment:35 nbruin]:
> {{{
> sage.functions.hypergeometric.hypergeometric : lambda A, B, X : [[mqapply],[[max_hyper, max_array],lisp_length(A)-1,lisp_length(B)-1],A,B,X]
> }}}
It's already included, as far as I can see.

Are there any issues left?


---

Comment by nbruin created at 2014-04-17 15:34:00

Replying to [comment:50 rws]:
> It's already included, as far as I can see.
Yep, I figured out later how to get your branch to compile, so I provided the change

> Are there any issues left?
It should be safe to delete the line
`self.__name__ = self.__repr__()`
now.

I haven't looked into much of the details of this; I mainly checked to see that translation to/from maxima_lib was done properly (and I think it is now).


---

Comment by git created at 2014-04-18 17:08:46

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by rws created at 2014-04-18 17:09:42

Replying to [comment:51 nbruin]:
> It should be safe to delete the line
> `self.__name__ = self.__repr__()`
> now.
Thanks. I also noticed that only the check for `DynamicMetaclass` will make all resp. doctests pass.
> I haven't looked into much of the details of this; I mainly checked to see that translation to/from maxima_lib was done properly (and I think it is now).
Please add your name as reviewer anyway. If you cannot give positive I will then ask in sage-devel.


---

Comment by nbruin created at 2014-04-24 18:25:40

I can't vouch for the mathematical correctness here, but the translation to/from maxima seems sound.


---

Comment by chapoton created at 2014-05-10 06:27:02

Changing status from needs_review to needs_work.


---

Comment by chapoton created at 2014-05-10 06:27:02

Some of the new functions needs to be doctested


---

Comment by git created at 2014-05-10 08:50:22

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by rws created at 2014-05-10 08:51:08

Changing status from needs_work to needs_review.


---

Comment by git created at 2014-05-11 07:35:02

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2014-06-21 12:34:28

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by rws created at 2014-06-21 12:35:55

Changing keywords from "hypergeometric" to "hypergeometric, special".


---

Comment by rws created at 2014-06-22 15:07:33

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

Comment by rws created at 2014-06-22 16:25:28

Looks like there are circular imports in `maxima_lib`. But is it the cause?


---

Comment by git created at 2014-06-23 16:16:07

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by rws created at 2014-06-23 16:18:20

Changing status from needs_review to needs_work.


---

Comment by rws created at 2014-06-23 16:18:20

Now that the lazy import no longer causes a docbuild error a doctest fail appears:

```
sage -t --long src/sage/functions/hypergeometric.py  # 1 doctest failed
```



---

Comment by nbruin created at 2014-06-23 23:10:59

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

Comment by rws created at 2014-06-24 08:54:56

Reset to before lazy import. Reviewers will just have to ignore the `PluginFailed` from patchbot.

I'll grab the occasion and announce that I will not run after every upgrade merge fail from now, but simply upload a patch that reviewers/other authors should apply at merge conflict. If that patch goes stale as well, too bad.


---

Comment by rws created at 2014-06-24 08:54:56

Changing status from needs_work to needs_review.


---

Comment by rws created at 2014-06-29 14:05:02

Now that the lazy import experiment was abandoned, is there anything amiss?


---

Comment by vbraun created at 2014-07-08 13:08:32

Looks good to me but merge conflict with #16007. Either merge that branch in or wait until the next beta.


---

Comment by git created at 2014-07-08 14:35:25

Branch pushed to git repo; I updated commit sha1. Last 10 new commits:


---

Comment by rws created at 2014-07-08 14:36:42

Thanks to all other authors and reviewers.


---

Comment by kcrisman created at 2014-07-08 15:22:42

> Thanks to all other authors and reviewers.
Thanks for sticking with it to make this a reality!

Does this fix either of the two remaining examples at #9908 (see [comment:11:ticket:9908 here])?  No worries about putting them here, but if so then we can mark that as an easy-to-fix ticket.


---

Comment by rws created at 2014-07-08 15:56:04

Replying to [comment:73 kcrisman]:
> Does this fix either of the two remaining examples at #9908 (see [comment:11:ticket:9908 here])?  No worries about putting them here, but if so then we can mark that as an easy-to-fix ticket.
Answered there.


---

Comment by rws created at 2014-07-08 17:35:50

I understand Volker's final remark as 'conditionally positive', and now the condition is fulfilled.


---

Comment by rws created at 2014-07-08 17:35:50

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2014-07-08 18:51:55

Resolution: fixed


---

Comment by tscrim created at 2014-08-02 23:26:33

See #16752 for a followup with some code/doc tweaks.


---

Comment by jdemeyer created at 2017-06-07 12:59:31

Does anybody remember why this `inspect.ismethod` condition was added here to the deprecation from #5930? I mean, either something is deprecated or not. It shouldn't depend on some very subtle condition like the type of the `_fast_callable_` attribute.

```python
            import inspect
            if not hasattr(_the_element,'_fast_callable_') or not inspect.ismethod(_the_element._fast_callable_):
                # only warn if _the_element is not dynamic
                from sage.misc.superseded import deprecation
                deprecation(5930, "Substitution using function-call syntax and unnamed arguments is deprecated and will be removed from a future release of Sage; you can use named arguments instead, like EXPR(x=..., y=...)")
```



---

Comment by jdemeyer created at 2017-06-07 13:27:45

Follow-up at #23159.
