# Issue 1173: implement numerical evaluation of erf at complex arguments

Issue created by migration from Trac.

Original creator: was

Original creation time: 2007-11-15 07:45:25

Assignee: was

CC:  benjaminfjones

When implemented, this would work:

sage: a = sqrt(pi)*I*erf(2*I)/2
sage: CC(a)
...


---

Comment by was created at 2007-11-15 07:48:11

See also
http://trac.sagemath.org/sage_trac/ticket/1174


---

Comment by boothby created at 2007-11-15 08:05:03

The following has a GPL'd implementation in c:

http://velveeta.che.wisc.edu/octave/lists/archive/octave-sources.1998/msg00032.html


---

Comment by was created at 2007-11-16 18:03:43

This looks like the wya to go:

Josh Kantor:

```
scipy has an error function that takes complex arguments

sage:  import numpy, scipy
sage:  from scipy import special
sage:  j=numpy.complex(0,1)
sage: -j*float(sqrt(pi))*special.erf(2*j)/2
(16.45262776550727+0j)

Unfortunately numpy and sage's complex numbers are not compatible yet.


```



---

Comment by kcrisman created at 2009-12-30 04:10:09

Numpy and Sage numbers now seem to work well, at least to some extent:

```
sage: import numpy
sage: CC(numpy.complex(0,1))
1.00000000000000*I
sage: CC(numpy.complex(1,1))
1.00000000000000 + 1.00000000000000*I
sage: import scipy
sage: CC(scipy.special.erf(numpy.complex(1,1)))
1.31615128169795 + 0.190453469237835*I
```

Is it time to wrap this now, two years after opening?


---

Comment by AlexGhitza created at 2010-01-02 07:21:53

This can also be done by mpmath in arbitrary precision, see


```
sage: import mpmath
sage: mpmath.erf?
```



---

Comment by kcrisman created at 2010-02-05 20:01:40

Replying to [comment:5 AlexGhitza]:
> This can also be done by mpmath in arbitrary precision, see
> 
> {{{
> sage: import mpmath
> sage: mpmath.erf?
> }}}

And erf already has an _eval_f method, so maybe this could be changed to use mpmath?  Even a loss in speed would be worth having the complex values.    This could apply to error_fcn/erfc and others as well.


---

Comment by kcrisman created at 2010-06-09 01:39:44

Update - yes, we should definitely do this because of the complex values - just had a support request about not being able to do 

```
sage: integrate(sin(x^2),(x,2,6))
```

and then use n() because of this (partly).  See also #9044.


---

Comment by dsm created at 2011-02-24 02:23:14

Okay, here's v0.prealpha0.0_1a of a patch which uses mpmath to get complex and arbitrary-precision behaviour for erf.  (If it works out we can do error_fcn the same way, as noted by kcrisman).

Unfortunately it does introduce a speed regression:


```
# 4.6.1, via pari
sage: timeit('float(erf(0))',number=1000) # must be float because 4.6.1 doesn't evaluate
1000 loops, best of 3: 109 µs per loop
sage: timeit('erf(0.1)',number=1000)
1000 loops, best of 3: 98.4 µs per loop
sage: timeit('erf(0.99)',number=1000)
1000 loops, best of 3: 98.5 µs per loop

# 4.6.2rc0 with patch
sage: timeit('erf(0)',number=1000)
1000 loops, best of 3: 68.3 µs per loop
sage: timeit('erf(0.1)',number=1000)
1000 loops, best of 3: 154 µs per loop
sage: timeit('erf(0.99)',number=1000)
1000 loops, best of 3: 165 µs per loop
```


I attempted to fix this by using the old approach for the default precision, but it usually wound up being more expensive to do the tests.  Someone with better speed-fu is encouraged to look at it.  I haven't finished a long testall yet, so there's probably something somewhere which breaks, but here's the first attempt.


---

Comment by burcin created at 2011-02-24 09:31:45

Changing status from new to needs_work.


---

Attachment

The patch looks really good. The only problem I spotted after a quick reading is that the code blocks in the documentation should be after `::`. If the `TESTS` title is followed by text, you don't need the `::` after that.

AFAIR, mpmath now supports extracting the precision from the input type in Sage. It is not necessary to do this in each calling function any more. I don't have an example handy though.

For examples of fast methods to check the type of the input you can look at `sage/symbolic/pynac.pyx`. If you replace the `PY_TYPE_CHECK()` calls with `isinstance()` you should get a reasonable speed from python.


---

