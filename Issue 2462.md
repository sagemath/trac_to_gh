# Issue 2462: Odd results when adding Laurent series

Issue created by migration from https://trac.sagemath.org/ticket/2462

Original creator: ljpk

Original creation time: 2008-03-10 21:32:53

Assignee: was

The following code, which defines a Laurent series ring over a field extension of QQ, gives a weird error when one tries to add and subract Laurent series, all defined over the same ring.


```
Qx.<xxx>=PolynomialRing(QQ)

K.<w>=NumberField(xxx^2+xxx+1)

R.<y>=PolynomialRing(K)

L.<s>=K.extension(y^6+y^5+y^4+y^3+y^2+y+1)

S.<q>=LaurentSeriesRing(L,"q")

eta1=1 - q - q^2 + q^5 + q^7 - q^12 - q^15 + q^22 + q^26 - q^35 - q^40 + \
q^51+ q^57 - q^70 - q^77 + q^92 + q^100 - q^117 - q^126 + q^145 + q^155 -\
q^176 - q^187 + q^210 + q^222 - q^247 - q^260 + \
q^287 + q^301 - q^330 -q^345 + q^376 + q^392 - q^425 - q^442 + q^477 + q^495

eta7=eta1(q^7 )+O(q^500)

eta49=eta1(q^49)+O(q^500)

x=q^(-2)*eta1*eta49^-1
y=eta7^4*eta49^-4

x+y-x-y
```


The error is:


```
<type 'exceptions.TypeError'>             Traceback (most recent call last)

/home/ljpk/<ipython console> in <module>()

/home/ljpk/element.pyx in sage.structure.element.ModuleElement.__sub__()

/home/ljpk/coerce.pxi in sage.structure.element._sub_c()

/home/ljpk/laurent_series_ring_element.pyx in sage.rings.laurent_series_ring_element.LaurentSeries._sub_c_impl()

/home/ljpk/laurent_series_ring_element.pyx in sage.rings.laurent_series_ring_element.LaurentSeries.__init__()

/home/ljpk/power_series_poly.pyx in sage.rings.power_series_poly.PowerSeries_poly.valuation()

/home/ljpk/polynomial_element.pyx in sage.rings.polynomial.polynomial_element.Polynomial.valuation()

<type 'exceptions.TypeError'>: The polynomial, p, must have the same parent as self.
```




---

Comment by dmharvey created at 2008-03-15 03:52:35

I've been debugging this for a while. The problem is somehow connected to the following. After running the example given, then do:


```
sage: h = ((x + y) - x).valuation_zero_part()
sage: k = y.valuation_zero_part()
sage: type(h)
<type 'sage.rings.power_series_poly.PowerSeries_poly'>
sage: type(k)
<type 'sage.rings.power_series_poly.PowerSeries_poly'>
sage: parent(h) is parent(k)
True
sage: f = (h - k).polynomial()
sage: f
0
sage: len(f.coeffs())
498
```


So somehow a polynomial is being created whose value is zero, yet which has 498 zero coefficients, i.e. it's not being normalised properly. Then the valuation method blows up:


```
sage: f.valuation()
[boom]
```



---

Comment by mabshoff created at 2008-10-29 13:27:54

Changing component from linear algebra to coercion.


---

Comment by mabshoff created at 2008-10-29 13:27:54

This is still a problem with 3.2.alpha2-ish:

