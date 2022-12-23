# Issue 7331: Conditions for non-split multiplicative reduction in p_primary_bound of Tate-Shafarevich groups

Issue created by migration from https://trac.sagemath.org/ticket/7331

Original creator: wuthrich

Original creation time: 2009-10-28 09:56:17

Assignee: davidloeffler

CC:  was rlm

Keywords: sha, tate-shafarevich group,  primary bound

`p_primary_bound` fails on the following rank 0 curve with non-split multiplicative reduction.


```
E = EllipticCurve('270b')
E.sha().p_primary_bound(5)
```



---

Comment by wuthrich created at 2009-10-28 13:00:47

exported against sage 4.2.alpha1


---

Comment by wuthrich created at 2009-10-28 13:02:44

Changing status from new to needs_review.


---

Attachment

This patch allows now for non-split multiplicative reduction and for p=3 when the rank is 0. (As we do not need p-adic heights in this case)


---

Comment by rlm created at 2009-10-28 16:28:35

Changing status from needs_review to needs_work.


---

Comment by rlm created at 2009-10-28 16:28:35

For `p=3`, an error is getting triggered in computation of the p-adic regulator:


```
sage: E = EllipticCurve('148a')
sage: E.is_surjective(3)
(True, None)
sage: E.has_additive_reduction(3)
False
sage: E.has_nonsplit_multiplicative_reduction(3)
False
sage: E.is_good(3)
True
sage: E.is_ordinary(3)
True
sage: E.sha().p_primary_bound(3)
BOOM
```


I have a feeling that this just means that the documentation needs to include the rank 0 condition when `p=3`:


```
E.rank()
1
```



---

Comment by rlm created at 2009-10-28 16:58:01

This one is a different failure:

```
sage: E = EllipticCurve('336c')
sage: E.rank()
0
sage: E.is_surjective(3)
(True, None)
sage: E.has_additive_reduction(3)
False
sage: E.has_nonsplit_multiplicative_reduction(3)
False
sage: E.is_good(3)
False
sage: E.is_ordinary(3)
True
sage: E.has_split_multiplicative_reduction(3)
True
sage: E.sha().p_primary_bound(3)
Traceback (most recent call last):
/space/rlm/sage-4.2.alpha0-x86_64-Linux/local/lib/python2.6/site-packages/sage/schemes/elliptic_curves/sha_tate.pyc in p_primary_bound(self, p)
    588             if not su :
    589                 raise ValueError, "The mod-p Galois representation is not surjective. Current knowledge about Euler systems does not provide an upper bound in this case. Try an_padic for a conjectural bound."
--> 590             shan = self.an_padic(p,prec = 0,use_twists=True)
    591             if shan == 0:
    592                 raise RuntimeError, "There is a bug in an_padic."

/space/rlm/sage-4.2.alpha0-x86_64-Linux/local/lib/python2.6/site-packages/sage/schemes/elliptic_curves/sha_tate.pyc in an_padic(self, p, prec, use_twists)
    450             not_yet_enough_prec = True
    451             while not_yet_enough_prec:
--> 452                 lps = lp.series(n,quadratic_twist=D,prec=r+1)
    453                 lstar = lps[r]
    454                 if (lstar != 0) or (prec != 0):

/space/rlm/sage-4.2.alpha0-x86_64-Linux/local/lib/python2.6/site-packages/sage/schemes/elliptic_curves/padic_lseries.pyc in series(self, n, quadratic_twist, prec)
    762                 for ell in prime_divisors(D):
    763                     if valuation(self._E.conductor(),ell) > valuation(D,ell) :
--> 764                         raise ValueError, "can not twist a curve of conductor (=%s) by the quadratic twist (=%s)."%(self._E.conductor(),D)
    765
    766

ValueError: can not twist a curve of conductor (=168) by the quadratic twist (=-4).
```



---

Comment by wuthrich created at 2009-10-28 18:48:29

I agree that I should change the documentation about p=3 => rank 0. I prefer not to catch them at the start of `p_primary_bound` since in principle it should work. The only issue is that Kedlaya's algorithm is not implemented in sage for p=3. 

But I can not reproduce your second issue. This should have been solved by #6455, merge in 4.2.alpha1.


---

Attachment

to be applied after teh first patch


---

Comment by rlm created at 2009-10-30 17:30:11

Changing status from needs_work to needs_review.


---

Comment by rlm created at 2009-10-30 17:30:19

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2009-10-31 16:27:15

Resolution: fixed
