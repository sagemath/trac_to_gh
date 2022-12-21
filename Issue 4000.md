# Issue 4000: Implement QQ['x'] via Flint ZZ['x'] + denominator

Issue created by migration from Trac.

Original creator: malb

Original creation time: 2008-08-30 12:21:46

Assignee: somebody

CC:  burcin drkirkby spancratz mhansen malb jdemeyer pjeremy

Bill Hart wrote on [sage-devel]:

"""
Almost everything over Q should probably be converted to a problem
over Z. I haven't seen any polynomial problems over Q which should not
be dealt with this way so far, but I suppose they may exist.
"""

Further justification:

```
sage: f = R.random_element(2000)
sage: g = R.random_element(2000)
sage: fD = f.denominator()
sage: gD = g.denominator()
sage: fZ = (fD * f).change_ring(ZZ)
sage: gZ = (gD * g).change_ring(ZZ)
sage: %time _ = f*g
CPU times: user 0.63 s, sys: 0.02 s, total: 0.66 s
Wall time: 0.67 s

sage: %time _ = (fZ*gZ)
CPU times: user 0.01 s, sys: 0.00 s, total: 0.01 s
Wall time: 0.01 s

sage: %time _ = (fZ*gZ)/(fD*gD) 
CPU times: user 0.06 s, sys: 0.00 s, total: 0.06 s
Wall time: 0.06 s

sage: fM = magma(f)
sage: gM = magma(g)
sage: t = magma.cputime()
sage: _ = fM*gM
sage: magma.cputime(t)
0.059999999999999998
```



```
sage: f = R.random_element(4000) 
sage: g = R.random_element(4000) 
sage: fD = f.denominator()
sage: gD = g.denominator()
sage: fZ = (fD * f).change_ring(ZZ)
sage: gZ = (gD * g).change_ring(ZZ)
sage: %time _ = f*g
CPU times: user 2.11 s, sys: 0.00 s, total: 2.12 s
Wall time: 2.14 s
sage: %time _ = (fZ*gZ)
CPU times: user 0.02 s, sys: 0.00 s, total: 0.02 s
Wall time: 0.02 s
sage: %time _ = (fZ*gZ)/(fD*gD)
CPU times: user 0.14 s, sys: 0.01 s, total: 0.15 s
Wall time: 0.15 s
sage: fM = magma(f)
sage: gM = magma(g)
sage: t = magma.cputime()
sage: _ = fM*gM
sage: magma.cputime(t)
0.10000000000000001
```



---

Comment by malb created at 2009-09-02 14:08:58

The attached patch provides the basic skeleton for the proposed new implementation. The following already works with the attached patch:


```python
sage: from sage.rings.polynomial.polynomial_rational_flint import Polynomial_rational_dense_flint
sage: P.<t> = QQ[]
sage: a = Polynomial_rational_dense_flint(P,1/2)
sage: b = Polynomial_rational_dense_flint(P,2/1)
sage: t = Polynomial_rational_dense_flint(P,is_gen=True)
sage: a*t
1/2*t
sage: a*t*b
t
sage: a*t*b*b
2*t
sage: a*t*b*(b*t)
2*t^2
sage: a*t*b*(b*t)*a
t^2
```



---

Comment by spancratz created at 2009-09-07 23:19:42

I've now implemented most methods in the prototype from the previous patch uploaded, and sent a message to sage-devel under the thread "Improving QQ['x']" with some questions.

Sebastian


---

Comment by malb created at 2009-09-08 09:56:54

*Some remarks*

 * the patch uses the old style docstring format, cf. http://wiki.sagemath.org/combinat/HelpOnTheDoc 
 * you should claim copyright
 * `cdef inline int _celement_canonicalise` why not `void`?
 * *all* `celement_foo` functions should have doctests, which call the `QQ[x]` methods which call the `celement_` functions
 * have you tried switching the default to this implementation to see how many doctests fail?


---

Comment by spancratz created at 2009-09-09 22:06:48

Hi Martin,

I've now implemented all methods in the prototype.  (I'll attach a new patch in a few minutes.)  All of your above comments make sense and I can go through this tomorrow.  One thing I could not get done is make SAGE use this implementation by default.  In the file polynomial_ring.py, I tried replacing the line 1185 with

    from sage.rings.polynomial.polynomial_rational_flint import Polynomial_rational_dense_flint
    element_class = Polynomial_rational_dense_flint

and while building still works, executing ./sage results in a whole screen full output, ending with

    b37bb0/home/suser/sage-4.1.2.alpha0/local/bin/sage-sage: line 199: 16297 Aborted                 sage-ipython "$`@`" -i

Am I making a mistake in the way I am trying to switch the default, or does this due to problems in the actual new implementation?  I've got no idea how to fix this.  Of course, I am then happy to do lots of testing.

Kind regards,

Sebastian


---

Comment by malb created at 2009-09-09 23:01:57

I can take a look tomorrow to debug this.


---

Comment by malb created at 2009-09-10 11:59:01

I fixed the startup crash. I suggest you take a look at `fmpq.diff` to see what I changed. If you want to debug these kind of issues start Sage using `sage -gdb` or `sage -valgrind` (you will need to install the optional Valgrind SPKG for this to work). Note that there is still some conversion code missing in `polynomial_rational_flint.pyx`.


```python
sage: P.<x> = QQ[]
sage: f = P.random_element(2000)
sage: g = P.random_element(2000)
sage: %time _ = f*g
CPU times: user 0.01 s, sys: 0.00 s, total: 0.01 s
Wall time: 0.02 s
```



```python
sage: P.<x> = PolynomialRing(QQ,'x',implementation='pari')
sage: f = P.random_element(2000)
sage: g = P.random_element(2000)
sage: %time _ = f*g
CPU times: user 0.59 s, sys: 0.00 s, total: 0.59 s
Wall time: 0.59 s
```



```python
sage: P.<x> = QQ[]
sage: f = P.random_element(5000)
sage: g = P.random_element(5000)
sage: %time _ = f*g
CPU times: user 0.03 s, sys: 0.00 s, total: 0.03 s
Wall time: 0.04 s
```



```python
sage: fM = magma(f)
sage: gM = magma(g)
sage: t = magma.cputime()
sage: _ = fM*gM
sage: magma.cputime(t)
0.12
```



---

Comment by spancratz created at 2009-09-10 21:24:34

Thanks for the quick debugging and making the code accessible in SAGE for testing!  I'll upload a new version of the patch later.  Here are a few (unsorted) remarks:

- The printing isn't "nice" yet:  Rationals are still printed in the form r/s even if s divides r.  In fact, all coefficients are printed with the common denominator of the polynomial.  I've got an idea of how to fix that, but I am not sure it'll work;  I'll give it a try later.

- Say we set up to polynomial rings R[x] and S[y], one using the generic implementation and one using FLINT.  Then sometimes (usually?) coercion like "f_flint = S(f_generic)" or "f_generic = R(f_flint)" works, but sometimes it ends in a segfault.  For two random polynomials f and d, of two successive calls "q, s, t = xgcd(f, d)" the first one succeeded and the second one ended in a segfault.  This seems *very* strange to me!

- We achieve a performance gain except in the cases of addition and subtraction.  (See below.)

- The method xgcd doesn't give the right result yet, I'll look into that later.

- I have no idea what you mean by "Note that there is still some conversion code missing in polynomial_rational_flint.pyx."  Are there any examples of this in other files?

- I'll write up the doctests later.  Regarding your comments on using the "old" documentation style, I don't quite understand this.

Here is a complete (except for XGCD) list of performance comparisons, using the local installation of SAGE 4.1.2.alpha0 plus this patch on my laptop (Ubuntu 8.10, Intel Core 2 Duo).  The first few tests, from comparison through to power, involve random polynomials f and g of degrees 2000, the division tests use random polynomials f and d of degrees 800 and 560, and for the GCD test f and d have degree 60 and 42.  In each case, the first output line is for the generic implementation, the second output line is for the new implementation using FLINT.

    {{{
    Comparison: f == g
    1 loops, best of 3: 10 µs per loop
    1 loops, best of 3: 954 ns per loop
    Comparison: f < g
    1 loops, best of 3: 11 µs per loop
    1 loops, best of 3: 1.91 µs per loop
    Addition: f + g
    1 loops, best of 3: 373 µs per loop
    1 loops, best of 3: 2.26 ms per loop
    Subtraction: f - g
    1 loops, best of 3: 474 µs per loop
    1 loops, best of 3: 2.23 ms per loop
    Negation: -f
    1 loops, best of 3: 12.9 ms per loop
    1 loops, best of 3: 39.8 µs per loop
    Multiplication: f * g
    1 loops, best of 3: 549 ms per loop
    1 loops, best of 3: 15.9 ms per loop
    Power: f ** 4
    1 loops, best of 3: 15.1 s per loop
    1 loops, best of 3: 63.7 ms per loop
    Division: q, r = f.quo_rem(d)
    1 loops, best of 3: 2.42 s per loop
    1 loops, best of 3: 177 ms per loop
    Division: q = f // d
    1 loops, best of 3: 2.43 s per loop
    1 loops, best of 3: 63.9 ms per loop
    Division: r = f % d
    1 loops, best of 3: 2.43 s per loop
    1 loops, best of 3: 193 ms per loop
    GCD
    1 loops, best of 3: 1.81 s per loop
    1 loops, best of 3: 88.9 µs per loop
    }}}

Sebastian


---

Comment by malb created at 2009-09-10 23:59:33

Replying to [comment:8 spancratz]:
> - Say we set up to polynomial rings R[x] and S[y], one using the generic implementation and one using FLINT.  Then sometimes (usually?) coercion like "f_flint = S(f_generic)" or "f_generic = R(f_flint)" works, but sometimes it ends in a segfault.  For two random polynomials f and d, of two successive calls "q, s, t = xgcd(f, d)" the first one succeeded and the second one ended in a segfault.  This seems *very* strange to me!

Try running Sage with `sage -gdb` and/or `sage -valgrind`. The later requires the optional Valgrind SPKG. The output of valgrind is incredibly useful and can be found in `~/.sage/valgrind`. If you don't get anywhere, I can take a look. But learning Valgrind is well worth it :)

> - We achieve a performance gain except in the cases of addition and subtraction.  (See below.)

We should think about how to make it more efficient, e.g. by only multiplying by the multiplier to get the LCM? Magma can do it faster than what we can do it seems.

> - The method xgcd doesn't give the right result yet, I'll look into that later.
> 
> - I have no idea what you mean by "Note that there is still some conversion code missing in polynomial_rational_flint.pyx."  Are there any examples of this in other files?

You are right, the overflow I was expecting doesn't happen (I think this is handled correctly in the base ring). We should consider making `x + 1` (1 either int or Integer) fast though by writing special code similar to the Rational code in the `__init__` function of `polynomial_rational_flint.pyx`. Also, construction from a list `P([1,2,3,4])` should be made faster, cf. the zmod_poly implementation.

> - I'll write up the doctests later.  Regarding your comments on using the "old" documentation style, I don't quite understand this.

You wrote e.g. ` \code{foo} ` which is the old LaTeX style. It should be using the Sphinx markup now.

> Here is a complete (except for XGCD) list of performance comparisons, using the local installation of SAGE 4.1.2.alpha0 plus this patch on my laptop (Ubuntu 8.10, Intel Core 2 Duo).  The first few tests, from comparison through to power, involve random polynomials f and g of degrees 2000, the division tests use random polynomials f and d of degrees 800 and 560, and for the GCD test f and d have degree 60 and 42.  In each case, the first output line is for the generic implementation, the second output line is for the new implementation using FLINT.

This is encouraging!


---

Comment by malb created at 2009-09-11 00:01:45

Also, I think our design for `.den` is false. It shouldn't be preallocated because this makes you call realloc, i.e. we have two system calls instead of one. This is quite expensive.


---

Comment by spancratz created at 2009-09-11 11:33:51

Actually, I am not quite sure about this.  When working with a random polynomial of degree 2000, which will have lots of non-zero entries all of type fmpz_t, it shouldn't really matter whether we manually initialise a few more for the denominators.

I've tried implementing the denominator with the convention that it is either ``NULL`` (which should be interpreted as one) or initialised to a positive integer.  But this didn't really change the performance.

Another idea, which will sometimes help to keep numbers small, is to instead represented the polynomial over the rationals as ``(num / dem) prim`` where ``num / dem`` is a rational number in reduced form and ``prim`` is a primitive integer polynomial with positive leading coefficient.  Obviously, this change vastly improved the performance of negation (which then only operates on the rational number and leaves the integer polynomial part alone).  But it didn't change much apart from that.  Anyway, given we need to compute the content of the numerator anyway to ensure that it is coprime to the denominator, we might as well store it separately.  I'll implement this throughout the patch and upload a new version later today.

This still leaves the problem:  How can we speed up addition?

At the moment, I don't have any further ideas.  In fact, I think it might perhaps be the case that we simply can't, since in this kind of implementation we have to at least do a few polynomial scalar multiplications (and perhaps polynomial scalar divisions as well as integer gcd computations to maintain the form of the representation) plus all the coefficient additions.  In contrast to this, implementing polynomials as an array of coefficients one only has to do the (rational!) coefficient additions.

So the next things I'll do are

- Change the fmpq_poly_t data type
- Change all the methods accordingly
- Write docstrings

Does anyone have any ideas about the addition?

Sebastian


---

Comment by malb created at 2009-09-11 12:18:35

Replying to [comment:11 spancratz]:
> Actually, I am not quite sure about this.  When working with a random polynomial of degree 2000, which will have lots of non-zero entries all of type fmpz_t, it shouldn't really matter whether we manually initialise a few more for the denominators.

