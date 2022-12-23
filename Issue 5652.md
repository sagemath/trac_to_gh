# Issue 5652: powermod is slower than Integer.power_mod

Issue created by migration from https://trac.sagemath.org/ticket/5652

Original creator: bober

Original creation time: 2009-03-31 20:51:20

Assignee: somebody

CC:  mvngu was

Consider the following example:


```
sage: time a = power_mod(5, 10^2000, 10^3000)
CPU times: user 3.67 s, sys: 0.00 s, total: 3.67 s
Wall time: 3.67 s
sage: time b = 5.powermod(10^2000, 10^3000)  
CPU times: user 2.82 s, sys: 0.00 s, total: 2.83 s
Wall time: 2.84 s
sage: a == b
True
sage: time a = power_mod(5, 10^4000, 10^7000)
CPU times: user 27.17 s, sys: 0.01 s, total: 27.18 s
Wall time: 27.30 s
sage: time b = 5.powermod(10^4000, 10^7000)  
CPU times: user 21.38 s, sys: 0.04 s, total: 21.42 s
Wall time: 21.44 s
sage: a == b
True
```


(The problem is that power_mod() uses generic code, while Integer.powermod() uses gmp, which is faster.)


---

Comment by burcin created at 2009-07-15 19:50:44

This is a duplicate of #5082.

I suggest it is closed as a duplicate. Since trac doesn't let me, Minh or William, as release managers, can you close this?


---

Comment by mvngu created at 2009-07-15 19:53:45

Replying to [comment:1 burcin]:
> This is a duplicate of #5082.
> 
> I suggest it is closed as a duplicate. Since trac doesn't let me, Minh or William, as release managers, can you close this?
I don't have admin privileges on trac, so I can't close tickets at the moment. I've merged about 5 tickets so far, but their status has not been set accordingly.


---

Comment by mvngu created at 2009-07-21 03:20:04

Resolution: duplicate
