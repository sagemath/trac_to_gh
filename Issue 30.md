# Issue 30: left multiplication of scalar times vector

Issue created by migration from https://trac.sagemath.org/ticket/30

Original creator: was

Original creation time: 2006-09-12 23:26:40

Assignee: somebody

there is currently no easy way for people to implement 
    vectors with left multiplication.  In fact, left multiplication
    doesn't even work right now. 


---

Comment by mabshoff created at 2007-08-24 13:23:40

This seems to work for me:

```
sage: v = vector([1,2,3])
sage: v*2
(2, 4, 6)
sage: 2*v
(2, 4, 6)
```

So, should we close this as "worksforme" or did I misunderstand?

Cheers,

Michael


---

Comment by was created at 2007-08-30 00:00:09

Resolution: fixed
