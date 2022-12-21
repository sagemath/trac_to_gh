# Issue 4965: [with patch, needs work] Z/nZ[x] via FLINT's zmod_poly

Issue created by migration from Trac.

Original creator: malb

Original creation time: 2009-01-11 22:03:25

Assignee: somebody

CC:  burcin was

The attached patches wrap FLINT's Z/nZ[x] for word sized n. This provides a considerable speed-up (~ 20x) for univariate polynomial arithmetic over these rings and also cleans up the code using the `polynomial_template.pxi` mechanism. For that `polynomial_template.pxi` was also cleaned-up which should make it more suitable for other backend implementations.


---

Comment by malb created at 2009-01-11 22:03:41

apply this first


---

Attachment

## Speed-Up on sage.math

### Old


```
sage: P.<x> = PolynomialRing(GF(7))
sage: type(x)
<type 'sage.rings.polynomial.polynomial_modn_dense_ntl.Polynomial_dense_mod_p'>
sage: f = P.random_element(100)
sage: g = P.random_element(100)
sage: %timeit f*g
1000 loops, best of 3: 445 µs per loop
```


### New


```
sage: P.<x> = PolynomialRing(GF(7))
sage: type(x)
<type 'sage.rings.polynomial.polynomial_zmod_flint.Polynomial_zmod_flint'>
sage: f = P.random_element(100)
sage: g = P.random_element(100)
sage: %timeit f*g
100000 loops, best of 3: 7.92 µs per loop
```



---

Comment by malb created at 2009-01-11 22:07:52

At least these two doctests fail.


```
sage -t  "devel/sage/sage/schemes/hyperelliptic_curves/hyperelliptic_padic_field.py"
sage -t  "devel/sage/sage/schemes/elliptic_curves/ell_number_field.py"
```


I would greatly appreciate input/pointers where to look for the bug. Once I figured out which of the functions I've touched returns wrong/unexpected answers, I can fix it. However, as of now, I don't know which one it is.


---

Comment by malb created at 2009-01-11 22:17:09

More details:


```
sage -t  ".../sage/schemes/hyperelliptic_curves/hyperelliptic_padic_field.py"
**********************************************************************
File ".../sage/schemes/hyperelliptic_curves/hyperelliptic_padic_field.py", line 198:
    sage: w.coleman_integral(P, Q)
Expected:
    O(11^6)
Got:
    6 + 7*11 + 8*11^2 + 7*11^3 + 3*11^4 + 10*11^5 + O(11^6)
**********************************************************************
File ".../sage/schemes/hyperelliptic_curves/hyperelliptic_padic_field.py", line 200:
    sage: C.coleman_integral(x*w, P, Q)
Expected:
    O(11^6)
Got:
    3 + 11 + 6*11^2 + 2*11^3 + 8*11^5 + O(11^6)
**********************************************************************
File ".../sage/schemes/hyperelliptic_curves/hyperelliptic_padic_field.py", line 202:
    sage: C.coleman_integral(x^2*w, P, Q)
Expected:
    3*11 + 2*11^2 + 7*11^3 + 2*11^4 + 10*11^5 + O(11^6)
Got:
    5 + 11 + 8*11^2 + 11^3 + 7*11^4 + 6*11^5 + O(11^6)
**********************************************************************
File ".../sage/schemes/hyperelliptic_curves/hyperelliptic_padic_field.py", line 213:
    sage: w.integrate(P, Q), (x*w).integrate(P, Q)
Expected:
    (O(71^4), O(71^4))
Got:
    (40 + 4*71 + 21*71^2 + 39*71^3 + O(71^4), 2 + 58*71 + 27*71^2 + 49*71^3 + O(71^4))
**********************************************************************
File ".../sage/schemes/hyperelliptic_curves/hyperelliptic_padic_field.py", line 216:
    sage: w.integrate(P, R)
Expected:
    42*71 + 63*71^2 + 55*71^3 + O(71^4)
Got:
    14 + 27*71 + 46*71^2 + 10*71^3 + O(71^4)
```



