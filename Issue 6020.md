# Issue 6020: [fixed by #6671] bug in delta_qexp over finite fields

archive/issues_006020.json:
```json
{
    "body": "Assignee: @craigcitro\n\nKeywords: delta q-expansion finite field\n\nThis is in sage-3.4.2:\n\n```\nsage: delta_qexp(K=GF(5))\nTypeError                                 Traceback (most recent call last)\n...\nTypeError: unable to coerce <type 'sage.libs.ntl.ntl_ZZX.ntl_ZZX'> to an integer\n```\n\nI don't have time to investigate this right now, but it might be a similar issue as #5102.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6020\n\n",
    "closed_at": "2010-04-15T05:56:20Z",
    "created_at": "2009-05-11T12:08:47Z",
    "labels": [
        "component: modular forms",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4",
    "title": "[fixed by #6671] bug in delta_qexp over finite fields",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6020",
    "user": "https://github.com/aghitza"
}
```
Assignee: @craigcitro

Keywords: delta q-expansion finite field

This is in sage-3.4.2:

```
sage: delta_qexp(K=GF(5))
TypeError                                 Traceback (most recent call last)
...
TypeError: unable to coerce <type 'sage.libs.ntl.ntl_ZZX.ntl_ZZX'> to an integer
```

I don't have time to investigate this right now, but it might be a similar issue as #5102.


Issue created by migration from https://trac.sagemath.org/ticket/6020





---

archive/issue_comments_047836.json:
```json
{
    "body": "Attachment [trac-6020.patch](tarball://root/attachments/some-uuid/ticket6020/trac-6020.patch) by @craigcitro created at 2009-05-11 17:00:36",
    "created_at": "2009-05-11T17:00:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6020",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6020#issuecomment-47836",
    "user": "https://github.com/craigcitro"
}
```

