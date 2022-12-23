# Issue 5451: Bug in addition of rational functions over a finite field

archive/issues_005451.json:
```json
{
    "body": "Assignee: tbd\n\nKeywords: rational function addition\n\nAlex Lara reported on sage-support on 20090307:\n\n```\nI recently upgrade sage from 3.2.3 to 3.3. I'm also have sage 3.1.1\nThe thing is that the following commands give different results:\n\nF.<theta>=FiniteField(9)\nA.<t> = PolynomialRing(F)\nK.<t> = FractionField(A)\nf= 2/(t^2+2*t); g =t^9/(t^18 + t^10 + t^2);f+g\n\nIn 3.1.1 gives the right answer (I guess) but in 3.2.3 give an error:\n\nZeroDivisionError                         Traceback (most recent call\nlast)\n...\nZeroDivisionError: division by zero in finite field.\n```\n\n\nIn more detail that traceback is\n\n```\nZeroDivisionError                         Traceback (most recent call last)\n\n/home/john/.sage/temp/ubuntu/30503/_home_john__sage_init_sage_0.py in <module>()\n\n/home/john/sage-3.4.alpha0/local/lib/python2.5/site-packages/sage/structure/element.so in sage.structure.element.ModuleElement.__add__ (sage/structure/element.c:5746)()\n\n/home/john/sage-3.4.alpha0/local/lib/python2.5/site-packages/sage/rings/fraction_field_element.so in sage.rings.fraction_field_element.FractionFieldElement._add_ (sage/rings/fraction_field_element.c:3975)()\n\n/home/john/sage-3.4.alpha0/local/lib/python2.5/site-packages/sage/structure/element.so in sage.structure.element.PrincipalIdealDomainElement.gcd (sage/structure/element.c:11697)()\n\n/home/john/sage-3.4.alpha0/local/lib/python2.5/site-packages/sage/rings/polynomial/polynomial_element_generic.pyc in _gcd(self, other)\n    558         Return the GCD of self and other, as a monic polynomial.\n    559         \"\"\"\n--> 560         g = EuclideanDomainElement._gcd(self, other)\n    561         c = g.leading_coefficient()\n    562         if c.is_unit():\n\n/home/john/sage-3.4.alpha0/local/lib/python2.5/site-packages/sage/structure/element.so in sage.structure.element.EuclideanDomainElement._gcd (sage/structure/element.c:11939)()\n\n/home/john/sage-3.4.alpha0/local/lib/python2.5/site-packages/sage/rings/polynomial/polynomial_element_generic.pyc in quo_rem(self, other)\n    542         Q = P.zero_element()\n    543         while R.degree() >= B.degree():\n--> 544             aaa = R.leading_coefficient()/B.leading_coefficient()\n    545             diff_deg=R.degree()-B.degree()\n    546             Q += P(aaa).shift(diff_deg)\n\n/home/john/sage-3.4.alpha0/local/lib/python2.5/site-packages/sage/structure/element.so in sage.structure.element.RingElement.__div__ (sage/structure/element.c:9099)()\n\n/home/john/sage-3.4.alpha0/local/lib/python2.5/site-packages/sage/rings/finite_field_givaro.so in sage.rings.finite_field_givaro.FiniteField_givaroElement._div_ (sage/rings/finite_field_givaro.cpp:9661)()\n\nZeroDivisionError: division by zero in finite field.\n```\n\n\nwhich shows that somewhere in a gcd computation, a leading coefficient of 0 is being returned.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5451\n\n",
    "created_at": "2009-03-07T14:35:16Z",
    "labels": [
        "algebra",
        "major",
        "bug"
    ],
    "title": "Bug in addition of rational functions over a finite field",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5451",
    "user": "cremona"
}
```
Assignee: tbd

Keywords: rational function addition

Alex Lara reported on sage-support on 20090307:

```
I recently upgrade sage from 3.2.3 to 3.3. I'm also have sage 3.1.1
The thing is that the following commands give different results:

F.<theta>=FiniteField(9)
A.<t> = PolynomialRing(F)
K.<t> = FractionField(A)
f= 2/(t^2+2*t); g =t^9/(t^18 + t^10 + t^2);f+g

In 3.1.1 gives the right answer (I guess) but in 3.2.3 give an error:

ZeroDivisionError                         Traceback (most recent call
last)
...
ZeroDivisionError: division by zero in finite field.
```


In more detail that traceback is

```
ZeroDivisionError                         Traceback (most recent call last)

/home/john/.sage/temp/ubuntu/30503/_home_john__sage_init_sage_0.py in <module>()

/home/john/sage-3.4.alpha0/local/lib/python2.5/site-packages/sage/structure/element.so in sage.structure.element.ModuleElement.__add__ (sage/structure/element.c:5746)()

