# Issue 4229: special functions should use mpfr when available

Issue created by migration from Trac.

Original creator: AlexGhitza

Original creation time: 2008-10-01 09:55:56

Assignee: burcin

CC:  jdemeyer

MPFR has fast implementations for restricted types of arguments in some special functions, e.g. Bessel J and Y with integer order and positive real argument.  We should be using these instead of Pari or Maxima or Scipy whenever that is feasible.

Example:


```
sage: a = RR(2)
sage: timeit("bessel_J(1, a)")
625 loops, best of 3: 370 µs per loop
sage: timeit("a.j1()")
625 loops, best of 3: 13.9 µs per loop
```


That's 26 times faster than Pari.


---

Comment by kcrisman created at 2011-03-16 15:38:19

Or maybe we should use mpmath - there are a number of tickets about that.  Such as Alex's own comment in #3426 :)


---

Comment by kcrisman created at 2011-03-16 15:38:19

Changing priority from major to minor.


---

Comment by burcin created at 2011-06-14 18:07:42

This ticket is too broad, I suggest we close it as invalid.

At the time it was created, there was no general framework to handle these functions. The (not so) new pynac-based symbolics provide this framework. It is true that a lot of work is still needed to sort these numerical evaluation issues out, but we need a separate specific ticket for each issue.

See [symbolics/functions](symbolics-functions) for an overview on the progress of symbolic functions.


---

Comment by burcin created at 2011-06-14 18:07:42

Changing keywords from "" to "sd31".


---

Comment by burcin created at 2011-06-14 18:07:42

Changing status from new to needs_review.


---

Comment by kcrisman created at 2011-06-14 18:09:51

Agreed.  This wiki page solves the problem.


---

Comment by kcrisman created at 2011-06-14 18:09:51

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2011-06-14 20:39:08

Resolution: duplicate
