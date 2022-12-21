# Issue 864: Asymptotically slow pari <--> python long conversions

Issue created by migration from Trac.

Original creator: craigcitro

Original creation time: 2007-10-12 19:47:59

Assignee: craigcitro

Keywords: pari

This is really a leftover from ticket #467, split because I wanted the first half of the fix to make it into 2.8.7. Here's a summary of the badness:


```
sage: x = 10^100000

sage: time y = pari(x)
CPU times: user 1.18 s, sys: 0.01 s, total: 1.19 s
Wall time: 1.26

sage: time z = Integer(y)
CPU times: user 0.00 s, sys: 0.00 s, total: 0.01 s
Wall time: 0.02

sage: time u = int(y)
CPU times: user 1.94 s, sys: 1.33 s, total: 3.27 s
Wall time: 3.58

sage: time u = int(Integer(y))
CPU times: user 0.00 s, sys: 0.00 s, total: 0.01 s
Wall time: 0.03


sage: x = 10^1000000

sage: time y = pari(x)
CPU times: user 105.12 s, sys: 1.26 s, total: 106.38 s
Wall time: 121.86

sage: time z = Integer(y)
CPU times: user 0.03 s, sys: 0.02 s, total: 0.05 s
Wall time: 0.09

sage: time u = int(y)
CPU times: user 188.17 s, sys: 145.12 s, total: 333.28 s
Wall time: 364.80

sage: time u = int(Integer(y))
CPU times: user 0.04 s, sys: 0.02 s, total: 0.06 s
Wall time: 0.07
```


And here's the state of affairs after the first patch:


```
sage: x = 10^100000

sage: time y = pari(x)
CPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s
Wall time: 0.00

sage: time z = Integer(y)
CPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s
Wall time: 0.00

sage: time u = int(y)
CPU times: user 1.64 s, sys: 1.09 s, total: 2.73 s
Wall time: 2.79

sage: time u = int(Integer(y))
CPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s
Wall time: 0.00

sage: x = 10^1000000

sage: time y = pari(x)
CPU times: user 0.00 s, sys: 0.00 s, total: 0.01 s
Wall time: 0.01

sage: time z = Integer(y)
CPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s
Wall time: 0.00

sage: time u = int(y)
CPU times: user 220.90 s, sys: 137.34 s, total: 358.24 s
Wall time: 408.11

sage: time u = int(Integer(y))
CPU times: user 0.00 s, sys: 0.00 s, total: 0.01 s
Wall time: 0.01

```


Clearly that third function call needs to be fixed, and it will be within a few days.


---

Comment by craigcitro created at 2007-10-12 19:50:20

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-12-13 11:55:41

Hi Craig,

this has been open a while. The current timings from sage.math:

```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: x = 10^100000
sage: time y = pari(x)
CPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s
Wall time: 0.00 s
sage: time z = Integer(y)
CPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s
Wall time: 0.00 s
sage: time u = int(y)
CPU times: user 0.48 s, sys: 0.00 s, total: 0.48 s
Wall time: 0.48 s
sage: time u = int(Integer(y))
CPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s
Wall time: 0.00 s
```



---

Comment by pbruin created at 2013-09-09 18:40:00

Changing component from interfaces to performance.


---

Comment by pbruin created at 2013-09-09 18:40:00

I am uploading a patch that implements conversion from PARI `t_INT` to Python long via an intermediate `mpz_t`, so `long(y)` essentially does `long(Integer(y))`.

Some timings:

```
sage: x = 10^1000000
sage: %timeit y=pari(x)
10000 loops, best of 3: 197 us per loop
sage: %timeit z=Integer(y)
100 loops, best of 3: 4.11 ms per loop
sage: %timeit u=long(y)
100 loops, best of 3: 13 ms per loop
sage: %timeit u=long(Integer(y))
100 loops, best of 3: 13.8 ms per loop

sage: x = 10^10000000
sage: %timeit y=pari(x)                                                         
100 loops, best of 3: 5.57 ms per loop
sage: %timeit z=Integer(y)
100 loops, best of 3: 2.94 ms per loop
sage: %timeit u=long(y)
100 loops, best of 3: 13.9 ms per loop
sage: %timeit u=long(Integer(y))
100 loops, best of 3: 13.8 ms per loop
```



---

Comment by pbruin created at 2013-09-09 18:40:00

Changing status from new to needs_review.


---

Attachment


---

Comment by jdemeyer created at 2013-10-29 07:45:31

Replying to [comment:4 pbruin]:
> so `long(y)` essentially does `long(Integer(y))`.
Why not literally do `long(Integer(y))` then and save many lines of code?


---

Comment by jdemeyer created at 2013-10-29 07:49:32

Note that this works:

```
sage: Integer(pari("Mod(2,7)"))
2
```

so you would get these cases for free...


---

Comment by pbruin created at 2013-10-29 11:00:42

Replying to [comment:5 jdemeyer]:
> Replying to [comment:4 pbruin]:
> > so `long(y)` essentially does `long(Integer(y))`.
> Why not literally do `long(Integer(y))` then and save many lines of code?
I thought that the penalty for creating an `Integer` was quite heavy in some cases; for example, with the current patch applied, I get

```
sage: y=pari(10^10000)
sage: %timeit -c -r 1 u=long(y)
100000 loops, best of 1: 12.2 us per loop
sage: %timeit -c -r 1 u=long(Integer(y))
10000 loops, best of 1: 19.6 us per loop
```

However, I just tried implementing `gen.__long__(self)` as `return long(Integer(self))`, and it is just as fast, thanks to Cython I guess.  I also agree that `long(pari("Mod(2,7)"))` is nice to get for free.  New patch coming soon.


---

Comment by jdemeyer created at 2013-10-29 11:13:38

Changing status from needs_review to needs_work.


---

Attachment


---

Comment by pbruin created at 2013-10-29 12:16:18

apply trac_864-pari_int_long_conversion.patch


---

Comment by pbruin created at 2013-10-29 12:16:18

Changing status from needs_work to needs_review.


---

Comment by jdemeyer created at 2013-10-31 08:22:28

Looks good!


---

Comment by jdemeyer created at 2013-10-31 08:22:28

Resolution: fixed