Comment by dsm created at 2011-02-24 09:57:55

`@`burcin:

Okay, so just to be clear: EXAMPLES and TESTS don't need trailing colons, whether double or single (although double does seem pretty common; is it okay to use it?), but I should definitely use a double colon after test descriptions, e.g.


```
TESTS[::?]

Test that addition works::

    sage: 2+3
    5

Test that subtraction works::

    sage: 3-2
    1

```


instead of


```
TESTS::

Test that addition works:

    sage: 2+3
    5

Test that subtraction works:

    sage: 3-2
    1
```


That's easy enough to fix.  The other two will take a bit more work, but I'll see what I can find.  Examples to pattern after are very welcome.  `:-)`


---

Comment by kcrisman created at 2011-02-24 14:58:27

Usually we use one colon after `TEST` if there is text after it.  The double colon needs to be before any actual test block.  Also, doing `./sage -docbuild reference html` should give warning messages if it's wrong, if the file is in the reference manual (not all are).


---

Comment by dsm created at 2011-02-25 15:58:43

It seems like most of the speed decrease isn't due to anything I'm doing in _evalf_ but in _eval_, namely that I have one as opposed to the default BuiltinFunction._eval_.  When I switch back to the default one I recover the old speeds, except that I no longer know how to get erf(0)=0 without wrapping the whole thing, and it has strange ideas about which arguments shouldn't be evaluated (such as ComplexField).  I also didn't manage to find whatever mpmath magic will allow me to avoid the if isinstance(parent, Parent) and hasattr(parent, 'prec') or try: parent.prec() approach.

I'm at a loss for ways to proceed that don't involve modifying function.pyx, cythonizing, or wrapping the entire function to patch the holes.


---

Comment by burcin created at 2011-06-17 19:21:31

Replying to [comment:12 dsm]:
> I'm at a loss for ways to proceed that don't involve modifying function.pyx, cythonizing, or wrapping the entire function to patch the holes.  

The speed problems can be solved by replacing the zero test `x == 0` with the example in comment:17:ticket:11143. The patch attached to that ticket also contains an example call to mpmath without the `prec` clutter. AFAICT, the only remaining issue with this ticket is the docstring formatting.

I'd be happy to give positive review to a patch with these changes... :)


---

Comment by kcrisman created at 2011-06-17 19:32:29

I'd say that it should also add one _very_ minor additional doctest, for `erf(sqrt(2))`.  That would allow us to close #9044 without not having a doctest.  I realize that symbolic input is checked, but it would be nice to have for completeness and addressing specific user requests :)


---

Comment by kcrisman created at 2011-06-20 15:59:24

Here's another thing that should be added, reported by one of the PREP workshop participants before this patch was in:

```
erf(4500).n()
1.0000000
erf(45000).n()
<boom>
```

So Pari was not handling big number in erf before.  With this patch, though

```
sage: erf(4500).n()
1.00000000000000
sage: erf(45000).n()
1.00000000000000
sage: erf(4500000000).n()
1.00000000000000
```

Since none of the doctests in the current patch seem to test "big" real input to erf, we should add this too.


---

Comment by kcrisman created at 2011-08-01 16:43:13

This should also solve #11626, I think?


---

Comment by zimmerma created at 2011-08-18 10:09:48

Replying to [comment:16 kcrisman]:
> This should also solve #11626, I think?

right, thus #11626 can be closed as soon as this ticket is closed
(or maybe right now?).

Douglas, can you implement the work issues in your patch?

Paul


---

Comment by kcrisman created at 2011-08-18 14:51:29

So, to review:
 * Burcin and I want a small formatting change so the doc would build correctly.
 * Burcin wants the speed to be fixed using the thing referenced at #11143, using the patch at #11513.
 * I want a doctest that checks big numbers will work (as in [comment:15 comment 15]).
 * Paul and I want a doctest for #11626, to verify it is fixed.
 * Burcin _recommends_ calling mpmath without prec as at #11143.

This would make this depend on #11513.  I'm still a little skeptical on this; will we really not get any wrong answers with that?


---

Comment by zimmerma created at 2011-08-18 15:10:36

Replying to [comment:18 kcrisman]:
> So, to review:
>  * I want a doctest that checks big numbers will work (as in [comment:15 comment 15]).
>  * Paul and I want a doctest for #11626, to verify it is fixed.

the current patch already contains examples with prec=100, both for real and complex numbers,
and thus is fine to me.

Paul


---

Comment by kcrisman created at 2011-08-18 15:31:37

