# Issue 3865: Bug in conversion from gp elements to p-adics

Issue created by migration from https://trac.sagemath.org/ticket/3865

Original creator: craigcitro

Original creation time: 2008-08-15 02:38:07

Assignee: craigcitro

David Loeffler ran into the following:


```
sage: v = gp.polrootspadic(x^2-2, 7, 20)[1]

sage: R = Zp(7, 10, "capped-rel")

sage: R(v)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/Users/craigcitro/<ipython console> in <module>()

/Users/craigcitro/three-one/local/lib/python2.5/site-packages/sage/rings/padics/padic_generic.py in __call__(self, x, absprec, relprec)
     82             Casts x into self.  Uses the constructor of self._element_class.
     83         """
---> 84         return self._element_class(self, x, absprec, relprec)
     85 
     86     def _coerce_impl(self, x):

/Users/craigcitro/padic_capped_relative_element.pyx in sage.rings.padics.padic_capped_relative_element.pAdicCappedRelativeElement.__init__ (sage/rings/padics/padic_capped_relative_element.c:4872)()

/Users/craigcitro/rational.pyx in sage.rings.rational.Rational.__init__ (sage/rings/rational.c:3767)()

/Users/craigcitro/rational.pyx in sage.rings.rational.Rational.__set_value (sage/rings/rational.c:4567)()

/Users/craigcitro/three-one/local/lib/python2.5/site-packages/sage/interfaces/expect.py in _rational_(self)
   1393     def _rational_(self):
   1394         import sage.rings.all
-> 1395         return sage.rings.all.Rational(repr(self))
   1396 
   1397     def name(self, new_name=None):

/Users/craigcitro/rational.pyx in sage.rings.rational.Rational.__init__ (sage/rings/rational.c:3767)()

/Users/craigcitro/rational.pyx in sage.rings.rational.Rational.__set_value (sage/rings/rational.c:4533)()

TypeError: unable to convert 3 + 7 + 2*7^2 + 6*7^3 + 7^4 + 2*7^5 + 7^6 + 2*7^7 + 4*7^8 + 6*7^9 + 6*7^10 + 2*7^11 + 7^12 + 7^13 + 2*7^15 + 7^16 + 7^17 + 4*7^18 + 6*7^19 + O(7^20) to a rational
```


The trouble is that the code in the `__init__` method for `pAdicCappedRelativeElement`s only looks for Pari `gen` objects, not `GpElement`s. The fix should be trivial, but I'm going to look at it tomorrow.


---

Comment by mabshoff created at 2008-09-29 06:26:56

Tick Tick :p

Cheers,

Michael


---

Attachment

Patch against 5.11.beta3


---

Comment by davidloeffler created at 2013-07-22 19:48:32

... tock. :-)


---

Comment by davidloeffler created at 2013-07-22 19:48:32

Changing status from new to needs_review.


---

Comment by davidloeffler created at 2013-07-23 12:01:13

Changing keywords from "" to "sd51".


---

Comment by jantuitman created at 2013-07-23 15:01:12

looks good and works!


---

Comment by jantuitman created at 2013-07-23 15:01:12

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2013-08-16 21:17:16

Resolution: fixed
