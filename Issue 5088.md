# Issue 5088: [with patch, needs review] use Pohlig-Hellman for generic discrete logarithm

archive/issues_005088.json:
```json
{
    "body": "Assignee: somebody\n\nAlgorithm summary:\nhttp://en.wikipedia.org/wiki/Pohlig-Hellman_algorithm\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5088\n\n",
    "created_at": "2009-01-24T15:16:29Z",
    "labels": [
        "component: basic arithmetic"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "[with patch, needs review] use Pohlig-Hellman for generic discrete logarithm",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5088",
    "user": "https://trac.sagemath.org/admin/accounts/users/ylchapuy"
}
```
Assignee: somebody

Algorithm summary:
http://en.wikipedia.org/wiki/Pohlig-Hellman_algorithm


Issue created by migration from https://trac.sagemath.org/ticket/5088





---

archive/issue_comments_038690.json:
```json
{
    "body": "Attachment [trac-5088.patch](tarball://root/attachments/some-uuid/ticket5088/trac-5088.patch) by ylchapuy created at 2009-01-24 15:19:58",
    "created_at": "2009-01-24T15:19:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5088",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5088#issuecomment-38690",
    "user": "https://trac.sagemath.org/admin/accounts/users/ylchapuy"
}
```

Attachment [trac-5088.patch](tarball://root/attachments/some-uuid/ticket5088/trac-5088.patch) by ylchapuy created at 2009-01-24 15:19:58



---

archive/issue_comments_038691.json:
```json
{
    "body": "My patch include the Pohlig-Hellman algorithm, and also modified the arguments of discrete_log, the \"ord\" argument wasn't used as announced but as a bound.\n\nI also wonder why we keep an old_discrete_log, but this another story...",
    "created_at": "2009-01-24T15:25:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5088",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5088#issuecomment-38691",
    "user": "https://trac.sagemath.org/admin/accounts/users/ylchapuy"
}
```

My patch include the Pohlig-Hellman algorithm, and also modified the arguments of discrete_log, the "ord" argument wasn't used as announced but as a bound.

I also wonder why we keep an old_discrete_log, but this another story...



---

archive/issue_comments_038692.json:
```json
{
    "body": "Can you post some timings comparing your new code to sage before your new code...?",
    "created_at": "2009-01-24T15:44:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5088",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5088#issuecomment-38692",
    "user": "https://github.com/williamstein"
}
```

Can you post some timings comparing your new code to sage before your new code...?



---

archive/issue_comments_038693.json:
```json
{
    "body": "With a smooth order:\n\n```\nsage: factor(5^15-1)\n2^2 * 11 * 31 * 71 * 181 * 1741\n```\n\nBEFORE:\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nsage: F.<a>=GF(5^15)\nsage: g=F.gen()\nsage: u=g^123456789\nsage: time log(u,g)\nCPU times: user 271.39 s, sys: 4.72 s, total: 276.11 s\nWall time: 276.96 s\n123456789\nsage: get_memory_usage()\n378.21875\n```\n\nAFTER:\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nLoading Sage library. Current Mercurial branch is: yann\nsage: F.<a>=GF(5^15)\nsage: g=F.gen()\nsage: u=g^123456789\nsage: time log(u,g)\nCPU times: user 0.14 s, sys: 0.00 s, total: 0.14 s\nWall time: 0.16 s\n123456789\nsage: get_memory_usage()\n115.8984375\n```\n",
    "created_at": "2009-01-24T16:25:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5088",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5088#issuecomment-38693",
    "user": "https://trac.sagemath.org/admin/accounts/users/ylchapuy"
}
```

With a smooth order:

```
sage: factor(5^15-1)
2^2 * 11 * 31 * 71 * 181 * 1741
```

BEFORE:

```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: F.<a>=GF(5^15)
sage: g=F.gen()
sage: u=g^123456789
sage: time log(u,g)
CPU times: user 271.39 s, sys: 4.72 s, total: 276.11 s
Wall time: 276.96 s
123456789
sage: get_memory_usage()
378.21875
```

AFTER:

```
----------------------------------------------------------------------
----------------------------------------------------------------------
Loading Sage library. Current Mercurial branch is: yann
sage: F.<a>=GF(5^15)
sage: g=F.gen()
sage: u=g^123456789
sage: time log(u,g)
CPU times: user 0.14 s, sys: 0.00 s, total: 0.14 s
Wall time: 0.16 s
123456789
sage: get_memory_usage()
115.8984375
```




---

archive/issue_comments_038694.json:
```json
{
    "body": "NICE!",
    "created_at": "2009-01-24T16:38:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5088",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5088#issuecomment-38694",
    "user": "https://github.com/williamstein"
}
```

NICE!



---

archive/issue_comments_038695.json:
```json
{
    "body": "and a not so smooth example\n\n```\nsage:factor(3^13-1)\n2 * 797161\n```\n\nBEFORE:\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nsage: F.<a>=GF(3**13)\nsage: g=F.gen()\nsage: u=g^1234567\nsage: timeit('log(u,g)')\n5 loops, best of 3: 1.54 s per loop\nsage: get_memory_usage()\n155.11328125\n```\n\nAFTER:\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nLoading Sage library. Current Mercurial branch is: yann\nsage: F.<a>=GF(3**13)\nsage: g=F.gen()\nsage: u=g^1234567\nsage: timeit('log(u,g)')\n5 loops, best of 3: 931 ms per loop\nsage: get_memory_usage()\n139.4296875\n```\n",
    "created_at": "2009-01-24T16:44:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5088",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5088#issuecomment-38695",
    "user": "https://trac.sagemath.org/admin/accounts/users/ylchapuy"
}
```

and a not so smooth example

```
sage:factor(3^13-1)
2 * 797161
```

BEFORE:

```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: F.<a>=GF(3**13)
sage: g=F.gen()
sage: u=g^1234567
sage: timeit('log(u,g)')
5 loops, best of 3: 1.54 s per loop
sage: get_memory_usage()
155.11328125
```

AFTER:

```
----------------------------------------------------------------------
----------------------------------------------------------------------
Loading Sage library. Current Mercurial branch is: yann
sage: F.<a>=GF(3**13)
sage: g=F.gen()
sage: u=g^1234567
sage: timeit('log(u,g)')
5 loops, best of 3: 931 ms per loop
sage: get_memory_usage()
139.4296875
```




---

archive/issue_comments_038696.json:
```json
{
    "body": "I am very pleased that someone is as interested as I am in improving this!  The original discrete log was wriiten by Stin & Joiner i think;  I rewrote it to work more generaically using the generic bsgs code;  I left the old code in through squaemishness about deleting what other people have written, that's all.\n\nCan I clarify what the changes you have made are doing?   You are still using BSGS to find dlogs in a cyclic group, but instead of doing one big computation in the whole group, you factor the order and do it in each p-primary subgroup separately.  If so, that sounds very sensible, but I think it would be a good idea to cache the group order's factorization so that the factorization is not repeated on subsequent calls.  The only way I can see of doing that is to have  the base element (which might be additive or multiplicative) cache both its own order and the factorization of that order.\n\nThe next improvement we need is to replace the BSGS by something which takes less memory, but that's not a reason for delaying this patch.\n\nI have not reviewed this yet, only looked at the patch code, but will do.",
    "created_at": "2009-01-24T17:36:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5088",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5088#issuecomment-38696",
    "user": "https://github.com/JohnCremona"
}
```

I am very pleased that someone is as interested as I am in improving this!  The original discrete log was wriiten by Stin & Joiner i think;  I rewrote it to work more generaically using the generic bsgs code;  I left the old code in through squaemishness about deleting what other people have written, that's all.

Can I clarify what the changes you have made are doing?   You are still using BSGS to find dlogs in a cyclic group, but instead of doing one big computation in the whole group, you factor the order and do it in each p-primary subgroup separately.  If so, that sounds very sensible, but I think it would be a good idea to cache the group order's factorization so that the factorization is not repeated on subsequent calls.  The only way I can see of doing that is to have  the base element (which might be additive or multiplicative) cache both its own order and the factorization of that order.

The next improvement we need is to replace the BSGS by something which takes less memory, but that's not a reason for delaying this patch.

I have not reviewed this yet, only looked at the patch code, but will do.



---

archive/issue_events_011743.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-01-24T18:07:59Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5088",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5088#event-11743"
}
```



---

archive/issue_comments_038697.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-24T18:07:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5088",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5088#issuecomment-38697",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_038698.json:
```json
{
    "body": "John: William already gave this a positive review.\n\nMerged in Sage 3.3.alpha2\n\nCheers,\n\nMichael",
    "created_at": "2009-01-24T18:07:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5088",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5088#issuecomment-38698",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

John: William already gave this a positive review.

Merged in Sage 3.3.alpha2

Cheers,

Michael



---

archive/issue_comments_038699.json:
```json
{
    "body": "Replying to [comment:7 mabshoff]:\n> John: William already gave this a positive review.\n\nOK, I saw that after saying I would do it.  I did have two doctest failures but they seem to be unrelated since they also fail in my unpatched main branch, and are probably due to the messed up upgrade.\n\n> \n> Merged in Sage 3.3.alpha2\n> \n> Cheers,\n> \n> Michael",
    "created_at": "2009-01-24T18:15:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5088",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5088#issuecomment-38699",
    "user": "https://github.com/JohnCremona"
}
```

Replying to [comment:7 mabshoff]:
> John: William already gave this a positive review.

OK, I saw that after saying I would do it.  I did have two doctest failures but they seem to be unrelated since they also fail in my unpatched main branch, and are probably due to the messed up upgrade.

> 
> Merged in Sage 3.3.alpha2
> 
> Cheers,
> 
> Michael



---

archive/issue_comments_038700.json:
```json
{
    "body": "Changing keywords from \"\" to \"discrete logarithm, speedup\".",
    "created_at": "2020-10-20T23:49:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5088",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5088#issuecomment-38700",
    "user": "https://github.com/slel"
}
```

Changing keywords from "" to "discrete logarithm, speedup".



---

archive/issue_comments_038701.json:
```json
{
    "body": "This ticket is mentioned in this video (from 00:17:00 to 00:22:27):\n\n- https://www.microsoft.com/en-us/research/video/the-sage-mathematical-software-project",
    "created_at": "2020-10-20T23:49:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5088",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5088#issuecomment-38701",
    "user": "https://github.com/slel"
}
```

This ticket is mentioned in this video (from 00:17:00 to 00:22:27):

- https://www.microsoft.com/en-us/research/video/the-sage-mathematical-software-project
