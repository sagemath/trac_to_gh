# Issue 9263: airy_ai yields wrong results in arbitrary precision

archive/issues_009263.json:
```json
{
    "body": "Assignee: @aghitza\n\nCC:  @eviatarbach\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nsage: n(airy_ai(1),digits=100)\n0.1352924163128813861423083153567858971655368804931640625000000000000000000000000000000000000000000000\n```\nClearly the last digits are wrong. It looks like Sage only knows how\nto compute Ai(x) in double precision, and then extended the double\nprecision result to 100 digits.\n| Sage Version 4.4.2, Release Date: 2010-05-19                       |\n| Type notebook() for the GUI, and license() for information.        |\nThis is a *defect*: an error should be raised if the target precision cannot be attained (or Sage should be able to compute\nAi(x) to arbitrary precision).\n\nI guess this problem concerns other functions than Ai.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9263\n\n",
    "created_at": "2010-06-18T11:33:59Z",
    "labels": [
        "component: basic arithmetic",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "airy_ai yields wrong results in arbitrary precision",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9263",
    "user": "https://github.com/zimmermann6"
}
```
Assignee: @aghitza

CC:  @eviatarbach

```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: n(airy_ai(1),digits=100)
0.1352924163128813861423083153567858971655368804931640625000000000000000000000000000000000000000000000
```
Clearly the last digits are wrong. It looks like Sage only knows how
to compute Ai(x) in double precision, and then extended the double
precision result to 100 digits.
| Sage Version 4.4.2, Release Date: 2010-05-19                       |
| Type notebook() for the GUI, and license() for information.        |
This is a *defect*: an error should be raised if the target precision cannot be attained (or Sage should be able to compute
Ai(x) to arbitrary precision).

I guess this problem concerns other functions than Ai.

Issue created by migration from https://trac.sagemath.org/ticket/9263





---

archive/issue_comments_087017.json:
```json
{
    "body": "one solution would be to use mpmath:\n\n```\nsage: import mpmath\nsage: mpmath.mp.dps = 100\nsage: mpmath.airyai(1)\nmpf('0.1352924163128814155241474235154663061749441429883307060091020547576335348022657236634871099087486832138')\n```",
    "created_at": "2010-06-18T23:54:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9263",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9263#issuecomment-87017",
    "user": "https://trac.sagemath.org/admin/accounts/users/ylchapuy"
}
```

one solution would be to use mpmath:

```
sage: import mpmath
sage: mpmath.mp.dps = 100
sage: mpmath.airyai(1)
mpf('0.1352924163128814155241474235154663061749441429883307060091020547576335348022657236634871099087486832138')
```



---

archive/issue_comments_087018.json:
```json
{
    "body": "There appear to be two different problems related to numerical evaluation with Maxima. First, that some functions are locked to float precision. In Maxima:\n\n```\n(%i15) airy_ai(bfloat(%pi)),fpprec:20;\n(%o15)                 airy_ai(3.1415926535897932385b0)\n```\n\nI think it's returning unevaluated because `airy_ai` doesn't know how to operate on `bigfloat`s.\n\nOther functions do know how to operate on `bigfloat`s:\n\n```\n(%i18) bfloat(spherical_bessel_j(4, bfloat(%pi))),fpprec:200;\n(%o18) 6.471630031847746208103870635408583211756194941699504852294921875b-2\n```\n\nBut, the interface is losing precision:\n\n```\nsage: spherical_bessel_J(4, pi.n(digits=1000)).n(digits=100)\n0.06471630031847745712081376723290304653346538543701171875000000000000000000000000000000000000000000000\n```\n\nThis is because Maxima truncates to float precision:\n\n\n```\n(%i20) 3.141592653589793238462643383279502884197169399375105820974944592307816406286208998628034825,fpprec:200;\n(%o20)                         3.141592653589793\n```\n\nOne way of avoiding this is converting to an exact rational and passing it to `bfloat`, which may not be worth the overhead. Maybe something like the patch in #11643?",
    "created_at": "2013-06-14T08:23:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9263",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9263#issuecomment-87018",
    "user": "https://github.com/eviatarbach"
}
```

There appear to be two different problems related to numerical evaluation with Maxima. First, that some functions are locked to float precision. In Maxima:

```
(%i15) airy_ai(bfloat(%pi)),fpprec:20;
(%o15)                 airy_ai(3.1415926535897932385b0)
```

I think it's returning unevaluated because `airy_ai` doesn't know how to operate on `bigfloat`s.

Other functions do know how to operate on `bigfloat`s:

```
(%i18) bfloat(spherical_bessel_j(4, bfloat(%pi))),fpprec:200;
(%o18) 6.471630031847746208103870635408583211756194941699504852294921875b-2
```

But, the interface is losing precision:

```
sage: spherical_bessel_J(4, pi.n(digits=1000)).n(digits=100)
0.06471630031847745712081376723290304653346538543701171875000000000000000000000000000000000000000000000
```

This is because Maxima truncates to float precision:


```
(%i20) 3.141592653589793238462643383279502884197169399375105820974944592307816406286208998628034825,fpprec:200;
(%o20)                         3.141592653589793
```

One way of avoiding this is converting to an exact rational and passing it to `bfloat`, which may not be worth the overhead. Maybe something like the patch in #11643?



---

archive/issue_comments_087019.json:
```json
{
    "body": "I believe the \"correct\" solution (for Sage) for now is to use #12455 and mpmath for (at least default) evaluation.  I've cc:ed you on that ticket.",
    "created_at": "2013-06-14T12:13:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9263",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9263#issuecomment-87019",
    "user": "https://github.com/kcrisman"
}
```

I believe the "correct" solution (for Sage) for now is to use #12455 and mpmath for (at least default) evaluation.  I've cc:ed you on that ticket.



---

archive/issue_comments_087020.json:
```json
{
    "body": "Oh, thank you. I guess there's not much use working on the Maxima problems when mpmath works well. I'll change this ticket to apply to all Maxima-evaluated functions.",
    "created_at": "2013-06-14T18:24:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9263",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9263#issuecomment-87020",
    "user": "https://github.com/eviatarbach"
}
```

Oh, thank you. I guess there's not much use working on the Maxima problems when mpmath works well. I'll change this ticket to apply to all Maxima-evaluated functions.



---

archive/issue_comments_087021.json:
```json
{
    "body": "Changing component from basic arithmetic to numerical.",
    "created_at": "2013-06-14T18:32:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9263",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9263#issuecomment-87021",
    "user": "https://github.com/eviatarbach"
}
```

Changing component from basic arithmetic to numerical.



---

archive/issue_comments_087022.json:
```json
{
    "body": "Changing assignee from @aghitza to jason, jkantor.",
    "created_at": "2013-06-14T18:32:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9263",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9263#issuecomment-87022",
    "user": "https://github.com/eviatarbach"
}
```

Changing assignee from @aghitza to jason, jkantor.



---

archive/issue_comments_087023.json:
```json
{
    "body": "That is a good change.  However, we don't have that many of those left, and so probably it will have to wait until we reliably have a keyword for evaluation algorithm.",
    "created_at": "2013-06-14T18:40:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9263",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9263#issuecomment-87023",
    "user": "https://github.com/kcrisman"
}
```

That is a good change.  However, we don't have that many of those left, and so probably it will have to wait until we reliably have a keyword for evaluation algorithm.



---

archive/issue_comments_087024.json:
```json
{
    "body": "Maybe there is a way to sense whether we are passing in something other than regular precision and then ask Maxima to use a bfloat.",
    "created_at": "2013-06-14T18:41:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9263",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9263#issuecomment-87024",
    "user": "https://github.com/kcrisman"
}
```

Maybe there is a way to sense whether we are passing in something other than regular precision and then ask Maxima to use a bfloat.



---

archive/issue_comments_087025.json:
```json
{
    "body": "Do you mean #12289? What would be the problem with changing the backend before that's implemented though?\n\nActually, this ticket applies to many more functions than I thought initially. I added them to the description.\n\nI also changed it again to apply to all special functions that don't work with arbitrary precision.",
    "created_at": "2013-06-14T19:09:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9263",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9263#issuecomment-87025",
    "user": "https://github.com/eviatarbach"
}
```

Do you mean #12289? What would be the problem with changing the backend before that's implemented though?

Actually, this ticket applies to many more functions than I thought initially. I added them to the description.

I also changed it again to apply to all special functions that don't work with arbitrary precision.



---

archive/issue_comments_087026.json:
```json
{
    "body": "> Do you mean #12289? What would be the problem with changing the backend before that's implemented though?\n\nNo problem at all, I just meant that it would make more sense to switch them to mpmath first, and then worry about getting Maxima to have the right precision after that ticket.  Though I guess even spherical Bessel hasn't been implemented in mpmath yet...",
    "created_at": "2013-06-14T19:22:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9263",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9263#issuecomment-87026",
    "user": "https://github.com/kcrisman"
}
```

> Do you mean #12289? What would be the problem with changing the backend before that's implemented though?

No problem at all, I just meant that it would make more sense to switch them to mpmath first, and then worry about getting Maxima to have the right precision after that ticket.  Though I guess even spherical Bessel hasn't been implemented in mpmath yet...



---

archive/issue_events_022812.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9263",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9263#event-22812"
}
```



