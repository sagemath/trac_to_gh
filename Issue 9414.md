# Issue 9414: make the rational number field, consistent with other number fields

archive/issues_009414.json:
```json
{
    "body": "Assignee: davidloeffler\n\nKeywords: number field, rationals\n\nCurrently QQ behaves different than a generic number field. This forces number theory functions to treat QQ separately, which is inconvenient.\n\n\n```\nK = QQ\nI = K.ideal(7)\n```\n\n\nThis creates ideal that does not have the functions I.denominator, I.numerator, I.prime_ideals() ... which a fractional ideal in a number field should have\n\n\n```\nK.<a> = NumberField(x^2+2)\nI = K.ideal(7)\n```\n\n\nSimilarly, QQ.places() is not implemented; it should return the one infinite place for Q. Although there seems to be QQ.embeddings().\n\n\n```\nQQ.places()\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9414\n\n",
    "created_at": "2010-07-03T02:38:31Z",
    "labels": [
        "number fields",
        "major",
        "bug"
    ],
    "title": "make the rational number field, consistent with other number fields",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9414",
    "user": "rkirov"
}
```
Assignee: davidloeffler

Keywords: number field, rationals

Currently QQ behaves different than a generic number field. This forces number theory functions to treat QQ separately, which is inconvenient.


```
K = QQ
I = K.ideal(7)
```


This creates ideal that does not have the functions I.denominator, I.numerator, I.prime_ideals() ... which a fractional ideal in a number field should have


```
K.<a> = NumberField(x^2+2)
I = K.ideal(7)
```


Similarly, QQ.places() is not implemented; it should return the one infinite place for Q. Although there seems to be QQ.embeddings().


```
QQ.places()
```


Issue created by migration from https://trac.sagemath.org/ticket/9414





---

archive/issue_comments_089738.json:
```json
{
    "body": "This is a duplicate of #7596. I'm putting it as positive review so that someone with the right abilities will see it an close this as duplicate ticket.",
    "created_at": "2011-02-10T14:07:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9414",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9414#issuecomment-89738",
    "user": "mderickx"
}
```

This is a duplicate of #7596. I'm putting it as positive review so that someone with the right abilities will see it an close this as duplicate ticket.



---

archive/issue_comments_089739.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2011-02-10T14:07:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9414",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9414#issuecomment-89739",
    "user": "mderickx"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_089740.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-02-10T14:08:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9414",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9414#issuecomment-89740",
    "user": "mderickx"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_089741.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2011-02-16T09:36:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9414",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9414#issuecomment-89741",
    "user": "jdemeyer"
}
```

Resolution: duplicate
