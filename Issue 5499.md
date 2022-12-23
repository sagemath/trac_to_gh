# Issue 5499: Wrong precision when creating p-adic field element

archive/issues_005499.json:
```json
{
    "body": "Assignee: was\n\nThis was originally reported on ticket #5076 but seems to be a separate issue.\n\n```\nsage: K = Qp(11,8)\nsage: a = 11^-2 + O(11^5)\nsage: a\n11^-2 + O(11^3)\n```\n\nBy contrast:\n\n```\nsage: K = Qp(11,8)\nsage: 11^(-2) + K(O(11^5))\n11^-2 + O(11^5)\n```\n\nNote that\n\n```\nsage: O(11^5).parent()\n11-adic Ring with capped relative precision 5\nsage: O(11^5).parent() == K\nFalse\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5499\n\n",
    "created_at": "2009-03-12T05:18:12Z",
    "labels": [
        "number theory",
        "major",
        "bug"
    ],
    "title": "Wrong precision when creating p-adic field element",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5499",
    "user": "kedlaya"
}
```
Assignee: was

This was originally reported on ticket #5076 but seems to be a separate issue.

```
sage: K = Qp(11,8)
sage: a = 11^-2 + O(11^5)
sage: a
11^-2 + O(11^3)
```

By contrast:

```
sage: K = Qp(11,8)
sage: 11^(-2) + K(O(11^5))
11^-2 + O(11^5)
```

Note that

```
sage: O(11^5).parent()
11-adic Ring with capped relative precision 5
sage: O(11^5).parent() == K
False
```



Issue created by migration from https://trac.sagemath.org/ticket/5499





---

archive/issue_comments_042709.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-03-17T05:31:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5499",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5499#issuecomment-42709",
    "user": "roed"
}
```

Attachment



---

archive/issue_comments_042710.json:
```json
{
    "body": "The explanation looks good, I'm not sure how one would get around this without doing something lazily. Also, +1 to only allowing `O(x^n)` not `O((x+1)^n)`\n\nHowever, what's up with the change of comparison direction in the last three files of the patch? Is this fixing an separate bug?",
    "created_at": "2009-03-18T05:01:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5499",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5499#issuecomment-42710",
    "user": "robertwb"
}
```

The explanation looks good, I'm not sure how one would get around this without doing something lazily. Also, +1 to only allowing `O(x^n)` not `O((x+1)^n)`

However, what's up with the change of comparison direction in the last three files of the patch? Is this fixing an separate bug?



---

archive/issue_comments_042711.json:
```json
{
    "body": "David: Any chance you could answer Robert's question since this patch is holding up the merge of #4637?\n\nCheers,\n\nMichael",
    "created_at": "2009-03-25T06:58:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5499",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5499#issuecomment-42711",
    "user": "mabshoff"
}
```

David: Any chance you could answer Robert's question since this patch is holding up the merge of #4637?

Cheers,

Michael



---

