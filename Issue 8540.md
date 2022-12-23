# Issue 8540: ** BLOCKER ** very simple basic sqrt simplification totally broken bad

Issue created by migration from https://trac.sagemath.org/ticket/8540

Original creator: was

Original creation time: 2010-03-15 05:17:30

Assignee: burcin

CC:  robertwb mhansen


```
sage: a = 3/4
sage: b = a^(-1/2)
sage: b^2
12
```


But it should be 4/3.  

Reported by Paul Nelson, a grad student at Caltech.


---

Comment by was created at 2010-03-16 03:58:09

This serious bug is present in sage-4.0, but not in 3.4.2, so it was caused in the switch to Pynac.


---

Comment by jason created at 2010-03-16 05:25:00

Even earlier than the square:


```
sage: (3/4)^(-1/2)
6*sqrt(1/3)
sage: n((.75)^(-1/2))
1.15470053837925
sage: n(6*sqrt(1/3))
3.46410161513775
```



---

Comment by burcin created at 2010-03-16 09:17:38

During the push for the switch, some code was added to simplify these cases (where the base and exponent are rational, but the result is not exact) further than what ginac can do. See `sage.rings.rational.rational_power_parts` for example.

I am taking a look at this right now, but I don't have much time, so I can't promise any results.


---

Comment by burcin created at 2010-03-16 12:14:11

Changing component from symbolics to basic arithmetic.


---

Comment by burcin created at 2010-03-16 12:14:11

Changing status from new to needs_review.


---

Attachment

attachment:trac_8540-rational_power.patch fixes the problem, please review.


---

Comment by mhansen created at 2010-03-16 18:29:16

Looks good.


---

Comment by mhansen created at 2010-03-16 18:29:16

Changing status from needs_review to positive_review.


---

Comment by mvngu created at 2010-03-17 06:42:41

Resolution: fixed