---

archive/issue_comments_087027.json:
```json
{
    "body": "about `hypergeometric_U`, the documentation (in Sage 5.11) says that Pari is the default, contrary to what is said in the description of this ticket. Which one is correct?\n\nPaul",
    "created_at": "2013-08-24T12:55:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9263",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9263#issuecomment-87027",
    "user": "https://github.com/zimmermann6"
}
```

about `hypergeometric_U`, the documentation (in Sage 5.11) says that Pari is the default, contrary to what is said in the description of this ticket. Which one is correct?

Paul



---

archive/issue_comments_087028.json:
```json
{
    "body": "`bessel_K` and `bessel_Y` are fixed in Sage 5.11 thanks to #4102, thus I update the description:\n\n```\nsage: n(bessel_K(1,2), prec=100)\n0.13986588181652242728459880704\nsage: n(bessel_Y(1,2), prec=100)\n-0.10703243154093754688837077228\n```\nPaul",
    "created_at": "2013-08-24T12:58:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9263",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9263#issuecomment-87028",
    "user": "https://github.com/zimmermann6"
}
```

`bessel_K` and `bessel_Y` are fixed in Sage 5.11 thanks to #4102, thus I update the description:

```
sage: n(bessel_K(1,2), prec=100)
0.13986588181652242728459880704
sage: n(bessel_Y(1,2), prec=100)
-0.10703243154093754688837077228
```
Paul