archive/issue_comments_042712.json:
```json
{
    "body": "This patch causes many doctest failures:\n\n```\n\tsage -t -long devel/sage/sage/schemes/elliptic_curves/padic_lseries.py # 1 doctests failed\n\tsage -t -long devel/sage/sage/schemes/elliptic_curves/ell_rational_field.py # 1 doctests failed\n\tsage -t -long devel/sage/sage/schemes/elliptic_curves/ell_tate_curve.py # 1 doctests failed\n\tsage -t -long devel/sage/doc/fr/tutorial/tour_polynomial.rst # 1 doctests failed\n\tsage -t -long devel/sage/sage/schemes/elliptic_curves/formal_group.py # 8 doctests failed\n\tsage -t -long devel/sage/doc/en/tutorial/tour_polynomial.rst # 1 doctests failed\n\tsage -t -long devel/sage/sage/rings/laurent_series_ring_element.pyx # 48 doctests failed\n\tsage -t -long devel/sage/sage/rings/laurent_series_ring.py # 3 doctests failed\n\tsage -t -long devel/sage/sage/rings/big_oh.py # 2 doctests failed\n\tsage -t -long devel/sage/sage/schemes/elliptic_curves/padics.py # Segfault\n```\n\nThe last seems to get very slow, i.e. only the last step in the following computation\n\n```\nTrying:\n    E = EllipticCurve('37a')###line 585:_sage_    >>> E = EllipticCurve('37a')\nExpecting nothing\nok\nTrying:\n    E.is_supersingular(Integer(3))###line 586:_sage_    >>> E.is_supersingular(3)\nExpecting:\n    True\nok\nTrying:\n    h = E.padic_height(Integer(3), Integer(5))###line 588:_sage_    >>> h = E.padic_height(3, 5)\nExpecting nothing\nok\nTrying:\n    h(E.gens()[Integer(0)])###line 589:_sage_    >>> h(E.gens()[0])\nExpecting:\n    (2*3 + 2*3^2 + 3^3 + 2*3^4 + 2*3^5 + O(3^6), 3^2 + 3^3 + 3^4 + 3^5 + O(3^7))\n```\n\ntakes more than 3 minutes CPU time on sage.math.\n\nCheers,\n\nMichael",
    "created_at": "2009-03-25T07:15:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5499",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5499#issuecomment-42712",
    "user": "mabshoff"
}
```

This patch causes many doctest failures:

```
	sage -t -long devel/sage/sage/schemes/elliptic_curves/padic_lseries.py # 1 doctests failed
	sage -t -long devel/sage/sage/schemes/elliptic_curves/ell_rational_field.py # 1 doctests failed
	sage -t -long devel/sage/sage/schemes/elliptic_curves/ell_tate_curve.py # 1 doctests failed
	sage -t -long devel/sage/doc/fr/tutorial/tour_polynomial.rst # 1 doctests failed
	sage -t -long devel/sage/sage/schemes/elliptic_curves/formal_group.py # 8 doctests failed
	sage -t -long devel/sage/doc/en/tutorial/tour_polynomial.rst # 1 doctests failed
	sage -t -long devel/sage/sage/rings/laurent_series_ring_element.pyx # 48 doctests failed
	sage -t -long devel/sage/sage/rings/laurent_series_ring.py # 3 doctests failed
	sage -t -long devel/sage/sage/rings/big_oh.py # 2 doctests failed
	sage -t -long devel/sage/sage/schemes/elliptic_curves/padics.py # Segfault
```

The last seems to get very slow, i.e. only the last step in the following computation

```
Trying:
    E = EllipticCurve('37a')###line 585:_sage_    >>> E = EllipticCurve('37a')
Expecting nothing
ok
Trying:
    E.is_supersingular(Integer(3))###line 586:_sage_    >>> E.is_supersingular(3)
Expecting:
    True
ok
Trying:
    h = E.padic_height(Integer(3), Integer(5))###line 588:_sage_    >>> h = E.padic_height(3, 5)
Expecting nothing
ok
Trying:
    h(E.gens()[Integer(0)])###line 589:_sage_    >>> h(E.gens()[0])
Expecting:
    (2*3 + 2*3^2 + 3^3 + 2*3^4 + 2*3^5 + O(3^6), 3^2 + 3^3 + 3^4 + 3^5 + O(3^7))
