# Issue 8291: eisenstein_series_qexp ridiculously bad  over finite fields

Issue created by migration from Trac.

Original creator: AlexGhitza

Original creation time: 2010-02-17 03:00:31

Assignee: craigcitro

CC:  mraum davidloeffler

I was the one who made Eisenstein series "work" over arbitrary fields.  It turns out that I didn't do a very good job, and you don't have to go very far to break it:


```
sage: eisenstein_series_qexp(26, 10, GF(13))
---------------------------------------------------------------------------
OverflowError                             Traceback (most recent call last)

/opt/sage-4.3.2/devel/sage-main/sage/modular/modform/<ipython console> in <module>()

/home/ghitza/sage-devel/local/lib/python2.6/site-packages/sage/modular/modform/eis_series.pyc in eisenstein_series_qexp(k, prec, K, var, integral)
    105     val[0] = a0
    106     R = K[This is the Trac macro *var* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#var-macro)
--> 107     return R(val, prec=prec, check=False)
    108 
    109 ######################################################################

/home/ghitza/sage-devel/local/lib/python2.6/site-packages/sage/rings/power_series_ring.pyc in __call__(self, f, prec, check)
    408             v = sage_eval(f.Eltseq())
    409             return self(v) * (self.gen(0)**f.Valuation())
--> 410         return self.__power_series_class(self, f, prec, check=check)
    411         
    412     def construction(self):

/home/ghitza/sage-devel/local/lib/python2.6/site-packages/sage/rings/power_series_poly.so in sage.rings.power_series_poly.PowerSeries_poly.__init__ (sage/rings/power_series_poly.c:2373)()

/home/ghitza/sage-devel/local/lib/python2.6/site-packages/sage/structure/parent.so in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:6228)()

/home/ghitza/sage-devel/local/lib/python2.6/site-packages/sage/structure/coerce_maps.so in sage.structure.coerce_maps.DefaultConvertMap_unique._call_with_args (sage/structure/coerce_maps.c:3532)()

/home/ghitza/sage-devel/local/lib/python2.6/site-packages/sage/structure/coerce_maps.so in sage.structure.coerce_maps.DefaultConvertMap_unique._call_with_args (sage/structure/coerce_maps.c:3353)()

/home/ghitza/sage-devel/local/lib/python2.6/site-packages/sage/rings/polynomial/polynomial_ring.pyc in _element_constructor_(self, x, check, is_gen, construct, **kwds)
    310                 x = x.Polrev()
    311 
--> 312         return C(self, x, check, is_gen, construct=construct, **kwds)
    313 
    314     def is_integral_domain(self, proof = True):

/home/ghitza/sage-devel/local/lib/python2.6/site-packages/sage/rings/polynomial/polynomial_zmod_flint.so in sage.rings.polynomial.polynomial_zmod_flint.Polynomial_zmod_flint.__init__ (sage/rings/polynomial/polynomial_zmod_flint.c:10916)()

/home/ghitza/sage-devel/local/lib/python2.6/site-packages/sage/rings/polynomial/polynomial_zmod_flint.so in sage.rings.polynomial.polynomial_zmod_flint.Polynomial_zmod_flint._set_list (sage/rings/polynomial/polynomial_zmod_flint.c:11368)()

OverflowError: long int too large to convert
```


A side note: the workaround at the end of the method is not necessary any more, and can be removed.



---

Comment by AlexGhitza created at 2010-11-05 08:13:47

This bug appears to be gone in sage-4.6.  I'm not sure at what point it was fixed, but it was most likely when Martin Raum or David Loeffler touched the code recently.

In any case, I am attaching a mini-patch with a doctest that verifies that it is fixed.


---

Attachment


---

Comment by AlexGhitza created at 2010-11-05 08:15:52

cc-ing Martin and David in case they have more info about this.


---

Comment by AlexGhitza created at 2010-11-05 08:15:52

Changing status from new to needs_review.


---

Comment by mraum created at 2010-11-05 15:47:55

Changing status from needs_review to positive_review.


---

Comment by mraum created at 2010-11-05 15:47:55

This has been indeed fixed by David from what I see in googlecodes, and he also added the doctest right before yours. It's a good a idea to introduce another explicit test and it won't cost much time. So this gets a positive review.


---

Comment by jdemeyer created at 2010-11-10 22:19:38

Resolution: fixed