---

Comment by malb created at 2009-01-11 22:19:27


```
File ".../sage/schemes/elliptic_curves/ell_number_field.py", line 728:
    sage: EllipticCurve([1 + a , -1 + a , 1 + a , -11 + a , 5 -9*a  ]).conductor()
Exception raised:
    Traceback (most recent call last):
      File ".../sage/schemes/elliptic_curves/ell_number_field.py", line 747, in conductor
        for d in self.local_data()],\
      File ".../sage/schemes/elliptic_curves/ell_number_field.py", line 396, in local_data
        return [self._get_local_data(pr, proof) for pr in primes]
      File ".../sage/schemes/elliptic_curves/ell_number_field.py", line 418, in _get_local_data
        self._local_data[P] = EllipticCurveLocalData(self, P, proof)
      File ".../schemes/elliptic_curves/ell_local_data.py", line 140, in __init__
        self._Emin, ch, self._val_disc, self._fp, self._KS, self._cp, self._split = self._tate(proof)
      File ".../sage/schemes/elliptic_curves/ell_local_data.py", line 520, in _tate
        r = proot(-b6, 3)
      File ".../sage/schemes/elliptic_curves/ell_local_data.py", line 451, in <lambda>
        proot = lambda x,e: F.lift(F(x).nth_root(e, extend = False, all = True)[0])
      File "integer_mod.pyx", line 855, in sage.rings.integer_mod.IntegerMod_abstract.nth_root (sage/rings/integer_mod.c:7712)
      File "polynomial_element.pyx", line 3715, in sage.rings.polynomial.polynomial_element.Polynomial.roots (sage/rings/polynomial/polynomial_element.c:24924)
      File "polynomial_element.pyx", line 2096, in sage.rings.polynomial.polynomial_element.Polynomial.factor (sage/rings/polynomial/polynomial_element.c:15667)
    ValueError: factorization of 0 not defined
```



---

Comment by cremona created at 2009-01-11 22:34:20

I'll try to look at the second of those since it seems to crop up in code which I wrote.  But I em extremely busy at the moment so cannot promise anything very quickly.


---

Comment by malb created at 2009-01-11 22:45:42

Replying to [comment:5 cremona]:
> I'll try to look at the second of those since it seems to crop up in code which I wrote.  But I em extremely busy at the moment so cannot promise anything very quickly.

Thanks!


---

Comment by malb created at 2009-01-12 12:25:58

