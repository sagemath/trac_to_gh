# Issue 681: new MQ submodule for sage.crypto [with patch]

archive/issues_000681.json:
```json
{
    "body": "Assignee: was\n\nThe attached patch implements a **MPolynomialSystem**, a **MPolynomialSystemGenerator** class, and as a generator for small scale AES variants.\n\n\n**MPolynomialSystem** is supposed to model multivariate polynomial systems as they appear in e.g. algebraic cryptanalysis. The implemented design is as follows: There is a class **MPolynomialSystem** which models the actual polynomial system. This class contains a list of **MPolynomialRoundSystems** to model the rounds of a cipher to add some structure. **MPolynomialSystem** is furthermore specialised to **MPolynomialSystem_gf2[e]** classes which have additional features. E.g. systems over `GF(2^e)` can be projected down to `GF(2)` and systems over `GF(2)` may eventually contain rountines for ANF-CNF conversion.\n\nAlso there is a class called **MPolynomialSystemGenerator** which is meant as a base class for specific generators for polynomial systems like AES or the Courtois Toy Cipher (CTC).\n\nThe patch also contains a generator for polynomial systems for small scale AES variants (SR) over `GF(2)` and `GF(2^e)` as introduced in http://www.isg.rhul.ac.uk/~sean/smallAES-fse05.pdf .\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/681\n\n",
    "created_at": "2007-09-17T16:00:55Z",
    "labels": [
        "algebraic geometry",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.5",
    "title": "new MQ submodule for sage.crypto [with patch]",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/681",
    "user": "malb"
}
```
Assignee: was

The attached patch implements a **MPolynomialSystem**, a **MPolynomialSystemGenerator** class, and as a generator for small scale AES variants.


**MPolynomialSystem** is supposed to model multivariate polynomial systems as they appear in e.g. algebraic cryptanalysis. The implemented design is as follows: There is a class **MPolynomialSystem** which models the actual polynomial system. This class contains a list of **MPolynomialRoundSystems** to model the rounds of a cipher to add some structure. **MPolynomialSystem** is furthermore specialised to **MPolynomialSystem_gf2[e]** classes which have additional features. E.g. systems over `GF(2^e)` can be projected down to `GF(2)` and systems over `GF(2)` may eventually contain rountines for ANF-CNF conversion.

Also there is a class called **MPolynomialSystemGenerator** which is meant as a base class for specific generators for polynomial systems like AES or the Courtois Toy Cipher (CTC).

The patch also contains a generator for polynomial systems for small scale AES variants (SR) over `GF(2)` and `GF(2^e)` as introduced in http://www.isg.rhul.ac.uk/~sean/smallAES-fse05.pdf .


Issue created by migration from https://trac.sagemath.org/ticket/681





---

archive/issue_comments_003533.json:
```json
{
    "body": "Attachment [mq.patch](tarball://root/attachments/some-uuid/ticket681/mq.patch) by malb created at 2007-09-17 16:01:35",
    "created_at": "2007-09-17T16:01:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/681",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/681#issuecomment-3533",
    "user": "malb"
}
```

Attachment [mq.patch](tarball://root/attachments/some-uuid/ticket681/mq.patch) by malb created at 2007-09-17 16:01:35



---

archive/issue_comments_003534.json:
```json
{
    "body": "Great, first bugfix already. See second attachment.",
    "created_at": "2007-09-17T17:18:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/681",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/681#issuecomment-3534",
    "user": "malb"
}
```

Great, first bugfix already. See second attachment.



---

archive/issue_comments_003535.json:
```json
{
    "body": "Attachment [mq-change_ring-bugfix.patch](tarball://root/attachments/some-uuid/ticket681/mq-change_ring-bugfix.patch) by mhansen created at 2007-09-20 00:39:41",
    "created_at": "2007-09-20T00:39:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/681",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/681#issuecomment-3535",
    "user": "mhansen"
}
```

Attachment [mq-change_ring-bugfix.patch](tarball://root/attachments/some-uuid/ticket681/mq-change_ring-bugfix.patch) by mhansen created at 2007-09-20 00:39:41



---

archive/issue_comments_003536.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-09-21T01:55:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/681",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/681#issuecomment-3536",
    "user": "was"
}
```

Resolution: fixed