We shouldn't forget about small polynomials, they should be fast too. Two instead of one system call sounds rather expensive to me for basic arithmetic.
 
> I've tried implementing the denominator with the convention that it is either ``NULL`` (which should be interpreted as one) or initialised to a positive integer.  But this didn't really change the performance.

Did you try small examples? Also, how much does the realloc trick you implemented give you?

> Another idea, which will sometimes help to keep numbers small, is to instead represented the polynomial over the rationals as ``(num / dem) prim`` where ``num / dem`` is a rational number in reduced form and ``prim`` is a primitive integer polynomial with positive leading coefficient.  Obviously, this change vastly improved the performance of negation (which then only operates on the rational number and leaves the integer polynomial part alone).  But it didn't change much apart from that.  Anyway, given we need to compute the content of the numerator anyway to ensure that it is coprime to the denominator, we might as well store it separately.  I'll implement this throughout the patch and upload a new version later today.
> 
> This still leaves the problem:  How can we speed up addition?

Did you try the LCM idea? Rationale:


```python
sage: P.<x> = QQ[]
sage: f = P.random_element(3000)
sage: g = P.random_element(3000)
sage: fD = f.denominator()
sage: gD = g.denominator()
sage: (fD*gD).nbits()
320
sage: (fD.lcm(gD)).nbits()
228
```


> At the moment, I don't have any further ideas.  In fact, I think it might perhaps be the case that we simply can't, since in this kind of implementation we have to at least do a few polynomial scalar multiplications (and perhaps polynomial scalar divisions as well as integer gcd computations to maintain the form of the representation) plus all the coefficient additions.  In contrast to this, implementing polynomials as an array of coefficients one only has to do the (rational!) coefficient additions.

Well, this other implementation would have to do quite a few rational additions where it would have to deal with denominators quite a bit. I am not convinced yet it has to be this slow. You could also ask on [sage-devel] I am sure, e.g. Bill Hart (main author of FLINT) would have some cool ideas.


---

Comment by spancratz created at 2009-09-12 23:06:28

I am sorry for the delay in working on this.  Rather than trying the approach of writing the polynomial as `r A / s`, I've tried again to write this as `A / s` only as you laid out initially, this time trying really hard to avoid allocating anything new.  Not everything is working again yet, I still need to re-write the three division functions, exponentiation and the two gcd functions.  The upside is that everything seems to be lots faster now :).

Hopefully I'll be able to upload something useful tomorrow.

Sebastian


---

Comment by spancratz created at 2009-09-14 00:03:24

The switch to include NULL denominators still isn't quite done.  However, I *think* addition and multiplication are bug-free already and show another massive improvement in speed.  There are definitely still bugs in the division method, and the modular exponentiation as well as the gcd methods aren't implemented yet.  I should be able to look into this tomorrow.

Sebastian


---

Comment by malb created at 2009-09-14 11:47:25

I can't test the most current patch (on geom.math):

```python
sage: P.<x> = PolynomialRing(QQ)
sage: f = P.random_element(2000)
...
__celement_den_fit_limbs
Error: division by zero!
/scratch/malb/sage-4.1.2.alpha1/local/bin/sage-sage: line 199: 12195 Aborted                 sage-ipython "$`@`" -i
```



---

Comment by spancratz created at 2009-09-14 14:49:42

Hi Martin,

I am sorry for that.  Last night and this morning I fixed another couple of bugs.  In a few minutes, I'll upload a new patch (or rather, again the difference from the 20090911 patch).  By the way, for debugging purposes all methods in the linkage file now begin with printing the method's name (although in all but the floordiv method, that line begins with '#').

Random (performance!, not correctness...) tests ran fine last night for polynomials of degree 2000 for the methods ==, <, +, -, neg, *, ^.  I thought the three division methods should work fine now, until I stumbled across the following segfault:

    {{{
    sage: S.<y> = QQ[]
    sage: f = -3 * y^10 - 4 * y^9
    sage: g = (1/2) * y^6 + 3 * y^5 + 160930 * y^4
    sage: f // g
    celement_floordiv
    Perform pseudo division -3*x<sup>10-4*x</sup>9 x<sup>6+6*x</sup>5+321860*x^4
    
    
    ------------------------------------------------------------
    Unhandled SIGSEGV: A segmentation fault occured in SAGE.
    This probably occured because a *compiled* component
    of SAGE has a bug in it (typically accessing invalid memory)
    or is not properly wrapped with _sig_on, _sig_off.
    You might want to run SAGE under gdb with 'sage -gdb' to debug this.
    SAGE will now terminate (sorry).
    ------------------------------------------------------------
    }}}

This strikes me as very odd because the segfault seems to occur in the call ``fmpz_poly_pseudo_div(q.num, &m, a.num, b.num)`` with ``a.num`` the polynomial ``-3*x<sup>10-4*x</sup>9`` and ``b.den`` the polynomial ``x<sup>6+6*x</sup>5+321860*x^4``.  Perhaps you could have a look at this one?

I haven't looked at the two gcd methods yet, but I'll do that later today or tomorrow.

As the last question about the implementation (for this method), I noticed that polynomials over QQ in SAGE have the method ``denominator``, which clearly this implementation should overwrite.  On which level/ in which file should this be done?

Finally, here are the performance timings, in each case for ten random polynomials of degree 2000, first the time for the generic implementation and then the time for this implementation with FLINT:

- ``==`` -  20µs, 1µs
- ``<`` -  20µs, 1µs
- ``+`` -  400µs, 100µs
- ``-`` -  400µs, 100µs
- ``neg`` -  20ms, 20µs
- ``*`` -  500ms, 1ms
- ``^`` (to the 4th power) -  15s, 30µs

Kind regards,

Sebastian


---

Comment by spancratz created at 2009-09-14 16:38:15

Hi Martin,

I just started to look at the gcd methods again and I also looked at the logic in polynomial_template.pxi.  Here's the question:

Since the gcd of two polynomials is only defined up to multiplication by rationals, what's the *right* way of dealing with this?  I think one can make a good argument for always returning the same normalisation.  This would also mean that we do *not* necessarily have gcd(a,0) == a.  This is currently the way it's handled in the file polynomial_template.pxi.  If we want to normalise the gcd, in which way should this be done?  If it's non-zero..

  -  Monic rational polynomial
  -  Primitive integer polynomial with positive leading coefficient

Of course, there are lots more but I think these two might be the most sensible choices.

The first one has the advantage that it generalises to all polynomial rings (over commutative rings with 1, at least).  Upon adding a method returning the monic scalar multiple of a polynomial to the template file, one can still handle the cases of gcd(a,0) and gcd(0,b) in the template file.

Personally though, I am more in favour of the second option, since this might lead to faster code when working with QQ[].  In this case, we should remove the handling of the above two cases from the template file and always pass the call on to celement_gcd.  This would mean that we leave the normalisation up to the actual implementation of the polynomial ring, rather than enforcing it across all base rings using the template file.  We would then also have to make sure that all celement_gcd methods are happy to deal with zero arguments.

What do you think?

Sebastian


---

Comment by malb created at 2009-09-14 20:50:35

Replying to [comment:16 spancratz]:
> Perhaps you could have a look at this one?

I will (hopefully) take a look later this week.

> As the last question about the implementation (for this method), I noticed that polynomials over QQ in SAGE have the method ``denominator``, which clearly this implementation should overwrite.  On which level/ in which file should this be done?

You would add a method `denominator()` to `Polynomial_rational_dense_flint`.

> Finally, here are the performance timings, in each case for ten random polynomials of degree 2000, first the time for the generic implementation and then the time for this implementation with FLINT:

If I understand this correctly, then addition is 20x faster than the previous implementation just because you avoid a remalloc?


---

Comment by malb created at 2009-09-14 20:54:59

Replying to [comment:17 spancratz]:
> Since the gcd of two polynomials is only defined up to multiplication by rationals, what's the *right* way of dealing with this?  I think one can make a good argument for always returning the same normalisation.  This would also mean that we do *not* necessarily have gcd(a,0) == a.  This is currently the way it's handled in the file polynomial_template.pxi.  If we want to normalise the gcd, in which way should this be done?  If it's non-zero..

I think we should have `gcd(a,0) = 1` because this is what `gcd(1/2,0)` returns. I would like to avoid to put this logic in the celement_gcd implementations but if we have to then ... well we have to :)

> Personally though, I am more in favour of the second option, since this might lead to faster code when working with QQ[].  In this case, we should remove the handling of the above two cases from the template file and always pass the call on to celement_gcd.  This would mean that we leave the normalisation up to the actual implementation of the polynomial ring, rather than enforcing it across all base rings using the template file.  We would then also have to make sure that all celement_gcd methods are happy to deal with zero arguments.

This might be worth raising on [sage-devel] where people care much more about this than I do, i.e. I guess it is a relevant corner case for number theory and thus people might have strong feelings about it?


---

Comment by spancratz created at 2009-09-14 21:20:55

> > As the last question about the implementation (for this method), I noticed that polynomials over QQ in SAGE have the method ``denominator``, which clearly this implementation should overwrite.  On which level/ in which file should this be done?
> 
> You would add a method `denominator()` to `Polynomial_rational_dense_flint`.

OK, I'll do that.

> > Finally, here are the performance timings, in each case for ten random polynomials of degree 2000, first the time for the generic implementation and then the time for this implementation with FLINT:
> 
> If I understand this correctly, then addition is 20x faster than the previous implementation just because you avoid a remalloc?

Yes.  Actually, throughout I am now trying very hard to re-use variables rather than allocating new variables all over the place.  It makes the code quite ugly...  but definitely faster, which this is about, right? :)


---

Comment by spancratz created at 2009-09-14 21:40:19

Replying to [comment:19 malb]:
> Replying to [comment:17 spancratz]:
> I think we should have `gcd(a,0) = 1` because this is what `gcd(1/2,0)` returns. I would like to avoid to put this logic in the celement_gcd implementations but if we have to then ... well we have to :)

I didn't mean the above for rational numbers ``a``, but for rational polynomials ``a``.  Your integer example above highlights that ``gcd`` doesn't necessarily guarantee ``gcd(a, 0) == a``.  The behaviour of ``gcd`` for integers suggests the method should return the monic normalisation.  However, the current logic in ``template_polynomial.pxi`` doesn't do this, for example:

    {{{
    sage: R.<t> = PolynomialRing(IntegerModRing(3), 't')
    sage: f = 2*t + 1
    sage: type(f)
    <type 'sage.rings.polynomial.polynomial_zmod_flint.Polynomial_zmod_flint'>
    sage: gcd(f, R(0))
    2*t + 1
    }}}

In the above case, the monic version would be ``t + 2``.

> This might be worth raising on [sage-devel] where people care much more about this than I do, i.e. I guess it is a relevant corner case for number theory and thus people might have strong feelings about it?

OK, I'll do this.

Sebastian


---

Comment by spancratz created at 2009-09-16 13:10:36

I have now opened another ticket, #6941, to change the template implementation, pushing all the logic into the ``celement_foo`` methods rather than taking away the cases ``gcd(a,0)`` and ``gcd(0,b)`` on a higher level.  The patch is very short --- it only does the small expected changes to the template file and the GF2X and ZMOD linkage files, plus one other file in the hyperelliptic curve module where the current behaviour of xgcd is used.

Martin, would you be happy to review that patch?

Sebastian


---

Comment by spancratz created at 2009-09-19 19:40:06

I've now implemented almost all functionality from the former generic implementation, most of it massively improved through FLINT.  There are also some new methods.  All of this is in the patch I uploaded just now, still as a difference to the 20090911 patch.  Running make test still results in many failures, although fewer than last week.

Sebastian


---

Comment by spancratz created at 2009-09-21 22:18:01

Apart from a bad indentation in ``polynomial_quotient_ring_element``, for which I didn't want to re-upload a patch, I am now down to the following doctest failures:

        {{{
        sage -t  "devel/sage/sage/schemes/elliptic_curves/padic_lseries.py"
        sage -t  "devel/sage/sage/schemes/elliptic_curves/ell_generic.py"
        sage -t  "devel/sage/sage/schemes/elliptic_curves/padics.py"
        sage -t  "devel/sage/sage/schemes/elliptic_curves/ell_curve_isogeny.py"
        sage -t  "devel/sage/sage/tests/book_stein_modform.py"
        sage -t  "devel/sage/sage/rings/qqbar.py"
        sage -t  "devel/sage/sage/rings/number_field/number_field_element.pyx"
        sage -t  "devel/sage/sage/modular/modform/element.py"
        sage -t  "devel/sage/sage/modular/overconvergent/genus0.py"
        sage -t  "devel/sage/sage/modular/hecke/submodule.py"
        sage -t  "devel/sage/sage/structure/sage_object.pyx"
        }}}

All but one of them are memory problems, either in ``mpq_canonicalize`` (called in the ``__getitem__`` method) or in ``fmpz_poly_mul`` called in ``celement_mul``.  At the moment, I do not know how to resolve these.

Sebastian


---

Comment by spancratz created at 2009-09-23 10:53:46

Almost all of the memory problems are now resolved.  They were arising because I wrongly assumed ``fmpz_`` methods (*not* ``fmpz_poly_``;  they work just fine) supported aliasing of the inputs and outputs.  Apart from the method ``fmpz_neg``, I think I have fixed this in all places where I am using it, apart from the square-free decomposition in polynomial_rational_flint.pyx.  I'll rewrite that, too, but I've already checked that this method does not get called in the following last two remaining doctest failures:

    {{{
    The following tests failed:
    
        sage -t  "devel/sage/sage/rings/qqbar.py"
        sage -t  "devel/sage/sage/structure/sage_object.pyx"
    }}}

