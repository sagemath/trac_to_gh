# Issue 6472: ideal.groebner_basis gives incorrect answers

archive/issues_006472.json:
```json
{
    "body": "Assignee: tbd\n\nThis is wrong:\n\n\n```\nsage: R.<a,b,c,d>=PolynomialRing(QQ,order=\"lex\")\nsage: ideal(a-b^16,b-c^16,c-d^1024).groebner_basis()\n[a - d^4096, b - d^16384, c - d^1024]\n```\n\n\nThe correct answer as given by Macaulay 2:\n\n\n```\ni30 : R=QQ[a,b,c,d, MonomialOrder=>Lex];\ni31 : I=ideal(a-b^16,b-c^16,c-d^1024);\ni32 : gens gb I\no32 = | c-d1024 b-d16384 a-d262144 |\n```\n\n\nIn particular the binomial involving a should raise d to the power 262144=2<sup>18</sup>, not 4096=2<sup>12</sup> as Sage reports.\n\nI suspect that the reason is that by default Sage uses Singular to implement groebner_basis, and Singular has limitations on the size of exponents. See http://www.singular.uni-kl.de/Manual/latest/sing_343.htm#SEC384 which in particular says\n\n\n```\nthe maximal allowed exponent of a ring variable depends on the ordering of the ring and is at least 32767.\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6472\n\n",
    "created_at": "2009-07-07T04:49:45Z",
    "labels": [
        "algebra",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "ideal.groebner_basis gives incorrect answers",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6472",
    "user": "broune"
}
```
Assignee: tbd

This is wrong:


```
sage: R.<a,b,c,d>=PolynomialRing(QQ,order="lex")
sage: ideal(a-b^16,b-c^16,c-d^1024).groebner_basis()
[a - d^4096, b - d^16384, c - d^1024]
```


The correct answer as given by Macaulay 2:


```
i30 : R=QQ[a,b,c,d, MonomialOrder=>Lex];
i31 : I=ideal(a-b^16,b-c^16,c-d^1024);
i32 : gens gb I
o32 = | c-d1024 b-d16384 a-d262144 |
```


In particular the binomial involving a should raise d to the power 262144=2<sup>18</sup>, not 4096=2<sup>12</sup> as Sage reports.

I suspect that the reason is that by default Sage uses Singular to implement groebner_basis, and Singular has limitations on the size of exponents. See http://www.singular.uni-kl.de/Manual/latest/sing_343.htm#SEC384 which in particular says


```
the maximal allowed exponent of a ring variable depends on the ordering of the ring and is at least 32767.
```


Issue created by migration from https://trac.sagemath.org/ticket/6472





---

archive/issue_comments_052320.json:
```json
{
    "body": "Changing component from algebra to commutative algebra.",
    "created_at": "2009-11-15T13:15:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6472",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6472#issuecomment-52320",
    "user": "@aghitza"
}
```

Changing component from algebra to commutative algebra.



---

archive/issue_comments_052321.json:
```json
{
    "body": "reported upstream:\n\nhttps://www.singular.uni-kl.de:8005/trac/ticket/774#ticket",
    "created_at": "2016-10-04T23:18:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6472",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6472#issuecomment-52321",
    "user": "jakobkroeker"
}
```

reported upstream:

https://www.singular.uni-kl.de:8005/trac/ticket/774#ticket



---

archive/issue_comments_052322.json:
```json
{
    "body": "another funny example :\n\n\n```\nR.<b,c,d>=PolynomialRing(QQ,order=\"lex\")\nsage: ideal(b-c^64,c-d^1024).groebner_basis()\n```\n\n(wrong result and zero not shown)\n\n```\n[b - , c - d^1024]\n```\n",
    "created_at": "2016-10-04T23:50:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6472",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6472#issuecomment-52322",
    "user": "jakobkroeker"
}
```

another funny example :


```
R.<b,c,d>=PolynomialRing(QQ,order="lex")
sage: ideal(b-c^64,c-d^1024).groebner_basis()
```

(wrong result and zero not shown)

```
[b - , c - d^1024]
```




---

archive/issue_comments_052323.json:
```json
{
    "body": "Does Singular simply return incorrect results, or it's rather a Sage interface bug?",
    "created_at": "2016-10-05T23:49:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6472",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6472#issuecomment-52323",
    "user": "@dimpase"
}
```

Does Singular simply return incorrect results, or it's rather a Sage interface bug?



---

archive/issue_comments_052324.json:
```json
{
    "body": "fixed in https://github.com/Singular/Sources/commit/349e5e898aad7e735b03bda328f2741a7c36a092\n\nbroken again for 'groebner' with https://github.com/Singular/Sources/commit/17510a828cdc33aa541d40a9bbfb825b72812521",
    "created_at": "2016-10-06T22:57:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6472",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6472#issuecomment-52324",
    "user": "jakobkroeker"
}
```

fixed in https://github.com/Singular/Sources/commit/349e5e898aad7e735b03bda328f2741a7c36a092

broken again for 'groebner' with https://github.com/Singular/Sources/commit/17510a828cdc33aa541d40a9bbfb825b72812521



---

archive/issue_comments_052325.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2018-07-01T20:44:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6472",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6472#issuecomment-52325",
    "user": "@simonbrandhorst"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_052326.json:
```json
{
    "body": "\n```\nsage: R.<a,b,c,d>=PolynomialRing(QQ,order=\"lex\")\n....: \nsage: I = ideal(a-b^16,b-c^16,c-d^1024)\nsage: I.groebner_basis()\n   skipping text from `)` error at token `)`\n---------------------------------------------------------------------------\nRuntimeError                              Traceback (most recent call last)\nRuntimeError: Error raised calling singular function\n...\nRuntimeError: error in Singular function call 'groebner':\nexponent bound is 65535\nerror occurred in or before standard.lib::stdhilb line 381: `    i=interred(i);`\nleaving standard.lib::stdhilb\nleaving standard.lib::groebner\n```\n\n\nLooks good to me.",
    "created_at": "2018-07-01T20:44:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6472",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6472#issuecomment-52326",
    "user": "@simonbrandhorst"
}
```


```
sage: R.<a,b,c,d>=PolynomialRing(QQ,order="lex")
....: 
sage: I = ideal(a-b^16,b-c^16,c-d^1024)
sage: I.groebner_basis()
   skipping text from `)` error at token `)`
---------------------------------------------------------------------------
RuntimeError                              Traceback (most recent call last)
RuntimeError: Error raised calling singular function
...
RuntimeError: error in Singular function call 'groebner':
exponent bound is 65535
error occurred in or before standard.lib::stdhilb line 381: `    i=interred(i);`
leaving standard.lib::stdhilb
leaving standard.lib::groebner
```


Looks good to me.



---

archive/issue_comments_052327.json:
```json
{
    "body": "This \n\n```\n  skipping text from `)` error at token `)`\n```\n\nlooks ugly, but otherwise there seems nothing to fix here---unless nowadays Singular offers an option to have bigger exponents.",
    "created_at": "2018-07-01T20:51:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6472",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6472#issuecomment-52327",
    "user": "@dimpase"
}
```

This 

```
  skipping text from `)` error at token `)`
```

looks ugly, but otherwise there seems nothing to fix here---unless nowadays Singular offers an option to have bigger exponents.



---

archive/issue_comments_052328.json:
```json
{
    "body": "Resolution: worksforme",
    "created_at": "2018-08-14T17:30:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6472",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6472#issuecomment-52328",
    "user": "@embray"
}
```

Resolution: worksforme
