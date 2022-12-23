# Issue 9883: slow coercion of polynomial to list over integer mod ring

Issue created by migration from https://trac.sagemath.org/ticket/9884

Original creator: dmharvey

Original creation time: 2010-09-09 16:03:04

Assignee: tbd

Sage 4.5.3, 2.6GHz Opteron, Linux


```
sage: R = Integers(3^20)
sage: S.<x> = PolynomialRing(R)
sage: f = S([R.random_element() for i in range(100)])
sage: timeit("L = f.list()")
125 loops, best of 3: 1.13 ms per loop
```


That's about 29000 cycles per coefficient conversion. See also #9883.


---

Comment by roed created at 2010-09-23 11:30:21

This is sped up by about a factor of 33 by the patch at #9887.  If that's positively reviewed, I would suggest closing this ticket.


---

Comment by mmezzarobba created at 2014-02-02 11:51:39

6.2.beta4, on an Intel(R) Core(TM) i5-3320M CPU `@` 2.60GHz:

```
sage: R = Integers(3^20)
sage: S.<x> = PolynomialRing(R)
sage: f = S([R.random_element() for i in range(100)])
sage: timeit("L = f.list()")
625 loops, best of 3: 166 µs per loop
```

So I only get a factor of ~7 wrt the timings reported by David Harvey.

David (Roe), can you please check if you still observe the same speedup or if there has been a regression in the meantime?


---

Comment by mmezzarobba created at 2014-03-14 16:19:15

Changing status from new to needs_info.


---

Comment by edgarcosta created at 2016-03-22 21:48:40

Version 7.1.beta3 - Intel(R) Core(TM) i5-4278U CPU `@` 2.60GHz

```
sage: R = Integers(3^20)
sage: S.<x> = PolynomialRing(R)
sage: f = S([R.random_element() for i in range(100)])
sage: timeit("L = f.list()")
625 loops, best of 3: 85.8 µs per loop

```


a bit faster on my slightly faster cpu.

Fast enough?
