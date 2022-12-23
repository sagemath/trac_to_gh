# Issue 2508: Probkem converting a Laurent Series from pari to Sage

Issue created by migration from https://trac.sagemath.org/ticket/2508

Original creator: cremona

Original creation time: 2008-03-13 18:35:51

Assignee: was

CC:  jdemeyer

Keywords: Laurent series, pari

The elliptic curve function modular_parametrization() returns a list of two pari objects which are Laurent Series in x (of degrees -2, -3).  I wanted to convert these into proper Sage Laurent Series, but that does not work.  However if I invert these (so they have positive degree, i.e. are power series) then I can coerce them into the Laurent series ring, and then invert again!


```
sage: X = E=EllipticCurve('389a1').modular_parametrization()[0]
sage: type(X)
<type 'sage.libs.pari.gen.gen'>
sage: X
x^-2 + 2*x^-1 + 4 + 7*x + 13*x^2 + 18*x^3 + 31*x^4 + 49*x^5 + 74*x^6 + 111*x^7 + 173*x^8 + 251*x^9 + 379*x^10 + 560*x^11 + 824*x^12 + 1199*x^13 + 1773*x^14 + O(x^15)
sage: R=LaurentSeriesRing(QQ,'q')
sage: R(X)
---------------------------------------------------------------------------
<class 'sage.libs.pari.gen.PariError'>    Traceback (most recent call last)

/home/jec/<ipython console> in <module>()

/home/jec/sage-2.10.3/local/lib/python2.5/site-packages/sage/rings/laurent_series_ring.py in __call__(self, x, n)
    182             return self.gen()**n * x
    183         else:
--> 184             return laurent_series_ring_element.LaurentSeries(self, x, n)
    185
    186     def _coerce_impl(self, x):

/home/jec/laurent_series_ring_element.pyx in sage.rings.laurent_series_ring_element.LaurentSeries.__init__()

/home/jec/sage-2.10.3/local/lib/python2.5/site-packages/sage/rings/power_series_ring.py in __call__(self, f, prec, check)
    324             v = sage_eval(f.Eltseq())
    325             return self(v) * (self.gen(0)**f.Valuation())
--> 326         return self.__power_series_class(self, f, prec, check=check)
    327
    328     def construction(self):

/home/jec/power_series_poly.pyx in sage.rings.power_series_poly.PowerSeries_poly.__init__()

/home/jec/sage-2.10.3/local/lib/python2.5/site-packages/sage/rings/polynomial/polynomial_ring.py in __call__(self, x, check, is_gen, construct, absprec)
    237         elif isinstance(x, pari_gen):
    238             if x.type() != 't_POL':
--> 239                 x = x.Polrev()
    240
    241         C = self.__polynomial_class

/home/jec/gen.pyx in sage.libs.pari.gen._pari_trap()

<class 'sage.libs.pari.gen.PariError'>:  (8)
sage: 1/R(1/X)
q^-2 + 2*q^-1 + 4 + 7*q + 13*q^2 + 18*q^3 + 31*q^4 + 49*q^5 + 74*q^6 + 111*q^7 + 173*q^8 + 251*q^9 + 379*q^10 + 560*q^11 + 824*q^12 + 1199*q^13 + 1773*q^14 + 2365*q^15 + 3463*q^16 + 4508*q^17 + O(q^18)
```



---

Comment by AlexGhitza created at 2008-03-23 23:41:08

I cannot replicate John's example (maybe it has already been fixed?):


```
sage: X = E=EllipticCurve('389a1').modular_parametrization()[0]
sage: X
q^-2 + 2*q^-1 + 4 + 7*q + 13*q^2 + 18*q^3 + 31*q^4 + 49*q^5 + 74*q^6 + 111*q^7 + 173*q^8 + 251*q^9 + 379*q^10 + 560*q^11 + 824*q^12 + 1199*q^13 + 1773*q^14 + 2365*q^15 + 3463*q^16 + 4508*q^17 + O(q^18)
sage: type(X)
<type 'sage.rings.laurent_series_ring_element.LaurentSeries'>
sage: version()
'SAGE Version 2.10.4, Release Date: 2008-03-17'
```


Notice how modular_parametrization() now returns a Sage LaurentSeries instead of a pari object.


---

Comment by cremona created at 2008-03-24 11:17:33

Alex,

That's right, I changed the code to return a proper Laurent series:

```
       R = LaurentSeriesRing(RationalField(),'q')
        XY = self.pari_mincurve().elltaniyama()
        return [1/R(1/XY[0]),1/R(1/XY[1])]
```


But look at what I had to do to coerce the pari Laurent series into the Sage ring R!  X and Y have negative valuation;  I could only get the coercions to work with things of positive valuation, so had to insert two spurious inversions  (for each of X and Y)

The following shoud work but does not:

```
sage: E=EllipticCurve('11a1')
sage: R = LaurentSeriesRing(RationalField(),'q')
sage: XY = E.pari_mincurve().elltaniyama()
sage: [R(XY[0]),R(XY[1])]
```



---

Comment by jdemeyer created at 2010-08-01 15:29:35

Changing priority from minor to major.


---

Comment by jdemeyer created at 2010-08-02 20:14:37

Changing assignee from was to jdemeyer.


---

Comment by jdemeyer created at 2010-08-02 20:35:23

Note also that the answer wrongly gets more terms:

```
sage: E = EllipticCurve('11a1')
sage: R = LaurentSeriesRing(RationalField(),'q')
sage: XY = E.pari_mincurve().elltaniyama()
sage: XY[0]
x^-2 + 2*x^-1 + 4 + 5*x + 8*x^2 + x^3 + 7*x^4 - 11*x^5 + 10*x^6 - 12*x^7 - 18*x^8 - 22*x^9 + 26*x^10 - 11*x^11 + 41*x^12 + 44*x^13 - 15*x^14 + O(x^15)
sage: E.modular_parametrization().power_series()[0]
q^-2 + 2*q^-1 + 4 + 5*q + 8*q^2 + q^3 + 7*q^4 - 11*q^5 + 10*q^6 - 12*q^7 - 18*q^8 - 22*q^9 + 26*q^10 - 11*q^11 + 41*q^12 + 44*q^13 - 15*q^14 + 19746*q^15 + 51565*q^16 + 150132*q^17 + O(q^18)
```



---

Comment by jdemeyer created at 2010-08-03 07:13:47

Changing status from new to needs_review.


---

Comment by cremona created at 2010-08-04 01:30:17

Patch looks very good, and applies fine to 4.5.2.rc0.  Testing now..


---

Comment by cremona created at 2010-08-04 01:48:20

Changing status from needs_review to positive_review.


---

Comment by cremona created at 2010-08-04 01:48:20

... and all passed (entire Sage library but without -long).


---

Comment by mpatel created at 2010-08-07 05:03:37

Changing status from positive_review to needs_work.


---

Comment by mpatel created at 2010-08-07 05:03:37

Could someone update the patch with a more descriptive commit string?


---

Comment by mpatel created at 2010-08-09 08:31:23

Changing status from needs_work to positive_review.


---

Attachment

Thanks, Jeroen!


---

Comment by mpatel created at 2010-08-09 09:50:56

Resolution: fixed
