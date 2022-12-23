# Issue 28: weird power series behavior

Issue created by migration from https://trac.sagemath.org/ticket/28

Original creator: was

Original creation time: 2006-09-12 23:25:31

Assignee: somebody


```
sage: R.<m> = LaurentSeriesRing(QQ)
   sage: S.<t> = LaurentSeriesRing(pAdicField(11))
   sage: S(m^(-2) + 10*m + m^2 + O(m^3))
   t^1 + 10*t^3 + t^4 + O(t^5) + 10*t^4 + 10*t^3 + t^4 + O(t^5) + t^5 + 10*t^3 + t^4 + O(t^5) + O(t^6 + 10*t^3 + t^4 + O(t^5))
```

  
Huh?


---

Comment by dmharvey created at 2006-09-13 00:39:51

looks similar to ticket #7


---

Comment by was created at 2007-01-13 01:57:30

This is now fixed in sage-1.6:

```
sage: R.<m> = LaurentSeriesRing(QQ)
   sage: S.<t> = LaurentSeriesRing(pAdicField(11))
   sage: S(m^(-2) + 10*m + m^2 + O(m^3))
t^-2 + (10 + O(11^Infinity))*t + t^2 + O(t^3)
```



---

Comment by was created at 2007-01-13 01:57:44

Resolution: fixed
