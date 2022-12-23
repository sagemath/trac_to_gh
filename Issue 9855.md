# Issue 9855: improve `augment` method for sparse matrices

archive/issues_009855.json:
```json
{
    "body": "Assignee: jason, was\n\nCC:  zimmerma\n\nsee #7199 for a patch improving `stack`.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9856\n\n",
    "created_at": "2010-09-04T20:27:21Z",
    "labels": [
        "linear algebra",
        "major",
        "enhancement"
    ],
    "title": "improve `augment` method for sparse matrices",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9855",
    "user": "ylchapuy"
}
```
Assignee: jason, was

CC:  zimmerma

see #7199 for a patch improving `stack`.

Issue created by migration from https://trac.sagemath.org/ticket/9856





---

archive/issue_comments_097283.json:
```json
{
    "body": "Attachment\n\nPatch based on sage 4.5.3 + #7199 (but I don't know if it depends on it).\nPaul, as you did such a good job reviewing the other ticket, I cc'd you.",
    "created_at": "2010-09-22T08:44:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9855",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9855#issuecomment-97283",
    "user": "ylchapuy"
}
```

Attachment

Patch based on sage 4.5.3 + #7199 (but I don't know if it depends on it).
Paul, as you did such a good job reviewing the other ticket, I cc'd you.



---

archive/issue_comments_097284.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-09-22T08:44:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9855",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9855#issuecomment-97284",
    "user": "ylchapuy"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_097285.json:
```json
{
    "body": "> Paul, as you did such a good job reviewing the other ticket, I cc'd you.\n\nYann, please could you provide a description saying in what sense you did \"improve\"\naugment, maybe with an example? Is that an improvement in functionality or speed?\n\nPaul",
    "created_at": "2010-09-22T09:52:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9855",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9855#issuecomment-97285",
    "user": "zimmerma"
}
```

> Paul, as you did such a good job reviewing the other ticket, I cc'd you.

Yann, please could you provide a description saying in what sense you did "improve"
augment, maybe with an example? Is that an improvement in functionality or speed?

Paul



---

archive/issue_comments_097286.json:
```json
{
    "body": "Changing status from needs_review to needs_info.",
    "created_at": "2010-09-22T09:52:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9855",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9855#issuecomment-97286",
    "user": "zimmerma"
}
```

Changing status from needs_review to needs_info.



---

archive/issue_comments_097287.json:
```json
{
    "body": "It's a speed improvement. Here's the example:\n\n\n```\nsage: m = identity_matrix(QQ, 1000, sparse=True)\nsage: timeit('m.augment(m)')\n```\n\n\nBEFORE\n\n```\n5 loops, best of 3: 368 ms per loop\n```\n\nAFTER\n\n```\n625 loops, best of 3: 1.2 ms per loop\n```\n\n\nAnd we are not loosing anything for small cases:\n\n```\nsage: m = identity_matrix(QQ, 5, sparse=True)  \nsage: timeit('m.augment(m)')\n```\n\n\nBEFORE\n\n```\n625 loops, best of 3: 198 \u00b5s per loop\n```\n\nAFTER\n\n```\n625 loops, best of 3: 197 \u00b5s per loop\n```\n",
    "created_at": "2010-09-22T11:43:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9855",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9855#issuecomment-97287",
    "user": "ylchapuy"
}
```

It's a speed improvement. Here's the example:


```
sage: m = identity_matrix(QQ, 1000, sparse=True)
sage: timeit('m.augment(m)')
```


BEFORE

```
5 loops, best of 3: 368 ms per loop
```

AFTER

```
625 loops, best of 3: 1.2 ms per loop
```


And we are not loosing anything for small cases:

```
sage: m = identity_matrix(QQ, 5, sparse=True)  
sage: timeit('m.augment(m)')
```


BEFORE

```
625 loops, best of 3: 198 µs per loop
```

AFTER

```
625 loops, best of 3: 197 µs per loop
```




---

archive/issue_comments_097288.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2010-09-22T11:43:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9855",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9855#issuecomment-97288",
    "user": "ylchapuy"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_097289.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-09-22T19:49:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9855",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9855#issuecomment-97289",
    "user": "zimmerma"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_097290.json:
```json
{
    "body": "A small typo in the code: \"number of columns must be the same\" should be\n\"number of rows must be the same\". I confirm the great speed improvement.\nOnce the typo is fixed, I will check the doctests still pass.\n\nPaul",
    "created_at": "2010-09-22T19:49:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9855",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9855#issuecomment-97290",
    "user": "zimmerma"
}
```

A small typo in the code: "number of columns must be the same" should be
"number of rows must be the same". I confirm the great speed improvement.
Once the typo is fixed, I will check the doctests still pass.

Paul



---

archive/issue_comments_097291.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-09-23T00:28:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9855",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9855#issuecomment-97291",
    "user": "ylchapuy"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_097292.json:
```json
{
    "body": "Attachment\n\nNice spot, typo fixed. Apply both patches.\n\n    Yann",
    "created_at": "2010-09-23T00:28:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9855",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9855#issuecomment-97292",
    "user": "ylchapuy"
}
```

Attachment

Nice spot, typo fixed. Apply both patches.

    Yann



---

archive/issue_comments_097293.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-09-24T20:04:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9855",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9855#issuecomment-97293",
    "user": "zimmerma"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_097294.json:
```json
{
    "body": "good work once again, Yann!\n\nPaul",
    "created_at": "2010-09-24T20:04:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9855",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9855#issuecomment-97294",
    "user": "zimmerma"
}
```

good work once again, Yann!

Paul



---

archive/issue_comments_097295.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-09-28T10:58:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9855",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9855#issuecomment-97295",
    "user": "mpatel"
}
```

Resolution: fixed
