# Issue 9952: int(symbolic expr) off by 1

Issue created by migration from Trac.

Original creator: schilly

Original creation time: 2010-09-20 10:16:21

Assignee: burcin

CC:  fredrik.johansson kcrisman zaf mjo

Problem, last digit is either 6 or 7. In short:


```
fermat(n) = 2**2**n + 1
fermat(9) gives ....4097 but:
int(fermat(9)) gives ...4096L.
Same with: long(fermat(9)).
int(2**2**9 +1) gives ...4097L
```


Burcin says: int(x) for a symbolic expression x just calls int(x.n(prec=100)). We lose that 1 in the approximation.

full example in 4.5.2:


```
sage: fermat(n) = 2**2**n + 1
sage: fermat(9)
134078079299425970995740249982058461274793658205923933777\
235614437217640300735469768018742981669034276900318581864\
86050853753882811946569946433649006084097
sage: int(fermat(9))
134078079299425970995740249982058461274793658205923933777\
235614437217640300735469768018742981669034276900318581864\
86050853753882811946569946433649006084096L
sage: long(fermat(9))
134078079299425970995740249982058461274793658205923933777\
235614437217640300735469768018742981669034276900318581864\
86050853753882811946569946433649006084096L
sage: int(2**2**9 +1)
134078079299425970995740249982058461274793658205923933777\
235614437217640300735469768018742981669034276900318581864\
86050853753882811946569946433649006084097L
```




---

Attachment


---

Comment by roed created at 2010-10-25 21:28:05

Changing status from new to needs_work.


---

Comment by roed created at 2010-10-25 21:28:05

I don't want to work on this much, but I believe that this patch should fix the problem.  If someone wants to add some doctests and polish it a bit, go for it.


---

Comment by dsm created at 2011-02-18 19:02:51

The current patch won't work for 0 or negative numbers (the log2 breaks).  This can be easily fixed, but dealing with cases like 


```
sage: f = 1-1/10**100
sage: int(f)
0
sage: int(SR(f))
1
```


where the precision needed to get the right result isn't a function of the size is a little trickier.  Maybe fast-path the common cases and then fall back on the existing floor/ceil logic?


---

Comment by dsm created at 2011-02-19 09:26:59

This appears to be a duplicate of #9627.


---

Comment by burcin created at 2012-05-22 22:40:29

Changing status from needs_work to positive_review.


---

Comment by burcin created at 2012-05-22 22:40:29

#12968 has a patch with a positive review which fixes this. We should close this as a duplicate.


---

Comment by jdemeyer created at 2012-06-19 13:25:33

Resolution: duplicate
