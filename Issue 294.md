# Issue 294: slowness in mpfr_root

Issue created by migration from Trac.

Original creator: dmharvey

Original creation time: 2007-02-24 17:15:26

Assignee: somebody

The `RealNumber.nth_root()` function (new patch, not yet committed) is very slow when the index is large, e.g.


```
sage: x = RealNumber(8)

sage: time x.nth_root(100000)
CPU times: user 1.97 s, sys: 0.14 s, total: 2.11 s
Wall time: 2.11
 1.00002079463162
```


Seems to be caused by `mpfr_root()` itself; probably needs to be discussed upstream with the mpfr developers.



---

Comment by mabshoff created at 2007-09-10 02:52:34

Any volunteers for this? Maybe it should be checked out if mpfr 2.3.0 still has the problem.

Cheers,

Michael


---

Comment by mabshoff created at 2007-09-15 09:41:43

This is still a problem with Sage 2.8.4.2 + mpfr 2.3:

```
sage: x = RealNumber(8)
sage: time x.nth_root(100)
CPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s
Wall time: 0.00
1.02101212570719
sage: time x.nth_root(1000)
CPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s
Wall time: 0.00
1.00208160507963
sage: time x.nth_root(10000)
CPU times: user 0.10 s, sys: 0.00 s, total: 0.10 s
Wall time: 0.11
1.00020796577605
sage: time x.nth_root(100000)
CPU times: user 1.97 s, sys: 0.15 s, total: 2.12 s
Wall time: 2.12
1.00002079463162
sage: time x.nth_root(1000000)
CPU times: user 32.92 s, sys: 2.14 s, total: 35.07 s
Wall time: 35.07
1.00000207944370
```


Cheers,

Michael


---

Attachment


---

Comment by cwitty created at 2007-10-08 05:24:12

I've attached a patch for nth_root that uses a different algorithm for the cases that were slow before.  Now we get:

```
sage: x = RR(8)
sage: timeit x.nth_root(10)
100000 loops, best of 3: 10.3 µs per loop
sage: timeit x.nth_root(100)
1000 loops, best of 3: 207 µs per loop
sage: timeit x.nth_root(1000)
1000 loops, best of 3: 461 µs per loop
sage: timeit x.nth_root(10000)
1000 loops, best of 3: 461 µs per loop
sage: timeit x.nth_root(100000)
1000 loops, best of 3: 462 µs per loop
sage: timeit x.nth_root(1000000)
1000 loops, best of 3: 456 µs per loop
sage: timeit x.nth_root(10000000)
1000 loops, best of 3: 455 µs per loop
```



---

Comment by was created at 2007-10-13 05:23:44

Resolution: fixed
