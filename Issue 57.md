# Issue 57: certain p-adic coercions insanely slow

Issue created by migration from https://trac.sagemath.org/ticket/57

Original creator: dmharvey

Original creation time: 2006-09-14 01:55:25

Assignee: somebody

The following calculation should be virtually instantaneous:


```
sage: x = 2**120000/3**100000
sage: K = pAdicField(5, 5)
sage: time y = K(x)
CPU times: user 2.72 s, sys: 0.00 s, total: 2.72 s
Wall time: 2.72
```


It should take about as long as just reducing numerator and denominator separately:

```
sage: time z = K(x.numerator())
CPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s
Wall time: 0.00

sage: time z = K(x.denominator())
CPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s
Wall time: 0.00
```




---

Comment by dmharvey created at 2006-09-16 05:04:20

Resolution: fixed


---

Comment by dmharvey created at 2006-09-16 05:04:20

Fixed:

Thu Sep 14 19:17:11 PDT 2006  dmharvey`@`math.harvard.edu
  * padic.py -- fixes trac bug #57
