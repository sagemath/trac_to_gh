# Issue 5076: bug with (coercion in?) p-adic extension fields

archive/issues_005076.json:
```json
{
    "body": "Assignee: was\n\nSage gets confused when coercing things to a p-adic extension: i.e., this doesn't work:\n\n```\nsage: K = Qp(11,8)\nsage: b = -2\nsage: S.<x> = QQ['x']\nsage: J.<a> = K.extension((x+b)**11-b)\nsage: J(11^-1+O(11))\n---------------------------------------------------------------------------\nValueError                                Traceback (most recent call last)\n\n/home/jen/<ipython console> in <module>()\n\n/usr/local/sage/local/lib/python2.5/site-packages/sage/rings/padics/padic_generic.pyc in __call__(self, x, absprec, relprec)\n     82             Casts x into self.  Uses the constructor of self._element_class.\n     83         \"\"\"\n---> 84         return self._element_class(self, x, absprec, relprec)\n     85 \n     86     def _coerce_impl(self, x):\n\n/usr/local/sage/local/lib/python2.5/site-packages/sage/rings/padics/padic_ZZ_pX_CR_element.so in sage.rings.padics.padic_ZZ_pX_CR_element.pAdicZZpXCRElement.__init__ (sage/rings/padics/padic_ZZ_pX_CR_element.cpp:3550)()\n\n/usr/local/sage/local/lib/python2.5/site-packages/sage/rings/padics/padic_capped_relative_element.so in sage.rings.padics.padic_capped_relative_element.pAdicCappedRelativeElement._set_to_mpz (sage/rings/padics/padic_capped_relative_element.c:6980)()\n\nValueError: negative valuation\n```\n\nHowever, this does:\n\n```\nsage: J(11^-1)\n10*a^-11 + 10*a^-10 + 8*a^-9 + 10*a^-8 + a^-7 + 7*a^-6 + 2*a^-5 + 4*a^-4 + 10*a^-3 + 2*a^-2 + 2*a^-1 + 6 + 3*a^2 + 9*a^5 + 5*a^6 + 2*a^7 + 8*a^8 + 5*a^9 + 2*a^10 + 2*a^11 + 7*a^12 + a^13 + 8*a^14 + 4*a^16 + 4*a^17 + 4*a^18 + 6*a^19 + 5*a^20 + 4*a^21 + 7*a^22 + 7*a^23 + 3*a^24 + 6*a^25 + 5*a^26 + 10*a^27 + 9*a^28 + 8*a^30 + 6*a^31 + a^32 + 6*a^33 + 6*a^34 + 4*a^35 + 8*a^36 + 10*a^38 + 8*a^39 + 4*a^40 + 7*a^41 + 2*a^42 + 5*a^44 + 5*a^45 + 5*a^46 + 4*a^47 + 5*a^48 + 3*a^49 + 3*a^50 + a^52 + 7*a^53 + 9*a^54 + 5*a^55 + 5*a^56 + 3*a^57 + 8*a^58 + 7*a^60 + 8*a^61 + 8*a^62 + 5*a^63 + 2*a^64 + 9*a^66 + 3*a^67 + 10*a^68 + 4*a^69 + 5*a^71 + 4*a^72 + 3*a^73 + 3*a^74 + 4*a^75 + 6*a^76 + O(a^77)\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5076\n\n",
    "created_at": "2009-01-23T21:24:55Z",
    "labels": [
        "number theory",
        "major",
        "bug"
    ],
    "title": "bug with (coercion in?) p-adic extension fields",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5076",
    "user": "jen"
}
```
Assignee: was

Sage gets confused when coercing things to a p-adic extension: i.e., this doesn't work:

```
sage: K = Qp(11,8)
sage: b = -2
sage: S.<x> = QQ['x']
sage: J.<a> = K.extension((x+b)**11-b)
sage: J(11^-1+O(11))
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)

/home/jen/<ipython console> in <module>()