The test in ``qqbar.py`` that seems to break down is the following piece of code:

    {{{
    sage: x = polygen(AA)
    sage: r = QQbar.polynomial_root(x^5 - x - 1, CIF(RIF(0.1, 0.2), RIF(1.0, 1.1))); r
    sage: r.real().minpoly()
    }}}

The test in ``sage_object.pyx`` that breaks has to do with unpickling, and it's triggered by the following two lines:

    {{{
    sage: std = os.environ['SAGE_DATA'] + '/extcode/pickle_jar/pickle_jar.tar.bz2'
    sage: sage.structure.sage_object.unpickle_all(std)
    }}}

I will try to chase down the first problem a little further than the ``minpoly()`` function, perhaps I can resolve it myself.  But any help with the second problem in particular would be very much appreciated.

Sebastian


---

Comment by mhansen created at 2009-09-24 05:36:46

I've added a patch which fixes the unpickling problem making sure that the old polynomials unpickle as the new polynomials.


---

Comment by mhansen created at 2009-09-24 05:50:51

This gives the same answers for me before and after the patch.


```
    sage: x = polygen(AA)
    sage: r = QQbar.polynomial_root(x^5 - x - 1, CIF(RIF(0.1, 0.2), RIF(1.0, 1.1))); r
    sage: r.real().minpoly()
```


The only difference is the test on line 2262. It expected 


```
    cp = AA.common_polynomial(1/2*x^4 - 1/95*x^3 - 1/2*x^2 - 4)
```


but got 


```
    cp = AA.common_polynomial(x^4 - 2/95*x^3 - x^2 - 8)
```


I think that this is okay since they only differ by a multiple of 2 and thus have the exact same roots.


---

Comment by spancratz created at 2009-09-24 10:59:41

Hello Mike,

Thank you for fixing the unpickling problem!

About the second problem, the one in ``qqbar.py``, are you saying that the following code

    {{{
    sage: x = polygen(AA)
    sage: r = QQbar.polynomial_root(x^5 - x - 1, CIF(RIF(0.1, 0.2), RIF(1.0, 1.1))); r
    sage: r.real().minpoly()
    }}}

now executes without problems on your setup?  On mine, it still crashes with a segmentation fault.  I've uploaded the complete traceback to http://sage.pastebin.com/m5249e09.  I still seems strange to me that the traceback doesn't seem to contain methods that this patch modifies directly.

The other difference you mention is no problem, of course.  That's because I have taken care to ensure that methods returning results that are only defined up to units return monic normalisations.

Many thanks again for taking a look at this patch,

Sebastian


---

Comment by spancratz created at 2009-09-24 18:20:17

As said, the above three lines of code extracted from the ``qqbar.py`` doctests still cause a problem for me.  I've chased it down for the last three hours now, and the following code breaks on my setup:

    {{{
    sage: R.<x> = QQ[]
    sage: f = 422826864750/4773824138704099*x^18 - 8134231405059/9547648277408198*x^16 + 11311262264874/4773824138704099*x^14 - 12814039341867/4773824138704099*x^12 - 8509019074752/4773824138704099*x^10 + 707815020483605/9547648277408198*x^8 - 1781974116019893/4773824138704099*x^6+ 1316925435907659/4773824138704099*x^4 - 1088322011947813/9547648277408198*x^2 - 1/2*x + 1289415905296105/4773824138704099
    sage: g = -76937/62774*x^19 - 30011/62774*x^18 + 144945/31387*x^17 + 174999/62774*x^16 - 377075/31387*x^15 - 354028/31387*x^14 + 929437/62774*x^13 + 983229/62774*x^12 - 725164/31387*x^11 - 984029/31387*x^10 + 945031/62774*x^9 + 1132829/31387*x^8 + 277343/31387*x^7 - 1107925/62774*x^6 - 432756/31387*x^5 - 23909/62774*x^4 + 202423/31387*x^3 + 167709/31387*x^2 - 10729/31387*x - 47216/31387
    sage: f(g)
    }}}

I've upload a complete log of the session to [url]http://sage.pastebin.com/m7757deba[/url].  I am happy also re-implement polynomial composition using FLINT, it should be a lot faster than the generic code for this anyway.  (Idea:  To compose F = f/d with G = g/e, where f, g are in ZZ[] and d, e are integers, first "rescale" F by 1/e --- this method is implemented already --- and then compose the new polynomial with g.  There is a FLINT function for the last part.)  However, I don't know how or where the generic code is implemented in SAGE.

Sebastian


---

Comment by mhansen created at 2009-09-25 04:15:48

Replying to [comment:29 spancratz]:
> As said, the above three lines of code extracted from the ``qqbar.py`` doctests still cause a problem for me.  I've chased it down for the last three hours now, and the following code breaks on my setup:
> 
>     {{{
>     sage: R.<x> = QQ[]
>     sage: f = 422826864750/4773824138704099*x^18 - 8134231405059/9547648277408198*x^16 + 11311262264874/4773824138704099*x^14 - 12814039341867/4773824138704099*x^12 - 8509019074752/4773824138704099*x^10 + 707815020483605/9547648277408198*x^8 - 1781974116019893/4773824138704099*x^6+ 1316925435907659/4773824138704099*x^4 - 1088322011947813/9547648277408198*x^2 - 1/2*x + 1289415905296105/4773824138704099
>     sage: g = -76937/62774*x^19 - 30011/62774*x^18 + 144945/31387*x^17 + 174999/62774*x^16 - 377075/31387*x^15 - 354028/31387*x^14 + 929437/62774*x^13 + 983229/62774*x^12 - 725164/31387*x^11 - 984029/31387*x^10 + 945031/62774*x^9 + 1132829/31387*x^8 + 277343/31387*x^7 - 1107925/62774*x^6 - 432756/31387*x^5 - 23909/62774*x^4 + 202423/31387*x^3 + 167709/31387*x^2 - 10729/31387*x - 47216/31387
>     sage: f(g)
>     }}}
> 
> I've upload a complete log of the session to [url]http://sage.pastebin.com/m7757deba[/url].  I am happy also re-implement polynomial composition using FLINT, it should be a lot faster than the generic code for this anyway.  (Idea:  To compose F = f/d with G = g/e, where f, g are in ZZ[] and d, e are integers, first "rescale" F by 1/e --- this method is implemented already --- and then compose the new polynomial with g.  There is a FLINT function for the last part.)  However, I don't know how or where the generic code is implemented in SAGE.
> 
> Sebastian

This does not crash for me on 64-bit linux with both FLINT 1.3.0 and FLINT 1.5.0.  You should try the FLINT 1.5.0 spkg at http://sage.math.washington.edu/home/mhansen/flint-1.5.0.spkg.

--Mike
>     sage: f = 422826864750/4773824138704099*x^18 - 8134231405059/9547648277408198*x^16 + 11311262264874/4773824138704099*x^14 - 12814039341867/4773824138704099*x^12 - 8509019074752/4773824138704099*x^10 + 707815020483605/9547648277408198*x^8 - 1781974116019893/4773824138704099*x^6+ 1316925435907659/4773824138704099*x^4 - 1088322011947813/9547648277408198*x^2 - 1/2*x + 1289415905296105/4773824138704099
>     sage: g = -76937/62774*x^19 - 30011/62774*x^18 + 144945/31387*x^17 + 174999/62774*x^16 - 377075/31387*x^15 - 354028/31387*x^14 + 929437/62774*x^13 + 983229/62774*x^12 - 725164/31387*x^11 - 984029/31387*x^10 + 945031/62774*x^9 + 1132829/31387*x^8 + 277343/31387*x^7 - 1107925/62774*x^6 - 432756/31387*x^5 - 23909/62774*x^4 + 202423/31387*x^3 + 167709/31387*x^2 - 10729/31387*x - 47216/31387
>     sage: f(g)
>     }}}
> 
> I've upload a complete log of the session to [url]http://sage.pastebin.com/m7757deba[/url].  I am happy also re-implement polynomial composition using FLINT, it should be a lot faster than the generic code for this anyway.  (Idea:  To compose F = f/d with G = g/e, where f, g are in ZZ[] and d, e are integers, first "rescale" F by 1/e --- this method is implemented already --- and then compose the new polynomial with g.  There is a FLINT function for the last part.)  However, I don't know how or where the generic code


---

Comment by spancratz created at 2009-09-25 22:22:03

Firstly, I am sorry for the bad patches I uploaded earlier --- I didn't realise that new files aren't included in a patch by default.  I have changed this now and uploaded a new complete patch ``fmpq_20090925.patch``.

There is one problem with the ``squarefree_decomposition`` method, which for some unknown reason was causing memory failures in the latest version.  For the time being, I've just changed it back to my earlier code, which still uses bad aliasing of arguments to ``fmpz_`` methods.

Mike:  Thanks for taking a look at the composition problem, too.  The failure on my setup must be rather strange, since the traceback also includes ``finance/fractal.so``.  I don't think I understand the ``__call__`` method well enough to do much about it.  In any case, I think the current code (catching polynomial composition, and otherwise passing the call on to ``Polynomial.__call__``) should be preferable.

I am not quite sure what I should do at this point.  I think it would be best to wait until the release of the next stable release of SAGE and then look at this again with the goal to have sorted out as soon as possible.  What do other people think?  If someone has a suggestion for what I should do at the moment, while I might not have too much time during the next few weeks, I should definitely be able to look at this every weekend.

Sebastian


---

Comment by malb created at 2009-11-17 22:50:39

Sebastian, what's the current status of this code? What needs to be done to finish it etc?


---

Comment by spancratz created at 2010-01-20 10:37:20

The plan is to re-base this on #383, which should take care of two segfaults that currently remain.


---

Comment by spancratz created at 2010-01-20 15:14:06

I've now added two patches to this.  The first one ``trac383.patch`` contains all three patches from ticket #383.  The second patch ``trac4000_rebase_431rc0_383.patch`` is the main patch from this patch, which is now rebased on 4.3.1.rc0 *and* the first patch.  With this, the only remaining doctests failures are


```
sage -t  "devel/sage-qq/sage/combinat/species/composition_species.py"
**********************************************************************
File "/scratch/pancratz/sage-4.3.1.rc0/devel/sage-qq/sage/combinat/species/composition_species.py", line 235:
    sage: S.isotype_generating_series().coefficients(5) #indirect
Expected:
    [1, t, t^2 + t, t^3 + t^2 + t, t^4 + t^3 + 2*t^2 + t]
Got:
    [1, t, 1/2*t^2, 1/6*t^3, 1/24*t^4]
**********************************************************************
File "/scratch/pancratz/sage-4.3.1.rc0/devel/sage-qq/sage/combinat/species/composition_species.py", line 247:
    sage: Par.isotype_generating_series().coefficients(5)
Expected:
    [1, t, t^2 + t, t^3 + t^2 + t, t^4 + t^3 + 2*t^2 + t]
Got:
    [1, t, 1/2*t^2 + 1/2*t, 1/6*t^3 + 1/2*t^2 + 1/6*t, 1/24*t^4 + 1/4*t^3 + 7/24*t^2 + 1/24*t]
**********************************************************************
1 items had failures:
   2 of  15 in __main__.example_11
***Test Failed*** 2 failures.
For whitespace errors, see the file /home/pancratz/.sage//tmp/.doctest_composition_species.py
         [5.7 s]
exit code: 1024

----------------------------------------------------------------------
The following tests failed:


        sage -t  "devel/sage-qq/sage/combinat/species/composition_species.py"
```


I am not sure what's going on here.  Could someone else please take a look at this?

Thanks!

Sebastian


---

Comment by spancratz created at 2010-01-20 16:12:31

