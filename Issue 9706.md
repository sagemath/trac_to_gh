# Issue 9706: New Version of orthogonal Polynomials

Issue created by migration from https://trac.sagemath.org/ticket/9706

Original creator: maldun

Original creation time: 2010-08-08 00:37:05

Assignee: burcin

CC:  fredrik.johansson fstan kcrisman

Keywords: orthogonal polynomials, symbolics

The current implementation of orthogonal polynomials is just a wrapper around maxima. (see http://wiki.sagemath.org/symbolics/)
There are the following improvements planed:

-using of the pynac class for symbolic functions.
-faster evaluation in general
-evaluation of special values
-mpmath for numeric evaluation


---

Attachment

A new version of the orthogonal_polys.py file.


---

Comment by maldun created at 2010-08-09 00:13:36

Newer version, with legendre_P, and faster evaluation of symbolic expressions


---

Attachment

Version from 10. August 2010


---

Comment by maldun created at 2010-08-11 00:07:02

Latest version. It holds classes of all polys (but not all completed yet)


---

Attachment

All Polys now have their own class.
Much faster evaluation is added.
Numerical evaluation is provided. 
Except for legendre_Q, gen_legendre_P, and gen_legendre_Q these aren't ready yet


---

Comment by maldun created at 2010-08-11 00:11:08

Replying to [comment:1 maldun]:
> All Polys now have their own class.
> Much faster evaluation is added.
> Numerical evaluation is provided. 
> Except for legendre_Q, gen_legendre_P, and gen_legendre_Q these aren't ready yet

orthogonal_polys4.py hold all changes but is not a patch yet, because it holds old code fragments,
which I have to clean up...


---

Comment by maldun created at 2010-08-12 10:25:41

I added in the latest patch (and orthogonal_polys.4.py contains these changes also) a new symbolic evaluation method for the orthogonal polynomials: Instead of call Maxima or use of the recursion, the polynomial is evaluated just using explicit formulas from Abramowitz and Stegun. This is an O(n) algorithm of course.

a little comparison on my machine:
old version:

sage: time chebyshev_T(10,x);
CPU times: user 0.01 s, sys: 0.00 s, total: 0.01 s
Wall time: 0.04 s
sage: time chebyshev_T(100,x);
CPU times: user 0.13 s, sys: 0.01 s, total: 0.14 s
Wall time: 0.23 s
sage: time chebyshev_T(1000,x);
CPU times: user 5.01 s, sys: 0.01 s, total: 5.02 s
Wall time: 6.98 s
sage time chebyshev_T(5000,x);
??? (I got no output her after 2min)

sage: time gegenbauer(10,5,x);
CPU times: user 0.01 s, sys: 0.00 s, total: 0.01 s
Wall time: 0.05 s
sage: time gegenbauer(100,5,x);
CPU times: user 0.19 s, sys: 0.00 s, total: 0.19 s
Wall time: 0.29 s
sage: time gegenbauer(1000,5,x);
CPU times: user 5.46 s, sys: 0.02 s, total: 5.48 s
Wall time: 7.79 s


New Version
sage: time chebyshev_T(10,x);
CPU times: user 0.01 s, sys: 0.00 s, total: 0.01 s
Wall time: 0.01 s
sage: time chebyshev_T(100,x);
CPU times: user 0.06 s, sys: 0.00 s, total: 0.06 s
Wall time: 0.08 s
sage: time chebyshev_T(1000,x);
CPU times: user 1.22 s, sys: 0.00 s, total: 1.22 s
Wall time: 1.22 s
sage: time chebyshev_T(5000,x);
CPU times: user 27.17 s, sys: 0.15 s, total: 27.32 s
Wall time: 27.46 s

sage: time gegenbauer(10,5,x);
CPU times: user 0.01 s, sys: 0.00 s, total: 0.01 s
Wall time: 0.01 s
sage: time gegenbauer(100,5,x);
CPU times: user 0.03 s, sys: 0.00 s, total: 0.03 s
Wall time: 0.04 s
sage: time gegenbauer(1000,5,x);
CPU times: user 1.08 s, sys: 0.01 s, total: 1.09 s
Wall time: 1.11 s

 
A little bit faster :) I also don't need to spawn an instance of maxima which makes the initialisation faster.

And now also wider symbolic evaluation is possible:

old version:
sage: var('a')
a
sage: gegenbauer(3,a,x)
...
NameError: name 'a' is not defined

new version:
sage: var('a')
a
sage: gegenbauer(3,a,x)
4/3*x^3*gamma(a + 3) - 2*x*gamma(a + 2)

The code needs now some cleanup, especially the documentations.
The complete versions for legendre_Q, gen_legendre_P, and gen_legendre_Q will not be finished
soon since the mpmath functions, don't seem to work correctly...
I only provide a call function for maxima for them now.


---

Comment by fredrik.johansson created at 2010-08-12 11:12:10

> The complete versions for legendre_Q, gen_legendre_P, and gen_legendre_Q will not be finished soon since the mpmath functions, don't seem to work correctly...

Care to elaborate?


---

Attachment

Latest version from 12. August 2010 (with bugfix in legendre_P)


---

Comment by maldun created at 2010-08-12 11:16:40

Killed bug in legendre_P


---

Comment by maldun created at 2010-08-16 11:51:22

Replying to [comment:5 fredrik.johansson]:
> > The complete versions for legendre_Q, gen_legendre_P, and gen_legendre_Q will not be finished soon since the mpmath functions, don't seem to work correctly...
> 
> Care to elaborate?

Sorry for the late answer, I was on holidays.

In mpmath I have probs with the legenp and legenq functions. For some inputs I get this error:


```
sage: mpmath.call(mpmath.legenp,5,1,2)
---------------------------------------------------------------------------
OverflowError                             Traceback (most recent call last)

/home/maldun/prog/sage/ortho/<ipython console> in <module>()

/home/maldun/sage/sage-4.5.1/local/lib/python2.6/site-packages/sage/libs/mpmath/utils.so in sage.libs.mpmath.utils.call (sage/libs/mpmath/utils.c:5021)()

/home/maldun/sage/sage-4.5.1/local/lib/python2.6/site-packages/mpmath/functions/hypergeometric.pyc in legenp(ctx, n, m, z, type, **kwargs)
   1481             T = [1+z, 1-z], [g, -g], [], [1-m], [-n, n+1], [1-m], 0.5*(1-z)
   1482             return (T,)
-> 1483         return ctx.hypercomb(h, [n,m], **kwargs)
   1484     if type == 3:
   1485         def h(n,m):

/home/maldun/sage/sage-4.5.1/local/lib/python2.6/site-packages/mpmath/functions/hypergeometric.pyc in hypercomb(ctx, function, params, discard_known_zeros, **kwargs)
    125                     [ctx.gamma(a) for a in alpha_s] + \
    126                     [ctx.rgamma(b) for b in beta_s] + \
--> 127                     [ctx.power(w,c) for (w,c) in zip(w_s,c_s)])
    128                 if verbose:
    129                     print "    Value:", v

/home/maldun/sage/sage-4.5.1/local/lib/python2.6/site-packages/mpmath/ctx_base.pyc in power(ctx, x, y)
    417             3.16470269330255923143453723949e+12978188
    418         """
--> 419         return ctx.convert(x) ** ctx.convert(y)
    420 
    421     def _zeta_int(ctx, n):

/home/maldun/sage/sage-4.5.1/local/lib/python2.6/site-packages/sage/libs/mpmath/ext_main.so in sage.libs.mpmath.ext_main.mpnumber.__pow__ (sage/libs/mpmath/ext_main.c:13946)()

/home/maldun/sage/sage-4.5.1/local/lib/python2.6/site-packages/sage/libs/mpmath/ext_main.so in sage.libs.mpmath.ext_main.binop (sage/libs/mpmath/ext_main.c:4588)()

/home/maldun/sage/sage-4.5.1/local/lib/python2.6/site-packages/mpmath/libmp/libelefun.pyc in mpf_pow(s, t, prec, rnd)
    340     # General formula: s**t = exp(t*log(s))
    341     # TODO: handle rnd direction of the logarithm carefully
--> 342     c = mpf_log(s, prec+10, rnd)
    343     return mpf_exp(mpf_mul(t, c), prec, rnd)
    344 

/home/maldun/sage/sage-4.5.1/local/lib/python2.6/site-packages/mpmath/libmp/libelefun.pyc in mpf_log(x, prec, rnd)
    725     # optimal between 1000 and 100,000 digits.
    726     if wp <= LOG_TAYLOR_PREC:
--> 727         m = log_taylor_cached(lshift(man, wp-bc), wp)
    728         if mag:
    729             m += mag*ln2_fixed(wp)

/home/maldun/sage/sage-4.5.1/local/lib/python2.6/site-packages/mpmath/libmp/libelefun.pyc in log_taylor_cached(x, prec)
    643     else:
    644         a = n << (cached_prec - LOG_TAYLOR_SHIFT)
--> 645         log_a = log_taylor(a, cached_prec, 8)
    646         log_taylor_cache[n, cached_prec] = (a, log_a)
    647     a >>= dprec

/home/maldun/sage/sage-4.5.1/local/lib/python2.6/site-packages/mpmath/libmp/libelefun.pyc in log_taylor(x, prec, r)
    607     """
    608     for i in xrange(r):
--> 609         x = isqrt_fast(x<<prec)
    610     one = MPZ_ONE << prec
    611     v = ((x-one)<<prec)//(x+one)

/home/maldun/sage/sage-4.5.1/local/lib/python2.6/site-packages/mpmath/libmp/libintmath.pyc in isqrt_fast_python(x)
    240                     y = (y + x//y) >> 1
    241         return y
--> 242     bc = bitcount(x)
    243     guard_bits = 10
    244     x <<= 2*guard_bits

/home/maldun/sage/sage-4.5.1/local/lib/python2.6/site-packages/mpmath/libmp/libintmath.pyc in python_bitcount(n)
     78     if bc != 300:
     79         return bc
---> 80     bc = int(math.log(n, 2)) - 4
     81     return bc + bctable[n>>bc]
     82 

OverflowError: cannot convert float infinity to integer
```



---

Comment by fredrik.johansson created at 2010-08-16 15:55:46

That looks strange. I get:


```
sage: import sage.libs.mpmath.all as mpmath
sage: mpmath.call(mpmath.legenp, 5,1,2)
-2.96434298694874e-22 - 912.574269237852*I
sage: mpmath.call(mpmath.legenp, 5,1,2, prec=100)
-2.1062923756778274648015607872e-36 - 912.57426923785222402727329118*I
```



---

Comment by maldun created at 2010-08-17 08:54:50

