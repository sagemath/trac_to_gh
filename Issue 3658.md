# Issue 3658: A PARI bug results in an unreliable prime_pi

archive/issues_003658.json:
```json
{
    "body": "Assignee: @williamstein\n\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n| SAGE Version 3.0.5, Release Date: 2008-07-11                       |\n| Type notebook() for the GUI, and license() for information.        |\nsage: [prime_pi(n) for n in [500508..500510]]\n[41580, 45056, 41581]\nsage: [prime_pi(n) for n in [500508..500510]]\n[41580, 41581, 41581]\n```\n\n\nThe problem lies with pari/gp:\n\n```\nsage: %gp\n\n  --> Switching to GP/PARI interpreter <-- \n\n''\ngp: for(n=500508, 500510, print(primepi(n)))\n\n41580\n45056\n  *** primepi: not enough precomputed primes, need primelimit ~ 500510.\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3658\n\n",
    "created_at": "2008-07-15T20:50:50Z",
    "labels": [
        "component: number theory",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "A PARI bug results in an unreliable prime_pi",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3658",
    "user": "https://trac.sagemath.org/admin/accounts/users/fwclarke"
}
```
Assignee: @williamstein


```
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 3.0.5, Release Date: 2008-07-11                       |
| Type notebook() for the GUI, and license() for information.        |
sage: [prime_pi(n) for n in [500508..500510]]
[41580, 45056, 41581]
sage: [prime_pi(n) for n in [500508..500510]]
[41580, 41581, 41581]
```


The problem lies with pari/gp:

```
sage: %gp

  --> Switching to GP/PARI interpreter <-- 

''
gp: for(n=500508, 500510, print(primepi(n)))

41580
45056
  *** primepi: not enough precomputed primes, need primelimit ~ 500510.
```


Issue created by migration from https://trac.sagemath.org/ticket/3658





---

archive/issue_comments_025802.json:
```json
{
    "body": "Changing assignee from @williamstein to @craigcitro.",
    "created_at": "2009-01-23T14:21:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3658",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3658#issuecomment-25802",
    "user": "https://github.com/craigcitro"
}
```

Changing assignee from @williamstein to @craigcitro.



---

archive/issue_comments_025803.json:
```json
{
    "body": "The attached patch fixes the issue. This was a strange case -- in some cases, Pari is more than happy to return an (incorrect!) answer when you call `primepi` with a number larger than the prime limit. This patch fixes this in a uniform way.",
    "created_at": "2009-01-23T14:21:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3658",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3658#issuecomment-25803",
    "user": "https://github.com/craigcitro"
}
```

The attached patch fixes the issue. This was a strange case -- in some cases, Pari is more than happy to return an (incorrect!) answer when you call `primepi` with a number larger than the prime limit. This patch fixes this in a uniform way.



---

archive/issue_comments_025804.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-01-23T14:21:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3658",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3658#issuecomment-25804",
    "user": "https://github.com/craigcitro"
}
```

Changing status from new to assigned.



---

archive/issue_comments_025805.json:
```json
{
    "body": "works for me",
    "created_at": "2009-01-24T10:39:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3658",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3658#issuecomment-25805",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

works for me



---

archive/issue_comments_025806.json:
```json
{
    "body": "On sage.math: oops:\n\n```\nsage -t -long \"devel/sage/sage/libs/pari/gen.pyx\"           \n**********************************************************************\nFile \"/scratch/mabshoff/sage-3.3.alpha2/devel/sage/sage/libs/pari/gen.pyx\", line 7400:\n    sage: pari._primelimit()\nExpected:\n    500000\nGot:\n    500519\n**********************************************************************\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2009-01-24T16:24:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3658",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3658#issuecomment-25806",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

On sage.math: oops:

```
sage -t -long "devel/sage/sage/libs/pari/gen.pyx"           
**********************************************************************
File "/scratch/mabshoff/sage-3.3.alpha2/devel/sage/sage/libs/pari/gen.pyx", line 7400:
    sage: pari._primelimit()
Expected:
    500000
Got:
    500519
**********************************************************************
```


Cheers,

Michael



---

archive/issue_comments_025807.json:
```json
{
    "body": "Attachment [trac-3658.patch](tarball://root/attachments/some-uuid/ticket3658/trac-3658.patch) by @craigcitro created at 2009-01-24 19:57:19",
    "created_at": "2009-01-24T19:57:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3658",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3658#issuecomment-25807",
    "user": "https://github.com/craigcitro"
}
```

Attachment [trac-3658.patch](tarball://root/attachments/some-uuid/ticket3658/trac-3658.patch) by @craigcitro created at 2009-01-24 19:57:19



---

archive/issue_comments_025808.json:
```json
{
    "body": "+1",
    "created_at": "2009-01-24T20:00:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3658",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3658#issuecomment-25808",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

+1



---

archive/issue_comments_025809.json:
```json
{
    "body": "Merged in Sage 3.3.alpha2.\n\nCheers,\n\nMichael",
    "created_at": "2009-01-24T23:00:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3658",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3658#issuecomment-25809",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.3.alpha2.

Cheers,

Michael



---

archive/issue_comments_025810.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-24T23:00:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3658",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3658#issuecomment-25810",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_003877.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2009-01-24T23:00:49Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3658",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3658#event-3877"
}
```
