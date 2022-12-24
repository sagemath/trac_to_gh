# Issue 6565: substitution cryptosystems: converting a key from alphabetic to numerical values

archive/issues_006565.json:
```json
{
    "body": "Assignee: somebody\n\nKeywords: substitution cryptosystem\n\nThe class `SubstitutionCryptosystem` accepts keys whose values are alphabetic characters. We should implement a method to allow a key\nto be converted between alphabetic characters and numerical values. For example, here is what I have in mind:\n\n```\nsage: A = AlphabeticStrings()\nsage: S = SubstitutionCryptosystem(A)\nsage: key = S.random_key()\nABC\nsage: S.alphabet_to_numbers(key)\n012\nsage: S.numbers_to_alphabet([0, 1, 2])\nABC\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6565\n\n",
    "created_at": "2009-07-20T11:49:03Z",
    "labels": [
        "cryptography",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "substitution cryptosystems: converting a key from alphabetic to numerical values",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6565",
    "user": "mvngu"
}
```
Assignee: somebody

Keywords: substitution cryptosystem

The class `SubstitutionCryptosystem` accepts keys whose values are alphabetic characters. We should implement a method to allow a key
to be converted between alphabetic characters and numerical values. For example, here is what I have in mind:

```
sage: A = AlphabeticStrings()
sage: S = SubstitutionCryptosystem(A)
sage: key = S.random_key()
ABC
sage: S.alphabet_to_numbers(key)
012
sage: S.numbers_to_alphabet([0, 1, 2])
ABC
```


Issue created by migration from https://trac.sagemath.org/ticket/6565





---

archive/issue_comments_053556.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2015-05-26T19:01:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6565",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6565#issuecomment-53556",
    "user": "@tscholl2"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_053557.json:
```json
{
    "body": "I think it would be better to add some kind of conversion/coercion for string monoids instead of specifically for substitution cryptosystem strings. Also I don't believe there is an ASCII/byte value monoid. In either case, that would be a different ticket (see #9118). If someone still wants that they should open a new ticket.\n\nThis is also pretty easy to do by hand if someone wants to. For example, to take and element from an alphabetic monoid to a list of ascii values you can use this:\n\n```\n    sage: A = AlphabeticStrings()\n    sage: a = A.encoding(\"THISISATURTLE\")\n    sage: map(lambda x: ord(str(x)),a)\n    [84, 72, 73, 83, 73, 83, 65, 84, 85, 82, 84, 76, 69]\n```\n\n\nI'm going to set this as won't fix and give it positive review.",
    "created_at": "2015-05-26T19:01:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6565",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6565#issuecomment-53557",
    "user": "@tscholl2"
}
```

I think it would be better to add some kind of conversion/coercion for string monoids instead of specifically for substitution cryptosystem strings. Also I don't believe there is an ASCII/byte value monoid. In either case, that would be a different ticket (see #9118). If someone still wants that they should open a new ticket.

This is also pretty easy to do by hand if someone wants to. For example, to take and element from an alphabetic monoid to a list of ascii values you can use this:

```
    sage: A = AlphabeticStrings()
    sage: a = A.encoding("THISISATURTLE")
    sage: map(lambda x: ord(str(x)),a)
    [84, 72, 73, 83, 73, 83, 65, 84, 85, 82, 84, 76, 69]
```


I'm going to set this as won't fix and give it positive review.



---

archive/issue_comments_053558.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2015-05-26T19:02:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6565",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6565#issuecomment-53558",
    "user": "@tscholl2"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_053559.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2015-06-19T08:38:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6565",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6565#issuecomment-53559",
    "user": "@vbraun"
}
```

Resolution: wontfix
