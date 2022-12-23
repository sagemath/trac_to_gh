# Issue 1343: singular factorize is randomly slow

Issue created by migration from https://trac.sagemath.org/ticket/1343

Original creator: jbmohler

Original creation time: 2007-11-30 15:12:45

Assignee: malb

Singular's factorize command is immensely slow at times, but other times it is decent.  I'd not report this as a bug except for the fact that it appears that some tuning of something might fix this.

Run this in singular (binary 3-0-4 from upstream as well):

```
ring R=0,(p10,g0,g1,g2,g3,g4,X1,X2),dp;
poly t=-p10^170*X1^10*X2^10+p10^130*X1^10*X2^5+p10^130*X1^5*X2^10-p10^90*X1^5*X2^5+p10^80*X1^5*X2^5-p10^40*X1^5-p10^40*X2^5+1;
factorize(t);
```

Repeat the factorize command a couple of times.  You'll get extreme fluctation on the amount of time required to factor (nearly instantaneous all the way out to 5-10 minutes!).

Obviously, sage demonstrates the same bizarre timing statistics:

```
sage: R.<p10,g0,g1,g2,g3,g4,X1,X2>=QQ[]
sage: t=-p10^170*X1^10*X2^10+p10^130*X1^10*X2^5+p10^130*X1^5*X2^10-p10^90*X1^5*X2^5+p10^80*X1^5*X2^5-p10^40*X1^5-p10^40*X2^5+1
sage: time _=t.factor()
CPU times: user 25.63 s, sys: 0.02 s, total: 25.65 s
Wall time: 26.18
sage: time _=t.factor()
CPU times: user 5.95 s, sys: 0.00 s, total: 5.95 s
Wall time: 5.95
sage: time _=t.factor()
CPU times: user 310.76 s, sys: 0.21 s, total: 310.97 s
Wall time: 311.65
```


I've reported this to the upstream forum as well (with no response so far):
http://singular.mathematik.uni-kl.de/forum/viewtopic.php?t=1652
I also just now submitted the bug through the singular bug request form.


---

Comment by was created at 2007-12-03 17:26:42

It turns out Magma and Maple are very fast and everybody else is slow. 


```

Here's a new 2007 paper I just found that has an algorithm for
multivariate polynomial factorization that the authors claims
blows away Maple in many cases:

          http://arxiv.org/abs/math/0701670v1

There are a lot of references in this paper.  So this might
be a very good paper to study so Sage can do something
that beats everybody. 

William
```



---

Comment by was created at 2008-10-30 17:15:53

Please see also #2152, which has some additional easier-to-try examples, but is really a duplicate of this ticket (so I close it as a dupe).


---

Comment by malb created at 2009-01-22 20:12:34

Changing type from defect to enhancement.


---

Comment by malb created at 2009-01-22 20:12:34

This certainly is an enhancement.


---

Comment by was created at 2009-08-17 11:16:09

This can be closed since in sage-4.1.1 the problem is gone:

```
sage: time _=t.factor()CPU times: user 19.92 s, sys: 0.00 s, total: 19.92 s
Wall time: 19.92 s
sage: time _=t.factor()
CPU times: user 9.83 s, sys: 0.01 s, total: 9.84 s
Wall time: 9.84 s
sage: time _=t.factor()
CPU times: user 17.45 s, sys: 0.00 s, total: 17.45 s
Wall time: 17.45 s
sage: time _=t.factor()
CPU times: user 1.20 s, sys: 0.00 s, total: 1.20 s
Wall time: 1.21 s
sage: time _=t.factor()
CPU times: user 10.57 s, sys: 0.00 s, total: 10.57 s
Wall time: 10.56 s
```



---

Comment by was created at 2009-08-17 11:16:09

Resolution: fixed
