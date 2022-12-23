# Issue 2362: Integer digits method

Issue created by migration from https://trac.sagemath.org/ticket/2362

Original creator: jbmohler

Original creation time: 2008-03-01 20:09:20

Assignee: somebody

The digits method should take large bases.


```
sage: n=982352935629356293856239856239852352352
sage: n.digits(928365923856928)
...
<type 'exceptions.OverflowError'>: long int too large to convert to int
```




---

Comment by jbmohler created at 2008-03-02 05:51:15

I've added a patch which fixes this bug and 2170.


```
sage: n=3^100000
sage: time _=n.digits(10)  # evidence of fixing 2170
CPU times: user 0.07 s, sys: 0.00 s, total: 0.07 s
Wall time: 0.07
sage: time _=n.str(10)
CPU times: user 0.02 s, sys: 0.00 s, total: 0.02 s
Wall time: 0.02
sage: time _=n.digits(10^40)  # evidence of fixing this bug
CPU times: user 0.03 s, sys: 0.00 s, total: 0.03 s
Wall time: 0.03
```



---

Comment by was created at 2008-03-02 08:14:35

Could you add the extremely impressive times in your comment above to the docstring. 

By the way, EXCELLENT WORK on this  -- it's fast.  Excellent!


---

Attachment


---

Comment by jbmohler created at 2008-03-03 20:24:09

Use digits.2.patch.

This new patch fixes up some speed regressions compared to unpatched 2.10.2.  It seems that small cases are much better off using the naive base-conversion algorithm.  It also fixes some things so that we are just a bit faster for large input.

Note that I also tweaked the ndigits method just a bit so that it works for arbitrary large input.


---

Attachment

Now, you should use digits.patch

This latest patch has been rebased on 2.10.3


---

Comment by mhansen created at 2008-03-15 22:16:04

Looks good to me.  Note that this basically forces a -ba due to a change in integer.pxd.


---

Comment by mabshoff created at 2008-03-16 00:07:23

Resolution: fixed


---

Comment by mabshoff created at 2008-03-16 00:07:23

Merged digits.patch in Sage 2.10.4.rc0
