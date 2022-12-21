# Issue 8309: speedup prime range

Issue created by migration from Trac.

Original creator: robertwb

Original creation time: 2010-02-20 01:49:28

Assignee: was

CC:  craigcitro

Uses Pari's `NEXT_PRIME_VIADIFF` directly, which avoids the intermediate GEN objects. Also adds a `py_ints` option for a 5x speedup, and is much faster for ranges not starting at 0. 


---

Comment by robertwb created at 2010-02-20 01:50:35

Changing status from new to needs_review.


---

Comment by zimmerma created at 2010-02-25 22:53:32

Changing status from needs_review to needs_info.


---

Comment by zimmerma created at 2010-02-25 22:53:32

Robert, an example is missing to demonstrate the speedup.

Paul


---

Attachment


---

Comment by robertwb created at 2010-02-26 08:10:25

Changing status from needs_info to needs_review.


---

Comment by robertwb created at 2010-02-26 08:10:25

BEFORE


```
sage: timeit("prime_range(10)", number=10000)
10000 loops, best of 3: 57.8 µs per loop
sage: timeit("prime_range(100)", number=10000)
10000 loops, best of 3: 61.2 µs per loop
sage: timeit("prime_range(1000)", number=10000)
10000 loops, best of 3: 102 µs per loop
sage: timeit("prime_range(1000,2000)", number=10000)
10000 loops, best of 3: 123 µs per loop
sage: timeit("prime_range(1e6)")
5 loops, best of 3: 36.9 ms per loop
sage: timeit("prime_range(2e6)")
5 loops, best of 3: 69.7 ms per loop
sage: timeit("prime_range(2e6)")
5 loops, best of 3: 69.7 ms per loop
sage: timeit("prime_range(1e6,2e6)")
5 loops, best of 3: 40.6 ms per loop
sage: timeit("prime_range(1e6,1e6+100)")
25 loops, best of 3: 8.21 ms per loop
```


AFTER


```
sage: timeit("prime_range(10)", number=10000)
10000 loops, best of 3: 969 ns per loop
sage: timeit("prime_range(100)", number=10000)
10000 loops, best of 3: 3.24 µs per loop
sage: timeit("prime_range(1000)", number=10000)
10000 loops, best of 3: 30.3 µs per loop
sage: timeit("prime_range(1000,2000)", number=10000)
10000 loops, best of 3: 22.2 µs per loop
sage: timeit("prime_range(1e6)")
25 loops, best of 3: 28.5 ms per loop
sage: timeit("prime_range(2e6)")
5 loops, best of 3: 53.8 ms per loop
sage: timeit("prime_range(2e6)")
5 loops, best of 3: 55 ms per loop
sage: timeit("prime_range(1e6,2e6)")
25 loops, best of 3: 25.6 ms per loop
sage: timeit("prime_range(1e6,1e6+100)")
625 loops, best of 3: 259 µs per loop
```


AFTER INTS


```
sage: timeit("prime_range(10, py_ints=True)", number=10000)
10000 loops, best of 3: 1.27 µs per loop
sage: timeit("prime_range(100, py_ints=True)", number=10000)
10000 loops, best of 3: 3.11 µs per loop
sage: timeit("prime_range(1000, py_ints=True)", number=10000)
10000 loops, best of 3: 11.5 µs per loop
sage: timeit("prime_range(1000, 2000, py_ints=True)", number=10000)
10000 loops, best of 3: 11.7 µs per loop
sage: timeit("prime_range(1e6, py_ints=True)")
125 loops, best of 3: 4.1 ms per loop
sage: timeit("prime_range(2e6, py_ints=True)")
125 loops, best of 3: 7.9 ms per loop
sage: timeit("prime_range(2e6, py_ints=True)")
125 loops, best of 3: 7.83 ms per loop
sage: timeit("prime_range(1e6,2e6, py_ints=True)")
125 loops, best of 3: 3.88 ms per loop
sage: timeit("prime_range(1e6,1e6+100, py_ints=True)")
625 loops, best of 3: 260 µs per loop
```


I also cleaned up the patch a bit (e.g. using pari.init_primes rather than resetting diffptr manually).


---

