# Issue 4612: [with patch, needs review] is_perfect_power for rationals

archive/issues_004612.json:
```json
{
    "body": "Assignee: somebody\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4612\n\n",
    "created_at": "2008-11-25T07:21:25Z",
    "labels": [
        "basic arithmetic",
        "major",
        "bug"
    ],
    "title": "[with patch, needs review] is_perfect_power for rationals",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4612",
    "user": "robertwb"
}
```
Assignee: somebody



Issue created by migration from https://trac.sagemath.org/ticket/4612





---

archive/issue_comments_034611.json:
```json
{
    "body": "The code looks good, but doesn't handle negatives correctly:\n\n\n```\nsage: (-1/25).is_perfect_power()\nTrue\n```\n\n\nFix is pretty obvious (call `mpz_sgn` on the numerator, make sure we don't get -1), so I'm adding a patch that fixes it.",
    "created_at": "2008-11-27T07:50:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4612",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4612#issuecomment-34611",
    "user": "craigcitro"
}
```

The code looks good, but doesn't handle negatives correctly:


```
sage: (-1/25).is_perfect_power()
True
```


Fix is pretty obvious (call `mpz_sgn` on the numerator, make sure we don't get -1), so I'm adding a patch that fixes it.



---

archive/issue_comments_034612.json:
```json
{
    "body": "Actually, I retract my review above. This patch is completely wrong! In particular, look at this:\n\n\n```\nsage: (4/27).is_perfect_power()\nTrue\n```\n\n\nThat's absolutely not a perfect power! This code is too naive. If both the numerator and denominator are perfect powers, we need to see what powers they are, and make sure that one of the powers divides the other. Here's a battery of tests that needs to pass:\n\n\n```\n sage: (2/27).is_perfect_power()\n False\n sage: (4/27).is_perfect_power()\n False\n sage: (-1/25).is_perfect_power()\n False\n sage: (-1/27).is_perfect_power()\n True\n```\n\n\nOne might want even more doctests ...",
    "created_at": "2008-11-27T08:05:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4612",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4612#issuecomment-34612",
    "user": "craigcitro"
}
```

Actually, I retract my review above. This patch is completely wrong! In particular, look at this:


```
sage: (4/27).is_perfect_power()
True
```


That's absolutely not a perfect power! This code is too naive. If both the numerator and denominator are perfect powers, we need to see what powers they are, and make sure that one of the powers divides the other. Here's a battery of tests that needs to pass:


```
 sage: (2/27).is_perfect_power()
 False
 sage: (4/27).is_perfect_power()
 False
 sage: (-1/25).is_perfect_power()
 False
 sage: (-1/27).is_perfect_power()
 True
```


One might want even more doctests ...



---

archive/issue_comments_034613.json:
```json
{
    "body": "Oops... Yeah, that's totally wrong. I'll fix this.",
    "created_at": "2008-11-28T08:18:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4612",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4612#issuecomment-34613",
    "user": "robertwb"
}
```

Oops... Yeah, that's totally wrong. I'll fix this.



---

archive/issue_comments_034614.json:
```json
{
    "body": "It won't be trivial to fix since the gmp function only returns whether or not the argument is a perfect power, not what the root or exponents are.\n\nI suggest that we implement something involving the factorizations.  Assuming that both numerator and denonimator are perfect powers, compute (where the input is r = +-n/d)\n\n```\ngcd(gcd([e for p,e in n.factor()]), gcd([e for p,e in d.factor()]))\n```\n\nIf that is 1 return 1.  If it is e>1 then return e if r is positive or if e is odd and r is negative, otherwise (e even, r<0) return e.prime_to_m_part(2), i.e. the odd part of e.  This will return the largest e such that r is an e'th power.\n\nI don't see what else we can do unless gmp has a better function.",
    "created_at": "2008-12-19T20:35:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4612",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4612#issuecomment-34614",
    "user": "cremona"
}
```

It won't be trivial to fix since the gmp function only returns whether or not the argument is a perfect power, not what the root or exponents are.

I suggest that we implement something involving the factorizations.  Assuming that both numerator and denonimator are perfect powers, compute (where the input is r = +-n/d)

```
gcd(gcd([e for p,e in n.factor()]), gcd([e for p,e in d.factor()]))
```

If that is 1 return 1.  If it is e>1 then return e if r is positive or if e is odd and r is negative, otherwise (e even, r<0) return e.prime_to_m_part(2), i.e. the odd part of e.  This will return the largest e such that r is an e'th power.

I don't see what else we can do unless gmp has a better function.



---

archive/issue_comments_034615.json:
```json
{
    "body": "Factoring the numerator/denominator completely may be prohibitively expensive. It would probably be cheaper to compute the nth root and see if it is exact for n in from 2 to lg(n).",
    "created_at": "2008-12-19T21:04:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4612",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4612#issuecomment-34615",
    "user": "robertwb"
}
```

Factoring the numerator/denominator completely may be prohibitively expensive. It would probably be cheaper to compute the nth root and see if it is exact for n in from 2 to lg(n).



---

archive/issue_comments_034616.json:
```json
{
    "body": "I just looked at the gmp source, it does trial division for all three-digit primes, aborting if it finds any inconsistency. If small factors were found, it can bound the nth roots it needs to test on the remainder (if any), otherwise it tries taking nth roots for primes up to lg(2). \n\nIt does not compute the largest exponent for which it is an nth root, only a divisor of it. I wonder if MPIR will would be willing to provide such a function. \n\nHowever, I believe there is an easier solution. Noting that the numerator and denominator are relatively prime, one only needs to check if the product is a perfect power, and if it is their ratio will be as well. (It is unclear however whether or not it would be a time savings to do the (cheaper) test on the smallest of the numerator/denominator first.)",
    "created_at": "2008-12-19T21:24:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4612",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4612#issuecomment-34616",
    "user": "robertwb"
}
```

I just looked at the gmp source, it does trial division for all three-digit primes, aborting if it finds any inconsistency. If small factors were found, it can bound the nth roots it needs to test on the remainder (if any), otherwise it tries taking nth roots for primes up to lg(2). 

It does not compute the largest exponent for which it is an nth root, only a divisor of it. I wonder if MPIR will would be willing to provide such a function. 

However, I believe there is an easier solution. Noting that the numerator and denominator are relatively prime, one only needs to check if the product is a perfect power, and if it is their ratio will be as well. (It is unclear however whether or not it would be a time savings to do the (cheaper) test on the smallest of the numerator/denominator first.)



---

archive/issue_comments_034617.json:
```json
{
    "body": "Replying to [comment:6 robertwb]:\n> I just looked at the gmp source, it does trial division for all three-digit primes, aborting if it finds any inconsistency. If small factors were found, it can bound the nth roots it needs to test on the remainder (if any), otherwise it tries taking nth roots for primes up to lg(2). \n\nok -- I had not thought of checking the p-valuation for small primes but that's a good idea.  Otherwise it's the textbook method, which would not be hard to adapt to provide the exponent.\n\n> \n> It does not compute the largest exponent for which it is an nth root, only a divisor of it. I wonder if MPIR will would be willing to provide such a function. \n\nThat would be good.  All we have to do is ask!\n\n> \n> However, I believe there is an easier solution. Noting that the numerator and denominator are relatively prime, one only needs to check if the product is a perfect power, and if it is their ratio will be as well. (It is unclear however whether or not it would be a time savings to do the (cheaper) test on the smallest of the numerator/denominator first.)\n\nCertainly it's clear that you can replace n/d by n*d, but we already know what to do if know the numerator is an e'th power and the denom is an f'th power (answer = gcd(e,f), or the odd part of that if the number was negative), which would be more efficient.  So as long as we can solve the problem (with the exponent) for integers then it will be easy to do it for rationals.",
    "created_at": "2008-12-19T23:08:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4612",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4612#issuecomment-34617",
    "user": "cremona"
}
```

Replying to [comment:6 robertwb]:
> I just looked at the gmp source, it does trial division for all three-digit primes, aborting if it finds any inconsistency. If small factors were found, it can bound the nth roots it needs to test on the remainder (if any), otherwise it tries taking nth roots for primes up to lg(2). 

ok -- I had not thought of checking the p-valuation for small primes but that's a good idea.  Otherwise it's the textbook method, which would not be hard to adapt to provide the exponent.

> 
> It does not compute the largest exponent for which it is an nth root, only a divisor of it. I wonder if MPIR will would be willing to provide such a function. 

That would be good.  All we have to do is ask!

> 
> However, I believe there is an easier solution. Noting that the numerator and denominator are relatively prime, one only needs to check if the product is a perfect power, and if it is their ratio will be as well. (It is unclear however whether or not it would be a time savings to do the (cheaper) test on the smallest of the numerator/denominator first.)

Certainly it's clear that you can replace n/d by n*d, but we already know what to do if know the numerator is an e'th power and the denom is an f'th power (answer = gcd(e,f), or the odd part of that if the number was negative), which would be more efficient.  So as long as we can solve the problem (with the exponent) for integers then it will be easy to do it for rationals.



---

archive/issue_comments_034618.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-12-19T23:11:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4612",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4612#issuecomment-34618",
    "user": "robertwb"
}
```

Attachment



---

archive/issue_comments_034619.json:
```json
{
    "body": "A new patch is up. If n/d is a not perfect power, it is usually cheaper to check min(n,d) for being a perfect power first, but that is redundant if n/d is in fact a perfect power. I added an extra parameter to handle that, let me know if you think it's a good idea or excessive. \n\nIt is more work to figure out the maximal exponent a number can be expressed with than it is to detect whether it can be expressed with any exponent. For example, consider $p^(2r) / q^(2s)$. It is easy to detect that both are perfect squares, but finding r and s is more work. \n\nClearly, the optimal solution would look something like gmp's mpz_perfect_power_p done in parallel on the numerator and denominator.",
    "created_at": "2008-12-19T23:23:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4612",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4612#issuecomment-34619",
    "user": "robertwb"
}
```

A new patch is up. If n/d is a not perfect power, it is usually cheaper to check min(n,d) for being a perfect power first, but that is redundant if n/d is in fact a perfect power. I added an extra parameter to handle that, let me know if you think it's a good idea or excessive. 

It is more work to figure out the maximal exponent a number can be expressed with than it is to detect whether it can be expressed with any exponent. For example, consider $p^(2r) / q^(2s)$. It is easy to detect that both are perfect squares, but finding r and s is more work. 

Clearly, the optimal solution would look something like gmp's mpz_perfect_power_p done in parallel on the numerator and denominator.



---

archive/issue_comments_034620.json:
```json
{
    "body": "Something is wrong:\n\n```\nsage: a=(-1/20)^3\nsage: a.is_perfect_power()\nFalse\n```\n\nbut then so is this:\n\n```\nsage: a=(-20)^3\nsage: a.is_perfect_power()\nFalse\n```\n\nwhich does not call the new function but the old one (with integers).  Is this a bug in gmp?  If so it should be reported.",
    "created_at": "2008-12-20T21:18:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4612",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4612#issuecomment-34620",
    "user": "cremona"
}
```

Something is wrong:

```
sage: a=(-1/20)^3
sage: a.is_perfect_power()
False
```

but then so is this:

```
sage: a=(-20)^3
sage: a.is_perfect_power()
False
```

which does not call the new function but the old one (with integers).  Is this a bug in gmp?  If so it should be reported.



---

archive/issue_comments_034621.json:
```json
{
    "body": "Integer.is_perfect_power is a direct call to mpz_perfect_power_p. Looks like a bug in gmp to me. That's really bad.",
    "created_at": "2008-12-20T21:41:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4612",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4612#issuecomment-34621",
    "user": "robertwb"
}
```

Integer.is_perfect_power is a direct call to mpz_perfect_power_p. Looks like a bug in gmp to me. That's really bad.



---

archive/issue_comments_034622.json:
```json
{
    "body": "Replying to [comment:10 robertwb]:\n> Integer.is_perfect_power is a direct call to mpz_perfect_power_p. Looks like a bug in gmp to me. That's really bad. \n\n```\nsage: len([a for a in srange(100) if not (-a^3).is_perfect_power()])\n24\n```\n\nExperiment shows that it gives the wrong answer for `-a^3` whenever a is not square-free.",
    "created_at": "2008-12-21T12:04:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4612",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4612#issuecomment-34622",
    "user": "cremona"
}
```

Replying to [comment:10 robertwb]:
> Integer.is_perfect_power is a direct call to mpz_perfect_power_p. Looks like a bug in gmp to me. That's really bad. 

```
sage: len([a for a in srange(100) if not (-a^3).is_perfect_power()])
24
```

Experiment shows that it gives the wrong answer for `-a^3` whenever a is not square-free.



---

archive/issue_comments_034623.json:
```json
{
    "body": "I did ping the eMPIRe list - see http://groups.google.com/group/mpir-devel/t/dc3682208383afc7\n\nCheers,\n\nMichael",
    "created_at": "2008-12-23T00:10:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4612",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4612#issuecomment-34623",
    "user": "mabshoff"
}
```

I did ping the eMPIRe list - see http://groups.google.com/group/mpir-devel/t/dc3682208383afc7

Cheers,

Michael



---

archive/issue_comments_034624.json:
```json
{
    "body": "The upcoming eMPIRe will fix the issue that we are currently seeing in gmp:\n\n```\nsage: len([a for a in srange(10**6) if not (-a^3).is_perfect_power()]) \n0 \n```\n\nThis is mpir-svn1523 and we are planning to switch in Sage 3.4, so this will happen around SD12.\n\nCheers,\n\nMichael",
    "created_at": "2009-01-04T01:28:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4612",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4612#issuecomment-34624",
    "user": "mabshoff"
}
```

The upcoming eMPIRe will fix the issue that we are currently seeing in gmp:

```
sage: len([a for a in srange(10**6) if not (-a^3).is_perfect_power()]) 
0 
```

This is mpir-svn1523 and we are planning to switch in Sage 3.4, so this will happen around SD12.

Cheers,

Michael



---

archive/issue_comments_034625.json:
```json
{
    "body": "Note that with the old gmp as well as the new eMPIRe this operation leaks like a sieve:\n\n```\nsage: get_memory_usage()\n798.4765625\nsage: time len([a for a in srange(10**6) if not (-a^3).is_perfect_power()])\nCPU times: user 2.84 s, sys: 0.27 s, total: 3.12 s\nWall time: 3.12 s\n241224\nsage: get_memory_usage()\n868.921875\n```\n\n\nI have made this #4935 since it is seemingly unrelated to the correctness issue.\n\nCheers,\n\nMichael",
    "created_at": "2009-01-04T02:35:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4612",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4612#issuecomment-34625",
    "user": "mabshoff"
}
```

Note that with the old gmp as well as the new eMPIRe this operation leaks like a sieve:

```
sage: get_memory_usage()
798.4765625
sage: time len([a for a in srange(10**6) if not (-a^3).is_perfect_power()])
CPU times: user 2.84 s, sys: 0.27 s, total: 3.12 s
Wall time: 3.12 s
241224
sage: get_memory_usage()
868.921875
```


I have made this #4935 since it is seemingly unrelated to the correctness issue.

Cheers,

Michael



---

archive/issue_comments_034626.json:
```json
{
    "body": "Alright, I've coded up a new version of the above patch that we should use until we merge either a new GMP or eMPIRe with the fix included. This patch works around the GMP bug for both integers and rationals.\n\nAssuming that this gets a positive review, I'll open another ticket to say \"remove ugly workaround\" once we merge a new arithmetic package with a fix.\n\n(Credit also goes to Rob Bradshaw for code, and John Cremona for refereeing.)",
    "created_at": "2009-01-11T08:30:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4612",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4612#issuecomment-34626",
    "user": "craigcitro"
}
```

Alright, I've coded up a new version of the above patch that we should use until we merge either a new GMP or eMPIRe with the fix included. This patch works around the GMP bug for both integers and rationals.

Assuming that this gets a positive review, I'll open another ticket to say "remove ugly workaround" once we merge a new arithmetic package with a fix.

(Credit also goes to Rob Bradshaw for code, and John Cremona for refereeing.)



---

archive/issue_comments_034627.json:
```json
{
    "body": "Changing assignee from somebody to craigcitro.",
    "created_at": "2009-01-11T08:30:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4612",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4612#issuecomment-34627",
    "user": "craigcitro"
}
```

Changing assignee from somebody to craigcitro.



---

archive/issue_comments_034628.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-01-11T08:30:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4612",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4612#issuecomment-34628",
    "user": "craigcitro"
}
```

