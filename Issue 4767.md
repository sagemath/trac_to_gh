# Issue 4767: [with patch; needs review] magma/sage interface -- speed up conversion of integers and rationals to Magma

Issue created by migration from https://trac.sagemath.org/ticket/4767

Original creator: was

Original creation time: 2008-12-12 06:17:24

Assignee: was

Use hex very carefully (magma has issues, let's say) to convert large integers and rationals to Magma much much more quickly than before.  E.g., in the example below the conversion is 22 times faster than it was before -- 3.2 seconds versus 71.47 seconds!

```
sage: n = ZZ.random_element(x=0,y=2^(10^8))
sage: time k = magma(n)
CPU time: 1.03 s,  Wall time: 3.20 s
sage: time j = magma(str(n))
CPU time: 54.71 s,  Wall time: 71.47 s
sage: 71.47/3.20
22.3343750000000
```


NOTE: The attached patch also speed up is_integral (by a factor of 500!!!) for rational numbers, since I needed that for the rational number conversion speedup.
 
BEFORE:

```
sage: n = -485/82847
sage: n.is_integral()
False
sage: timeit('n.is_integral()')
625 loops, best of 3: 160 µs per loop
```

AFTER:

```
sage: n = -485/82847
sage: n.is_integral()
False
sage: timeit('n.is_integral()')
625 loops, best of 3: 294 ns per loop
```






---

Attachment


---

Comment by malb created at 2008-12-12 14:56:14

patch applies cleanly, reads good, doctests pass.


---

Comment by mabshoff created at 2008-12-12 16:04:41

Resolution: fixed


---

Comment by mabshoff created at 2008-12-12 16:04:41

Merged in Sage 3.2.2.alpha2
