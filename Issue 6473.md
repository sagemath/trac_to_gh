# Issue 6473: ideal.interreduced_basis hangs forever

archive/issues_006473.json:
```json
{
    "body": "Assignee: tbd\n\nThis completes in a fraction of a second:\n\n\n```\nsage: R.<a,b,c,d>=PolynomialRing(QQ,order=\"lex\")\nsage: ideal(a^16,a-b^16,b-c^16,c-d^15).interreduced_basis()\n[d^61440, c - d^15, b - d^240, a - d^3840]\n```\n\n\nI stopped the following after more than an hour, which leads me to believe that Sage is stuck in an infinite loop:\n\n\n```\nsage: R.<a,b,c,d>=PolynomialRing(QQ,order=\"lex\")\nsage: ideal(a^16,a-b^16,b-c^16,c-d^16).interreduced_basis()\n```\n\n\nThe only difference between the two is that the power of d in the input binomial involving c as the initial term is increased from 15 to 16. This difference has no mathematical significance and should have no impact on the computation time.\n\nI suspect that the reason is that by default Sage uses Singular to implement interreduced_basis, and Singular has limitations on the size of exponents. See http://www.singular.uni-kl.de/Manual/latest/sing_343.htm#SEC384 which in particular says\n\n\n```\nthe maximal allowed exponent of a ring variable depends on the ordering of the ring and is at least 32767.\n```\n\n\nIn this case increasing the exponent from 15 to 16 makes the output have an exponent of 16<sup>4</sup>=2<sup>16</sup>=65536, while leaving it at 15 puts it just a bit below that, allowing to contain it within a 16 bit integer.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6473\n\n",
    "created_at": "2009-07-07T05:00:28Z",
    "labels": [
        "algebra",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "ideal.interreduced_basis hangs forever",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6473",
    "user": "broune"
}
```
Assignee: tbd

This completes in a fraction of a second:


```
sage: R.<a,b,c,d>=PolynomialRing(QQ,order="lex")
sage: ideal(a^16,a-b^16,b-c^16,c-d^15).interreduced_basis()
[d^61440, c - d^15, b - d^240, a - d^3840]
```


I stopped the following after more than an hour, which leads me to believe that Sage is stuck in an infinite loop:


```
sage: R.<a,b,c,d>=PolynomialRing(QQ,order="lex")
sage: ideal(a^16,a-b^16,b-c^16,c-d^16).interreduced_basis()
```


The only difference between the two is that the power of d in the input binomial involving c as the initial term is increased from 15 to 16. This difference has no mathematical significance and should have no impact on the computation time.

I suspect that the reason is that by default Sage uses Singular to implement interreduced_basis, and Singular has limitations on the size of exponents. See http://www.singular.uni-kl.de/Manual/latest/sing_343.htm#SEC384 which in particular says


```
the maximal allowed exponent of a ring variable depends on the ordering of the ring and is at least 32767.
```


In this case increasing the exponent from 15 to 16 makes the output have an exponent of 16<sup>4</sup>=2<sup>16</sup>=65536, while leaving it at 15 puts it just a bit below that, allowing to contain it within a 16 bit integer.


Issue created by migration from https://trac.sagemath.org/ticket/6473





---

archive/issue_comments_052329.json:
```json
{
    "body": "Changing component from algebra to commutative algebra.",
    "created_at": "2009-11-15T13:15:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6473",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6473#issuecomment-52329",
    "user": "AlexGhitza"
}
```

Changing component from algebra to commutative algebra.



---

archive/issue_comments_052330.json:
```json
{
    "body": "Changing keywords from \"\" to \"groebner\".",
    "created_at": "2020-10-13T11:18:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6473",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6473#issuecomment-52330",
    "user": "chapoton"
}
```

Changing keywords from "" to "groebner".