Changing status from new to assigned.



---

archive/issue_comments_034629.json:
```json
{
    "body": "Attachment\n\nNote: apply **only** `trac-4612-v2.patch`, i.e. don't apply it on top of Robert's patch.",
    "created_at": "2009-01-11T08:30:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4612",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4612#issuecomment-34629",
    "user": "craigcitro"
}
```

Attachment

Note: apply **only** `trac-4612-v2.patch`, i.e. don't apply it on top of Robert's patch.



---

archive/issue_comments_034630.json:
```json
{
    "body": "Patch applies cleanly to 3.2.3, code looks good, tests pass.  Pass!",
    "created_at": "2009-01-13T21:52:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4612",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4612#issuecomment-34630",
    "user": "cremona"
}
```

Patch applies cleanly to 3.2.3, code looks good, tests pass.  Pass!



---

archive/issue_comments_034631.json:
```json
{
    "body": "Replying to [comment:17 cremona]:\n> Patch applies cleanly to 3.2.3, code looks good, tests pass.  Pass!\n\nWe are switching to eMPIRe in 3.3.alpha0, so I am not sure how much of the workaround in this patch ought to be removed. It might be a good idea to rebase this patch for 3.3.alpha0 and hold on for now.\n\nCheers,\n\nMichael",
    "created_at": "2009-01-13T21:54:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4612",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4612#issuecomment-34631",
    "user": "mabshoff"
}
```