Replying to [comment:8 fredrik.johansson]:
> That looks strange. I get:
> 
> {{{
> sage: import sage.libs.mpmath.all as mpmath
> sage: mpmath.call(mpmath.legenp, 5,1,2)
> -2.96434298694874e-22 - 912.574269237852*I
> sage: mpmath.call(mpmath.legenp, 5,1,2, prec=100)
> -2.1062923756778274648015607872e-36 - 912.57426923785222402727329118*I
> }}}

Hm strange. Today I install the new Sage version, perhaps it will then work again


---

Comment by maldun created at 2010-08-18 16:31:58

Replying to [comment:8 fredrik.johansson]:
> That looks strange. I get:
> 
> {{{
> sage: import sage.libs.mpmath.all as mpmath
> sage: mpmath.call(mpmath.legenp, 5,1,2)
> -2.96434298694874e-22 - 912.574269237852*I
> sage: mpmath.call(mpmath.legenp, 5,1,2, prec=100)
> -2.1062923756778274648015607872e-36 - 912.57426923785222402727329118*I
> }}}

It was the old version!a Thanx for pointing that out, I will continue soon =)


---

Comment by maldun created at 2010-08-19 16:24:16

Version from 19. August 2010


---

Attachment

So now a "beta" is ready with full support of all classes.

Only the Legendre functions are still using Maxima.

some advances for the future:

-Zernike polys (this should be done in the next time, since explicit formulas are available)
-support for numpy_eval. (But this will be done, when the scipy package is updated to 0.8, else it has no sense, because the current version of scipy does not support ortho polys well, but the newer can handle them)

Now I need some people for testing this out =)


---

Comment by maldun created at 2010-08-19 16:34:50

And there was an interisting bug:

the import of mpmath at the beginning of the file caused the whole trouble I had with the numeric evaluation of the legendre functions....

I think I should report this..


---

Comment by maldun created at 2010-08-19 16:35:08

Changing type from defect to enhancement.


---

Comment by maldun created at 2010-08-19 19:54:21

Added numpy support, eliminated some bugs (19.08.2010)


---

Attachment

> -support for numpy_eval. (But this will be done, when the scipy package is updated to 0.8, else it has no sense, because the current version of scipy does not support ortho polys well, but the newer can handle them)

I decided to give at least some numpy support for compability reasons.
But this is a bad hack...when scipy 0.8 comes I use scipy itself, I change this to a better version :)


---

Comment by maldun created at 2010-08-19 23:56:01

Changing status from new to needs_review.


---

Comment by maldun created at 2010-08-20 00:08:44

Some of the old doctests fail.
But it is not my fault, it seem's that it is a bug in the SymbolicFunction class.

see: http://trac.sagemath.org/sage_trac/ticket/9769


---

Attachment

Latest version with some code cleanup (no program changes)


---

Comment by maldun created at 2010-08-26 14:50:26

Changing assignee from burcin to burcin, maldun.


---

Comment by burcin created at 2010-08-28 12:03:30

Hi Stefan,

can you post a patch corresponding to attachment:orthogonal_polys.8.py for review?

Thanks,

Burcin


---

Comment by maldun created at 2010-08-28 16:49:03

Patch for latest version with some code cleanup (no program changes)


---

Attachment

Replying to [comment:20 burcin]:
> Hi Stefan,
> 
> can you post a patch corresponding to attachment:orthogonal_polys.8.py for review?
> 
> Thanks,

> Burcin

Done!


---

Comment by fredrik.johansson created at 2010-09-03 13:07:05

Why is mpmath's precision used by default? Shouldn't the default be RR / CC precision? Actually, does _evalf_ ever get called without this information?

Some complex tests would be nice.


---

Comment by maldun created at 2010-09-03 19:59:28

Replying to [comment:22 fredrik.johansson]:
> Why is mpmath's precision used by default? Shouldn't the default be RR / CC precision? Actually, does _evalf_ ever get called without this information?
> 
> Some complex tests would be nice.
> 

This is a good point, and it shouldn't be a problem to change that.
But I don't think it's a big deal, because the function takes the "parents" precision, which means, if my input is RR it evals it with RR's precision.

Of course can you call _evalf_ just with (), and then the default value is used.

I just sticked to the old's version tests, and expanded it. Of course it's possible to expand the tests. I hope I will find some time for it soon, since I have some other more urgent things todo also.


---

Comment by maldun created at 2010-09-03 20:05:52

Replying to [comment:23 maldun]:
> Replying to [comment:22 fredrik.johansson]:
> > Why is mpmath's precision used by default? Shouldn't the default be RR / CC precision? Actually, does _evalf_ ever get called without this information?
> > 
> > Some complex tests would be nice.
> > 
> 
> This is a good point, and it shouldn't be a problem to change that.
> But I don't think it's a big deal, because the function takes the "parents" precision, which means, if my input is RR it evals it with RR's precision.
> 
> Of course can you call _evalf_ just with (), and then the default value is used.
> 
Ok sorry, wrong explination: when your input are exact data types like ZZ ore QQ then the parent has no precision, then you need a default value


---

Comment by maldun created at 2010-09-05 10:27:48

