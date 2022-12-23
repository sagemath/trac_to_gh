# Issue 9825: Memory corruption in polynomial complex_roots() method

Issue created by migration from https://trac.sagemath.org/ticket/9826

Original creator: hlaw

Original creation time: 2010-08-27 22:58:22

Assignee: somebody

CC:  mjo

Keywords: complex root, polynomial, finite field

Obviously the following code should raise an error (which is correctly given at the end), but it shouldn't be trying to `free()` non-aligned pointers.

```
sage: k.<a> = GF(7^3)
sage: P.<x> = PolynomialRing(k)
sage: P.random_element().complex_roots()
python(29941) malloc: *** error for object 0x5a45c: Non-aligned pointer being freed
*** set a breakpoint in malloc_error_break to debug
python(29941) malloc: *** error for object 0x2fffc: Non-aligned pointer being freed
*** set a breakpoint in malloc_error_break to debug
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/Users/hlaw/<ipython console> in <module>()

/Users/hlaw/src/sage-src/local/lib/python2.6/site-packages/sage/rings/polynomial/polynomial_element.so in sage.rings.polynomial.polynomial_element.Polynomial.complex_roots (sage/rings/polynomial/polynomial_element.c:32235)()

/Users/hlaw/src/sage-src/local/lib/python2.6/site-packages/sage/rings/polynomial/polynomial_element.so in sage.rings.polynomial.polynomial_element.Polynomial.roots (sage/rings/polynomial/polynomial_element.c:31226)()

/Users/hlaw/src/sage-src/local/lib/python2.6/site-packages/sage/rings/polynomial/polynomial_element.so in sage.rings.polynomial.polynomial_element.Polynomial.change_ring (sage/rings/polynomial/polynomial_element.c:16456)()

/Users/hlaw/src/sage-src/local/lib/python2.6/site-packages/sage/structure/parent.so in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:6407)()

/Users/hlaw/src/sage-src/local/lib/python2.6/site-packages/sage/structure/coerce_maps.so in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:3108)()

/Users/hlaw/src/sage-src/local/lib/python2.6/site-packages/sage/structure/coerce_maps.so in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:3010)()

/Users/hlaw/src/sage-src/local/lib/python2.6/site-packages/sage/rings/polynomial/polynomial_ring.pyc in _element_constructor_(self, x, check, is_gen, construct, **kwds)
    311                 x = x.Polrev()
    312 
--> 313         return C(self, x, check, is_gen, construct=construct, **kwds)
    314 
    315     def is_integral_domain(self, proof = True):

/Users/hlaw/src/sage-src/local/lib/python2.6/site-packages/sage/rings/polynomial/polynomial_real_mpfr_dense.so in sage.rings.polynomial.polynomial_real_mpfr_dense.PolynomialRealDense.__init__ (sage/rings/polynomial/polynomial_real_mpfr_dense.c:3609)()

/Users/hlaw/src/sage-src/local/lib/python2.6/site-packages/sage/structure/parent.so in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:6407)()

/Users/hlaw/src/sage-src/local/lib/python2.6/site-packages/sage/structure/coerce_maps.so in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:3108)()

/Users/hlaw/src/sage-src/local/lib/python2.6/site-packages/sage/structure/coerce_maps.so in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:3010)()

/Users/hlaw/src/sage-src/local/lib/python2.6/site-packages/sage/rings/real_mpfr.so in sage.rings.real_mpfr.RealField_class._element_constructor_ (sage/rings/real_mpfr.c:5058)()

/Users/hlaw/src/sage-src/local/lib/python2.6/site-packages/sage/rings/real_mpfr.so in sage.rings.real_mpfr.RealNumber._set (sage/rings/real_mpfr.c:8767)()

TypeError: Unable to convert x (='2*a^2+6*a+6') to real number.
```

If you run the code `P.random_element().complex_roots()` a few more times, you get a segfault:

```
sage: P.random_element().complex_roots()


------------------------------------------------------------
Unhandled SIGSEGV: A segmentation fault occurred in Sage.
This probably occurred because a *compiled* component
of Sage has a bug in it (typically accessing invalid memory)
or is not properly wrapped with _sig_on, _sig_off.
You might want to run Sage under gdb with 'sage -gdb' to debug this.
Sage will now terminate (sorry).
------------------------------------------------------------
```

Environment: Sage 4.5.2 on Mac OS X 10.5.8 (32 bit).


---

Comment by johanbosman created at 2011-04-07 14:07:00

Changing status from new to needs_review.


---

Comment by johanbosman created at 2011-04-07 14:07:00

The bug is caused by a deallocation method trying to clean up all coefficients of a polynomial, which segfaults if not all coefficients have been initialised, which in turn happens if the init gets wrong input.  The attached patch should fix this.

By the way, it is not clear to me why the milestone was set to sage-5.0.  I thought that was for Windows-related issues.  Please correct me if I'm wrong.


---

Comment by johanbosman created at 2011-04-11 18:47:12

The patch also fixes #10901.


---

Comment by mjo created at 2012-01-02 14:15:20

Refreshed patch, with a doctest.


---

Attachment

The fix works and makes sense to me (positive review for that). I've added a doctest (needs review), and rebased the original patch against 4.8.alpha5.

Unfortunately, something is wrong with exceptions at the moment:


```
sage: (a*x).complex_roots()
ERROR: An unexpected error occurred while tokenizing input
The following traceback may be corrupted or invalid
The error message is: ('EOF in multi-line statement', (1731, 0))
...
```


and that's fixed by Simon King's patch in #11900, so I've added a dependency there. The milestone update is to match #11900.


---

Comment by mjo created at 2012-01-05 02:38:24

Nevermind that; the ERRORs still happen in 4.8.alpha6, but the doctests don't seem bothered.


---

Comment by johanbosman created at 2012-02-29 15:30:57

In sage-5.0.beta4 this all works fine, so if you're okay with this, I suggest we give this ticket a positive review.


---

Comment by mjo created at 2012-02-29 19:40:59

Well, we should definitely keep the doctest since this was a bug that was somehow fixed.

It looks to me like your original fix is still valid, though, from my not-too-deep understanding of mpfr. I'll ask on sage-devel.


---

Comment by fbissey created at 2012-02-29 20:39:41

Do you mean "uninitialized" instead of "ininitialized"?


---

Comment by davidloeffler created at 2012-03-11 19:50:02

Apply sage-trac_9826.patch

(for patchbot)


---

Comment by vbraun created at 2012-04-24 04:05:32

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2012-04-24 04:05:32

This should have been merged a while ago!


---

Comment by mjo created at 2012-04-24 04:14:47

Same patch with my typo fixed.


---

Attachment

I guess I should finally fix that typo, huh. The only change is to spell "uninitialized" correctly, but I'm uploading a separate patch since it's got a positive review.


---

Comment by jdemeyer created at 2012-04-26 20:10:52

Resolution: fixed
