# Issue 2952: LaurentPolynomialRing coercion error

archive/issues_002952.json:
```json
{
    "body": "Assignee: @roed314\n\nCurrently\n\n```\nsage: R.<q>=QQ[]\nsage: L.<x,y,z> = LaurentPolynomialRing(R)\nsage: f=(x+y+z^-1)^2\nsage: f.substitute(z=1)\n```\ngives an error because it PolynomialRing isn't imported categories/pushout.py for the Laurent functor.\n\nOnce, that it is fixed, the above commands give a coercion error between the fraction field of QQ['q'] and the Laurent polynomial ring over QQ['q']\n\nIssue created by migration from https://trac.sagemath.org/ticket/2952\n\n",
    "created_at": "2008-04-18T21:04:57Z",
    "labels": [
        "component: coercion",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.3",
    "title": "LaurentPolynomialRing coercion error",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2952",
    "user": "https://github.com/mwhansen"
}
```
Assignee: @roed314

Currently

```
sage: R.<q>=QQ[]
sage: L.<x,y,z> = LaurentPolynomialRing(R)
sage: f=(x+y+z^-1)^2
sage: f.substitute(z=1)
```
gives an error because it PolynomialRing isn't imported categories/pushout.py for the Laurent functor.

Once, that it is fixed, the above commands give a coercion error between the fraction field of QQ['q'] and the Laurent polynomial ring over QQ['q']

Issue created by migration from https://trac.sagemath.org/ticket/2952





---