Attachment [trac-6020.patch](tarball://root/attachments/some-uuid/ticket6020/trac-6020.patch) by @craigcitro created at 2009-05-11 17:00:36



---

archive/issue_comments_047837.json:
```json
{
    "body": "Okay, I've attached a patch. The issue is that we can't coerce from NTL into a finite field.\n\nThis patch isn't anything too clever -- I just do the naive thing and work over the base ring from the start instead of using NTL. It runs at the same speed for `100000` terms, and only loses about `3%` performance at `1000000`, so this should definitely do the job. I'm happy to come back and either unify these (maybe we don't need to manually use NTL anymore?) or do some additional work to speed it up in the finite field case later on.",
    "created_at": "2009-05-11T17:03:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6020",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6020#issuecomment-47837",
    "user": "https://github.com/craigcitro"
}
```

Okay, I've attached a patch. The issue is that we can't coerce from NTL into a finite field.

This patch isn't anything too clever -- I just do the naive thing and work over the base ring from the start instead of using NTL. It runs at the same speed for `100000` terms, and only loses about `3%` performance at `1000000`, so this should definitely do the job. I'm happy to come back and either unify these (maybe we don't need to manually use NTL anymore?) or do some additional work to speed it up in the finite field case later on.



---

archive/issue_comments_047838.json:
```json
{
    "body": "Wait a minute:  \nChanging \n\n```\n if K is ZZ:\n```\nto\n\n```\n if False and K is ZZ:\n```\nresults in code that is way *faster*!  That's because FLINT kick's NTL's ass, and FLINT is the default for poly's over ZZ now.  Just get rid of the flint implementation.\n\nWith NTL (on my OS X laptop):\n\n```\nsage: time b = delta_qexp(50000)\nCPU times: user 0.44 s, sys: 0.00 s, total: 0.44 s\nWall time: 0.44 s\nsage: time b = delta_qexp(100000)\nCPU times: user 1.07 s, sys: 0.07 s, total: 1.14 s\nWall time: 1.14 s\nsage: time b = delta_qexp(200000)\nCPU times: user 2.65 s, sys: 0.06 s, total: 2.71 s\nWall time: 2.72 s\n```\n\nWith the \"False\" as above inserted, so FLINT gets used:\n\n```\nsage: time b = delta_qexp(50000)\nCPU times: user 0.21 s, sys: 0.08 s, total: 0.29 s\nWall time: 0.30 s\nsage: time b = delta_qexp(100000)\nCPU times: user 0.58 s, sys: 0.12 s, total: 0.70 s\nWall time: 0.70 s\nsage: time b = delta_qexp(200000)\nCPU times: user 1.35 s, sys: 0.33 s, total: 1.68 s\nWall time: 1.68 s\n```",
    "created_at": "2009-05-12T06:55:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6020",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6020#issuecomment-47838",
    "user": "https://github.com/williamstein"
}
```

Wait a minute:  
Changing 

```
 if K is ZZ:
```
to

```
 if False and K is ZZ:
```
results in code that is way *faster*!  That's because FLINT kick's NTL's ass, and FLINT is the default for poly's over ZZ now.  Just get rid of the flint implementation.

With NTL (on my OS X laptop):

```
sage: time b = delta_qexp(50000)
CPU times: user 0.44 s, sys: 0.00 s, total: 0.44 s
Wall time: 0.44 s
sage: time b = delta_qexp(100000)
CPU times: user 1.07 s, sys: 0.07 s, total: 1.14 s
Wall time: 1.14 s
sage: time b = delta_qexp(200000)
CPU times: user 2.65 s, sys: 0.06 s, total: 2.71 s
Wall time: 2.72 s
```

With the "False" as above inserted, so FLINT gets used:

```
sage: time b = delta_qexp(50000)
CPU times: user 0.21 s, sys: 0.08 s, total: 0.29 s
Wall time: 0.30 s
sage: time b = delta_qexp(100000)
CPU times: user 0.58 s, sys: 0.12 s, total: 0.70 s
Wall time: 0.70 s
sage: time b = delta_qexp(200000)
CPU times: user 1.35 s, sys: 0.33 s, total: 1.68 s
Wall time: 1.68 s
```



---

archive/issue_events_014141.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2009-05-12T06:55:14Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6020",
    "milestone": "sage-4.0",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6020#event-14141"
}
```



---

archive/issue_comments_047839.json:
```json
{
    "body": "This is pretty interesting: I get entirely different timings on my laptop, which is why I didn't remove the NTL code. I wonder if something funky went on with my FLINT compilation?\n\nThe `NTL` version:\n\n```\nsage: time b = delta_qexp(50000)\nCPU times: user 0.50 s, sys: 0.02 s, total: 0.52 s\nWall time: 0.53 s\n\nsage: time b = delta_qexp(100000)\nCPU times: user 1.04 s, sys: 0.04 s, total: 1.08 s\nWall time: 1.15 s\n\nsage: time b = delta_qexp(200000)\nCPU times: user 2.08 s, sys: 0.09 s, total: 2.18 s\nWall time: 2.20 s\n```\n\nThe `FLINT` version:\n\n```\nsage: time b = delta_qexp(50000)\nCPU times: user 1.01 s, sys: 0.35 s, total: 1.36 s\nWall time: 1.37 s\n\nsage: time b = delta_qexp(100000)\nCPU times: user 2.08 s, sys: 0.70 s, total: 2.78 s\nWall time: 2.81 s\n\nsage: time b = delta_qexp(200000)\nCPU times: user 4.34 s, sys: 1.46 s, total: 5.80 s\nWall time: 5.88 s\n```\n\nThat seems really weird ... I'm going to try looking at this tomorrow when I'm sitting next to you. This is kinda weird; I'd like to do some random timing comparisons.",
    "created_at": "2009-05-12T07:22:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6020",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6020#issuecomment-47839",
    "user": "https://github.com/craigcitro"
}
```

This is pretty interesting: I get entirely different timings on my laptop, which is why I didn't remove the NTL code. I wonder if something funky went on with my FLINT compilation?

The `NTL` version:

```
sage: time b = delta_qexp(50000)
CPU times: user 0.50 s, sys: 0.02 s, total: 0.52 s
Wall time: 0.53 s

sage: time b = delta_qexp(100000)
CPU times: user 1.04 s, sys: 0.04 s, total: 1.08 s
Wall time: 1.15 s

sage: time b = delta_qexp(200000)
CPU times: user 2.08 s, sys: 0.09 s, total: 2.18 s
Wall time: 2.20 s
```

The `FLINT` version:

```
sage: time b = delta_qexp(50000)
CPU times: user 1.01 s, sys: 0.35 s, total: 1.36 s
Wall time: 1.37 s

sage: time b = delta_qexp(100000)
CPU times: user 2.08 s, sys: 0.70 s, total: 2.78 s
Wall time: 2.81 s

sage: time b = delta_qexp(200000)
CPU times: user 4.34 s, sys: 1.46 s, total: 5.80 s
Wall time: 5.88 s
```

That seems really weird ... I'm going to try looking at this tomorrow when I'm sitting next to you. This is kinda weird; I'd like to do some random timing comparisons.



---

archive/issue_comments_047840.json:
```json
{
    "body": "On my 32-bit Linux laptop, I get these timings:\n\nWith NTL:\n\n```\nsage: sage: time b = delta_qexp(50000)\nCPU times: user 0.95 s, sys: 0.04 s, total: 0.99 s\nWall time: 1.01 s\nsage: sage: time b = delta_qexp(100000)\nCPU times: user 2.03 s, sys: 0.04 s, total: 2.06 s\nWall time: 2.08 s\nsage: sage: time b = delta_qexp(200000)\nCPU times: user 4.46 s, sys: 0.13 s, total: 4.59 s\nWall time: 4.91 s\n```\n\nWith FLINT, i.e. with the \"if False\" hack:\n\n```\nsage: sage: time b = delta_qexp(50000)\nCPU times: user 0.76 s, sys: 0.07 s, total: 0.83 s\nWall time: 0.85 s\nsage: sage: time b = delta_qexp(100000)\nCPU times: user 1.62 s, sys: 0.16 s, total: 1.78 s\nWall time: 1.79 s\nsage: sage: time b = delta_qexp(200000)\nCPU times: user 3.50 s, sys: 0.40 s, total: 3.91 s\nWall time: 4.03 s\n```\n\nSo FLINT is faster for me (but not by so much as for William).",
    "created_at": "2009-05-12T09:20:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6020",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6020#issuecomment-47840",
    "user": "https://github.com/loefflerd"
}
```

On my 32-bit Linux laptop, I get these timings:

With NTL:

```
sage: sage: time b = delta_qexp(50000)
CPU times: user 0.95 s, sys: 0.04 s, total: 0.99 s
Wall time: 1.01 s
sage: sage: time b = delta_qexp(100000)
CPU times: user 2.03 s, sys: 0.04 s, total: 2.06 s
Wall time: 2.08 s
sage: sage: time b = delta_qexp(200000)
CPU times: user 4.46 s, sys: 0.13 s, total: 4.59 s
Wall time: 4.91 s
```

With FLINT, i.e. with the "if False" hack:

```
sage: sage: time b = delta_qexp(50000)
CPU times: user 0.76 s, sys: 0.07 s, total: 0.83 s
Wall time: 0.85 s
sage: sage: time b = delta_qexp(100000)
CPU times: user 1.62 s, sys: 0.16 s, total: 1.78 s
Wall time: 1.79 s
sage: sage: time b = delta_qexp(200000)
CPU times: user 3.50 s, sys: 0.40 s, total: 3.91 s
Wall time: 4.03 s
```

So FLINT is faster for me (but not by so much as for William).



---

archive/issue_comments_047841.json:
```json
{
    "body": "What is the status here?\n\nCheers,\n\nMichael",
    "created_at": "2009-05-14T05:27:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6020",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6020#issuecomment-47841",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

What is the status here?

Cheers,

Michael



---

archive/issue_events_014142.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-05-14T05:27:10Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6020",
    "milestone": "sage-4.0",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6020#event-14142"
}
```



---

archive/issue_events_014143.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-05-14T05:27:10Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6020",
    "milestone": "sage-4.0.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6020#event-14143"
}
```



---

archive/issue_comments_047842.json:
```json
{
    "body": "I'm going to fix this soon, at SD15 if not before. (Me giving three talks during SD15 may prevent it from happening before.)\n\nHere's the status, though: we've discovered that on 64-bit OSX and on `sage.math`, it's much faster to just call the naive code (the `else` clause in the patch above. However, it's **slower** on 32-bit OSX. So I looked at the code a little more, and we're spending a fair amount of time doing silly things (coercion, poor use of truncation, etc.). So I'm going to make a new ticket with some fixes/additions to the polynomial code, and then rewrite this patch to use these improvements. I suspect that it'll beat the old code on all architectures in that case (I'm basing this on some rough timings on my laptop), in which case we're all set.\n\nI'm changing the status to something slightly snarky to summarize the above. :)",
    "created_at": "2009-05-14T05:56:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6020",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6020#issuecomment-47842",
    "user": "https://github.com/craigcitro"
}
```

I'm going to fix this soon, at SD15 if not before. (Me giving three talks during SD15 may prevent it from happening before.)

Here's the status, though: we've discovered that on 64-bit OSX and on `sage.math`, it's much faster to just call the naive code (the `else` clause in the patch above. However, it's **slower** on 32-bit OSX. So I looked at the code a little more, and we're spending a fair amount of time doing silly things (coercion, poor use of truncation, etc.). So I'm going to make a new ticket with some fixes/additions to the polynomial code, and then rewrite this patch to use these improvements. I suspect that it'll beat the old code on all architectures in that case (I'm basing this on some rough timings on my laptop), in which case we're all set.