The updated patch
 * addresses a couple of remarks by Bill Hart off-list
 * changes the celement definition (following Burcin's alternative implementation)

Burcin also wrapped `zmod_poly_t` two months ago and our patches match a lot. Thus, copyright should be shared. The only reason I'm using my patches as a basis is because I know them better. Btw. Burcin's patches rearrange a fair amount of stuff in `polynomial_ring.pyx` which I don't. He also splits the `polynomial_template.pxi` in `polynomial_template.pxi` and `polynomial_template_field.pxi`.


---

Comment by malb created at 2009-01-12 12:36:50

## "Long" Doctest Failures

this one is easy:


```
sage -t --long "devel/sage/sage/schemes/elliptic_curves/padics.py"
...
sage.rings.polynomial.polynomial_zmod_flint.Polynomial_zmod_flint._derivative 
...
sage.libs.ntl.ntl_lzz_pContext.ntl_zz_pContext     ValueError: Modulus (=2384185791015625) is too big
```



```
File ".../sage/schemes/elliptic_curves/ell_number_field.py", line 728:
    sage: EllipticCurve([1 + a , -1 + a , 1 + a , -11 + a , 5 -9*a  ]).conductor()
...
    ValueError: factorization of 0 not defined
```



```
sage -t --long "devel/sage/sage/schemes/elliptic_curves/sha_tate.py"
...
    sage: EllipticCurve('858k2').sha().an_padic(7)  #rank 0, non trivial sha  (long
...
sage.libs.ntl.ntl_lzz_pContext.ntl_zz_pContext     ValueError: Modulus (=558545864083284007) is too big
```



```
sage -t --long "devel/sage/sage/schemes/hyperelliptic_curves/hyperelliptic_padic_field.py"
**********************************************************************
    sage: w.coleman_integral(P, Q)
Expected:
    O(11^6)
Got:
    6 + 7*11 + 8*11^2 + 7*11^3 + 3*11^4 + 10*11^5 + O(11^6)
**********************************************************************
    sage: C.coleman_integral(x*w, P, Q)
Expected:
    O(11^6)
Got:
    3 + 11 + 6*11^2 + 2*11^3 + 8*11^5 + O(11^6)
**********************************************************************
    sage: C.coleman_integral(x^2*w, P, Q)
Expected:
    3*11 + 2*11^2 + 7*11^3 + 2*11^4 + 10*11^5 + O(11^6)
Got:
    5 + 11 + 8*11^2 + 11^3 + 7*11^4 + 6*11^5 + O(11^6)
**********************************************************************
    sage: w.integrate(P, Q), (x*w).integrate(P, Q)
Expected:
    (O(71^4), O(71^4))
Got:
    (40 + 4*71 + 21*71^2 + 39*71^3 + O(71^4), 2 + 58*71 + 27*71^2 + 49*71^3 + O(71^4))
**********************************************************************
    sage: w.integrate(P, R)
Expected:
    42*71 + 63*71^2 + 55*71^3 + O(71^4)
Got:
    14 + 27*71 + 46*71^2 + 10*71^3 + O(71^4)
**********************************************************************
```



---

Comment by malb created at 2009-01-12 16:31:38

The updated `zmod_poly.patch` fixes the two 


```
ValueError: Modulus (...) is too big
```


errors. So we're back to square one and these two fail:


```
sage -t  "devel/sage/sage/schemes/hyperelliptic_curves/hyperelliptic_padic_field.py"
sage -t  "devel/sage/sage/schemes/elliptic_curves/ell_number_field.py"
```



---

Comment by malb created at 2009-01-13 01:16:03

The patch update adds a simple zn_poly interface to `Polynomial_zmod_flint`.

## Performance


```
def f(p,n):
    P = PolynomialRing(GF(next_prime(p)),'x')
    f = P.random_element(n)
    g = P.random_element(n)

    t0 = cputime()
    r0 = f*g
    t0 = cputime(t0)

    t1 = cputime()
    r1 = f._mul_zn_poly(g)
    t1 = cputime(t1)

    assert(r0 == r1)

    return p,n,t0,t1

for i in range(21): 
   f(2**47,2**i)
```


returns


```
# (140737488355328, 1, 0.0, 0.0)
# (140737488355328, 2, 0.0, 0.0)
# (140737488355328, 4, 0.00099999999999766942, 0.0)
# (140737488355328, 8, 0.0, 0.0)
# (140737488355328, 16, 0.0, 0.0)
# (140737488355328, 32, 0.0059990000000027521, 0.0)
# (140737488355328, 64, 0.0, 0.0)
# (140737488355328, 128, 0.0, 0.0)
# (140737488355328, 256, 0.0, 0.0)
# (140737488355328, 512, 0.0, 0.00099999999999766942)
# (140737488355328, 1024, 0.00099999999999766942, 0.0)
# (140737488355328, 2048, 0.0020000000000024443, 0.0019989999999978636)
# (140737488355328, 4096, 0.0049989999999979773, 0.005000000000002558)
# (140737488355328, 8192, 0.010998000000000729, 0.011997999999998399)
# (140737488355328, 16384, 0.023995999999996798, 0.023997000000001378)
# (140737488355328, 32768, 0.050992000000000814, 0.052991999999996153)
# (140737488355328, 65536, 0.1149820000000048, 0.10598499999999689)
# (140737488355328, 131072, 0.29195599999999189, 0.21996599999999944)
# (140737488355328, 262144, 0.6119070000000022, 0.45393199999999467)
# (140737488355328, 524288, 1.5217689999999919, 1.0278430000000043)
# (140737488355328, 1048576, 3.1365230000000111, 2.0966819999999871)
```



---

Comment by cremona created at 2009-01-13 23:05:43

Here's what is causing the problem in the ell_number_field.py test:

If F is a field of 3 elements, b=F(0), then b.nth_root(0) gives an error:

```
sage: K.<a>=NumberField(x^2-x+3)
sage: F=K.residue_field(a); F; F.order()
Residue field of Fractional ideal (a)
3
sage: b=F(0); b
0
sage: b.nth_root(3)
ValueError: factorization of 0 not defined
```

The nth_root() function being called here is at fault, but that's as far as I got.


---

Comment by cremona created at 2009-01-14 08:54:56

PS To the above:  The nth_root() function should definitely catch x=0 as a special trivial case.  But here that would just hide the problem, that calling roots() on the polynomial `x^3` over the field F causes a crash.  I have not time to dig deeper:  I would expect that first one would take `gcd(x<sup>3,x</sup>3-x)` ...


---

Comment by malb created at 2009-01-14 09:47:27

Thanks a lot John! I now have a function to debug which should be sufficient to track down the bug.


---

Comment by malb created at 2009-01-14 13:41:04

Thanks to John's comment we're now down to one doctest failure:


```
sage -t --long ...sage/schemes/hyperelliptic_curves/hyperelliptic_padic_field.py
```



```
**********************************************************************
File ".../sage/schemes/hyperelliptic_curves/hyperelliptic_padic_field.py", line 198:
    sage: w.coleman_integral(P, Q)
Expected:
    O(11^6)
Got:
    6 + 7*11 + 8*11^2 + 7*11^3 + 3*11^4 + 10*11^5 + O(11^6)
**********************************************************************
File ".../sage/schemes/hyperelliptic_curves/hyperelliptic_padic_field.py", line 200:
    sage: C.coleman_integral(x*w, P, Q)
Expected:
    O(11^6)
Got:
    3 + 11 + 6*11^2 + 2*11^3 + 8*11^5 + O(11^6)
**********************************************************************
File ".../sage/schemes/hyperelliptic_curves/hyperelliptic_padic_field.py", line 202:
    sage: C.coleman_integral(x^2*w, P, Q)
Expected:
    3*11 + 2*11^2 + 7*11^3 + 2*11^4 + 10*11^5 + O(11^6)
Got:
    5 + 11 + 8*11^2 + 11^3 + 7*11^4 + 6*11^5 + O(11^6)
**********************************************************************
File ".../sage/schemes/hyperelliptic_curves/hyperelliptic_padic_field.py", line 213:
    sage: w.integrate(P, Q), (x*w).integrate(P, Q)
Expected:
    (O(71^4), O(71^4))
Got:
    (40 + 4*71 + 21*71^2 + 39*71^3 + O(71^4), 2 + 58*71 + 27*71^2 + 49*71^3 + O(71^4))
**********************************************************************
File ".../sage/schemes/hyperelliptic_curves/hyperelliptic_padic_field.py", line 216:
    sage: w.integrate(P, R)
Expected:
    42*71 + 63*71^2 + 55*71^3 + O(71^4)
Got:
    14 + 27*71 + 46*71^2 + 10*71^3 + O(71^4)
```



---

Comment by cremona created at 2009-01-14 20:38:14

I'm glad that this bug made me look at that code, since what I found was that the only situations where I was calling that nth_root() function were for square roots in residue fields of characteristic 2 and cube roots in char. 3.  In both cases there is a special p'th root function implemented by jhpalmieri in #4553 which I reviewed and which could be used instead, which should be quicker.  So this bug will have had a useful side-effect or two...


---

Comment by robertwb created at 2009-01-15 02:17:04

Some comments: 

1) Is there any reason __len__ was removed from GF(2)[x]? If we're going to take it out, it should at lest be deprecated, but I think it's useful to have. 
2) It is preferable to use .pxd files rather than .pxi files. 

