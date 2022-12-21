# Issue 7: very strange bug with LaurentSeriesRing

Issue created by migration from Trac.

Original creator: dmharvey

Original creation time: 2006-09-12 02:35:46

Assignee: somebody


```
sage: R.<u> = LaurentSeriesRing(pAdicField(5, 10))
sage: S.<t> = LaurentSeriesRing(RationalField())
sage: R(t + t^2 + O(t^3))
 u^1 + t + O(t^2) + u^2 + t + O(t^2) + O(u^3 + t + O(t^2))
```


???!!!!???



---

Attachment


---

Comment by was created at 2006-11-06 08:22:20

Resolution: fixed


---

Comment by was created at 2006-11-06 08:22:20

Fixed for sage-1.5


---

Comment by dimpase created at 2022-09-08 08:29:03

a comment to facilitate GH import, please ignore.
