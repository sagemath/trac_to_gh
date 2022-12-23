# Issue 1935: [with patch, needs review] legendre_symbol currently quite slow

archive/issues_001935.json:
```json
{
    "body": "Assignee: craigcitro\n\nThe legendre_symbol command is pretty slow; this patch speeds it up a good bit. Here are some timings:\n\nBEFORE:\n\n```\nsage: time for _ in range(10000): a = legendre_symbol(12,5)\nCPU times: user 0.46 s, sys: 0.05 s, total: 0.52 s\nWall time: 0.52\n```\n\n\nAFTER:\n\n```\nsage: time for _ in range(10000): a = legendre_symbol(12,5)\nCPU times: user 0.11 s, sys: 0.02 s, total: 0.13 s\nWall time: 0.13\n```\n\n\nHowever, it's still *much* slower than kronecker_symbol:\n\n```\nsage: time for _ in range(10000): a = kronecker_symbol(12,5)\nCPU times: user 0.02 s, sys: 0.00 s, total: 0.02 s\nWall time: 0.02\n```\n\n\nHere's most of the discrepancy:\n\n```\nsage: time for _ in range(10000): 5.is_prime()\nCPU times: user 0.06 s, sys: 0.02 s, total: 0.08 s\nWall time: 0.08\n```\n\n\nIt's amusing, because there's no need for legendre_symbol to check whether or not its argument is prime, since under the hood it just calls kronecker. Of course, it would work when it shouldn't, which is probably bad. So this is a happy medium.\n\nI suspect that this is still wildly slower than Pari, Magma, etc -- indeed, Magma can do that calculation about 250,000 times in the same time frame. It's not wildly important, but moving arith.py to Cython could help close that gap.\n\nIssue created by migration from https://trac.sagemath.org/ticket/1935\n\n",
    "created_at": "2008-01-26T09:33:26Z",
    "labels": [
        "number theory",
        "minor",
        "bug"
    ],
    "title": "[with patch, needs review] legendre_symbol currently quite slow",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1935",
    "user": "craigcitro"
}
```
Assignee: craigcitro

The legendre_symbol command is pretty slow; this patch speeds it up a good bit. Here are some timings:

BEFORE:

```
sage: time for _ in range(10000): a = legendre_symbol(12,5)
CPU times: user 0.46 s, sys: 0.05 s, total: 0.52 s
Wall time: 0.52
```


AFTER:

```
sage: time for _ in range(10000): a = legendre_symbol(12,5)
CPU times: user 0.11 s, sys: 0.02 s, total: 0.13 s
Wall time: 0.13
```


However, it's still *much* slower than kronecker_symbol:

```
sage: time for _ in range(10000): a = kronecker_symbol(12,5)
CPU times: user 0.02 s, sys: 0.00 s, total: 0.02 s
Wall time: 0.02
```


Here's most of the discrepancy:

```
sage: time for _ in range(10000): 5.is_prime()
CPU times: user 0.06 s, sys: 0.02 s, total: 0.08 s
Wall time: 0.08
```


It's amusing, because there's no need for legendre_symbol to check whether or not its argument is prime, since under the hood it just calls kronecker. Of course, it would work when it shouldn't, which is probably bad. So this is a happy medium.

I suspect that this is still wildly slower than Pari, Magma, etc -- indeed, Magma can do that calculation about 250,000 times in the same time frame. It's not wildly important, but moving arith.py to Cython could help close that gap.

Issue created by migration from https://trac.sagemath.org/ticket/1935





---

archive/issue_comments_012277.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-01-26T09:34:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1935",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1935#issuecomment-12277",
    "user": "craigcitro"
}
```

Attachment



---

archive/issue_comments_012278.json:
```json
{
    "body": "The patch looks good to me.\n\nCheers,\n\nMichael",
    "created_at": "2008-01-26T09:47:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1935",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1935#issuecomment-12278",
    "user": "mabshoff"
}
```

The patch looks good to me.

Cheers,

Michael



---

archive/issue_comments_012279.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-26T11:15:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1935",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1935#issuecomment-12279",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_012280.json:
```json
{
    "body": "Merged in Sage 2.10.1.rc0",
    "created_at": "2008-01-26T11:15:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1935",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1935#issuecomment-12280",
    "user": "mabshoff"
}
```

Merged in Sage 2.10.1.rc0
