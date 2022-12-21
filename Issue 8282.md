# Issue 8282: implement victor_miller_basis over an arbitrary base ring

Issue created by migration from Trac.

Original creator: AlexGhitza

Original creation time: 2010-02-16 13:11:56

Assignee: craigcitro

This can now be done as:


```
sage: time bas = victor_miller_basis(2000, prec=200)
CPU times: user 8.44 s, sys: 0.08 s, total: 8.52 s
Wall time: 8.55 s
sage: time bas_mod7 = [ f.change_ring(GF(7)) for f in bas ]
CPU times: user 2.52 s, sys: 0.00 s, total: 2.52 s
Wall time: 2.61 s
```


It would be nice (and presumably much faster and less memory-consuming) to compute the Victor Miller basis *directly over GF(7)*.

