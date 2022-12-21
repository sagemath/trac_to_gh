# Issue 149: failure in E.sha_an()

Issue created by migration from Trac.

Original creator: was

Original creation time: 2006-10-23 21:02:32

Assignee: was


```
sage: EllipticCurve([0,-432*6^2]).sha_an()
---------------------------------------------------------------------------
<type 'exceptions.RuntimeError'>          Traceback (most recent call last)

/Volumes/HOME/<ipython console> in <module>()

/Volumes/HOME/sage-stable/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/ell_rational_field.py in sha_an(self, use_database)
   2588             if not arith.is_square(Sha):
   2589                 raise RuntimeError, \
-> 2590                       "There is a bug in sha_an, since the computed conjectural order of Sha is %s, which is not a square."%Sha
   2591             self.__sha_an = Sha
   2592             return Sha

<type 'exceptions.RuntimeError'>: There is a bug in sha_an, since the computed conjectural order of Sha is 2, which is not a square.
```



---

Comment by was created at 2006-10-23 21:03:32

Another problem:

```
sage: e = EllipticCurve([0,-432*6^2])
sage: e.sha_an?
sage: e.sha_an(use_database=True)
---------------------------------------------------------------------------
<type 'exceptions.AttributeError'>        Traceback (most recent call last)

/Volumes/HOME/<ipython console> in <module>()

/Volumes/HOME/sage-stable/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/ell_rational_field.py in sha_an(self, use_database)
   2550         if use_database:
   2551             try:
-> 2552                 self.__sha_an = int(round(float(self.database_curve().db_extra[4])))
   2553                 return self.__sha_an
   2554             except RuntimeError, AttributeError:

<type 'exceptions.AttributeError'>: 'EllipticCurve_rational_field' object has no attribute 'db_extra'
```



---

Comment by was created at 2006-10-23 21:03:51

There obviously need to be way more and much better doctests in the elliptic curve file.


---

Comment by was created at 2007-01-22 03:01:48

Resolution: fixed


---

Comment by was created at 2007-01-22 03:01:48

Fixed


```
rank4:~/d/sage was$ hg export tip
# HG changeset patch
# User William Stein <wstein`@`gmail.com>
# Date 1169434711 28800
# Node ID 3ca3f4250d3073970959522a8e6a4b651d441594
# Parent  5b995af189989c3e0e6af0b4942fb296cdca5749
Fix trac #149 -- E.sha_an() issue -- just needed to minimize curve first.

diff -r 5b995af18998 -r 3ca3f4250d30 sage/schemes/elliptic_curves/ell_rational_field.py
--- a/sage/schemes/elliptic_curves/ell_rational_field.py        Sun Jan 21 18:25:46 2007 -0800
+++ b/sage/schemes/elliptic_curves/ell_rational_field.py        Sun Jan 21 18:58:31 2007 -0800
`@``@` -1341,15 +1341,30 `@``@` class EllipticCurve_rational_field(Ellip
 
     def omega(self):
         """
-        Returns the real period.  This is the correct period in the BSD
-        conjecture, i.e., it is the least real period * 2 when the period
-        lattice is rectangular.
+        Returns the real period.
+
+        If self is given by a \emph{minimal Weierstrass equation} then
+        this is the correct period in the BSD conjecture, i.e., it is
+        the least real period * 2 when the period lattice is
+        rectangular.  
 
         EXAMPLES:
             sage: E = EllipticCurve('37a')
             sage: E.omega()
             5.986917292463919259664019               # 32-bit
             5.986917292463919259664019958905016      # 64-bit
+
+        
+        This is not a minimal model.
+            sage: E = EllipticCurve([0,-432*6^2])
+            sage: E.omega()
+            0.48610938571005642989723045
+
+        If you were to plug the above omega into the BSD conjecture, you
+        would get nonsense.   The following works though:
+            sage: F = E.minimal_model()
+            sage: F.omega()
+            0.97221877142011285979446091
         """
         return self.period_lattice()[0] * self.real_components()
 
`@``@` -2541,6 +2556,11 `@``@` class EllipticCurve_rational_field(Ellip
             sage: E.sha_an()
             4
 
+        In this case the input curve is not minimal, and if this function didn't
+        transform it to be minimal, it would give nonsense:
+            sage: E = EllipticCurve([0,-432*6^2])
+            sage: E.sha_an()
+            1
         """
 #            sage: e = EllipticCurve([1, 0, 0, -19491080, -33122512122])   # 15834T2
 #            sage: e.sha_an()                          # takes a long time (way too long!!)
`@``@` -2552,14 +2572,17 `@``@` class EllipticCurve_rational_field(Ellip
                 self.__sha_an = int(round(float(self.database_curve().db_extra[4])))
                 return self.__sha_an
             except RuntimeError, AttributeError:
-                pass            
-        eps = self.root_number()
+                pass
+
+        # it's critical to switch to the minimal model.
+        E = self.minimal_model()  
+        eps = E.root_number()
         if eps == 1:
-            L1_over_omega = self.L_ratio()
+            L1_over_omega = E.L_ratio()
             if L1_over_omega == 0:
                 return 0
-            T = self.torsion_subgroup().order()
-            Sha = (L1_over_omega * T * T) / Q(self.tamagawa_product())
+            T = E.torsion_subgroup().order()
+            Sha = (L1_over_omega * T * T) / Q(E.tamagawa_product())
             try:
                 Sha = Z(Sha)
             except ValueError:
`@``@` -2568,18 +2591,20 `@``@` class EllipticCurve_rational_field(Ellip
             if not arith.is_square(Sha):
                 raise RuntimeError, \
                       "There is a bug in sha_an, since the computed conjectural order of Sha is %s, which is not a square."%Sha
+            E.__sha_an = Sha
             self.__sha_an = Sha
             return Sha
         
         else:  # rank > 0  (Not provably correct)
-            L1, error_bound = self.Lseries_deriv_at1(10*sqrt(self.conductor()) + 10)
+            L1, error_bound = E.Lseries_deriv_at1(10*sqrt(E.conductor()) + 10)
             if abs(L1) < error_bound:
+                E.__sha_an = 0
                 self.__sha_an = 0
                 return 0   # vanishes to order > 1, to computed precision
-            regulator = self.regulator()   # this could take a *long* time; and could fail...?
-            T = self.torsion_subgroup().order()
-            omega = self.omega()
-            Sha = int(round ( (L1 * T * T) / (self.tamagawa_product() * regulator * omega) ))
+            regulator = E.regulator()   # this could take a *long* time; and could fail...?
+            T = E.torsion_subgroup().order()
+            omega = E.omega()
+            Sha = int(round ( (L1 * T * T) / (E.tamagawa_product() * regulator * omega) ))
             try:
                 Sha = Z(Sha)
             except ValueError:
`@``@` -2588,6 +2613,7 `@``@` class EllipticCurve_rational_field(Ellip
             if not arith.is_square(Sha):
                 raise RuntimeError, \
                       "There is a bug in sha_an, since the computed conjectural order of Sha is %s, which is not a square."%Sha
+            E.__sha_an = Sha
             self.__sha_an = Sha
             return Sha
             
```

