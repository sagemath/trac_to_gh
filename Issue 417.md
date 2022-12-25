# Issue 417: Faster GF(p^n) arithmetic for p^n >= 2^16

archive/issues_000417.json:
```json
{
    "body": "Assignee: somebody\n\nCC:  ylchapuy @koffie\n\nThe Pari+Python interface is too slow. ntl.ZZ_pE+Cython should be much faster.\n\nIssue created by migration from https://trac.sagemath.org/ticket/417\n\n",
    "created_at": "2007-08-10T15:15:29Z",
    "labels": [
        "component: basic arithmetic",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "Faster GF(p^n) arithmetic for p^n >= 2^16",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/417",
    "user": "https://github.com/malb"
}
```
Assignee: somebody

CC:  ylchapuy @koffie

The Pari+Python interface is too slow. ntl.ZZ_pE+Cython should be much faster.

Issue created by migration from https://trac.sagemath.org/ticket/417





---

archive/issue_events_001008.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-09-10T02:42:48Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/417",
    "milestone": "sage-wishlist",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/417#event-1008"
}
```



---

archive/issue_events_001009.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-10-27T20:14:17Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/417",
    "milestone": "sage-wishlist",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/417#event-1009"
}
```



---

archive/issue_events_001010.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-10-27T20:14:17Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/417",
    "milestone": "sage-2.8.9",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/417#event-1010"
}
```



---

archive/issue_comments_002047.json:
```json
{
    "body": "Hmm, could this have been fixed by the NTL wrapper rewrite?\n\nCheers,\n\nMichael",
    "created_at": "2007-10-27T20:14:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/417",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/417#issuecomment-2047",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Hmm, could this have been fixed by the NTL wrapper rewrite?

Cheers,

Michael



---

archive/issue_events_001011.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-10-27T20:39:35Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/417",
    "milestone": "sage-2.8.9",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/417#event-1011"
}
```



---

archive/issue_events_001012.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-10-27T20:39:35Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/417",
    "milestone": "sage-2.8.10",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/417#event-1012"
}
```



---

archive/issue_comments_002048.json:
```json
{
    "body": "No, this was not fixed by the NTL wrapper rewrite. NTL still needs to be actually used internally by `FiniteField`. This ticket requires two new implementations. GF(p<sup>n</sup>) for p < (sizeof(long)<<3) and for p >= (sizeof(long)<<3). These are different classes in NTL and should both be wrapped.",
    "created_at": "2007-10-30T15:01:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/417",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/417#issuecomment-2048",
    "user": "https://github.com/malb"
}
```

No, this was not fixed by the NTL wrapper rewrite. NTL still needs to be actually used internally by `FiniteField`. This ticket requires two new implementations. GF(p<sup>n</sup>) for p < (sizeof(long)<<3) and for p >= (sizeof(long)<<3). These are different classes in NTL and should both be wrapped.



---

archive/issue_comments_002049.json:
```json
{
    "body": "Replying to [ticket:417 malb]:\n> The Pari+Python interface is too slow. ntl.ZZ_pE+Cython should be much faster.\nI completely agree.  How much work has been done on this yet and how much work still needs to be done?",
    "created_at": "2011-08-18T17:19:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/417",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/417#issuecomment-2049",
    "user": "https://trac.sagemath.org/admin/accounts/users/johanbosman"
}
```

Replying to [ticket:417 malb]:
> The Pari+Python interface is too slow. ntl.ZZ_pE+Cython should be much faster.
I completely agree.  How much work has been done on this yet and how much work still needs to be done?



---

archive/issue_comments_002050.json:
```json
{
    "body": "I don't think anybody worked on this much. GF(2<sup>e</sup>) was switched to NTL, but nothing else happened. \n\nHowever, the GF(2<sup>e</sup>) should be a reasonable starting point for doing other fields (word-sized primes and general primes). \n\nAlso, we should eventually move sparse moduli interally but that's for another project :)",
    "created_at": "2011-08-18T17:30:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/417",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/417#issuecomment-2050",
    "user": "https://github.com/malb"
}
```

I don't think anybody worked on this much. GF(2<sup>e</sup>) was switched to NTL, but nothing else happened. 

However, the GF(2<sup>e</sup>) should be a reasonable starting point for doing other fields (word-sized primes and general primes). 

Also, we should eventually move sparse moduli interally but that's for another project :)



---

archive/issue_events_001013.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/417",
    "milestone": "sage-2.8.10",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/417#event-1013"
}
```



---

archive/issue_events_001014.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/417",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/417#event-1014"
}
```



---

archive/issue_events_001015.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/417",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/417#event-1015"
}
```



---

archive/issue_events_001016.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/417",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/417#event-1016"
}
```



---

archive/issue_events_001017.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/417",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/417#event-1017"
}
```



---

archive/issue_events_001018.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/417",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/417#event-1018"
}
```



---

archive/issue_events_001019.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/417",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/417#event-1019"
}
```



---

archive/issue_events_001020.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/417",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/417#event-1020"
}
```
