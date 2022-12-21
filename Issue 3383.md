# Issue 3383: division_points() fails for elliptic curve over number field

Issue created by migration from Trac.

Original creator: cremona

Original creation time: 2008-06-08 17:04:20

Assignee: was

Keywords: elliptic curve

While testing/reviewing #3377 I found a problem with E.division_points() over a number field:


```
sage: E = EllipticCurve('19a1')
sage: K.<t> = NumberField(x^9-3*x^8-4*x^7+16*x^6-3*x^5-21*x^4+5*x^3+7*x^2-7*x+1)
sage: EK = E.base_extend(K)
sage: E(0).division_points(3)
[(0 : 1 : 0), (5 : -10 : 1), (5 : 9 : 1)]
sage: EK(0).division_points(3)
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)

/home/jec/<ipython console> in <module>()

/home/jec/sage-current/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/ell_point.py in division_points(self, m, poly_only)
    586             [(1 : 1 : 1)]
    587         """
--> 588         return self._division_points(m, poly_only=False)
    589
    590     def _division_points(self, m, poly_only):

/home/jec/sage-current/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/ell_point.py in _division_points(self, m, poly_only)
    609         F_to_E = F.isomorphism_to(E)
    610         E_to_F = E.isomorphism_to(F)
--> 611         f = F.multiplication_by_m(m, x_only=True)
    612
    613         # Map self (our point) over to the short Weierstrass model.

/home/jec/sage-current/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/ell_generic.py in multiplication_by_m(self, m, x_only)
   1822         # Silverman AEC Ex III.3.7, page 105.
   1823         phi_m = x*psi(m)**2 - psi(m+1)*psi(m-1)
-> 1824         x_coord = normalize(phi_m / psi_m**2)
   1825         if x_only:
   1826             # Return it if the optional parameter x_only is set.

/home/jec/sage-current/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/ell_generic.py in normalize(f)
   1817         Q = R.quotient(y**2 - x**3 - A*x - B)
   1818         def normalize(f):
-> 1819             return Q(f.numerator()).lift() / Q(f.denominator()).lift()
   1820
   1821         # Write down the x coordinate using the formula in

/home/jec/sage-current/local/lib/python2.5/site-packages/sage/rings/quotient_ring.py in __call__(self, x, coerce)
    402             R = self.cover_ring()
    403             x = R(x)
--> 404         return quotient_ring_element.QuotientRingElement(self, x)
    405
    406     def _coerce_impl(self, x):

/home/jec/sage-current/local/lib/python2.5/site-packages/sage/rings/quotient_ring_element.py in __init__(self, parent, rep, reduce)
     72         self.__rep = rep
     73         if reduce:
---> 74             self._reduce_()
     75
     76     def _reduce_(self):

/home/jec/sage-current/local/lib/python2.5/site-packages/sage/rings/quotient_ring_element.py in _reduce_(self)
     76     def _reduce_(self):
     77         I = self.parent().defining_ideal()
---> 78         self.__rep = I.reduce(self.__rep)
     79
     80     def copy(self):

/home/jec/sage-current/local/lib/python2.5/site-packages/sage/rings/polynomial/multi_polynomial_ideal.py in reduce(self, f)
   1921         very expensive operation.
   1922         """
-> 1923         gb = self.groebner_basis()
   1924         return f.reduce(gb)
   1925

/home/jec/sage-current/local/lib/python2.5/site-packages/sage/rings/polynomial/multi_polynomial_ideal.py in groebner_basis(self, algorithm, *args, **kwds)
   1840                 except TypeError: # conversion to Singular not supported
   1841                     # we might want to print a warning here
-> 1842                     gb = toy_buchberger.buchberger_improved(self, *args, **kwds)
   1843         elif algorithm.startswith('singular:'):
   1844             gb = self._groebner_basis_using_singular(algorithm[9:])

/home/jec/sage-current/local/lib/python2.5/site-packages/sage/rings/polynomial/toy_buchberger.py in buchberger_improved(F)
    203     function printing intermediate Groebner bases.
    204     """
--> 205     F = inter_reduction(F.gens())
    206
    207     G = set()

/home/jec/sage-current/local/lib/python2.5/site-packages/sage/rings/polynomial/toy_buchberger.py in inter_reduction(Q)
    343         for p in Qbar:
    344             p = Q.pop()
--> 345             h = p.reduce(Q)
    346             if h!=0:
    347                 Q.add(h)

/home/jec/sage-current/local/lib/python2.5/site-packages/sage/rings/polynomial/multi_polynomial_element.py in reduce(self, I)
   1543                         break
   1544                 else:
-> 1545                     plt = p.lt()
   1546                     r += plt
   1547                     p -= plt

/home/jec/sage-current/local/lib/python2.5/site-packages/sage/rings/polynomial/multi_polynomial_element.py in lt(self)
   1160             R = self.parent()
   1161             f = self._MPolynomial_element__element.dict()
-> 1162             res = self._MPolynomial_element__element.lcmt( R.term_order().greater_tuple )
   1163             self.__lt = MPolynomial_polydict(R,polydict.PolyDict({res:f[res]},force_int_exponents=False, force_etuples=False))
   1164             return self.__lt

/home/jec/sage-current/local/lib/python2.5/site-packages/sage/rings/polynomial/term_order.py in __getattr__(self, name)
    351         elif name=='greater_tuple':
    352             if len(self.blocks) == 1:
--> 353                 return getattr(self,'greater_tuple_'+self.__singular_str)
    354             else:
    355                 return self.greater_tuple_block

/home/jec/sage-current/local/lib/python2.5/site-packages/sage/rings/polynomial/term_order.py in __getattr__(self, name)
    355                 return self.greater_tuple_block
    356         else:
--> 357             raise AttributeError,name
    358
    359     def compare_tuples_lp(self,f,g):

AttributeError: greater_tuple_revlex
```