In addition to my earlier post, I seems there is a problem with the first patch (the one collecting the three patches from #383 for convenience), which I am sorry for.  Nonetheless, applying the three patches straight from that ticket and adding the second patch above yields the desired state, apart from the one remaining doctest.

Sebastian


---

Comment by spancratz created at 2010-01-20 23:15:22

The above ticket provided by Mike Hanses applies to 4.3.1.rc0 after applying the three tickets from #383.  We've tested on two separate machines and it passes all doctests.

Thanks to Mike for helping to track down the (hopefully) last remaining bug before lunchtime!

I'll go over the code again in the next week or two, adding further documentation and more doctests.  In the meantime, I would be very grateful if other people interested in reviewing it could start looking at the code and provide further comments.

Sebastian


---

Comment by spancratz created at 2010-01-20 23:15:22

Changing status from needs_work to needs_review.


---

Comment by spancratz created at 2010-01-21 03:26:00

In the above three patches, I've now added some further documentation and made cosmetic changes to the layout in some files.  I still want to add many more test cases for the polynomial arithmetic.  Please let me know if there is something else that you think I ought to change.

Sebastian


---

Comment by AlexGhitza created at 2010-01-23 00:26:38

Sebastian, I am marking this ticket as needs_work since you are saying that you want to add more tests.  Just mark it needs_review when you feel it's ready.


---

Comment by AlexGhitza created at 2010-01-23 00:26:38

Changing status from needs_review to needs_work.


---

Comment by malb created at 2010-01-23 12:39:05

`@`Sebastian, what do I have to apply in which order to test your patches? `@`Alex, we can probably start testing stuff except we shouldn't complain about missing doctests yet.


---

Comment by mhansen created at 2010-01-23 19:58:21

I believe all of the above patches in the order they appear.


---

Comment by spancratz created at 2010-01-23 20:41:42

Martin:  Yes, they should apply to 4.3.1.rc0 in the order they appear.  Although, after applying the main patch, there should be some choice on the order in which you apply the patches as they mostly (apart from fmpq_poly and fmpq_poly_alias) touch distinct sets of files, I think.

Morally speaking, this should definitely be ``needs_review`` (although I understand if someone would formally want to argue that this should be ``needs_work``), and it'd be great if you could let me know of any changes I should make, including doctests.  The ones I intend to add weren't for any specific method, but rather for the arithmetic in `\QQ[t]`, which I think would have to go to the top of the file ``polynomial_rational_flint`` since the methods themselves are in the polynomial template file.

Thanks,

Sebastian


---

Comment by AlexGhitza created at 2010-01-24 04:01:36

Changing status from needs_work to needs_review.


---

Comment by AlexGhitza created at 2010-01-24 04:01:36

Having applied all the patches, I'm getting:


```
sage: R.<x> = QQ[]
sage: S.<a> = R.quotient(3*x^3 + 3/2*x -1/3)
sage: 3 * a^3 + S.modulus()
Error: unable to alloc/realloc memory
/home/ghitza/sage-devel/local/bin/sage-sage: line 206: 13092 Aborted                 (core dumped) sage-ipython "$`@`" -i
```


(This is a doctest in `rings/polynomial/polynomial_quotient_ring_element.py`, which is how I ran into it.)

I don't know if it matters, but this is happening on a 32-bit machine.


---

Comment by spancratz created at 2010-01-24 14:40:38

There's clearly something dodgy going on here.  On my 32-bit laptop, with a clean 4.3.1.rc0 install and only the patches from this thread,


```
sage: R.<x> = QQ[]
sage: S.<a> = R.quotient(3*x^3 + 3/2*x -1/3)
sage: 3 * a^3 + S.modulus()
-3/2*a + 1/3
sage: timeit('_ = 3 * a^3 + S.modulus()')
5 loops, best of 3: 14.3 s per loop
```


That is, it takes forever...  Alex, could you perhaps elaborate on your setup?

Thanks,
Sebastian


---

Comment by spancratz created at 2010-01-25 00:11:48

Here is a simpler instance of the problem:

```
sage: R.<x> = QQ[]
sage: f = 3/2*x - 1/3
sage: %time _ = f % f
CPU times: user 5.67 s, sys: 0.17 s, total: 5.84 s
Wall time: 5.86 s
```


I do *not* think that the problem is a coercion problem.  After inserting "print" statements into the Cython code at various points, I instead think the code in the block from line 881 in fmpq_poly_linkage.pxi actually takes this long, although I do not understand at all why this might be the case.

The two lines at actually seem to take time (assuming that inserting "print" statements is a valid way to determine this) are

```
    fmpz_pow_ui(t, lead, m)
    fmpz_mul(r.den, t, a.den)
```

but, once again, I've got not clue why this might be the case.

Tomorrow or on Tuesday, I will try to reproduce the problem in plain C.  If I manage to do this, I'll forward it to Bill Hart.  If not, I wouldn't really know what else to look into.

Sebastian


---

Comment by AlexGhitza created at 2010-01-25 06:13:51

Replying to [comment:43 spancratz]:
> There's clearly something dodgy going on here.  On my 32-bit laptop, with a clean 4.3.1.rc0 install and only the patches from this thread,
> 
> {{{
> sage: R.<x> = QQ[]
> sage: S.<a> = R.quotient(3*x^3 + 3/2*x -1/3)
> sage: 3 * a^3 + S.modulus()
> -3/2*a + 1/3
> sage: timeit('_ = 3 * a^3 + S.modulus()')
> 5 loops, best of 3: 14.3 s per loop
> }}}

I've tried a couple more times and I'm still getting the memory problem followed by crash and core dump.  I'm running 32-bit archlinux on a Dell laptop, with version 4.4.2 of gcc.  It's a clean build of sage-4.3.1 with the patches here.

I also have a macbook running 64-bit archlinux.  It's busy doing other things now, but I can try to test this on it later.


---

Comment by AlexGhitza created at 2010-01-25 06:15:42

Replying to [comment:44 spancratz]:
> Here is a simpler instance of the problem:
> {{{
> sage: R.<x> = QQ[]
> sage: f = 3/2*x - 1/3
> sage: %time _ = f % f
> CPU times: user 5.67 s, sys: 0.17 s, total: 5.84 s
> Wall time: 5.86 s
> }}}

On my laptop, this gives me


```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: sage: R.<x> = QQ[]
sage: sage: f = 3/2*x - 1/3
sage: sage: %time _ = f % f
Error: unable to alloc/realloc memory
/opt/sage-4.3.1-archlinux-32bit-i686-Linux/local/bin/sage-sage: line 206: 17772 Aborted                 (core dumped) sage-ipython "$`@`" -i
```



---

Comment by spancratz created at 2010-01-28 23:31:01

I am sorry for only getting on with this today.  Just now I tried to re-produce the problem in plain C with FLINT, but needless to say, I didn't manage.  A simple-minded reproduction of the relevant code executed in no time and without any problems.  Currently, I am completely out of ideas on how to fix this problem.  That's why I'll raise the issue on sage-devel and conclude this message with a description of the behaviour that I experience on my machine (Lenovo T500 laptop, Intel Core2 Duo CPU, Ubuntu 9.10):

After applying all patches from this ticket to a 4.3.1.rc0 installation, modify the ``else`` block from line 882 in ``sage/libs/flint/fmpq_poly_linkage.pxi`` to the following:

```
            print "In case 3B"
            t = fmpz_init(limbs)
            print "den_fit_limbs"
            __fmpq_poly_den_fit_limbs(r, limbs + fmpz_size(a.den))
            print "pow_ui"
            fmpz_pow_ui(t, lead, m)
            print "mul"
            fmpz_mul(r.den, t, a.den)
            print "clear"
            fmpz_clear(t)
```

This only includes the ``print`` commands.

Then, upon executing the same sequence of commands that produce the crash in Alex' previous message, I receive the following output:

```
sage: R.<x> = QQ[]
sage: f = 3/2*x - 1/3
sage: %time _ = f % f
In case 3B
den_fit_limbs
pow_ui
mul
clear
CPU times: user 19.10 s, sys: 0.54 s, total: 19.64 s
Wall time: 19.72 s
```


What I find very strange (besides the fact that this takes 20s to obtain the correct result) is that there are two very noticeable delays of a couple of seconds, one after the output ``"pow_ui"``, and another after the output of ``"mul"``.

Sebastian


---

Comment by malb created at 2010-01-29 00:04:23

Did you do a sanity checks on the inputs to each function? E.g. what is `limbs`, What is `r`? What does `fmpz_size(a.den)` return? and so forth? Alex error message complains about some allocation not working so I'd assume some wrong size (negative or unitialised?) is passed to FLINT?


---

Comment by spancratz created at 2010-01-29 14:02:18

Hi Martin,

Thank you for joining in!  I've just done this now and posted on sage-devel.  The problem doesn't seem to be in fmpz_pow_ui or fmpz_mul, but in fmpz_poly_pseudo_divrem.  Well, I am not sure it's a problem in FLINT, since I couldn't reproduce it in plain C yet, but's related to that bit in the code rather than the later calls.

Sebastian


---

Comment by spancratz created at 2010-01-29 14:05:18

I've just uploaded a file which if applied adds some debug output.  If the file is copied into the directory ``devel/sage`` then from within the directory it can be applied via 


```
patch -p1 < trac4000_fmpz_poly_pseudo_divrem_debug.diff
```


Sebastian


---

Comment by spancratz created at 2010-01-30 01:20:23

Dear Alex,

I've just uploaded a patch which should fix problem you reported, which was related to a bug in FLINT that you stumbled upon (see sage-devel).  Is there anything else that you think I should change related to this ticket, at the moment?

Thank you very much again for looking at this!

Sebastian


---

Comment by AlexGhitza created at 2010-01-30 02:22:31

I have just applied your last patch, and I confirm that it gets rid of the nasty doctest failure.

I'd like to test this on some more machines to see if all is well.  And it will most likely have to be rebased, since it touches so many files.  For now I'll keep using 4.3.1, on which it applies fine.


---

Comment by cremona created at 2010-02-07 15:41:55

When there's a version which applies to 4.3.2 I'll be happy to test it too.


---

Comment by spancratz created at 2010-02-15 00:15:01

Dear John,

I am sorry I am only reading this now --- I was out of the country for a while this past week.  I am busy teaching on Monday and Tuesday, but I can hopefully (try to re-base) this to 4.3.2 in the second half of the week.

Thank you for offering your help with testing this,

Sebastian


---

Comment by cremona created at 2010-02-20 16:05:21

I think 7 consecutive patches is too much to ask -- please may we have a single combined patch?


---

Comment by spancratz created at 2010-02-27 00:40:01

I've just uploaded a new patch combining all previous ones, rebased to 4.3.3.  I am currently running a test with ``sage -t devel/sage/sage`` and I am certainly expecting the odd new doctest failure with 4.3.3, but overall I expect it to mostly work fine.  In any case, I will post the results tomorrow.

Sebastian


---

Comment by spancratz created at 2010-02-27 17:07:14


```
The following tests failed:

        sage -t  devel/sage/sage/rings/polynomial/infinite_polynomial_element.py # 1 doctests failed
        sage -t  devel/sage/sage/structure/parent.pyx # 2 doctests failed
```


More precisely,

```
sage -t  "devel/sage/sage/rings/polynomial/infinite_polynomial_element.py"
**********************************************************************
File "/home/suser/sage-4.3.3/devel/sage/sage/rings/polynomial/infinite_polynomial_element.py", line 853:
    sage: type(Z._P)
Expected:
    <class 'sage.rings.polynomial.multi_polynomial_ring.MPolynomialRing_polydict'>
Got:
    <class 'sage.rings.polynomial.multi_polynomial_ring.MPolynomialRing_polydict_domain'>
**********************************************************************
1 items had failures:
   1 of  12 in __main__.example_26
***Test Failed*** 1 failures.
For whitespace errors, see the file /home/suser/.sage//tmp/.doctest_infinite_polynomial_element.py
         [3.4 s]

----------------------------------------------------------------------
The following tests failed:


        sage -t  "devel/sage/sage/rings/polynomial/infinite_polynomial_element.py"
```

and

```
sage -t  "devel/sage/sage/structure/parent.pyx"                                                                                
**********************************************************************                                                         
File "/home/suser/sage-4.3.3/devel/sage/sage/structure/parent.pyx", line 162:                                                  
    sage: sage.structure.parent.raise_attribute_error(QQ[x].gen(), "bla")                                                      
Expected:                                                                                                                      
    Traceback (most recent call last):                                                                                         
    ...                                                                                                                        
    AttributeError: 'Polynomial_rational_dense' object has no attribute 'bla'                                                  
Got:                                                                                                                           
    Traceback (most recent call last):                                                                                         
      File "/home/suser/sage-4.3.3/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/suser/sage-4.3.3/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/suser/sage-4.3.3/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_2[3]>", line 1, in <module>
        sage.structure.parent.raise_attribute_error(QQ[x].gen(), "bla")###line 162:
    sage: sage.structure.parent.raise_attribute_error(QQ[x].gen(), "bla")
      File "parent.pyx", line 169, in sage.structure.parent.raise_attribute_error (sage/structure/parent.c:2611)
    AttributeError: 'sage.rings.polynomial.polynomial_rational_flint.Polynomial_rational_dense_flint' object has no attribute 'bla'
**********************************************************************
File "/home/suser/sage-4.3.3/devel/sage/sage/structure/parent.pyx", line 220:
    sage: getattr_from_other_class(QQ[x].one(), A, "lazy_attribute")
Exception raised:
    Traceback (most recent call last):
      File "/home/suser/sage-4.3.3/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/suser/sage-4.3.3/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/suser/sage-4.3.3/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_3[8]>", line 1, in <module>
        getattr_from_other_class(QQ[x].one(), A, "lazy_attribute")###line 220:
    sage: getattr_from_other_class(QQ[x].one(), A, "lazy_attribute")
      File "parent.pyx", line 245, in sage.structure.parent.getattr_from_other_class (sage/structure/parent.c:2953)
      File "/home/suser/sage-4.3.3/local/lib/python/site-packages/sage/misc/lazy_attribute.py", line 502, in __get__
        setattr(a, self.f.__name__, result)
    AttributeError: 'sage.rings.polynomial.polynomial_rational_flint.Polynomial_rational_dense_flint' object has no attribute 'lazy_attribute'
**********************************************************************
2 items had failures:
   1 of   4 in __main__.example_2
   1 of  10 in __main__.example_3
***Test Failed*** 2 failures.
For whitespace errors, see the file /home/suser/.sage//tmp/.doctest_parent.py
         [9.9 s]
```


I think the correct fix for the first problem is a change in the docstring, but I am not sure about this.  For the second one, the docstring needs to be changed.  And, finally, for the third one (about the lazy_attribute), I have no idea.

Can someone else please comment on this?

Many thanks,
Sebastian


---

Comment by malb created at 2010-03-07 16:39:43

Replying to [comment:57 spancratz]:
Hi, sorry for the late reply:



```
sage -t  "devel/sage/sage/rings/polynomial/infinite_polynomial_element.py"
**********************************************************************
    sage: type(Z._P)
Expected:
    <class 'sage.rings.polynomial.multi_polynomial_ring.MPolynomialRing_polydict'>
Got:
    <class 'sage.rings.polynomial.multi_polynomial_ring.MPolynomialRing_polydict_domain'>
**********************************************************************
```


If `Z._P` is over a domain, then yes change the doctest.


```
    sage: sage.structure.parent.raise_attribute_error(QQ[x].gen(), "bla")                                                      
Expected:                                                                                                                      
    Traceback (most recent call last):                                                                                         
    ...                                                                                                                        
    AttributeError: 'Polynomial_rational_dense' object has no attribute 'bla'                                                  
Got:                                                                                                                           
    Traceback (most recent call last):                                                                                         
      File "/home/suser/sage-4.3.3/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/suser/sage-4.3.3/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/suser/sage-4.3.3/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_2[3]>", line 1, in <module>
        sage.structure.parent.raise_attribute_error(QQ[x].gen(), "bla")###line 162:
    sage: sage.structure.parent.raise_attribute_error(QQ[x].gen(), "bla")
      File "parent.pyx", line 169, in sage.structure.parent.raise_attribute_error (sage/structure/parent.c:2611)
    AttributeError: 'sage.rings.polynomial.polynomial_rational_flint.Polynomial_rational_dense_flint' object has no attribute 'bla'
```


Yes, you need to change the doctest.


```
Exception raised:
    Traceback (most recent call last):
      File "/home/suser/sage-4.3.3/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/suser/sage-4.3.3/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/suser/sage-4.3.3/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_3[8]>", line 1, in <module>
        getattr_from_other_class(QQ[x].one(), A, "lazy_attribute")###line 220:
    sage: getattr_from_other_class(QQ[x].one(), A, "lazy_attribute")
      File "parent.pyx", line 245, in sage.structure.parent.getattr_from_other_class (sage/structure/parent.c:2953)
      File "/home/suser/sage-4.3.3/local/lib/python/site-packages/sage/misc/lazy_attribute.py", line 502, in __get__
        setattr(a, self.f.__name__, result)
    AttributeError: 'sage.rings.polynomial.polynomial_rational_flint.Polynomial_rational_dense_flint' object has no attribute 'lazy_attribute'
```


You probably need to implement `lazy_attribute`. I don't know what it is supposed to be doing, so you should ask on [sage-devel].


---

Comment by cremona created at 2010-04-05 15:47:37

Changing status from needs_review to needs_work.


---

Comment by cremona created at 2010-04-05 15:47:37

I just checked that the combined patch applies fine to 4.3.5.  I got just two doctest failures, as in the above report.  Otherwise all pass (64-bit ubuntu).

For parent.pyx: this must be the same thing as in #8332?  You could just delete that doctest, since it tests something on an essentailly random class to which it used to apply but no longer does.

Let's get these last two little things fixed, then this can at last get merged!


---

Comment by cremona created at 2010-04-30 14:24:09

On 4.4 there needs to be a little rebasing:

```
applying trac4000_433_combined.patch
patching file sage/rings/integer.pyx
Hunk #1 FAILED at 1688
1 out of 2 hunks FAILED -- saving rejects to file sage/rings/integer.pyx.rej
patching file sage/rings/polynomial/multi_polynomial_ideal.py
Hunk #1 succeeded at 2622 with fuzz 2 (offset 0 lines).
patching file sage/rings/polynomial/polynomial_element.pyx
Hunk #1 FAILED at 1096
1 out of 4 hunks FAILED -- saving rejects to file sage/rings/polynomial/polynomial_element.pyx.rej
patching file sage/rings/polynomial/polynomial_element_generic.py
Hunk #1 FAILED at 604
1 out of 1 hunks FAILED -- saving rejects to file sage/rings/polynomial/polynomial_element_generic.py.rej
patch failed, unable to continue (try -v)
patch failed, rejects left in working dir
errors during apply, please fix and refresh trac4000_433_combined.patch
```



---

Comment by spancratz created at 2010-05-26 09:05:56

Dear all,

For my own work, I have re-written the fmpq_poly_ methods in plain C with a FLINT-like interface and set up more detailed test routines (triggering essentially every line of code).  From memory (since I have the relevant sheets of paper on my desk in Oxford), as a result of that I found three possible memory leaks.

During the last few days, I was wondering whether it might be better to include this C code instead of the Cython code from the patch?  I somehow feel that this would be cleaner, however, this might just be me preferring C to Cython.

As for a possible schedule, I recently signed up to attend Sage Days 23 at Leiden, which might be a very convenient place to discuss this and work on the code as necessary.  Perhaps it might then be possible to review this at least before the end of Sage Days 24 in Linz, if not before that.

Best wishes,
Sebastian


---

Comment by robertwb created at 2010-05-27 22:19:40

Hi Sebastian, 

I was just wondering what was up with this ticket yesterday. If you think this is eventually going to make it into FLINT itself, it may be better to provide the C (or even a patched FLINT spkg). Otherwise, Cython is preferable as many more people in the Sage community will be able and willing to edit it. 

Given the history of this ticket, I would be more comfortable with first a very clean, straightforward implementation based on FLINT (without avoiding allocation at all costs, the NULL denominator savings, etc.) and get that fully vetted, refereed, and in. Hopefully that should be a simpler task (i.e. less endless chasing down segfaults, random doctest failures, and a much simpler referee process with a high confidence in the correctness of the implementation). That should (I'd guess) already be a significant performance improvement (right?). Once we've done that, then we can go ahead and optimize things further.


---

Comment by spancratz created at 2010-07-03 22:42:42

Hi Robert,

Thank you for the suggestions.  I've been in touch with Bill Hart and he is quite keen to have a module for Q[t] in FLINT.  Given this, I think the following seems sensible:

  - Make a separate spkg for Q[t] on top of FLINT
  - Check that the interface for Q[t] is such that it will require as little work as possible during the antipated change from FLINT 1 to FLINT 2
  - Go over the C code again, simplifying the fmpz_t memory management where possible, since this won't be necessary in FLINT 2 any more
  - Go over the documentation again
  - Add further test cases

I'm happy to do all the work on the C side of things.  Hopefully, I can ask someone for help regarding the Sage spkg side of things at the workshop in Leiden.

Best wishes,
Sebastian


---

Comment by was created at 2010-07-21 12:21:04

On sage.math, qq.patch applies to sage-4.5 and passes all tests except the pickling test:

```
The following tests failed:

        sage -t  -long devel/sage/sage/misc/explain_pickle.py # 2 doctests failed
        sage -t  -long devel/sage/sage/structure/sage_object.pyx # 0 doctests failed
```


And it's damned fast, compared to what is in sage now:

```
sage: R.<x> = QQ[]
sage: f = R.random_element(degree=100)
sage: timeit('f*f')
625 loops, best of 3: 29 µs per loop
sage: S.<x> = PolynomialRing(QQ,implementation='ntl')
sage: g = S.random_element(degree=100)
sage: timeit('g*g')
625 loops, best of 3: 1.29 ms per loop
sage: 1.29/0.029
44.4827586206897
sage: f = R.random_element(degree=1000)
sage: g = S.random_element(degree=1000)
sage: timeit('f*f')
625 loops, best of 3: 1.31 ms per loop
sage: timeit('g*g')
5 loops, best of 3: 104 ms per loop
sage: 104/1.31
79.3893129770992
```



---

Comment by malb created at 2010-07-21 14:10:19

Comments

 * add copyright note to sage/libs/flint/fmpq_poly.pxd
 * delete old example module
 * add copyright note to polynomial/polynomial_rational_flint.pxd
 * add class docstring to Polynomial_rational_flint and to the file
 * There are many r""" which aren't needed
 * !__init!__ doesn't document parameters
 * many functions need docstrings
 * ell_foo.py remove?
 * remove the explicit implementation="FLINT" stuff?


---

Comment by spancratz created at 2010-07-24 14:39:29

Hi Martin,

Thank you for the feedback.  I've just uploaded three separate patches.  I'd be grateful if you could have another look at the main patch file and provide some more feedback!

Please note that at the moment there are a few test failures, which weren't there before, but I'll fix them during the next few days and upload another patch then.

Thanks,
Sebastian


---

Comment by spancratz created at 2010-07-26 00:35:40

Changing status from needs_work to needs_review.


---

Comment by spancratz created at 2010-07-26 00:35:40

Dear all,

I've uploaded a set of four patches now, which can be applied in any order.  They should pass all doctests, although on sage.math there is an error as follows


```
    sage -t  "devel/sage-qq/sage/rings/polynomial/polynomial_rational_flint.pyx"
    Error: unable to alloc/realloc memory
```


I do not know why this error is there since this test works just fine for me on my laptop.

The test failures I mentioned in the earlier post have all been resolved.

Sebastian


---

Comment by schilly created at 2010-07-26 11:32:39

Changing status from needs_review to needs_work.


---

Comment by schilly created at 2010-07-26 11:32:39

i tested on ubuntu 9.04 32bit, Intel(R) Core(TM)2 Duo CPU and gcc version 4.3.3 (Ubuntu 4.3.3-5ubuntu4) ... 2 times the same failure in "en" and "fr" tutorial:


```
File "/scratch/scratch/schilly/sage/sage-4.5/devel/sage/doc/en/tutorial/tour_polynomial.rst", line 166:
    sage: R.<x> = PolynomialRing(QQ)
    sage: S.<y> = PolynomialRing(QQ)
    sage: x == y
Expected:
    False
Got:
    True
```



---

Comment by spancratz created at 2010-07-26 16:26:20

Hi Harald,

Thank you for testing this.  The easiest way to deal with this is to simply leave the current behaviour unchanged by not overwriting ``hash`` or any of the comparison methods.  This is a bit of a shame since the C-based test for equality should be much faster than the inherited method, but I think it is the sensible decision at this point.  I will update the patches accordingly later.

Sebastian


---

Comment by spancratz created at 2010-07-26 20:54:44

The ticket now consists of five patches:

#. trac4000_0.patch
#. trac4000_1.patch
#. trac4000_doctest_output.patch
#. trac4000_fmpq_poly_c.patch
#. trac4000_fmpq_poly_pxd.patch

Only 0 and 1 have to be applied in this order.  The remaining patches can be applied in any order.  After having removed the methods for comparisons (which caused a problem as Harald noticed above), these should now hopefully be very, very close to finalised.  I've also included the signal handling around most C library calls.

Best wishes, and many thanks for looking at this ticket!

Sebastian

PS:  Perhaps someone with the appropriate rights could delete all the unnecessary attachments to this ticket?  I don't think we need the earlier ones any more.  In any case, I accidentally added this one, ``trac4000_fmpq_poly_c.2.patch``.


---

Comment by spancratz created at 2010-07-26 20:54:44

Changing status from needs_work to needs_review.


---

Comment by rlm created at 2010-07-27 08:09:25

Replying to [comment:70 spancratz]:
> PS:  Perhaps someone with the appropriate rights could delete all the unnecessary attachments to this ticket?  I don't think we need the earlier ones any more.  In any case, I accidentally added this one, ``trac4000_fmpq_poly_c.2.patch``.

Done.


---

Comment by rlm created at 2010-07-27 08:44:09

Some minor quibbles:

 1. You might want to clean up the commit messages in the patches. Right now they don't include the ticket number, etc. If you're using queues this is `hg qrefresh -e` when the relevant patch is at the top of the applied part of the queue.

 2. I'm not sure it's necessary to have things like

```
NOTES: 

    (S Pancratz)  Extracted from polynomial_template.pxi. 
```

since the files are all under revision control, and in fact every line has a list of authors associated to it.

 3. It might be useful to have the cimports and the imports in separate blocks, since the cimports happen at compile time, and the imports happen at runtime, frequently on startup.


---

Comment by spancratz created at 2010-07-27 12:05:45

Hi Robert,

Thanks for the suggestions.  As for 1), yes, I'll do that.  The note in 2) should have disappeared (along with the method __hash__) by applying trac4000_1.patch.  Finally, I'll do 3), too.  That said, I'm about to begin catching up on more than a week's administrative work, so I'll probably upload new patches very late tonight.

Sebastian


---

Comment by spancratz created at 2010-07-27 22:03:14

I've now made the changes that Robert suggested.


---

Comment by spancratz created at 2010-07-31 23:02:53

Main patch


---

Attachment

fmpq_poly.c and header


---

Attachment

fmpq_poly.pxd


---

Comment by schilly created at 2010-08-01 21:34:41

Hi, william's nagbot reminded me of this here and I installed these last 3 patches on my 4.5.2 RC build. I tried to replicate your timings, but they are less convincing than I thought:


```
sage: S = PolynomialRing(QQ, 'x', implementation="flint")
sage: R = PolynomialRing(QQ, 'y', implementation="NTL")
sage: f = R.random_element(degree=30); timeit('f*f')
625 loops, best of 3: 15.6 µs per loop
sage: g = S.random_element(degree=30); timeit('g*g')
625 loops, best of 3: 14.7 µs per loop
sage: f = R.random_element(degree=300); timeit('f*f')
625 loops, best of 3: 602 µs per loop
sage: g = S.random_element(degree=300); timeit('g*g')
625 loops, best of 3: 350 µs per loop
sage: f = R.random_element(degree=3000); timeit('f*f')
25 loops, best of 3: 15.2 ms per loop
sage: g = S.random_element(degree=3000); timeit('g*g')
25 loops, best of 3: 19.5 ms per loop
sage: f = R.random_element(degree=3000); timeit('f*f')
25 loops, best of 3: 16.3 ms per loop
sage: g = S.random_element(degree=3000); timeit('g*g')
25 loops, best of 3: 14.3 ms per loop
sage: f = R.random_element(degree=30000); timeit('f*f')
5 loops, best of 3: 1.03 s per loop
sage: g = S.random_element(degree=30000); timeit('g*g')
5 loops, best of 3: 1.04 s per loop
sage: f = R.random_element(degree=30000); timeit('f*f')
5 loops, best of 3: 995 ms per loop
sage: g = S.random_element(degree=30000); timeit('g*g')
5 loops, best of 3: 1.09 s per loop
```


Maybe I did something wrong?

I also got this doctest error (my RC built w/o any errors) when checking the rings/polynomial dir.


```
File "/scratch/scratch/schilly/sage/sage-4.5.2.rc0/devel/sage-main/sage/rings/polynomial/polynomial_element.pyx", line 474:
    sage: f(x) is f
Expected:
    True
Got:
    False
```


Btw, the doctest failure in the tutorial I reported earlier is fixed.

The system were I did run this is Ubuntu 8.10 32 bit, gcc version 4.3.2 (Ubuntu 4.3.2-1ubuntu12),  Intel(R) Core(TM)2 Quad CPU    Q9400


---

Comment by spancratz created at 2010-08-01 23:25:18

Hi Harald,

Thank you for looking at this again.  The timings you provide are all obtained by the new implementation.  For example, multiplying to degree 3000 polynomials takes 15ms with the new implementation as you show, but took 600ms before as explained in the description at the top of this ticket! --- And this is the advertised improvement by a factor of 40 in a basic arithmetic operation :)

This is because the implementation is provided alongside the old, it is simply a drop in replacement for the old one.  Using the parameter "implementation" doesn't raise an error, but it doesn't do anything useful either.

So far, I have only tested the patch against Sage 4.4.4 and so I can't comment on the last problem that you mention.  I will look at that soon.  As a preliminary opinion I believe that the test is a very bad one:  I can see that f(x) == f should return true.  However, I do not think that f(x) is f should return true.  After all, f(g) for any other g, e.g. g = x*x, returns a new polynomial object.

Many thanks for looking at this,

Sebastian


---

Comment by schilly created at 2010-08-02 10:24:18

Ah ok, lol. I've also complete a ptestlong and it's just this f(x) is or == f thing. I also think that this depends on what f is. if f is already an "f(x)" then f(x) should be the same as f, otherwise not. Behind the scene it is symbolic_expression(f).function(x) and I can only speculate that it makes sense to make this function behave idempotent, but only in special cases. Sorry that I don't know more about this and I also cannot comment on the code itself, apart from that it is apparently working for me ;)


---

Comment by rlm created at 2010-08-03 21:18:46

I get the following error:

```
sage -t -long "devel/sage-main/sage/rings/polynomial/polynomial_rational_flint.pyx"
Error: unable to alloc/realloc memory
**********************************************************************
File "/scratch/rlmill/sage-4.5.1.vg/devel/sage-main/sage/rings/polynomial/polynomial_rational_flint.pyx", line 992:
    sage: (1 + t)^(2^31)
Expected:
    Traceback (most recent call last):
    ...
    OverflowError: long int too large to convert to int
Got:
    Traceback (most recent call last):
      File "/scratch/rlmill/sage-4.5.1.vg/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/rlmill/sage-4.5.1.vg/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/rlmill/sage-4.5.1.vg/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_32[11]>", line 1, in <module>
        (Integer(1) + t)**(Integer(2)**Integer(31))###line 992:
    sage: (1 + t)^(2^31)
    RuntimeError
**********************************************************************
```



---

Comment by spancratz created at 2010-08-04 14:50:38

Hi Robert and Harald,

Thank you for looking at this.

About the first problem (the ``f(x) is f`` issue), I won't fix this on this ticket yet since I believe this doctest simply should not be merged into 4.5.2 and I don't want to play catching up with the moving target that a current release candidate is.  If this doctest does end up getting into 4.5.2, I'll adjust it on this ticket as soon as 4.5.2 is out.

The second problem Robert mentions is a 32-bit versus 64-bit issue.  I'm sorry I've missed this, in particular since in the same file there is a similar issue already which I did attend to.  Anyway, I've got an updated patch (just replacing ``31`` by ``64``) which I'll upload later.  With this, all tests pass on sage.math.

Thanks again,

Sebastian

PS:  I'm sorry for the delay in replying to this.  I've been very busy working on FLINT2, but that now compiles with ``-ansi -pedantic -Wall -Werror`` :)


---

Comment by rlm created at 2010-08-06 15:55:37

Seb,

Replying to [comment:79 spancratz]:
> PS:  I'm sorry for the delay in replying to this.  I've been very busy working on FLINT2, but that now compiles with ``-ansi -pedantic -Wall -Werror`` :)

Nice work! I think that once the 32/64 bit issue is fixed, this should be ready to go, and unless anyone else objects, I'll move it to positive review once that's finished. I think this is an impressive bit of work and definitely needs to be merged before bits start rotting.


---

Comment by was created at 2010-08-11 18:21:08

fix the 32/64-bit doctest that Robert found... thus hopefully meaning this is ready for positive review!


---

Attachment

Replying to [comment:80 rlm]:
> Nice work! I think that once the 32/64 bit issue is fixed, this should be ready to go, and unless anyone else objects, I'll move it to positive review once that's finished.

I posted a patch that finishes the 32/64 bit issue.


---

Attachment

there was another issue with an "is" in a doctest...


---

Comment by was created at 2010-08-11 18:56:06

I can give this a positive review, since I didn't write it, and I'm just adding two trivial patches exactly as discussed above.


---

Comment by was created at 2010-08-11 18:56:06

Changing status from needs_review to positive_review.


---

Comment by spancratz created at 2010-08-22 16:52:07

I'm sorry I didn't post on this ticket in a while.  Just this afternoon I had a quick look at how this patch played with 4.5.3.alpha1 and I was going to make exactly the changes that William has made already --- as I notice now!

In any case, a big THANK YOU for finally pushing this one over the line,

Sebastian


---

Comment by mpatel created at 2010-09-15 11:13:55

Resolution: fixed


---

Comment by mpatel created at 2010-09-16 22:56:57

Changing status from closed to new.


---

Comment by mpatel created at 2010-09-16 22:56:57

Resolution changed from fixed to 


---

Comment by mpatel created at 2010-09-16 22:56:57

I get a build error on the Solaris machines t2.math and {fulvia,mark,mark2}.skynet:

```
building 'sage.rings.polynomial.polynomial_rational_flint' extension
gcc -fno-strict-aliasing -g -O2 -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -fPIC -I/home/mpatel/build/fulvia/sage-4.6.alpha1/local/include/FLINT/ -I/home/mpatel/build/fulvia/sage-4.6.alpha1/devel/sage/sage/libs/flint/ -I/home/mpatel/build/fulvia/sage-4.6.alpha1/local//include -I/home/mpatel/build/fulvia/sage-4.6.alpha1/local//include/csage -I/home/mpatel/build/fulvia/sage-4.6.alpha1/devel//sage/sage/ext -I/home/mpatel/build/fulvia/sage-4.6.alpha1/local/include/python2.6 -c sage/rings/polynomial/polynomial_rational_flint.cpp -o build/temp.solaris-2.10-i86pc-2.6/sage/rings/polynomial/polynomial_rational_flint.o -std=c99 -D_XPG6 -w
cc1plus: warning: command line option "-Wstrict-prototypes" is valid for Ada/C/ObjC but not for C++
In file included from /usr/include/limits.h:18:0,
                 from /usr/local/gcc-4.5.1/x86_64-SunOS-core2-sun-ld/lib/gcc/i386-pc-solaris2.10/4.5.1/include-fixed/limits.h:169,
                 from /usr/local/gcc-4.5.1/x86_64-SunOS-core2-sun-ld/lib/gcc/i386-pc-solaris2.10/4.5.1/include-fixed/syslimits.h:7,
                 from /usr/local/gcc-4.5.1/x86_64-SunOS-core2-sun-ld/lib/gcc/i386-pc-solaris2.10/4.5.1/include-fixed/limits.h:34,
                 from /home/mpatel/build/fulvia/sage-4.6.alpha1/local/include/python2.6/Python.h:19,
                 from sage/rings/polynomial/polynomial_rational_flint.cpp:4:
/usr/local/gcc-4.5.1/x86_64-SunOS-core2-sun-ld/lib/gcc/i386-pc-solaris2.10/4.5.1/include-fixed/sys/feature_tests.h:345:2: error: #error "Compiler or options invalid; UNIX 03 and POSIX.1-2001 applications     require the use of c99"
error: command 'gcc' failed with exit status 1
sage: There was an error installing modified sage library code.
```


I'm reopening this ticket.  Unless someone can post a patch within a day or so, I'll "unmerge" the changes from 4.6.alpha1.

There are also some doctest errors...


---

Comment by mpatel created at 2010-09-16 23:01:38

I get this error on sage.math and several other Sage cluster and Skynet machines on which 4.6.alpha1 builds successfully:

```
sage -t -long  devel/sage/sage/rings/polynomial/polynomial_rational_flint.pyx
**********************************************************************
File "/mnt/usb1/scratch/mpatel/tmp/sage-4.6.alpha1/devel/sage-main/sage/rings/polynomial/polynomial_rational_flint.pyx", line 1549:
    sage: R((x-1)*(x+1)).hensel_lift(7, 2)
Exception raised:
    Traceback (most recent call last):
      File "/mnt/usb1/scratch/mpatel/tmp/sage-4.6.alpha1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/mnt/usb1/scratch/mpatel/tmp/sage-4.6.alpha1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/mnt/usb1/scratch/mpatel/tmp/sage-4.6.alpha1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_44[3]>", line 1, in <module>
        R((x-Integer(1))*(x+Integer(1))).hensel_lift(Integer(7), Integer(2))###line 1549:
    sage: R((x-1)*(x+1)).hensel_lift(7, 2)
      File "polynomial_rational_flint.pyx", line 1588, in sage.rings.polynomial.polynomial_rational_flint.Polynomial_rational_flint.hensel_lift (sage/rings/polynomial/polynomial_rational_flint.cpp:12625)
        H = self._pari_().polhensellift(y, p, e)
      File "gen.pyx", line 9460, in sage.libs.pari.gen._pari_trap (sage/libs/pari/gen.c:45047)
    PariError:  (5)
```

Is this easy to fix?


---

Comment by mhansen created at 2010-09-16 23:04:14

For the Solaris / fulvia issue, what if you change the "-std=c99" in module_list.py to "-std=gnu99" ?


---

Comment by mpatel created at 2010-09-16 23:05:39

I get these doctest errors on sage.math and several other Sage cluster and Skynet machines on which 4.6.alpha1 builds successfully:

```python
sage -t -long  devel/sage/sage/graphs/generic_graph.py
**********************************************************************
File "/mnt/usb1/scratch/mpatel/tmp/sage-4.6.alpha1/devel/sage-main/sage/graphs/generic_graph.py", line 6563:
    sage: dsc = sage.rings.polynomial.polynomial_element_generic.Polynomial_rational_dense.discriminant
Exception raised:
    Traceback (most recent call last):
      File "/mnt/usb1/scratch/mpatel/tmp/sage-4.6.alpha1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/mnt/usb1/scratch/mpatel/tmp/sage-4.6.alpha1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/mnt/usb1/scratch/mpatel/tmp/sage-4.6.alpha1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_98[12]>", line 1, in <module>
        dsc = sage.rings.polynomial.polynomial_element_generic.Polynomial_rational_dense.discriminant###line 6563:
    sage: dsc = sage.rings.polynomial.polynomial_element_generic.Polynomial_rational_dense.discriminant
    AttributeError: 'module' object has no attribute 'Polynomial_rational_dense'
**********************************************************************
File "/mnt/usb1/scratch/mpatel/tmp/sage-4.6.alpha1/devel/sage-main/sage/graphs/generic_graph.py", line 6564:
    sage: K.vertices(key=dsc)
Exception raised:
    Traceback (most recent call last):
      File "/mnt/usb1/scratch/mpatel/tmp/sage-4.6.alpha1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/mnt/usb1/scratch/mpatel/tmp/sage-4.6.alpha1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/mnt/usb1/scratch/mpatel/tmp/sage-4.6.alpha1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_98[13]>", line 1, in <module>
        K.vertices(key=dsc)###line 6564:
    sage: K.vertices(key=dsc)
    NameError: name 'dsc' is not defined
```

The second just follows from the first.


---

Comment by mpatel created at 2010-09-16 23:35:15

Replying to [comment:87 mhansen]:
> For the Solaris / fulvia issue, what if you change the "-std=c99" in module_list.py to "-std=gnu99" ?

I get the same error message.


---

Comment by mpatel created at 2010-09-17 00:50:08

By the way, the unofficial, trial 4.6.alpha1 is in `/home/release/sage-4.6.alpha1` on the Sage cluster.


---

Comment by mpatel created at 2010-09-17 01:00:16

Changing status from new to needs_work.


---

Comment by mpatel created at 2010-09-17 01:00:16

David, do you have any thoughts about [comment:85 comment 85ff]?


---

Comment by drkirkby created at 2010-09-17 01:18:38

Replying to [comment:91 mpatel]:
> David, do you have any thoughts about [comment:85 comment 85ff]?

It looks like the compiler is compiling for a different standard to what the code is. Changing to C99 mode might cure it, but that can cause problems too, as some code may not compile in C99 mode - there are some compatibility issues. 

The Solaris headers are stricter than the Linux ones, so something things that you can get away with on linux, you can't on Solaris. For example, the macro infinity is not defined until C99, but linux header seems to define it irrespective of what mode the compiler is in. For Solaris, the compiler will have to be set to C99 otherwise it wont work. 

I've no idea precisely what the problem is here, as others have suggested, it looks like the code does not agree with what the compiler is set to.


---

Comment by mpatel created at 2010-09-17 02:14:17

From around line 345 of Skynet's `/usr/local/gcc-4.5.1/x86_64-SunOS-core2-sun-ld/lib/gcc/i386-pc-solaris2.10/4.5.1/include-fixed/sys/feature_tests.h`:

```c
/*
 * It is invalid to compile an XPG3, XPG4, XPG4v2, or XPG5 application
 * using c99.  The same is true for POSIX.1-1990, POSIX.2-1992, POSIX.1b,
 * and POSIX.1c applications. Likewise, it is invalid to compile an XPG6
 * or a POSIX.1-2001 application with anything other than a c99 or later
 * compiler.  Therefore, we force an error in both cases.
 */
#if defined(_STDC_C99) && (defined(__XOPEN_OR_POSIX) && !defined(_XPG6))
#error "Compiler or options invalid for pre-UNIX 03 X/Open applications \
        and pre-2001 POSIX applications"
#elif !defined(_STDC_C99) && \
        (defined(__XOPEN_OR_POSIX) && defined(_XPG6))
#error "Compiler or options invalid; UNIX 03 and POSIX.1-2001 applications \
        require the use of c99"
#endif
```



---

Comment by mpatel created at 2010-09-17 08:56:50

Replying to [comment:89 mpatel]:
> Replying to [comment:87 mhansen]:
> > For the Solaris / fulvia issue, what if you change the "-std=c99" in module_list.py to "-std=gnu99" ?
> 
> I get the same error message.

For what it's worth, dropping `-D_XPG6` allows `sage -b` and the build to finish on fulvia.  I'm running the tests now.


---

Comment by mpatel created at 2010-09-17 10:28:15

Replying to [comment:94 mpatel]:
> Replying to [comment:89 mpatel]:
> > Replying to [comment:87 mhansen]:
> > > For the Solaris / fulvia issue, what if you change the "-std=c99" in module_list.py to "-std=gnu99" ?
> > 
> > I get the same error message.
> 
> For what it's worth, dropping `-D_XPG6` allows `sage -b` and the build to finish on fulvia.  I'm running the tests now.

The long doctests pass, except for the errors I mentioned above, #9916, and #9924.


---

Comment by leif created at 2010-09-17 21:42:36

Replying to [comment:92 drkirkby]:
> Replying to [comment:91 mpatel]:
> > David, do you have any thoughts about [comment:85 comment 85ff]?
> 
> It looks like the compiler is compiling for a different standard to what the code is. Changing to C99 mode might cure it, but that can cause problems too, as some code may not compile in C99 mode - there are some compatibility issues. 
> 
> The Solaris headers are stricter than the Linux ones, so something things that you can get away with on linux, you can't on Solaris. For example, the macro infinity is not defined until C99, but linux header seems to define it irrespective of what mode the compiler is in. For Solaris, the compiler will have to be set to C99 otherwise it wont work. 

How does one compile C++ with `-std=c99`? ;-)


---

Comment by leif created at 2010-09-18 06:08:40

Replying to [comment:86 mpatel]:
> I get this error on sage.math and several other Sage cluster and Skynet machines on which 4.6.alpha1 builds successfully:

```
sage -t -long  devel/sage/sage/rings/polynomial/polynomial_rational_flint.pyx
**********************************************************************
File "/mnt/usb1/scratch/mpatel/tmp/sage-4.6.alpha1/devel/sage-main/sage/rings/polynomial/polynomial_rational_flint.pyx", line 1549:
    sage: R((x-1)*(x+1)).hensel_lift(7, 2)
Exception raised:
    Traceback (most recent call last):
      File "/mnt/usb1/scratch/mpatel/tmp/sage-4.6.alpha1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/mnt/usb1/scratch/mpatel/tmp/sage-4.6.alpha1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/mnt/usb1/scratch/mpatel/tmp/sage-4.6.alpha1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_44[3]>", line 1, in <module>
        R((x-Integer(1))*(x+Integer(1))).hensel_lift(Integer(7), Integer(2))###line 1549:
    sage: R((x-1)*(x+1)).hensel_lift(7, 2)
      File "polynomial_rational_flint.pyx", line 1588, in sage.rings.polynomial.polynomial_rational_flint.Polynomial_rational_flint.hensel_lift (sage/rings/polynomial/polynomial_rational_flint.cpp:12625)
        H = self._pari_().polhensellift(y, p, e)
      File "gen.pyx", line 9460, in sage.libs.pari.gen._pari_trap (sage/libs/pari/gen.c:45047)
    PariError:  (5)
```

> Is this easy to fix?

*No! * (I wonder who decided to give such error messages.)

----

There are at least two ways to fix this, either in the Sage library:

```diff
diff --git a/sage/libs/pari/gen.pyx b/sage/libs/pari/gen.pyx
--- a/sage/libs/pari/gen.pyx
+++ b/sage/libs/pari/gen.pyx
`@``@` -7025,7 +7025,7 `@``@`
         t0GEN(y)
         t1GEN(p)
         _sig_on
-        return self.new_gen(polhensellift(self.g, t0, t1, e))
+        return self.new_gen(polhensellift(self.g, lift(t0), t1, e))
 
     def polisirreducible(self):
         """
```

or "upstream" / in the PARI 2.4.3.svn-12577.* spkg (e.g. in #9876's `.p6`, too):

```diff
diff --git a/src/src/modules/Hensel.c b/src/src/modules/Hensel.c
--- a/src/src/modules/Hensel.c
+++ b/src/src/modules/Hensel.c
`@``@` -394,6 +394,7 `@``@`
   if (N < 1) pari_err(talker, "not a positive exponent in polhensellift");
 
   l = lg(L); L = leafcopy(L);
+  L = lift(L); /* make sure the coeffs are integers and not intmods */
   for (i = 1; i < l; i++)
   {
     if (typ(gel(L,i)) != t_POL)
```


Probably someone more knowledgeable could fix this in a better way.


---

Attachment

Fixes issue with hensel_lift()


---

Comment by jdemeyer created at 2010-09-18 20:00:58

Replying to [comment:86 mpatel]:
> Is this easy to fix?

Yes, see patch.  Note that I have not tested this patch yet against the rest of Sage.


---

Comment by jdemeyer created at 2010-09-18 20:00:58

Changing status from needs_work to needs_review.


---

Comment by jdemeyer created at 2010-09-18 20:51:33

Replying to [comment:97 leif]:
> (I wonder who decided to give such error messages.)

This is one of the issues with PARI I would like to address, but it won't be soon.


---

Comment by mpatel created at 2010-09-18 21:33:44

I'm "unmerging" this from 4.6.alpha1, since alpha1 is otherwise almost ready to release.  We'll still have a 4.6.alpha2 into which I can merge this important and long-awaited improvement.

I can't test Jeroen's patch now.  The `generic_graph.py` error appears easy to fix.  We just need to get `sage -b` to succeed on Solaris.


---

Comment by drkirkby created at 2010-09-18 22:11:27

Replying to [comment:96 leif]:
> Replying to [comment:92 drkirkby]:

> > The Solaris headers are stricter than the Linux ones, so something things that you can get away with on linux, you can't on Solaris. For example, the macro infinity is not defined until C99, but linux header seems to define it irrespective of what mode the compiler is in. For Solaris, the compiler will have to be set to C99 otherwise it wont work. 
> 
> How does one compile C++ with `-std=c99`? ;-)

It would be a lot less confusing if people used gcc to compile C and g++ to compile C++. What next, g++ to compile Fortran? 

It would be nice to get rid of the endless warnings like:


```
cc1plus: warning: command line option "-Wstrict-prototypes" is valid for Ada/C/ObjC but not for C++
```



---

Comment by mpatel created at 2010-09-18 23:12:48

The failures in `generic_graph.py` stem from the newly merged #9741.  I've added a comment there.


---

Comment by mpatel created at 2010-09-18 23:43:49

I asked Bill Hart, FLINT's lead developer, about the Solaris error.  He replied:

```
>> It looks to me like _STDC_C99 is not defined by the compiler on this
>> platform. Due to a bug in Solaris's headers, this causes it to fail.
>>
>> You *might* be able to work around it with one of the following fixes:
>>
>> 1) pass -std=gnu99 instead of -std=c99 (I do not guarantee flint will
>> compile with this flag)
>>
>> 2) don't pass XPG6 (it's technically correct, but triggers the bug, basically)
>>
>> 3) pass -stdc=c99 (I am unsure if this will work)
>>
>> If none of those work, I suggest you report the bug to Sun. It is
>> certainly not a flint bug.
```

(I've reproduced this with Bill's permission.)  Thoughts?


---

Comment by drkirkby created at 2010-09-19 00:22:47

Using Google, there are plenty of references to the fact `_STDC_C99` should not be defined for C++, only C99. But this is C++ code.


---

Comment by drkirkby created at 2010-09-19 01:00:21

BTW, in the next week or so I should be able to try this on AIX 5.3 with the IBM C and C++ compilers. That would bypass gcc/g++ and Solaris headers. It would be a *completely* different build environment. It would be interesting to see what happens there. 

Does anyone have a copy of the latest C and C++ standards? 

Dave


---

Comment by mpatel created at 2010-09-19 06:50:45

Changing priority from major to blocker.


---

Comment by mpatel created at 2010-09-19 06:51:10

Changing status from needs_review to needs_work.


---

Comment by mpatel created at 2010-09-19 06:52:47

I've changed the status to "needs work", because we still need fixes for the other problems.


---

Comment by leif created at 2010-09-19 11:52:04

Replying to [comment:101 drkirkby]:
> It would be a lot less confusing if people used gcc to compile C and g++ to compile C++. What next, g++ to compile Fortran? 

Note that `gcc` is not the C compiler, but a compiler _driver_ (and GCC is the GNU _Compiler Collection_, renamed years ago).

So it's in general pretty ok to use `gcc` to preprocess, assemble or link files, compile C, C++ or even Fortran files with `gcc`, but one should pass the appropriate options (and e.g. libraries that are _not_ added by default in that case) depending on the source language.

Of course using `gjc` for Java, `g++` for C++ and `gfortran` for Fortran is less confusing (and perhaps less error-prone).

> It would be nice to get rid of the endless warnings like:
> 

```
cc1plus: warning: command line option "-Wstrict-prototypes" is valid for Ada/C/ObjC but not for C++
```


Again _ceterum censeo ..._ (I don't recall how often I complained about that).

Also, (besides `libcsage.*`) `libstdc++.*` is linked to each and every extension module regardless of the `language`.

Note also that the XPG6 / C99 issue is not an upstream (FLINT) problem, since FLINT is C, not C++, but we compile FLINT source code as C++.

In addition, the Solaris headers are patched by GCC's `fix-includes`, so I'm not sure who's to blame for the failure. The relevant test should certainly also make a distinction on C++.


---

Comment by mpatel created at 2010-09-20 10:42:13

On the Solaris build error: From `SAGE_ROOT/devel/sage/module_list.py`:

```python
    Extension('sage.rings.polynomial.polynomial_rational_flint',
              sources = ['sage/rings/polynomial/polynomial_rational_flint.pyx', 'sage/libs/flint/fmpq_poly.c'],
              language = 'c++',
              extra_compile_args=["-std=c99", "-D_XPG6"],
              libraries = ["csage", "flint", "ntl", "gmpxx", "gmp"],
              include_dirs = [SAGE_ROOT + '/local/include/FLINT/', SAGE_ROOT + '/devel/sage/sage/libs/flint/'],
              depends = [SAGE_ROOT + "/local/include/FLINT/flint.h"]),
