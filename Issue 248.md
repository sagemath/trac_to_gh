# Issue 248: elliptic curve constructor in funny case -- coercion issues

archive/issues_000248.json:
```json
{
    "body": "Assignee: @williamstein\n\n\n```\n \nWe still have problems coercing constants into polynomial rings, when\nthe constants are themselves in interesting rings...\n \nsage: R = ZZ['u', 'v']\n \nsage: EllipticCurve(R, [1,1])\n---------------------------------------------------------------------------\n<type 'exceptions.TypeError'>             Traceback (most recent call\nlast)\n \n/Users/nalexand/<ipython console> in <module>()\n \n/Users/nalexand/Devel/sage/local/lib/python2.5/site-packages/sage/\nschemes/elliptic_curves/constructor.py in EllipticCurve(x, y)\n     97             return\nell_finite_field.EllipticCurve_finite_field(x, y)\n     98         else:\n---> 99             return ell_generic.EllipticCurve_generic(x, y)\n    100\n    101     if isinstance(x, str):\n \n/Users/nalexand/Devel/sage/local/lib/python2.5/site-packages/sage/\nschemes/elliptic_curves/ell_generic.py in __init__(self, ainvs, extra)\n     95         a1, a2, a3, a4, a6 = ainvs\n     96         f = y**2*z + (a1*x + a3*z)*y*z \\\n---> 97             - (x**3 + a2*x**2*z + a4*x*z**2 + a6*z**3)\n     98         plane_curve.ProjectiveCurve_generic.__init__(self, PP,\nf)\n     99         if K.is_field():\n \n/Users/nalexand/element.pyx in element.RingElement.__mul__()\n \n/Users/nalexand/element.pyx in element.bin_op_c()\n \n<type 'exceptions.TypeError'>: unsupported operand parent(s) for '*':\n'Polynomial Ring in u, v over Integer Ring' and 'Polynomial Ring in x,\ny, z over Polynomial Ring in u, v over Integer Ring'\n \nNick\n \n \n----\n\n \nHmm, I thought this was a bug, but the following works:\n \nsage: R = ZZ['u', 'v'].fraction_field()\n \nsage: EllipticCurve(R, [1,1])\n Elliptic Curve defined by y^2  = x^3 + x +1 over Fraction Field of\nPolynomial Ring in u, v over Integer Ring\n \nMaybe the previous post shouldn't work, because it's a ring, not a\nfield?  There are some algorithms that use the discrepancy, so\nwhatever happens the situation should be clarified.\n \nNick\n\n----\n\n \nOn Tue, 6 Feb 2007, Nick Alexander wrote:\n> sage: R = ZZ['u', 'v']\n>  \n> sage: EllipticCurve(R, [1,1])\n> ---------------------------------------------------------------------------\n> <type 'exceptions.TypeError'>             Traceback (most recent call\n> last)\n \nBut the one variable version works ...\n \nRegards,\nIfti\n====\nsage: R = ZZ['u']\nsage: EllipticCurve(R, [1,1])\nElliptic Curve defined by y^2 + (0)*x*y + (0)*y = x^3 + (0)*x^2 + x +1\nover Univariate Polynomial Ring in u over Integer Ring\n \n \n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/248\n\n",
    "created_at": "2007-02-07T06:03:31Z",
    "labels": [
        "component: algebraic geometry",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.2",
    "title": "elliptic curve constructor in funny case -- coercion issues",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/248",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein


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


Issue created by migration from https://trac.sagemath.org/ticket/248





---

archive/issue_comments_001089.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-08-18T18:04:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/248",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/248#issuecomment-1089",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_events_000262.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-08-18T18:04:17Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/248",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/248#event-262"
}
```