Replying to [comment:19 zimmerma]:
> Replying to [comment:18 kcrisman]:
> > So, to review:
> >  * I want a doctest that checks big numbers will work (as in [comment:15 comment 15]).
> >  * Paul and I want a doctest for #11626, to verify it is fixed.
> 
> the current patch already contains examples with prec=100, both for real and complex numbers,
> and thus is fine to me.

Okay.  I was thinking that because was not yet a test with the syntax `n(erf(2),100)`, which some users might find nicer than the other one, but of course they mean the same thing.  I'll leave that up to Doug, then.


---

Comment by kcrisman created at 2011-08-19 14:15:17

So:
 * Burcin and I want a small formatting change so the doc would build correctly.
 * Burcin wants the speed to be fixed using the thing referenced at #11143, using the patch at #11513.
 * I want a doctest that checks big numbers like `erf(45000).n()` will work (as in [comment:15 comment 15]).
 * I want a doctest for `erf(sqrt(2))` so #9044 can stay closed.
 * Burcin _recommends_ calling mpmath without prec as at #11143.


---

Comment by kcrisman created at 2011-10-25 01:18:01

See also #11948.


---

Comment by ddrake created at 2011-10-25 02:08:33

I ran into this problem (https://groups.google.com/d/topic/sage-support/SNw_6mLFnrg/discussion) and this patch fixes it. This patch seems to have some issues with a speed regression and some doctests, but it does fix a problem that I have.


---

Comment by dsm created at 2011-10-29 00:55:06

</lurk>

Okay, I'm back.  Is it worth finishing this patch or should we follow the #11948 path instead?


---

Comment by kcrisman created at 2011-10-29 02:14:37

> Okay, I'm back.  Is it worth finishing this patch or should we follow the #11948 path instead?

Go for it!


---

Comment by dsm created at 2011-10-29 20:17:26

Now I remember why I found this so frustrating.  I rewrote the patch following -- plagiarizing is more like it! -- the pattern used in #11143, but the speed issue hasn't gone away.  


```

# 4.7.1, OS X 10.6.8
sage: timeit('erf(0.1)',number=1000)
1000 loops, best of 3: 82.9 µs per loop
sage: timeit('erf(10.0)',number=1000)
1000 loops, best of 3: 72.8 µs per loop
sage: timeit('erf(100.0)',number=1000)
1000 loops, best of 3: 73.5 µs per loop

# 4.7.2 before patch
sage: timeit('erf(0.1)',number=1000)
1000 loops, best of 3: 69.4 µs per loop
sage: timeit('erf(10.0)',number=1000)
1000 loops, best of 3: 62.6 µs per loop
sage: timeit('erf(100.0)',number=1000)
1000 loops, best of 3: 62 µs per loop

# 4.7.2 after patch
sage: timeit('erf(0.1)',number=1000)
1000 loops, best of 3: 137 µs per loop
sage: timeit('erf(10.0)',number=1000)
1000 loops, best of 3: 116 µs per loop
sage: timeit('erf(100.0)',number=1000)
1000 loops, best of 3: 116 µs per loop

sage: import mpmath
sage: timeit('mpmath.erf(0.1)')
625 loops, best of 3: 95 µs per loop
sage: timeit('mpmath.erf(10.0)')
625 loops, best of 3: 75.4 µs per loop
sage: timeit('mpmath.erf(100.0)')
625 loops, best of 3: 76.2 µs per loop

```


That is, there's about a factor of two penalty in speed for the standard case, but it's not because the underlying mpmath code is slow:


```
sage: timeit('mpmath.erf(0.1r)')
625 loops, best of 3: 27.7 µs per loop
sage: timeit('mpmath.erf(10.0r)')
625 loops, best of 3: 9.85 µs per loop
sage: timeit('mpmath.erf(100.0r)')
625 loops, best of 3: 9.95 µs per loop
```


In fact, mpmath isn't that much slower than MPFR:


```
sage: z = RR(2); timeit('z.erf()')
625 loops, best of 3: 20 µs per loop
sage: z = 2.0r; timeit('mpmath.erf(z)')
625 loops, best of 3: 57.9 µs per loop
sage: timeit('erf(2.0)') # new code
625 loops, best of 3: 181 µs per loop
```


So not much of the total time is spent actually doing any calculations: it's all overhead.  :-(  This affects #11143 as well:


```
sage: timeit('exp_integral_e1(2.0)')
625 loops, best of 3: 165 µs per loop
sage: z = exp_integral_e1(2); timeit('z.n()')
625 loops, best of 3: 143 µs per loop
sage: timeit('exponential_integral_1(2.0)')
625 loops, best of 3: 44.7 µs per loop
sage: timeit('mpmath.e1(2.0)')
625 loops, best of 3: 123 µs per loop
sage: timeit('mpmath.e1(2.0r)')
625 loops, best of 3: 51 µs per loop

```



To wrap up:

(1) Both this patch and #11143 suffer a significant slowdown relative to PARI, and have major overheads relative to calling mpmath.  Some of that's unavoidable given the symbolic path, but ISTM we should be able to do better.  Ideally there would be a reasonably efficient general special function implementation pattern, along the lines of what Benjamin used, that intermittent developers like me could be pointed to as a reference.

(2) In the case of erf and erfc, mpfr offers a very fast evaluation for real numbers, fast enough that it might be worth using as the default in those cases (although Python-level branching is slow in my experience, maybe slow enough to wash away the benefits).  Once we settle on an approach for erf I'll do the same for erfc.

(3) Should I move this out of other.py to special.py, where the complementary error_fcn function lives now?  It would seem a more natural location for it.  We also have some unfortunate naming (erf and error_fcn) it might be worth addressing.

I don't have numbers for #11948 -- too many dependencies -- but it's probably considerably faster than this approach.  I figure it's probably worth getting the #11143 -style mpmath wrapper to be faster, though, even if we went #11948 instead for erf/erfc.

[There are a few doctest failures: "devel/sage/doc/en/bordeaux_2008/l_series.rst", which I think is unrelated; a timeout in devel/sage/sage/modules/free_module.py, again probably unrelated.]


---

Comment by dsm created at 2011-10-29 20:40:28

11143-style mpmath erf


---

Attachment

Replying to [comment:26 dsm]:
<snip>
> To wrap up:
> 
> (1) Both this patch and #11143 suffer a significant slowdown relative to PARI, and have major overheads relative to calling mpmath.  Some of that's unavoidable given the symbolic path, but ISTM we should be able to do better.  Ideally there would be a reasonably efficient general special function implementation pattern, along the lines of what Benjamin used, that intermittent developers like me could be pointed to as a reference.

I agree that we should do better. Note that the pattern you request is being developed in #11143  and here. Even though pynac based symbolics was merged in Sage quite a while ago, it hasn't been used properly yet.

The code path to call symbolic functions is rather convoluted. This is inevitable since symbolic functions have to play well with many different subsystems, such as fast float, numpy, etc. But it should still be possible to reduce the overhead.

For `BuiltinFunction`s the code path for evaluation goes through `Function.__call__()` in `sage/symbolic/function.pyx`, then into pynac, then to the python method you define for `_eval_()`, if numeric evaluation is needed to `_evalf_()` later. Here, between the python and C++ code, conversion functions are called to wrap pynac objects in Expression instances or to remove these wrappers.

I believe most of the overhead comes from the `__call__()` method, then having to decide if the arguments are numeric in `_eval_()`, and checking if an argument is zero (#11513).

> (2) In the case of erf and erfc, mpfr offers a very fast evaluation for real numbers, fast enough that it might be worth using as the default in those cases (although Python-level branching is slow in my experience, maybe slow enough to wash away the benefits).  Once we settle on an approach for erf I'll do the same for erfc.

MPFR should be the default numeric evaluation method if it is available. In general, it's better to let the types choose the numeric evaluation method. Most special functions in Sage first see if an object implements a method with the same name first and calls that. For instance `erf()` should call `.erf()` for element of `RR`.

I see that for subclasses of `GinacFunction` the `__call__()` method does this automatically. This is not used for other `BuiltinFunction`s though. It might make sense to move this method to `BuiltinFunction`. This would speed up most of the timings for real numbers above.

Unfortunately, floats would still go through the long path. Since these are used quite often in plotting, perhaps we should add a special case in `__call__()` to go directly to `_evalf_()` as well.

I made this change in attachment:trac_1173-move_call.patch. Now I get:


```
sage: t = RR(2.0)
sage: %timeit z = t.erf()
625 loops, best of 3: 16.9 µs per loop
sage: %timeit z = erf(t)
625 loops, best of 3: 18.2 µs per loop
```


Performance for `float` is still pretty bad.


```
sage: u = 2.0r
sage: %timeit z = erf(u)
625 loops, best of 3: 156 µs per loop
```


I didn't check if this patch breaks anything.

> (3) Should I move this out of other.py to special.py, where the complementary error_fcn function lives now?  It would seem a more natural location for it.  We also have some unfortunate naming (erf and error_fcn) it might be worth addressing.

I don't think there is a need to move this to `special.py`. That file is also overcrowded and needs serious cleanup. You could create a new file names `error_fn.py` if you think that's necessary.

What names do other systems use for these functions? AFAIK, `erf()` and `erfc()` are pretty much standard. I wonder where `error_fcn()` came from.


---

Attachment


---

Comment by dsm created at 2011-10-30 21:27:58

Okay, this looks a bit better.  With trac_1173-move_call.patch, trac_11885_v2.patch, trac_11513-is_numerically_zero.patch, and trac_1173_complex_erf_v3.patch:


```
alpha3:

0.100000000000000 float               121 µs per loop
0.100000000000000 RDF                 51.6 µs per loop
0.100000000000000 RR                  61.2 µs per loop
0.100000000000000 RealField(100)      64.5 µs per loop
0.100000000000000 RealField(1000)     304 µs per loop

new:
0.100000000000000 float               49.3 µs per loop
0.100000000000000 RDF                 773 ns per loop
0.100000000000000 RR                  7.07 µs per loop
0.100000000000000 RealField(100)      10.6 µs per loop
0.100000000000000 RealField(1000)     248 µs per loop
0.100000000000000 complex             131 µs per loop
0.100000000000000 CDF                 185 µs per loop
0.100000000000000 CC                  254 µs per loop
0.100000000000000 ComplexField(100)   262 µs per loop
0.100000000000000 ComplexField(1000)  470 µs per loop
0.100000000000000*I complex             247 µs per loop
0.100000000000000*I CDF                 389 µs per loop
0.100000000000000*I CC                  405 µs per loop
0.100000000000000*I ComplexField(100)   470 µs per loop
0.100000000000000*I ComplexField(1000)  565 µs per loop

```


Now not only is there no regression, we've improved.  The speedups relative to alpha3 for reals are due to using the existing mpfr .erf()s instead of pari; float was special-cased through RDF.  As I mentioned, I don't have the new pari, and that's probably faster than mpmath.  But at least it's not killing me anymore.

There's a doctest failure in gamma_inc due to trac_1173-move_call.patch, I think-- formerly,


```
sage: parent(gamma_inc(RDF(1),3))
Complex Field with 53 bits of precision
```

but now 

```
sage: parent(gamma_inc(RDF(1),3))
Real Double Field
```


but gamma_inc doesn't preserve types the way I'd have expected.  Anyway, I think this is a step in the right direction.


---

Attachment

11143-style erf, use mpfr where possible


---

Comment by kcrisman created at 2011-11-22 01:46:30

Qs, as this is now official fodder for [wiki/days35.5/bugs Sage Days 35.5]:
 * What patches should be applied here?  
 * Are we ready for review?   (I.e., are all work issues taken care of?)
 * What's the status of #11513 with respect to this patch?

Thanks!


---

Comment by benjaminfjones created at 2011-12-16 01:43:52

Replying to [comment:29 kcrisman]:
> Qs, as this is now official fodder for [wiki/days35.5/bugs Sage Days 35.5]:
>  * What patches should be applied here?  
>  * Are we ready for review?   (I.e., are all work issues taken care of?)
>  * What's the status of #11513 with respect to this patch?
> 
> Thanks!

I started to review the patch. Looks like:

 * The only dependency is #11513 which should be applied before [trac_1173_complex_erf_v3.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/1173/trac_1173_complex_erf_v3.patch)
 * All of the work issues are taken care of
 * #11513 hasn't changed since Burcin uploaded the initial draft patch. I don't have the expertise to work on it or else I would in support of the various tickets we've got now that depend on it. 

The patch trac_1173_complex_erf_v3.patch applies to 4.8.alpha3 cleanly (as does the patch at #11513) and all doctests pass. 

It also looks like the "move call" patch should be applied to speed things up after some doctests are fixed. I'd say this should go into a new ticket because the issue is independent of evaluation of erf() at complex inputs.

Positive review.


---

Comment by kcrisman created at 2011-12-19 17:59:07

Does this also take care of #8983?


---

Comment by benjaminfjones created at 2011-12-19 18:47:43

Yes, both of these doctests are in DSM's patch:


```
sage: erf(0) 
0 
sage: solve(erf(x)==0,x) 
[x == 0] 
```



---

Comment by zimmerma created at 2011-12-24 14:52:00

Benjamin or Burcin, please could you add in the description which patches have to be applied, and in which order?

Paul


---

Comment by zimmerma created at 2011-12-24 14:55:24

Benjamin, you gave a positive review in comment [comment:31] but forgot to change the status accordingly.

Paul


---

Comment by benjaminfjones created at 2011-12-24 16:09:55

Changing status from needs_work to positive_review.


---

Comment by benjaminfjones created at 2011-12-24 16:11:07

Done. I was waiting to see if anyone else had comments or concerns before setting the status to positive review, but looks like it's been long enough. I've done some work on #11513 in the last few days. I'll update there the next change I get.


---

Comment by jdemeyer created at 2011-12-26 09:33:21

This obviously conflicts with #11948


---

Comment by vbraun created at 2012-01-08 18:38:26

Fixed in #11948, so I the release manager should close this ticket as duplicate.


---

Comment by kcrisman created at 2012-01-08 20:38:50

Though perhaps we should check that all doctests are still included!


---

Comment by jdemeyer created at 2012-01-09 13:07:57

Replying to [comment:41 kcrisman]:
> Though perhaps we should check that all doctests are still included!

Which is certainly not the case.  In fact, this ticket here does more than simply implementing `erf()` for complex arguments.


---

Comment by benjaminfjones created at 2012-01-09 15:44:28

It seems to me that both PARI and mpmath should be an option via an `algorithm` keyword argument. I'm at Sage Days 35.5 working on this stuff, so one thing I could do is take the improvements in this ticket and rebase them on top of #11948 which has been merged in 4.8.alpha6. If folks agree, I guess that should be a new ticket and this one could be closed.


---

Comment by benjaminfjones created at 2012-01-09 15:44:28

Changing keywords from "" to "sd35.5".


---

Comment by kcrisman created at 2012-01-09 16:03:38

Sounds good, as long as you keep any "good stuff" from this ticket.


---

Comment by zimmerma created at 2012-01-09 16:24:15

Hi Benjamin,

note that 4.8.rc1 is already out, should be newer than 4.8.alpha6.

Paul (at SD 35.5 too, but remotely)


---

Comment by benjaminfjones created at 2012-01-09 16:31:59

Hi Paul, are you on IRC? We're using the #sagemath-days channel. It looks like the 4.8.rc1 is still under construction according to the README. I'm looking in http://sage.math.washington.edu/home/release/sage-4.8.rc1/


---

Comment by zimmerma created at 2012-01-09 16:44:31

no I'm not on IRC. Ok, then I'll use 4.8.alpha6 instead.

Paul


---

Comment by jdemeyer created at 2012-01-09 20:03:12

Replying to [comment:45 zimmerma]:
> Hi Benjamin,
> 
> note that 4.8.rc1 is already out, should be newer than 4.8.alpha6.

It certainly isn't out yet (and maybe it will never even exist if rc0 solves all our problems).  The easiest way to find out the latest development release is [http://www.sagemath.org/download-latest.html](http://www.sagemath.org/download-latest.html), accessible as www.sagemath.org -> Download -> Development Release.
Alternatively, look at the sage-release announcements.


---

Comment by benjaminfjones created at 2012-01-09 21:00:56

Changing status from positive_review to needs_work.


---

Comment by benjaminfjones created at 2012-01-09 21:00:56

OK, the feeling here at SD35.5 is to hijack this ticket (change the ticket description) to rebase the work done by DSM on top of Sage-4.8.alpha6 (rather than making a new ticket) so the work and documentation improvements here are preserved and compatible with #11948. Please pipe up if you're following this ticket and have an opinion.


---

Comment by jdemeyer created at 2012-01-09 21:10:21

Fine by me.


---

Comment by kcrisman created at 2012-07-02 14:02:22

See comments at #11948 for why we probably want to do this or #13050 as soon as possible.


---

Comment by kcrisman created at 2013-06-12 20:12:30

With respect to the move call patch, see also #13933.


---

Comment by kcrisman created at 2013-06-12 20:13:49

Apply trac_1173_complex_erf_v3.patch


---

Comment by kcrisman created at 2013-06-19 06:20:18

Pretty much everything here was done at #11948 or #13001.  So let's close this (just a little I moved to #13050.


---

Comment by kcrisman created at 2013-06-19 06:20:18

Changing status from needs_work to positive_review.


---

Comment by jdemeyer created at 2013-06-19 12:16:37

Resolution: duplicate
