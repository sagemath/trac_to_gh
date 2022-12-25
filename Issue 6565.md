# Issue 6565: substitution cryptosystems: converting a key from alphabetic to numerical values

archive/issues_006565.json:
```json
{
    "body": "Assignee: somebody\n\nKeywords: substitution cryptosystem\n\nThe class `SubstitutionCryptosystem` accepts keys whose values are alphabetic characters. We should implement a method to allow a key\nto be converted between alphabetic characters and numerical values. For example, here is what I have in mind:\n\n```\nsage: A = AlphabeticStrings()\nsage: S = SubstitutionCryptosystem(A)\nsage: key = S.random_key()\nABC\nsage: S.alphabet_to_numbers(key)\n012\nsage: S.numbers_to_alphabet([0, 1, 2])\nABC\n```\nGeneralizing from this, we can also have methods to do the following conversions:\n\n* from alphabetic characters to binary values and vice versa\n\n* from alphabetic characters to hexadecimal values and vice versa\n\n* from alphabetic characters to mod 26 values and vice versa\n\n* from alphabetic characters to ASCII values and vice versa\n\nIssue created by migration from https://trac.sagemath.org/ticket/6565\n\n",
    "closed_at": "2015-06-19T08:38:23Z",
    "created_at": "2009-07-20T11:49:03Z",
    "labels": [
        "component: cryptography"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "substitution cryptosystems: converting a key from alphabetic to numerical values",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6565",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
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
Generalizing from this, we can also have methods to do the following conversions:

* from alphabetic characters to binary values and vice versa

* from alphabetic characters to hexadecimal values and vice versa

* from alphabetic characters to mod 26 values and vice versa

* from alphabetic characters to ASCII values and vice versa

Issue created by migration from https://trac.sagemath.org/ticket/6565





---

archive/issue_events_015483.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6565",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6565#event-15483"
}
```



---

archive/issue_events_015484.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6565",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6565#event-15484"
}
```



---

archive/issue_events_015485.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6565",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6565#event-15485"
}
```



---

archive/issue_events_015486.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6565",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6565#event-15486"
}
```



---

archive/issue_events_015487.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6565",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6565#event-15487"
}
```



---

archive/issue_events_015488.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6565",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6565#event-15488"
}
```



---

archive/issue_events_015489.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6565",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6565#event-15489"
}
```



---

archive/issue_comments_053456.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2015-05-26T19:01:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6565",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6565#issuecomment-53456",
    "user": "https://github.com/tscholl2"
}
```

Changing status from new to needs_review.



---

archive/issue_events_015490.json:
```json
{
    "actor": "https://github.com/tscholl2",
    "created_at": "2015-05-26T19:01:50Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6565",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6565#event-15490"
}
```



---

archive/issue_events_015491.json:
```json
{
    "actor": "https://github.com/tscholl2",
    "created_at": "2015-05-26T19:01:50Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6565",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6565#event-15491"
}
```



---

archive/issue_comments_053457.json:
```json
{
    "body": "I think it would be better to add some kind of conversion/coercion for string monoids instead of specifically for substitution cryptosystem strings. Also I don't believe there is an ASCII/byte value monoid. In either case, that would be a different ticket (see #9118). If someone still wants that they should open a new ticket.\n\nThis is also pretty easy to do by hand if someone wants to. For example, to take and element from an alphabetic monoid to a list of ascii values you can use this:\n\n```\n    sage: A = AlphabeticStrings()\n    sage: a = A.encoding(\"THISISATURTLE\")\n    sage: map(lambda x: ord(str(x)),a)\n    [84, 72, 73, 83, 73, 83, 65, 84, 85, 82, 84, 76, 69]\n```\n\nI'm going to set this as won't fix and give it positive review.",
    "created_at": "2015-05-26T19:01:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6565",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6565#issuecomment-53457",
    "user": "https://github.com/tscholl2"
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

archive/issue_comments_053458.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2015-05-26T19:02:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6565",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6565#issuecomment-53458",
    "user": "https://github.com/tscholl2"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_053459.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2015-06-19T08:38:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6565",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6565#issuecomment-53459",
    "user": "https://github.com/vbraun"
}
```

Resolution: wontfix



---

archive/issue_events_015492.json:
```json
{
    "actor": "https://github.com/vbraun",
    "created_at": "2015-06-19T08:38:23Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6565",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6565#event-15492"
}
```
