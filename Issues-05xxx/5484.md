# Issue 5484: improve quotients of univariate polynomial rings

archive/issues_005484.json:
```json
{
    "body": "Assignee: @malb\n\nCC:  jpflori\n\nRoi Docampo and I noticed the following at Sage Days 14.\n\nThis works:\n\n```\nsage: R.<x,y> = ZZ[]\nsage: R.quo(R.ideal(2))\nQuotient of Multivariate Polynomial Ring in x, y over Integer Ring by the ideal (2)\n```\n\nBut this doesn't:\n\n```\nsage: R.<x> = ZZ[]\nsage: R.quo(R.ideal(2))\n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n\n/home/aghitza/.sage/temp/cartan/12118/_home_aghitza__sage_init_sage_0.py in <module>()\n\n/opt/sage/local/lib/python2.5/site-packages/sage/rings/ring.so in sage.rings.ring.CommutativeRing.quo (sage/rings/ring.c:5717)()\n\n/opt/sage/local/lib/python2.5/site-packages/sage/rings/ring.so in sage.rings.ring.CommutativeRing.quotient (sage/rings/ring.c:5624)()\n\n/opt/sage/local/lib/python2.5/site-packages/sage/rings/quotient_ring.pyc in QuotientRing(R, I, names)\n    120     try:\n    121         if I.is_principal():\n--> 122             return R.quotient_by_principal_ideal(I.gen(), names)\n    123     except (AttributeError, NotImplementedError):\n    124         pass\n\n/opt/sage/local/lib/python2.5/site-packages/sage/rings/polynomial/polynomial_ring.pyc in quotient_by_principal_ideal(self, f, names)\n   1004         \"\"\"\n   1005         import sage.rings.polynomial.polynomial_quotient_ring\n-> 1006         return sage.rings.polynomial.polynomial_quotient_ring.PolynomialQuotientRing(self, f, names)\n   1007     \n   1008 \n\n/opt/sage/local/lib/python2.5/site-packages/sage/rings/polynomial/polynomial_quotient_ring.pyc in PolynomialQuotientRing(ring, polynomial, names)\n    133     c = polynomial.leading_coefficient()\n    134     if not c.is_unit():\n--> 135         raise TypeError, \"polynomial must have unit leading coefficient\"\n    136     R = ring.base_ring()\n    137     if isinstance(R, sage.rings.integral_domain.IntegralDomain):\n\nTypeError: polynomial must have unit leading coefficient\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5484\n\n",
    "created_at": "2009-03-11T08:16:23Z",
    "labels": [
        "component: commutative algebra"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.8",
    "title": "improve quotients of univariate polynomial rings",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5484",
    "user": "https://github.com/aghitza"
}
```
Assignee: @malb

CC:  jpflori

Roi Docampo and I noticed the following at Sage Days 14.

This works:

```
sage: R.<x,y> = ZZ[]
sage: R.quo(R.ideal(2))
Quotient of Multivariate Polynomial Ring in x, y over Integer Ring by the ideal (2)
```

But this doesn't:

```
sage: R.<x> = ZZ[]
sage: R.quo(R.ideal(2))
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/aghitza/.sage/temp/cartan/12118/_home_aghitza__sage_init_sage_0.py in <module>()

/opt/sage/local/lib/python2.5/site-packages/sage/rings/ring.so in sage.rings.ring.CommutativeRing.quo (sage/rings/ring.c:5717)()

/opt/sage/local/lib/python2.5/site-packages/sage/rings/ring.so in sage.rings.ring.CommutativeRing.quotient (sage/rings/ring.c:5624)()

/opt/sage/local/lib/python2.5/site-packages/sage/rings/quotient_ring.pyc in QuotientRing(R, I, names)
    120     try:
    121         if I.is_principal():
--> 122             return R.quotient_by_principal_ideal(I.gen(), names)
    123     except (AttributeError, NotImplementedError):
    124         pass

