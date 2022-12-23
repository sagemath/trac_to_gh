# Issue 4296: univariate polynomial power ignores 2nd argument

archive/issues_004296.json:
```json
{
    "body": "Assignee: somebody\n\n\n```\nsage: R = PolynomialRing(GF(2), x)\nsage: f = R(x^9 + x^7 + x^6 + x^5 + x^4 + x^2 + x)\nsage: h = R(x^10 + x^7 + x^6 + x^5 + x^4 + x^3 + x^2 + 1)\nsage: (f^2) % h\nx^9 + x^8 + x^7 + x^5 + x^3\nsage: pow(f, 2, h)\nx^18 + x^14 + x^12 + x^10 + x^8 + x^4 + x^2\n```\n\nWe should expect both results to be equal to f^2 mod h.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4296\n\n",
    "created_at": "2008-10-15T13:47:21Z",
    "labels": [
        "basic arithmetic",
        "critical",
        "bug"
    ],
    "title": "univariate polynomial power ignores 2nd argument",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4296",
    "user": "zimmerma"
}
```
Assignee: somebody


```
sage: R = PolynomialRing(GF(2), x)
sage: f = R(x^9 + x^7 + x^6 + x^5 + x^4 + x^2 + x)
sage: h = R(x^10 + x^7 + x^6 + x^5 + x^4 + x^3 + x^2 + 1)
sage: (f^2) % h
x^9 + x^8 + x^7 + x^5 + x^3
sage: pow(f, 2, h)
x^18 + x^14 + x^12 + x^10 + x^8 + x^4 + x^2
```

We should expect both results to be equal to f^2 mod h.

Issue created by migration from https://trac.sagemath.org/ticket/4296





---

archive/issue_comments_031425.json:
```json
{
    "body": "This works for me in sage-3.2.2.",
    "created_at": "2008-12-28T12:27:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4296",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4296#issuecomment-31425",
    "user": "AlexGhitza"
}
```

This works for me in sage-3.2.2.



---

