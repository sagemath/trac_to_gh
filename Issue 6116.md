# Issue 6116: error in real literal -> RIF conversion

Issue created by migration from https://trac.sagemath.org/ticket/6116

Original creator: robertwb

Original creation time: 2009-05-21 20:13:01

Assignee: somebody


```
sage: RIF(21/10).diameter()
2.11471052309554e-16
sage: RIF(2.1).diameter()
0.000000000000000
```



---

Comment by jdemeyer created at 2015-08-21 20:28:34

I don't think this is a bug, it's just the way how real literals work...


---

Comment by jdemeyer created at 2015-08-21 20:28:34

Changing status from new to needs_review.


---

Comment by jdemeyer created at 2015-08-21 20:30:00

And if you really want the real literal `2.1` to behave like `21/10`, there are a lot more bugs than just this one.


---

Comment by vdelecroix created at 2015-09-17 02:59:15

This is more about floating point rather than real literal

```
sage: a = 1.0 * RR(2.1)
sage: type(a)
<type 'sage.rings.real_mpfr.RealNumber'>
sage: RIF(a).lower() == RIF(a).upper() == a
True
```

And the last line would be true given *any* floating point (with 53 bits of precision).

Though, it would be nice to explain the difference between `RIF(2.1)` and `RIF(21/10)` in the documentation of `RIF`. Don't you think?

Vincent


---

Comment by vdelecroix created at 2015-09-17 02:59:28

Changing status from needs_review to needs_info.


---

Comment by embray created at 2018-08-14 17:00:51

Resolution: worksforme


---

Comment by embray created at 2018-08-14 17:00:51

The docs for `RIF` currently state:


```
 |      Values which can be represented as an exact floating-point number
 |      (of the precision of this ``RealIntervalField``) result in a precise
 |      interval, where the lower bound is equal to the upper bound (even
 |      if they print differently). Other values typically result in an
 |      interval where the lower and upper bounds are adjacent
 |      floating-point numbers.
```


and goes on to provide several examples, e.g. both with rational and floating point arguments.