It looks quite deep in polynomial code but might turn out to be something simple.


---

Comment by malb created at 2008-06-10 18:02:47

The code tries to compute in 
 * a local ordering "revlex" for which toy_buchberger.py is inadequat
 * a ordering "revlex" which isn't really supported or misnamed, we do have "invlex"


---

Comment by cremona created at 2008-06-10 19:13:36

Replying to [comment:2 malb]:
> The code tries to compute in 
>  * a local ordering "revlex" for which toy_buchberger.py is inadequat
>  * a ordering "revlex" which isn't really supported or misnamed, we do have "invlex"

malb: I am fixing this as part of a rewrite for division-polynomial related stuff, which will not need to use such things at all, so I don't think you need to worry about this (at least for now).
John


---

Comment by mabshoff created at 2008-08-13 07:23:35

This works for me:

```
mabshoff`@`sage:/scratch/mabshoff/release-cycle/sage-3.1.alpha2$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 3.1.alpha1, Release Date: 2008-08-11                  |
| Type notebook() for the GUI, and license() for information.        |
sage: E = EllipticCurve('19a1')
sage: K.<t> = NumberField(x^9-3*x^8-4*x^7+16*x^6-3*x^5-21*x^4+5*x^3+7*x^2-7*x+1)
sage: EK = E.base_extend(K)
sage: E(0).division_points(3)
[(0 : 1 : 0), (5 : -10 : 1), (5 : 9 : 1)]
sage: EK(0).division_points(3)
[(0 : 1 : 0), (5 : 9 : 1), (5 : -10 : 1)]
```



---

Comment by cremona created at 2008-08-13 08:27:52

It works for me too.  I think that something deep down changed, so now it just works.

It is still true that I am working on improving division poly stuff -- but on a clone which is on a machine currently broken, preventing me from finishing it off.

In the meantime, let's just close this.


---

Comment by mabshoff created at 2008-08-13 08:32:23

Hi John,

Replying to [comment:5 cremona]:
> It works for me too.  I think that something deep down changed, so now it just works.
> 
> It is still true that I am working on improving division poly stuff -- but on a clone which is on a machine currently broken, preventing me from finishing it off.
> 
> In the meantime, let's just close this.

I agree, but let's add a doctest to catch this in case someone breaks it again.

Cheers,

Michael


---

Comment by cremona created at 2008-08-13 08:37:13

Replying to [comment:6 mabshoff]:
> Hi John,
> 
> Replying to [comment:5 cremona]:
> > It works for me too.  I think that something deep down changed, so now it just works.
> > 
> > It is still true that I am working on improving division poly stuff -- but on a clone which is on a machine currently broken, preventing me from finishing it off.
> > 
> > In the meantime, let's just close this.
> 
> I agree, but let's add a doctest to catch this in case someone breaks it again.
> 

Coming up...

John

> Cheers,
> 
> Michael


---

Attachment

The patch just adds a doctest to show that the bug no longer exists.


---

Comment by mabshoff created at 2008-08-13 09:14:09

Looks good to me and doctests fine. William also likes it.

Cheers,

Michael


---

Comment by mabshoff created at 2008-08-13 09:14:30

Merged in Sage 3.1.alpha2


---

Comment by mabshoff created at 2008-08-13 09:14:30

Resolution: fixed
