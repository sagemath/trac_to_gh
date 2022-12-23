# Issue 8791: improve doctest coverage of libs/mpmath/ext_main.pyx

Issue created by migration from https://trac.sagemath.org/ticket/8791

Original creator: mvngu

Original creation time: 2010-04-28 04:44:20

Assignee: mvngu

CC:  fredrik.johansson schilly

As the subject says. As of Sage 4.4, the doctest coverage of `sage/libs/mpmath/ext_main.pyx` is:

```
[mvngu@sage mpmath]$ sage -coverage ext_main.pyx 
----------------------------------------------------------------------
ext_main.pyx
ERROR: Please add a `TestSuite(s).run()` doctest.
SCORE ext_main.pyx: 0% (0 of 102)

Missing documentation:
	 * __cinit__(ctx):
	 * default(ctx):
	 * _get_prec(ctx):
	 * _set_prec(ctx, prec):
	 * _set_dps(ctx, n):
	 * _get_dps(ctx):
	 * _get_prec_rounding(ctx):
	 * mpf make_mpf(ctx, tuple v):
	 * mpc make_mpc(ctx, tuple v):
	 * _convert_param(ctx, x):
	 * _wrap_libmp_function(ctx, mpf_f, mpc_f=None, mpi_f=None, doc="<no doc>"):
	 * _wrap_specfun(cls, name, f, wrap):
	 * __init__(self, mpf_f, mpc_f=None, mpi_f=None, doc="<no doc>"):
	 * __call__(self, x, **kwargs):
	 * __init__(self, name, f):
	 * __call__(self, *args, **kwargs):
	 * __richcmp__(self, other, int op):
	 * __add__(self, other):
	 * __sub__(self, other):
	 * __mul__(self, other):
	 * __div__(self, other):
	 * __mod__(self, other):
	 * __pow__(self, other, mod):
	 * ae(s, t, rel_eps=None, abs_eps=None):
	 * __hash__(self):
	 * __repr__(self):
	 * __str__(self):
	 * real(self):
	 * imag(self):
	 * conjugate(self):
	 * man(self):
	 * exp(self):
	 * bc(self):
	 * __int__(self):
	 * __long__(self):
	 * __float__(self):
	 * __complex__(self):
	 * to_fixed(self, prec):
	 * __getstate__(self):
	 * __setstate__(self, val):
	 * __init__(self, x=0, **kwargs):
	 * __reduce__(self):
	 * _get_mpf(self):
	 * _set_mpf(self, v):
	 * __nonzero__(self):
	 * __hash__(self):
	 * real(self):
	 * imag(self):
	 * conjugate(self):
	 * man(self):
	 * exp(self):
	 * bc(self):
	 * to_fixed(self, long prec):
	 * __int__(self):
	 * __float__(self):
	 * __getstate__(self):
	 * __setstate__(self, val):
	 * __cinit__(self):
	 * __neg__(s):
	 * __pos__(s):
	 * __abs__(s):
	 * sqrt(s):
	 * __richcmp__(self, other, int op):
	 * __init__(self, func, name, docname=''):
	 * __call__(self, prec=None, dps=None, rounding=None):
	 * _mpf_(self):
	 * __repr__(self):
	 * __nonzero__(self):
	 * __neg__(self):
	 * __pos__(self):
	 * __abs__(self):
	 * sqrt(self):
	 * to_fixed(self, prec):
	 * __getstate__(self):
	 * __setstate__(self, val):
	 * __hash__(self):
	 * __richcmp__(self, other, int op):
	 * __init__(self, real=0, imag=0):
	 * __cinit__(self):
	 * __reduce__(self):
	 * __setstate__(self, val):
	 * __repr__(self):
	 * __str__(s):
	 * __nonzero__(self):
	 * __complex__(self):
	 * _get_mpc(self):
	 * _set_mpc(self, tuple v):
	 * real(self):
	 * imag(self):
	 * __hash__(self):
	 * __neg__(s):
	 * conjugate(s):
	 * __pos__(s):
	 * __abs__(s):
	 * __richcmp__(self, other, int op):


Missing doctests:
	 * convert(ctx, x, strings=True):
	 * isnan(ctx, x):
	 * isinf(ctx, x):
	 * isint(ctx, x):
	 * fsum(ctx, terms, bint absolute=False, bint squared=False):
	 * fdot(ctx, A, B=None):
	 * mag(ctx, x):
```