Replying to [comment:17 cremona]:
> Patch applies cleanly to 3.2.3, code looks good, tests pass.  Pass!

We are switching to eMPIRe in 3.3.alpha0, so I am not sure how much of the workaround in this patch ought to be removed. It might be a good idea to rebase this patch for 3.3.alpha0 and hold on for now.

Cheers,

Michael



---

archive/issue_comments_034632.json:
```json
{
    "body": "Ah, I wrote this before I knew eMRIPe was so close. I agree, once it's merged, I'll make a new patch with that alpha or rc.",
    "created_at": "2009-01-13T22:17:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4612",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4612#issuecomment-34632",
    "user": "craigcitro"
}
```

Ah, I wrote this before I knew eMRIPe was so close. I agree, once it's merged, I'll make a new patch with that alpha or rc.



---

archive/issue_comments_034633.json:
```json
{
    "body": "Fair enough.  I just hope that the empire versions pass these doctests....",
    "created_at": "2009-01-13T22:45:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4612",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4612#issuecomment-34633",
    "user": "cremona"
}
```

Fair enough.  I just hope that the empire versions pass these doctests....



---

archive/issue_comments_034634.json:
```json
{
    "body": "Replying to [comment:19 craigcitro]:\n> Ah, I wrote this before I knew eMRIPe was so close. I agree, once it's merged, I'll make a new patch with that alpha or rc.\n\nThis is going in as is for now even though eMPIRe will be in 3.3.alpha0. I will open a followup ticket to deal with using the eMPIRe function directly again, but since this adds doctests it will be merged.\n\nCheers,\n\nMichael",
    "created_at": "2009-01-18T14:13:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4612",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4612#issuecomment-34634",
    "user": "mabshoff"
}
```

Replying to [comment:19 craigcitro]:
> Ah, I wrote this before I knew eMRIPe was so close. I agree, once it's merged, I'll make a new patch with that alpha or rc.

This is going in as is for now even though eMPIRe will be in 3.3.alpha0. I will open a followup ticket to deal with using the eMPIRe function directly again, but since this adds doctests it will be merged.

Cheers,

Michael



---

archive/issue_comments_034635.json:
```json
{
    "body": "Merged trac-4612-v2.patch in Sage 3.3.alpha0",
    "created_at": "2009-01-18T14:45:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4612",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4612#issuecomment-34635",
    "user": "mabshoff"
}
```

Merged trac-4612-v2.patch in Sage 3.3.alpha0



---

archive/issue_comments_034636.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-18T14:45:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4612",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4612#issuecomment-34636",
    "user": "mabshoff"
}
```

Resolution: fixed
