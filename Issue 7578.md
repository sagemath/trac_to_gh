# Issue 7578: Slowness of InfinitePolynomialRing basic arithmetic

Issue created by migration from Trac.

Original creator: SimonKing

Original creation time: 2009-12-01 23:14:52

Assignee: SimonKing

Keywords: infinite polynomial ring, basic arithmetic

[Martin Albrecht](http://groups.google.com/group/sage-devel/browse_thread/thread/20e0fc8f5c5be582) reported the following example:


```
sage: X.<x> = InfinitePolynomialRing(QQ)
sage: x10000 = x[10000]
sage: x10001 = x[10001]
sage: %time 1/2*x10000
CPU times: user 43.09 s, sys: 0.02 s, total: 43.12 s
Wall time: 43.12 s
1/2*x10000
```


This is inacceptably slow.

Note that this problem does not occur with the sparse implementation of infinite polynomial rings:


```
sage: X.<x> = InfinitePolynomialRing(QQ,implementation='sparse')
sage: x10000 = x[10000]
sage: x10001 = x[10001]
sage: %time 1/2*x10000
CPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s
Wall time: 0.00 s
1/2*x10000
```


Part of the problem is a slowness of element conversion in polynomial rings:


```
sage: R1 = PolynomialRing(QQ,'x',10001)
sage: R2 = PolynomialRing(QQ,'x',10002)
sage: x10000 = R1('x10000')
sage: %time a = R2(x10000)
CPU times: user 4.96 s, sys: 0.12 s, total: 5.08 s
Wall time: 5.11 s
```

which is rather slow as  well.


---

Comment by SimonKing created at 2009-12-01 23:22:09

Improving basic arithmetic of infinite polynomial rings


---

Attachment

With the attached patch, the example improves a lot:

```
sage: X.<x> = InfinitePolynomialRing(QQ)
sage: x10000 = x[10000]
sage: x10001 = x[10001]
sage: %time 1/2*x10000
CPU times: user 7.37 s, sys: 0.01 s, total: 7.38 s
Wall time: 7.38 s
1/2*x10000
```


Of course, this is still a shame. But it may be better than nothing.

The idea / reason for the slowness:

 * When x10001 is created, the underlying finite polynomial ring of X changes. At this point, the underlying finite polynomial of x10000 does not belong to the underlying ring of X anymore.
 * In the old code, the underlying finite polynomial of x10000 was not updated.
 * With the patch, it will be updated as soon as x10000 is involved in any multiplication, summation or difference.

Hence, the timing is essentially reduced to the time for conversion of the underlying polynomials; namely, after restarting sage (clearing the cache):

```
sage: X.<x> = InfinitePolynomialRing(QQ)
sage: x10000 = x[10000]
sage: x10001 = x[10001]
sage: %time x10000._p = X._P(x10000._p)
CPU times: user 6.90 s, sys: 0.01 s, total: 6.91 s
Wall time: 6.91 s
```


I don't think that this is a satisfying time, but it is some progress, and as long as element conversion for polynomial rings isn't improved, I see no way to do it better.


---

Comment by SimonKing created at 2009-12-01 23:50:45

Changing status from new to needs_review.


---

Comment by malb created at 2009-12-02 11:36:44

Changing status from needs_review to positive_review.


---

Comment by malb created at 2009-12-02 11:36:44

The change seems sensible, applies cleanly against 4.3.alpha0, doctests pass. positive review.


---

Comment by mhansen created at 2009-12-02 12:39:08

Resolution: fixed