archive/issue_events_006743.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2008-04-21T02:34:54Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2952",
    "milestone": "sage-3.0.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2952#event-6743"
}
```



---

archive/issue_comments_020310.json:
```json
{
    "body": "Attachment [2952.2.patch](tarball://root/attachments/some-uuid/ticket2952/2952.2.patch) by @roed314 created at 2008-04-21 10:27:10",
    "created_at": "2008-04-21T10:27:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2952",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2952#issuecomment-20310",
    "user": "https://github.com/roed314"
}
```

Attachment [2952.2.patch](tarball://root/attachments/some-uuid/ticket2952/2952.2.patch) by @roed314 created at 2008-04-21 10:27:10



---

archive/issue_comments_020311.json:
```json
{
    "body": "The patch doesn't work.  We'll wait on this until the new coercion framework goes in.",
    "created_at": "2008-04-26T01:51:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2952",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2952#issuecomment-20311",
    "user": "https://github.com/mwhansen"
}
```

The patch doesn't work.  We'll wait on this until the new coercion framework goes in.



---

archive/issue_comments_020312.json:
```json
{
    "body": "This is still broken and the new coercion framework has been merged:\n\n```\n----------------------------------------------------------------------\n| SAGE Version 3.1.2.rc2, Release Date: 2008-09-12                   |\n| Type notebook() for the GUI, and license() for information.        |\nsage: R.<q>=QQ[]\nsage: L.<x,y,z> = LaurentPolynomialRing(R)\nsage: \nsage: f=(x+y+z^-1)^2\nsage: f.substitute(z=1)\n---------------------------------------------------------------------------\nNameError                                 Traceback (most recent call last)\n\n/scratch/mabshoff/release-cycle/sage-3.1.2.rc3/<ipython console> in <module>()\n\n/scratch/mabshoff/release-cycle/sage-3.1.2.rc3/element.pyx in sage.structure.element.Element.substitute (sage/structure/element.c:3756)()\n\n/scratch/mabshoff/release-cycle/sage-3.1.2.rc3/laurent_polynomial.pyx in sage.rings.polynomial.laurent_polynomial.LaurentPolynomial_mpair.subs (sage/rings/polynomial/laurent_polynomial.c:6666)()\n\n/scratch/mabshoff/release-cycle/sage-3.1.2.rc3/element.pyx in sage.structure.element.RingElement.__imul__ (sage/structure/element.c:9590)()\n\n/scratch/mabshoff/release-cycle/sage-3.1.2.rc3/coerce.pyx in sage.structure.coerce.CoercionModel_cache_maps.bin_op (sage/structure/coerce.c:6008)()\n\n/scratch/mabshoff/release-cycle/sage-3.1.2.rc3/coerce.pyx in sage.structure.coerce.CoercionModel_cache_maps.get_action (sage/structure/coerce.c:9310)()\n\n/scratch/mabshoff/release-cycle/sage-3.1.2.rc3/coerce.pyx in sage.structure.coerce.CoercionModel_cache_maps.discover_action (sage/structure/coerce.c:10441)()\n\n/scratch/mabshoff/release-cycle/sage-3.1.2.rc3/coerce.pyx in sage.structure.coerce.CoercionModel_cache_maps.discover_action (sage/structure/coerce.c:10088)()\n\n/scratch/mabshoff/release-cycle/sage-3.1.2.rc3/parent.pyx in sage.structure.parent.Parent.get_action (sage/structure/parent.c:8569)()\n\n/scratch/mabshoff/release-cycle/sage-3.1.2.rc3/parent_old.pyx in sage.structure.parent_old.Parent._get_action_ (sage/structure/parent_old.c:5963)()\n\n/scratch/mabshoff/release-cycle/sage-3.1.2.rc3/parent_old.pyx in sage.structure.parent_old.Parent.get_action_c (sage/structure/parent_old.c:2264)()\n\n/scratch/mabshoff/release-cycle/sage-3.1.2.rc3/parent_old.pyx in sage.structure.parent_old.Parent.get_action_impl (sage/structure/parent_old.c:2481)()\n\n/scratch/mabshoff/release-cycle/sage-3.1.2.rc3/parent_old.pyx in sage.structure.parent_old.Parent.get_action_c_impl (sage/structure/parent_old.c:3341)()\n\n/scratch/mabshoff/release-cycle/sage-3.1.2.rc3/coerce_actions.pyx in sage.structure.coerce_actions.ModuleAction.__init__ (sage/structure/coerce_actions.c:3706)()\n\n/scratch/mabshoff/release-cycle/sage-3.1.2.rc3/local/lib/python2.5/site-packages/sage/categories/pushout.py in pushout(R, S)\n    437         if len(Sc) == 0:\n    438             c = Rc.pop()\n--> 439             Z = c(Z)\n    440         elif len(Rc) == 0:\n    441             c = Sc.pop()\n\n/scratch/mabshoff/release-cycle/sage-3.1.2.rc3/local/lib/python2.5/site-packages/sage/categories/pushout.py in __call__(self, R)\n    136             return LaurentPolynomialRing(R.base_ring(), (list(R.variable_names()) + [self.var]))\n    137         else:\n--> 138             return PolynomialRing(R, self.var)\n    139     def __cmp__(self, other):\n    140         c = cmp(type(self), type(other))\n\nNameError: global name 'PolynomialRing' is not defined\nsage: \n```\nIt seems that David's patch is not the right solution, so can someone come up with a better patch?\n\nCheers,\n\nMichael",
    "created_at": "2008-09-14T02:32:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2952",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2952#issuecomment-20312",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This is still broken and the new coercion framework has been merged:

```
----------------------------------------------------------------------
| SAGE Version 3.1.2.rc2, Release Date: 2008-09-12                   |
| Type notebook() for the GUI, and license() for information.        |
sage: R.<q>=QQ[]
sage: L.<x,y,z> = LaurentPolynomialRing(R)
sage: 
sage: f=(x+y+z^-1)^2
sage: f.substitute(z=1)
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)

/scratch/mabshoff/release-cycle/sage-3.1.2.rc3/<ipython console> in <module>()

/scratch/mabshoff/release-cycle/sage-3.1.2.rc3/element.pyx in sage.structure.element.Element.substitute (sage/structure/element.c:3756)()

/scratch/mabshoff/release-cycle/sage-3.1.2.rc3/laurent_polynomial.pyx in sage.rings.polynomial.laurent_polynomial.LaurentPolynomial_mpair.subs (sage/rings/polynomial/laurent_polynomial.c:6666)()

/scratch/mabshoff/release-cycle/sage-3.1.2.rc3/element.pyx in sage.structure.element.RingElement.__imul__ (sage/structure/element.c:9590)()

/scratch/mabshoff/release-cycle/sage-3.1.2.rc3/coerce.pyx in sage.structure.coerce.CoercionModel_cache_maps.bin_op (sage/structure/coerce.c:6008)()

/scratch/mabshoff/release-cycle/sage-3.1.2.rc3/coerce.pyx in sage.structure.coerce.CoercionModel_cache_maps.get_action (sage/structure/coerce.c:9310)()

/scratch/mabshoff/release-cycle/sage-3.1.2.rc3/coerce.pyx in sage.structure.coerce.CoercionModel_cache_maps.discover_action (sage/structure/coerce.c:10441)()

/scratch/mabshoff/release-cycle/sage-3.1.2.rc3/coerce.pyx in sage.structure.coerce.CoercionModel_cache_maps.discover_action (sage/structure/coerce.c:10088)()

/scratch/mabshoff/release-cycle/sage-3.1.2.rc3/parent.pyx in sage.structure.parent.Parent.get_action (sage/structure/parent.c:8569)()

/scratch/mabshoff/release-cycle/sage-3.1.2.rc3/parent_old.pyx in sage.structure.parent_old.Parent._get_action_ (sage/structure/parent_old.c:5963)()

/scratch/mabshoff/release-cycle/sage-3.1.2.rc3/parent_old.pyx in sage.structure.parent_old.Parent.get_action_c (sage/structure/parent_old.c:2264)()

/scratch/mabshoff/release-cycle/sage-3.1.2.rc3/parent_old.pyx in sage.structure.parent_old.Parent.get_action_impl (sage/structure/parent_old.c:2481)()

/scratch/mabshoff/release-cycle/sage-3.1.2.rc3/parent_old.pyx in sage.structure.parent_old.Parent.get_action_c_impl (sage/structure/parent_old.c:3341)()

/scratch/mabshoff/release-cycle/sage-3.1.2.rc3/coerce_actions.pyx in sage.structure.coerce_actions.ModuleAction.__init__ (sage/structure/coerce_actions.c:3706)()

/scratch/mabshoff/release-cycle/sage-3.1.2.rc3/local/lib/python2.5/site-packages/sage/categories/pushout.py in pushout(R, S)
    437         if len(Sc) == 0:
    438             c = Rc.pop()
--> 439             Z = c(Z)
    440         elif len(Rc) == 0:
    441             c = Sc.pop()

/scratch/mabshoff/release-cycle/sage-3.1.2.rc3/local/lib/python2.5/site-packages/sage/categories/pushout.py in __call__(self, R)
    136             return LaurentPolynomialRing(R.base_ring(), (list(R.variable_names()) + [self.var]))
    137         else:
--> 138             return PolynomialRing(R, self.var)
    139     def __cmp__(self, other):
    140         c = cmp(type(self), type(other))

NameError: global name 'PolynomialRing' is not defined
sage: 
```
It seems that David's patch is not the right solution, so can someone come up with a better patch?

Cheers,

Michael



---

archive/issue_events_006744.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:34:36Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2952",
    "milestone": "sage-3.0.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2952#event-6744"
}
```



---

archive/issue_events_006745.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:34:36Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2952",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2952#event-6745"
}
```