/opt/sage/local/lib/python2.5/site-packages/sage/rings/polynomial/polynomial_ring.pyc in quotient_by_principal_ideal(self, f, names)
   1004         """
   1005         import sage.rings.polynomial.polynomial_quotient_ring
-> 1006         return sage.rings.polynomial.polynomial_quotient_ring.PolynomialQuotientRing(self, f, names)
   1007     
   1008 

/opt/sage/local/lib/python2.5/site-packages/sage/rings/polynomial/polynomial_quotient_ring.pyc in PolynomialQuotientRing(ring, polynomial, names)
    133     c = polynomial.leading_coefficient()
    134     if not c.is_unit():
--> 135         raise TypeError, "polynomial must have unit leading coefficient"
    136     R = ring.base_ring()
    137     if isinstance(R, sage.rings.integral_domain.IntegralDomain):

TypeError: polynomial must have unit leading coefficient
```


Issue created by migration from https://trac.sagemath.org/ticket/5484





---

archive/issue_comments_042473.json:
```json
{
    "body": "Changing component from algebraic geometry to commutative algebra.",
    "created_at": "2009-03-11T08:26:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5484",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5484#issuecomment-42473",
    "user": "https://github.com/aghitza"
}
```

Changing component from algebraic geometry to commutative algebra.



---

archive/issue_comments_042474.json:
```json
{
    "body": "Changing assignee from @williamstein to @malb.",
    "created_at": "2009-03-11T08:26:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5484",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5484#issuecomment-42474",
    "user": "https://github.com/aghitza"
}
```

Changing assignee from @williamstein to @malb.



---

archive/issue_events_012814.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5484",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5484#event-12814"
}
```



---

archive/issue_events_012815.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5484",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5484#event-12815"
}
```



---

archive/issue_events_012816.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5484",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5484#event-12816"
}
```



---

archive/issue_events_012817.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5484",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5484#event-12817"
}
```



---

archive/issue_events_012818.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5484",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5484#event-12818"
}
```



---

archive/issue_events_012819.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5484",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5484#event-12819"
}
```



---

archive/issue_events_012820.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5484",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5484#event-12820"
}
```



---

archive/issue_comments_042475.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2015-04-22T15:21:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5484",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5484#issuecomment-42475",
    "user": "https://github.com/bgrenet"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_042476.json:
```json
{
    "body": "I made the following proposition:\n\nSuppose that `R = PolynomialRing(S,'x')` for some ring `S`, and `f` is a polynomial over `S`. \n* Keep the same thing if `f` has degree `> 0` or `f` is a unit, that is return `PolynomialQuotientRing(S, f, 'x')`;\n* Return `PolynomialRing(S.quo(f), 'x')` when `f` is a non-unit constant.\n\nIn particular:\n\n```\nsage: R = ZZ['x']\nsage: R.quo(2)\nUnivariate Polynomial Ring in x over Ring of integers modulo 2 (using NTL)\n```\n\nDoes this make sense?\n\n---\nNew commits:",
    "created_at": "2015-04-22T15:21:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5484",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5484#issuecomment-42476",
    "user": "https://github.com/bgrenet"
}
```

I made the following proposition:

Suppose that `R = PolynomialRing(S,'x')` for some ring `S`, and `f` is a polynomial over `S`. 
* Keep the same thing if `f` has degree `> 0` or `f` is a unit, that is return `PolynomialQuotientRing(S, f, 'x')`;
* Return `PolynomialRing(S.quo(f), 'x')` when `f` is a non-unit constant.

In particular:

```
sage: R = ZZ['x']
sage: R.quo(2)
Univariate Polynomial Ring in x over Ring of integers modulo 2 (using NTL)
```

Does this make sense?

---
New commits:



---

archive/issue_comments_042477.json:
```json
{
    "body": "doc does not build, see patchbot report\n\nyou wrongly replaced a TEST: by TEST::",
    "created_at": "2015-06-01T07:52:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5484",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5484#issuecomment-42477",
    "user": "https://github.com/fchapoton"
}
```

doc does not build, see patchbot report

you wrongly replaced a TEST: by TEST::



---

archive/issue_comments_042478.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2015-06-01T07:52:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5484",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5484#issuecomment-42478",
    "user": "https://github.com/fchapoton"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_events_012821.json:
```json
{
    "actor": "https://github.com/fchapoton",
    "created_at": "2015-06-01T07:52:18Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5484",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5484#event-12821"
}
```



---

archive/issue_events_012822.json:
```json
{
    "actor": "https://github.com/fchapoton",
    "created_at": "2015-06-01T07:52:18Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5484",
    "milestone": "sage-6.8",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5484#event-12822"
}
```



---

archive/issue_comments_042479.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2015-06-01T08:51:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5484",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5484#issuecomment-42479",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_042480.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2015-06-01T08:52:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5484",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5484#issuecomment-42480",
    "user": "https://github.com/bgrenet"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_042481.json:
```json
{
    "body": "Replying to [comment:9 chapoton]:\n> doc does not build, see patchbot report\n> \n> you wrongly replaced a TEST: by TEST::\n\n\nShould work now. Sorry for the same mistake on two distinct tickets ;-)",
    "created_at": "2015-06-01T08:52:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5484",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5484#issuecomment-42481",
    "user": "https://github.com/bgrenet"
}
```

Replying to [comment:9 chapoton]:
> doc does not build, see patchbot report
> 
> you wrongly replaced a TEST: by TEST::


Should work now. Sorry for the same mistake on two distinct tickets ;-)



---

archive/issue_comments_042482.json:
```json
{
    "body": "Sorry, but the new quotient rings don't play well with the quotient ring interface (or what could be reasonably expected to be the quotient ring interface):\n\n```\nsage: R = ZZ['x']\nsage: x = R.gen()\nsage: J = R.ideal(2)\nsage: T = R.quotient_by_principal_ideal(J)\nsage: T(x)\nx\nsage: T.lift(_)\n---------------------------------------------------------------------------\nAttributeError                            Traceback (most recent call last)\n<ipython-input-30-260465055124> in <module>()\n----> 1 T.lift(_)\n\n/home/skraeling/sage/src/sage/structure/parent.pyx in sage.structure.parent.Parent.__getattr__ (build/cythonized/sage/structure/parent.c:7885)()\n    839             return self.__cached_methods[name]\n    840         except KeyError:\n--> 841             attr = getattr_from_other_class(self, self._category.parent_class, name)\n    842             self.__cached_methods[name] = attr\n    843             return attr\n\n/home/skraeling/sage/src/sage/structure/misc.pyx in sage.structure.misc.getattr_from_other_class (build/cythonized/sage/structure/misc.c:1582)()\n    251         dummy_error_message.cls = type(self)\n    252         dummy_error_message.name = name\n--> 253         raise dummy_attribute_error\n    254     try:\n    255         attribute = getattr(cls, name)\n\nAttributeError: 'PolynomialRing_dense_mod_p_with_category' object has no attribute 'lift'\n```",
    "created_at": "2015-06-06T22:04:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5484",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5484#issuecomment-42482",
    "user": "https://github.com/darijgr"
}
```

Sorry, but the new quotient rings don't play well with the quotient ring interface (or what could be reasonably expected to be the quotient ring interface):

```
sage: R = ZZ['x']
sage: x = R.gen()
sage: J = R.ideal(2)
sage: T = R.quotient_by_principal_ideal(J)
sage: T(x)
x
sage: T.lift(_)
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-30-260465055124> in <module>()
----> 1 T.lift(_)

/home/skraeling/sage/src/sage/structure/parent.pyx in sage.structure.parent.Parent.__getattr__ (build/cythonized/sage/structure/parent.c:7885)()
    839             return self.__cached_methods[name]
    840         except KeyError:
--> 841             attr = getattr_from_other_class(self, self._category.parent_class, name)
    842             self.__cached_methods[name] = attr
    843             return attr

/home/skraeling/sage/src/sage/structure/misc.pyx in sage.structure.misc.getattr_from_other_class (build/cythonized/sage/structure/misc.c:1582)()
    251         dummy_error_message.cls = type(self)
    252         dummy_error_message.name = name
--> 253         raise dummy_attribute_error
    254     try:
    255         attribute = getattr(cls, name)

AttributeError: 'PolynomialRing_dense_mod_p_with_category' object has no attribute 'lift'
```



---

archive/issue_comments_042483.json:
```json
{
    "body": "Replying to [comment:12 darij]:\n> Sorry, but the new quotient rings don't play well with the quotient ring interface (or what could be reasonably expected to be the quotient ring interface):\n\n\nWhat do you suggest? I can imagine three solutions:\n* Make `R.quotient_by_principal_ideal(R.ideal(2))` return a `Polynomial_quotient_ring`: I doubt this is in principle impossible, but at least it requires quite a lot of changes. \n* Keep `R.quotient_by_principal_ideal(R.ideal(2))` return a `TypeError`\n* Implement a `lift` method for `PolynomialRing_dense_mod_p`.\n\nNone of the three solutions is really fine to my mind, so feel free to suggest another one!",
    "created_at": "2015-06-08T09:20:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5484",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5484#issuecomment-42483",
    "user": "https://github.com/bgrenet"
}
```

Replying to [comment:12 darij]:
> Sorry, but the new quotient rings don't play well with the quotient ring interface (or what could be reasonably expected to be the quotient ring interface):


What do you suggest? I can imagine three solutions:
* Make `R.quotient_by_principal_ideal(R.ideal(2))` return a `Polynomial_quotient_ring`: I doubt this is in principle impossible, but at least it requires quite a lot of changes. 
* Keep `R.quotient_by_principal_ideal(R.ideal(2))` return a `TypeError`
* Implement a `lift` method for `PolynomialRing_dense_mod_p`.

None of the three solutions is really fine to my mind, so feel free to suggest another one!



---

archive/issue_comments_042484.json:
```json
{
    "body": "I fear I cannot help here. If you ask me, the whole system is broken. Methods like \"quotient\" should not return rings but quotient homomorphisms, and these homomorphisms (not their images) should have `lift` attributes...",
    "created_at": "2015-06-08T09:54:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5484",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5484#issuecomment-42484",
    "user": "https://github.com/darijgr"
}
```

I fear I cannot help here. If you ask me, the whole system is broken. Methods like "quotient" should not return rings but quotient homomorphisms, and these homomorphisms (not their images) should have `lift` attributes...



---

archive/issue_comments_042485.json:
```json
{
    "body": "I agree that the system is broken. However, I think that the proposed change improves the situation. I think what we should do here is add a comment stating what the previous comment says. After that I think it would be good to go. What do you think?",
    "created_at": "2016-05-04T16:25:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5484",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5484#issuecomment-42485",
    "user": "https://github.com/saraedum"
}
```

I agree that the system is broken. However, I think that the proposed change improves the situation. I think what we should do here is add a comment stating what the previous comment says. After that I think it would be good to go. What do you think?



---

archive/issue_comments_042486.json:
```json
{
    "body": "Changing status from needs_review to needs_info.",
    "created_at": "2016-05-04T16:25:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5484",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5484#issuecomment-42486",
    "user": "https://github.com/saraedum"
}
```

Changing status from needs_review to needs_info.
