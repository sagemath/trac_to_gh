# Issue 793: [with new patch, positive review] wrapper for hyperelliptic curve zeta functions

archive/issues_000793.json:
```json
{
    "body": "Assignee: @williamstein\n\nEven though we have functionality for computing zeta functions of hyperelliptic curves, the `HyperellipticCurve` curve object itself doesn't yet have a method like `zeta_function`. This shouldn't be hard to do (over prime fields at least), using code in `sage/schemes/hyperelliptic_curves/frobenius.pyx` and `sage/schemes/elliptic_curves/monsky_washnitzer.py`.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/793\n\n",
    "closed_at": "2009-04-01T23:54:00Z",
    "created_at": "2007-10-02T19:32:58Z",
    "labels": [
        "component: number theory"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4.1",
    "title": "[with new patch, positive review] wrapper for hyperelliptic curve zeta functions",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/793",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```
Assignee: @williamstein

Even though we have functionality for computing zeta functions of hyperelliptic curves, the `HyperellipticCurve` curve object itself doesn't yet have a method like `zeta_function`. This shouldn't be hard to do (over prime fields at least), using code in `sage/schemes/hyperelliptic_curves/frobenius.pyx` and `sage/schemes/elliptic_curves/monsky_washnitzer.py`.


Issue created by migration from https://trac.sagemath.org/ticket/793





---

archive/issue_comments_004749.json:
```json
{
    "body": "see also #811",
    "created_at": "2007-10-03T16:49:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/793",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/793#issuecomment-4749",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```

see also #811



---

