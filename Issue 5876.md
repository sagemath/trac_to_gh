# Issue 5876: [with patch, needs review] Vast speedup in P1List construction

archive/issues_005876.json:
```json
{
    "body": "Assignee: @craigcitro\n\nCC:  georgsweber mtaranes @williamstein\n\nKeywords: modular manin symbols\n\nThe P1List() constructor for Manin symbols (elements of `P^1(ZZ/NZZ)` was rather inefficient.  It constructed vastly too many symbols, normalised them all and then deleted duplicates.\n\nThis is quite unnecessary since it is easy to generate the list with no duplicates (and with simpler code).\n\nAs reported on sage-nt:\n\nBefore (3.4.1):\n\n\n```\nsage: time P1List(100000)\nCPU times: user 3.52 s, sys: 0.03 s, total: 3.55 s\nWall time: 3.55 s\nThe projective line over the integers modulo 100000\nsage: time P1List(1000000)\nCPU times: user 129.11 s, sys: 0.64 s, total: 129.75 s\nWall time: 131.96 s\nThe projective line over the integers modulo 1000000\n```\n\n\nAfter:\n\n\n```\nsage: time P1List(100000)\nCPU times: user 0.41 s, sys: 0.01 s, total: 0.42 s\nWall time: 0.42 s\nThe projective line over the integers modulo 100000\nsage: time P1List(1000000)\nCPU times: user 8.33 s, sys: 0.12 s, total: 8.45 s\nWall time: 8.80 s\nThe projective line over the integers modulo 1000000\n```\n\n\nThe patch does this for both versions `p1list_int()` and `p1list_llong()`.\n\nI think similar speedups are possible in the p1_normalise functions which would be significant in practice, and will try to get to that tomorrow.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5876\n\n",
    "created_at": "2009-04-23T16:23:46Z",
    "labels": [
        "component: modular forms"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4.2",
    "title": "[with patch, needs review] Vast speedup in P1List construction",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5876",
    "user": "https://github.com/JohnCremona"
}
```
Assignee: @craigcitro

CC:  georgsweber mtaranes @williamstein

Keywords: modular manin symbols

