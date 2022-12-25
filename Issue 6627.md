# Issue 6627: lyndon and standard factorization of words is broken

archive/issues_006627.json:
```json
{
    "body": "Assignee: @saliola\n\nCC:  @seblabbe\n\nThe last 1 in the word disappeared:\n\n```\nsage: Word([1,2,1,3,1,2,1]).lyndon_factorization()\n(1213.12)\n```\n\nLyndon factorization of the empty word should work.\n\n```\nsage: Words('01')('').lyndon_factorization()\nTraceback (most recent call last):\n...\nStopIteration\n```\n\nThe standard factorization of 321 is 32.1.\n\n```\nsage: sage: Word([3,2,1]).standard_factorization()\n(321.)\n``` \n\nThe standard factorization of the empty word should return the empty word, and not two copies of the empty word. \n\n```\nsage: Words('123')('').standard_factorization()\n(.)\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/6627\n\n",
    "created_at": "2009-07-26T09:54:18Z",
    "labels": [
        "component: combinatorics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.2",
    "title": "lyndon and standard factorization of words is broken",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6627",
    "user": "https://github.com/saliola"
}
```
Assignee: @saliola

CC:  @seblabbe

The last 1 in the word disappeared:

```
sage: Word([1,2,1,3,1,2,1]).lyndon_factorization()
(1213.12)
```

Lyndon factorization of the empty word should work.

```
sage: Words('01')('').lyndon_factorization()
Traceback (most recent call last):
...
StopIteration
```

The standard factorization of 321 is 32.1.

```
sage: sage: Word([3,2,1]).standard_factorization()
(321.)
``` 

The standard factorization of the empty word should return the empty word, and not two copies of the empty word. 

```
sage: Words('123')('').standard_factorization()
(.)
```

Issue created by migration from https://trac.sagemath.org/ticket/6627





---

archive/issue_comments_054188.json:
```json
{
    "body": "Attachment [trac_6627-lyndon_words_fix.patch](tarball://root/attachments/some-uuid/ticket6627/trac_6627-lyndon_words_fix.patch) by @saliola created at 2009-07-26 12:01:30\n\nbased on sage-4.1.1.alpha0",
    "created_at": "2009-07-26T12:01:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6627",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6627#issuecomment-54188",
    "user": "https://github.com/saliola"
}
```

Attachment [trac_6627-lyndon_words_fix.patch](tarball://root/attachments/some-uuid/ticket6627/trac_6627-lyndon_words_fix.patch) by @saliola created at 2009-07-26 12:01:30

based on sage-4.1.1.alpha0



---

archive/issue_comments_054189.json:
```json
{
    "body": "This new implementation is correct and also faster.\n\n```\nsage: sage: Word([1,2,1,3,1,2,1]).lyndon_factorization()\n(1213, 12, 1)\nsage: sage: Words('01')('').lyndon_factorization()\n()\nsage: sage: sage: Word([3,2,1]).standard_factorization()\n(32, 1)\nsage: sage: Words('123')('').standard_factorization()\n()\n```\n\nI also changed the repr of the (word) Factorization class to use ',' instead of '.' because otherwise the period is confusing if you factor a long word:\n\n```\nsage: WordOptions(truncate_length=10)\nsage: tm = words.ThueMorseWord()\nsage: tm[:100].lyndon_factorization()\n(011, 01, 0011, 00101101, 0010110011..., 0010110011..., 0010110011..., 0010110011, 0)\n```",
    "created_at": "2009-07-26T12:11:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6627",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6627#issuecomment-54189",
    "user": "https://github.com/saliola"
}
```

This new implementation is correct and also faster.

```
sage: sage: Word([1,2,1,3,1,2,1]).lyndon_factorization()
(1213, 12, 1)
sage: sage: Words('01')('').lyndon_factorization()
()
sage: sage: sage: Word([3,2,1]).standard_factorization()
(32, 1)
sage: sage: Words('123')('').standard_factorization()
()
```

I also changed the repr of the (word) Factorization class to use ',' instead of '.' because otherwise the period is confusing if you factor a long word:

```
sage: WordOptions(truncate_length=10)
sage: tm = words.ThueMorseWord()
sage: tm[:100].lyndon_factorization()
(011, 01, 0011, 00101101, 0010110011..., 0010110011..., 0010110011..., 0010110011, 0)
```



---

archive/issue_comments_054190.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-08-24T23:54:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6627",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6627#issuecomment-54190",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed



---

archive/issue_events_015642.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2009-08-24T23:54:20Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6627",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6627#event-15642"
}
```



---

archive/issue_events_015643.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2009-08-25T00:32:24Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6627",
    "milestone": "sage-4.1.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6627#event-15643"
}
```
