# Issue 5732: digits,exact_log,ndigits speed overhaul

Issue created by migration from Trac.

Original creator: jbmohler

Original creation time: 2009-04-10 09:55:10

Assignee: somebody

The Integer.exact_log method is very slow for small input simply because it has never been optimized for this usage.  The attached patch provides a specialized case for small input to exact log.  It also adds a super-fast path for cases when the exact_log can conveniently be computed by log 2 estimation.


---

Comment by jbmohler created at 2009-04-10 10:07:35

Some timings:

```
new patch
sage: n=5^1000
sage: m=2975982357823879528793587928793592
sage: timeit("n.exact_log(m)")
625 loops, best of 3: 714 ns per loop
sage: n=5^50
sage: m=33
sage: timeit("n.exact_log(m)")
625 loops, best of 3: 2.49 Âµs per loop
```



```
Vanilla sage 3.4
sage: n=5^1000
sage: m=2975982357823879528793587928793592
sage: timeit("n.exact_log(m)")
625 loops, best of 3: 620 Âµs per loop
sage: n=5^50
sage: m=33
sage: timeit("n.exact_log(m)")
625 loops, best of 3: 92.2 Âµs per loop
```


I really like the first example :), but it's a bit of a pathology.  There's a relatively narrow band of cases where the log base 2 estimate is quickly provable and exactly correct.


---

Comment by mabshoff created at 2009-04-11 00:32:26

This is quote a nice speedup, but unless it gets reviewed soon it will not be in 3.4.1. Since I do not consider this a blocker I am reassigning this to 3.4.2 until it gets a review.

Cheers,

Michael


---

Attachment

rebased against 4.0


---

Comment by wbhart created at 2009-06-03 14:51:47

I've tested the code using:


```
def random(n):
    a = ZZ.random_element(n)
    return a

def z_exact_log_test(m, n, k):
    for i in range(0, m) :
        a = random(n) + 2
        b = random(k)
        c = a^b
        d = c.exact_log(a)
        if b != d:
            print "Error", b, "!=", d
```


for all sorts of values m, n, k, small large, etc. Everything passes.

The documentation is sufficient, the code reads well and appears correct. There are doctests.

It is also fast as advertised:


```
def zlog(m, n, k):
    for i in range(0, m/1000):
        a = ZZ.random_element(n)+2
        b = ZZ.random_element(k)
        c = a^b
        for i in range (0, 1000):
            c.exact_log(a)
```


Old sage 4.0:


```
sage: time zlog(100000, 2^100, 100)
CPU times: user 23.19 s, sys: 0.19 s, total: 23.38 s
Wall time: 23.40 s

sage: time zlog(100000, 100, 100)
CPU times: user 3.46 s, sys: 0.02 s, total: 3.48 s
Wall time: 3.48 s
```


new times with patch:


```
sage: time zlog(100000, 2^100, 100)
CPU times: user 1.90 s, sys: 0.03 s, total: 1.93 s
Wall time: 1.93 s

sage: time zlog(1000000, 100, 100)
CPU times: user 0.49 s, sys: 0.06 s, total: 0.55 s
Wall time: 0.55 s
```



---

Comment by mhansen created at 2009-06-03 20:19:32

Merged in 4.0.1.rc0.


---

Comment by mhansen created at 2009-06-03 20:19:32

Resolution: fixed
