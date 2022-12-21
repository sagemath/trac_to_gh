# Issue 171: bug in power series hom constructor

Issue created by migration from Trac.

Original creator: was

Original creation time: 2006-11-30 13:18:26

Assignee: somebody


```
In short,


sage: S = RationalField(); R.<t>=PowerSeriesRing(S)
sage: R.hom([S(0)])
Traceback (most recent call last):
...
TypeError: images do not define a valid homomorphism
----


On Thu, 30 Nov 2006 03:59:21 -0800, James Cranch <jdc41`@`cam.ac.uk> wrote:

> Dear William,
>
> I'd like an account for the SAGE bug tracker.

What login name would you like?

> I may as well write my bug report here. Whether you read it or not,  
> it'll be easy to copy and paste it over later.
>
> The routine "PowerSeriesRing_generic._is_valid_homomorphism_" in  
> power_series_ring.py seems to be coded incorrectly: there are often  
> valid ring homomorphisms out of R[This is the Trac macro *x* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#x-macro) sending x to 0 (say, from R[This is the Trac macro *x* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#x-macro)  
> to R itself), and these aren't recognised.

You're right -- That's definitely a bug. 

>
> A dialogue revealing the error follows below the email.
>
> I looked at the source code; the comments make me think this is a maths  
> error, not a coding error (insofar as the distinction matters). If you  
> agree that I'm not being stupid, I could patch it myself.


>--------------------------------------------------------
> | SAGE Version 1.3.7.3.3, Build Date: 2006-09-21       |
> | Distributed under the GNU General Public License V2. |
> --------------------------------------------------------
>
> sage: S = RationalField() sage: R.<t>=PowerSeriesRing(S) sage: R Power  
> Series Ring in t over Rational Field sage: H = Hom(R,S) sage: H([0])  
> ---------------------------------------------------------------------------  
> exceptions.TypeError Traceback (most recent call last)
>
> /home/james/Documents/comp/sage/<ipython console>
>
> /home/james/installations/programming/sage/sage-1.3.7.3.3/local/lib/python2.4/site-packages/sage/rings/homset.py  
> in __call__(self, im_gens, check)
>
> TypeError: images do not define a valid homomorphism sage: R.hom([0], S)  
> ---------------------------------------------------------------------------  
> exceptions.TypeError Traceback (most recent call last)
>
> /home/james/Documents/comp/sage/<ipython console>
>
> /home/james/Documents/comp/sage/gens.pyx in gens.Generators.hom()
>
> /home/james/installations/programming/sage/sage-1.3.7.3.3/local/lib/python2.4/site-packages/sage/rings/homset.py  
> in __call__(self, im_gens, check)
>
> TypeError: images do not define a valid homomorphism
```




---

Comment by was created at 2007-01-13 01:44:14

Fixed for sage-1.7


```
# HG changeset patch
# User William Stein <wstein`@`gmail.com>
# Date 1168652611 28800
# Node ID 86ad31ae2e4abe1ce83b5f6cb0ee9a2dc263a1c8
# Parent  931f47e34e11519acdd0b2bb8ae0c811c252e13f
Fix trac bug #171: power series ring homomorphism creation.

diff -r 931f47e34e11 -r 86ad31ae2e4a sage/rings/homset.py
--- a/sage/rings/homset.py      Fri Jan 12 17:33:06 2007 -0800
+++ b/sage/rings/homset.py      Fri Jan 12 17:43:31 2007 -0800
`@``@` -47,7 +47,7 `@``@` class RingHomset_generic(HomsetWithBase)
         try:
             return morphism.RingHomomorphism_im_gens(self, im_gens, check=check)
         except (NotImplementedError, ValueError), err:
-            raise TypeError, "images do not define a valid homomorphism"
+            raise TypeError, "%s\nimages do not define a valid homomorphism"%err
 
     def natural_map(self):
         return morphism.RingHomomorphism_coercion(self)
diff -r 931f47e34e11 -r 86ad31ae2e4a sage/rings/power_series_ring.py
--- a/sage/rings/power_series_ring.py   Fri Jan 12 17:33:06 2007 -0800
+++ b/sage/rings/power_series_ring.py   Fri Jan 12 17:43:31 2007 -0800
`@``@` -289,11 +289,27 `@``@` class PowerSeriesRing_generic(commutativ
         
 
     def _is_valid_homomorphism_(self, codomain, im_gens):
-        ## NOTE: There are no ring homomorphisms from the ring of
-        ## all formal power series to most rings, e.g, the p-adic
-        ## field, since you can always (mathematically!) construct
-        ## some power series that doesn't converge.
-        ## Note that 0 is not a *ring* homomorphism.
+        r"""
+        This gets called implicitly when one constructs a ring
+        homomorphism from a power series ring.
+        
+        EXAMPLE:
+            sage: S = RationalField(); R.<t>=PowerSeriesRing(S)
+            sage: f = R.hom([0])
+            sage: f(3)
+            3
+            sage: g = R.hom([t^2])
+            sage: g(-1 + 3/5 * t)
+            -1 + 3/5*t^2
+            
+        NOTE: There are no ring homomorphisms from the ring of all
+        formal power series to most rings, e.g, the p-adic field,
+        since you can always (mathematically!) construct some power
+        series that doesn't converge.  Note that 0 is not a
+        \emph{ring} homomorphism.
+        """
+        if im_gens[0] == 0:
+            return True   # this is allowed.
         from laurent_series_ring import is_LaurentSeriesRing
         if is_PowerSeriesRing(codomain) or is_LaurentSeriesRing(codomain):
             return im_gens[0].valuation() > 0
diff -r 931f47e34e11 -r 86ad31ae2e4a sage/rings/power_series_ring_element.py
--- a/sage/rings/power_series_ring_element.py   Fri Jan 12 17:33:06 2007 -0800
+++ b/sage/rings/power_series_ring_element.py   Fri Jan 12 17:43:31 2007 -0800
`@``@` -754,7 +754,8 `@``@` class PowerSeries_generic_dense(PowerSer
     def __call__(self, x):
         try:
             if x.parent() is self.parent():
-                x = x.add_bigoh(self.prec()*x.valuation())
+                if self.prec() != infinity:
+                    x = x.add_bigoh(self.prec()*x.valuation())
         except AttributeError:
             pass
         return self.__f(x)
```



---

Comment by was created at 2007-01-13 01:44:19

Resolution: fixed
