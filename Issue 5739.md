# Issue 5739: zeta(CDF(1)) go boom!

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-04-10 23:09:59

Assignee: was

CC:  robertwb fredrik


```
wstein`@`bsd:~/build/sage-3.4.1.rc1$ uname -a
Darwin bsd.local 9.6.0 Darwin Kernel Version 9.6.0: Mon Nov 24 17:37:00 PST 2008; root:xnu-1228.9.59~1/RELEASE_I386 i386

wstein`@`bsd:~/build/sage-3.4.1.rc1$ sage
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: zeta(CDF(1))
| Sage Version 3.4.1.rc1, Release Date: 2009-04-05                   |
| Type notebook() for the GUI, and license() for information.        |

------------------------------------------------------------
Unhandled SIGSEGV: A segmentation fault occured in SAGE.
This probably occured because a *compiled* component
of SAGE has a bug in it (typically accessing invalid memory)
or is not properly wrapped with _sig_on, _sig_off.
You might want to run SAGE under gdb with 'sage -gdb' to debug this.
SAGE will now terminate (sorry).
------------------------------------------------------------
```




---

Comment by was created at 2009-04-11 05:43:44

I think Robert Bradshaw massively optimized CDF special functions, and that's where this comes from.  Changing the code for zeta in complex_double.pyx to:

```
        cdef pari_sp sp
        sp = avma
        _sig_on
        x = self._new_from_gen_c(  gzeta(self._gen(), PREC),   sp)
        _sig_off
        return x
```

somewhat fixes the problem, though doing 

```
sage: zeta(CDF(0))
```

then raises a RuntimeError.   Unfortunately, doing this doesn't work because the _sig_on/_sig_off stuff doesn't play well with Cython exceptions:

```
        cdef pari_sp sp
        sp = avma
        try:
           _sig_on
           x = self._new_from_gen_c(  gzeta(self._gen(), PREC),   sp)
           _sig_off
        except:
           raise ValueError
        return x
```


So I'm not sure how to fix this in general in a nice way with the right exception, but definitely adding _sig_on/_sig_off's around all the calls to pari is a very very good idea.


---

Comment by mhansen created at 2009-06-05 04:42:50

We should be able to replace the calls to pari with calls to mpmath.


---

Comment by mhansen created at 2009-06-05 04:42:50

Changing assignee from was to fredrik.


---

Comment by mhansen created at 2010-01-17 06:44:37

Changing status from new to needs_review.


---

Comment by kcrisman created at 2010-01-18 16:22:05

Changing status from needs_review to needs_info.


---

Attachment

The patch looks fine, but results in zeta of a CDF being approximately fifty times slower.  This seems problematic, and perhaps also something that would happen a lot if we start switching things to mpmath?  Mpmath looks like a great package, but if it has the same issue as NetworkX versus C graphs, we might not want to move default behavior there quite yet. 

Marking as needs_info since there does not seem to be a Sage-wide policy on mpmath at this point, and I am reluctant to give positive review to such a marked slowdown.


---

Attachment


---

Comment by robertwb created at 2010-01-18 19:46:59

Changing status from needs_info to needs_review.


---

Comment by robertwb created at 2010-01-18 19:46:59

I added an alternative patch that special cases the one pole at s=1 (returning the unsigned infinity, as gamma does).


---

Comment by kcrisman created at 2010-01-19 18:15:20

I hate to send this back to the drawing board again, but let's just fix things once and for all...

```
sage: zeta(CDF(1))
Infinity
sage: zeta(CC(1))
---------------------------------------------------------------------------
PariError                                 Traceback (most recent call last)

/Users/.../<ipython console> in <module>()

/Users/.../sage-4.3.1.alpha2/local/lib/python2.6/site-packages/sage/functions/transcendental.pyc in zeta(s)
    153     """
    154     try:
--> 155         return s.zeta()
    156     except AttributeError:
    157         return ComplexField()(s).zeta()

/Users/.../sage-4.3.1.alpha2/local/lib/python2.6/site-packages/sage/rings/complex_number.so in sage.rings.complex_number.ComplexNumber.zeta (sage/rings/complex_number.c:12174)()

/Users/.../sage-4.3.1.alpha2/local/lib/python2.6/site-packages/sage/libs/pari/gen.so in sage.libs.pari.gen._pari_trap (sage/libs/pari/gen.c:44110)()

PariError:  (8)
```

Can we think of any other places where this needs to be checked?  For instance, zeta(1) returns this error too, though I think it inherits it from the CC example.  

Also, regarding whether it should be Infinity or some signed infinity:

```
sage: zeta(RR(1))
+infinity
sage: zeta(RDF(1))
+infinity
```

I'm not saying which one is better, just what the current behavior is.  What do folks think?


---

Comment by kcrisman created at 2010-01-19 18:15:20

Changing status from needs_review to needs_work.


