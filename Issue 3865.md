# Issue 3865: Bug in conversion from gp elements to p-adics

archive/issues_003865.json:
```json
{
    "body": "Assignee: @craigcitro\n\nDavid Loeffler ran into the following:\n\n\n```\nsage: v = gp.polrootspadic(x^2-2, 7, 20)[1]\n\nsage: R = Zp(7, 10, \"capped-rel\")\n\nsage: R(v)\n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n\n/Users/craigcitro/<ipython console> in <module>()\n\n/Users/craigcitro/three-one/local/lib/python2.5/site-packages/sage/rings/padics/padic_generic.py in __call__(self, x, absprec, relprec)\n     82             Casts x into self.  Uses the constructor of self._element_class.\n     83         \"\"\"\n---> 84         return self._element_class(self, x, absprec, relprec)\n     85 \n     86     def _coerce_impl(self, x):\n\n/Users/craigcitro/padic_capped_relative_element.pyx in sage.rings.padics.padic_capped_relative_element.pAdicCappedRelativeElement.__init__ (sage/rings/padics/padic_capped_relative_element.c:4872)()\n\n/Users/craigcitro/rational.pyx in sage.rings.rational.Rational.__init__ (sage/rings/rational.c:3767)()\n\n/Users/craigcitro/rational.pyx in sage.rings.rational.Rational.__set_value (sage/rings/rational.c:4567)()\n\n/Users/craigcitro/three-one/local/lib/python2.5/site-packages/sage/interfaces/expect.py in _rational_(self)\n   1393     def _rational_(self):\n   1394         import sage.rings.all\n-> 1395         return sage.rings.all.Rational(repr(self))\n   1396 \n   1397     def name(self, new_name=None):\n\n/Users/craigcitro/rational.pyx in sage.rings.rational.Rational.__init__ (sage/rings/rational.c:3767)()\n\n/Users/craigcitro/rational.pyx in sage.rings.rational.Rational.__set_value (sage/rings/rational.c:4533)()\n\nTypeError: unable to convert 3 + 7 + 2*7^2 + 6*7^3 + 7^4 + 2*7^5 + 7^6 + 2*7^7 + 4*7^8 + 6*7^9 + 6*7^10 + 2*7^11 + 7^12 + 7^13 + 2*7^15 + 7^16 + 7^17 + 4*7^18 + 6*7^19 + O(7^20) to a rational\n```\n\n\nThe trouble is that the code in the `__init__` method for `pAdicCappedRelativeElement`s only looks for Pari `gen` objects, not `GpElement`s. The fix should be trivial, but I'm going to look at it tomorrow.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3865\n\n",
    "created_at": "2008-08-15T02:38:07Z",
    "labels": [
        "component: interfaces",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-5.12",
    "title": "Bug in conversion from gp elements to p-adics",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3865",
    "user": "https://github.com/craigcitro"
}
```
Assignee: @craigcitro

David Loeffler ran into the following:


```
sage: v = gp.polrootspadic(x^2-2, 7, 20)[1]

sage: R = Zp(7, 10, "capped-rel")

sage: R(v)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/Users/craigcitro/<ipython console> in <module>()

/Users/craigcitro/three-one/local/lib/python2.5/site-packages/sage/rings/padics/padic_generic.py in __call__(self, x, absprec, relprec)
     82             Casts x into self.  Uses the constructor of self._element_class.
     83         """
---> 84         return self._element_class(self, x, absprec, relprec)
     85 
     86     def _coerce_impl(self, x):

/Users/craigcitro/padic_capped_relative_element.pyx in sage.rings.padics.padic_capped_relative_element.pAdicCappedRelativeElement.__init__ (sage/rings/padics/padic_capped_relative_element.c:4872)()

/Users/craigcitro/rational.pyx in sage.rings.rational.Rational.__init__ (sage/rings/rational.c:3767)()

/Users/craigcitro/rational.pyx in sage.rings.rational.Rational.__set_value (sage/rings/rational.c:4567)()

/Users/craigcitro/three-one/local/lib/python2.5/site-packages/sage/interfaces/expect.py in _rational_(self)
   1393     def _rational_(self):
   1394         import sage.rings.all
-> 1395         return sage.rings.all.Rational(repr(self))
   1396 
   1397     def name(self, new_name=None):

/Users/craigcitro/rational.pyx in sage.rings.rational.Rational.__init__ (sage/rings/rational.c:3767)()

/Users/craigcitro/rational.pyx in sage.rings.rational.Rational.__set_value (sage/rings/rational.c:4533)()

TypeError: unable to convert 3 + 7 + 2*7^2 + 6*7^3 + 7^4 + 2*7^5 + 7^6 + 2*7^7 + 4*7^8 + 6*7^9 + 6*7^10 + 2*7^11 + 7^12 + 7^13 + 2*7^15 + 7^16 + 7^17 + 4*7^18 + 6*7^19 + O(7^20) to a rational
```


The trouble is that the code in the `__init__` method for `pAdicCappedRelativeElement`s only looks for Pari `gen` objects, not `GpElement`s. The fix should be trivial, but I'm going to look at it tomorrow.

Issue created by migration from https://trac.sagemath.org/ticket/3865





---

archive/issue_comments_027491.json:
```json
{
    "body": "Tick Tick :p\n\nCheers,\n\nMichael",
    "created_at": "2008-09-29T06:26:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3865",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3865#issuecomment-27491",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Tick Tick :p

Cheers,

Michael



---

archive/issue_comments_027492.json:
```json
{
    "body": "Attachment [trac_3865.patch](tarball://root/attachments/some-uuid/ticket3865/trac_3865.patch) by @loefflerd created at 2013-07-22 19:46:43\n\nPatch against 5.11.beta3",
    "created_at": "2013-07-22T19:46:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3865",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3865#issuecomment-27492",
    "user": "https://github.com/loefflerd"
}
```

Attachment [trac_3865.patch](tarball://root/attachments/some-uuid/ticket3865/trac_3865.patch) by @loefflerd created at 2013-07-22 19:46:43

Patch against 5.11.beta3



---

archive/issue_comments_027493.json:
```json
{
    "body": "... tock. :-)",
    "created_at": "2013-07-22T19:48:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3865",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3865#issuecomment-27493",
    "user": "https://github.com/loefflerd"
}
```

... tock. :-)



---

archive/issue_comments_027494.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2013-07-22T19:48:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3865",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3865#issuecomment-27494",
    "user": "https://github.com/loefflerd"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_027495.json:
```json
{
    "body": "Changing keywords from \"\" to \"sd51\".",
    "created_at": "2013-07-23T12:01:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3865",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3865#issuecomment-27495",
    "user": "https://github.com/loefflerd"
}
```

Changing keywords from "" to "sd51".



---

archive/issue_comments_027496.json:
```json
{
    "body": "looks good and works!",
    "created_at": "2013-07-23T15:01:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3865",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3865#issuecomment-27496",
    "user": "https://trac.sagemath.org/admin/accounts/users/jantuitman"
}
```

looks good and works!



---

archive/issue_comments_027497.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2013-07-23T15:01:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3865",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3865#issuecomment-27497",
    "user": "https://trac.sagemath.org/admin/accounts/users/jantuitman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_027498.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2013-08-16T21:17:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3865",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3865#issuecomment-27498",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed
