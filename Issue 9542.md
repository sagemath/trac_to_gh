# Issue 9542: optimize znpoly arithmetic -- it's way, way too slow because of the polynomial template thingy

Issue created by migration from https://trac.sagemath.org/ticket/9542

Original creator: was

Original creation time: 2010-07-18 19:18:03

Assignee: AlexGhitza




---

Attachment

speeds up multiplication by a factor of *20* for many benchmarks... but causes a segfault when doctesting rings/arith.py


---

Comment by jpflori created at 2014-02-26 21:53:59

Maybe this can be closed now...
I'll run basic test laters.


---

Comment by jpflori created at 2014-02-26 23:30:28

Changing status from new to needs_review.


---

Comment by jpflori created at 2014-02-26 23:30:28

Based on the same idea (`_mul_no_template_`):

```
sage: K = Integers(2**6)
sage: R.<x> = K[]
sage: f = R([1,2,5,-9]); g = R([1,2,3,4])
sage: %timeit f._mul_zn_poly(g)
100000 loops, best of 3: 5.32 us per loop
sage: %timeit f._mul_(g)
1000000 loops, best of 3: 1 us per loop
sage: %timeit f._mul_no_template(g)
1000000 loops, best of 3: 790 ns per loop
sage: %timeit f*g
1000000 loops, best of 3: 845 ns per loop
```

So it seems the templating overhead is not so terrible.
It also varies a little bit depending on the finite field.
And it does not seem the templating code can be really trimmed down and further optimized.

So I suggest to close this ticket as won't fix.


---

Comment by jpflori created at 2014-02-26 23:30:45

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2014-02-27 22:11:51

Resolution: wontfix
