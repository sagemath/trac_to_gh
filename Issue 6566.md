# Issue 6566: method key_space() for classical cryptosystems

archive/issues_006566.json:
```json
{
    "body": "Assignee: somebody\n\nKeywords: key space, classical cryptosystems\n\nAdd method `key_space()` to the following classes:\n\n* `sage.crypto.classical.HillCryptosystem`\n\n* `sage.crypto.classical.SubstitutionCryptosystem`\n\n* `sage.crypto.classical.TranspositionCryptosystem`\n\n* `sage.crypto.classical.VigenereCryptosystem`\n\nThe new method `key_space()` should output the number of possible keys for each of the above cryptosystems.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6566\n\n",
    "created_at": "2009-07-20T11:56:13Z",
    "labels": [
        "cryptography",
        "major",
        "enhancement"
    ],
    "title": "method key_space() for classical cryptosystems",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6566",
    "user": "mvngu"
}
```
Assignee: somebody

Keywords: key space, classical cryptosystems

Add method `key_space()` to the following classes:

* `sage.crypto.classical.HillCryptosystem`

* `sage.crypto.classical.SubstitutionCryptosystem`

* `sage.crypto.classical.TranspositionCryptosystem`

* `sage.crypto.classical.VigenereCryptosystem`

The new method `key_space()` should output the number of possible keys for each of the above cryptosystems.

Issue created by migration from https://trac.sagemath.org/ticket/6566





---

archive/issue_comments_053560.json:
```json
{
    "body": "As far as I can tell, these have been implemented since forever. For example: \n\n\n```\nsage: S = AlphabeticStrings()\nsage: H = HillCryptosystem(S,3)\nsage: H.key_space()\nFull MatrixSpace of 3 by 3 dense matrices over Ring of integers modulo 26\n```\n    \n\nSimilar results can be produced for all other ciphers mentioned. This is either inherited from SymmetricKeyCryptosystem or is overridden in the init methods.",
    "created_at": "2012-12-16T13:27:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6566",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6566#issuecomment-53560",
    "user": "scotts"
}
```

As far as I can tell, these have been implemented since forever. For example: 


```
sage: S = AlphabeticStrings()
sage: H = HillCryptosystem(S,3)
sage: H.key_space()
Full MatrixSpace of 3 by 3 dense matrices over Ring of integers modulo 26
```
    

Similar results can be produced for all other ciphers mentioned. This is either inherited from SymmetricKeyCryptosystem or is overridden in the init methods.



---

archive/issue_comments_053561.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2015-05-26T18:40:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6566",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6566#issuecomment-53561",
    "user": "tscholl2"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_053562.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2015-05-26T18:40:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6566",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6566#issuecomment-53562",
    "user": "tscholl2"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_053563.json:
```json
{
    "body": "I marked this as wont fix because it's implemented at least as of 6.4. In 6.7 The following works\n\n\n```\n    sage: S = HillCryptosystem(AlphabeticStrings(),3)\n    sage: S.key_space()\n    Full MatrixSpace of 3 by 3 dense matrices over Ring of integers modulo 26\n\n    sage: S = SubstitutionCryptosystem(AlphabeticStrings())\n    sage: S.key_space()\n    Free alphabetic string monoid on A-Z\n\n    sage: S = TranspositionCryptosystem(AlphabeticStrings(),2)\n    sage: S.key_space()\n    Symmetric group of order 2! as a permutation group\n\n    sage: S = VigenereCryptosystem(AlphabeticStrings(), 2)\n    sage: S.key_space()\n    Free alphabetic string monoid on A-Z\n```\n",
    "created_at": "2015-05-26T18:43:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6566",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6566#issuecomment-53563",
    "user": "tscholl2"
}
```

I marked this as wont fix because it's implemented at least as of 6.4. In 6.7 The following works


```
    sage: S = HillCryptosystem(AlphabeticStrings(),3)
    sage: S.key_space()
    Full MatrixSpace of 3 by 3 dense matrices over Ring of integers modulo 26

    sage: S = SubstitutionCryptosystem(AlphabeticStrings())
    sage: S.key_space()
    Free alphabetic string monoid on A-Z

    sage: S = TranspositionCryptosystem(AlphabeticStrings(),2)
    sage: S.key_space()
    Symmetric group of order 2! as a permutation group

    sage: S = VigenereCryptosystem(AlphabeticStrings(), 2)
    sage: S.key_space()
    Free alphabetic string monoid on A-Z
```




---

archive/issue_comments_053564.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2015-06-19T08:38:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6566",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6566#issuecomment-53564",
    "user": "vbraun"
}
```

Resolution: fixed
