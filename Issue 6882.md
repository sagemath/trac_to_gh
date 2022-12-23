# Issue 6882: bug in conversion of "i" from Maxima to Sage

Issue created by migration from https://trac.sagemath.org/ticket/6882

Original creator: was

Original creation time: 2009-09-03 22:58:43

Assignee: burcin

CC:  robert.marik


```
-----------
sage: from sage.calculus.calculus import symbolic_expression_from_maxima_string
sage: symbolic_expression_from_maxima_string('%i')
I
sage: symbolic_expression_from_maxima_string('i')
I
-----------

So as you see, we are converting both '%i' and 'i' to  imaginary 'I' !!!!
```


See the sage-devel thread about this on Sept 3 for some discussion and motivation.


---

Comment by kcrisman created at 2009-10-23 23:57:48

Here is the relevant [discussion](http://groups.google.com/group/sage-devel/browse_thread/thread/93713a7c32100625/31b2cd361def53b0?show_docid=31b2cd361def53b0#).


---

Comment by kcrisman created at 2009-10-24 00:04:01

This will also happen with %e and e, and any other similar pairs, so a fix should take care of all of them.


---

Comment by robert.marik created at 2010-03-23 21:34:44

As another consequence, solving of ode y'=c*x is not correct, the free variable is messed up with a parameter, see [sage-devel](http://groups.google.cz/group/sage-devel/browse_thread/thread/e04cbc547095f2ac) - thanks for  	 	
Yuri Karadzhov

```
[marik@um-bc107 /opt/sage-4.3.4]$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: from sage.calculus.calculus import symbolic_expression_from_maxima_string
sage: symbolic_expression_from_maxima_string('%c')
c
sage: c=var('c'); y=function('y',x); eq=diff(y,x)==c*x; eq
D[0](y)(x) == c*x
sage: desolve(eq,y,ivar=x)
1/2*c*x^2 + c
```

the answer should be something like 1/2*c*x^2 + c1


---

Comment by jason created at 2010-05-03 17:35:13

See #8734 for what I think is a "needs work" solution.


---

Comment by jason created at 2010-05-03 17:36:52

Actually, I guess the patch at #8734 will *help* with the solution, but may not totally solve the problem.


---

Comment by robert.marik created at 2010-07-04 15:53:31

This should fix also #9421.


---

Comment by kcrisman created at 2012-07-26 15:04:53

Also, in a situation where we _don't_ have the duplication of constants, we get

```
sage: c
Traceback (click to the left of this block for traceback)
...
NameError: name 'c' is not defined
```

which isn't good either, though apparently that part of the expression still has type SymbolicExpression.


---

Comment by rws created at 2014-02-18 07:39:57

Set to critical due to dependent tickets.


---

Comment by rws created at 2014-02-18 07:39:57

Changing priority from major to critical.


---

Comment by rws created at 2014-03-24 17:59:05

Replying to [comment:5 jason]:
> Actually, I guess the patch at #8734 will *help* with the solution, but may not totally solve the problem.

Indeed, because the patch at #8734 (needing review) only is about vars, and it will only help with the problem in comment:3 if the then marked sage vars are renamed to some other specific string before output in desolve...().


---

Comment by rws created at 2014-03-26 16:07:04

Replying to [comment:3 robert.marik]:
> As another consequence, solving of ode y'=c*x is not correct
> ...
> the answer should be something like 1/2*c*x^2 + c1

This one is resolved in #16007. So it seems only variables are left (#8734).


---

Comment by kcrisman created at 2014-03-27 16:43:23

Yes, variables are all that's left, but the other way around!   (Don't forget the initial examples of this ticket.) We need to disambiguate Maxima variables like `i` and `e` from the things that become those in Sage - `%i` and `%e`.   I suppose one could take the Maxima variables `i` and `I` and turn them into `_i` and `_I`, and likewise for e, as at #16007, but I'm not sure if that's ideal or not.  Thoughts?


---

Comment by rws created at 2014-06-06 13:41:33

Priority changed as the more important fixes were outsourced to other tickets.


---

Comment by rws created at 2014-06-06 13:41:33