/home/john/sage-3.4.alpha0/local/lib/python2.5/site-packages/sage/rings/fraction_field_element.so in sage.rings.fraction_field_element.FractionFieldElement._add_ (sage/rings/fraction_field_element.c:3975)()

/home/john/sage-3.4.alpha0/local/lib/python2.5/site-packages/sage/structure/element.so in sage.structure.element.PrincipalIdealDomainElement.gcd (sage/structure/element.c:11697)()

/home/john/sage-3.4.alpha0/local/lib/python2.5/site-packages/sage/rings/polynomial/polynomial_element_generic.pyc in _gcd(self, other)
    558         Return the GCD of self and other, as a monic polynomial.
    559         """
--> 560         g = EuclideanDomainElement._gcd(self, other)
    561         c = g.leading_coefficient()
    562         if c.is_unit():

/home/john/sage-3.4.alpha0/local/lib/python2.5/site-packages/sage/structure/element.so in sage.structure.element.EuclideanDomainElement._gcd (sage/structure/element.c:11939)()

/home/john/sage-3.4.alpha0/local/lib/python2.5/site-packages/sage/rings/polynomial/polynomial_element_generic.pyc in quo_rem(self, other)
    542         Q = P.zero_element()
    543         while R.degree() >= B.degree():
--> 544             aaa = R.leading_coefficient()/B.leading_coefficient()
    545             diff_deg=R.degree()-B.degree()
    546             Q += P(aaa).shift(diff_deg)

/home/john/sage-3.4.alpha0/local/lib/python2.5/site-packages/sage/structure/element.so in sage.structure.element.RingElement.__div__ (sage/structure/element.c:9099)()

/home/john/sage-3.4.alpha0/local/lib/python2.5/site-packages/sage/rings/finite_field_givaro.so in sage.rings.finite_field_givaro.FiniteField_givaroElement._div_ (sage/rings/finite_field_givaro.cpp:9661)()

ZeroDivisionError: division by zero in finite field.
```


which shows that somewhere in a gcd computation, a leading coefficient of 0 is being returned.

Issue created by migration from https://trac.sagemath.org/ticket/5451





---

archive/issue_comments_042202.json:
```json
{
    "body": "In sage/rings/polynomial/polynomial_ring_generic.py, in the function quo_rem, the test of other.is_zero() is sometimes returning False despite other being zero!  I added some print statements and here is an example:\n\n```\nin quo_rem (parent = Univariate Polynomial Ring in t over Finite Field in theta of size 3^2)...\nself =  t\nother =  0\nother.is_zero() =  False\nA =  t\nB =  0\n---------------------------------------------------------------------------\nZeroDivisionError  \n```\n\n\nThat is as far as I got.",
    "created_at": "2009-03-07T14:54:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5451",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5451#issuecomment-42202",
    "user": "cremona"
}
```

In sage/rings/polynomial/polynomial_ring_generic.py, in the function quo_rem, the test of other.is_zero() is sometimes returning False despite other being zero!  I added some print statements and here is an example:

```
in quo_rem (parent = Univariate Polynomial Ring in t over Finite Field in theta of size 3^2)...
self =  t
other =  0
other.is_zero() =  False
A =  t
B =  0
---------------------------------------------------------------------------
ZeroDivisionError  
```


That is as far as I got.



---

archive/issue_comments_042203.json:
```json
{
    "body": "Replying to [comment:1 cremona]:\n\nThis is a consequence of this:\n\n```\nsage: A.<x>=GF(9,'a')[]\nsage: A(0).shift(7).degree()\n6\n```\n",
    "created_at": "2009-03-07T15:18:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5451",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5451#issuecomment-42203",
    "user": "ylchapuy"
}
```

Replying to [comment:1 cremona]:

This is a consequence of this:

```
sage: A.<x>=GF(9,'a')[]
sage: A(0).shift(7).degree()
6
```




---

archive/issue_comments_042204.json:
```json
{
    "body": "Replying to [comment:2 ylchapuy]:\nreplying to myself: see also #5434",
    "created_at": "2009-03-07T15:21:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5451",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5451#issuecomment-42204",
    "user": "ylchapuy"
}
```

Replying to [comment:2 ylchapuy]:
replying to myself: see also #5434



---

archive/issue_comments_042205.json:
```json
{
    "body": "Thanks ylchpuy: I checked that applying the patch at 5434 makes this problem go away.\n\nHence this ticket can be scrapped, unless we want to add a doctest somewhere.",
    "created_at": "2009-03-07T15:30:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5451",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5451#issuecomment-42205",
    "user": "cremona"
}
```

Thanks ylchpuy: I checked that applying the patch at 5434 makes this problem go away.

Hence this ticket can be scrapped, unless we want to add a doctest somewhere.



---

archive/issue_comments_042206.json:
```json
{
    "body": "In a newly built 3.4.rc1 I can conform that the problem has indeed been solved by the other bug fix mentioned in this ticket:\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nsage: F.<theta>=FiniteField(9)\nsage: A.<t> = PolynomialRing(F)\nsage: K.<t> = FractionField(A)\nsage: f= 2/(t^2+2*t); g =t^9/(t^18 + t^10 + t^2);f+g\n(2*t^15 + 2*t^14 + 2*t^13 + 2*t^12 + 2*t^11 + 2*t^10 + 2*t^9 + t^7 + t^6 + t^5 + t^4 + t^3 + t^2 + t + 1)/(t^17 + t^9 + t)\n```\n\n| Sage Version 3.4.rc1, Release Date: 2009-03-08                     |\n| Type notebook() for the GUI, and license() for information.        |\nThis ticket can therefore be closed.",
    "created_at": "2009-03-09T13:18:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5451",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5451#issuecomment-42206",
    "user": "cremona"
}
```

In a newly built 3.4.rc1 I can conform that the problem has indeed been solved by the other bug fix mentioned in this ticket:

```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: F.<theta>=FiniteField(9)
sage: A.<t> = PolynomialRing(F)
sage: K.<t> = FractionField(A)
sage: f= 2/(t^2+2*t); g =t^9/(t^18 + t^10 + t^2);f+g
(2*t^15 + 2*t^14 + 2*t^13 + 2*t^12 + 2*t^11 + 2*t^10 + 2*t^9 + t^7 + t^6 + t^5 + t^4 + t^3 + t^2 + t + 1)/(t^17 + t^9 + t)
```

| Sage Version 3.4.rc1, Release Date: 2009-03-08                     |
| Type notebook() for the GUI, and license() for information.        |
This ticket can therefore be closed.



---

archive/issue_comments_042207.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-03-25T17:55:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5451",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5451#issuecomment-42207",
    "user": "burcin"
}
```

Resolution: fixed



---

archive/issue_comments_042208.json:
```json
{
    "body": "This ticket seems to have slipped under mabshoff's radar. I can verify that it is fixed in 3.4.",
    "created_at": "2009-03-25T17:55:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5451",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5451#issuecomment-42208",
    "user": "burcin"
}
```

This ticket seems to have slipped under mabshoff's radar. I can verify that it is fixed in 3.4.



---

archive/issue_comments_042209.json:
```json
{
    "body": "Hmm, what about a doctest then?\n\nCheers,\n\nMichael",
    "created_at": "2009-03-25T19:05:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5451",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5451#issuecomment-42209",
    "user": "mabshoff"
}
```

Hmm, what about a doctest then?

Cheers,

Michael



---

archive/issue_comments_042210.json:
```json
{
    "body": "Attachment\n\nadd doctest",
    "created_at": "2009-03-25T20:31:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5451",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5451#issuecomment-42210",
    "user": "burcin"
}
```

Attachment

add doctest



---

archive/issue_comments_042211.json:
```json
{
    "body": "Right, nothing gets past you. :)\n\nattachment:trac_5451-ratfun_doctest.patch adds the doctest.\n\nCheers,\nBurcin",
    "created_at": "2009-03-25T20:33:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5451",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5451#issuecomment-42211",
    "user": "burcin"
}
```

Right, nothing gets past you. :)

attachment:trac_5451-ratfun_doctest.patch adds the doctest.

Cheers,
Burcin



---

archive/issue_comments_042212.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2009-03-25T20:33:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5451",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5451#issuecomment-42212",
    "user": "burcin"
}
```

Changing status from closed to reopened.



---

archive/issue_comments_042213.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2009-03-25T20:33:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5451",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5451#issuecomment-42213",
    "user": "burcin"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_042214.json:
```json
{
    "body": "Looks good to me. This is consistent with the result from Sage 3.2 :)\n\nCheers,\n\nMichael",
    "created_at": "2009-03-25T22:18:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5451",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5451#issuecomment-42214",
    "user": "mabshoff"
}
```

Looks good to me. This is consistent with the result from Sage 3.2 :)

Cheers,

Michael



---

archive/issue_comments_042215.json:
```json
{
    "body": "Merged in Sage 3.4.1.alpha0.\n\nCheers,\n\nMichael",
    "created_at": "2009-03-25T23:01:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5451",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5451#issuecomment-42215",
    "user": "mabshoff"
}
```

Merged in Sage 3.4.1.alpha0.

Cheers,

Michael



---

archive/issue_comments_042216.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-03-25T23:01:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5451",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5451#issuecomment-42216",
    "user": "mabshoff"
}
```

Resolution: fixed
