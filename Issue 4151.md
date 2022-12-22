# Issue 4151: [with patch, needs review] implementation of Dickman's function

Issue created by migration from Trac.

Original creator: robertwb

Original creation time: 2008-09-19 09:45:59

Assignee: was

See 

http://en.wikipedia.org/wiki/Dickman-de_Bruijn_function


---

Attachment

I tried installing this (under Sage 3.1.1) and now I get an error whenever I start up Sage:


```
/home/david/sage-3.1.1/local/lib/python2.5/site-packages/sage/functions/transcendental.py in <module>()
    378
    379
--> 380 from sage.rings.polynomial.polynomial_real_mpfr_dense import PolynomialRealDense
    381
    382 class DickmanRhoComputer:

ImportError: /home/david/sage-3.1.1/local/lib/python2.5/site-packages/sage/rings/polynomial/polynomial_real_mpfr_dense.so: undefined symbol: mpfr_set_z
```

I tried doing "sage -ba" and that didn't help. Does it only work if installed against one of the 3.1.2 alpha builds?

David


---

Comment by mabshoff created at 2008-09-21 10:07:34

I am pretty sure this is an issue with setup.py and OSX doing lazy symbols lookup at runtime:

```
   Extension('sage.rings.polynomial.polynomial_real_mpfr_dense', 
   sources = ['sage/rings/polynomial/polynomial_real_mpfr_dense.pyx']), \ 
```

Change that to 

```
   Extension('sage.rings.polynomial.polynomial_real_mpfr_dense', 
   sources = ['sage/rings/polynomial/polynomial_real_mpfr_dense.pyx'], 
   libraries = ['mpfr', 'gmp']), \
```

Cheers,

Michael


---

Attachment


---

Comment by davidloeffler created at 2008-09-21 15:12:16

OK, I changed setup.py and ran sage -ba and everything worked. I'm puzzled by what you say about the build problems being an OS X issue: I'm running SuSE Linux 10.3.

All doctests pass fine, but there are a couple of funny things:

- The definition states that rho(0) is 1 by definition, but your implementation gives

``` 
sage: dickman_rho(0)
0.000000000000000
```


I encountered this while trying to replicate the plot on the Wikipedia page, which fails nastily because log(rho(0)) is undefined.

Also, as discussed for Bessel functions at ticket #4102, it would be nice if the new dickman_rho function derived from calculus.PrimitiveFunction, as otherwise it doesn't play nicely with compositions etc:

```
sage: plot( log(dickman_rho(x)), (x, 0.0001, 15) )
# fails
sage: plot( lambda x: log(dickman_rho(x)), (0.001, 15))
# works, but not very intuitive for new users
```


Reading the code added to functions/transcendental.py, it's elegant and it obviously works, but it seems to throw away information in one case. Suppose I calculate dickman_rho(x) to d digits of precision. Then I want to know dickman_rho(y) to e digits, where y is slightly bigger than x (or, rather, bigger than 1.1x + 10) but e is *much* smaller than d. Then the code empties the cache and goes ahead and recalculates all of the power series from scratch, despite the fact that it already knows the first few terms to more than enough precision. I don't know if the added complication of getting around this problem is worth it; you'd have to remember not just current_prec() but the precision of the calculation of each series term. I guess in practice it's not something that's likely to be a problem.

Also, perhaps the instance variable self.f should be self._f, since it's very much for internal use. On a related note, perhaps it might be better to have a hidden function _compute_power_series, which avoids users having to know about this mysterious extra argument cache_ring, with a corresponding non-hidden function power_series() that takes only 2 arguments rather than 3. 

Anyway, I've uploaded a second patch which does the above attribute hiding, and returns 1 rather than 0 for rho(0); with these small changes I'd be more than happy to see this patch included, although I'm not sure my very limited Sage development experience gives me the authority to say this!

I wonder if there are other parts of the existing Sage library that would benefit from using native MPFR polynomials, in place of Sage polynomials over the MPFR real field?


---

Comment by mabshoff created at 2008-09-21 17:19:01

Replying to [comment:3 davidloeffler]:
> OK, I changed setup.py and ran sage -ba and everything worked. I'm puzzled by what you say about the build problems being an OS X issue: I'm running SuSE Linux 10.3.

My point is that the extensions works on OSX, but nowhere else, due to the way the OSX linker handles missing symbols. On all platforms but OSX linking in mpfr and its dependency explicitly fixes the problem.

I also changed the subject line to have the ticket get picked up by the standard reports.

Cheers,

Michael


---

Attachment

Thanks for your comments and improvements, I've attached a follow up patch. Nice catch about the value at 0. 

I agree with you that I could be saving some recalculation, but I don't think it's a common enough use case to justify the additional complexity. In fact, I throw away a lot as I go along--for example I don't want to cache 1000-bit 1000-term polynomials just in case one wants dickman_rho(10) to extremely high precision after computing dickman_rho(100).

I've opened #4168 to use native mpfr polynomials elsewhere, figuring it'd involve changes very irrelevant to this ticket.


---

Comment by davidloeffler created at 2008-09-23 11:43:26

That looks nice; I'm no expert on how the symbolics interface is supposed to work but the dickman_rho function now seems to behave a lot like the exp function, which is presumably a good guide, and you can do things like

```
sage:((dickman_rho(x) - 0.0001).find_root(0,10)
5.4478836002803135
```

which is nice.

The only problem I can see is that dickman_rho.approximate(1) returns a ZeroDivisionError, and dickman_rho.approximate(0.9) returns NaN. But I can't imagine any user being especially upset by this, as the docstring makes it clear that it's to be used for large values only.

I'd be happy to see this merged.

David


---

Comment by mabshoff created at 2008-09-23 22:07:06

Resolution: fixed


---

Comment by mabshoff created at 2008-09-23 22:07:06

Merged in Sage 3.1.3.alpha1
