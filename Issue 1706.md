# Issue 1706: Eigenspaces bug?

Issue created by migration from https://trac.sagemath.org/ticket/1706

Original creator: rlm

Original creation time: 2008-01-07 05:11:17

Assignee: was

CC:  ncalexander@gmail.com

Shouldn't the sum of the dimensions be 2?


```
sage: M = Matrix(CC, [[1,0],[0,1]])
sage: M

[1.00000000000000                0]
[               0 1.00000000000000]
sage: M.eigenspaces()

[
(1.00000000000000, [
(1.00000000000000, 0),
(0, 1.00000000000000)
]),
(1.00000000000000, [
(1.00000000000000, 0),
(0, 1.00000000000000)
])
]
```



---

Comment by craigcitro created at 2008-01-07 05:15:31

The problem is that fcp (factored char poly) returns (x-1)*(x-1), as opposed to (x-1)^2. (That is, it says that there are two distinct factors, each of which happens to be the same.) However, the eigenspaces algorithm implicitly assumes that the terms in self.fcp() are distinct.


---

Comment by jason created at 2008-01-19 06:58:22

More data from Sage 2.9.3 which might shed some light on the problem:


```
sage: M=Matrix(ZZ,[[1,0],[0,1]])
sage: M.fcp()
(x - 1)^2
sage: M=Matrix(QQ,[[1,0],[0,1]])
sage: M.fcp()
(x - 1)^2
sage: M=Matrix(RR,[[1,0],[0,1]])
sage: M.fcp()
(1.00000000000000*x - 1.00000000000000) * (1.00000000000000*x - 1.00000000000000)
sage: M=Matrix(CC,[[1,0],[0,1]])
sage: M.fcp()
(1.00000000000000*x - 1.00000000000000) * (1.00000000000000*x - 1.00000000000000)

```


and 


```
sage: R.<x>=RR[x]
sage: ((x-1)^2).factor()
(1.00000000000000*x - 1.00000000000000) * (1.00000000000000*x - 1.00000000000000)
sage: a=((x-1)^2).factor()
sage: a
(1.00000000000000*x - 1.00000000000000) * (1.00000000000000*x - 1.00000000000000)
sage: a[0]
(1.00000000000000*x - 1.00000000000000, 1)
sage: a[0]==a[1]
True
sage: var('x')
x
sage: Q.<x>=QQ[x]
sage: ((x-1)^2).factor()
(x - 1)^2
```



---

Comment by was created at 2008-02-05 05:01:14

See #2050 for a related ticket, which would likely remove the functionality that is broken above.


---

Comment by ncalexan created at 2008-02-17 00:47:33

If #2050 is applied, this will be fixed (the functionality will by default raise NotImplemented).  Patch is attached to #2050.


---

Comment by mhansen created at 2008-02-27 23:00:35

I can confirm that this is taken care of after #2050 is applied.


---

Comment by mhansen created at 2008-02-28 01:13:16

The patch for #2050 was merged in 2.10.3.rc0 .


---

Comment by mhansen created at 2008-02-28 01:13:16

Resolution: fixed