I'm still looking into why the doctest failure above, and nothing obvious is coming to mind. Falling back to ntl polynomials gives the same wrong answer, so it must be something different in the way polynomials are interfaced/used.


---

Attachment


---

Comment by robertwb created at 2009-01-15 05:32:43

See attached. 

Perhaps `__rshift__` and `__lshift__` should call shift, it seems redundant to have code in all three. Also, I bet ntl and flint can shift faster than a multiply and/or divide.


---

Comment by malb created at 2009-01-15 12:03:34

> Perhaps `__rshift__` and `__lshift__` should call shift, it seems 
> redundant to have code in all three. Also, I bet ntl and flint can shift faster
> than a multiply and/or divide. 

I'd expect them to detect shifts, but I might be wrong. Should there be a  `celement_rshift`/`celement_lshift`?


---

Comment by burcin created at 2009-01-15 12:21:28

Malb, my wrapper provides support for the shifts, you can just copy it from there.

I think keeping a generic implementation in the Polynomial_template class, and overriding it if there is support for faster methods is good enough. Though maybe separating the user interface and functionality into 2 different functions (e.g. shift_left(), _shift_left_c()) might be better, so that the user interface and docstrings are consistent for subclasses.


---

Comment by malb created at 2009-01-15 12:43:46

Replying to [comment:17 robertwb]:
> Some comments: 
> 
> 1) Is there any reason __len__ was removed from GF(2)[x]? If we're going to take it out, it should at lest be deprecated, but I think it's useful to have. 

