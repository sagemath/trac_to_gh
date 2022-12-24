# Issue 205: prime_range cast problem

archive/issues_000205.json:
```json
{
    "body": "Assignee: was\n\n\n```\nsage: [ p.is_prime() for p in prime_range(2**160, 2**160+2**12) ]\n---------------------------------------------------------------------------\n<type 'exceptions.OverflowError'>         Traceback (most recent call last)\n \n/Users/nalexand/Devel/sage-alpha8/devel/sage-main/<ipython console> in <module>()\n \n/Users/nalexand/Devel/sage/local/lib/python2.5/site-packages/sage/rings/arith.py in prime_range(start, stop, leave_pari)\n    477     if stop is None:\n    478         start, stop = 2, start\n--> 479     v = pari.primes_up_to_n(stop-1)\n    480     Z = sage.rings.integer.Integer\n    481     if leave_pari:\n }}}\n\nIssue created by migration from https://trac.sagemath.org/ticket/205\n\n",
    "created_at": "2007-01-22T20:12:39Z",
    "labels": [
        "number theory",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-1.9",
    "title": "prime_range cast problem",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/205",
    "user": "was"
}
```
Assignee: was


```
sage: [ p.is_prime() for p in prime_range(2**160, 2**160+2**12) ]
---------------------------------------------------------------------------
<type 'exceptions.OverflowError'>         Traceback (most recent call last)
 
/Users/nalexand/Devel/sage-alpha8/devel/sage-main/<ipython console> in <module>()
 
/Users/nalexand/Devel/sage/local/lib/python2.5/site-packages/sage/rings/arith.py in prime_range(start, stop, leave_pari)
    477     if stop is None:
    478         start, stop = 2, start
--> 479     v = pari.primes_up_to_n(stop-1)
    480     Z = sage.rings.integer.Integer
    481     if leave_pari:
 }}}

Issue created by migration from https://trac.sagemath.org/ticket/205





---

archive/issue_comments_000921.json:
```json
{
    "body": "fix (somewhat lame) for sage > 1.8",
    "created_at": "2007-01-23T23:38:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/205",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/205#issuecomment-921",
    "user": "was"
}
```

fix (somewhat lame) for sage > 1.8



---

archive/issue_comments_000922.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-01-23T23:38:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/205",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/205#issuecomment-922",
    "user": "was"
}
```

Resolution: fixed
