# Issue 696: SAGE's multivariate gcd sucks over QQ and/or ZZ

Issue created by migration from https://trac.sagemath.org/ticket/696

Original creator: was

Original creation time: 2007-09-19 20:25:11

Assignee: somebody


```

I think those timings are way out of date, since Singular 3 seems
to be *very* fast at mod p multivariate GCD computation, even
though it sucks over QQ.   Check out this paper:

          http://www.cecm.sfu.ca/CAG/papers/brown.ps

It on exactly the problem of GCD over QQ (or equiv ZZ),
and section 2 has a complete description of a gcd algorithm 
that reduces gcd over ZZ to doing gcd's mod p.

Who wants to be a hero -- like Jon Bober and number of partitions -- 
and implement this for Sage, so that multivariate GCD's aren't 
embarrassingly slow in Sage anymore?   This slowness *has* 
been something reported to me on several occasions during 
the last 2 years. 

William
```


NOTE -- I would implement this modular GCD algorithm in Sage, not Singular.

I would also investigate other algorithms mentioned in the paper.


---

Comment by was created at 2007-09-19 20:35:19

See #694 instead!


---

Comment by was created at 2007-09-19 20:35:19

Resolution: duplicate
