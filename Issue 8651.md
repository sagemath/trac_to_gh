# Issue 8651: binomial(n,k) evaluates to zero when 0 is subsituted for k

Issue created by migration from Trac.

Original creator: rhinton

Original creation time: 2010-04-05 12:31:30

Assignee: burcin

CC:  jason

Keywords: symbolic, binomial

We all know binomial(n,0) should be 1.  But we're not getting that answer in the following case.

```
sage: var('n, k')
(n, k)
sage: binomial(n, 0)  # this is OK
1
sage: binomial(n, k).subs(k=0)  # this is a problem!
0
```




---

Comment by burcin created at 2010-04-05 12:48:28

Good catch! I recall this being fixed in `GiNaC` recently. I'll import the relevant patch into pynac and make an updated package.


---

Comment by burcin created at 2010-04-05 12:48:28

Changing keywords from "symbolic, binomial" to "pynac, binomial".


---

Comment by burcin created at 2010-05-05 19:12:48

add doctests


---

Attachment

I uploaded a patch with the doctest, new pynac package with the fix coming soon.


---

Comment by burcin created at 2010-05-06 04:21:22

Changing status from new to needs_review.


---

Comment by burcin created at 2010-05-06 04:21:22

Corresponding pynac package is available at #8903. Note that the new package also contains fixes for #8542, #8688, #8775. Patches from these tickets should be applied before running doctests.


---

Comment by mhansen created at 2010-05-26 04:47:35

Looks good to me.  This can be merged now.


---

Comment by mhansen created at 2010-05-26 04:47:35

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2010-06-06 07:37:40

Resolution: fixed
