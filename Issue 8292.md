# Issue 8292: improvements to eisenstein_series_qexp

Issue created by migration from Trac.

Original creator: AlexGhitza

Original creation time: 2010-02-17 11:56:01

Assignee: craigcitro

The attached patch makes the following changes to `eisenstein_series_qexp`:

* removes the workaround at the end of the method, since it is no longer needed
* a few small modifications that speed things up a bit:

BEFORE THE PATCH:

```
sage: timeit("eisenstein_series_qexp(4, 100)")
125 loops, best of 3: 6.19 ms per loop
sage: timeit("eisenstein_series_qexp(4, 1000)")
5 loops, best of 3: 56.4 ms per loop
sage: timeit("eisenstein_series_qexp(4, 10000)")
5 loops, best of 3: 568 ms per loop
sage: timeit("eisenstein_series_qexp(4, 100000)")
5 loops, best of 3: 5.84 s per loop
sage: timeit("eisenstein_series_qexp(6, 100)")
125 loops, best of 3: 6.26 ms per loop
sage: timeit("eisenstein_series_qexp(6, 1000)")
5 loops, best of 3: 57 ms per loop
sage: timeit("eisenstein_series_qexp(6, 10000)")
5 loops, best of 3: 575 ms per loop
sage: timeit("eisenstein_series_qexp(6, 100000)")
5 loops, best of 3: 5.97 s per loop
sage: timeit("eisenstein_series_qexp(100, 1000)")
5 loops, best of 3: 100 ms per loop
sage: timeit("eisenstein_series_qexp(100, 10000)")
5 loops, best of 3: 1.21 s per loop
sage: timeit("eisenstein_series_qexp(1000, 10000)")
5 loops, best of 3: 12.9 s per loop
```


AFTER THE PATCH:

```
sage: timeit("eisenstein_series_qexp(4, 100)")
125 loops, best of 3: 2.21 ms per loop
sage: timeit("eisenstein_series_qexp(4, 1000)")
25 loops, best of 3: 20.5 ms per loop
sage: timeit("eisenstein_series_qexp(4, 10000)")
5 loops, best of 3: 220 ms per loop
sage: timeit("eisenstein_series_qexp(4, 100000)")
5 loops, best of 3: 2.41 s per loop
sage: timeit("eisenstein_series_qexp(6, 100)")
125 loops, best of 3: 2.24 ms per loop
sage: timeit("eisenstein_series_qexp(6, 1000)")
25 loops, best of 3: 21 ms per loop
sage: timeit("eisenstein_series_qexp(6, 10000)")
5 loops, best of 3: 223 ms per loop
sage: timeit("eisenstein_series_qexp(6, 100000)")
5 loops, best of 3: 2.54 s per loop
sage: timeit("eisenstein_series_qexp(100, 1000)")
5 loops, best of 3: 50.6 ms per loop
sage: timeit("eisenstein_series_qexp(100, 10000)")
5 loops, best of 3: 641 ms per loop
sage: timeit("eisenstein_series_qexp(1000, 10000)")
5 loops, best of 3: 8.62 s per loop
```




---

Attachment


---

Comment by mraum created at 2010-11-05 15:50:11

Changing status from new to needs_info.


---

Comment by mraum created at 2010-11-05 15:50:11

This is already covered by the cythonification of the Eisenstein series. I propose we close this ticket. Any objections, Alex?


---

Comment by AlexGhitza created at 2010-11-05 20:47:29

Changing status from needs_info to needs_review.


---

Comment by AlexGhitza created at 2010-11-05 20:47:29

That sounds right.

I'm marking this as "positive review" so it gets picked up.

To the release manager: please close this, as the issue has already been addressed by #6671.


---

Comment by AlexGhitza created at 2010-11-05 20:47:44

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2010-11-07 10:23:00

Resolution: duplicate
