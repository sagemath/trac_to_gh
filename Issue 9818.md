# Issue 9818: Add a default gcd and lcm methods for fields

archive/issues_009818.json:
```json
{
    "body": "Assignee: @aghitza\n\nKeywords: lcm, gcd, fields\n\nFor the case of field elements gcd and lcm methods are not of great interest. However, they can be addecuated for some reasons.\n\n- Some algorithms may accept as input either polynomials or rational functions. In these algorithms we may reduce a list of polynomials and rational functions to a common denominator. If all the inputs are polynomials, the denominators are the one element of the base field. In this case, lcm would fail.\n\nSee #9063 for a case of this problem.\n\n- Rational numbers already have custom gcd and lcm methods.\n\n-It would erase the following problem. Currently, if we are dealing with elements in a finite field, the gcd of the elements can be computed sometimes coercing to the integers and doing computations. This lead to inconsistencies.\n\n```\nsage: a=F(2)\nsage: gcd(a,a)\n2\nsage: gcd(a,p)\n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n\n/home/luisfe/Varios/Comprobantes-gastos/<ipython console> in <module>()\n\n/opt/SAGE/sage-4.5.2/local/lib/python2.6/site-packages/sage/rings/arith.pyc in gcd(a, b, **kwargs)\n   1423                 return ZZ(a).gcd(ZZ(b))\n   1424             except TypeError:\n-> 1425                 raise TypeError, \"unable to find gcd of %s and %s\"%(a,b)\n   1426     \n   1427     from sage.structure.sequence import Sequence\n\nTypeError: unable to find gcd of 2 and p\n```\n\nI propose the following:\n\n- For gcd, follow the convention of the rational cesa. If both elements are 0, return 0 (on the appropriate field). Otherwise return 1\n\n- For lcm, if one of the elements is zero, return zero. Otherwise return 1.\n\n#9063 depends on this bug to be merged.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9819\n\n",
    "created_at": "2010-08-27T10:55:25Z",
    "labels": [
        "component: algebra"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Add a default gcd and lcm methods for fields",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9818",
    "user": "https://github.com/lftabera"
}
```
Assignee: @aghitza

Keywords: lcm, gcd, fields

For the case of field elements gcd and lcm methods are not of great interest. However, they can be addecuated for some reasons.

- Some algorithms may accept as input either polynomials or rational functions. In these algorithms we may reduce a list of polynomials and rational functions to a common denominator. If all the inputs are polynomials, the denominators are the one element of the base field. In this case, lcm would fail.

See #9063 for a case of this problem.

- Rational numbers already have custom gcd and lcm methods.

-It would erase the following problem. Currently, if we are dealing with elements in a finite field, the gcd of the elements can be computed sometimes coercing to the integers and doing computations. This lead to inconsistencies.

```
sage: a=F(2)
sage: gcd(a,a)
2
sage: gcd(a,p)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/luisfe/Varios/Comprobantes-gastos/<ipython console> in <module>()

/opt/SAGE/sage-4.5.2/local/lib/python2.6/site-packages/sage/rings/arith.pyc in gcd(a, b, **kwargs)
   1423                 return ZZ(a).gcd(ZZ(b))
   1424             except TypeError:
-> 1425                 raise TypeError, "unable to find gcd of %s and %s"%(a,b)
   1426     
   1427     from sage.structure.sequence import Sequence

