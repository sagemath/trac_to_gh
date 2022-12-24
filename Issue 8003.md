# Issue 8003: EllipticCurve('522j1').sha().an_padic(13) fails

archive/issues_008003.json:
```json
{
    "body": "Assignee: cremona\n\nCC:  was wuthrich cremona\n\nThis is because the quadratic twist parameter `D` needs to be cast to an integer, but after the following patch it still fails.\n\n```\ndiff -r 0133676998bd sage/schemes/elliptic_curves/sha_tate.py\n--- a/sage/schemes/elliptic_curves/sha_tate.py\tTue Jan 19 10:28:48 2010 -0800\n+++ b/sage/schemes/elliptic_curves/sha_tate.py\tTue Jan 19 13:05:47 2010 -0800\n@@ -424,7 +424,7 @@\n                 if Et.conductor() < Nmin and valuation(Et.conductor(),2) <= valuation(DD,2):\n                     Nmin = Et.conductor()\n                     Dmax = DD\n-            D = Dmax\n+            D = ZZ(Dmax)\n             Et = self.E.quadratic_twist(D)\n             lp = Et.padic_lseries(p)\n         else :\n```\n\nThis time the failure is:\n\n```\nsage: EllipticCurve('522j1').sha().an_padic(13)\n---------------------------------------------------------------------------\nValueError                                Traceback (most recent call last)\n\n/Users/rlmill/sage-4.3.1.rc1/devel/sage-main/<ipython console> in <module>()\n\n/Users/rlmill/sage-4.3.1.rc1/local/lib/python2.6/site-packages/sage/schemes/elliptic_curves/sha_tate.pyc in an_padic(self, p, prec, use_twists)\n    504             not_yet_enough_prec = True    \n    505             while not_yet_enough_prec:     \n--> 506                 lps = lp.Dp_valued_series(n,quadratic_twist=D,prec=r+1)\n    507                 lstar = [lps[0][r],lps[1][r]]\n    508                 verbose(\"the leading terms : %s\"%lstar)\n\n/Users/rlmill/sage-4.3.1.rc1/local/lib/python2.6/site-packages/sage/schemes/elliptic_curves/padic_lseries.pyc in Dp_valued_series(self, n, quadratic_twist, prec)\n   1038         E = self._E\n   1039         p = self._p\n-> 1040         lps = self.series(n, quadratic_twist=quadratic_twist, prec=prec)\n   1041     \n   1042         # now split up the series in two lps = G + H * alpha\n\n/Users/rlmill/sage-4.3.1.rc1/local/lib/python2.6/site-packages/sage/schemes/elliptic_curves/padic_lseries.pyc in series(self, n, quadratic_twist, prec)\n    934                     raise ValueError, \"quadratic_twist (=%s) must be a fundamental discriminant of a quadratic field\"%D\n    935             if gcd(D,self._p*self._E.conductor()) != 1:\n--> 936                 raise ValueError, \"quadratic twist (=%s) must be coprime to p (=%s) and the conductor of the curve (%s) \"%(D,self._p,self._E.conductor())\n    937 \n    938         p = self._p\n\nValueError: quadratic twist (=-3) must be coprime to p (=13) and the conductor of the curve (174)\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8003\n\n",
    "created_at": "2010-01-19T21:10:47Z",
    "labels": [
        "elliptic curves",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.2",
    "title": "EllipticCurve('522j1').sha().an_padic(13) fails",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8003",
    "user": "rlm"
}
```
Assignee: cremona

CC:  was wuthrich cremona

This is because the quadratic twist parameter `D` needs to be cast to an integer, but after the following patch it still fails.

```
diff -r 0133676998bd sage/schemes/elliptic_curves/sha_tate.py
--- a/sage/schemes/elliptic_curves/sha_tate.py	Tue Jan 19 10:28:48 2010 -0800
+++ b/sage/schemes/elliptic_curves/sha_tate.py	Tue Jan 19 13:05:47 2010 -0800
@@ -424,7 +424,7 @@
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


Issue created by migration from https://trac.sagemath.org/ticket/8003





---

archive/issue_comments_069933.json:
```json
{
    "body": "Attachment [trac_8003-make_D_in_ZZ_only.patch](tarball://root/attachments/some-uuid/ticket8003/trac_8003-make_D_in_ZZ_only.patch) by rlm created at 2010-01-19 21:12:33\n\nfor reference",
    "created_at": "2010-01-19T21:12:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8003",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8003#issuecomment-69933",
    "user": "rlm"
}
```

Attachment [trac_8003-make_D_in_ZZ_only.patch](tarball://root/attachments/some-uuid/ticket8003/trac_8003-make_D_in_ZZ_only.patch) by rlm created at 2010-01-19 21:12:33

for reference



---

archive/issue_comments_069934.json:
```json
{
    "body": "This is a bug that I corrected earlier for the ordinary case and I forgot to adjust the supersingular case. But while I am at it, I am improving a bit an_padic.",
    "created_at": "2010-01-22T23:15:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8003",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8003#issuecomment-69934",
    "user": "wuthrich"
}
```

This is a bug that I corrected earlier for the ordinary case and I forgot to adjust the supersingular case. But while I am at it, I am improving a bit an_padic.



---

archive/issue_comments_069935.json:
```json
{
    "body": "Attachment [trac_8003.patch](tarball://root/attachments/some-uuid/ticket8003/trac_8003.patch) by wuthrich created at 2010-01-23 18:32:40\n\nexported against 4.3.1.",
    "created_at": "2010-01-23T18:32:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8003",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8003#issuecomment-69935",
    "user": "wuthrich"
}
```

Attachment [trac_8003.patch](tarball://root/attachments/some-uuid/ticket8003/trac_8003.patch) by wuthrich created at 2010-01-23 18:32:40

exported against 4.3.1.



---

archive/issue_comments_069936.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-23T18:37:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8003",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8003#issuecomment-69936",
    "user": "wuthrich"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_069937.json:
```json
{
    "body": "This patch solves the issues above.\n\nI have also worked a bit on an_padic. I made a short-cut for rank 0 curves. In this case the leading term of the p-adic series is known to be L_ratio, so there is no need to compute the p-adic L-series, the modular symbol at 0 suffices. This speeds up the computation.\n\nThe -long doctest decreased to a half of the length, without -long it is a little bit faster. Most of the time for -long is taken up by one example. But it needs to be there as it is the fastest example of a positive rank supersingular case.\n\nAlso. I did NOT include a doctest that tests this particular bug here. This is against the rules I know, but I believe that the shortest case in which it can be reproduced would take longer than what is allowed for a doctest. In particular the above axample is not adequate.",
    "created_at": "2010-01-23T18:37:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8003",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8003#issuecomment-69937",
    "user": "wuthrich"
}
```

This patch solves the issues above.

I have also worked a bit on an_padic. I made a short-cut for rank 0 curves. In this case the leading term of the p-adic series is known to be L_ratio, so there is no need to compute the p-adic L-series, the modular symbol at 0 suffices. This speeds up the computation.

The -long doctest decreased to a half of the length, without -long it is a little bit faster. Most of the time for -long is taken up by one example. But it needs to be there as it is the fastest example of a positive rank supersingular case.

Also. I did NOT include a doctest that tests this particular bug here. This is against the rules I know, but I believe that the shortest case in which it can be reproduced would take longer than what is allowed for a doctest. In particular the above axample is not adequate.



---

archive/issue_comments_069938.json:
```json
{
    "body": "Replying to [comment:3 wuthrich]:\n> This patch solves the issues above.\n\nI have verified this.\n\n> Also. I did NOT include a doctest that tests this particular bug here. This is against the rules I know, but I believe that the shortest case in which it can be reproduced would take longer than what is allowed for a doctest. In particular the above axample is not adequate.\n\nI completely agree.\n\n\n```\nsage: time EllipticCurve('522j1').sha().an_padic(13)\nCPU times: user 1557.39 s, sys: 50.77 s, total: 1608.16 s\nWall time: 1615.05 s\n1 + O(13)\n```\n\n\nAlmost half an hour!",
    "created_at": "2010-01-23T19:31:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8003",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8003#issuecomment-69938",
    "user": "rlm"
}
```

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

archive/issue_comments_069939.json:
```json
{
    "body": "LGTM",
    "created_at": "2010-01-23T19:33:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8003",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8003#issuecomment-69939",
    "user": "rlm"
}
```

LGTM



---

archive/issue_comments_069940.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-23T19:33:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8003",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8003#issuecomment-69940",
    "user": "rlm"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_069941.json:
```json
{
    "body": "Merged [trac_8003.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8003/trac_8003.patch).",
    "created_at": "2010-01-23T20:51:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8003",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8003#issuecomment-69941",
    "user": "mvngu"
}
```

Merged [trac_8003.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8003/trac_8003.patch).



---

archive/issue_comments_069942.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-23T20:51:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8003",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8003#issuecomment-69942",
    "user": "mvngu"
}
```

Resolution: fixed