---

archive/issue_events_022813.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9263",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9263#event-22813"
}
```



---

archive/issue_events_022814.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9263",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9263#event-22814"
}
```



---

archive/issue_events_022815.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9263",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9263#event-22815"
}
```



---

archive/issue_events_022816.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9263",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9263#event-22816"
}
```



---

archive/issue_events_022817.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9263",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9263#event-22817"
}
```



---

archive/issue_events_022818.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9263",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9263#event-22818"
}
```



---

archive/issue_events_022819.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2015-05-06T09:54:48Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9263",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9263#event-22819"
}
```



---

archive/issue_events_022820.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2015-05-06T09:54:48Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9263",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9263#event-22820"
}
```



---

archive/issue_comments_087029.json:
```json
{
    "body": "Works for me.",
    "created_at": "2015-05-06T09:54:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9263",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9263#issuecomment-87029",
    "user": "https://github.com/jdemeyer"
}
```

Works for me.



---

archive/issue_comments_087030.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2015-05-06T09:54:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9263",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9263#issuecomment-87030",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_087031.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2015-05-06T09:54:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9263",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9263#issuecomment-87031",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_087032.json:
```json
{
    "body": "`hypergeometric_U` is strange, since the answer is always 53 bits:\n\n```\nsage: hypergeometric_U(1,2,3)\n0.333333333333333\nsage: R = RealField(1000)\nsage: hypergeometric_U(R(1), R(2), R(3))\n0.333333333333333\nsage: hypergeometric_U(R(1), R(2), R(3)).n(100)\n...\nTypeError: cannot approximate to a precision of 100 bits, use at most 53 bits\n```\n\nThe others work properly.",
    "created_at": "2015-05-06T10:00:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9263",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9263#issuecomment-87032",
    "user": "https://github.com/jdemeyer"
}
```

`hypergeometric_U` is strange, since the answer is always 53 bits:

```
sage: hypergeometric_U(1,2,3)
0.333333333333333
sage: R = RealField(1000)
sage: hypergeometric_U(R(1), R(2), R(3))
0.333333333333333
sage: hypergeometric_U(R(1), R(2), R(3)).n(100)
...
TypeError: cannot approximate to a precision of 100 bits, use at most 53 bits
```

The others work properly.



---

archive/issue_comments_087033.json:
```json
{
    "body": "And the issue with `hypergeometric_U` is #14896.",
    "created_at": "2015-05-06T10:06:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9263",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9263#issuecomment-87033",
    "user": "https://github.com/jdemeyer"
}
```

And the issue with `hypergeometric_U` is #14896.



---

archive/issue_comments_087034.json:
```json
{
    "body": "with Sage 6.0 I get:\n\n```\nsage: R = RealField(1000)\nsage: hypergeometric_U(R(1), R(2), R(3)).n(100)\n0.33333333333333331482961625625\nsage: hypergeometric_U(1,2,3).n(100)\n0.33333333333333331482961625625\n```\nMaybe a regression?",
    "created_at": "2015-05-06T11:49:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9263",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9263#issuecomment-87034",
    "user": "https://github.com/zimmermann6"
}
```