```
----------------------------------------------------------------------
----------------------------------------------------------------------
| Sage Version 3.2.alpha1, Release Date: 2008-10-26                  |
| Type notebook() for the GUI, and license() for information.        |
sage: Qx.<xxx>=PolynomialRing(QQ)
sage: 
sage: K.<w>=NumberField(xxx^2+xxx+1)
sage: 
sage: R.<y>=PolynomialRing(K)
sage: 
sage: L.<s>=K.extension(y^6+y^5+y^4+y^3+y^2+y+1)
sage: 
sage: S.<q>=LaurentSeriesRing(L,"q")
sage: 
sage: eta1=1 - q - q^2 + q^5 + q^7 - q^12 - q^15 + q^22 + q^26 - q^35 - q^40 + \
....: q^51+ q^57 - q^70 - q^77 + q^92 + q^100 - q^117 - q^126 + q^145 + q^155 -\
....: q^176 - q^187 + q^210 + q^222 - q^247 - q^260 + \
....: q^287 + q^301 - q^330 -q^345 + q^376 + q^392 - q^425 - q^442 + q^477 + q^495
sage: 
sage: eta7=eta1(q^7 )+O(q^500)
sage: 
sage: eta49=eta1(q^49)+O(q^500)
sage: 
sage: x=q^(-2)*eta1*eta49^-1
sage: y=eta7^4*eta49^-4
sage: 
sage: x+y-x-y
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/scratch/mabshoff/release-cycle/sage-3.2.alpha2/<ipython console> in <module>()

/scratch/mabshoff/release-cycle/sage-3.2.alpha2/local/lib/python2.5/site-packages/sage/structure/element.so in sage.structure.element.ModuleElement.__sub__ (sage/structure/element.c:5718)()

/scratch/mabshoff/release-cycle/sage-3.2.alpha2/local/lib/python2.5/site-packages/sage/rings/laurent_series_ring_element.so in sage.rings.laurent_series_ring_element.LaurentSeries._sub_ (sage/rings/laurent_series_ring_element.c:5543)()

/scratch/mabshoff/release-cycle/sage-3.2.alpha2/local/lib/python2.5/site-packages/sage/rings/laurent_series_ring_element.so in sage.rings.laurent_series_ring_element.LaurentSeries.__init__ (sage/rings/laurent_series_ring_element.c:1831)()

/scratch/mabshoff/release-cycle/sage-3.2.alpha2/local/lib/python2.5/site-packages/sage/rings/power_series_poly.so in sage.rings.power_series_poly.PowerSeries_poly.valuation (sage/rings/power_series_poly.c:2296)()

/scratch/mabshoff/release-cycle/sage-3.2.alpha2/local/lib/python2.5/site-packages/sage/rings/polynomial/polynomial_element.so in sage.rings.polynomial.polynomial_element.Polynomial.valuation (sage/rings/polynomial/polynomial_element.c:24197)()

TypeError: The polynomial, p, must have the same parent as self.
```


Robert: Any idea what is going on here?

Cheers,

Michael


---

Comment by mabshoff created at 2008-10-29 13:27:54

Changing assignee from was to robertwb.


---

Comment by robertwb created at 2008-10-29 15:38:46

I really don't think this is due to coercion, as no coercion is going on here (all parents are identical, arithmetic is dispatched immediately). 

David Harvey is right, in polynomial_element.pyx:3672 we have 


```
        if p is None:
            for k from 0 <= k <= self.degree():
                if self[k]:
                    return ZZ(k)
```


because self is not detected to be zero earlier (even though it really is) the loop exits without returning, hence the [boom]. The error, however, occurred earlier. Somewhere, something's not getting normalized like it should be. I think the error is in polynomials. 

Continuing on David's session, 


```
sage: f = h.polynomial() - k.polynomial()
sage: f
0
sage: sage: len(f.coeffs())
500
sage: k.degree()
499
sage: k[499]  # ?!!
0
```



---

Comment by robertwb created at 2008-10-29 15:38:46

Changing assignee from robertwb to tbd.


---

Comment by robertwb created at 2008-10-29 15:38:46

Changing component from coercion to algebra.


---

Comment by robertwb created at 2008-10-30 18:57:30

More info 


```
sage: x.valuation_zero_part().polynomial().degree()
499
sage: x.valuation_zero_part().polynomial()[499]
0
```



---

Comment by robertwb created at 2008-10-30 19:40:46

Here's the actual error: 


```
sage: S.<q> = CC[] # generic poly implementation
sage: f = (1+q^10+q^100).truncate(50)
sage: f.degree()
49
```


I'm posting a patch to fix this.


---

Attachment


---

Comment by mabshoff created at 2008-10-31 00:18:58

#4406 is a followup ticket to this.

Cheers,

Michael


---

Comment by mhansen created at 2008-10-31 00:33:09

Looks good to me.


---

Comment by mabshoff created at 2008-10-31 02:44:21

Resolution: fixed


---

Comment by mabshoff created at 2008-10-31 02:44:21

Merged in Sage 3.2.alpha2