/usr/local/sage/local/lib/python2.5/site-packages/sage/rings/padics/padic_generic.pyc in __call__(self, x, absprec, relprec)
     82             Casts x into self.  Uses the constructor of self._element_class.
     83         """
---> 84         return self._element_class(self, x, absprec, relprec)
     85 
     86     def _coerce_impl(self, x):

/usr/local/sage/local/lib/python2.5/site-packages/sage/rings/padics/padic_ZZ_pX_CR_element.so in sage.rings.padics.padic_ZZ_pX_CR_element.pAdicZZpXCRElement.__init__ (sage/rings/padics/padic_ZZ_pX_CR_element.cpp:3550)()

/usr/local/sage/local/lib/python2.5/site-packages/sage/rings/padics/padic_capped_relative_element.so in sage.rings.padics.padic_capped_relative_element.pAdicCappedRelativeElement._set_to_mpz (sage/rings/padics/padic_capped_relative_element.c:6980)()

ValueError: negative valuation
```

However, this does:

```
sage: J(11^-1)
10*a^-11 + 10*a^-10 + 8*a^-9 + 10*a^-8 + a^-7 + 7*a^-6 + 2*a^-5 + 4*a^-4 + 10*a^-3 + 2*a^-2 + 2*a^-1 + 6 + 3*a^2 + 9*a^5 + 5*a^6 + 2*a^7 + 8*a^8 + 5*a^9 + 2*a^10 + 2*a^11 + 7*a^12 + a^13 + 8*a^14 + 4*a^16 + 4*a^17 + 4*a^18 + 6*a^19 + 5*a^20 + 4*a^21 + 7*a^22 + 7*a^23 + 3*a^24 + 6*a^25 + 5*a^26 + 10*a^27 + 9*a^28 + 8*a^30 + 6*a^31 + a^32 + 6*a^33 + 6*a^34 + 4*a^35 + 8*a^36 + 10*a^38 + 8*a^39 + 4*a^40 + 7*a^41 + 2*a^42 + 5*a^44 + 5*a^45 + 5*a^46 + 4*a^47 + 5*a^48 + 3*a^49 + 3*a^50 + a^52 + 7*a^53 + 9*a^54 + 5*a^55 + 5*a^56 + 3*a^57 + 8*a^58 + 7*a^60 + 8*a^61 + 8*a^62 + 5*a^63 + 2*a^64 + 9*a^66 + 3*a^67 + 10*a^68 + 4*a^69 + 5*a^71 + 4*a^72 + 3*a^73 + 3*a^74 + 4*a^75 + 6*a^76 + O(a^77)
```


Issue created by migration from https://trac.sagemath.org/ticket/5076





---

archive/issue_comments_038656.json:
```json
{
    "body": "Changing assignee from was to roed.",
    "created_at": "2009-01-24T18:24:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5076",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5076#issuecomment-38656",
    "user": "jen"
}
```

Changing assignee from was to roed.



---

archive/issue_comments_038657.json:
```json
{
    "body": "something else that might be related:\n\n```\nsage: K = Qp(11,8)\nsage: a = 11^-2 + O(11^5)\nsage: a\n11^-2 + O(11^3)\n```\n",
    "created_at": "2009-01-24T18:24:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5076",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5076#issuecomment-38657",
    "user": "jen"
}
```

something else that might be related:

```
sage: K = Qp(11,8)
sage: a = 11^-2 + O(11^5)
sage: a
11^-2 + O(11^3)
```




---

archive/issue_comments_038658.json:
```json
{
    "body": "I think this second thing is a separate issue. I created ticket #5499 to address it.",
    "created_at": "2009-03-12T05:19:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5076",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5076#issuecomment-38658",
    "user": "kedlaya"
}
```

I think this second thing is a separate issue. I created ticket #5499 to address it.



---

archive/issue_comments_038659.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-03-17T05:31:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5076",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5076#issuecomment-38659",
    "user": "roed"
}
```

Attachment



---

archive/issue_comments_038660.json:
```json
{
    "body": "This looks fine in itself, but the new doctests won't pass until #5499 is resolved.",
    "created_at": "2009-04-12T12:14:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5076",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5076#issuecomment-38660",
    "user": "kedlaya"
}
```

This looks fine in itself, but the new doctests won't pass until #5499 is resolved.



---

archive/issue_comments_038661.json:
```json
{
    "body": "The fix here is now part of #5778.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-25T09:29:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5076",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5076#issuecomment-38661",
    "user": "mabshoff"
}
```

The fix here is now part of #5778.

Cheers,

Michael



---

archive/issue_comments_038662.json:
```json
{
    "body": "Changing component from number theory to padics.",
    "created_at": "2009-04-26T19:56:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5076",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5076#issuecomment-38662",
    "user": "mabshoff"
}
```

Changing component from number theory to padics.



---

archive/issue_comments_038663.json:
```json
{
    "body": "Fixed in Sage 4.0.alpha0 via #5778.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-20T20:14:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5076",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5076#issuecomment-38663",
    "user": "mabshoff"
}
```

Fixed in Sage 4.0.alpha0 via #5778.

Cheers,

Michael



---

archive/issue_comments_038664.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-05-20T20:14:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5076",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5076#issuecomment-38664",
    "user": "mabshoff"
}
```

Resolution: fixed