The P1List() constructor for Manin symbols (elements of `P^1(ZZ/NZZ)` was rather inefficient.  It constructed vastly too many symbols, normalised them all and then deleted duplicates.

This is quite unnecessary since it is easy to generate the list with no duplicates (and with simpler code).

As reported on sage-nt:

Before (3.4.1):


```
sage: time P1List(100000)
CPU times: user 3.52 s, sys: 0.03 s, total: 3.55 s
Wall time: 3.55 s
The projective line over the integers modulo 100000
sage: time P1List(1000000)
CPU times: user 129.11 s, sys: 0.64 s, total: 129.75 s
Wall time: 131.96 s
The projective line over the integers modulo 1000000
```


After:


```
sage: time P1List(100000)
CPU times: user 0.41 s, sys: 0.01 s, total: 0.42 s
Wall time: 0.42 s
The projective line over the integers modulo 100000
sage: time P1List(1000000)
CPU times: user 8.33 s, sys: 0.12 s, total: 8.45 s
Wall time: 8.80 s
The projective line over the integers modulo 1000000
```


The patch does this for both versions `p1list_int()` and `p1list_llong()`.

I think similar speedups are possible in the p1_normalise functions which would be significant in practice, and will try to get to that tomorrow.

Issue created by migration from https://trac.sagemath.org/ticket/5876





---

archive/issue_comments_046324.json:
```json
{
    "body": "Attachment [p1list.patch](tarball://root/attachments/some-uuid/ticket5876/p1list.patch) by @JohnCremona created at 2009-04-23 16:24:46\n\nBased on 3.4.1",
    "created_at": "2009-04-23T16:24:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5876",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5876#issuecomment-46324",
    "user": "https://github.com/JohnCremona"
}
```

Attachment [p1list.patch](tarball://root/attachments/some-uuid/ticket5876/p1list.patch) by @JohnCremona created at 2009-04-23 16:24:46

Based on 3.4.1



---

archive/issue_comments_046325.json:
```json
{
    "body": "Cool. One question, why are you doing\n\n\n```\ng = arith_int.c_gcd_int(c,N)\nif g==c:  # is a divisor\n```\n\n\ninstead of simply\n\n\n```\nif N % c == 0:\n```\n\n\nAlso, would it be faster to initialize the list with (1, t) for 0 <= t < N (as this is often the bulk of P<sup>1</sup>(Z/nZ)) and then ignore/not compute these ones later?",
    "created_at": "2009-04-23T18:57:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5876",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5876#issuecomment-46325",
    "user": "https://github.com/robertwb"
}
```

Cool. One question, why are you doing


```
g = arith_int.c_gcd_int(c,N)
if g==c:  # is a divisor
```


instead of simply


```
if N % c == 0:
```


Also, would it be faster to initialize the list with (1, t) for 0 <= t < N (as this is often the bulk of P<sup>1</sup>(Z/nZ)) and then ignore/not compute these ones later?



---

archive/issue_comments_046326.json:
```json
{
    "body": "Enthusiastic positive review!\n\n> Why are you doing...\n\nNo good reason.  I just never got around to optimizing the code.\n\n> Also, would it be faster to initialize the list with (1, t) for \n> 0 <= t < N (as this is often the bulk of P1(Z/nZ)) and then ignore/not \n> compute these ones later? \n\nYes, that would be better.  That's what your g0n library does.  I always wanted that optimization to get implemented.",
    "created_at": "2009-04-23T19:15:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5876",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5876#issuecomment-46326",
    "user": "https://github.com/williamstein"
}
```

Enthusiastic positive review!

> Why are you doing...

No good reason.  I just never got around to optimizing the code.

> Also, would it be faster to initialize the list with (1, t) for 
> 0 <= t < N (as this is often the bulk of P1(Z/nZ)) and then ignore/not 
> compute these ones later? 

Yes, that would be better.  That's what your g0n library does.  I always wanted that optimization to get implemented.



---

archive/issue_comments_046327.json:
```json
{
    "body": "Wow, I put up that patch before cycling home, spent the journey thinking of all the extra speedups which are possible (including stopping the c loop at N/2 or even N/3 when N is odd), and now I find that you are ahead of me.\n\nI will try to improve it myself tonight (it's 8.40pm here) and post a new patch.",
    "created_at": "2009-04-23T19:39:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5876",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5876#issuecomment-46327",
    "user": "https://github.com/JohnCremona"
}
```

Wow, I put up that patch before cycling home, spent the journey thinking of all the extra speedups which are possible (including stopping the c loop at N/2 or even N/3 when N is odd), and now I find that you are ahead of me.

I will try to improve it myself tonight (it's 8.40pm here) and post a new patch.



---

archive/issue_comments_046328.json:
```json
{
    "body": "replaces previous",
    "created_at": "2009-04-23T20:02:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5876",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5876#issuecomment-46328",
    "user": "https://github.com/JohnCremona"
}
```

replaces previous



---

archive/issue_comments_046329.json:
```json
{
    "body": "Attachment [trac_5876.patch](tarball://root/attachments/some-uuid/ticket5876/trac_5876.patch) by @JohnCremona created at 2009-04-23 20:03:13\n\nNew patch replaces previous and implements suggestions.  Hard to compare times as I'm on a different machine.",
    "created_at": "2009-04-23T20:03:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5876",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5876#issuecomment-46329",
    "user": "https://github.com/JohnCremona"
}
```

Attachment [trac_5876.patch](tarball://root/attachments/some-uuid/ticket5876/trac_5876.patch) by @JohnCremona created at 2009-04-23 20:03:13

New patch replaces previous and implements suggestions.  Hard to compare times as I'm on a different machine.



---

archive/issue_comments_046330.json:
```json
{
    "body": "For the record, on the same machines the previous timings I now get\n\n```\nsage: time P1List(10^5)\nCPU times: user 0.35 s, sys: 0.01 s, total: 0.36 s\nWall time: 0.35 s\nThe projective line over the integers modulo 100000\nsage: time P1List(10^6)\nCPU times: user 7.22 s, sys: 0.13 s, total: 7.35 s\nWall time: 7.35 s\nThe projective line over the integers modulo 1000000\n```\n\n\nAlso\n\n```\nsage: time P1List(1009*1013)\nCPU times: user 7.33 s, sys: 0.02 s, total: 7.35 s\nWall time: 7.36 s\nThe projective line over the integers modulo 1022117\nsage: time P1List(1000003)\nCPU times: user 8.25 s, sys: 0.03 s, total: 8.28 s\nWall time: 8.28 s\nThe projective line over the integers modulo 1000003\n```\n\nWe could do a lot better if were allowed to factor N: i nthe last example (prime just over `10^6`) there is really nothing to do but it effectively does trial division up to N/5 !\n\nIt might be worth having a version which takes as in put as well as N a factorization (as a list of (p,e) pairs.  Or just a list of divisors of N.\nwhich is a worthwhile extra saving.",
    "created_at": "2009-04-23T21:26:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5876",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5876#issuecomment-46330",
    "user": "https://github.com/JohnCremona"
}
```

For the record, on the same machines the previous timings I now get

```
sage: time P1List(10^5)
CPU times: user 0.35 s, sys: 0.01 s, total: 0.36 s
Wall time: 0.35 s
The projective line over the integers modulo 100000
sage: time P1List(10^6)
CPU times: user 7.22 s, sys: 0.13 s, total: 7.35 s
Wall time: 7.35 s
The projective line over the integers modulo 1000000
```


Also

```
sage: time P1List(1009*1013)
CPU times: user 7.33 s, sys: 0.02 s, total: 7.35 s
Wall time: 7.36 s
The projective line over the integers modulo 1022117
sage: time P1List(1000003)
CPU times: user 8.25 s, sys: 0.03 s, total: 8.28 s
Wall time: 8.28 s
The projective line over the integers modulo 1000003
```

We could do a lot better if were allowed to factor N: i nthe last example (prime just over `10^6`) there is really nothing to do but it effectively does trial division up to N/5 !

It might be worth having a version which takes as in put as well as N a factorization (as a list of (p,e) pairs.  Or just a list of divisors of N.
which is a worthwhile extra saving.



---

archive/issue_comments_046331.json:
```json
{
    "body": "Last comment:  the code runs slower on a 64-bit machine (Bill Hart's, which I would have expected to be at least as fast as the standard-issue U of Warwick 32-bit desktop).  The `10^6` example takes 12.59s on Bill's machine compared with only 7.22s.\n\nI wonder why?",
    "created_at": "2009-04-23T21:38:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5876",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5876#issuecomment-46331",
    "user": "https://github.com/JohnCremona"
}
```

Last comment:  the code runs slower on a 64-bit machine (Bill Hart's, which I would have expected to be at least as fast as the standard-issue U of Warwick 32-bit desktop).  The `10^6` example takes 12.59s on Bill's machine compared with only 7.22s.

I wonder why?



---

archive/issue_comments_046332.json:
```json
{
    "body": "John, \n\ndo you an Maite shared credit for authorship here?\n\nCheers,\n\nMichael",
    "created_at": "2009-04-24T02:24:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5876",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5876#issuecomment-46332",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

John, 

do you an Maite shared credit for authorship here?

Cheers,

Michael



---

archive/issue_comments_046333.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-04-24T02:32:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5876",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5876#issuecomment-46333",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_046334.json:
```json
{
    "body": "Merged trac_5876.patch in Sage 3.4.2.alpha0.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-24T02:32:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5876",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5876#issuecomment-46334",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged trac_5876.patch in Sage 3.4.2.alpha0.

Cheers,

Michael



---

archive/issue_comments_046335.json:
```json
{
    "body": "The positive review was for the old patch, but the new one deserves one as well. Factoring/enumerating divisors would probably make a lot of sense, especially once we have fast factoring of small numbers (there's a project on this in William Stein's class right now). Not sure it would be a huge gain, as we are enumerating O(N) things anyways. \n\nThis should certainly go in. \n\n- Robert",
    "created_at": "2009-04-24T02:41:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5876",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5876#issuecomment-46335",
    "user": "https://github.com/robertwb"
}
```

The positive review was for the old patch, but the new one deserves one as well. Factoring/enumerating divisors would probably make a lot of sense, especially once we have fast factoring of small numbers (there's a project on this in William Stein's class right now). Not sure it would be a huge gain, as we are enumerating O(N) things anyways. 

This should certainly go in. 

- Robert



---

archive/issue_comments_046336.json:
```json
{
    "body": "Robert,\n\nthanks for following up, I did not notice that the review by William was for the first patch only. I did assign reviewer credit to William and you, so now I am waiting on John to tell us in the morning who gets credited for writing the patch (if there is anyone besides him).\n\nCheers,\n\nMichael",
    "created_at": "2009-04-24T02:54:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5876",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5876#issuecomment-46336",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Robert,

thanks for following up, I did not notice that the review by William was for the first patch only. I did assign reviewer credit to William and you, so now I am waiting on John to tell us in the morning who gets credited for writing the patch (if there is anyone besides him).

Cheers,

Michael



---

archive/issue_comments_046337.json:
```json
{
    "body": "Replying to [comment:10 mabshoff]:\n> Robert,\n> \n> thanks for following up, I did not notice that the review by William was for the first patch only. I did assign reviewer credit to William and you, so now I am waiting on John to tell us in the morning who gets credited for writing the patch (if there is anyone besides him).\n> \n> Cheers,\n> \n> Michael\n\nI think I'll take the credit.  Maite and I were looking at the code since we were working out how to do the same over number fields, and I had just written my contribution to sage-nt listing 4 possible methods there.  We noticed the inefficiency together, but I wrote the new code alone.  She can get credit for the number field version when it is ready!",
    "created_at": "2009-04-24T08:09:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5876",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5876#issuecomment-46337",
    "user": "https://github.com/JohnCremona"
}
```

Replying to [comment:10 mabshoff]:
> Robert,
> 
> thanks for following up, I did not notice that the review by William was for the first patch only. I did assign reviewer credit to William and you, so now I am waiting on John to tell us in the morning who gets credited for writing the patch (if there is anyone besides him).
> 
> Cheers,
> 
> Michael

I think I'll take the credit.  Maite and I were looking at the code since we were working out how to do the same over number fields, and I had just written my contribution to sage-nt listing 4 possible methods there.  We noticed the inefficiency together, but I wrote the new code alone.  She can get credit for the number field version when it is ready!



---

archive/issue_comments_046338.json:
```json
{
    "body": "Replying to [comment:11 cremona]:\n\n\n> I think I'll take the credit.  Maite and I were looking at the code since we were working out how to do the same over number fields, and I had just written my contribution to sage-nt listing 4 possible methods there.  We noticed the inefficiency together, but I wrote the new code alone.  She can get credit for the number field version when it is ready!\n\nThanks for clearing this up John.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-24T08:19:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5876",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5876#issuecomment-46338",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Replying to [comment:11 cremona]:


> I think I'll take the credit.  Maite and I were looking at the code since we were working out how to do the same over number fields, and I had just written my contribution to sage-nt listing 4 possible methods there.  We noticed the inefficiency together, but I wrote the new code alone.  She can get credit for the number field version when it is ready!

Thanks for clearing this up John.

Cheers,

Michael