---

Comment by fredrik.johansson created at 2010-01-23 08:45:49

kcrisman:

Starting with the next version, mpmath uses the Riemann-Siegel formula, so it should be much faster than Pari for large imaginary parts near the critical strip. Right now I even get a segmentation fault if I try to compute zeta(CDF(1/2+10000000*I)) in Sage.

For CDF, zeta could also use mpmath.fp.zeta that will be available in the next version of mpmath. This function is currently typically 10-50 times faster than mpmath.mp.zeta. However, fp.zeta loses accuracy proportional to the magnitude of the imaginary part near the critical strip, so the question is whether this loss would be acceptable. For small imaginary parts, it's quite accurate.

Both functions could be accelerated in Sage by overriding the base case of an internal function (mpmath/functions/zeta.py/_zetasum in the svn trunk, if anyone wants a go). This should require just few lines of Cython.

Other than that, I would recommend keeping Pari where it's faster.


---

Attachment

apply this and 5739-CDF-zeta.patch


---

Comment by robertwb created at 2010-01-24 11:14:12

Changing status from needs_work to needs_review.


---

Comment by robertwb created at 2010-01-24 11:14:12

I fixed CC. As to whether it should be a signed or unsigned infinity, I went with unsigned because it has a simple pole there. 


```
10000.5772229475
sage: zeta(.9999)
-9999.42279161783
```


When the new mpmath gets released, we could open a ticket with timings and accuracy comparison. Generally we favor correctness over speed.


---

Comment by davidloeffler created at 2010-07-02 19:29:13

Patch applies cleanly to 4.5.alpha1 and builds fine, but some doctests fail:

```
sage -t  sage/rings/real_mpfr.pyx
**********************************************************************
File "/storage/masiao/sage-4.5.alpha1/devel/sage-reviewing/sage/rings/real_mpfr.pyx", line 4487:
    sage: R(1).zeta()
Expected:
    Infinity
Got:
    +infinity
**********************************************************************
1 items had failures:
   1 of  12 in __main__.example_149
***Test Failed*** 1 failures.
For whitespace errors, see the file /home/masiao/.sage//tmp/.doctest_real_mpfr.py
         [10.2 s]
**********************************************************************
File "/storage/masiao/sage-4.5.alpha1/devel/sage-reviewing/sage/rings/complex_number.pyx", line 2093:
    sage: zeta(1)
Expected:
    Infinity
Got:
    zeta(1)
**********************************************************************
1 items had failures:
   1 of   8 in __main__.example_72
***Test Failed*** 1 failures.
For whitespace errors, see the file /home/masiao/.sage//tmp/.doctest_complex_number.py
         [8.6 s]
```


Moreover, it doesn't seem to live up to the promise in the title of making the return value of zeta(1) consistent:


```
sage: zeta(RR(1))
+infinity
sage: zeta(RDF(1))
Infinity
```



---

Comment by davidloeffler created at 2010-07-02 19:29:13

Changing status from needs_review to needs_work.


---

Comment by burcin created at 2010-07-02 22:44:00

Since #8864, `zeta(1)` returns the answer given by GiNaC, which leaves it unevaluated because it doesn't know about infinity. I'll change this in the next pynac release to return unsigned infinity.


---

Attachment

apply only this patch


---

Comment by robertwb created at 2010-07-29 06:52:43

Changing status from needs_work to needs_review.


---

Comment by robertwb created at 2010-07-29 06:52:43

It's really sad we still have this trivial-to-fix hard crash after over a year!

I've attached a patch that fixes the behavior of CDF(1).zeta() and CC(1).zeta(). It leaves the real fields alone, which I think is fine 'cause they have reasonable representations of (an) infinity, and we usually try to return something of the same type. (IN the complex case, infinity is a lot messier without a lot of special casing that's beyond the scope of this ticket...)


```
sage: RR(1).zeta(), RDF(1).zeta(), CC(1).zeta(), CDF(1).zeta()
(+infinity, +infinity, Infinity, Infinity)
```



---

Comment by davidloeffler created at 2010-09-23 10:13:03

OK, that looks fine. I'd still argue that it should be an unsigned infinity in the real field cases as well, but (as you say) more or less anything is better than the current behaviour! Let's get this in.


---

Comment by davidloeffler created at 2010-09-23 10:13:03

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-09-28 08:19:43

Changing status from positive_review to needs_work.


---

Comment by mpatel created at 2010-09-28 08:19:43

The patch is missing a Mercurial header.  Could someone add this and restore the positive review?


---

Comment by davidloeffler created at 2010-09-28 08:26:11

Version with Mercurial header


---

Comment by davidloeffler created at 2010-09-28 08:26:27

Changing status from needs_work to positive_review.


---

Attachment

Done


---

Comment by mpatel created at 2010-09-28 10:54:27

Resolution: fixed