```

If I understand correctly (and to recap, somewhat):

 * The `language` option just tells Cython to create a C++ file `polynomial_rational_flint.cpp` from the Cython file `polynomial_rational_flint.pyx`, so that we can compile the .cpp file with NTL's C++ headers, etc.
 * The `extra_compile_args` here are really only for compiling the C99 file `fmpq_poly.c`.  But distutils also uses them (and `-Wstrict-prototypes`) to compile `polynomial_rational_flint.cpp`, too.  This can give the warnings

```
cc1plus: warning: command line option "-std=c99" is valid for C/ObjC but not for C++
cc1plus: warning: command line option "-Wstrict-prototypes" is valid for Ada/C/ObjC but not for C++
```

 * We need `-std=c99` to compile the C99 file `fmpq_poly.c`.  Using `-std=gnu99` instead, gives, e.g.,

```
In file included from /usr/include/time.h:22:0,
                 from /home/mpatel/build/fulvia/sage-4.6.alpha1pre-4000/local/include/FLINT/zmod_poly.h:35,
                 from /home/mpatel/build/fulvia/sage-4.6.alpha1pre-4000/local/include/FLINT/fmpz_poly.h:40,
                 from sage/libs/flint/fmpq_poly.h:22,
                 from sage/libs/flint/fmpq_poly.c:15:
