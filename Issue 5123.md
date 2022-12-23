# Issue 5123: add univariate polynomial xgcd over GF(p) to sage

Issue created by migration from https://trac.sagemath.org/ticket/5123

Original creator: was

Original creation time: 2009-01-28 20:57:39

Assignee: somebody

This caused me trouble when preparing for my class today:


```
sage: k.<X> = GF(2)[]
sage: xgcd(X^2, X+1)
Traceback (most recent call last):
...
NotImplementedError
sage: (X^2).xgcd(X+1)
Traceback (most recent call last):
...
NotImplementedError
```


Note that PARI can do this, so that's an easy shortcut to implement *something*:

```
sage: pari(X^2).xgcd(X+1)
(Mod(1, 2), Mod(1, 2), Mod(1, 2)*X + Mod(1, 2))
```



---

Comment by mhansen created at 2009-06-05 01:19:32

Resolution: invalid


---

Comment by mhansen created at 2009-06-05 01:19:32

Fixed by #5393
