# Issue 5585: [with patch, needs review]

Issue created by migration from Trac.

Original creator: malb

Original creation time: 2009-03-22 17:53:42

Assignee: malb

CC:  burcin rpw

Keywords: crypto, aes

*Before*:

```
sage: sr = mq.SR(4,4,4,8,gf2=True,polybori=True,allow_zero_inversions=True)
sage: %time F,s = sr.polynomial_system()
CPU times: user 23.46 s, sys: 0.07 s, total: 23.52 s
Wall time: 23.61 s
```


*After*:

```
sage: sr = mq.SR(4,4,4,8,gf2=True,polybori=True,allow_zero_inversions=True)
sage: %time F,s = sr.polynomial_system()
CPU times: user 3.58 s, sys: 0.04 s, total: 3.62 s
Wall time: 3.63 s
sage: %time F,s = sr.polynomial_system()
CPU times: user 2.05 s, sys: 0.00 s, total: 2.05 s
Wall time: 2.05 s
```



---

Comment by malb created at 2009-03-22 20:09:28

Resolution: duplicate
