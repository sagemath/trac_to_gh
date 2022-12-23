# Issue 1043: constructing number field with check=False doesn't behave as it should

Issue created by migration from https://trac.sagemath.org/ticket/1043

Original creator: was

Original creation time: 2007-10-31 21:08:39

Assignee: was

Why does this take any time?  It shouldn't:


```
sage: p = next_prime(10^24); q = next_prime(10^26); D = p*q; D
sage: time K.<b> = NumberField(x^2 - D, check=False)
CPU time: 2.39 s,  Wall time: 3.10 s
```



---

Comment by was created at 2007-11-03 15:32:07

Robert bradshaw can easily fix this.


---

Comment by robertwb created at 2007-11-04 02:13:24

Resolution: duplicate


---

Comment by robertwb created at 2007-11-04 02:13:24

See #1055
