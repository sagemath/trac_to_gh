# Issue 6899: weird bug taking float of real part of a symbolic

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-09-07 03:21:53

Assignee: burcin

Here's a simple example:

```
sage: a = real((-I*float(1))^2); a
-1.00000000000000
sage: float(a)
Traceback (most recent call last):
...
TypeError: can't convert complex to float; use abs(z)
sage: b = a.simplify(); b
-1.0
sage: float(b)
-1.0
```


Dylan Thurston reported this on sage-support, but in a more complicated situation involving plotting. 


---

Comment by mhansen created at 2009-09-07 20:57:27

Changing status from new to assigned.


---

Comment by mhansen created at 2009-09-07 20:57:27

The issue is that `ComplexNumber.__float__` was automatically throwing an error.  However, that method is used for _conversions_ as well as coercions.  I made it work when the complex number is actually real.


---

Comment by mhansen created at 2009-09-07 20:57:27

Changing assignee from burcin to mhansen.


---

Comment by burcin created at 2009-09-12 18:55:37

faster conversion to float


---

Attachment

attachment:trac_6899.take2.patch doesn't go through python function calls for the conversions. Thus, it is much faster.

With the python calls to `.is_real()` and `.real_part()`:


```
sage: t = CC([2^20,0])
sage: float(t)
1048576.0
sage: %timeit u = float(t)
100000 loops, best of 3: 1.48 µs per loop
```


Using mpfr directly:


```
sage: t = CC([2^20,0])
sage: float(t)
1048576.0
sage: %timeit u = float(t)
1000000 loops, best of 3: 221 ns per loop
```


I give a positive review to Mike's changes. Mike, can you look over the two lines I touched?


---

Comment by kcrisman created at 2009-09-22 21:07:28

I see several doctest failures in rings/polynomial/pbori.pyx (sorry, can't cut and paste it here) involving the stable_hash function.  

Other than that passes tests in sage/rings and plot/complex_plot (perhaps a doctest should be added somewhere in plot/plot that shows this works?), and the mpfr fix seems appropriate, though perhaps an expert should weigh in...


---

Comment by burcin created at 2009-09-22 21:50:59

The errors with `stable_hash()` in `pbori.pyx` are probably a 32/64 bit issue caused by #6177. They definitely have nothing to do with this ticket.


---

Comment by mhansen created at 2009-10-05 04:44:11

I just tested this, and Burcin's changes look good to me.


---

Comment by mhansen created at 2009-10-15 09:49:03

Resolution: fixed
