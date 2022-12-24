# Issue 5999: faster recognise if there is no discrete log

archive/issues_005999.json:
```json
{
    "body": "Assignee: @williamstein\n\nKeywords: discrete log, factor\n\nJust one example:\nsage: n=15*(factorial(54)+1);a=Mod(8,n);b=Mod(7,n);discrete_log(a,b)\n\nAnd this takes lots of time, because sage first factorize n, and this takes about 4 minutes on my pc. However after finding 3 and 5 as primefactors of n you can immediately observe that `7^x==8 mod 15` is unsolvable so the original problem also.\n\nSo the idea is that: get \"small\" prime(power) divisors of n by trial division/another method, and when you find a primepower divisor then check if the problem is still solvable or not.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5999\n\n",
    "created_at": "2009-05-06T18:57:37Z",
    "labels": [
        "number theory",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "faster recognise if there is no discrete log",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5999",
    "user": "gerrob"
}
```
Assignee: @williamstein

Keywords: discrete log, factor

Just one example:
sage: n=15*(factorial(54)+1);a=Mod(8,n);b=Mod(7,n);discrete_log(a,b)

And this takes lots of time, because sage first factorize n, and this takes about 4 minutes on my pc. However after finding 3 and 5 as primefactors of n you can immediately observe that `7^x==8 mod 15` is unsolvable so the original problem also.

So the idea is that: get "small" prime(power) divisors of n by trial division/another method, and when you find a primepower divisor then check if the problem is still solvable or not.

Issue created by migration from https://trac.sagemath.org/ticket/5999


