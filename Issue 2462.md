# Issue 2462: Odd results when adding Laurent series

archive/issues_002462.json:
```json
{
    "body": "Assignee: was\n\nThe following code, which defines a Laurent series ring over a field extension of QQ, gives a weird error when one tries to add and subract Laurent series, all defined over the same ring.\n\n\n```\nQx.<xxx>=PolynomialRing(QQ)\n\nK.<w>=NumberField(xxx^2+xxx+1)\n\nR.<y>=PolynomialRing(K)\n\nL.<s>=K.extension(y^6+y^5+y^4+y^3+y^2+y+1)\n\nS.<q>=LaurentSeriesRing(L,\"q\")\n\neta1=1 - q - q^2 + q^5 + q^7 - q^12 - q^15 + q^22 + q^26 - q^35 - q^40 + \\\nq^51+ q^57 - q^70 - q^77 + q^92 + q^100 - q^117 - q^126 + q^145 + q^155 -\\\nq^176 - q^187 + q^210 + q^222 - q^247 - q^260 + \\\nq^287 + q^301 - q^330 -q^345 + q^376 + q^392 - q^425 - q^442 + q^477 + q^495\n\neta7=eta1(q^7 )+O(q^500)\n\neta49=eta1(q^49)+O(q^500)\n\nx=q^(-2)*eta1*eta49^-1\ny=eta7^4*eta49^-4\n\nx+y-x-y\n```\n\n\nThe error is:\n\n\n```\n<type 'exceptions.TypeError'>             Traceback (most recent call last)\n\n/home/ljpk/<ipython console> in <module>()\n\n/home/ljpk/element.pyx in sage.structure.element.ModuleElement.__sub__()\n\n/home/ljpk/coerce.pxi in sage.structure.element._sub_c()\n\n/home/ljpk/laurent_series_ring_element.pyx in sage.rings.laurent_series_ring_element.LaurentSeries._sub_c_impl()\n\n/home/ljpk/laurent_series_ring_element.pyx in sage.rings.laurent_series_ring_element.LaurentSeries.__init__()\n\n/home/ljpk/power_series_poly.pyx in sage.rings.power_series_poly.PowerSeries_poly.valuation()\n\n/home/ljpk/polynomial_element.pyx in sage.rings.polynomial.polynomial_element.Polynomial.valuation()\n\n<type 'exceptions.TypeError'>: The polynomial, p, must have the same parent as self.\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2462\n\n",
    "created_at": "2008-03-10T21:32:53Z",
    "labels": [
        "linear algebra",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2",
    "title": "Odd results when adding Laurent series",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2462",
    "user": "ljpk"
}
```
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



Issue created by migration from https://trac.sagemath.org/ticket/2462





---

archive/issue_comments_016684.json:
```json
{
    "body": "I've been debugging this for a while. The problem is somehow connected to the following. After running the example given, then do:\n\n\n```\nsage: h = ((x + y) - x).valuation_zero_part()\nsage: k = y.valuation_zero_part()\nsage: type(h)\n<type 'sage.rings.power_series_poly.PowerSeries_poly'>\nsage: type(k)\n<type 'sage.rings.power_series_poly.PowerSeries_poly'>\nsage: parent(h) is parent(k)\nTrue\nsage: f = (h - k).polynomial()\nsage: f\n0\nsage: len(f.coeffs())\n498\n```\n\n\nSo somehow a polynomial is being created whose value is zero, yet which has 498 zero coefficients, i.e. it's not being normalised properly. Then the valuation method blows up:\n\n\n```\nsage: f.valuation()\n[boom]\n```\n",
    "created_at": "2008-03-15T03:52:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2462",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2462#issuecomment-16684",
    "user": "dmharvey"
}
```

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

archive/issue_comments_016685.json:
```json
{
    "body": "Changing component from linear algebra to coercion.",
    "created_at": "2008-10-29T13:27:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2462",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2462#issuecomment-16685",
    "user": "mabshoff"
}
```

Changing component from linear algebra to coercion.



---

archive/issue_comments_016686.json:
```json
{
    "body": "This is still a problem with 3.2.alpha2-ish:\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n| Sage Version 3.2.alpha1, Release Date: 2008-10-26                  |\n| Type notebook() for the GUI, and license() for information.        |\nsage: Qx.<xxx>=PolynomialRing(QQ)\nsage: \nsage: K.<w>=NumberField(xxx^2+xxx+1)\nsage: \nsage: R.<y>=PolynomialRing(K)\nsage: \nsage: L.<s>=K.extension(y^6+y^5+y^4+y^3+y^2+y+1)\nsage: \nsage: S.<q>=LaurentSeriesRing(L,\"q\")\nsage: \nsage: eta1=1 - q - q^2 + q^5 + q^7 - q^12 - q^15 + q^22 + q^26 - q^35 - q^40 + \\\n....: q^51+ q^57 - q^70 - q^77 + q^92 + q^100 - q^117 - q^126 + q^145 + q^155 -\\\n....: q^176 - q^187 + q^210 + q^222 - q^247 - q^260 + \\\n....: q^287 + q^301 - q^330 -q^345 + q^376 + q^392 - q^425 - q^442 + q^477 + q^495\nsage: \nsage: eta7=eta1(q^7 )+O(q^500)\nsage: \nsage: eta49=eta1(q^49)+O(q^500)\nsage: \nsage: x=q^(-2)*eta1*eta49^-1\nsage: y=eta7^4*eta49^-4\nsage: \nsage: x+y-x-y\n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n\n/scratch/mabshoff/release-cycle/sage-3.2.alpha2/<ipython console> in <module>()\n\n/scratch/mabshoff/release-cycle/sage-3.2.alpha2/local/lib/python2.5/site-packages/sage/structure/element.so in sage.structure.element.ModuleElement.__sub__ (sage/structure/element.c:5718)()\n\n/scratch/mabshoff/release-cycle/sage-3.2.alpha2/local/lib/python2.5/site-packages/sage/rings/laurent_series_ring_element.so in sage.rings.laurent_series_ring_element.LaurentSeries._sub_ (sage/rings/laurent_series_ring_element.c:5543)()\n\n/scratch/mabshoff/release-cycle/sage-3.2.alpha2/local/lib/python2.5/site-packages/sage/rings/laurent_series_ring_element.so in sage.rings.laurent_series_ring_element.LaurentSeries.__init__ (sage/rings/laurent_series_ring_element.c:1831)()\n\n/scratch/mabshoff/release-cycle/sage-3.2.alpha2/local/lib/python2.5/site-packages/sage/rings/power_series_poly.so in sage.rings.power_series_poly.PowerSeries_poly.valuation (sage/rings/power_series_poly.c:2296)()\n\n/scratch/mabshoff/release-cycle/sage-3.2.alpha2/local/lib/python2.5/site-packages/sage/rings/polynomial/polynomial_element.so in sage.rings.polynomial.polynomial_element.Polynomial.valuation (sage/rings/polynomial/polynomial_element.c:24197)()\n\nTypeError: The polynomial, p, must have the same parent as self.\n```\n\n\nRobert: Any idea what is going on here?\n\nCheers,\n\nMichael",
    "created_at": "2008-10-29T13:27:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2462",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2462#issuecomment-16686",
    "user": "mabshoff"
}
```

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

archive/issue_comments_016687.json:
```json
{
    "body": "Changing assignee from was to robertwb.",
    "created_at": "2008-10-29T13:27:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2462",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2462#issuecomment-16687",
    "user": "mabshoff"
}
```

Changing assignee from was to robertwb.



---

archive/issue_comments_016688.json:
```json
{
    "body": "I really don't think this is due to coercion, as no coercion is going on here (all parents are identical, arithmetic is dispatched immediately). \n\nDavid Harvey is right, in polynomial_element.pyx:3672 we have \n\n\n```\n        if p is None:\n            for k from 0 <= k <= self.degree():\n                if self[k]:\n                    return ZZ(k)\n```\n\n\nbecause self is not detected to be zero earlier (even though it really is) the loop exits without returning, hence the [boom]. The error, however, occurred earlier. Somewhere, something's not getting normalized like it should be. I think the error is in polynomials. \n\nContinuing on David's session, \n\n\n```\nsage: f = h.polynomial() - k.polynomial()\nsage: f\n0\nsage: sage: len(f.coeffs())\n500\nsage: k.degree()\n499\nsage: k[499]  # ?!!\n0\n```\n",
    "created_at": "2008-10-29T15:38:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2462",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2462#issuecomment-16688",
    "user": "robertwb"
}
```

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

archive/issue_comments_016689.json:
```json
{
    "body": "Changing assignee from robertwb to tbd.",
    "created_at": "2008-10-29T15:38:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2462",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2462#issuecomment-16689",
    "user": "robertwb"
}
```

Changing assignee from robertwb to tbd.



---

archive/issue_comments_016690.json:
```json
{
    "body": "Changing component from coercion to algebra.",
    "created_at": "2008-10-29T15:38:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2462",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2462#issuecomment-16690",
    "user": "robertwb"
}
```

Changing component from coercion to algebra.



---

archive/issue_comments_016691.json:
```json
{
    "body": "More info \n\n\n```\nsage: x.valuation_zero_part().polynomial().degree()\n499\nsage: x.valuation_zero_part().polynomial()[499]\n0\n```\n",
    "created_at": "2008-10-30T18:57:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2462",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2462#issuecomment-16691",
    "user": "robertwb"
}
```

More info 


```
sage: x.valuation_zero_part().polynomial().degree()
499
sage: x.valuation_zero_part().polynomial()[499]
0
```




---

archive/issue_comments_016692.json:
```json
{
    "body": "Here's the actual error: \n\n\n```\nsage: S.<q> = CC[] # generic poly implementation\nsage: f = (1+q^10+q^100).truncate(50)\nsage: f.degree()\n49\n```\n\n\nI'm posting a patch to fix this.",
    "created_at": "2008-10-30T19:40:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2462",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2462#issuecomment-16692",
    "user": "robertwb"
}
```

Here's the actual error: 


```
sage: S.<q> = CC[] # generic poly implementation
sage: f = (1+q^10+q^100).truncate(50)
sage: f.degree()
49
```


I'm posting a patch to fix this.



---

archive/issue_comments_016693.json:
```json
{
    "body": "Attachment [2462-poly-truncate.patch](tarball://root/attachments/some-uuid/ticket2462/2462-poly-truncate.patch) by robertwb created at 2008-10-30 19:57:45",
    "created_at": "2008-10-30T19:57:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2462",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2462#issuecomment-16693",
    "user": "robertwb"
}
```

Attachment [2462-poly-truncate.patch](tarball://root/attachments/some-uuid/ticket2462/2462-poly-truncate.patch) by robertwb created at 2008-10-30 19:57:45



---

archive/issue_comments_016694.json:
```json
{
    "body": "#4406 is a followup ticket to this.\n\nCheers,\n\nMichael",
    "created_at": "2008-10-31T00:18:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2462",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2462#issuecomment-16694",
    "user": "mabshoff"
}
```

#4406 is a followup ticket to this.

Cheers,

Michael



---

archive/issue_comments_016695.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2008-10-31T00:33:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2462",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2462#issuecomment-16695",
    "user": "mhansen"
}
```

Looks good to me.



---

archive/issue_comments_016696.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-10-31T02:44:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2462",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2462#issuecomment-16696",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_016697.json:
```json
{
    "body": "Merged in Sage 3.2.alpha2",
    "created_at": "2008-10-31T02:44:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2462",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2462#issuecomment-16697",
    "user": "mabshoff"
}
```

Merged in Sage 3.2.alpha2