archive/issue_events_002199.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-10-04T19:54:30Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/793",
    "milestone": "sage-2.9",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/793#event-2199"
}
```



---

archive/issue_comments_004750.json:
```json
{
    "body": "See also #965. I've had several requests for this functionality, so it would be great if several of us could spend some time getting this ready for prime time.",
    "created_at": "2008-11-25T19:24:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/793",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/793#issuecomment-4750",
    "user": "https://github.com/kedlaya"
}
```

See also #965. I've had several requests for this functionality, so it would be great if several of us could spend some time getting this ready for prime time.



---

archive/issue_comments_004751.json:
```json
{
    "body": "Attachment [frobenius.patch](tarball://root/attachments/some-uuid/ticket793/frobenius.patch) by dmharvey created at 2009-03-17 19:17:34",
    "created_at": "2009-03-17T19:17:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/793",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/793#issuecomment-4751",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```

Attachment [frobenius.patch](tarball://root/attachments/some-uuid/ticket793/frobenius.patch) by dmharvey created at 2009-03-17 19:17:34



---

archive/issue_comments_004752.json:
```json
{
    "body": "Very basic wrapper attached. This is code by Nick Alexander and myself. Sample:\n\n```\nsage: R.<x> = PolynomialRing(GF(10007))\nsage: H = HyperellipticCurve(x^7 + x + 1)\nsage: time H.frobenius_polynomial()\nCPU times: user 1.62 s, sys: 0.01 s, total: 1.63 s\nWall time: 1.63 s\nx^6 + 4*x^5 + 21884*x^4 - 99088*x^3 + 218993188*x^2 + 400560196*x + 100210147034\n```",
    "created_at": "2009-03-17T19:18:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/793",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/793#issuecomment-4752",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```

Very basic wrapper attached. This is code by Nick Alexander and myself. Sample:

```
sage: R.<x> = PolynomialRing(GF(10007))
sage: H = HyperellipticCurve(x^7 + x + 1)
sage: time H.frobenius_polynomial()
CPU times: user 1.62 s, sys: 0.01 s, total: 1.63 s
Wall time: 1.63 s
x^6 + 4*x^5 + 21884*x^4 - 99088*x^3 + 218993188*x^2 + 400560196*x + 100210147034
```



---

archive/issue_events_002200.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/GeorgSWeber",
    "created_at": "2009-03-31T18:04:22Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/793",
    "milestone": "sage-2.9",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/793#event-2200"
}
```



---

archive/issue_events_002201.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/GeorgSWeber",
    "created_at": "2009-03-31T18:04:22Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/793",
    "milestone": "sage-3.4.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/793#event-2201"
}
```



---

archive/issue_comments_004753.json:
```json
{
    "body": "Looks good to me.\n\nTested against Sage-3.4.1.alpha0.",
    "created_at": "2009-03-31T18:04:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/793",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/793#issuecomment-4753",
    "user": "https://trac.sagemath.org/admin/accounts/users/GeorgSWeber"
}
```

Looks good to me.

Tested against Sage-3.4.1.alpha0.



---

archive/issue_comments_004754.json:
```json
{
    "body": "Several of the internal methods need doctests - the coverage of this patch is not even close to 100%.\n\nCheers,\n\nMichael",
    "created_at": "2009-03-31T21:41:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/793",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/793#issuecomment-4754",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Several of the internal methods need doctests - the coverage of this patch is not even close to 100%.

Cheers,

Michael



---

archive/issue_comments_004755.json:
```json
{
    "body": "But at least the doctests that are there pass for me in my 3.4.1.rc0 merge tree.\n\nCheers,\n\nMichael",
    "created_at": "2009-03-31T22:54:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/793",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/793#issuecomment-4755",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

But at least the doctests that are there pass for me in my 3.4.1.rc0 merge tree.

Cheers,

Michael



---

archive/issue_comments_004756.json:
```json
{
    "body": "Does this mean that if I combine all the functions into one megalithic unreadable function, it would pass review without writing any more doctests?",
    "created_at": "2009-04-01T06:07:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/793",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/793#issuecomment-4756",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```

Does this mean that if I combine all the functions into one megalithic unreadable function, it would pass review without writing any more doctests?



---

archive/issue_comments_004757.json:
```json
{
    "body": "Replying to [comment:9 dmharvey]:\n> Does this mean that if I combine all the functions into one megalithic unreadable function, it would pass review without writing any more doctests?\n\n\nTechnically yes, but I would not consider this the cleanest solution :)\n\nCheers,\n\nMichael",
    "created_at": "2009-04-01T06:18:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/793",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/793#issuecomment-4757",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Replying to [comment:9 dmharvey]:
> Does this mean that if I combine all the functions into one megalithic unreadable function, it would pass review without writing any more doctests?


Technically yes, but I would not consider this the cleanest solution :)

Cheers,

Michael



---

archive/issue_comments_004758.json:
```json
{
    "body": "I consider them to be tested indirectly by the main function.",
    "created_at": "2009-04-01T08:10:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/793",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/793#issuecomment-4758",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```

I consider them to be tested indirectly by the main function.



---

archive/issue_comments_004759.json:
```json
{
    "body": "> I consider them to be tested indirectly by the main function. \n\n\nSo are you refusing to doctest your functions and expect this patch to sit in limbo into either somebody else does it for you or the policy of the sage project for the last two years changes?\n\n> Does this mean that if I combine all the functions into one megalithic \n> unreadable  function, it would pass review without writing any more doctests? \n\n\nNot from me. \n\n -- William",
    "created_at": "2009-04-01T12:50:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/793",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/793#issuecomment-4759",
    "user": "https://github.com/williamstein"
}
```

> I consider them to be tested indirectly by the main function. 


So are you refusing to doctest your functions and expect this patch to sit in limbo into either somebody else does it for you or the policy of the sage project for the last two years changes?

> Does this mean that if I combine all the functions into one megalithic 
> unreadable  function, it would pass review without writing any more doctests? 


Not from me. 

 -- William



---

archive/issue_comments_004760.json:
```json
{
    "body": "I just noticed that the code does not take advantage of the symmetry of the zeta function and so uses a p-adic precision about twice as high as necessary. I withdraw the patch.",
    "created_at": "2009-04-01T13:34:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/793",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/793#issuecomment-4760",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```

I just noticed that the code does not take advantage of the symmetry of the zeta function and so uses a p-adic precision about twice as high as necessary. I withdraw the patch.



---

archive/issue_comments_004761.json:
```json
{
    "body": "Unfortunate.\n\nThe code was excellently commented, in fact the comments of the internal functions were so good, it just slipped by me that the mandatory doctesting lines were missing. (Which IMHO are trivial to add in this patch.)\n\nAnd if it is difficult to find \"special\" doctests for internal functions, one always has the possibility to do (another slightly modified instance of) the \"outer\" computation as a test and write \"#implicit doctest\" as comment. This serves the intended purpose (and I strongly guess neither Michael, nor William, would object). All in all, another to-be-better-documented issue.\n\nWith regard to the p-adic precision, I'd say \"functionality first and optimizations later\" (the patch as-is is mathematically correct :-) ), but that's my own personal opinion.\n\nCheers,\ngsw",
    "created_at": "2009-04-01T18:35:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/793",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/793#issuecomment-4761",
    "user": "https://trac.sagemath.org/admin/accounts/users/GeorgSWeber"
}
```

Unfortunate.

The code was excellently commented, in fact the comments of the internal functions were so good, it just slipped by me that the mandatory doctesting lines were missing. (Which IMHO are trivial to add in this patch.)

And if it is difficult to find "special" doctests for internal functions, one always has the possibility to do (another slightly modified instance of) the "outer" computation as a test and write "#implicit doctest" as comment. This serves the intended purpose (and I strongly guess neither Michael, nor William, would object). All in all, another to-be-better-documented issue.

With regard to the p-adic precision, I'd say "functionality first and optimizations later" (the patch as-is is mathematically correct :-) ), but that's my own personal opinion.

Cheers,
gsw



---

archive/issue_comments_004762.json:
```json
{
    "body": "Attachment [793.patch](tarball://root/attachments/some-uuid/ticket793/793.patch) by dmharvey created at 2009-04-01 19:28:57\n\nLet's try again. New patch should be applied on top of the old.\n\nGeorg: regarding the precision, I am preparing for a talk on Friday, and the slowdown caused by the p-adic precision overestimates actually made a big difference to the presentation.",
    "created_at": "2009-04-01T19:28:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/793",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/793#issuecomment-4762",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```

Attachment [793.patch](tarball://root/attachments/some-uuid/ticket793/793.patch) by dmharvey created at 2009-04-01 19:28:57

Let's try again. New patch should be applied on top of the old.

Georg: regarding the precision, I am preparing for a talk on Friday, and the slowdown caused by the p-adic precision overestimates actually made a big difference to the presentation.



---

archive/issue_comments_004763.json:
```json
{
    "body": "SCORE devel/sage/sage/schemes/hyperelliptic_curves/hyperelliptic_finite_field.py: 100% (6 of 6)\n\nLooks even better to me.\n\nAnd good luck for your presentation!\n\nCheers, gsw",
    "created_at": "2009-04-01T21:03:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/793",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/793#issuecomment-4763",
    "user": "https://trac.sagemath.org/admin/accounts/users/GeorgSWeber"
}
```

SCORE devel/sage/sage/schemes/hyperelliptic_curves/hyperelliptic_finite_field.py: 100% (6 of 6)

Looks even better to me.

And good luck for your presentation!

Cheers, gsw



---

archive/issue_events_002202.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-04-01T23:54:00Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/793",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/793#event-2202"
}
```



---

archive/issue_comments_004764.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-04-01T23:54:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/793",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/793#issuecomment-4764",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_004765.json:
```json
{
    "body": "Merged both patches in Sage 3.4.1.rc0.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-01T23:54:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/793",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/793#issuecomment-4765",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged both patches in Sage 3.4.1.rc0.

Cheers,

Michael