/usr/include/sys/types.h:536:23: error: duplicate ‘unsigned’
```

 The other extra argument, `-D_XPG6` is technically correct, as Bill says, but causes problems with gcc on Solaris.

Are there any objections to using

```python
              extra_compile_args=["-std=c99"] + uname_specific('SunOS', [], ['-D_XPG6']),
```

instead?


---

Comment by leif created at 2010-09-20 13:37:33

Replying to [comment:110 mpatel]:
> [...]
> Are there any objections to using

```python
              extra_compile_args=["-std=c99"] + uname_specific('SunOS', [], ['-D_XPG6']),
```

> instead?

I would really appreciate if this got fixed in a proper way, and not with yet another work-around.

I.e., IMHO one should
 * *drop the* `language="c++"` (since it is in fact C code),
 * clean up - unfortunately lots of - Cython header files (`.pxi`, `.pxd`) to not rather randomly include NTL[-related] wrappers / headers which trigger the need for C++. Some `.pyx` files then have to explicitly include these elsewhere omitted ones (but IIRC only `sage/algebras/quatalg/quaternion_algebra_element.pyx`).
 * Remove `"ntl"` and `"gmpxx"` from `libraries`.

I've actually given up to complete the second step, since for some reason Cython insists to put both

```C
#include "ntl_wrap.h"
```

and

```C
#include "FLINT/NTL-interface.h"
```

into the generated `polynomial_rational_flint.c` (for me, line 168 and 170).

If I manually remove these two lines, the extension module gets properly built and apparently works.

If we solve just the XPG6 issue (by getting around the bad Solaris headers), but keep the underlying cause, I'm pretty sure we'll revisit the same problem (needing to compile C code as if it was C++) soon.

Perhaps one should ask the authors why they added `language="c++"`; I guess just because they ran into the real problem.


---

Comment by leif created at 2010-09-20 13:42:36

P.S.: The `-Wstrict-prototypes` is a separate Cython / distutils problem. Perhaps fixed in Cython 0.13 (Robert B. is well aware of this), but I think it isn't yet.


---

Comment by leif created at 2010-09-20 14:02:08

P.P.S.:

```python
from sage.libs.flint.ntl_interface cimport *
```

also has to be removed from `polynomial_rational_flint.pyx`.


---

Comment by rbeezer created at 2010-09-20 18:12:59

Fixes doctest for graph vertex sorting, see #9741


---

Attachment

Replying to [comment:102 mpatel]:
> The failures in `generic_graph.py` stem from the newly merged #9741.  I've added a comment there.

#9741 has a doctest that uses vertices that are polynomials.  With module name changes here at #4000, one of the doctests needs to change.  I've added a bit of documentation (and expanded the test slightly) to make it clear why the fully-qualified name is being used - more discussion is on #9741.

I built this patch after applying everything up through the "hensel_lift" patch, but it should just depend on the renaming of the modules.  Tests now pass on `sage/graphs/generic_graph.py` and the documentation for this module looks fine.


---

Comment by leif created at 2010-09-22 04:48:26

Another P.S.:

While `ntl_wrap.h` does no harm (it can be included in C programs), `FLINT/NTL-interface.h` is quite funny:

```CC
...
NTL-interface.h: Header file for NTL-interface.cpp

