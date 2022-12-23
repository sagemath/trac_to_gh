# Issue 8869: float(CDF(1)) should return 1.0, not throw an error

Issue created by migration from https://trac.sagemath.org/ticket/8869

Original creator: jason

Original creation time: 2010-05-04 15:56:30

Assignee: AlexGhitza

Right now, we have the following behavior:


```
sage: float(CC(1.0))
1.0


sage: float(CDF(1.0))
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/jason/<ipython console> in <module>()

/home/jason/sage/local/lib/python2.6/site-packages/sage/rings/complex_double.so in sage.rings.complex_double.ComplexDoubleElement.__float__ (sage/rings/complex_double.c:6532)()

TypeError: can't convert complex to float; use abs(z)


sage: float(complex(1.0))
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/jason/<ipython console> in <module>()

TypeError: can't convert complex to float 
```


As robertwb and was voted (on http://trac.sagemath.org/sage_trac/ticket/5400#comment:12 and on sage-devel), we should make float conversion succeed if the imaginary part is zero.


---

Attachment


---

Comment by jason created at 2010-05-04 16:17:26

Changing status from new to needs_work.


---

Comment by jason created at 2010-05-04 16:18:04

The patch needs to have commit message, and doctests need to be run.


---

Comment by leif created at 2010-05-06 01:54:07

See also http://groups.google.com/group/sage-devel/browse_thread/thread/75b8f85d22499ceb#

(I don't like the use of Python conversion functions on Sage objects.)

Why (only) suggest use of `abs()`? What about `real_part()`?
Or even `imag_part()` and `arg()`, perhaps `norm()`, too?

Is `abs()` really more natural than `real_part()`?


---

Comment by kcrisman created at 2010-05-26 19:58:40

Changing status from needs_work to needs_review.


---

Comment by kcrisman created at 2010-05-26 19:58:40

Ready for review.  Leif's comment seems reasonable, so I added one (!) extra option in the error message.  Passes tests on these two files.


---

Attachment

Based on 4.4.2, apply only this patch


---

Comment by leif created at 2010-05-26 21:54:53

Well, `__long__()` could equally well succeed if the _fractional_ (and imaginary) part is zero... ;-)

(And note that `int(1.1)` *silently* _truncates_; i.e. the current situation is overall not very consistent, as I mentioned in the thread.)

Nevertheless, I'll test it as soon as the "normal" 4.4.3.alpha0 ptestlong finishes on my Pentium 4, just wait a few hours... ;-)


---

Comment by kcrisman created at 2010-05-27 00:40:10

I don't think we are trying to be contentious here.  Yes, there are inconsistencies, but that is just to be expected (I would even say it follows from Arrow's Theorem).  The point is to make it as natural to mathematicians as possible, and float(CDF(1)) certainly smells like 1.0 to me.  int is a little different, but it seems to me that since Python isn't consistent anyways

```
>>> int(1.1)
1
>>> float(1+0j)
Traceback (most recent call last):
  File "<stdin>", line 1, in ?
TypeError: can't convert complex to float; use abs(z)
```

we might as well make the best of it and let int be the "round closest to zero" function, in essence.  And it's documented, and it's not the natural thing one would do (Integer(1.1) behaves as you would like).


---

Comment by leif created at 2010-05-27 01:50:12

Changing status from needs_review to positive_review.


---

Comment by leif created at 2010-05-27 01:50:12

The Python behavior could be "catched" by the preparser. There have recently been long discussions about Sage's "coercion model"...

----

Applied Karl-Dieter's patch on 4.4.3.alpha0.

`sage -t -long devel/sage/sage/rings` passed all tests.

Positive review.


---

Comment by leif created at 2010-05-27 12:15:09

`make ptestlong` also did not give errors related to _this_ patch (again Sage 4.4.3.alpha0, Ubuntu 9.04 x86/32-bit).


---

Comment by leif created at 2010-05-27 12:15:09

Changing keywords from "" to "CDF conversion, complex double".


---

Comment by mhansen created at 2010-06-06 01:21:28

Resolution: fixed