---

Comment by fredrik.johansson created at 2010-04-28 07:00:30

Argh. Who wrote this code?

The actual code coverage, indirectly through mpmath's unit tests (which however aren't run automatically by Sage) is close to 99%, but writing Sage doctests slipped my mind entirely.

Some of these functions have doctests, but they're added at runtime when importing mpmath. I'm considering whether statically duplicating them is a good idea, or whether it's better to just add static placeholders.

Most of these are probably trivial to write, e.g.:

```
sage: import mpmath
sage: mpmath.mpf(1).__add__(1)
mpf('2.0')
```

But I can't say when I'll have time to do this.


---

Comment by schilly created at 2010-04-28 13:46:41

While I started to write some tests, I stumbled about `to_fixed()`. What does it do? Would be


```
sage: import mpmath
sage: mpmath.mpf('88494.93').to_fixed(6)
5663675
```


be a doctest or a total abuse?!


---

Comment by fredrik.johansson created at 2010-04-28 14:44:12

Thanks a *lot*, Harald!

to_fixed converts a number to binary fixed-point format. Perhaps for clarity something like the following could be used (1.25 is for exactness):


```
sage: mpmath.mpf(1.25).to_fixed(10)
1280
sage: int(1.25 * 2^10)
1280
```



---

Comment by schilly created at 2010-04-29 13:38:49

ok, i've done some more but i don't know how to really test init, cinit, call and some others.


---

Comment by schilly created at 2010-04-30 12:38:23

I have another question, is this a bug:

```
sage: mpmath.mpf(1) < 3
True
sage: 1 < mpmath.mpf(3)
False
sage: 4 == mpmath.mpf(4)
False


---

Comment by schilly created at 2010-04-30 13:26:14

I don't know how to test the remaining ones, but shouldn't be that hard to finish. Only 16 are still to go.


---

Comment by fredrik.johansson created at 2010-05-07 19:23:50

Thanks! Very nice work.

The comparisons are definitely a bug. I created #8924 for this.


---

Comment by fredrik.johansson created at 2011-11-14 20:03:19

Here is a new patch with almost full coverage: http://sage.math.washington.edu/home/fredrik/mpmath_doctests.patch

(I did not use Harald's old patch as a base, though I think that one will mostly still be working. Perhaps they could be combined.)

The functions still missing doctests are pickling support for classes that shouldn't be pickable (not sure why they are there).


---

Comment by was created at 2011-11-14 20:09:54

review this, not Harald's


---

Comment by was created at 2011-11-14 20:10:02

Changing status from new to needs_review.


---

Attachment


---

Comment by davidloeffler created at 2012-03-11 15:47:05

Apply mpmath_doctests.patch

(for patchbot)


---

Comment by davidloeffler created at 2012-03-13 17:26:32

Wow -- this is a monumental piece of doctesting! It looks great. This will get us a long way towards the 90% doctest coverage goal.


---

Comment by davidloeffler created at 2012-03-13 17:26:32

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2012-03-23 12:57:09

This obviously fails on 32-bit systems:

```
sage -t  --long -force_lib devel/sage/sage/libs/mpmath/ext_main.pyx
**********************************************************************
File "/export/home/buildbot/build/sage/hawk-1/hawk_full/build/sage-5.0.beta10/devel/sage-main/sage/libs/mpmath/ext_main.pyx", line 2023:
    sage: int(7.25 * 2**30)
Expected:
    7784628224
Got:
    7784628224L
**********************************************************************
```



---

Comment by jdemeyer created at 2012-03-23 12:57:09

Changing status from positive_review to needs_work.


---

Comment by davidloeffler created at 2012-03-25 14:59:22

apply over previous patch


---

Comment by davidloeffler created at 2012-03-25 15:00:30

Changing status from needs_work to needs_review.


---

Attachment

Apply mpmath_doctests.patch, trac_8791-fix.patch

This is a one-line fix -- anyone willing to quickly sign off on it?


---

Comment by jdemeyer created at 2012-03-27 15:52:52

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2012-03-27 15:52:52

Good!


---

Comment by jdemeyer created at 2012-03-28 10:02:47

Resolution: fixed
