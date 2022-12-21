# Issue 9887: matrix multiplication over integer mod ring is slow

Issue created by migration from Trac.

Original creator: dmharvey

Original creation time: 2010-09-09 16:21:26

Assignee: tbd

Sage 4.5.3, 2.6GHz Opteron, Linux

This is ok:

```
sage: M1 = Matrix([[randrange(3^20) for i in range(100)] for j in range(100)])
sage: M2 = Matrix([[randrange(3^20) for i in range(100)] for j in range(100)])
sage: timeit("M3 = M1 * M2")
5 loops, best of 3: 45.6 ms per loop
```


(That's about 4 times slower than Magma, but I can put up with that, that's a ticket for another day.)

Here is the problem:

```
sage: R = Integers(3^20)
sage: M1 = Matrix([[R.random_element() for i in range(100)] for j in range(100)])
sage: M2 = Matrix([[R.random_element() for i in range(100)] for j in range(100)])
sage: timeit("M3 = M1 * M2")
5 loops, best of 3: 877 ms per loop
```


In other words, I can multiply the matrices over R roughly 20x faster by multiplying over Z and then reducing! That's ridiculous!



---

Comment by robertwb created at 2010-09-09 16:29:27

I don't think anything has gone into non-word-sized modulus, so this is probably using totally generic per-element wrapping code :(. Should be an easy fix to get better than this, doing something real would be a bit more work.


---

Comment by kedlaya created at 2016-04-10 04:02:21

I just tried the timings again:

```
sage: sage: M1 = Matrix([[randrange(3^20) for i in range(100)] for j in range(100)])
sage: sage: M2 = Matrix([[randrange(3^20) for i in range(100)] for j in range(100)])
sage: sage: timeit("M3 = M1 * M2")
125 loops, best of 3: 5.62 ms per loop
sage: sage: R = Integers(3^20)
sage: sage: M1 = Matrix([[R.random_element() for i in range(100)] for j in range(100)])
sage: sage: M2 = Matrix([[R.random_element() for i in range(100)] for j in range(100)])
sage: sage: timeit("M3 = M1 * M2")
5 loops, best of 3: 530 ms per loop
```

so now the discrepancy is up to a factor of 100!

My recollection is that lifting the multiplication up to Z is in fact the correct algorithmic approach. In practice, this hands the problem off to FLINT, where (in this size range) the multiplication is done multimodular.


---

Comment by kedlaya created at 2016-08-17 01:08:23

See #12177 for a related discussion.


---

Comment by aly.deines created at 2017-10-22 18:32:02

Changing keywords from "" to "sd90".


---

Comment by kedlaya created at 2017-10-24 04:22:51

There appears to be special-purpose code using Linbox for modulus up to 2<sup>23</sup> in `sage/matrix/matrix_modn_dense_double.pyx` and `sage/matrix/matrix_modn_dense_float.pyx`. To handle this issue, it would be best to create a file `sage/matrix/matrix_modn_dense.pyx` in which we create the class `Matrix_modn_dense` with a special `_mul_` method. But we should make sure not to create a regression by disconnecting the existing code for smaller moduli.
