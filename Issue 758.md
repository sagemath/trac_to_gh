# Issue 758: Use NTL directly in Z/nZ polynomials

Issue created by migration from Trac.

Original creator: robertwb

Original creation time: 2007-09-28 11:52:26

Assignee: somebody

It can be vastly faster. There are several layers now...stripping them out one by one. 


```
sage: f = Integers(101)['x'](range(10))
sage: time for _ in range(10^5): g = f*f
CPU time: 2.97 s,  Wall time: 3.00 s

sage: f = Integers(100)['x'](range(10))
sage: time for _ in range(10^5): g = f*f
CPU time: 0.17 s,  Wall time: 0.18 s
```


(This is not quite fair because one is using ZZ_p and one is using zz_p, but there is only a factor of <2 between those in NTL.) 


---

Comment by robertwb created at 2007-09-28 11:53:29

Changing assignee from somebody to robertwb.


---

Comment by robertwb created at 2007-09-28 11:53:29

See also #757


---

Comment by robertwb created at 2007-09-28 11:53:29

Changing status from new to assigned.


---

Comment by robertwb created at 2007-09-30 07:50:40

NTL now used for all composite modn


---

Attachment

The latest bundle includes improvements to Laurent series, Monsky-Waschnitzer computations MUCH faster now (just waiting on fast p-adic linear algebra).


---

Comment by mabshoff created at 2007-10-21 14:10:17

It seems that this still could be applicable, even though it is somewhat faster (NTL rewrite, coercion?)

```
mabshoff`@`sage:/tmp/Work-mabshoff/sage-2.8.8$ sage
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 2.8.8, Release Date: 2007-10-20                       |
| Type notebook() for the GUI, and license() for information.        |
sage: sage: f = Integers(100)['x'](range(10))
sage: sage: time for _ in range(10^5): g = f*f
CPU times: user 0.23 s, sys: 0.04 s, total: 0.27 s
Wall time: 0.27
sage: sage: f = Integers(101)['x'](range(10))
sage: sage: time for _ in range(10^5): g = f*f
CPU times: user 2.12 s, sys: 0.03 s, total: 2.15 s
Wall time: 2.15
```

Cheers,

Michael


---

Comment by malb created at 2007-10-23 21:05:15

Resolution: fixed


---

Comment by malb created at 2007-10-23 21:05:15

This patch seems to be 'in' already. Closing therefor and sending e-mail to author.
