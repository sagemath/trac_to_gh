# Issue 5959: Better doctest for __cmp__ in primes.py

Issue created by migration from https://trac.sagemath.org/ticket/5959

Original creator: kcrisman

Original creation time: 2009-05-01 15:14:17

Assignee: mabshoff

From sage-devel, regarding whether 

```
Primes()>x^2+x
```

or not



> You should change the doctest to
> 
> sage: P != x^2 + x
> True
> 
> The comparison is completely arbitrary and will be machine specific.
> However equality or not is not arbitrary.

> 
> > sage: cmp(SR(3), x) in [-1,1]
> > True
> 




---

Comment by kcrisman created at 2009-05-01 15:15:07

Based on 3.4.2.rc0


---

Attachment

This is superseded by #5966.

Cheers,

Michael


---

Comment by mabshoff created at 2009-05-03 01:47:22

Resolution: duplicate