Changing priority from critical to minor.


---

Comment by kcrisman created at 2014-06-10 00:19:11

> Priority changed as the more important fixes were outsourced to other tickets.
Hmm, though the BDFL originally reported this with the comment

```
I think my email must have not been clear.  I think it's an instance   
of a *HUGE BUG* in Sage.  No more, no less.    
```



---

Comment by kcrisman created at 2014-06-24 15:47:55

Maybe we can change the Maxima `i` and `e` to Sage `_i` and `_e`, leaving `%i` and `%e` to become `i` and `e` as currently, and then taking advantage of the last changes at #16007 for typesetting more-or-less properly.


---

Comment by kcrisman created at 2014-06-24 15:47:55

Changing priority from minor to major.


---

Comment by rws created at 2014-06-26 09:39:30

The original bug report on sage-devel had:

```
sage: var('i')
i
sage: i
i
sage: a = i^2
sage: a.simplify_full()
-1
```

However, with develop I get `i^2`. Is this ticket still valid?


---

Comment by rws created at 2014-06-26 09:39:30

Changing status from new to needs_info.


---

Comment by kcrisman created at 2014-06-26 12:55:18

And indeed,

```
sage: from sage.calculus.calculus import symbolic_expression_from_maxima_string
sage: symbolic_expression_from_maxima_string('i')
i
sage: symbolic_expression_from_maxima_string('%i')
I
```

And the original solving case William reported is also fixed.  

Huh.  Is this before or after #8734? (I would imagine that one would have an impact.)  Anyway, I would say we add some doctests (for both the `sefms` and `i^2` cases) and call it a day, regardless of which ticket it depends on.  Good work, since ideally one wouldn't be creating a Maxima `i` and then trying to bring it to Sage.


---

Comment by rws created at 2014-06-26 16:48:28

Changing status from needs_info to needs_work.


---

Comment by rws created at 2014-06-26 16:48:28

With develop:

```
sage: from sage.calculus.calculus import symbolic_expression_from_maxima_string
sage: symbolic_expression_from_maxima_string('t')
t
sage: symbolic_expression_from_maxima_string('i')
I
sage: var('i')
i
sage: symbolic_expression_from_maxima_string('i')
i
```

So that example is a different animal than the ticket case.


---

Comment by kcrisman created at 2014-06-26 19:50:30

Okay, I see.  But the thing is that, in principle, we should never get `i` inside Maxima without asking for it via Sage having a variable `i`; we should only get `%i` the imaginary in Maxima, which translates differently (and correctly) now.  Does that make sense, or do you think this is still worth fixing?  (We should check what happens with `e` as well, maybe via `ln(e)`.)


---

Comment by rws created at 2014-06-26 20:48:09

With #8734 `I` can result from a Sage `I` variable, from Maxima `%i`, or from Maxima `i` which is only creatable from Sage via the Maxima interface. But not from any trick involving the Sage variable `i` due to the protection via `_SAGE_VAR_`. The `i` case is why Jason said #8734 will help, but not totally solve the problem.

I don't know why the `i^2` example failed at all, and when exactly it stopped failing. Maybe it didn't fail; certainly nobody posted a confirmation message. And certainly we all confirmed the sefms snippet because that's what the ticket presented.


---

Comment by kcrisman created at 2014-06-26 21:10:59

