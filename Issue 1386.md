# Issue 1386: Implement splitting fields

Issue created by migration from https://trac.sagemath.org/ticket/1386

Original creator: rlm

Original creation time: 2007-12-03 20:38:43

Assignee: malb

CC:  alexghitza

Should go something like:

```
sage: K.<a> = SplittingField(QQ, x^5 - 1)
```

Then maybe a1, ..., an would be roots of the polynomial not already in `QQ` or something...


---

Comment by rlm created at 2007-12-03 20:38:53

Changing type from defect to enhancement.


---

Comment by malb created at 2008-01-16 15:45:59

Changing assignee from malb to rlm.


---

Comment by jdemeyer created at 2012-03-20 22:39:07

Resolution: duplicate


---

Comment by jdemeyer created at 2012-03-20 22:39:07

Duplicate of #2217.