len shouldn't have been there in the first place because it is inconsistent with the rest of the univariate polynomials. 

> 2) It is preferable to use .pxd files rather than .pxi files. 

Okay, I'll change that then.


---

Comment by malb created at 2009-01-15 13:55:25

Replying to [comment:17 robertwb]:
> I'm still looking into why the doctest failure above, and nothing obvious is coming to mind. Falling back to ntl polynomials gives the same wrong answer, so it must be something different in the way polynomials are interfaced/used. 

I can't reproduce the behaviour you're describing. Maybe you missed that there are two places where `Polynomial_zmod_poly` is constructed (modn and modp). It fails if I leave the modn stuff in.


---

Comment by malb created at 2009-01-15 14:40:43

it seems like Robert's patch fixes the issue (I just realized now). I'm running `-t --long` now to see if everything is alright. Then I'll switch stuff around to pxd and do the shift business.


---

Comment by malb created at 2009-01-15 16:33:56


```
malb`@`sage:~/sage-3.2.2/devel/sage$ sage -tp 10 --long sage/
...
All tests passed!
```



---

Comment by robertwb created at 2009-01-15 19:58:43

malb: Yes, I was missing the fact that I had to change modn and modp, but in any case I found the bug in the end. 

Regarding len, I think it would be useful to have for all univariate polynomials, but it's not a big deal. 

Regarding shifts, I think we already have too many functions, and shouldn't be introducing even more. I think there should be a celement_shift (which takes positive and negative values), and the template `__lshift__, __rshift__`, and `shift` all call this. It's probably the exception to not have specialized shift methods, and in this case one would manually implement them in celement_shift.


---

Comment by robertwb created at 2009-01-15 19:59:09

I've made the shifting issue a new ticket: #4982


---

Comment by malb created at 2009-01-15 20:41:28

So I need to switch from pxi to pxd for 
 * `polynomial_template.pxi`
 * `ntl_GF2X_linkage.pxi`
 * `flint_zmod_poly_linkage.pxi`
and the ticket is ready for review. Or am I missing something?


---

Comment by robertwb created at 2009-01-15 21:04:10

Sorry for not being clear. The files you listed:

    * polynomial_template.pxi
    * flint_zmod_poly_linkage.pxi 

