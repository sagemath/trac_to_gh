# Issue 9885: slow coercion from integer mod ring to integer ring, part 2

Issue created by migration from https://trac.sagemath.org/ticket/9886

Original creator: dmharvey

Original creation time: 2010-09-09 16:07:25

Assignee: tbd

Sage 4.5.3, 2.6GHz Opteron, Linux

This is ok:


```
sage: R = Integers(3^20)
sage: u = R(2)
sage: timeit("z = u.lift()")
625 loops, best of 3: 351 ns per loop
```


This is not:

```
sage: timeit("z = ZZ(u)")
625 loops, best of 3: 37.9 µs per loop
```


Wow. See also #9885 for a not-quite-as-insane version of this.



---

Comment by roed created at 2010-09-23 11:27:56

The patch at #9887 should fix this, but it doesn't.  I'm not sure why.


---

Comment by roed created at 2010-10-15 07:43:59

I figured out why.  Hashing for R is slow, and ZZ._convert_map_hash needs to compute hash(R) to get the appropriate morphism.  See #10130 for a patch fixing this.


---

Comment by mmezzarobba created at 2014-03-14 17:19:14

Changing status from new to needs_review.


---

Comment by mmezzarobba created at 2014-03-14 17:19:14

sage-6.2.beta4:

```
sage: sage: timeit("z = u.lift()")
625 loops, best of 3: 142 ns per loop
sage: sage: timeit("z = ZZ(u)")
625 loops, best of 3: 280 ns per loop
```



---

Comment by rws created at 2014-03-24 16:55:21

Similar relative result here. (However, my times are 3x slower with 3GHz AMD Phenom, fascinating).


---

Comment by rws created at 2014-03-24 16:55:21

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2014-03-31 15:04:49

Resolution: duplicate
