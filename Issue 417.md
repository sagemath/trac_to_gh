# Issue 417: Faster GF(p^n) arithmetic for p^n >= 2^16

archive/issues_000417.json:
```json
{
    "body": "Assignee: somebody\n\nCC:  ylchapuy mderickx\n\nThe Pari+Python interface is too slow. ntl.ZZ_pE+Cython should be much faster.\n\nIssue created by migration from https://trac.sagemath.org/ticket/417\n\n",
    "created_at": "2007-08-10T15:15:29Z",
    "labels": [
        "basic arithmetic",
        "minor",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "Faster GF(p^n) arithmetic for p^n >= 2^16",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/417",
    "user": "malb"
}
```
Assignee: somebody

CC:  ylchapuy mderickx

The Pari+Python interface is too slow. ntl.ZZ_pE+Cython should be much faster.

Issue created by migration from https://trac.sagemath.org/ticket/417





---

archive/issue_comments_002056.json:
```json
{
    "body": "Hmm, could this have been fixed by the NTL wrapper rewrite?\n\nCheers,\n\nMichael",
    "created_at": "2007-10-27T20:14:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/417",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/417#issuecomment-2056",
    "user": "mabshoff"
}
```

Hmm, could this have been fixed by the NTL wrapper rewrite?

Cheers,

Michael



---

archive/issue_comments_002057.json:
```json
{
    "body": "No, this was not fixed by the NTL wrapper rewrite. NTL still needs to be actually used internally by `FiniteField`. This ticket requires two new implementations. GF(p<sup>n</sup>) for p < (sizeof(long)<<3) and for p >= (sizeof(long)<<3). These are different classes in NTL and should both be wrapped.",
    "created_at": "2007-10-30T15:01:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/417",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/417#issuecomment-2057",
    "user": "malb"
}
```

No, this was not fixed by the NTL wrapper rewrite. NTL still needs to be actually used internally by `FiniteField`. This ticket requires two new implementations. GF(p<sup>n</sup>) for p < (sizeof(long)<<3) and for p >= (sizeof(long)<<3). These are different classes in NTL and should both be wrapped.



---

archive/issue_comments_002058.json:
```json
{
    "body": "Replying to [ticket:417 malb]:\n> The Pari+Python interface is too slow. ntl.ZZ_pE+Cython should be much faster.\nI completely agree.  How much work has been done on this yet and how much work still needs to be done?",
    "created_at": "2011-08-18T17:19:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/417",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/417#issuecomment-2058",
    "user": "johanbosman"
}
```

Replying to [ticket:417 malb]:
> The Pari+Python interface is too slow. ntl.ZZ_pE+Cython should be much faster.
I completely agree.  How much work has been done on this yet and how much work still needs to be done?



---

archive/issue_comments_002059.json:
```json
{
    "body": "I don't think anybody worked on this much. GF(2<sup>e</sup>) was switched to NTL, but nothing else happened. \n\nHowever, the GF(2<sup>e</sup>) should be a reasonable starting point for doing other fields (word-sized primes and general primes). \n\nAlso, we should eventually move sparse moduli interally but that's for another project :)",
    "created_at": "2011-08-18T17:30:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/417",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/417#issuecomment-2059",
    "user": "malb"
}
```

I don't think anybody worked on this much. GF(2<sup>e</sup>) was switched to NTL, but nothing else happened. 

However, the GF(2<sup>e</sup>) should be a reasonable starting point for doing other fields (word-sized primes and general primes). 

Also, we should eventually move sparse moduli interally but that's for another project :)
