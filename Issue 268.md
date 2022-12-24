# Issue 268: IntegerMod sqrt() doesn't work for non-prime moduli

archive/issues_000268.json:
```json
{
    "body": "Assignee: somebody\n\nThis one's tricky; not sure the best way to proceed. The problem is that IntegerMod's `sqrt()` function uses PARI for the underlying functionality, but PARI doesn't work when the modulus is not a prime, even though you would hope it still works when the modulus is a *prime power*.\n\nRelevant reading is the `sqrt` function at\n\nhttp://www.skalatan.de/pariguide/doc/Transcendental_functions.html#sqrt\n\ne.g. some weirdness:\n\n\n```\nsage: Mod(4, 5).sqrt()\n 2\n\nsage: Mod(4, 25).sqrt()\n...\n<type 'exceptions.ValueError'>: self must be a square.\n\nsage: pari(Mod(4, 25)).sqrt()\n...\n<class 'gen.PariError'>:  (8)\n\nsage: pari(Mod(4, 125)).sqrt()\n...\n<class 'gen.PariError'>: non quadratic residue in gsqrt (51)\n```\n\n\nIt would be possible I guess to cast to a pari p-adic, but that would involve testing the modulus of the ring for being a prime power on every sqrt() invocation... seems horribly inefficient.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/268\n\n",
    "created_at": "2007-02-17T21:49:03Z",
    "labels": [
        "basic arithmetic",
        "major",
        "bug"
    ],
    "title": "IntegerMod sqrt() doesn't work for non-prime moduli",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/268",
    "user": "dmharvey"
}
```
Assignee: somebody

This one's tricky; not sure the best way to proceed. The problem is that IntegerMod's `sqrt()` function uses PARI for the underlying functionality, but PARI doesn't work when the modulus is not a prime, even though you would hope it still works when the modulus is a *prime power*.

Relevant reading is the `sqrt` function at

http://www.skalatan.de/pariguide/doc/Transcendental_functions.html#sqrt

e.g. some weirdness:


```
sage: Mod(4, 5).sqrt()
 2

sage: Mod(4, 25).sqrt()
...
<type 'exceptions.ValueError'>: self must be a square.

sage: pari(Mod(4, 25)).sqrt()
...
<class 'gen.PariError'>:  (8)

sage: pari(Mod(4, 125)).sqrt()
...
<class 'gen.PariError'>: non quadratic residue in gsqrt (51)
```


It would be possible I guess to cast to a pari p-adic, but that would involve testing the modulus of the ring for being a prime power on every sqrt() invocation... seems horribly inefficient.


Issue created by migration from https://trac.sagemath.org/ticket/268





---

archive/issue_comments_001259.json:
```json
{
    "body": "It works now in age-2.8.1.",
    "created_at": "2007-08-18T18:11:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/268",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/268#issuecomment-1259",
    "user": "@williamstein"
}
```

It works now in age-2.8.1.



---

archive/issue_comments_001260.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-08-18T18:11:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/268",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/268#issuecomment-1260",
    "user": "@williamstein"
}
```

Resolution: fixed
