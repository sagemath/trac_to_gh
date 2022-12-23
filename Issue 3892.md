# Issue 3892: PowerSeries random element over GF(q) (Givaro) fails

Issue created by migration from https://trac.sagemath.org/ticket/3892

Original creator: malb

Original creation time: 2008-08-18 15:35:03

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


---

Attachment


---

Comment by malb created at 2008-08-27 13:28:16

The attached patch fixes the reported issue. Credit for this fix goes to Hamish Ivey-Law.


---

Comment by AlexGhitza created at 2008-08-29 03:21:33

Looks good.


---

Comment by mabshoff created at 2008-08-29 04:49:32

Merged in Sage 3.1.2.alpha2


---

Comment by mabshoff created at 2008-08-29 04:49:32

Resolution: fixed
