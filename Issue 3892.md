# Issue 3892: PowerSeries random element over GF(q) (Givaro) fails

archive/issues_003892.json:
```json
{
    "body": "Assignee: malb\n\n\n```\nsage: P.<x> = PowerSeriesRing(GF(3^3, 'a'))\nsage: P.random_element(7)\n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n\n/home/malb/<ipython console> in <module>()\n\n/usr/local/sage-3.0.6/local/lib/python2.5/site-packages/sage/rings/power_series_ring.py in random_element(self, prec, bound)\n    544             1/15 + 19/17*t + 10/3*t^2 + 5/2*t^3 + 1/2*t^4 + O(t^5)\n    545         \"\"\"\n--> 546         return self(self.__poly_ring.random_element(prec, bound), prec)\n    547\n    548     def __cmp__(self, other):\n\n/usr/local/sage-3.0.6/local/lib/python2.5/site-packages/sage/rings/polynomial/polynomial_ring.py in random_element(self, degree, *args, **kwds)\n    785         \"\"\"\n    786         R = self.base_ring()\n--> 787         return self([R.random_element(*args, **kwds) for _ in xrange(degree+1)])\n    788\n    789     def _monics_degree( self, of_degree ):\n\nTypeError: random_element() takes no arguments (1 given)\n```\n\n\nThe proposed fix by Hamish Ivey-Law is to add (dummy) `*args` and `**kwds` to `GivaroGFq.random_element`. His patch\n\n\n```\ndiff -r 717c10d9cd4a sage/rings/finite_field_givaro.pyx\n--- a/sage/rings/finite_field_givaro.pyx        Fri Jul 11 11:46:02 2008\n-0700\n+++ b/sage/rings/finite_field_givaro.pyx        Mon Aug 18 16:10:50 2008\n+0200\n@@ -358,7 +358,7 @@ cdef class FiniteField_givaro(FiniteFiel\n         else:\n             return True\n\n-    def random_element(FiniteField_givaro self):\n+    def random_element(FiniteField_givaro self, *args, **kwds):\n         \"\"\"\n         Return a random element of self.\n```\n\n\nSince I agree with that fix:\n* this needs to be wrapped in an HG patch\n* a doctest needs to be added testing the new behavior \n\nIssue created by migration from https://trac.sagemath.org/ticket/3892\n\n",
    "created_at": "2008-08-18T15:35:03Z",
    "labels": [
        "basic arithmetic",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.2",
    "title": "PowerSeries random element over GF(q) (Givaro) fails",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3892",
    "user": "malb"
}
```
Assignee: malb


```
sage: P.<x> = PowerSeriesRing(GF(3^3, 'a'))
sage: P.random_element(7)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/malb/<ipython console> in <module>()

/usr/local/sage-3.0.6/local/lib/python2.5/site-packages/sage/rings/power_series_ring.py in random_element(self, prec, bound)
    544             1/15 + 19/17*t + 10/3*t^2 + 5/2*t^3 + 1/2*t^4 + O(t^5)
    545         """
--> 546         return self(self.__poly_ring.random_element(prec, bound), prec)
    547
    548     def __cmp__(self, other):

/usr/local/sage-3.0.6/local/lib/python2.5/site-packages/sage/rings/polynomial/polynomial_ring.py in random_element(self, degree, *args, **kwds)
    785         """
    786         R = self.base_ring()
--> 787         return self([R.random_element(*args, **kwds) for _ in xrange(degree+1)])
    788
    789     def _monics_degree( self, of_degree ):

TypeError: random_element() takes no arguments (1 given)
```


The proposed fix by Hamish Ivey-Law is to add (dummy) `*args` and `**kwds` to `GivaroGFq.random_element`. His patch


```
diff -r 717c10d9cd4a sage/rings/finite_field_givaro.pyx
--- a/sage/rings/finite_field_givaro.pyx        Fri Jul 11 11:46:02 2008
-0700
+++ b/sage/rings/finite_field_givaro.pyx        Mon Aug 18 16:10:50 2008
+0200
@@ -358,7 +358,7 @@ cdef class FiniteField_givaro(FiniteFiel
         else:
             return True

-    def random_element(FiniteField_givaro self):
+    def random_element(FiniteField_givaro self, *args, **kwds):
         """
         Return a random element of self.
```


Since I agree with that fix:
* this needs to be wrapped in an HG patch
* a doctest needs to be added testing the new behavior 

Issue created by migration from https://trac.sagemath.org/ticket/3892





---

archive/issue_comments_027814.json:
```json
{
    "body": "Attachment [finite_field_givaro_random_element.patch](tarball://root/attachments/some-uuid/ticket3892/finite_field_givaro_random_element.patch) by malb created at 2008-08-27 13:27:26",
    "created_at": "2008-08-27T13:27:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3892",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3892#issuecomment-27814",
    "user": "malb"
}
```

Attachment [finite_field_givaro_random_element.patch](tarball://root/attachments/some-uuid/ticket3892/finite_field_givaro_random_element.patch) by malb created at 2008-08-27 13:27:26



---

archive/issue_comments_027815.json:
```json
{
    "body": "The attached patch fixes the reported issue. Credit for this fix goes to Hamish Ivey-Law.",
    "created_at": "2008-08-27T13:28:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3892",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3892#issuecomment-27815",
    "user": "malb"
}
```

The attached patch fixes the reported issue. Credit for this fix goes to Hamish Ivey-Law.



---

archive/issue_comments_027816.json:
```json
{
    "body": "Looks good.",
    "created_at": "2008-08-29T03:21:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3892",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3892#issuecomment-27816",
    "user": "AlexGhitza"
}
```

Looks good.



---

archive/issue_comments_027817.json:
```json
{
    "body": "Merged in Sage 3.1.2.alpha2",
    "created_at": "2008-08-29T04:49:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3892",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3892#issuecomment-27817",
    "user": "mabshoff"
}
```

Merged in Sage 3.1.2.alpha2



---

archive/issue_comments_027818.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-08-29T04:49:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3892",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3892#issuecomment-27818",
    "user": "mabshoff"
}
```

Resolution: fixed