Yeah, even in Sage 4.4.4 (which I have lying around due to some custom fixes I use for research I'm too lazy to update) 

```
sage: var('i')
i
sage: i
i
sage: a = i^2
sage: a
i^2
sage: a.simplify_full()
i^2
```

Your thoughts on a resolution?  The thing that was a bug is not there any more, and the only potential bug is from 'user error', in some sense.


---

Comment by rws created at 2014-06-27 09:18:56

At the moment we also get behaviour like

```
sage: symbolic_expression_from_maxima_string('%inf')
Inf
```

so I think the ticket should implement `multi_word_replace()` in `sage.misc.multireplace` and use that on a symtable with additional entries `'e':'_e', 'i':'_i', 'I':'_I'`.


---

Comment by rws created at 2014-06-27 09:18:56

Changing assignee from burcin to rws.


---

Comment by kcrisman created at 2014-06-27 12:25:40

> At the moment we also get behaviour like
> {{{
> sage: symbolic_expression_from_maxima_string('%inf')
> Inf
> }}}
Is `%inf` a normal Maxima expression, though?  They just use `inf` and `minf`, I believe, which we replace correctly.
> so I think the ticket should implement `multi_word_replace()` in `sage.misc.multireplace` and use that on a symtable with additional entries `'e':'_e', 'i':'_i', 'I':'_I'`.
I guess one could do so... I'm just trying to imagine cases in which this would be necessary due only to Sage usage.  If someone uses Maxima to create variables it's quite different.


---

Comment by rws created at 2014-06-27 14:34:25

Replying to [comment:27 kcrisman]:
> Is `%inf` a normal Maxima expression, though?  They just use `inf` and `minf`, I believe, which we replace correctly.
No but we do not want to be surprised when some new Maxima variable starting `%i` is introduced. At the moment it's really just a string replace from `%i` to `I`, without sense of word boundaries.


---

Comment by kcrisman created at 2014-06-27 14:44:44

> > Is `%inf` a normal Maxima expression, though?  They just use `inf` and `minf`, I believe, which we replace correctly.
> No but we do not want to be surprised when some new Maxima variable starting `%i` is introduced. At the moment it's really just a string replace from `%i` to `I`, without sense of word boundaries.
Aha!  I didn't catch that was the reason.  I don't think Maxima introduces many new constants with `%` but I see your point.


---

Comment by rws created at 2014-06-28 16:27:04

I also found an error in the definition for maxima variable, because it didn't allow variable names without '%' or the '%' not at the beginning. Now the mentioned rules can be expressed as simple entries in symtable.
----
New commits:


---

Comment by rws created at 2014-06-28 16:27:04

Changing status from needs_work to needs_review.


---

Comment by kcrisman created at 2014-06-30 14:36:27

> I also found an error in the definition for maxima variable, because it didn't allow variable names without '%' or the '%' not at the beginning. Now the mentioned rules can be expressed as simple entries in symtable.
You'll note that `maxima_var` was never currently used in the codebase, so it wasn't a problem, more of just old code - [here](https://github.com/sagemath/sagetrac-mirror/blob/master/src/sage/calculus/calculus.py#n1792) is where the `%` were all replaced.  If you wanted I guess you could just replace that with `_` and it would be much more efficient than doing this whole loop every time, or so it seems to me.  How does this do with `timeit` for long expressions one gets in 'real life'?  (See sage/symbolic/random_tests.py.)  Also note that usually we end up having to special-case things with `%` anyway - e.g., `%ilt` (inverse Laplace transform) gets handled somewhere else, I'd have to look up where.


---

Comment by rws created at 2014-06-30 15:30:47

Replying to [comment:34 kcrisman]:
> How does this do with `timeit` for long expressions one gets in 'real life'?  (See sage/symbolic/random_tests.py.)
It's within the measurement error:

```
sage: from sage.calculus.calculus import symbolic_expression_from_maxima_string as sefms
sage: var('v1,v2,v3')
(v1, v2, v3)
sage: ex=-1/3*(pi + 1)*(3*(euler_gamma - e)*(pi - 3*v1 - v1/arcsech(1) + e^(-1)/pi) - 6*v3^2*arcsinh(-v1 + e)/v2 - v2 - 3*log_gamma(v1*v3)/v2 - 3*e^(-254) + 3)*(-catalan/v3)^(twinprime*pi - 1/2*v1 - 1/2*v2)*inverse_jacobi_cs(1, v3)/jacobi_sc(1/arccos(-1/(v1*csc(v3))), v3/v1 + e) - 1/4*(2*v3^2*(e + 1) + ((e*log_integral(arcsech(exp_integral_e1(v2^mertens - 1) - 4)) + 15*v1 + jacobi_dn(v2, pi))*v1*e^(-1) + golden_ratio*pi^v1*(1/v3^12 + jacobi_ds(-10, csc(v3^2)))^(v2 - 1/2/v2)*sinh(v2*e)/((v1 + v2 + v3 + 1)*v2))/(v1^2*inverse_jacobi_nc(v1, -e)) - 2*bessel_Y(v3, v2))/v2 + v3/inverse_jacobi_sc(1, v2) - (v1 + 1)/((v2 + v3)*(2*(v1 + e)*(v3 - 1)/(pi + v1) + (-v3*sech(v1*v3)/v2)^(-e/v1))) + inverse_jacobi_cn(pi + v1*v3, pi - v3) + jacobi_sn(e, arctanh(-(-log_integral(2) + log_integral(jacobi_ds(-1, v3)))^v2*e)^(1/7*(18*v2 - v3)*(14*v2 + e)/(v3*arctan(1/v2)*kronecker_delta(v1, v3))))
sage: timeit('sefms(str(ex))')
5 loops, best of 3: 2.19/2.14/2.15 s per loop (without #6882)
5 loops, best of 3: 2.13/2.11/2.12 s per loop (with #6882)
```

Obviously the whole routine takes so long that the loop doesn't signify. That may be worth an optimization ticket alone.
> Also note that usually we end up having to special-case things with `%` anyway - e.g., `%ilt` (inverse Laplace transform) gets handled somewhere else, I'd have to look up where.
Just put it in `symtable`, give it a special value, and ask for that value within the new loop. Having it all in the loop is more efficient than find every time.


---

Comment by rws created at 2014-06-30 16:06:17

Replying to [comment:35 rws]:
> {{{
> sage: timeit('sefms(str(ex))')
> 5 loops, best of 3: 2.19/2.14/2.15 s per loop (without #6882)
> 5 loops, best of 3: 2.13/2.11/2.12 s per loop (with #6882)
> }}}
It calls 120 times the function `MaximaLib._eval_line()` which takes 17ms in average = 2 seconds. 17 ms is an eternity.


---

Comment by kcrisman created at 2014-06-30 16:10:19

> > {{{
> > sage: timeit('sefms(str(ex))')
> > 5 loops, best of 3: 2.19/2.14/2.15 s per loop (without #6882)
> > 5 loops, best of 3: 2.13/2.11/2.12 s per loop (with #6882)
> > }}}
Wow, those timings are indeed an eternity, though presumably not for shorter expressions.  I'll put this ticket in my "finally finish reviewing" queue, then, for sure.


---

Comment by kcrisman created at 2014-07-02 02:44:01

Well, it's an improvement, though still not perfect:

```
# Before
sage: sefms('%inf')
Inf
sage: sefms('%minf')
-Infinity
# After
sage: sefms('%inf')
+Infinity
sage: sefms('%minf')
-Infinity
```

Neither of these are infinity in Maxima, of course.  And indeed here is what the [Maxima manual](http://maxima.sourceforge.net/docs/manual/en/maxima_6.html#SEC32) says about identifiers:

```
(%i1) %an_ordinary_identifier42;
(%o1)               %an_ordinary_identifier42
```

"A numeral may be the first character of an identifier if it is preceded by a backslash. "  But I don't know that we need to translate all identifiers in Maxima to Sage here... I guess I'm torn about that.  

```
sage: timeit('sefms(str(ex))')
5 loops, best of 3: 2.19/2.14/2.15 s per loop (without #6882)
5 loops, best of 3: 2.13/2.11/2.12 s per loop (with #6882)
```

Of course, thinking about it, that string is a Sage string, not a Maxima string, so `%time R = random_expr(50,nvars=2); sefms(repr(R._maxima_()))` is probably more accurate, but that is also wildly variant on the expression.

Okay, as far as I can tell this will not break anything (let's really hope!) and fixes the actual problem without slowing down what is already a very slow process (even for `random_expr(5,nvars=2)` it's 2-3 milliseconds either way).  Step in right direction, and again most people should not be affected in the slightest.  If passes tests, let's get it in.


---

Comment by kcrisman created at 2014-07-02 03:03:09

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2014-07-03 12:41:31

Resolution: fixed