Comment by zimmerma created at 2010-02-26 10:50:37

Changing status from needs_review to positive_review.


---

Comment by zimmerma created at 2010-02-26 10:50:37

Robert, I got one doctest failure in `graphs/generic_graph.py`. However after cloning again 4.3.3, and testing again with your patch, it worked. Thus it might be to an interference with the other patches I've tried.

On my side (Core 2 Duo) I get:


```
BEFORE:
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: timeit("prime_range(10)", number=10000)
10000 loops, best of 3: 26.5 µs per loop
sage: timeit("prime_range(100)", number=10000)
10000 loops, best of 3: 31 µs per loop
sage: timeit("prime_range(1000)", number=10000)
10000 loops, best of 3: 65 µs per loop
sage: timeit("prime_range(1000,2000)", number=10000)
10000 loops, best of 3: 81.1 µs per loop
sage: timeit("prime_range(1e6)")
25 loops, best of 3: 24.9 ms per loop
sage: timeit("prime_range(2e6)")
5 loops, best of 3: 45.9 ms per loop
sage: timeit("prime_range(2e6)")
5 loops, best of 3: 45.8 ms per loop
sage: timeit("prime_range(1e6,2e6)")
25 loops, best of 3: 28.3 ms per loop
sage: timeit("prime_range(1e6,1e6+100)")
125 loops, best of 3: 5.47 ms per loop
| Sage Version 4.3.3, Release Date: 2010-02-21                       |
| Type notebook() for the GUI, and license() for information.        |
AFTER:
Loading Sage library. Current Mercurial branch is: 8309
sage: timeit("prime_range(10)", number=10000)
10000 loops, best of 3: 649 ns per loop
sage: timeit("prime_range(100)", number=10000)
10000 loops, best of 3: 1.79 µs per loop
sage: timeit("prime_range(1000)", number=10000)
10000 loops, best of 3: 14.6 µs per loop
sage: timeit("prime_range(1000,2000)", number=10000)
10000 loops, best of 3: 10.8 µs per loop
sage: timeit("prime_range(1e6)")
25 loops, best of 3: 14.6 ms per loop
sage: timeit("prime_range(2e6)")
25 loops, best of 3: 30.2 ms per loop
sage: timeit("prime_range(2e6)")
25 loops, best of 3: 30.4 ms per loop
sage: timeit("prime_range(1e6,2e6)")
25 loops, best of 3: 12.7 ms per loop
sage: timeit("prime_range(1e6,1e6+100)")
625 loops, best of 3: 148 µs per loop

AFTER INTS:
sage: sage: timeit("prime_range(10, py_ints=True)", number=10000)
10000 loops, best of 3: 852 ns per loop
sage: sage: timeit("prime_range(100, py_ints=True)", number=10000)
10000 loops, best of 3: 1.73 µs per loop
sage: sage: timeit("prime_range(1000, py_ints=True)", number=10000)
10000 loops, best of 3: 6.95 µs per loop
sage: sage: timeit("prime_range(1000, 2000, py_ints=True)", number=10000)
10000 loops, best of 3: 6.44 µs per loop
sage: sage: timeit("prime_range(1e6, py_ints=True)")
125 loops, best of 3: 2.79 ms per loop
sage: sage: timeit("prime_range(2e6, py_ints=True)")
125 loops, best of 3: 7.15 ms per loop
sage: sage: timeit("prime_range(2e6, py_ints=True)")
125 loops, best of 3: 7.16 ms per loop
sage: sage: timeit("prime_range(1e6,2e6, py_ints=True)")
125 loops, best of 3: 2.34 ms per loop
sage: sage: timeit("prime_range(1e6,1e6+100, py_ints=True)")
625 loops, best of 3: 149 µs per loop
```

Given that py_ints is faster for ranges larger than 100, I wonder why you didn't make it the default. Anyway a positive review. Great work!

Paul


---

Comment by robertwb created at 2010-02-26 11:45:49

Thanks. 

The reason that py_ints isn't on by default is because then one wouldn't be able to do something like


```
for p in prime_range(100):
    if p.divides(N):
        ...
```



---

Comment by mvngu created at 2010-03-03 14:46:02

Resolution: fixed