```

takes more than 3 minutes CPU time on sage.math.

Cheers,

Michael



---

archive/issue_comments_042713.json:
```json
{
    "body": "I was originally unsure whether this was simply because those doctests depended on the old behavior. But in fact there is a real problem with the patch, as I extracted from the second file on Michael's list.\n\n```\nsage: E=EllipticCurve('389a1')\nsage: X,Y=E.modular_parametrization()\nsage: q = X.parent().gen()\nsage: E.defining_polynomial()(X,Y,1)\n869*q^11 + 2151*q^12 - 2768*q^13 + O(q^14)\nsage: E.defining_polynomial()(X,Y,1) + O(q^11)\n870*q^11 + 2151*q^12 - 2768*q^13 + O(q^14)\n```\n",
    "created_at": "2009-04-12T12:59:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5499",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5499#issuecomment-42713",
    "user": "kedlaya"
}
```

I was originally unsure whether this was simply because those doctests depended on the old behavior. But in fact there is a real problem with the patch, as I extracted from the second file on Michael's list.

```
sage: E=EllipticCurve('389a1')
sage: X,Y=E.modular_parametrization()
sage: q = X.parent().gen()
sage: E.defining_polynomial()(X,Y,1)
869*q^11 + 2151*q^12 - 2768*q^13 + O(q^14)
sage: E.defining_polynomial()(X,Y,1) + O(q^11)
870*q^11 + 2151*q^12 - 2768*q^13 + O(q^14)
```




---

archive/issue_comments_042714.json:
```json
{
    "body": "To clarify my previous comment: before the patch, we have correctly:\n\n```\nsage: R.<q> = LaurentSeriesRing(Rationals())\nsage: O(q^14)\nO(q^14)\n```\n\nbut afterwards we have:\n\n```\nsage: R.<q> = LaurentSeriesRing(Rationals())\nsage: O(q^14)\nq^14\n```\n",
    "created_at": "2009-04-12T14:06:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5499",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5499#issuecomment-42714",
    "user": "kedlaya"
}
```

To clarify my previous comment: before the patch, we have correctly:

```
sage: R.<q> = LaurentSeriesRing(Rationals())
sage: O(q^14)
O(q^14)
```

but afterwards we have:

```
sage: R.<q> = LaurentSeriesRing(Rationals())
sage: O(q^14)
q^14
```




---

archive/issue_comments_042715.json:
```json
{
    "body": "I fixed the problem with the laurent series ring, which was also causing the doctest failures.\n\nThe change in direction of the coercion maps is one that I discussed with Kiran at AWS.  I think it's a good idea, though it is a somewhat different issue.",
    "created_at": "2009-04-12T16:47:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5499",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5499#issuecomment-42715",
    "user": "roed"
}
```

I fixed the problem with the laurent series ring, which was also causing the doctest failures.

The change in direction of the coercion maps is one that I discussed with Kiran at AWS.  I think it's a good idea, though it is a somewhat different issue.



---

archive/issue_comments_042716.json:
```json
{
    "body": "Fixes laurents series, as well as p-adic l-series code affected by change in direction of coercion",
    "created_at": "2009-04-12T16:49:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5499",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5499#issuecomment-42716",
    "user": "roed"
}
```

Fixes laurents series, as well as p-adic l-series code affected by change in direction of coercion



---

archive/issue_comments_042717.json:
```json
{
    "body": "Attachment\n\nCool, trac_5499_2.patch only passes doctests for my 3.4.1.rc3 merge tree.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-13T03:03:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5499",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5499#issuecomment-42717",
    "user": "mabshoff"
}
```

Attachment

Cool, trac_5499_2.patch only passes doctests for my 3.4.1.rc3 merge tree.

Cheers,

Michael



---

archive/issue_comments_042718.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-04-13T08:47:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5499",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5499#issuecomment-42718",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_042719.json:
```json
{
    "body": "Merged trac_5499_2.patch in Sage 3.4.1.rc3.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-13T08:47:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5499",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5499#issuecomment-42719",
    "user": "mabshoff"
}
```

Merged trac_5499_2.patch in Sage 3.4.1.rc3.

Cheers,

Michael



---

archive/issue_comments_042720.json:
```json
{
    "body": "Regarding \"change in direction of the coercion maps\", this should at least be accompanied by some doctests to illistrate what's going on...",
    "created_at": "2009-04-14T02:15:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5499",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5499#issuecomment-42720",
    "user": "robertwb"
}
```

Regarding "change in direction of the coercion maps", this should at least be accompanied by some doctests to illistrate what's going on...



---

archive/issue_comments_042721.json:
```json
{
    "body": "This is the patch I imported which gives credit to David",
    "created_at": "2009-04-15T03:26:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5499",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5499#issuecomment-42721",
    "user": "mabshoff"
}
```

This is the patch I imported which gives credit to David
