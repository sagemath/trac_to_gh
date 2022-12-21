# Issue 9478: LaTeX error for iterated polynomial rings

Issue created by migration from Trac.

Original creator: novoselt

Original creation time: 2010-07-12 01:45:07

Assignee: burcin

Keywords: latex

I have just discovered the following:

```
sage: R1.<xi, x> = QQ[]
sage: print latex(xi*x)
\xi x
sage: R2.<a> = QQ[]
sage: R3.<xi, x> = R2[]
sage: print latex(xi*x)
\xix
```

Notice no space between variables on the last line. Of course, this gives an error.


---

Comment by fwclarke created at 2010-07-12 07:38:16

I am currently working  on a rewrite of the patch to #8938.  I will try to correct this at the same time.


---

Comment by burcin created at 2010-08-28 11:43:15

Changing component from symbolics to basic arithmetic.


---

Comment by burcin created at 2010-08-28 11:43:15

Changing assignee from burcin to AlexGhitza.


---

Comment by burcin created at 2010-08-28 11:43:15

This doesn't belong in the symbolics component.


---

Comment by novoselt created at 2010-11-08 15:55:55

This issue is still present in Sage-4.6.


---

Attachment


---

Comment by novoselt created at 2011-06-17 22:55:02

Changing keywords from "latex" to "latex, sd31".


---

Comment by novoselt created at 2011-06-17 23:51:58

Changing status from new to needs_review.


---

Comment by novoselt created at 2011-06-17 23:51:58

Changing keywords from "latex, sd31" to "latex, sd31, beginner".


---

Comment by kedlaya created at 2011-06-18 13:38:03

Looks fine, applies against 4.7, no doctest failures.


---

Comment by kedlaya created at 2011-06-18 13:38:03

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2011-07-04 12:02:20

Resolution: fixed
