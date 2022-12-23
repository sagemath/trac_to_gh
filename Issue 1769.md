# Issue 1769: [with patch] Fast Pari <--> Sage p-adic capped relative element conversions

archive/issues_001769.json:
```json
{
    "body": "Assignee: craigcitro\n\nI think the title pretty much says it all: I made the conversion back and forth between  t_PADIC and pAdicCappedRelativeElement significantly faster. Here are some timings:\n\nBEFORE:\n\n```\nsage: R = Zp(5) ; x = R(123123123153)\n\nsage: time for _ in range(30000): y = x._pari_()\nCPU times: user 1.56 s, sys: 0.32 s, total: 1.88 s\nWall time: 2.09\n\nsage: time for _ in range(30000): y = pari(x)\nCPU times: user 1.62 s, sys: 0.32 s, total: 1.94 s\nWall time: 2.10\n\nsage: time for _ in range(30000): z = R(y)\nCPU times: user 2.91 s, sys: 0.23 s, total: 3.14 s\nWall time: 3.40\n\nsage: z == x\n True\n```\n\n\nAFTER:\n\n```\nsage: R = Zp(5) ; x = R(123123123153)\n\nsage: time for _ in range(30000): y = x._pari_()\nCPU times: user 0.19 s, sys: 0.10 s, total: 0.29 s\nWall time: 0.32\n\nsage: time for _ in range(30000): y = pari(x)\nCPU times: user 0.28 s, sys: 0.11 s, total: 0.39 s\nWall time: 0.43\n\nsage: time for _ in range(30000): z = R(y)\nCPU times: user 0.98 s, sys: 0.01 s, total: 0.98 s\nWall time: 1.11\n\nsage: z == x\n True\n```\n\n\nIt's roughly 6-6.5X faster from Sage to Pari, and 3X faster in the other direction. I also got another 15-20% out of t_INT --> pAdicCappedRelativeElement conversions:\n\nBEFORE:\n\n```\nsage: R = Zp(5) ; x = pari(987987987344)\n\nsage: time for _ in range(30000): y = R(x)\nCPU times: user 1.14 s, sys: 0.09 s, total: 1.23 s\nWall time: 1.34\n```\n\n\nAFTER:\n\n```\nsage: R = Zp(5) ; x = pari(987987987344)\n\nsage: time for _ in range(30000): y = R(x)\nCPU times: user 0.97 s, sys: 0.09 s, total: 1.06 s\nWall time: 1.15\n```\n\n\nI'm going to file a ticket in a moment to do the same for capped-abs and fixedmod types, because I don't feel like doing it right now, and someone could probably roughly copy-paste what I did in those cases without any knowledge of the Pari side of things.\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1769\n\n",
    "created_at": "2008-01-14T02:18:08Z",
    "labels": [
        "interfaces",
        "major",
        "enhancement"
    ],
    "title": "[with patch] Fast Pari <--> Sage p-adic capped relative element conversions",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1769",
    "user": "craigcitro"
}
```
Assignee: craigcitro

I think the title pretty much says it all: I made the conversion back and forth between  t_PADIC and pAdicCappedRelativeElement significantly faster. Here are some timings:

BEFORE:

```
sage: R = Zp(5) ; x = R(123123123153)

sage: time for _ in range(30000): y = x._pari_()
CPU times: user 1.56 s, sys: 0.32 s, total: 1.88 s
Wall time: 2.09

sage: time for _ in range(30000): y = pari(x)
CPU times: user 1.62 s, sys: 0.32 s, total: 1.94 s
Wall time: 2.10

sage: time for _ in range(30000): z = R(y)
CPU times: user 2.91 s, sys: 0.23 s, total: 3.14 s
Wall time: 3.40

sage: z == x
 True
```


AFTER:

```
sage: R = Zp(5) ; x = R(123123123153)

sage: time for _ in range(30000): y = x._pari_()
CPU times: user 0.19 s, sys: 0.10 s, total: 0.29 s
Wall time: 0.32

sage: time for _ in range(30000): y = pari(x)
CPU times: user 0.28 s, sys: 0.11 s, total: 0.39 s
Wall time: 0.43

sage: time for _ in range(30000): z = R(y)
CPU times: user 0.98 s, sys: 0.01 s, total: 0.98 s
Wall time: 1.11

sage: z == x
 True
```


It's roughly 6-6.5X faster from Sage to Pari, and 3X faster in the other direction. I also got another 15-20% out of t_INT --> pAdicCappedRelativeElement conversions:

BEFORE:

```
sage: R = Zp(5) ; x = pari(987987987344)

sage: time for _ in range(30000): y = R(x)
CPU times: user 1.14 s, sys: 0.09 s, total: 1.23 s
Wall time: 1.34
```


AFTER:

```
sage: R = Zp(5) ; x = pari(987987987344)

sage: time for _ in range(30000): y = R(x)
CPU times: user 0.97 s, sys: 0.09 s, total: 1.06 s
Wall time: 1.15
```


I'm going to file a ticket in a moment to do the same for capped-abs and fixedmod types, because I don't feel like doing it right now, and someone could probably roughly copy-paste what I did in those cases without any knowledge of the Pari side of things.



Issue created by migration from https://trac.sagemath.org/ticket/1769





---

archive/issue_comments_011191.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-01-14T02:37:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1769",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1769#issuecomment-11191",
    "user": "craigcitro"
}
```

Changing status from new to assigned.



---

archive/issue_comments_011192.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-01-14T02:37:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1769",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1769#issuecomment-11192",
    "user": "craigcitro"
}
```

Attachment



---

archive/issue_comments_011193.json:
```json
{
    "body": "Adding one more small patch, that adds one initialization line that David Roe pointed out I forgot. The two patches should be applied in order.",
    "created_at": "2008-01-14T12:34:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1769",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1769#issuecomment-11193",
    "user": "craigcitro"
}
```

Adding one more small patch, that adds one initialization line that David Roe pointed out I forgot. The two patches should be applied in order.



---

archive/issue_comments_011194.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-01-14T22:28:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1769",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1769#issuecomment-11194",
    "user": "roed"
}
```

Attachment



---

archive/issue_comments_011195.json:
```json
{
    "body": "Looks good to me too.",
    "created_at": "2008-01-15T06:10:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1769",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1769#issuecomment-11195",
    "user": "robertwb"
}
```

Looks good to me too.



---

archive/issue_comments_011196.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-15T06:15:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1769",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1769#issuecomment-11196",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_011197.json:
```json
{
    "body": "Both patches merged in Sage 2.10.alpha3",
    "created_at": "2008-01-15T06:15:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1769",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1769#issuecomment-11197",
    "user": "mabshoff"
}
```

Both patches merged in Sage 2.10.alpha3
