# Issue 3571: ivalue field in integer_mod.pyx shouldn't be public

Issue created by migration from https://trac.sagemath.org/ticket/3571

Original creator: craigcitro

Original creation time: 2008-07-06 20:55:32

Assignee: craigcitro

The `ivalue` field for `IntegerMod_int` is `public`, but it shouldn't be. The following is very frightening, for instance:


```
sage: R = Integers(10)
sage: x = R(2)
sage: x
2
sage: x.ivalue = 33
sage: x
33
sage: R(2)
33
```


It's easy to make this field no longer be public, but lots of things are using the fact that it is, so one needs to go through and make everything work correctly again.


---

Comment by craigcitro created at 2009-01-23 08:01:48

Changing status from new to assigned.


---

Comment by craigcitro created at 2009-01-23 08:01:48

The attached patch fixes this issue, and in fact, gives about a 1.5-2X speedup on multiplying `IntegerMod_int`s. The interesting part is that previous to this patch, the `ivalue` field was occasionally being accessed as a Python attribute instead of a Cython attribute! That's why it broke if we made the field not `public` in the first place. Oops.

BEFORE:


```
sage: R = Integers(100) ; x = R(3) ; y = R(5)
sage: timeit('x*y')
625 loops, best of 3: 403 ns per loop
sage: timeit('x*y')
625 loops, best of 3: 370 ns per loop
sage: timeit('x*y')
625 loops, best of 3: 410 ns per loop
sage: timeit('x*y')
625 loops, best of 3: 405 ns per loop
```


AFTER:


```
sage: R = Integers(100) ; x = R(3) ; y = R(5)
sage: timeit('x*y')
625 loops, best of 3: 190 ns per loop
sage: timeit('x*y')
625 loops, best of 3: 213 ns per loop
sage: timeit('x*y')
625 loops, best of 3: 174 ns per loop
sage: timeit('x*y')
625 loops, best of 3: 191 ns per loop
```



---

Attachment


---

Comment by mabshoff created at 2009-01-23 09:39:41

Resolution: fixed


---

Comment by mabshoff created at 2009-01-23 09:39:41

Merged in Sage 3.3.alpha1

Cheers,

Michael