---

archive/issue_events_006746.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2952",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2952#event-6746"
}
```



---

archive/issue_events_006747.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2952",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2952#event-6747"
}
```



---

archive/issue_comments_020313.json:
```json
{
    "body": "Changing keywords from \"\" to \"laurent polynomials\".",
    "created_at": "2014-03-04T12:31:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2952",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2952#issuecomment-20313",
    "user": "https://github.com/fchapoton"
}
```

Changing keywords from "" to "laurent polynomials".



---

archive/issue_comments_020314.json:
```json
{
    "body": "It seems the underlying problem is that `LaurentPolynomial_mpair.__pow__()` can return Laurent polynomials whose coefficients do not lie in its base ring, but in its fraction field:\n\n```\nsage: R.<q>=QQ[]\nsage: L.<x,y,z> = LaurentPolynomialRing(R)\nsage: g=z^-1\nsage: parent(g)\nMultivariate Laurent Polynomial Ring in x, y, z over Univariate Polynomial Ring in q over Rational Field\nsage: parent(g.coefficients()[0])\nFraction Field of Univariate Polynomial Ring in q over Rational Field\n```\nThe last line should simply be `Univariate ...`\n\nA slightly unrelated note: `z^-1` still lies in `L` (ignoring this bug), but `1/z` and `~z` return elements of the fraction field of `L`.",
    "created_at": "2014-05-04T23:51:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2952",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2952#issuecomment-20314",
    "user": "https://github.com/pjbruin"
}
```