Since it seems that numpy-1.4.1, and scipy 0.8 should work now (see #9808) I programmed a version which uses scipy itself to evaluate the orthogonal polys for numpy arrays. 
When the new versions of numpy/scipy become merged into sage I will provide a patch for these.

Another thing I have to mention are these 2 failde doctests:
  * sage -t  -long "devel/sage/sage/symbolic/random_tests.py"
  * sage -t  -long "devel/sage/sage/symbolic/pynac.pyx"


```
sage -t -long "devel/sage/sage/symbolic/random_tests.py"    
**********************************************************************
File "/home/maldun/sage/sage-4.5.2/devel/sage/sage/symbolic/random_tests.py", line 17:
    sage: [f for (one,f,arity) in _mk_full_functions()]
Expected:
    [Ei, abs, arccos, arccosh, arccot, arccoth, arccsc, arccsch,
    arcsec, arcsech, arcsin, arcsinh, arctan, arctan2, arctanh,
    binomial, ceil, conjugate, cos, cosh, cot, coth, csc, csch,
    dickman_rho, dilog, dirac_delta, elliptic_e, elliptic_ec,
    elliptic_eu, elliptic_f, elliptic_kc, elliptic_pi, erf, exp,
    factorial, floor, heaviside, imag_part, integrate,
    kronecker_delta, log, polylog, real_part, sec, sech, sgn, sin,
    sinh, tan, tanh, unit_step, zeta, zetaderiv]
Got:
    [Ei, abs, arccos, arccosh, arccot, arccoth, arccsc, arccsch, arcsec, arcsech, arcsin, arcsinh, arctan, arctan2, arctanh, binomial, ceil, chebyshev_T, chebyshev_U, conjugate, cos, cosh, cot, coth, csc, csch, dickman_rho, dilog, dirac_delta, elliptic_e, elliptic_ec, elliptic_eu, elliptic_f, elliptic_kc, elliptic_pi, erf, exp, factorial, floor, gegenbauer, gen_laguerre, gen_legendre_P, gen_legendre_Q, heaviside, hermite, imag_part, integrate, jacobi_P, kronecker_delta, laguerre, legendre_P, legendre_Q, log, polylog, real_part, sec, sech, sgn, sin, sinh, tan, tanh, unit_step, zeta, zetaderiv]
**********************************************************************
File "/home/maldun/sage/sage-4.5.2/devel/sage/sage/symbolic/random_tests.py", line 237:
    sage: random_expr(50, nvars=3, coeff_generator=CDF.random_element)
Expected:
    (euler_gamma - v3^(-e) + (v2 - factorial(-e/v2))^(((2.85879036573 - 1.18163393202*I)*v2 + (2.85879036573 - 1.18163393202*I)*v3)*pi - 0.247786879678 + 0.931826724898*I)*arccsc((0.891138386848 - 0.0936820840629*I)/v1) + (-0.553423153995 + 0.5481180572*I)*v3 + 0.149683576515 - 0.155746451854*I)*v1 + arccsch(pi + e)*elliptic_f(khinchin*v2, 1.4656989704 + 0.863754357069*I)
Got:
    -v1*e^((0.0666829501658 + 0.206976992303*I)/(v3 + e))/v3 + hermite(-(v3^(-0.48519994364 - 0.485764091302*I) - log((1.21734510331 - 1.22580558833*I)*pi*v1 + zeta((0.781366128261 + 0.957400336147*I)*v1*e + (-1.8919687109 + 0.753422167447*I)*elliptic_f(v1, v1))*arccsch(v3)))*v1, (-0.647983235144 + 1.20665952957*I)*v1 + (0.0909404921682 + 0.281538203756*I)/v3)
**********************************************************************
File "/home/maldun/sage/sage-4.5.2/devel/sage/sage/symbolic/random_tests.py", line 239:
    sage: random_expr(5, verbose=True)
Exception raised:
    Traceback (most recent call last):
      File "/home/maldun/sage/sage-4.5.2/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/maldun/sage/sage-4.5.2/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/maldun/sage/sage-4.5.2/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_5[5]>", line 1, in <module>
        random_expr(Integer(5), verbose=True)###line 239:
    sage: random_expr(5, verbose=True)
      File "/home/maldun/sage/sage-4.5.2/local/lib/python/site-packages/sage/symbolic/random_tests.py", line 254, in random_expr
        return random_expr_helper(size, internal, leaves, verbose)
      File "/home/maldun/sage/sage-4.5.2/local/lib/python/site-packages/sage/symbolic/random_tests.py", line 210, in random_expr_helper
        return r[1](*children)
      File "element.pyx", line 1529, in sage.structure.element.RingElement.__div__ (sage/structure/element.c:11992)
      File "coerce.pyx", line 713, in sage.structure.coerce.CoercionModel_cache_maps.bin_op (sage/structure/coerce.c:6126)
      File "element.pyx", line 1527, in sage.structure.element.RingElement.__div__ (sage/structure/element.c:11973)
      File "expression.pyx", line 2269, in sage.symbolic.expression.Expression._div_ (sage/symbolic/expression.cpp:11444)
    ZeroDivisionError: Symbolic division by zero
**********************************************************************
2 items had failures:
   1 of   4 in __main__.example_0
   2 of   6 in __main__.example_5
***Test Failed*** 3 failures.
For whitespace errors, see the file /home/maldun/.sage//tmp/.doctest_random_tests.py
         [7.7 s]
 
----------------------------------------------------------------------
The following tests failed:


        sage -t -long "devel/sage/sage/symbolic/random_tests.py"
Total time for all tests: 7.8 seconds
```


I quite understand these, because we have introduced new functions, but I don't understand the exception in the last one


```
sage -t -long "devel/sage/sage/symbolic/pynac.pyx"          
**********************************************************************
File "/home/maldun/sage/sage-4.5.2/devel/sage/sage/symbolic/pynac.pyx", line 386:
    sage: get_sfunction_from_serial(i) == foo
Expected:
    True
Got:
    False
**********************************************************************
File "/home/maldun/sage/sage-4.5.2/devel/sage/sage/symbolic/pynac.pyx", line 388:
    sage: py_latex_function_pystring(i, (x,y^z))
Expected:
    'my args are: x, y^z'
Got:
    '\\mathrm{bar}\\left(x, y^{z}\\right)'
**********************************************************************
File "/home/maldun/sage/sage-4.5.2/devel/sage/sage/symbolic/pynac.pyx", line 478:
    sage: get_sfunction_from_serial(i) == foo
Expected:
    True
Got:
    False
**********************************************************************
File "/home/maldun/sage/sage-4.5.2/devel/sage/sage/symbolic/pynac.pyx", line 480:
    sage: py_print_fderivative(i, (0, 1, 0, 1), (x, y^z))
Expected:
    D[0, 1, 0, 1]func_with_args(x, y^z)
Got:
    D[0, 1, 0, 1](foo)(x, y^z)
**********************************************************************
File "/home/maldun/sage/sage-4.5.2/devel/sage/sage/symbolic/pynac.pyx", line 540:
    sage: get_sfunction_from_serial(i) == foo
Expected:
    True
Got:
    False
**********************************************************************
File "/home/maldun/sage/sage-4.5.2/devel/sage/sage/symbolic/pynac.pyx", line 542:
    sage: py_latex_fderivative(i, (0, 1, 0, 1), (x, y^z))
Expected:
    D[0, 1, 0, 1]func_with_args(x, y^z)
Got:
    D[0, 1, 0, 1]\left(\mathrm{bar}\right)\left(x, y^{z}\right)
**********************************************************************
3 items had failures:
   2 of  19 in __main__.example_14
   2 of  14 in __main__.example_16
   2 of  18 in __main__.example_18
***Test Failed*** 6 failures.
For whitespace errors, see the file /home/maldun/.sage//tmp/.doctest_pynac.py
         [7.3 s]
 
----------------------------------------------------------------------
The following tests failed:


        sage -t -long "devel/sage/sage/symbolic/pynac.pyx"
Total time for all tests: 7.3 seconds
```


And these are really strange, because when I type then into sage by hand everything works. wtf??
Can anyone have a look at these?


---

Comment by maldun created at 2010-09-05 10:30:07

ortho polys with scipy support


---

Comment by maldun created at 2010-10-03 00:49:32

Changing status from needs_review to needs_work.


---

Attachment


---

Comment by kcrisman created at 2010-10-15 18:42:08

Just cc:ing myself by commenting.  

Also, there seems to be a lot of stuff in the latest Python file that is the same as the original one (in terms of explanation, not code).  Maybe posting an updated patch (once the numpy/scipy-fest is over, which is hopefully the case) would help some of us figure this out.  Thanks for working on this - there is still a lot of overhauling that symbolics could use, but this is a great step.


---

Comment by maldun created at 2010-10-15 23:31:17

`@`kcrisman thanks for paying attention. I added now an updated patch and extended instructions.

the doctest changes in *symbolic.random_tests.py* are easy to explain: new functions are involved -> new random expressions. But I had to change
`random_expr(50, nvars=3, coeff_generator=CDF.random_element) ` to `random_expr(60, nvars=3, coeff_generator=CDF.random_element) ` or else one gets an expression generated where a division through zero occours.

As mentioned on sage-devel I repaired the doctests in *symbolic.pynac.pyx*, the trick is to enlarge the range of the for loop:
`for i in range(get_ginac_serial(), get_ginac_serial()+50):`
changed to
`for i in range(get_ginac_serial(), get_ginac_serial()+100):`
now it works. My explaination: since we have new functions we have longer to search, and then we reach our goal. What I can not explain is, that it works, when I type it in by hand.

All doctests pass now, so I think a review would be nice.

-maldun


---

Comment by maldun created at 2010-10-15 23:31:17

Changing status from needs_work to needs_review.


---

Comment by maldun created at 2010-10-15 23:55:00

Cleaned up discription of the ticket and some comments in the ortho polys file.


---

Comment by kcrisman created at 2010-10-16 03:27:13

I don't have time to review this for a while, but did take a quick look - thanks for polishing that patch!  I don't think we are allowed to import numpy or scipy like that anymore, but rather have to do it in an individual function (lest startup times get huge).  I don't quite understand exactly how that works, but anyway such a blanket import statement probably isn't appropriate, the way I understand what others have said.


---

Comment by maldun created at 2010-10-16 12:53:19

Latest version of orthogonal polys with scipy support, and changed doctests. Tested in sage-4.6.alpha3


---

Attachment

Replying to [comment:30 kcrisman]:
> I don't have time to review this for a while, but did take a quick look - thanks for polishing that patch!  I don't think we are allowed to import numpy or scipy like that anymore, but rather have to do it in an individual function (lest startup times get huge).  I don't quite understand exactly how that works, but anyway such a blanket import statement probably isn't appropriate, the way I understand what others have said.  

But thanks for giving feedback! I know that this patch isn't easy for review because the code grew from 650 to about 2300 lines of code. But I'm happy to get at least some info.

You are right the imports didn't change since I started this ticket and importing the whole numpy and scipy packages is to much. This isn't a very good Idea if one thinks about performance either.  I changed that now so that only functions that are really needed are importet. I did this also for mpmath but the problem with the global import remains.
(see above). Also changed some errors in the discription I missed and repaired a wrong doctest.

PS: If diffs or more changelogs are needed let me know. I'm keeping track with git on my machine of the changes.


---

Comment by burcin created at 2010-10-16 15:38:16

Changing status from needs_review to needs_work.


---

Comment by burcin created at 2010-10-16 15:38:16

Great work Stefan. Your patch looks good overall, but it needs a lot of polish. Thank you very much for this.

Here are some quick comments after reading attachment:trac_9706_orthogonal_polys.patch. I didn't try to apply and run the code yet. It would be better if other people try this as well since I am really short on time these days.

 * I suggest you use your real name in the HG headers. This information is used for copyright/license issues as well. In the future it might cause a lot of trouble if people have to chase down `maldun` for copyright questions.
 * You shouldn't import any part of `numpy` at the module level. This slows down startup too much. See #3561 for example. I'd say the same holds for `mpmath` and `scipy`.
 * line 385-386 has this:

```
Then after using one of these functions, it changes:: (The value is now  
False for chebyshev_T because chebyshev_T uses clenshaw method instead...)
```

 I don't think this is valid Sphinx.
 * delete line 412

```
#load /home/maldun/sage/sage-4.5.2/devel/sage-ortho/sage/functions/orthogonal_polys.py 
```

 * line 419: he -> the
 * There are no doctests for the `OrthogonalPolynomial` class, make sure your file passes `sage -coverage`
 * The commented timings in the docstring of `OrthogonalPolynomial._clenshaw_method_()` are confusing. It would be better if you provide a function in the same file that does these timings automatically and prints out the results. You should at least delete this from the documentation though.
 * In the docstring of `OrthogonalPolynomial._eval_()`
   * remove the empty first line (line 494) of
   * remove the commented out timings as well
   * you need an empty line after `EXAMPLES::`
   * the empty last line should be removed
 * add some comments to the `OrthogonalPolynomial._eval_()` method to indicate what you're trying to do with these tests.
   * lines 583-593 have a confusing comment and a bug

```
try: 
    #s = maxima(self._maxima_init_evaled_(*args)) 
    #This above is very inefficient! The older 
    #methods were much faster... 
    return self._maxima_init_evaled_(*args) 
except TypeError: 
    return None 
if self._maxima_name in repr(s): 
    return None 
else: 
    return s.sage() 
```

 * You don't need to state "Class for" on line 598, "The Chebyshev ..." is enough.
 * Why do you delete the `chebyshev_T(2,x)` test on line 371? You can just add the new ones after that.
 * line 626, `EXAMPLES:` -> `EXAMPLES::`
 * Don't use `*args` or `**kwds` when you don't need them. Name the arguments and be explicit. Remember the "Zen of Python", "Explicit is better than implicit."
 * OK, generally, fix the docstrings to conform to Sphinx standards. This should be documented somewhere in the developers guide.
 * line 673, `_maxima_init_evaled_()` doesn't have doctests.
 * line 678 - , `_clenshaw_method_()`
   * docstring is not indented properly.
   * It would be better to put the recursion formula in the docstring.
 * line 790 `_clenshaw_method_()` doesn't have doctests.
 * There is something wrong with the `_maxima_init_evaled_()` on line 821. Are you sure this function shouldn't just return a string to be run in maxima? How do we know that doctest actually calls this function? In any case, the right way to convert a maxima object to sage is to run `.sage()` on it. Never use `sage_eval()` on a string in the Sage library.
 * Calls to mpmath should be able to use the precision directly from the type of the argument now. Are you sure all this is necessary:

```
try: 
    step_parent = kwds['parent'] 
except KeyError: 
    step_parent = parent(args[-1]) 

try: 
    precision = step_parent.prec() 
except AttributeError: 
    precision = RR.prec() 
```

 See #9566.
 * line 924, change the error message to something more professional. "Derivative w.r.t. to the index is not supported, yet, and perhaps never will be..." is not acceptable. "Derivatives with respect to the index is not supported." would be enough.
 * Document the derivative formula in the docstring, using proper math notation
 * What needs to be discussed from the comments on line 968-974?
 * Same for lines 1058-1060?
 * no doctests for `_clenshaw_method_()` on line 1156.
 * no doctests for `_maxima_init_evaled_()` on line 1189.

I give up at this point. It seems that there are similar issues in the rest of the file as well.

After you clean up the code according to the comments above, perhaps a native English speaker like Karl-Dieter or Minh can help with the documentation.

Thanks again for all your work.


---

Comment by maldun created at 2013-11-09 22:29:50

Hi!

I will now retry to build the new orthogonal polynomials.
The last time I ran out of time due to my phd studies/theses
this time i will split the changes up into several patches. So it will be easier to 
apply the changes step by step, and the review process gets simpler.

Hope this time everything will work out!


---

Comment by maldun created at 2013-11-09 22:30:36

Changing status from needs_work to needs_review.


---

Comment by tscrim created at 2013-11-23 07:58:00

Here is a review patch which does a bunch of documentation formatting tweaks. There are probably one or two other things that will need to be addressed, but I'd like to get the ball rolling on this again (and I need some sleep right now).

Best,

Travis

For patchbot:

Apply: trac_9706_chebyshev.patch​, trac_9706-review-ts.patch


---

Comment by maldun created at 2013-11-29 16:44:09

Thanks for reviewing. It would be great if the new Chebyshev Polynomials could be added. If this ticket is done I will open the next issue and start working on the Legendre Polynomials


---

Comment by tscrim created at 2013-12-02 23:45:29

Okay, I've done a few other tweaks and I'd okay with it. If you're happy with my changes, then go ahead and set this to positive review.

For patchbot:

Apply: trac_9706_chebyshev.patch​, trac_9706-review-ts.patch


---

Comment by maldun created at 2013-12-03 12:15:58

Changing status from needs_review to positive_review.


---

Comment by maldun created at 2013-12-03 12:15:58

Thanks for your hard work in correcting all those small mistakes!

I'm very happy, that finally the new ortho polys are going into sage!


---

Comment by kcrisman created at 2013-12-03 16:07:49

I'm elevating Travis to an author because these are quite substantial review changes - thanks for being so meticulous on the formatting etc!

I'd love one final check from either of you.  There are a lot of imports added; I think most should be okay but the Maxima-related ones scare me, so if you can just check that startup time hasn't budged more than a couple milliseconds, that would be helpful.  I don't think this should import numpy, at least!


---

Comment by jdemeyer created at 2013-12-03 17:12:07

Sorry to spoil the party, but this is a regression:

```
sage: K.<a> = NumberField(x^3-x-1)
sage: chebyshev_T(10^3,a)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-17-aa97c56dd147> in <module>()
----> 1 chebyshev_T(Integer(10)**Integer(3),a)

/usr/local/src/sage-5.13.beta1/local/lib/python2.7/site-packages/sage/symbolic/function.so in sage.symbolic.function.BuiltinFunction.__call__ (sage/symbolic/function.cpp:8126)()

/usr/local/src/sage-5.13.beta1/local/lib/python2.7/site-packages/sage/symbolic/function.so in sage.symbolic.function.Function.__call__ (sage/symbolic/function.cpp:5279)()

TypeError: cannot coerce arguments: no canonical coercion from Number Field in a with defining polynomial x^3 - x - 1 to Symbolic Ring
```


(and yes: Chebyshev polynomials are important in number theory)


---

Comment by jdemeyer created at 2013-12-03 17:12:15

Changing status from positive_review to needs_work.


---

Comment by jdemeyer created at 2013-12-03 17:18:56

I would also like to point out that PARI is faster at evaluating Chebyshev polynomials:

```
sage: timeit('''chebyshev_T(10^5,2)''')
5 loops, best of 3: 270 ms per loop
sage: timeit('''pari('polchebyshev (10^5,1,2)')''')
625 loops, best of 3: 447 µs per loop
```



```
sage: timeit('''chebyshev_T(10^5, Mod(2,1009))''')
5 loops, best of 3: 208 ms per loop
sage: timeit('''pari('polchebyshev(10^5, 1, Mod(2,1009))')''')
625 loops, best of 3: 11.5 µs per loop
```


We should definately use PARI to evaluate Chebyshev polynomials for certain types of input.


---

Comment by jdemeyer created at 2013-12-03 17:19:11

Another regression:

```
sage: parent(chebyshev_T(10^2, RIF(2)))
Real Field with 53 bits of precision
```



---

Comment by jdemeyer created at 2013-12-03 17:29:00

The "Clenshaw method" uses a very naive method of evaluating the recursion which needs `O(n)` steps, while there is a much faster method (which compute `T_2n` and `U_2n` in function of `T_n` and `U_n`) which only needs `O(log(n))` steps.

Even this is totally feasible:

```
sage: timeit('''pari('polchebyshev(10^10, 1, Mod(2,1009))')''')
625 loops, best of 3: 16.3 µs per loop
```



---

Comment by jdemeyer created at 2013-12-03 17:32:45

This is also bad:

```
sage: R.<x> = QQ[]
sage: parent(chebyshev_T(5, x))
Symbolic Ring
```



---

Comment by jdemeyer created at 2013-12-03 17:35:24

Another suggestion: why not make the base class more general and call it `SymbolicPolynomial`? I think that's a more natural class of functions, which could (in the future) also include cyclotomic polynomials for example.


---

Comment by jdemeyer created at 2013-12-03 17:42:30

I propose the logic for evaluating `chebyshev_T(n, x)` should be:
 1. if `x` is symbolic, then use the method of the current patch.
 2. if `x` is not symbolic, try evaluation using PARI.
 3. if conversion to PARI fails (for example for `RIF`), use an efficient `O(log(n))` recursion algorithm.


---

Comment by fredrik.johansson created at 2013-12-03 18:08:57

Jeroen: do you know a reference for the recursion pari uses?


---

Comment by jdemeyer created at 2013-12-03 20:30:50

Replying to [comment:50 fredrik.johansson]:
> Jeroen: do you know a reference for the recursion pari uses?
No, but it's pretty straight-forward (think doubling formulas for `cos` and `sin`).


---

Comment by maldun created at 2013-12-04 07:47:43

Thank you all for the input! I think it is still a good idea that I only implement chebychev polys for now, since there are a lot of improvements out there.

`@`jdemeyer

`@`Bugs I will look into this. And yes I'm aware that Chebyshev Polynomials are important to number theory since there are quite interesting generalizations on general fields.

`@`Clenshaw: PARI is a good hint, I will look into this. And I already think I know how to generalize the clenshaw method, to get O(log N). 
The reason for this quite naive choice, was that the method can be applied to all ortho polys. Nevertheless I will adapt it on Chebychev Polys since there are more possibilities since we can use trigonometric formulas. I think the benefit of implementing it directly in sage is that there is less trouble if one wants to use more general data types, since there are no type casts. I will try to find an optimal way for this. (Maybe an additional switch)

`@`SymbolicPolynomial: I don't think this is a good idea because ortho polys are quite special even among the polynomials. But If you really would like to have a SymbolicPolynomial class I would propose to introduce the SymbolicPolynomial class, and derive the OrthogonalPolynomials from that class.
I make the following suggestion: I will finish the OrthogonalPolynomials with the current design. And then open an new ticket where we discuss the design of a general polynomial parent class. Fortunately, such design changes are very easy to implement in Python, and I don't see any big problem in introducing an intermediate class.
But if you want to introduce such a class there are some major decisions to make:
-Where do we put this class? (such a general class should not belong to orthogonoal_polys.py )
-What should all SymbolicPolynomials have in common?
-What should they have concerning other general polynomials?

But it would be really good to add the ortho polys, and I really want to finish this task.


---

Comment by jdemeyer created at 2013-12-04 08:38:33

> `SymbolicPolynomial`: I don't think this is a good idea because ortho polys are quite special even among the polynomials.
What's special about orthogonal polynomials from a *computer algebra* point of view? I can tell you that "symbolic polynomials" are special because you generally want to be able to evaluate them for any ring element (as opposed to other symbolic functions, which often only make sense in real or complex fields).

> I make the following suggestion: I will finish the OrthogonalPolynomials with the current design.
Sure...


---

Comment by maldun created at 2013-12-04 09:08:49

Replying to [comment:53 jdemeyer]:
> > `SymbolicPolynomial`: I don't think this is a good idea because ortho polys are quite special even among the polynomials.
> What's special about orthogonal polynomials from a *computer algebra* point of view? I can tell you that "symbolic polynomials" are special because you generally want to be able to evaluate them for any ring element (as opposed to other symbolic functions, which often only make sense in real or complex fields).
> 

It makes a difference in an *OO-Design* point of view, because you can apply a whole bunch of evaluation techniques and tricks due to the three term recursion (e.g. clenshaw method or the eval_numpy method are not needed for symbolic polynomials, since there are no methods for that). Thats the reason why I suggested to derive them from a base class on top to avoid redundant methods. That would be a clean solution. And I'm already thinking on some features, which I want to implement in future version, which are very specific to ortho polys. And if you want to introduce such a general class, you should not put it into orthogonal_polys.py, but somewhere else, were it fits better into the class hierarchy.

Please don't get me wrong, I'm not stating, that I think it is a bad idea to introduce such an abstract base class, but If you want a clean OO Design, it is not done by a simple renaming.


---

Comment by jdemeyer created at 2013-12-04 09:14:39

Evaluating `chebyshev_T(n,x)` can be done as

```
(Matrix(2,2,[x,x^2-1,1,x])^n)[0,0]
```


While `chebyshev_U(n-1,x)` equals

```
(Matrix(2,2,[x,x^2-1,1,x])^n)[1,0]
```


These can be evaluated with `O(log(n))` operations.


---

Comment by jdemeyer created at 2013-12-04 09:16:03

Replying to [comment:54 maldun]:
> And I'm already thinking on some features, which I want to implement in future version, which are very specific to ortho polys.
That alone is a very good to keep the `OrthogonalPolynomial` class.


---

Comment by maldun created at 2013-12-04 09:24:30

Replying to [comment:55 jdemeyer]:
> Evaluating `chebyshev_T(n,x)` can be done as
> {{{
> (Matrix(2,2,[x,x<sup>2-1,1,x])</sup>n)[0,0]
> }}}
> 
> While `chebyshev_U(n-1,x)` equals
> {{{
> (Matrix(2,2,[x,x<sup>2-1,1,x])</sup>n)[1,0]
> }}}
> 
> These can be evaluated with `O(log(n))` operations.

Thanks for the hint. I have also an own idea to implement this. My implementation   should be optimal with respect to the flop count, but yours could be faster since matrix multiplication and powers are well optimized. I will compare both methods and use the faster one.

For reference: The method which I mean is based on the generalized recursion formula (originating from the cosine addition theorem): 
T_{n+m} + T{n-m} = 2 T_n T_m 

For T_N one can now use the binary representation of N to recursively build T_N in O(log N) time


---

Comment by jdemeyer created at 2013-12-04 11:59:36

This should be a `ValueError`:

```
sage: chebyshev_T(1/2,0)
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-7-830f13ad2f0d> in <module>()
----> 1 chebyshev_T(Integer(1)/Integer(2),Integer(0))

/usr/local/src/sage-5.13.beta1/local/lib/python2.7/site-packages/sage/symbolic/function.so in sage.symbolic.function.BuiltinFunction.__call__ (sage/symbolic/function.cpp:8126)()                                                                                                                                                               

/usr/local/src/sage-5.13.beta1/local/lib/python2.7/site-packages/sage/symbolic/function.so in sage.symbolic.function.Function.__call__ (sage/symbolic/function.cpp:5531)()                                                                                                                                                                      

/usr/local/src/sage-5.13.beta1/local/lib/python2.7/site-packages/sage/functions/orthogonal_polys.pyc in _eval_(self, *args)
    489                 if not is_Expression(args[-1]):
    490                     try:
--> 491                         return self._evalf_(*args)
    492                     except AttributeError:
    493                         pass

/usr/local/src/sage-5.13.beta1/local/lib/python2.7/site-packages/sage/functions/orthogonal_polys.pyc in _evalf_(self, *args, **kwds)
    606             precision = step_parent.prec()
    607         except AttributeError:
--> 608             precision = RR.prec()
    609 
    610         from sage.libs.mpmath.all import call as mpcall

NameError: global name 'RR' is not defined
```



---

Comment by jdemeyer created at 2013-12-04 12:01:50

This should be `ArithmeticError` (I guess), since deriving w.r.t. the index simply isn't defined:

```
sage: var('n,x')
(n, x)
sage: chebyshev_T(n,x).diff(n)
---------------------------------------------------------------------------
NotImplementedError                       Traceback (most recent call last)
<ipython-input-14-a23f5209eb49> in <module>()
----> 1 chebyshev_T(n,x).diff(n)

/usr/local/src/sage-5.13.beta1/local/lib/python2.7/site-packages/sage/symbolic/expression.so in sage.symbolic.expression.Expression.derivative (sage/symbolic/expression.cpp:16561)()

/usr/local/src/sage-5.13.beta1/local/lib/python2.7/site-packages/sage/misc/derivative.so in sage.misc.derivative.multi_derivative (sage/misc/derivative.c:2715)()

/usr/local/src/sage-5.13.beta1/local/lib/python2.7/site-packages/sage/symbolic/expression.so in sage.symbolic.expression.Expression._derivative (sage/symbolic/expression.cpp:16951)()

/usr/local/src/sage-5.13.beta1/local/lib/python2.7/site-packages/sage/functions/orthogonal_polys.pyc in _derivative_(self, *args, **kwds)
    714         diff_param = kwds['diff_param']
    715         if diff_param == 0:
--> 716             raise NotImplementedError("derivative w.r.t. to the index is not supported yet")
    717 
    718         return args[0]*chebyshev_U(args[0]-1,args[1])

NotImplementedError: derivative w.r.t. to the index is not supported yet
```


Also: doctest your exceptions.


---

Comment by jdemeyer created at 2013-12-04 12:07:52

I personally like to define `chebyshev_T(-n,x) = chebyshev_T(n,x)` and `chebyshev_U(-n,x) = -chebyshev_U(n-2,x)`. This makes sense from a number-theoretic point of view and is also consistent with `chebyshev_T(n,cos(x)) = cos(n*x)` and `chebyshev_U(n-1,cos(x)) = sin(n*x)/sin(x)`.


---

Comment by jdemeyer created at 2013-12-04 14:42:23

For real/complex fields, you should use

```
chebyshev_T(n,x) = ((x+sqrt(x^2-1))^n + (x-sqrt(x^2-1))^n)/2
chebyshev_U(n-1,x) = ((x+sqrt(x^2-1))^n - (x-sqrt(x^2-1))^n)/(2*sqrt(x^2-1))
```



---

Comment by fredrik.johansson created at 2013-12-04 15:06:49

The doubling recursion formulas should be better also for real/complex fields, I think: computing nth powers is basically the same amount of work, and it's best to avoid the square roots (especially for real |x| < 1).


---

Comment by jdemeyer created at 2013-12-04 15:16:43

Replying to [comment:62 fredrik.johansson]:
> The doubling recursion formulas should be better also for real/complex fields, I think: computing nth powers is basically the same amount of work, and it's best to avoid the square roots (especially for real |x| < 1).
The matrix algorithm does seem more numerically stable (checked by using both algorithms inside `RIF`). So it's easy then, if there is one algorithm which is obviously the best.


---

Comment by maldun created at 2013-12-04 15:33:48

I found an interesting paper on this topic: [http://www.mathematik.uni-kassel.de/~koepf/cheby.pdf](http://www.mathematik.uni-kassel.de/~koepf/cheby.pdf)

Maybe this could give some input to the discussion.

It states that for an expanded representation the approach I have
initally chosen (series expansion) should be the best for the symbolic
evaluation, since this is somehow that what the user expects from ohter CAS.
However, the proposed recursive/symbolic method would be interesting too.
(p16f), since it gives a more compact form for large n. Maybe a switch for 
n >= 100?

Considering rational numbers as input, the recursion formula works best, due to this paper. This should be considered too.

`@`Matrix Multiplication: It's also my favorite, but I will compare first.


---

Comment by fredrik.johansson created at 2013-12-04 16:45:02

Here is an implementation of the divide-and-conquer algorithm that doesn't require caching (it only makes one recursive call). It might look even nicer if one rewrites it in iterative form. I think it's also equivalent to the code in pari. It should be faster than matrix powering by a constant factor, just like the analogous Fibonacci number algorithms.


```
def chebyshev_t(n, x):
    # returns (T(n,x), T(n-1,x)), or (T(n,x), _) if both=False
    def recur(n, x, both=False):
        if n == 0:
            return 1, x
        if n == 1:
            return x, 1
        a, b = recur((n+1)//2, x, both or n % 2)
        if n % 2 == 0:
            return 2*a^2 - 1, both and 2*a*b - x
        else:
            return 2*a*b - x, both and 2*b^2 - 1
    return recur(n, x, False)[0]
```


Come to think of it, it might even be useful to publicly expose a method that returns both T(n,x) and T(n-1,x) simultaneously.

Similar code for U (using same algorithm as Pari):


```
def chebyshev_u(n, x):
    def recur(n, x, both=False):
        if n == 0:
            return 1, both and 2*x
        if n == 1:
            return 2*x, both and 4*x^2-1
        a, b = recur((n-1)//2, x, True)
        if n % 2 == 0:
            return (b+a)*(b-a), both and 2*b*(x*b-a)
        else:
            return 2*a*(b-x*a), both and (b+a)*(b-a)
    return recur(n, x, False)[0]
```


Edit: streamlined the code.


---

Comment by maldun created at 2013-12-04 19:46:44

I think your recursive implementation is very good. If you try to implement it iteratively, you have to consider some cases (current in row even/odd and next in row even/odd), and the code gets quite ugly in my opinion. And I think Knuth is right. One should prefer readable code over over optimzed "faster" code...


---

Comment by maldun created at 2013-12-04 20:39:45

this would be a functioning iterative algorithm:



```
def chebyshev_t(n,x):
    
    if n == 0:
        return 1
    elif n == 1:
        return x
    elif n == 2:
        return 2*x**2-1
    else:
        T_c = x
        T_p = 2*x**2 -1
        
        for k in range(floor(log(n,2)),0,-1):
            T_p_old = T_p
            T_c_old = T_c
            if (n//2**(k-1)) % 2 == 0: # next is even
                T_p = 2*T_p_old*T_c_old - x
                T_c = 2*T_c_old**2 - 1
            elif (n//2**(k-1)) % 2  == 1: # next is odd
                T_p = 2*T_p_old**2 - 1
                T_c = 2*T_p_old*T_c_old - x
        
        # Cases for output
        if log(n - 1,2) in ZZ or log(n-2,2) in ZZ:
            return T_c
        
        elif n % 2 == 0:
            if n//2 % 2 == 0:                   
                return T_c
            else:
                return T_p
        elif n % 2 == 1:
            if n//2 % 2 == 0:                   
                return T_p
            else:
                return T_c
```


I made it shorter. What is preferable? recursive or iterative? Normaly iterative, but in this case it is longer due to the indices battles ...

Edit: I also measured time: recursive is faster, even if I do some optimization (e.g. xrange)


---

Comment by maldun created at 2013-12-04 22:01:05

Replying to [comment:42 jdemeyer]:
> Sorry to spoil the party, but this is a regression:
> {{{
> sage: K.<a> = NumberField(x^3-x-1)
> sage: chebyshev_T(10^3,a)
> ---------------------------------------------------------------------------
> TypeError                                 Traceback (most recent call last)
> <ipython-input-17-aa97c56dd147> in <module>()
> ----> 1 chebyshev_T(Integer(10)**Integer(3),a)
> 
> /usr/local/src/sage-5.13.beta1/local/lib/python2.7/site-packages/sage/symbolic/function.so in sage.symbolic.function.BuiltinFunction.__call__ (sage/symbolic/function.cpp:8126)()
> 
> /usr/local/src/sage-5.13.beta1/local/lib/python2.7/site-packages/sage/symbolic/function.so in sage.symbolic.function.Function.__call__ (sage/symbolic/function.cpp:5279)()
> 
> TypeError: cannot coerce arguments: no canonical coercion from Number Field in a with defining polynomial x^3 - x - 1 to Symbolic Ring
> }}}
> 
> (and yes: Chebyshev polynomials are important in number theory)

I had now a look on these regressions: The problem originates from the fact, tat the ortho polys are now symbolic functions instead of simple function call in maxima.
the symbolic functions have a lot more mechanisms concerning type coercions.

The only way around this would be a hack to chatch this coercion troubles, e.g.



```
def __call__(self,n,x):

    try:
        super(Func_chebyshev_T,self).__call__(n,x)
    except TypeError:
        return self._clenshaw_method_(n,x)
```


would work for that problem and some others. But how to catch such things correctly?
Use a try catch, or make several is_instance checks? This could get a quite long list on coercions...


---

Comment by maldun created at 2013-12-04 23:30:50

new fixes and patches


---

Attachment

Replying to [comment:68 maldun]:
> would work for that problem and some others. But how to catch such things correctly?

I think there are only two cases: the "symbolic" case and the "algebraic" case. The latter means that we really consider the polynomial as a polynomial, not a symbolic function. In `chebyshev(n,x)`, if either `n` or `x` is symbolic, we are in the symbolic case, otherwise we're in the algebraic case. In the algebraic case, the index `n` must be a concrete integer and we use the iterative algorithm.


---

Comment by jdemeyer created at 2013-12-04 23:53:48

maldun: I don't like all the log's in your approach (I don't think you need them), but otherwise I'm happy with either the recursive or iterative approach.


---

Comment by maldun created at 2013-12-05 08:17:51

Replying to [comment:69 jdemeyer]:
> Replying to [comment:68 maldun]:
> > would work for that problem and some others. But how to catch such things correctly?
> 
> I think there are only two cases: the "symbolic" case and the "algebraic" case. The latter means that we really consider the polynomial as a polynomial, not a symbolic function. In `chebyshev(n,x)`, if either `n` or `x` is symbolic, we are in the symbolic case, otherwise we're in the algebraic case. In the algebraic case, the index `n` must be a concrete integer and we use the iterative algorithm.

Thank you for the input, that's a great idea!

Based on that I propose the following switch:



```
def __call__(self,n,x):
    if n in ZZ: # check if n is integer -> consider polynomial as algebraic structure
        self._eval_(n,x) # Let eval methode decide which is best
    else:
        super(OrthogonalPolynomial,self).__call__(n,x)
```



---

Comment by jdemeyer created at 2013-12-05 08:43:18

I think that `chebyshev_T(1/2, 2)` should raise a `ValueError` (or can we make sense of this?). So, in your code there should really be 3 cases: integer, symbolic and "something else" which is always an error.

So, I would do something like

```
def __call__(self,n,x):
    if is_Expression(n):
        return super(OrthogonalPolynomial, self).__call__(n,x)
    # We consider the polynomial really as a polynomial,
    # not a symbolic expression.
    try:
        n = ZZ(n)
    except StandardError:
        raise ValueError("Index for symbolic polynomials must be an integer")
    return self._eval_polynomial(n, x)
```



---

Comment by maldun created at 2013-12-05 08:54:31

Replying to [comment:70 jdemeyer]:
> maldun: I don't like all the log's in your approach (I don't think you need them), but otherwise I'm happy with either the recursive or iterative approach.

I removed the logs, it is much faster now, but still slower than the recursive implementation about a constant factor of 2 (which is not much considering that we are talking about µs, but still)


---

Comment by maldun created at 2013-12-05 09:06:11

Replying to [comment:72 jdemeyer]:
> I think that `chebyshev_T(1/2, 2)` should raise a `ValueError` (or can we make sense of this?). So, in your code there should really be 3 cases: integer, symbolic and "something else" which is always an error.
> 
> So, I would do something like
> {{{
> def __call__(self,n,x):
>     if is_Expression(n):
>         return super(OrthogonalPolynomial, self).__call__(n,x)
>     # We consider the polynomial really as a polynomial,
>     # not a symbolic expression.
>     try:
>         n = ZZ(n)
>     except StandardError:
>         raise ValueError("Index for symbolic polynomials must be an integer")
>     return self._eval_polynomial(n, x)
> }}}

No there are several other cases to consider: You can also have complex and real input values if you consider a chebyshev polynomial as extension of the Hypergeometric function 1F2 like mpmath does: [http://mpmath.googlecode.com/svn/trunk/doc/build/functions/orthogonal.html#chebyt](http://mpmath.googlecode.com/svn/trunk/doc/build/functions/orthogonal.html#chebyt)
That's the reason for the message in the _derive_ method, since it would be theoretically possible to differentiate a chebyshev polynomial with respect to the index.

So the way I proposed makes sense, since this could be important for symbolic computation purposes where hypergeometric functions play an important role (eg. Zeilberger algorithm), and of course for analytical considerations.


---

Comment by jdemeyer created at 2013-12-05 09:27:15

OK, I agree.

What remains to do:
- support [comment:60 negative indices]
- add many doctests (essentially, all the examples I mentioned on this ticket should become doctests)
- for ease of reviewing, fold all the patches into one patch.


---

Comment by maldun created at 2013-12-05 19:12:45

Patch in a whole with corrections etc.


---

Comment by maldun created at 2013-12-05 19:14:23

Changing status from needs_work to needs_review.


---

Attachment

New patch attached. I incorporated all changes discussed.

`@`Pari I tried the evaluation with pari, but with Fredericks recursion, there is no gain in speed, due to the type checks beforehand. And the recursion in sage avoid type conversions.


---

Comment by jdemeyer created at 2013-12-05 19:40:55

meldun: please adjust the "apply" section in the ticket description so it's clear which patch(es) should be applied.


---

Attachment

cheby changes


---

Comment by jdemeyer created at 2013-12-05 19:46:35

Folded the 4 patches.


---

Comment by jdemeyer created at 2013-12-05 19:50:06

What's the advantage of the `_clenshaw_method_` over the recursive method? I see no need for the two different implementations and suggest to remove `_clenshaw_method_`.


---

Comment by jdemeyer created at 2013-12-05 19:52:17

Changing status from needs_review to needs_work.


---

Comment by jdemeyer created at 2013-12-05 19:52:17

More doctests are needed, this still doesn't work:

```
sage: chebyshev_T(1/2, 0)
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-2-c142cc68c50b> in <module>()
----> 1 chebyshev_T(Integer(1)/Integer(2), Integer(0))

/usr/local/src/sage-5.13.beta1/local/lib/python2.7/site-packages/sage/functions/orthogonal_polys.pyc in __call__(self, n, x)
    554             return self._eval_(n,x) # Let eval methode decide which is best
    555         else: # Consider OrthogonalPolynomial as symbol
--> 556             return super(OrthogonalPolynomial,self).__call__(n,x)
    557 
    558 

/usr/local/src/sage-5.13.beta1/local/lib/python2.7/site-packages/sage/symbolic/function.so in sage.symbolic.function.BuiltinFunction.__call__ (sage/symbolic/function.cpp:8126)()

/usr/local/src/sage-5.13.beta1/local/lib/python2.7/site-packages/sage/symbolic/function.so in sage.symbolic.function.Function.__call__ (sage/symbolic/function.cpp:5531)()

/usr/local/src/sage-5.13.beta1/local/lib/python2.7/site-packages/sage/functions/orthogonal_polys.pyc in _eval_(self, *args)
    493                 if not is_Expression(args[-1]):
    494                     try:
--> 495                         return self._evalf_(*args)
    496                     except AttributeError:
    497                         pass

/usr/local/src/sage-5.13.beta1/local/lib/python2.7/site-packages/sage/functions/orthogonal_polys.pyc in _evalf_(self, *args, **kwds)
    641             precision = step_parent.prec()
    642         except AttributeError:
--> 643             precision = RR.prec()
    644 
    645         from sage.libs.mpmath.all import call as mpcall

NameError: global name 'RR' is not defined
```



---

Comment by jdemeyer created at 2013-12-05 20:00:04

Why do we have `__call__` and `_eval_` given they do essentially the same thing? Please keep in mind [comment:69] also in the `_eval_()` function (I really don't understand why it needs to be so complicated).

This is also still broken:

```
sage: parent(chebyshev_T(4, RIF(5)))
Real Field with 53 bits of precision
```


Please fix all issues that I mentioned *and turn them into doctests*.


---

Comment by jdemeyer created at 2013-12-05 22:35:59

For the `REFERENCES`, see [http://sagemath.org/doc/developer/conventions.html#docstring-markup-with-rest-and-sphinx](http://sagemath.org/doc/developer/conventions.html#docstring-markup-with-rest-and-sphinx) for the right syntax.


---

Comment by maldun created at 2013-12-05 23:14:40

`@`clenshaw_method: there is a difference. clenshaw method also applies a direct formula for small n and calls the recursive method else. The difference is that the recursive evaluation does not give an expanded representation of the polynomial, which is wanted for small n, because that was the standard till now and people expect this, especially if you are used to mathematica or maxima. Expanding huge expressions costs a lot of time, and this approach is much faster in that situation. Of course it is a matter of naming. But the reason why I have 2 methods, is to avoid too long code segments, and splitting them apart is better for readability. It also is important concerning other orthogonal polynomials.

`@`__call__ & _eval_ : This convention is part of the BuiltinFunction structure.
__call__ does all the stuff like coercions, transforming into a symbolic expression (e.g. if n is a symbolic value don't return a polynomial but hold the closed form.)
_eval cares about evaluating the polynomial (e.g return a number if x is a number etc.)
Look into the symbolic.function module for more details
And eval is so complicated because there are several cases to consider: correct evaluation of symbolic expressions, numerical expressions and numpy arrays etc.
This is also part of the BuiltinFunction structure. And you also have to keep in mind that this method should work for all ortho polys. 

`@`bugs Sorry, during the patch merging process I had forgotten to apply a patch, which I'm now missing, since I work on different machines ... I will correct this tomorrow.
It's annoying since I already had fixed it ...


---

Attachment

incorporated things that were already been done ...


---

Comment by maldun created at 2013-12-06 00:00:16

Ok I incorporated the bugfixes and doctests *again* ...

there are still some minor changes (formatting and new doctests) todo. Please let me know if you find more bugs.


---

Comment by jdemeyer created at 2013-12-06 10:11:44

Replying to [comment:86 maldun]:
> `@`clenshaw_method: there is a difference. clenshaw method also applies a direct formula for small n and calls the recursive method else. The difference is that the recursive evaluation does not give an expanded representation of the polynomial, which is wanted for small n
OK, fine. But for simplicity, you could simply call `_cheb_recur_(...).expand()` instead which would achieve the same thing without an additional method.

> _eval cares about evaluating the polynomial (e.g return a number if x is a number etc.)
> Look into the symbolic.function module for more details
> And eval is so complicated because there are several cases to consider: correct evaluation of symbolic expressions, numerical expressions and numpy arrays etc.
If you really think the complexity is justified (I have a hard time believing that), you should add comments in the code to describe the various cases, because I'm having a hard time understanding the logic. A comment like `# A faster check would be nice...` doesn't mean much to me because I don't understand what you're trying to do.


---

Comment by jdemeyer created at 2013-12-06 10:14:52

I think `mpmath` should only be used for the "pure" `RealField()` and `ComplexField()` and `RDF` and `CDF`, nothing else.

This is bad:

```
sage: chebyshev_T(5,Qp(3)(2))
...
TypeError: unable to coerce to a ComplexNumber: <type 'sage.rings.padics.padic_capped_relative_element.pAdicCappedRelativeElement'>
```


and the way you use `RIF` is also kind of stupid since the computation should really be done using the recursive formula.


---

Comment by jdemeyer created at 2013-12-06 10:17:52

Also, you should never simply `print` stuff. Either delete those prints or use a [Python warning](http://docs.python.org/2/library/warnings.html#available-functions).

```
sage: chebyshev_T(10^6,RealField(256)(2))
Warning: mpmath returns NoConvergence!
Switching to clenshaw_method, but it may not be stable!
1.764019427245793968639371137094247875315949668035854027376792158135922267593e571947
```


The message is also misleading, since for some inputs it retries `mpmath` anyway:

```
sage: chebyshev_T(100001/2, 2)
---------------------------------------------------------------------------
NoConvergence                             Traceback (most recent call last)
<ipython-input-34-9c95a5ff4276> in <module>()
----> 1 chebyshev_T(Integer(100001)/Integer(2), Integer(2))

/usr/local/src/sage-5.13.beta1/local/lib/python2.7/site-packages/sage/functions/ort
    557             return self._eval_(n,x) # Let eval methode decide which is best
    558         else: # Consider OrthogonalPolynomial as symbol
--> 559             return super(OrthogonalPolynomial,self).__call__(n,x)
    560 
    561 

/usr/local/src/sage-5.13.beta1/local/lib/python2.7/site-packages/sage/symbolic/function.so in sage.symbolic.function.BuiltinFp:8126)()                                                                                                                    

/usr/local/src/sage-5.13.beta1/local/lib/python2.7/site-packages/sage/symbolic/function.so in sage.symbolic.function.Function()                                                                                                                           

/usr/local/src/sage-5.13.beta1/local/lib/python2.7/site-packages/sage/functions/orth
    496                 if not is_Expression(args[-1]):
    497                     try:
--> 498                         return self._evalf_(*args)
    499                     except AttributeError:
    500                         pass

/usr/local/src/sage-5.13.beta1/local/lib/python2.7/site-packages/sage/functions/orthogonal_polys.pyc in _evalf_(self, *args, 
    651         from sage.libs.mpmath.all import chebyt as mpchebyt
    652 
--> 653         return mpcall(mpchebyt,args[0],args[-1],prec = precision)
    654 
    655     def _maxima_init_evaled_(self, *args):

/usr/local/src/sage-5.13.beta1/local/lib/python2.7/site-packages/sage/libs/mpmath/utils.so in sage.libs.mpmath.utils.call (sage/libs/

/usr/local/src/sage-5.13.beta1/local/lib/python2.7/site-packages/sage/libs/mpmath/ext_main.so in sage.libs.mpmath.ext_main.wrapped_specfun.__call__ (sage/lit_main.c:17447)()                                                                                                                                           

/usr/local/src/sage-5.13.beta1/local/lib/python2.7/site-packages/mpmath/functions/orthogonal.pyc in chebyt(ctx, n, x, **kwarg
    444     if (not x) and ctx.isint(n) and int(ctx._re(n)) % 2 == 1:
    445         return x * 0
--> 446     return ctx.hyp2f1(-n,n,(1,2),(1-x)/2, **kwargs)
    447 
    448 @defun_wrapped

/usr/local/src/sage-5.13.beta1/local/lib/python2.7/site-packages/mpmath/functions/hypergeometric.pyc in hyp2f1(ctx, a, b, c, z, **kwargs)
    248 @defun
    249 def hyp2f1(ctx,a,b,c,z,**kwargs):
--> 250     return ctx.hyper([a,b],[c],z,**kwargs)
    251 
    252 @defun

/usr/local/src/sage-5.13.beta1/local/lib/python2.7/site-packages/mpmath/functions/hypergeometric.pyc in hyper(ctx, a_s, b_s, z, **kwargs)
    223         elif q == 0: return ctx._hyp1f0(a_s[0][0], z)
    224     elif p == 2:
--> 225         if   q == 1: return ctx._hyp2f1(a_s, b_s, z, **kwargs)
    226         elif q == 2: return ctx._hyp2f2(a_s, b_s, z, **kwargs)
    227         elif q == 3: return ctx._hyp2f3(a_s, b_s, z, **kwargs)

/usr/local/src/sage-5.13.beta1/local/lib/python2.7/site-packages/mpmath/functions/hypergeometric.pyc in _hyp2f1(ctx, a_s, b_s, z, **kwargs)
    442     if absz <= 0.8 or (ctx.isint(a) and a <= 0 and a >= -1000) or \
    443                       (ctx.isint(b) and b <= 0 and b >= -1000):
--> 444         return ctx.hypsum(2, 1, (atype, btype, ctype), [a, b, c], z, **kwargs)
    445 
    446     orig = ctx.prec

/usr/local/src/sage-5.13.beta1/local/lib/python2.7/site-packages/mpmath/ctx_mp.pyc in hypsum(ctx, p, q, flags, coeffs, z, accurate_small, **kwargs)
    640                 mag_dict = {}
    641             zv, have_complex, magnitude = summator(coeffs, v, prec, wp, \
--> 642                 epsshift, mag_dict, **kwargs)
    643             cancel = -magnitude
    644             jumps_resolved = True

/usr/local/src/sage-5.13.beta1/local/lib/python2.7/site-packages/mpmath/libmp/libhyper.pyc in _hypsum(coeffs, z, prec, wp, epsshift, magnitude_check, **kwargs)
    319         def _hypsum(coeffs, z, prec, wp, epsshift, magnitude_check, **kwargs):
    320             return hypsum_internal(p, q, param_types, ztype, coeffs, z,
--> 321                 prec, wp, epsshift, magnitude_check, kwargs)
    322 
    323         return "(none)", _hypsum

/usr/local/src/sage-5.13.beta1/local/lib/python2.7/site-packages/sage/libs/mpmath/ext_main.so in sage.libs.mpmath.ext_main.hypsum_internal (sage/libs/mpmath/ext_main.c:24850)()

/usr/local/src/sage-5.13.beta1/local/lib/python2.7/site-packages/sage/libs/mpmath/ext_impl.so in sage.libs.mpmath.ext_impl.MPF_hypsum (sage/libs/mpmath/ext_impl.c:20614)()

NoConvergence: Hypergeometric series converges too slowly. Try increasing maxterms.
```



---

Comment by jdemeyer created at 2013-12-06 10:24:09

Don't forget to fix the `REFERENCES`.


---

Comment by jdemeyer created at 2013-12-06 13:27:04


```
sage: chebyshev_U(-1, Mod(2,5))
...
RuntimeError: maximum recursion depth exceeded
```



---

Comment by jdemeyer created at 2013-12-06 13:28:40

This is totally meaningless (this should be a `ValueError`):

```
sage: chebyshev_U(1.5, Mod(8,9))
63.8753125671848
```



---

Comment by jdemeyer created at 2013-12-06 13:42:35

`mpmath` is slower than `_cheb_recur_()`, so I think `mpmath` should be only used in cases where the index is not an integer.

Perhaps the `_eval_` logic should be
 1. `n` in `ZZ` => use recursion. If `x` is symbolic and `abs(n) <= 50`, `expand()` the result
 2. `n` or `x` symbolic => use symbolic evaluation
 3. `n` and `x` real/complex => use `mpmath`
 4. anything else => `raise ValueError`


---

Comment by jdemeyer created at 2013-12-06 13:46:24

One should be able to convert to maxima (otherwise, what's the point of introducing symbolic Chebyshev polynomials):

```
sage: var('n,x')
(n, x)
sage: maxima( chebyshev_T(n, cos(x)) )
...
TypeError: unable to convert x (=n) to an integer
```



---

Comment by maldun created at 2013-12-08 15:13:42

Replying to [comment:93 jdemeyer]:
> This is totally meaningless (this should be a `ValueError`):
> {{{
> sage: chebyshev_U(1.5, Mod(8,9))
> 63.8753125671848
> }}}

Indeed, but it's not my fault. It appears, that the BuiltinFunction calls the _eval_numpy_ method. E.g.


```
sage: csc(Mod(8,9))
1.01075621840010
```

makes no sense either but works. Maybe we should open a ticket on this?

I have worked out now a new patch, where _eval_ returns None, like expected, but still returns this numerical value. But it should be patched in the Symbolic function classes and not here.


---

Comment by maldun created at 2013-12-08 15:20:11

Replying to [comment:95 jdemeyer]:
> One should be able to convert to maxima (otherwise, what's the point of introducing symbolic Chebyshev polynomials):
> {{{
> sage: var('n,x')
> (n, x)
> sage: maxima( chebyshev_T(n, cos(x)) )
> ...
> TypeError: unable to convert x (=n) to an integer
> }}}

One of the reasons I started this rewriting buisness, was the fact, that Maxima is very limited in respect to Orthogonal polynomials. And if we consider advanced use for symbolic methods like 'Creative Telescoping' it makes perfect sense to allow a non
Maxima conform representation, since Sage symbolic capabilities don't relie on Maxima allone.


---

Comment by jdemeyer created at 2013-12-08 17:17:05

Replying to [comment:97 maldun]:
> One of the reasons I started this rewriting buisness, was the fact, that Maxima is very limited in respect to Orthogonal polynomials. And if we consider advanced use for symbolic methods like 'Creative Telescoping' it makes perfect sense to allow a non
> Maxima conform representation, since Sage symbolic capabilities don't relie on Maxima allone.
This looks like a poor excuse to me, since Maxima can deal with Chebyshev polynomials just fine. The following works:

```
sage: maxima('chebysheb_t(n,x)')
```

The fact that the conversion to Maxima doesn't work is a fault of your patch, don't blame Maxima for that.


---

Comment by jdemeyer created at 2013-12-08 17:17:45

Replying to [comment:96 maldun]:
> {{{
> sage: csc(Mod(8,9))
> 1.01075621840010
> }}}
> makes no sense either but works. Maybe we should open a ticket on this?
I agree, this is a problem.


---

Comment by maldun created at 2013-12-08 18:14:30

Replying to [comment:98 jdemeyer]:
> Replying to [comment:97 maldun]:
> > One of the reasons I started this rewriting buisness, was the fact, that Maxima is very limited in respect to Orthogonal polynomials. And if we consider advanced use for symbolic methods like 'Creative Telescoping' it makes perfect sense to allow a non
> > Maxima conform representation, since Sage symbolic capabilities don't relie on Maxima allone.
> This looks like a poor excuse to me, since Maxima can deal with Chebyshev polynomials just fine. The following works:
> {{{
> sage: maxima('chebysheb_t(n,x)')
> }}}
> The fact that the conversion to Maxima doesn't work is a fault of your patch, don't blame Maxima for that.

I'm not blaming maxima, but this never worked on the main branch in the first place:



```
maxima( chebyshev_T(n, cos(x)) )
...
TypeError: unable to convert x (=n) to an integer
```


so I did not break anything ...

You can argue that this is an open improvement, but it's definitely no regression.
Nevertheless it will be corrected in the next patch.


---

Comment by maldun created at 2013-12-08 21:04:46

Bunch of corrections and new doctests


---

Attachment

I incorporated now the things you wished for, except things for ducumentation.
I also added many new doctests.

I also cleaned up the evaluation methods.


---

Attachment

corrected name of file


---

Attachment

docu changes


---

Comment by maldun created at 2013-12-08 22:22:43

docu changes


---

Comment by maldun created at 2013-12-08 22:24:27

Changing status from needs_work to needs_review.


---

Attachment

added changes in docu.

Still one bug to fix


---

Comment by maldun created at 2013-12-08 22:27:03

Changing status from needs_review to needs_work.


---

Comment by maldun created at 2013-12-08 22:41:00

fixed bugs with chebyshev_U(-1,...)


---

Attachment

Finally fixed the chebyshev_U(-1,...) issue


---

Comment by maldun created at 2013-12-08 22:41:58

Changing status from needs_work to needs_review.


---

Comment by maldun created at 2013-12-08 23:06:11

collection of all patches


---

Attachment


---

Comment by jdemeyer created at 2013-12-09 10:59:42

Working on reviewer patch...


---

Comment by jdemeyer created at 2013-12-09 14:31:06

Changing priority from minor to major.


---

Comment by jdemeyer created at 2013-12-09 14:34:31

Review patch, mainly simplifies the code: less special cases and use actual arguments instead of `args` and `kwds`. Also add some more doctests.


---

Comment by maldun created at 2013-12-09 17:09:37

Replying to [comment:109 jdemeyer]:
> Review patch, mainly simplifies the code: less special cases and use actual arguments instead of `args` and `kwds`. Also add some more doctests.

Is it really a good idea to replace *args and **kwds in the OrthogonalPolynomial class?

Since not all ortho polys only have 2 arguments, e.g. Gegenbauer polynomials [http://en.wikipedia.org/wiki/Gegenbauer_polynomials](http://en.wikipedia.org/wiki/Gegenbauer_polynomials) which have an additional parameter alpha
It makes perfect sense for the chebyshev polys though

I know that the base class looks strange from the point of the Chebyshev polys,
but there is some reasoning behind this =)


---

Attachment

Replying to [comment:110 maldun]:
> Is it really a good idea to replace *args and **kwds in the OrthogonalPolynomial class?
> 
> Since not all ortho polys only have 2 arguments, e.g. Gegenbauer polynomials [http://en.wikipedia.org/wiki/Gegenbauer_polynomials](http://en.wikipedia.org/wiki/Gegenbauer_polynomials) which have an additional parameter alpha
> It makes perfect sense for the chebyshev polys though
Ok, it's always difficult to design an interface for something you don't have an implementation for, but I made the change such that the Gegenbauer polynomials should (in theory) work.


---

Comment by maldun created at 2013-12-09 20:10:55

Replying to [comment:111 jdemeyer]:
> Replying to [comment:110 maldun]:
> > Is it really a good idea to replace *args and **kwds in the OrthogonalPolynomial class?
> > 
> > Since not all ortho polys only have 2 arguments, e.g. Gegenbauer polynomials [http://en.wikipedia.org/wiki/Gegenbauer_polynomials](http://en.wikipedia.org/wiki/Gegenbauer_polynomials) which have an additional parameter alpha
> > It makes perfect sense for the chebyshev polys though
> Ok, it's always difficult to design an interface for something you don't have an implementation for, but I made the change such that the Gegenbauer polynomials should (in theory) work.

Maybe you should have a short look ino this patch: [http://trac.sagemath.org/attachment/ticket/9706/trac_9706_orthogonal_polys.patch](http://trac.sagemath.org/attachment/ticket/9706/trac_9706_orthogonal_polys.patch)
it contains already prototypes of the most ortho polys.

I have some remarks concerning your patch:



```
sage: chebyshev_T(n,Mod(0,8))
1/2*(-1)^(1/2*n)*((-1)^n + 1)
```

but this makes no sense since 1/2 is not defined in Mod(8). This was the reason for the 0 in CC check at this point.

You evaluate numerical expressions for n in NN with recursion. this is favorable for chebyshev polynomials, but not for all ortho polys you can evaluate numeric values in O(log n). You have already problems with the legendre polynomials, since the coefficients depend on n, and the recursion is not stable. Thus other evaluation methods should be used. Thats the reason why _evalf_ with mpmath should come first.
In case of chebyshev I catched this with an explicit call of the recursion in _evalf_.

The _old_maxima_ method is used for some oddballs, where the only useful implementation is in maxima, and for some special cases. So removing is probably not a good idea.

The reason why negative values are checked in special values, is that in later versions, or for other polys non integral negative values can be treated analogously, as in the case of their algebraic counterpart. E.g negative legendre polynomials would return associated legendre functions, but have no algebraic sense.

Another reason to allow the special values check for non symbolic input, is that e.g. (-1)^100000000 is evaluated faster, than applying the recursion, or other special points.
I use this feature sometimes to evaluate certain polynomials at the end points of an intervall e.g. [-1,1]

*Question:* Since the Legendre Polynomials already conflicts with the design in the ortho poly class, should we add legendre_P too, to get a better overview, what actually should be kept in the orthogonal poly class? then we could also add more reasonable doctests, to understand the evaluation methods better. 

I have to admit, that about 3 years have passed since I wrote the initial version, and I'm not remembering why I took some design desicisions back then, but slowly my memories are coming back.


---

Comment by jdemeyer created at 2013-12-09 20:26:11

Replying to [comment:112 maldun]:
> *Question:* Since the Legendre Polynomials already conflicts with the design in the ortho poly class, should we add legendre_P too, to get a better overview, what actually should be kept in the orthogonal poly class?
Absolutely not. The patch is already big enough now.


---

Comment by jdemeyer created at 2013-12-09 20:30:04

If the various orthogonal polynomials are so different, then perhaps the simple answer is that we shouldn't try to force a generic `_eval_` which will work for all orthogonal polynomials.

We could have a common superclass for both kinds of Chebyshev polynomials and implement `_eval_()` there. For Legendre polynomials, we could implement a different `_eval_()`. That would be a much simpler solution than making an overly complicated generic `_eval_()`.


---

Comment by tscrim created at 2013-12-09 20:47:52

Replying to [comment:114 jdemeyer]:
> If the various orthogonal polynomials are so different, then perhaps the simple answer is that we shouldn't try to force a generic `_eval_` which will work for all orthogonal polynomials.
> 
> We could have a common superclass for both kinds of Chebyshev polynomials and implement `_eval_()` there. For Legendre polynomials, we could implement a different `_eval_()`. That would be a much simpler solution than making an overly complicated generic `_eval_()`.

I think this would be a good course of action, and that we should put other orthogonal polynomials in other tickets. However, I think it might be worthwhile to at least diagram/pseudocode the overall class structure we want at the end of the day. Currently I believe the proposal is something like:

```
* Orthogonal polynomials

  * Chebyshev polynomials
    - general _evel_(x, n) method

    * Chebyshev T
      - specific code (ex. _evalf_() method), recursions, ...
    * Chebyshev U
      - specific code (ex. _evalf_() method), recursions, ...

  * Legendre polynomials
    - general _evel_(x, n) method

    * Legendre P
    * Legendre Q

  * Gegenbauer polynomials
    - an _evel_(x, n, alpha) method
```

Hopefully my notation is clear


---

Comment by jdemeyer created at 2013-12-09 21:04:25

Something like that looks right indeed. maldun: what do you think?

Perhaps the only code so far that could be truly generic is the `__call__` method.


---

Comment by jdemeyer created at 2013-12-09 21:04:34

Something like that looks right indeed. maldun: what do you think?

Perhaps the only code so far that could be truly generic is the `__call__` method.


---

Comment by maldun created at 2013-12-09 21:21:56

after some thinking, I guess you are right. A General OrthogonalPolynomial is sophisticated, but it needs too much tweaking, and too much exception cathing, which makes the code unsafe.

`@` __call__ : I'm not even sure about that, since we check for negative integers, but some ortho polys get only an analytical expression with non negative integers, and no algebraic meaning.

I propose the following

* OrthogonalPolynomial: Naming Conventions and __init__ method
* ChebyshevPolynomial: base Class for Cheby_t and Cheby_u (Current Orthogonal Polynomials)
* LegendrePolynomials
.... etc.


---

Attachment

proposed new structure


---

Comment by maldun created at 2013-12-11 06:01:54

I added an intermediate class between OrthogonalPolynomials and the Chebyshev polynomals namely ChebyshevPolynomial.

Any comments on that?


---

Comment by tscrim created at 2013-12-11 06:38:40

Sorry for lagging behind on reviewing this, but I think the class structure is good. I'll write a small review patch tomorrow afternoon (in the US Pacific timezone) on a few tweaks (and pet peeves of mine).


---

Comment by jdemeyer created at 2013-12-11 07:22:50

I am currently working on finishing the Sage 5.13 release, so I don't feel like reviewing this now.


---

Comment by tscrim created at 2013-12-11 22:57:33

Okay, I've made the tweaks I wanted to. So it's a positive review from me, and someone will just need to review my changes.


---

Comment by maldun created at 2013-12-12 19:28:30

Okay thanks. I set it on positive review then.
And good idea to replace the old % format string operator, since it will be deprecated in Python 3 (although I will miss it ...)


---

Comment by maldun created at 2013-12-12 19:28:30

Changing status from needs_review to positive_review.


---

Comment by nbruin created at 2013-12-12 21:04:05

Replying to [comment:123 maldun]:
> And good idea to replace the old % format string operator, since it will be deprecated in Python 3

This has been a rumour that didn't pan out. I don't think a time line has been set towards actual deprecation of %. The possibility of deprecation is mentioned in 
http://www.python.org/dev/peps/pep-3101/
but it's careful to argue that deprecation is not required at all. At some point it was planned to deprecate % in 3.0 and remove it in 3.1 but that hasn't happened. I suspect it's so ingrained by now that deprecation and removal is impractical.


---

Comment by jdemeyer created at 2013-12-16 09:30:48

Travis: are you sure you applied the dependency #15422? I am suspicious because you added

```diff
-            (2^7 + O(2^8))*t^5 + (O(2^8))*t^4 + (2^6 + O(2^8))*t^3 + (O(2^8))*t^2 + (1 + 2^6 + O(2^8))*t + (O(2^8))
+            (2^7 + O(2^8))*t^5 + (2^6 + O(2^8))*t^3 + (1 + 2^6 + O(2^8))*t
```

which seems to be a doctest failure.


---

Comment by jdemeyer created at 2013-12-16 09:44:08

I also don't agree with all changes of

```
if condition:
    return A
else:
    return B
```

to

```
if condition:
    return A
return B
```

but I guess that's one of your pet peeves.

I personally prefer

```
if condition:
    return A
else:
    return B
```

if there are clearly two cases and the code might as well have been written as

```
if not condition:
    return B
else:
    return A
```


So I personally would keep the `if/else` structure for the `if n % 2 == 0` test. And for the `n >= 0` test, I would say that

```
if n < 0:
    return B
return A
```

would be a lot better that what you did:

```
if n >= 0:
    return A
return B
```

The first feels much better to me because you put the normal case outside the `if` block and the special cases `if n == 0` and `if n < 0` would be inside `if`s.

(Of course these are all personal preferences, I'm not asking you to change this, maybe just think about it.)


---

Comment by jdemeyer created at 2013-12-16 11:01:06

Changing status from positive_review to needs_info.


---

Attachment


---

Comment by tscrim created at 2013-12-16 15:15:04

I had missed the #15422 dependency. Fixed.

As for the `if/else`, I've seen (sometimes long) `else` blocks that constitute the normal cases and I try to be uniform about it. Plus with the extra indents, I sometimes have difficulties knowing what the correct indent level should be (although not in this case). I do agree that the cases should be swapped -- I had only removed the `else:`. I added back in the `else` blocks for the `if n % 2 == 0`.


---

Comment by tscrim created at 2013-12-16 15:15:04

Changing status from needs_info to needs_review.


---

Comment by jdemeyer created at 2013-12-16 15:46:38

Changing status from needs_review to positive_review.


---

Comment by maldun created at 2013-12-17 12:01:13

First stage done. Next step: Legendre Polys.

I will keep up the new design + incorporate more doc tests next time. I guess it is important to look at the algebraic aspects too concerning doc tests.

Thank all reviewers for their hard work and the good input!


---

Comment by vbraun created at 2013-12-21 14:30:42

New commits:


---

Comment by vbraun created at 2013-12-21 18:43:54

Resolution: fixed