I'm changing the status to something slightly snarky to summarize the above. :)



---

archive/issue_comments_047843.json:
```json
{
    "body": "As I said #6671 I merge this with the new code given there. I did some timings and the result is clear: Coercion into the new ring after using FLINT is fast.\nTimeing:\n\n```\nsage: P = PowerSeriesRing(GF(7), 'q')\nsage: from sage.modular.modform.vm_basis import _delta_poly\n\nsage: %timeit P(_delta_poly(50).list(), check = True)\n625 loops, best of 3: 407 \u00b5s per loop\nsage: %timeit _delta_poly(50, GF(7))\n625 loops, best of 3: 1.41 ms per loop\n\nsage: %timeit P(_delta_poly(10**5).list(), check = True)\n5 loops, best of 3: 620 ms per loop\nsage: %timeit _delta_poly(10**5, GF(7))\n5 loops, best of 3: 1.62 s per loop\n\nsage: %timeit h = P(_delta_poly(10**6).list(), check = True)\n5 loops, best of 3: 7.98 s per loop\nsage: %timeit h =_delta_poly(10**6, GF(7))\n5 loops, best of 3: 16.9 s per loop\n\n```\n\nI conclude that it is better to wait for Craig's new code. If nobody is opposed I will asked the current release manager (I think it's Minh) to make this as closed (since it is fixed by #6671).",
    "created_at": "2010-04-09T17:11:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6020",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6020#issuecomment-47843",
    "user": "https://trac.sagemath.org/admin/accounts/users/mraum"
}
```

