# Issue 9882: slow coercion of list to polynomial over integer mod ring

Issue created by migration from https://trac.sagemath.org/ticket/9883

Original creator: dmharvey

Original creation time: 2010-09-09 16:00:33

Assignee: tbd

Sage 4.5.3, 2.6GHz Opteron, Linux: 


```
sage: R = Integers(3^20)
sage: S.<x> = PolynomialRing(R)
sage: L = [R.random_element() for i in range(100)]
sage: timeit("f = S(L)")
125 loops, best of 3: 4.79 ms per loop
```


That's about 124000 cycles per coefficient conversion. Compare to the cost of multiplying polynomials of the same degree:

```
sage: f = S([R.random_element() for i in range(100)])
sage: g = S([R.random_element() for i in range(100)])
sage: timeit("h = f * g")
625 loops, best of 3: 31.8 µs per loop
```




---

Comment by roed created at 2010-09-23 11:31:28

This is sped up by about a factor of 200 by the patch at #9887. If that's positively reviewed, I would suggest closing this ticket.


---

Comment by mmezzarobba created at 2014-02-02 11:48:23

Changing status from new to needs_review.


---

Comment by mmezzarobba created at 2014-02-02 11:48:23

With sage-6.1:

```
sage: sage: R = Integers(3^20)
sage: sage: S.<x> = PolynomialRing(R)
sage: sage: L = [R.random_element() for i in range(100)]
sage: sage: timeit("f = S(L)")
625 loops, best of 3: 49.6 µs per loop
sage: sage: L = [R.random_element() for i in range(1000)]
sage: sage: timeit("f = S(L)")
625 loops, best of 3: 388 µs per loop

sage: sage: f = S([R.random_element() for i in range(100)])
sage: sage: g = S([R.random_element() for i in range(100)])
sage: sage: timeit("h = f * g")
625 loops, best of 3: 10.9 µs per loop
```



---

Comment by aapitzsch created at 2014-02-09 21:14:08

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2014-02-11 21:22:19

Resolution: duplicate