It seems the underlying problem is that `LaurentPolynomial_mpair.__pow__()` can return Laurent polynomials whose coefficients do not lie in its base ring, but in its fraction field:

```
sage: R.<q>=QQ[]
sage: L.<x,y,z> = LaurentPolynomialRing(R)
sage: g=z^-1
sage: parent(g)
Multivariate Laurent Polynomial Ring in x, y, z over Univariate Polynomial Ring in q over Rational Field
sage: parent(g.coefficients()[0])
Fraction Field of Univariate Polynomial Ring in q over Rational Field
```
The last line should simply be `Univariate ...`

A slightly unrelated note: `z^-1` still lies in `L` (ignoring this bug), but `1/z` and `~z` return elements of the fraction field of `L`.



---

archive/issue_comments_020315.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2014-05-05T01:23:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2952",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2952#issuecomment-20315",
    "user": "https://github.com/pjbruin"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_020316.json:
```json
{
    "body": "Changing component from coercion to algebra.",
    "created_at": "2014-05-05T01:23:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2952",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2952#issuecomment-20316",
    "user": "https://github.com/pjbruin"
}
```

Changing component from coercion to algebra.



---

archive/issue_comments_020317.json:
```json
{
    "body": "The attached branch implements `LaurentPolynomial_mpair.__invert__()` from scratch and uses this for `__pow__()` with a negative exponent.",
    "created_at": "2014-05-05T01:23:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2952",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2952#issuecomment-20317",
    "user": "https://github.com/pjbruin"
}
```

The attached branch implements `LaurentPolynomial_mpair.__invert__()` from scratch and uses this for `__pow__()` with a negative exponent.



---

archive/issue_events_006748.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2952",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2952#event-6748"
}
```



---

archive/issue_events_006749.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2952",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2952#event-6749"
}
```



---

archive/issue_comments_020318.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2014-06-04T19:41:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2952",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2952#issuecomment-20318",
    "user": "https://github.com/fchapoton"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_020319.json:
```json
{
    "body": "Looks good to me, and the bot is happy. I have made very minor changes, so I allow myself to put this to positive review.\n\n---\nNew commits:",
    "created_at": "2014-06-04T19:41:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2952",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2952#issuecomment-20319",
    "user": "https://github.com/fchapoton"
}
```

Looks good to me, and the bot is happy. I have made very minor changes, so I allow myself to put this to positive review.

---
New commits:



---

archive/issue_comments_020320.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2014-06-06T11:00:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2952",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2952#issuecomment-20320",
    "user": "https://github.com/vbraun"
}
```

Resolution: fixed



---

archive/issue_events_006750.json:
```json
{
    "actor": "https://github.com/vbraun",
    "created_at": "2014-06-06T11:00:32Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2952",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2952#event-6750"
}
```