archive/issue_comments_031426.json:
```json
{
    "body": "Same for me:\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nsage: R = PolynomialRing(GF(2), x)\nsage: f = R(x^9 + x^7 + x^6 + x^5 + x^4 + x^2 + x)\nsage: h = R(x^10 + x^7 + x^6 + x^5 + x^4 + x^3 + x^2 + 1)\nsage: (f^2) % h\nx^9 + x^8 + x^7 + x^5 + x^3\nsage: pow(f, 2, h)\nx^9 + x^8 + x^7 + x^5 + x^3\nsage: \n```\n\nPlease add a doctest and once it has been merged we can close this ticket.\n| Sage Version 3.2.2, Release Date: 2008-12-18                       |\n| Type notebook() for the GUI, and license() for information.        |\nCheers,\n\nMichael",
    "created_at": "2008-12-28T15:40:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4296",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4296#issuecomment-31426",
    "user": "mabshoff"
}
```

Same for me:

```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: R = PolynomialRing(GF(2), x)
sage: f = R(x^9 + x^7 + x^6 + x^5 + x^4 + x^2 + x)
sage: h = R(x^10 + x^7 + x^6 + x^5 + x^4 + x^3 + x^2 + 1)
sage: (f^2) % h
x^9 + x^8 + x^7 + x^5 + x^3
sage: pow(f, 2, h)
x^9 + x^8 + x^7 + x^5 + x^3
sage: 
```

Please add a doctest and once it has been merged we can close this ticket.
| Sage Version 3.2.2, Release Date: 2008-12-18                       |
| Type notebook() for the GUI, and license() for information.        |
Cheers,

Michael



---

archive/issue_comments_031427.json:
```json
{
    "body": "OK, a patch with the doctest is attached.",
    "created_at": "2008-12-28T15:59:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4296",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4296#issuecomment-31427",
    "user": "AlexGhitza"
}
```

OK, a patch with the doctest is attached.



---

archive/issue_comments_031428.json:
```json
{
    "body": "Attachment\n\nThe attached patch seems to be just the doctest, no new code...",
    "created_at": "2008-12-29T20:20:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4296",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4296#issuecomment-31428",
    "user": "robertwb"
}
```

Attachment

The attached patch seems to be just the doctest, no new code...



---

archive/issue_comments_031429.json:
```json
{
    "body": "Replying to [comment:5 robertwb]:\n> The attached patch seems to be just the doctest, no new code...\n\nYes, because the bug originally reported has been fixed [or so it seems :)].\n\nCheers,\n\nMichael",
    "created_at": "2008-12-29T20:25:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4296",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4296#issuecomment-31429",
    "user": "mabshoff"
}
```

Replying to [comment:5 robertwb]:
> The attached patch seems to be just the doctest, no new code...

Yes, because the bug originally reported has been fixed [or so it seems :)].

Cheers,

Michael



---

archive/issue_comments_031430.json:
```json
{
    "body": "Ah, good point. \n\nI'm not sure how I feel about throwing the symbolic x around all around, though I guess efficiency doesn't matter too much here. \n\nAlso, just looking at the code it can be very inefficient--it computes (a^b) in full, then divides by the modulus taking the remainder. This is fine for small exponents, but for anything large is wasteful.",
    "created_at": "2008-12-29T21:02:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4296",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4296#issuecomment-31430",
    "user": "robertwb"
}
```

Ah, good point. 

I'm not sure how I feel about throwing the symbolic x around all around, though I guess efficiency doesn't matter too much here. 

Also, just looking at the code it can be very inefficient--it computes (a^b) in full, then divides by the modulus taking the remainder. This is fine for small exponents, but for anything large is wasteful.



---

archive/issue_comments_031431.json:
```json
{
    "body": "Replying to [comment:7 robertwb]:\n> Ah, good point. \n\n:)\n\n> I'm not sure how I feel about throwing the symbolic x around all around, though I guess efficiency doesn't matter too much here. \n\nYeah, I would consider it a good idea to get this in as is and open another ticket to make this more efficient.\n\n> Also, just looking at the code it can be very inefficient--it computes `(a^b)` in full, then divides by the modulus taking the remainder. This is fine for small exponents, but for anything large is wasteful. \n\nCheers,\n\nMichael",
    "created_at": "2008-12-29T21:45:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4296",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4296#issuecomment-31431",
    "user": "mabshoff"
}
```

Replying to [comment:7 robertwb]:
> Ah, good point. 

:)

> I'm not sure how I feel about throwing the symbolic x around all around, though I guess efficiency doesn't matter too much here. 

Yeah, I would consider it a good idea to get this in as is and open another ticket to make this more efficient.

> Also, just looking at the code it can be very inefficient--it computes `(a^b)` in full, then divides by the modulus taking the remainder. This is fine for small exponents, but for anything large is wasteful. 

Cheers,

Michael



---

archive/issue_comments_031432.json:
```json
{
    "body": "I give this a positive review since it is just a doctest showing that something which used to fail now works.\n\nI sympathise with robertwb's concern, but that should be a separate ticket.  I looked for, but could not find anywhere, the code which pow(f,2,h) runs.",
    "created_at": "2009-01-18T17:44:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4296",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4296#issuecomment-31432",
    "user": "cremona"
}
```

I give this a positive review since it is just a doctest showing that something which used to fail now works.

I sympathise with robertwb's concern, but that should be a separate ticket.  I looked for, but could not find anywhere, the code which pow(f,2,h) runs.



---

archive/issue_comments_031433.json:
```json
{
    "body": "Merged in Sage 3.3.alpha0",
    "created_at": "2009-01-19T04:16:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4296",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4296#issuecomment-31433",
    "user": "mabshoff"
}
```

Merged in Sage 3.3.alpha0



---

archive/issue_comments_031434.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-19T04:16:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4296",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4296#issuecomment-31434",
    "user": "mabshoff"
}
```

Resolution: fixed
