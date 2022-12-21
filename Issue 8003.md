# Issue 8003: EllipticCurve('522j1').sha().an_padic(13) fails

Issue created by migration from Trac.

Original creator: rlm

Original creation time: 2010-01-19 21:10:47

Assignee: cremona

CC:  was wuthrich cremona

This is because the quadratic twist parameter `D` needs to be cast to an integer, but after the following patch it still fails.

```
diff -r 0133676998bd sage/schemes/elliptic_curves/sha_tate.py
--- a/sage/schemes/elliptic_curves/sha_tate.py	Tue Jan 19 10:28:48 2010 -0800
+++ b/sage/schemes/elliptic_curves/sha_tate.py	Tue Jan 19 13:05:47 2010 -0800
`@``@` -424,7 +424,7 `@``@`
                 if Et.conductor() < Nmin and valuation(Et.conductor(),2) <= valuation(DD,2):
                     Nmin = Et.conductor()
                     Dmax = DD
-            D = Dmax
+            D = ZZ(Dmax)
             Et = self.E.quadratic_twist(D)
             lp = Et.padic_lseries(p)
         else :
```

This time the failure is:

```
sage: EllipticCurve('522j1').sha().an_padic(13)
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)

/Users/rlmill/sage-4.3.1.rc1/devel/sage-main/<ipython console> in <module>()

/Users/rlmill/sage-4.3.1.rc1/local/lib/python2.6/site-packages/sage/schemes/elliptic_curves/sha_tate.pyc in an_padic(self, p, prec, use_twists)
    504             not_yet_enough_prec = True    
    505             while not_yet_enough_prec:     
--> 506                 lps = lp.Dp_valued_series(n,quadratic_twist=D,prec=r+1)
    507                 lstar = [lps[0][r],lps[1][r]]
    508                 verbose("the leading terms : %s"%lstar)

/Users/rlmill/sage-4.3.1.rc1/local/lib/python2.6/site-packages/sage/schemes/elliptic_curves/padic_lseries.pyc in Dp_valued_series(self, n, quadratic_twist, prec)
   1038         E = self._E
   1039         p = self._p
-> 1040         lps = self.series(n, quadratic_twist=quadratic_twist, prec=prec)
   1041     
   1042         # now split up the series in two lps = G + H * alpha

/Users/rlmill/sage-4.3.1.rc1/local/lib/python2.6/site-packages/sage/schemes/elliptic_curves/padic_lseries.pyc in series(self, n, quadratic_twist, prec)
    934                     raise ValueError, "quadratic_twist (=%s) must be a fundamental discriminant of a quadratic field"%D
    935             if gcd(D,self._p*self._E.conductor()) != 1:
--> 936                 raise ValueError, "quadratic twist (=%s) must be coprime to p (=%s) and the conductor of the curve (%s) "%(D,self._p,self._E.conductor())
    937 
    938         p = self._p

ValueError: quadratic twist (=-3) must be coprime to p (=13) and the conductor of the curve (174)
```



---

Attachment

for reference


---

Comment by wuthrich created at 2010-01-22 23:15:05

This is a bug that I corrected earlier for the ordinary case and I forgot to adjust the supersingular case. But while I am at it, I am improving a bit an_padic.


---

Attachment

exported against 4.3.1.


---

Comment by wuthrich created at 2010-01-23 18:37:50

Changing status from new to needs_review.


---

Comment by wuthrich created at 2010-01-23 18:37:50

This patch solves the issues above.

I have also worked a bit on an_padic. I made a short-cut for rank 0 curves. In this case the leading term of the p-adic series is known to be L_ratio, so there is no need to compute the p-adic L-series, the modular symbol at 0 suffices. This speeds up the computation.

The -long doctest decreased to a half of the length, without -long it is a little bit faster. Most of the time for -long is taken up by one example. But it needs to be there as it is the fastest example of a positive rank supersingular case.

Also. I did NOT include a doctest that tests this particular bug here. This is against the rules I know, but I believe that the shortest case in which it can be reproduced would take longer than what is allowed for a doctest. In particular the above axample is not adequate.


---

Comment by rlm created at 2010-01-23 19:31:27

Replying to [comment:3 wuthrich]:
> This patch solves the issues above.

I have verified this.

> Also. I did NOT include a doctest that tests this particular bug here. This is against the rules I know, but I believe that the shortest case in which it can be reproduced would take longer than what is allowed for a doctest. In particular the above axample is not adequate.

I completely agree.


```
sage: time EllipticCurve('522j1').sha().an_padic(13)
CPU times: user 1557.39 s, sys: 50.77 s, total: 1608.16 s
Wall time: 1615.05 s
1 + O(13)
```


Almost half an hour!


---

Comment by rlm created at 2010-01-23 19:33:21

LGTM


---

Comment by rlm created at 2010-01-23 19:33:21

Changing status from needs_review to positive_review.


---

Comment by mvngu created at 2010-01-23 20:51:56

Merged [trac_8003.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8003/trac_8003.patch).


---

Comment by mvngu created at 2010-01-23 20:51:56

Resolution: fixed