As I said #6671 I merge this with the new code given there. I did some timings and the result is clear: Coercion into the new ring after using FLINT is fast.
Timeing:

```
sage: P = PowerSeriesRing(GF(7), 'q')
sage: from sage.modular.modform.vm_basis import _delta_poly

sage: %timeit P(_delta_poly(50).list(), check = True)
625 loops, best of 3: 407 µs per loop
sage: %timeit _delta_poly(50, GF(7))
625 loops, best of 3: 1.41 ms per loop

sage: %timeit P(_delta_poly(10**5).list(), check = True)
5 loops, best of 3: 620 ms per loop
sage: %timeit _delta_poly(10**5, GF(7))
5 loops, best of 3: 1.62 s per loop

sage: %timeit h = P(_delta_poly(10**6).list(), check = True)
5 loops, best of 3: 7.98 s per loop
sage: %timeit h =_delta_poly(10**6, GF(7))
5 loops, best of 3: 16.9 s per loop

```

I conclude that it is better to wait for Craig's new code. If nobody is opposed I will asked the current release manager (I think it's Minh) to make this as closed (since it is fixed by #6671).



---

archive/issue_comments_047844.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-04-12T14:10:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6020",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6020#issuecomment-47844",
    "user": "https://github.com/loefflerd"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_047845.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-04-12T14:11:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6020",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6020#issuecomment-47845",
    "user": "https://github.com/loefflerd"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_047846.json:
```json
{
    "body": "Resolution: worksforme",
    "created_at": "2010-04-15T05:56:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6020",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6020#issuecomment-47846",
    "user": "https://github.com/jhpalmieri"
}
```

Resolution: worksforme



---

archive/issue_comments_047847.json:
```json
{
    "body": "Closed as requested (fixed by #6671).",
    "created_at": "2010-04-15T05:56:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6020",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6020#issuecomment-47847",
    "user": "https://github.com/jhpalmieri"
}
```

Closed as requested (fixed by #6671).



---

archive/issue_events_014144.json:
```json
{
    "actor": "https://github.com/jhpalmieri",
    "created_at": "2010-04-15T05:56:20Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6020",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6020#event-14144"
}
```
