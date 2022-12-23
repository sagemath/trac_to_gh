# Issue 5031: get doctesting of matrix/misc.pyx up to 100%; also make A.lift() 20 times faster by moving a "gem"

Issue created by migration from https://trac.sagemath.org/ticket/5031

Original creator: was

Original creation time: 2009-01-20 05:46:23

Assignee: was




---

Comment by was created at 2009-01-20 05:50:07

Some timings

```
BEFORE:
sage: a = random_matrix(GF(19),500)
sage: time b = a.lift()
CPU times: user 0.93 s, sys: 0.02 s, total: 0.95 s
Wall time: 0.96 s
sage: a = random_matrix(GF(19),200,sparse=True)
sage: time b = a.lift()
CPU times: user 0.81 s, sys: 0.01 s, total: 0.82 s
Wall time: 0.82 s

AFTER:
sage: a = random_matrix(GF(19),500)
sage: time b = a.lift()
CPU times: user 0.02 s, sys: 0.01 s, total: 0.04 s
Wall time: 0.04 s
sage: a = random_matrix(GF(19),200,sparse=True)
sage: time b = a.lift()
CPU times: user 0.04 s, sys: 0.00 s, total: 0.04 s
Wall time: 0.04 s
sage: 0.82/0.04
20.5000000000000
```



---

Comment by was created at 2009-01-20 06:28:03

this is against sage-3.3.alpha0


---

Attachment

I get even larger speedups (factor of 21 to 23), the doctest coverage for all 5 touched files is increased, and the code is fine. Positive review.


---

Comment by robertwb created at 2009-01-20 18:07:08

You got to it while I was sleeping... The code looks good to me too, and this cleans things up a lot. +1


---

Comment by mabshoff created at 2009-01-23 09:06:40

Merged in Sage 3.3.alpha1


---

Comment by mabshoff created at 2009-01-23 09:06:40

Resolution: fixed
