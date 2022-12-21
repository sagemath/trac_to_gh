# Issue 528: write new Integer_mod_dense class that wraps NTL directly

Issue created by migration from Trac.

Original creator: dmharvey

Original creation time: 2007-08-30 13:20:50

Assignee: dmharvey

Currently `Integer_mod_dense` wraps the `ZZX` class in `ntl.pyx`. This causes a lot of overhead for small polynomials.


---

Comment by dmharvey created at 2007-09-11 00:29:37

related: #331


---

Attachment

moves Polynomial_integer_dense to cython


---

Comment by dmharvey created at 2007-09-11 15:08:01

The patch `poly-int-dense1.hg` moves `Polynomial_integer_dense` to a new cython file `polynomial_integer_dense_ntl.pyx` and renames the class to `Polynomial_integer_dense_ntl`, and minimal changes needed to make this build and pass tests.

This is the first step in addressing this ticket. Next step will be to change the underlying implementation to work with the NTL ZZX object directly instead of via `ntl.pyx`.

Already there's an improvement in overheads for arithmetic on small objects:

```
sage: R.<x> = PolynomialRing(ZZ)
sage: f = x^2 + x^3 - 5*x^4
sage: g = 47*x^2 + 3
sage: timeit h = f * g
10000 loops, best of 3: 23.8 µs per loop
```

vs

```
100000 loops, best of 3: 17.7 µs per loop
```



---

Comment by robertwb created at 2007-09-11 21:18:18

Some thoughts to consider: 

  * How far away is FLINT from doing the basic arithmetic at least? If it is close, how much effort should be spent on this? 
  * Is there anything to learn from the re-wrapping of NTL by Craig Citro and Joel Mohler?


---

Comment by dmharvey created at 2007-09-11 21:30:06

> How far away is FLINT from doing the basic arithmetic at least? If it is close, how much effort should be spent on this?

I don't know. I am not working on FLINT presently due to lack of time. The amount of effort required to get FLINT to production standard appears to be way more than the time required to get this ticket done.

> Is there anything to learn from the re-wrapping of NTL by Craig Citro and Joel Mohler?

Yes most definitely. I've discussed with this Joel, and I'll be studying that code before moving onto the next phase.


---

Comment by was created at 2007-09-11 21:42:24

I've applied the bundle poly-int-dense1.hg to the official repo for the next SAGE release.


---

Comment by dmharvey created at 2007-09-21 02:31:16

I've added a patch `patch-528.hg`. This makes the `Polynomial_integer_dense_ntl` class talk directly to NTL, instead of wrapping an NTL object from ntl.pyx.

Also it adds many new doctests for polynomials over Z.

It's still pretty damn ugly though. Just the minimum to get the job done. A lot of work is still needed.

I think it basically works, but I wasn't able to run doctests properly because there are currently lots of other doctest failures in the repository.


---

Comment by dmharvey created at 2007-09-23 23:02:00

Note: `patch-528.hg` replaces an old version of the same name; it should be applied directly to sage 2.8.5. It also includes the patch for #738.


---

Comment by dmharvey created at 2007-09-30 19:05:04

hmmm that last patch is currently in conflict. Please ignore it for now; I'm going to work on a new one at SD5 anyway.


---

Attachment

hopefully better now


---

Comment by was created at 2007-10-04 18:24:25

Resolution: fixed
