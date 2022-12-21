# Issue 4623: x^2 is wrong in RealIntervalField

Issue created by migration from Trac.

Original creator: zimmerma

Original creation time: 2008-11-26 14:04:05

Assignee: somebody


```
sage: R=RealIntervalField(53)
sage: x=R(-1,2)
sage: xx=x^2
sage: xx.lower(), xx.upper()
(-2.00000000000000, 4.00000000000000)
```

The result should be (0, 4) instead, since for -1 <= x <= 2, we have 0 <= x^2 <= 4.
(Of course (-2, 4) is a correct enclosure, but any specialist of interval arithmetic
will consider that as a real bug.)


---

Comment by AlexGhitza created at 2009-01-22 18:19:06

Changing type from defect to enhancement.


---

Attachment

The attachment fixes that problem, and adds some doctest examples.

For the reviewer:
* I'm not sure divmod is the best way to test if a number is even
* I'm not sure .abs() is the best way to force the lower bound to 0

Note also that x^0 returns 1, which is not an interval (but that was already the case before
that patch).


---

Attachment

apply on top of the previous patch


---

Comment by AlexGhitza created at 2009-01-24 07:05:35

Looks good to me.  I have tried a few other approaches to the two questions Paul asked above, but they turn out to be slower, so I think the patch is good to go as it is.

I have made a tiny modification that makes the frequent special case exponent=2 almost three times faster.  Apply both patches to 3.3.alpha1.


---

Comment by zimmerma created at 2009-01-24 10:18:56

thanks Alex for your review. I was not aware of x.square(). Then probably we should replace
xq * xq by xq.square() in my patch:

```
sage: x=RealIntervalField(53)((-e,pi))
sage: %timeit x.square()
1000000 loops, best of 3: 769 ns per loop
sage: %timeit (x * x)
1000000 loops, best of 3: 948 ns per loop
```



---

Comment by mabshoff created at 2009-01-24 17:14:10

Resolution: fixed


---

Comment by mabshoff created at 2009-01-24 17:14:10

Merged in Sage 3.3.alpha2


---

Attachment


---

Comment by mabshoff created at 2009-01-24 20:05:03

trac_4623_2.patch looks good and has been merged in Sage 3.3.alpha2.

Cheers,

Michael