TypeError: unable to find gcd of 2 and p
```

I propose the following:

- For gcd, follow the convention of the rational cesa. If both elements are 0, return 0 (on the appropriate field). Otherwise return 1

- For lcm, if one of the elements is zero, return zero. Otherwise return 1.

#9063 depends on this bug to be merged.

Issue created by migration from https://trac.sagemath.org/ticket/9819





---

archive/issue_events_024690.json:
```json
{
    "actor": "https://github.com/lftabera",
    "created_at": "2010-08-27T11:13:54Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9818",
    "milestone": "sage-4.5.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9818#event-24690"
}
```



---

archive/issue_comments_096657.json:
```json
{
    "body": "To make thing worse, currently (sage 4.5.3.alpha2) GF(5)(4) is an IntegerMod_int that does not derive from FieldElement but CommutativeRingElement",
    "created_at": "2010-09-01T14:27:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9818",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9818#issuecomment-96657",
    "user": "https://github.com/lftabera"
}
```

To make thing worse, currently (sage 4.5.3.alpha2) GF(5)(4) is an IntegerMod_int that does not derive from FieldElement but CommutativeRingElement



---

archive/issue_comments_096658.json:
```json
{
    "body": "related ticket with different proposal: #10771",
    "created_at": "2011-02-14T14:59:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9818",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9818#issuecomment-96658",
    "user": "https://github.com/mstreng"
}
```

related ticket with different proposal: #10771



---

archive/issue_comments_096659.json:
```json
{
    "body": "Replying to [comment:3 mstreng]:\n> related ticket with different proposal: #10771\n\n\nI wouldn't say that it is a different proposal. #10771 treats the case of fields that happen to be the fraction field of a unique factorization domain. In this case, one can do better than to return either 0 or 1.\n\nHowever, #10771 does not consider the case of fields that are no fraction fields, or are fraction fields of rings that do not provide lcm and gcd. I suggest that for that purpose, one should implement gcd and lcd as element methods of the category of `Fields()`. That would also solve the problem that `IntegerMod_int` does not derive from `FieldElement`.",
    "created_at": "2011-02-14T15:31:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9818",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9818#issuecomment-96659",
    "user": "https://github.com/simon-king-jena"
}
```

Replying to [comment:3 mstreng]:
> related ticket with different proposal: #10771


I wouldn't say that it is a different proposal. #10771 treats the case of fields that happen to be the fraction field of a unique factorization domain. In this case, one can do better than to return either 0 or 1.

However, #10771 does not consider the case of fields that are no fraction fields, or are fraction fields of rings that do not provide lcm and gcd. I suggest that for that purpose, one should implement gcd and lcd as element methods of the category of `Fields()`. That would also solve the problem that `IntegerMod_int` does not derive from `FieldElement`.



---

archive/issue_events_024691.json:
```json
{
    "actor": "https://github.com/mstreng",
    "created_at": "2012-01-12T12:05:07Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9818",
    "milestone": "sage-4.5.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9818#event-24691"
}
```



---

archive/issue_events_024692.json:
```json
{
    "actor": "https://github.com/mstreng",
    "created_at": "2012-01-12T12:05:07Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9818",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9818#event-24692"
}
```



---

archive/issue_comments_096660.json:
```json
{
    "body": "Is everything on this ticket fixed already? It seems that #10771 did implement `Fields.ElementMethods.gcd()` after all and its behaviour is as requested in this ticket.",
    "created_at": "2012-01-12T12:05:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9818",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9818#issuecomment-96660",
    "user": "https://github.com/mstreng"
}
```

Is everything on this ticket fixed already? It seems that #10771 did implement `Fields.ElementMethods.gcd()` after all and its behaviour is as requested in this ticket.



---

archive/issue_comments_096661.json:
```json
{
    "body": "Changing status from new to needs_info.",
    "created_at": "2012-01-12T12:05:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9818",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9818#issuecomment-96661",
    "user": "https://github.com/mstreng"
}
```

Changing status from new to needs_info.



---

archive/issue_comments_096662.json:
```json
{
    "body": "Yes, this ticket should be resolved as duplicated.",
    "created_at": "2012-01-12T17:32:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9818",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9818#issuecomment-96662",
    "user": "https://github.com/lftabera"
}
```

Yes, this ticket should be resolved as duplicated.



---

archive/issue_comments_096663.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2012-01-12T17:32:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9818",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9818#issuecomment-96663",
    "user": "https://github.com/lftabera"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_096664.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2012-01-16T15:00:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9818",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9818#issuecomment-96664",
    "user": "https://github.com/mstreng"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_096665.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2012-01-31T09:39:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9818",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9818#issuecomment-96665",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: duplicate



---

archive/issue_events_024693.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2012-01-31T09:39:34Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9818",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9818#event-24693"
}
```
