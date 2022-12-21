# Issue 4874: performance issue for generic polynomial rings

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-12-24 18:51:32

Assignee: somebody


```
replacing multiplications by shift in quo_rem found
polynomial_element_generic.py gives great improvement on this tiny
example:

sage: R.<x>=PolynomialRing(GF(4,'a'))
sage: P=R.random_element(20)
sage: Q=R.random_element(256)
sage: time Q % P

before:
CPU time: 0.08 s,  Wall time: 0.08 s

after:
CPU time: 0.74 s,  Wall time: 0.74 s

should be very easy to fix
the diff is:

545,549c545,547
<             aaa = (R.leading_coefficient()/B.leading_coefficient())
<             bbb = X**(R.degree()-B.degree())
<             S = aaa * bbb
<             Q += S
<             R -= S*B
---
>             aaa = P(R.leading_coefficient()/B.leading_coefficient())
>             Q += aaa.shift(R.degree()-B.degree())
>             R -= (aaa * B).shift(R.degree()-B.degree())

```


Credit should go to "yannlaiglechapuy".

This came up in sage-devel. 


---

Comment by ylchapuy created at 2009-01-06 19:40:49

patch added


---

Comment by mabshoff created at 2009-01-06 19:52:31

Thanks for the patch.

For the credit situation: "yannlaiglechapuy" in real life is "Yann Laigle-Chapuy" :)

Assigned to 3.3 since it would be nice to get this in due to its improved performance.

Cheers,

Michael


---

Attachment


---

Comment by cremona created at 2009-01-18 17:50:40

Review: Patch looks good, applies cleanly to 3.2.3, all tests in rings/polynomial pass.  Publish!


---

Comment by mabshoff created at 2009-01-19 03:45:46

Merged in Sage 3.3.alpha0


---

Comment by mabshoff created at 2009-01-19 03:45:46

Resolution: fixed
