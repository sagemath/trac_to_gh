# Issue 9539: segfault after memory exhausted using GF(9001)((x))

Issue created by migration from https://trac.sagemath.org/ticket/9539

Original creator: fchyzak

Original creation time: 2010-07-18 15:55:11

Assignee: AlexGhitza

CC:  burcin

On a MacBook Pro with 2Go (Mac OS X 10.4.11), filling the memory terminates with a seg fault:

code used:

```
from sage.all import LaurentSeriesRing, GF, timeit
R = LaurentSeriesRing(GF(9001), 'x')
f = R([1, 1])
for i in range(27):
    timeit('g = f*f', number=1, repeat=1) ; f = f*f
```


output is:

```
1 loops, best of 1: 16.5 s per loop
1 loops, best of 1: 28.4 s per loop
1 loops, best of 1: 88.6 s per loop
python(6488) malloc: *** vm_allocate(size=2147614720) failed (error code=3)
python(6488) malloc: *** error: can't allocate region
python(6488) malloc: *** set a breakpoint in szone_error to debug


------------------------------------------------------------
Unhandled SIGBUS: A bus error occured in Sage.
This probably occured because a *compiled* component
of Sage has a bug in it (typically accessing invalid memory)
or is not properly wrapped with _sig_on, _sig_off.
You might want to run Sage under gdb with 'sage -gdb' to debug this.
Sage will now terminate (sorry).
------------------------------------------------------------
```



---

Comment by burcin created at 2010-09-08 11:52:39

Changing assignee from AlexGhitza to rlm.


---

Comment by burcin created at 2010-09-08 11:52:39

Changing component from basic arithmetic to memleak.
