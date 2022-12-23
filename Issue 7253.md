# Issue 7253: inefficient polynomial powering for positive characteristic

Issue created by migration from https://trac.sagemath.org/ticket/7253

Original creator: robertwb

Original creation time: 2009-10-20 06:07:13

Assignee: tbd

One can take advantage of the fact that (a+b)<sup>p</sup> = a<sup>p</sup> + b<sup>p</sup> to quickly expand f<sup>n</sup> = f<sup>qp</sup> * f<sup>r</sup> (where r<p, so one can literally write out the resulting monomials). 

See http://groups.google.com/group/sage-support/browse_thread/thread/38c3d619a7684a90


---

Comment by kedlaya created at 2016-04-05 17:37:42

This behavior still appears to be present in 2016. Since the underlying representation of multivariate polynomials over a finite field appears to be in Singular, I've raised the issue upstream: 

http://www.singular.uni-kl.de/forum/viewtopic.php?f=10&t=2523

For univariate polynomials over a finite field, the underlying representation is in FLINT, and there this seems to be handled correctly (although I haven't looked at the source or asked a developer to confirm):

```
sage: F = GF(7)
sage: P.<x> = PolynomialRing(F)
sage: u = (x^3 + 1)^3
sage: time v = u^(7^7); # a large power!
CPU times: user 1.17 s, sys: 44 ms, total: 1.21 s
Wall time: 1.21 s
sage: time v = u^1000000; # even larger! 
CPU times: user 1.58 s, sys: 36 ms, total: 1.62 s
Wall time: 1.62 s
```



---

Comment by kedlaya created at 2017-09-23 06:52:37

This has been resolved upstream (see previous Singular link), so I propose to close this ticket.


---

Comment by kedlaya created at 2017-10-23 12:16:51

Changing status from new to needs_review.


---

Comment by roed created at 2017-10-25 16:01:21

Changing status from needs_review to positive_review.


---

Comment by embray created at 2017-12-12 08:23:33

Resolution: wontfix
