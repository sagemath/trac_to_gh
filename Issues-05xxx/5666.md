# Issue 5666: forming ideals in IntegerModRing_generic does not work

archive/issues_005666.json:
```json
{
    "body": "Assignee: tbd\n\nIt is impossible to create ideals in rings of the form Integers mod n:\n\n```\nsage: R = Integers(10)\nsage: R.ideal(1)\n---------------------------------------------------------------------------\nAttributeError                            Traceback (most recent call last)\n\n/home/masgaj/.sage/temp/host_56_150/5831/_home_masgaj__sage_init_sage_0.py\nin <module>()\n\n/local/jec/sage-3.4.1.alpha0/local/lib/python2.5/site-packages/sage/rings/quotient_ring.pyc\nin ideal(self, *gens, **kwds)\n   487             gens = gens[0]\n   488         from\nsage.rings.polynomial.multi_polynomial_libsingular import\nMPolynomialRing_libsingular\n--> 489         if not\nisinstance(self.__R,MPolynomialRing_libsingular) and not\nself.__R._has_singular:\n   490             # pass through\n   491             MPolynomialRing_generic.ideal(self,gens,**kwds)\n\nAttributeError: 'sage.rings.integer_ring.IntegerRing_class' object has\nno attribute '_has_singular'\nsage: R.ideal([2,4])\n---------------------------------------------------------------------------\nAttributeError                            Traceback (most recent call last)\n\n(as above)\n```\n\nIt looks as if the ideal() method for class  `QuotientRing_generic ` is\nonly really geared to polynomial ring quotients.\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5666\n\n",
    "closed_at": "2010-01-18T22:41:43Z",
    "created_at": "2009-04-02T15:41:15Z",
    "labels": [
        "component: algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.1",
    "title": "forming ideals in IntegerModRing_generic does not work",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5666",
    "user": "https://github.com/JohnCremona"
}
```
Assignee: tbd

It is impossible to create ideals in rings of the form Integers mod n:

```
sage: R = Integers(10)
sage: R.ideal(1)
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)

/home/masgaj/.sage/temp/host_56_150/5831/_home_masgaj__sage_init_sage_0.py
in <module>()

/local/jec/sage-3.4.1.alpha0/local/lib/python2.5/site-packages/sage/rings/quotient_ring.pyc
in ideal(self, *gens, **kwds)
   487             gens = gens[0]
   488         from
sage.rings.polynomial.multi_polynomial_libsingular import
MPolynomialRing_libsingular
--> 489         if not
isinstance(self.__R,MPolynomialRing_libsingular) and not
self.__R._has_singular:
   490             # pass through
   491             MPolynomialRing_generic.ideal(self,gens,**kwds)

AttributeError: 'sage.rings.integer_ring.IntegerRing_class' object has
no attribute '_has_singular'
sage: R.ideal([2,4])
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)

(as above)
```

It looks as if the ideal() method for class  `QuotientRing_generic ` is
only really geared to polynomial ring quotients.



Issue created by migration from https://trac.sagemath.org/ticket/5666





---

archive/issue_events_013321.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-04-23T08:06:21Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5666",
    "milestone": "sage-4.0",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5666#event-13321"
}
```



---

archive/issue_comments_044249.json:
```json
{
    "body": "Attachment [trac_5666.patch](tarball://root/attachments/some-uuid/ticket5666/trac_5666.patch) by @williamstein created at 2010-01-17 06:36:24",
    "created_at": "2010-01-17T06:36:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5666",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5666#issuecomment-44249",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac_5666.patch](tarball://root/attachments/some-uuid/ticket5666/trac_5666.patch) by @williamstein created at 2010-01-17 06:36:24



---

archive/issue_comments_044250.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-17T06:36:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5666",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5666#issuecomment-44250",
    "user": "https://github.com/williamstein"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_044251.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-18T05:20:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5666",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5666#issuecomment-44251",
    "user": "https://github.com/rbeezer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_044252.json:
```json
{
    "body": "Passes tests and allows creation of ideals within rings of integers mod n.\n\nBut it seems the resulting ideals still need some work, for example `_contains_()` in `rings.ideal.Ideal_generic` is not implemented.\n\n```\nsage: R=Integers(40)\nsage: Q=R.ideal([2,3])\nsage: type(Q)\n<class 'sage.rings.ideal.Ideal_generic'>\nsage: 1 in Q\n------------------\nNotImplementedError\n<snip>\n```",
    "created_at": "2010-01-18T05:20:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5666",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5666#issuecomment-44252",
    "user": "https://github.com/rbeezer"
}
```

Passes tests and allows creation of ideals within rings of integers mod n.

But it seems the resulting ideals still need some work, for example `_contains_()` in `rings.ideal.Ideal_generic` is not implemented.

```
sage: R=Integers(40)
sage: Q=R.ideal([2,3])
sage: type(Q)
<class 'sage.rings.ideal.Ideal_generic'>
sage: 1 in Q
------------------
NotImplementedError
<snip>
```



---

archive/issue_events_013322.json:
```json
{
    "actor": "https://github.com/rlmill",
    "created_at": "2010-01-18T22:41:43Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5666",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5666#event-13322"
}
```



---

archive/issue_comments_044253.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-18T22:41:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5666",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5666#issuecomment-44253",
    "user": "https://github.com/rlmill"
}
```

Resolution: fixed