are the ones that should be .pxi (as they're actually included). The files that should be .pxd are

 * flint.pxi
 * ntl_interface.pxi
 * zmod_poly.pxi

as they are declaration files. An example is worth a thousand words, I'll attach a patch (which you can fold into yours if you want).


---

Comment by robertwb created at 2009-01-15 21:19:27

move pxi declarations to pxd


---

Attachment

OK, I attached a patch. This should probably be folded into zmod_poly.patch


---

Comment by mabshoff created at 2009-01-15 22:21:53

I had a lock and the direct use of ling in the FLINT headers is a bad thing on LLP platforms, i.e. Solaris, for at least efficiency reasons. I will complain about this to Bill and see what happens, but I guess this should not prevent this patch from going in for now.

Cheers,

Michael


---

Comment by malb created at 2009-01-19 02:37:36

to apply:
 * `polynomial_template.patch`
 * `zmod_poly.patch`


---

Comment by mabshoff created at 2009-01-19 05:45:49

For the record: Doctests on sage.math pass.

Robert: If humanly possible can you review this in the next couple hours? Then this patch will make it into 3.3.alpha0.

Cheers,

Michael


---

Comment by robertwb created at 2009-01-19 21:28:35

The code looks good, and seems to work for me. 

One failure in the doctests: 


```
sage -t  "sage/rings/polynomial//polynomial_zmod_flint.pyx" 
**********************************************************************
File "/Users/robert/sage/sage-3.1.3/devel/sage-trac4965/sage/rings/polynomial/polynomial_zmod_flint.pyx", line 236:
    sage: f*g == f._mul_zn_poly(g)
Exception raised:
    Traceback (most recent call last):
      File "/Users/robert/sage/current/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/Users/robert/sage/current/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/Users/robert/sage/current/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_8[5]>", line 1, in <module>
        f*g == f._mul_zn_poly(g)###line 236:
    sage: f*g == f._mul_zn_poly(g)
    AttributeError: 'sage.rings.polynomial.polynomial_modn_dense_ntl.Po' object has no attribute '_mul_zn_poly'
**********************************************************************
1 items had failures:
   1 of  10 in __main__.example_8
***Test Failed*** 1 failures.
For whitespace errors, see the file /Users/robert/sage/current/tmp/.doctest_polynomial_zmod_flint.py
```


should be an easy fix.


---

Comment by malb created at 2009-01-20 05:53:14

I cannot reproduce your failure neither could mabshoff (from the above statement). Maybe there was a problem applying the patches?


---

Comment by robertwb created at 2009-01-20 06:01:29

I bet I have a different cutoff between flint and ntl for a 32-bit machine.


---

Comment by malb created at 2009-01-20 06:13:11

You are of course right. I changed the doctest to use `next_prime(GF(2^31))` which should work on 32-bit systems. However, this raises the question whether we want to be consistent across all platforms for the cutoff: w.r.t. `Matrix_modn_dense` mabshoff and wstein indicated their desire to do so in another ticket.


---

Comment by robertwb created at 2009-01-20 06:20:42

Looks like you have to go down to 2^30. 


```
sage: P.<x> = PolynomialRing(GF(next_prime(2^31)))
sage: type(x)
<type 'sage.rings.polynomial.polynomial_modn_dense_ntl.Polynomial_dense_mod_p'>
sage: P.<x> = PolynomialRing(GF(next_prime(2^30)))
sage: type(x)
<type 'sage.rings.polynomial.polynomial_zmod_flint.Polynomial_zmod_flint'>
```


Personally, I think it's a bad idea to impose a 32-b it cutoff for 64-bit platforms.


---

Attachment

going down to 2^30


---

Comment by malb created at 2009-01-20 06:27:02

Replying to [comment:37 robertwb]:
> Looks like you have to go down to 2^30. 

done.


---

Comment by robertwb created at 2009-01-20 07:06:28

That resolved all of my concerns, positive review.


---

Comment by mabshoff created at 2009-01-22 23:34:40

Resolution: fixed


---

Comment by mabshoff created at 2009-01-22 23:34:40

Merged polynomial_template.patch and zmod_poly.patch in Sage 3.3.alpha1
