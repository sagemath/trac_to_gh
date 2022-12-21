# Issue 53: p-adic log is broken

Issue created by migration from Trac.

Original creator: dmharvey

Original creation time: 2006-09-13 19:43:11

Assignee: dmharvey


```
sage: x = 1 + 5 + O(5^6)
sage: y = 1 + 5 + O(5^5)
sage: x.log()
 5 + 2*5^2 + 4*5^3 + 2*5^4 + O(5^6)
sage: y.log()
 5 + 2*5^2 + 4*5^3 + 5^4 + O(5^5)
```


The answers should agree mod 5!^5. I bet someone forgot to take into account the p-adic valuation of the denominators in the series.



---

Comment by dmharvey created at 2006-09-16 05:05:54

Resolution: fixed


---

Comment by dmharvey created at 2006-09-16 05:05:54

Fixed.

Wed Sep 13 18:09:41 PDT 2006  dmharvey`@`math.harvard.edu
  * fix p-adic log -- fixed p-adic log which gave incorrect answers sometimes (trac ticket #53)