with Sage 6.0 I get:

```
sage: R = RealField(1000)
sage: hypergeometric_U(R(1), R(2), R(3)).n(100)
0.33333333333333331482961625625
sage: hypergeometric_U(1,2,3).n(100)
0.33333333333333331482961625625
```
Maybe a regression?



---

archive/issue_comments_087035.json:
```json
{
    "body": "is the issue with `airy_ai` fixed? I still get with Sage 6.0:\n\n```\nsage: n(airy_ai(1),digits=75)\n0.135292416312881413897883930985699407756328582763671875000000000000000000000\n```",
    "created_at": "2015-05-06T11:53:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9263",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9263#issuecomment-87035",
    "user": "https://github.com/zimmermann6"
}
```

is the issue with `airy_ai` fixed? I still get with Sage 6.0:

```
sage: n(airy_ai(1),digits=75)
0.135292416312881413897883930985699407756328582763671875000000000000000000000
```



---

archive/issue_comments_087036.json:
```json
{
    "body": "Well, Sage 6.0 is ancient.\n\nWith 6.7.beta4:\n\n```\nsage: n(airy_ai(1),digits=75)\n0.135292416312881415524147423515466306174944142988330706009102054757633534802\n```\nand\n\n```\nsage: hypergeometric_U(1,2,3).n(100)\n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n<ipython-input-4-7c7c457a86be> in <module>()\n----> 1 hypergeometric_U(Integer(1),Integer(2),Integer(3)).n(Integer(100))\n\n/usr/local/src/sage-config/src/sage/structure/element.pyx in sage.structure.element.Element.numerical_approx (build/cythonized/sage/structure/element.c:7437)()\n    744         \"\"\"\n    745         from sage.misc.functional import numerical_approx\n--> 746         return numerical_approx(self, prec=prec, digits=digits,\n    747                                 algorithm=algorithm)\n    748     n = numerical_approx\n\n/usr/local/src/sage-config/local/lib/python2.7/site-packages/sage/misc/functional.pyc in numerical_approx(x, prec, digits, algorithm)\n   1329 \n   1330     if prec > inprec:\n-> 1331         raise TypeError(\"cannot approximate to a precision of %s bits, use at most %s bits\" % (prec, inprec))\n   1332 \n   1333     # The issue is not precision, try conversion instead\n\nTypeError: cannot approximate to a precision of 100 bits, use at most 53 bits\n```",
    "created_at": "2015-05-06T12:14:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9263",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9263#issuecomment-87036",
    "user": "https://github.com/jdemeyer"
}
```

Well, Sage 6.0 is ancient.

With 6.7.beta4:

```
sage: n(airy_ai(1),digits=75)
0.135292416312881415524147423515466306174944142988330706009102054757633534802
```
and

```
sage: hypergeometric_U(1,2,3).n(100)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-4-7c7c457a86be> in <module>()
----> 1 hypergeometric_U(Integer(1),Integer(2),Integer(3)).n(Integer(100))

/usr/local/src/sage-config/src/sage/structure/element.pyx in sage.structure.element.Element.numerical_approx (build/cythonized/sage/structure/element.c:7437)()
    744         """
    745         from sage.misc.functional import numerical_approx
--> 746         return numerical_approx(self, prec=prec, digits=digits,
    747                                 algorithm=algorithm)
    748     n = numerical_approx

/usr/local/src/sage-config/local/lib/python2.7/site-packages/sage/misc/functional.pyc in numerical_approx(x, prec, digits, algorithm)
   1329 
   1330     if prec > inprec:
-> 1331         raise TypeError("cannot approximate to a precision of %s bits, use at most %s bits" % (prec, inprec))
   1332 
   1333     # The issue is not precision, try conversion instead

TypeError: cannot approximate to a precision of 100 bits, use at most 53 bits
```



---

archive/issue_comments_087037.json:
```json
{
    "body": "Note that Maxima functions we didn't usually have a good precision interface with, if that is what is going on with the hgu.",
    "created_at": "2015-05-06T15:20:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9263",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9263#issuecomment-87037",
    "user": "https://github.com/kcrisman"
}
```

Note that Maxima functions we didn't usually have a good precision interface with, if that is what is going on with the hgu.



---

archive/issue_events_022821.json:
```json
{
    "actor": "https://github.com/vbraun",
    "created_at": "2015-05-19T06:43:17Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9263",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9263#event-22821"
}
```



---

archive/issue_comments_087038.json:
```json
{
    "body": "Resolution: worksforme",
    "created_at": "2015-05-19T06:43:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9263",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9263#issuecomment-87038",
    "user": "https://github.com/vbraun"
}
```

Resolution: worksforme
