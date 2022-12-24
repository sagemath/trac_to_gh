# Issue 8291: eisenstein_series_qexp ridiculously bad  over finite fields

archive/issues_008291.json:
```json
{
    "body": "Assignee: craigcitro\n\nCC:  mraum davidloeffler\n\nI was the one who made Eisenstein series \"work\" over arbitrary fields.  It turns out that I didn't do a very good job, and you don't have to go very far to break it:\n\n\n```\nsage: eisenstein_series_qexp(26, 10, GF(13))\n---------------------------------------------------------------------------\nOverflowError                             Traceback (most recent call last)\n\n/opt/sage-4.3.2/devel/sage-main/sage/modular/modform/<ipython console> in <module>()\n\n/home/ghitza/sage-devel/local/lib/python2.6/site-packages/sage/modular/modform/eis_series.pyc in eisenstein_series_qexp(k, prec, K, var, integral)\n    105     val[0] = a0\n    106     R = K[[var]]\n--> 107     return R(val, prec=prec, check=False)\n    108 \n    109 ######################################################################\n\n/home/ghitza/sage-devel/local/lib/python2.6/site-packages/sage/rings/power_series_ring.pyc in __call__(self, f, prec, check)\n    408             v = sage_eval(f.Eltseq())\n    409             return self(v) * (self.gen(0)**f.Valuation())\n--> 410         return self.__power_series_class(self, f, prec, check=check)\n    411         \n    412     def construction(self):\n\n/home/ghitza/sage-devel/local/lib/python2.6/site-packages/sage/rings/power_series_poly.so in sage.rings.power_series_poly.PowerSeries_poly.__init__ (sage/rings/power_series_poly.c:2373)()\n\n/home/ghitza/sage-devel/local/lib/python2.6/site-packages/sage/structure/parent.so in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:6228)()\n\n/home/ghitza/sage-devel/local/lib/python2.6/site-packages/sage/structure/coerce_maps.so in sage.structure.coerce_maps.DefaultConvertMap_unique._call_with_args (sage/structure/coerce_maps.c:3532)()\n\n/home/ghitza/sage-devel/local/lib/python2.6/site-packages/sage/structure/coerce_maps.so in sage.structure.coerce_maps.DefaultConvertMap_unique._call_with_args (sage/structure/coerce_maps.c:3353)()\n\n/home/ghitza/sage-devel/local/lib/python2.6/site-packages/sage/rings/polynomial/polynomial_ring.pyc in _element_constructor_(self, x, check, is_gen, construct, **kwds)\n    310                 x = x.Polrev()\n    311 \n--> 312         return C(self, x, check, is_gen, construct=construct, **kwds)\n    313 \n    314     def is_integral_domain(self, proof = True):\n\n/home/ghitza/sage-devel/local/lib/python2.6/site-packages/sage/rings/polynomial/polynomial_zmod_flint.so in sage.rings.polynomial.polynomial_zmod_flint.Polynomial_zmod_flint.__init__ (sage/rings/polynomial/polynomial_zmod_flint.c:10916)()\n\n/home/ghitza/sage-devel/local/lib/python2.6/site-packages/sage/rings/polynomial/polynomial_zmod_flint.so in sage.rings.polynomial.polynomial_zmod_flint.Polynomial_zmod_flint._set_list (sage/rings/polynomial/polynomial_zmod_flint.c:11368)()\n\nOverflowError: long int too large to convert\n```\n\n\nA side note: the workaround at the end of the method is not necessary any more, and can be removed.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8291\n\n",
    "created_at": "2010-02-17T03:00:31Z",
    "labels": [
        "modular forms",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6.1",
    "title": "eisenstein_series_qexp ridiculously bad  over finite fields",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8291",
    "user": "AlexGhitza"
}
```
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
    106     R = K[[var]]
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


Issue created by migration from https://trac.sagemath.org/ticket/8291





---

archive/issue_comments_073459.json:
```json
{
    "body": "This bug appears to be gone in sage-4.6.  I'm not sure at what point it was fixed, but it was most likely when Martin Raum or David Loeffler touched the code recently.\n\nIn any case, I am attaching a mini-patch with a doctest that verifies that it is fixed.",
    "created_at": "2010-11-05T08:13:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8291",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8291#issuecomment-73459",
    "user": "AlexGhitza"
}
```

This bug appears to be gone in sage-4.6.  I'm not sure at what point it was fixed, but it was most likely when Martin Raum or David Loeffler touched the code recently.

In any case, I am attaching a mini-patch with a doctest that verifies that it is fixed.



---

archive/issue_comments_073460.json:
```json
{
    "body": "Attachment [trac_8291.patch](tarball://root/attachments/some-uuid/ticket8291/trac_8291.patch) by AlexGhitza created at 2010-11-05 08:14:12",
    "created_at": "2010-11-05T08:14:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8291",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8291#issuecomment-73460",
    "user": "AlexGhitza"
}
```

Attachment [trac_8291.patch](tarball://root/attachments/some-uuid/ticket8291/trac_8291.patch) by AlexGhitza created at 2010-11-05 08:14:12



---

archive/issue_comments_073461.json:
```json
{
    "body": "cc-ing Martin and David in case they have more info about this.",
    "created_at": "2010-11-05T08:15:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8291",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8291#issuecomment-73461",
    "user": "AlexGhitza"
}
```

cc-ing Martin and David in case they have more info about this.



---

archive/issue_comments_073462.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-11-05T08:15:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8291",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8291#issuecomment-73462",
    "user": "AlexGhitza"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_073463.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-11-05T15:47:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8291",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8291#issuecomment-73463",
    "user": "mraum"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_073464.json:
```json
{
    "body": "This has been indeed fixed by David from what I see in googlecodes, and he also added the doctest right before yours. It's a good a idea to introduce another explicit test and it won't cost much time. So this gets a positive review.",
    "created_at": "2010-11-05T15:47:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8291",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8291#issuecomment-73464",
    "user": "mraum"
}
```

This has been indeed fixed by David from what I see in googlecodes, and he also added the doctest right before yours. It's a good a idea to introduce another explicit test and it won't cost much time. So this gets a positive review.



---

archive/issue_comments_073465.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-11-10T22:19:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8291",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8291#issuecomment-73465",
    "user": "jdemeyer"
}
```

Resolution: fixed
