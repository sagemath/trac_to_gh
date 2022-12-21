# Issue 248: elliptic curve constructor in funny case -- coercion issues

Issue created by migration from Trac.

Original creator: was

Original creation time: 2007-02-07 06:03:31

Assignee: was


```
 
We still have problems coercing constants into polynomial rings, when
the constants are themselves in interesting rings...
 
sage: R = ZZ['u', 'v']
 
sage: EllipticCurve(R, [1,1])
---------------------------------------------------------------------------
<type 'exceptions.TypeError'>             Traceback (most recent call
last)
 
/Users/nalexand/<ipython console> in <module>()
 
/Users/nalexand/Devel/sage/local/lib/python2.5/site-packages/sage/
schemes/elliptic_curves/constructor.py in EllipticCurve(x, y)
     97             return
ell_finite_field.EllipticCurve_finite_field(x, y)
     98         else:
---> 99             return ell_generic.EllipticCurve_generic(x, y)
    100
    101     if isinstance(x, str):
 
/Users/nalexand/Devel/sage/local/lib/python2.5/site-packages/sage/
schemes/elliptic_curves/ell_generic.py in __init__(self, ainvs, extra)
     95         a1, a2, a3, a4, a6 = ainvs
     96         f = y**2*z + (a1*x + a3*z)*y*z \
---> 97             - (x**3 + a2*x**2*z + a4*x*z**2 + a6*z**3)
     98         plane_curve.ProjectiveCurve_generic.__init__(self, PP,
f)
     99         if K.is_field():
 
/Users/nalexand/element.pyx in element.RingElement.__mul__()
 
/Users/nalexand/element.pyx in element.bin_op_c()
 
<type 'exceptions.TypeError'>: unsupported operand parent(s) for '*':
'Polynomial Ring in u, v over Integer Ring' and 'Polynomial Ring in x,
y, z over Polynomial Ring in u, v over Integer Ring'
 
Nick
 
 
----

 
Hmm, I thought this was a bug, but the following works:
 
sage: R = ZZ['u', 'v'].fraction_field()
 
sage: EllipticCurve(R, [1,1])
 Elliptic Curve defined by y^2  = x^3 + x +1 over Fraction Field of
Polynomial Ring in u, v over Integer Ring
 
Maybe the previous post shouldn't work, because it's a ring, not a
field?  There are some algorithms that use the discrepancy, so
whatever happens the situation should be clarified.
 
Nick

----

 
On Tue, 6 Feb 2007, Nick Alexander wrote:
> sage: R = ZZ['u', 'v']
>  
> sage: EllipticCurve(R, [1,1])
> ---------------------------------------------------------------------------
> <type 'exceptions.TypeError'>             Traceback (most recent call
> last)
 
But the one variable version works ...
 
Regards,
Ifti
====
sage: R = ZZ['u']
sage: EllipticCurve(R, [1,1])
Elliptic Curve defined by y^2 + (0)*x*y + (0)*y = x^3 + (0)*x^2 + x +1
over Univariate Polynomial Ring in u over Integer Ring
 
 
```



---

Comment by was created at 2007-08-18 18:04:17

Resolution: fixed