Copyright (C) 2007, William Hart

*****************************************************************************/

#ifndef FLINT_NTL_INT_H
#define FLINT_NTL_INT_H

#ifdef __cplusplus
 extern "C" {
#endif

#include <NTL/ZZ.h>
#include <NTL/ZZX.h>

#include "flint.h"
#include "F_mpz.h"
#include "fmpz.h"
#include "fmpz_poly.h"

NTL_CLIENT

/*
   Returns the number of limbs taken up by an NTL ZZ
*/

unsigned long ZZ_limbs(const ZZ& z);

...
```



---

Comment by leif created at 2010-09-23 13:37:47

I've finally managed to build `sage.rings.polynomial.polynomial_rational_flint` as a *C* extension module; have to sort out the changes though (but not today).

This also fixes the Solaris headers issue.


---

Comment by spancratz created at 2010-09-23 15:42:39

Dear Leif,

I just wanted to say thank you for looking at this.

Best wishes,
Sebastian


---

Comment by mpatel created at 2010-10-05 05:37:06

Replying to [comment:118 spancratz]:
> Dear Leif, I just wanted to say thank you for looking at this. Best wishes, Sebastian

Indeed, thanks very much for working on a proper solution.  It would be nice to get #4000 into 4.6.alpha3 for wider testing.  What do you think about using the workaround temporarily and having a separate ticket for doing it right?


---

Comment by spancratz created at 2010-10-06 23:08:00

I think this would be the appropriate way to handle this.  Sebastian


---

Comment by mpatel created at 2010-10-07 06:08:16

Applying [attachment:trac4000_0.patch] to 4.6.alpha2, I get a failed "hunk":

```diff
--- polynomial_ring.py
+++ polynomial_ring.py
`@``@` -1220,28 +1220,34 `@``@`
             sage: type(R.gen())
             <class 'sage.rings.polynomial.polynomial_element_generic.Polynomial_generic_dense_field'>
         """
-        if implementation is None: implementation="NTL"
         from sage.rings.finite_rings.finite_field_base import is_FiniteField
+        from sage.rings.rational_field import QQ
+        from sage.rings.polynomial.polynomial_singular_interface import can_convert_to_singular
+        if implementation is None:
+            implementation = "NTL"
+
         if implementation == "NTL" and is_FiniteField(base_ring):
-            p=base_ring.characteristic()
             from sage.libs.ntl.ntl_ZZ_pEContext import ntl_ZZ_pEContext
             from sage.libs.ntl.ntl_ZZ_pX import ntl_ZZ_pX
+            from sage.rings.polynomial.polynomial_zz_pex import Polynomial_ZZ_pEX
+
+            p = base_ring.characteristic()
             self._modulus = ntl_ZZ_pEContext(ntl_ZZ_pX(list(base_ring.polynomial()), p))
-            from sage.rings.polynomial.polynomial_zz_pex import Polynomial_ZZ_pEX
-            element_class=Polynomial_ZZ_pEX
+            element_class = Polynomial_ZZ_pEX
 
         if not element_class:
             if sparse:
                 element_class = polynomial_element_generic.Polynomial_generic_sparse_field
             elif isinstance(base_ring, rational_field.RationalField):
-                element_class = polynomial_element_generic.Polynomial_rational_dense
+                from sage.rings.polynomial.polynomial_rational_flint import Polynomial_rational_flint
+                element_class = Polynomial_rational_flint
             elif is_RealField(base_ring):
                 element_class = PolynomialRealDense
             else:
                 element_class = polynomial_element_generic.Polynomial_generic_dense_field
+
         PolynomialRing_integral_domain.__init__(self, base_ring, name=name, sparse=sparse, element_class=element_class)
 
-        from sage.rings.polynomial.polynomial_singular_interface import can_convert_to_singular
         self._has_singular = can_convert_to_singular(self)
 
     def divided_difference(self, points, full_table=False):
```

Could someone who knows this code please rebase the patch?


---

Comment by mpatel created at 2010-10-08 08:41:02

Main patch rebased against 4.6.alpha3


---

Attachment

Solaris work around


---

Comment by mpatel created at 2010-10-08 09:00:07

I've attached a rebased patch and a workaround for the Solaris GCC problem.  The patches to apply are now:

 * [attachment:trac4000_0.2.patch]
 * [attachment:trac4000_fmpq_poly_c.patch]
 * [attachment:trac4000_fmpq_poly_pxd.patch]
 * [attachment:trac4000_64bit.patch]
 * [attachment:trac4000_is.patch]
 * [attachment:4000_fix_hensel_lift.patch]
 * [attachment:trac_4000-graph-vertex-sort-fix.patch]
 * [attachment:trac_4000-sunos_workaround.patch]


---

Comment by mpatel created at 2010-10-08 09:00:07

Changing status from needs_work to needs_review.


---

Comment by mpatel created at 2010-10-08 09:27:00

The tests pass with a trial 4.6.alpha3 (which is probably the same as alpha2 for this ticket) on sage.math, except for

```python
sage -t -long -force_lib "devel/sage/sage/rings/number_field/number_field_ideal.py"
**********************************************************************
File "/mnt/usb1/scratch/mpatel/apps/sage-4.6.a3/devel/sage/sage/rings/number_field/number_field_ideal.py", line 194:
    sage: NumberField(x^2 + 1, 'a').ideal(7).__hash__()
Expected:
    -9223372036854775779                 
Got:
    -288230376151711715
```

On David Kirkby's OpenSolaris machine hawk, I get

```python
sage -t -long -force_lib "devel/sage/sage/rings/number_field/number_field_ideal.py"
**********************************************************************
File "/export/home/buildbot/build/sage/hawk-1/hawk_full/build/sage-4.6.alpha3/devel/sage/sage/rings/number_field/number_field_ideal.py", line 194:
    sage: NumberField(x^2 + 1, 'a').ideal(7).__hash__()
Expected:
    -2147483619
Got:
    -67108835
```


I'm inclined to merge this into 4.6.alpha3.  We can open a new ticket for the new error, unless it indicates a serious problem.  I'd like to release 4.6.alpha3 in a day or so, so please let me know as soon as possible.


---

Comment by mpatel created at 2010-10-08 09:27:38

Combined patch that replaces all of the others


---

Attachment

I've also attached a combined patch that replaces all of the others.


---

Comment by drkirkby created at 2010-10-08 10:09:32

Replying to [comment:123 mpatel]:
> The tests pass with a trial 4.6.alpha3 (which is probably the same as alpha2 for this ticket) on sage.math, except for
> {{{
> #!python
> sage -t -long -force_lib "devel/sage/sage/rings/number_field/number_field_ideal.py"
> **********************************************************************
> File "/mnt/usb1/scratch/mpatel/apps/sage-4.6.a3/devel/sage/sage/rings/number_field/number_field_ideal.py", line 194:
>     sage: NumberField(x^2 + 1, 'a').ideal(7).__hash__()
> Expected:
>     -9223372036854775779                 
> Got:
>     -288230376151711715
> }}}
> On David Kirkby's OpenSolaris machine hawk, I get
> {{{
> #!python
> sage -t -long -force_lib "devel/sage/sage/rings/number_field/number_field_ideal.py"
> **********************************************************************
> File "/export/home/buildbot/build/sage/hawk-1/hawk_full/build/sage-4.6.alpha3/devel/sage/sage/rings/number_field/number_field_ideal.py", line 194:
>     sage: NumberField(x^2 + 1, 'a').ideal(7).__hash__()
> Expected:
>     -2147483619
> Got:
>     -67108835
> }}}
> 
> I'm inclined to merge this into 4.6.alpha3.  We can open a new ticket for the new error, unless it indicates a serious problem.  I'd like to release 4.6.alpha3 in a day or so, so please let me know as soon as possible.




Personally, I think it would be best to fix it first. Otherwise it strikes me of this comment

http://trac.sagemath.org/sage_trac/ticket/6456#comment:67

by Peter Jeremy.
----
*I am very concerned at this "release it now, we'll make it work later" mentality.*
----
 
If it is on the strict understanding it does not get into a release until fixed, then I'm OK with it. That is the purpose of alphas. But I thought the intension was to have a feature freeze after this alpha. Merging this could be dangerous thing to do. 

The ticket has been open two years - I would have thought those working on it would have had time to checked it! 

Dave


---

Comment by drkirkby created at 2010-10-08 10:11:26

As a matter of interest, what is the rationale for making a ticket a blocker, when it has been open for two years? If we have lived without it for two years, I find the 'blocker' status a bit unnecessary.


---

Comment by mpatel created at 2010-10-08 10:13:19

On bsd.math, I get

```python
sage -t -long  -force_lib devel/sage/sage/rings/number_field/number_field_ideal.py
**********************************************************************
File "/Users/buildbot/build/sage/bsd-1/bsd_full/build/sage-4.6.alpha3/devel/sage-main/sage/rings/number_field/number_field_ideal.py", line 194:
    sage: NumberField(x^2 + 1, 'a').ideal(7).__hash__()
Expected:
    -9223372036854775779                 
Got:
    -288230376151711715
```

so it seems we can just update the example at line 194 in `number_field_ideal.py`, which is currently:

```python
            sage: NumberField(x^2 + 1, 'a').ideal(7).__hash__()
            -9223372036854775779                 # 64-bit
            -2147483619                          # 32-bit
```

Is is OK?


---

Comment by drkirkby created at 2010-10-08 10:18:12

For the record, here is a slightly longer quote of what Peter said:

_I am very concerned at this "release it now, we'll make it work later" mentality. If Sage is going to be a viable alternative to the M's, it needs to be trustworthy - complaints of "feature X is missing" are easily rectified, claims of "Sage gave me wrong answers" can quickly turn into "you can't trust the output from Sage" and are far more difficult to refute. _


---

Comment by mpatel created at 2010-10-08 10:23:39

Fix 32/64-bit number_field_ideal doctest.  Apply only this patch.


---

Attachment

I made this ticket a 4.6 blocker three weeks ago.  The most recent doctest error appeared because of a recent change, probably in 4.6.alpha2.  Yes, I meant to say that I'd make the new ticket a 4.6 blocker.  4.6.alpha3 is not out yet and we are not yet in feature freeze.

I've added V2 of the combined patch, which adjusts the `number_field_ideal.py` example as I suggest above.

This ticket still needs a final review, and if it's positively reviewed by the time #10097 is merged, I'll merge it into 4.6.alpha3.


---

Comment by was created at 2010-10-08 21:59:09

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-10-08 22:48:52

Resolution: fixed


---

Comment by rlm created at 2010-10-11 17:31:05

And there was much rejoicing.


---

Comment by leif created at 2011-09-05 22:26:55

For the record:

There's a bug in `fmpq_poly_xgcd()` that can lead to severe heap corruption, which in turn can cause almost any kind of failure.

See #11771 for details.

(Unfortunately FLINT 2.2, which includes its own / a newer version of `fmpq_poly`, doesn't yet provide `xgcd()` for rational polynomials.)


---

Comment by leif created at 2011-09-05 23:46:42

Replying to [comment:134 leif]:
> There's a bug in `fmpq_poly_xgcd()` that can lead to severe heap corruption, which in turn can cause almost any kind of failure.
> 
> See #11771 for details.

Patch is up there.

It would be nice if one of the many reviewers here could review my patch there. He/she should IMHO also take a look at the sizes used in other memory (re)allocations / for other variables, in `fmpq_poly_xgcd()` at least.
