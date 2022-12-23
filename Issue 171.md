# Issue 171: bug in power series hom constructor

archive/issues_000171.json:
```json
{
    "body": "Assignee: somebody\n\n\n```\nIn short,\n\n\nsage: S = RationalField(); R.<t>=PowerSeriesRing(S)\nsage: R.hom([S(0)])\nTraceback (most recent call last):\n...\nTypeError: images do not define a valid homomorphism\n----\n\n\nOn Thu, 30 Nov 2006 03:59:21 -0800, James Cranch <jdc41@cam.ac.uk> wrote:\n\n> Dear William,\n>\n> I'd like an account for the SAGE bug tracker.\n\nWhat login name would you like?\n\n> I may as well write my bug report here. Whether you read it or not,  \n> it'll be easy to copy and paste it over later.\n>\n> The routine \"PowerSeriesRing_generic._is_valid_homomorphism_\" in  \n> power_series_ring.py seems to be coded incorrectly: there are often  \n> valid ring homomorphisms out of R[[x]] sending x to 0 (say, from R[[x]]  \n> to R itself), and these aren't recognised.\n\nYou're right -- That's definitely a bug. \n\n>\n> A dialogue revealing the error follows below the email.\n>\n> I looked at the source code; the comments make me think this is a maths  \n> error, not a coding error (insofar as the distinction matters). If you  \n> agree that I'm not being stupid, I could patch it myself.\n\n\n>--------------------------------------------------------\n> | SAGE Version 1.3.7.3.3, Build Date: 2006-09-21       |\n> | Distributed under the GNU General Public License V2. |\n> --------------------------------------------------------\n>\n> sage: S = RationalField() sage: R.<t>=PowerSeriesRing(S) sage: R Power  \n> Series Ring in t over Rational Field sage: H = Hom(R,S) sage: H([0])  \n> ---------------------------------------------------------------------------  \n> exceptions.TypeError Traceback (most recent call last)\n>\n> /home/james/Documents/comp/sage/<ipython console>\n>\n> /home/james/installations/programming/sage/sage-1.3.7.3.3/local/lib/python2.4/site-packages/sage/rings/homset.py  \n> in __call__(self, im_gens, check)\n>\n> TypeError: images do not define a valid homomorphism sage: R.hom([0], S)  \n> ---------------------------------------------------------------------------  \n> exceptions.TypeError Traceback (most recent call last)\n>\n> /home/james/Documents/comp/sage/<ipython console>\n>\n> /home/james/Documents/comp/sage/gens.pyx in gens.Generators.hom()\n>\n> /home/james/installations/programming/sage/sage-1.3.7.3.3/local/lib/python2.4/site-packages/sage/rings/homset.py  \n> in __call__(self, im_gens, check)\n>\n> TypeError: images do not define a valid homomorphism\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/171\n\n",
    "created_at": "2006-11-30T13:18:26Z",
    "labels": [
        "basic arithmetic",
        "major",
        "bug"
    ],
    "title": "bug in power series hom constructor",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/171",
    "user": "was"
}
```
Assignee: somebody


```
In short,


sage: S = RationalField(); R.<t>=PowerSeriesRing(S)
sage: R.hom([S(0)])
Traceback (most recent call last):
...
TypeError: images do not define a valid homomorphism
----


On Thu, 30 Nov 2006 03:59:21 -0800, James Cranch <jdc41@cam.ac.uk> wrote:

> Dear William,
>
> I'd like an account for the SAGE bug tracker.

What login name would you like?

> I may as well write my bug report here. Whether you read it or not,  
> it'll be easy to copy and paste it over later.
>
> The routine "PowerSeriesRing_generic._is_valid_homomorphism_" in  
> power_series_ring.py seems to be coded incorrectly: there are often  
> valid ring homomorphisms out of R[[x]] sending x to 0 (say, from R[[x]]  
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



Issue created by migration from https://trac.sagemath.org/ticket/171





---

archive/issue_comments_000784.json:
```json
{
    "body": "Fixed for sage-1.7\n\n\n```\n# HG changeset patch\n# User William Stein <wstein@gmail.com>\n# Date 1168652611 28800\n# Node ID 86ad31ae2e4abe1ce83b5f6cb0ee9a2dc263a1c8\n# Parent  931f47e34e11519acdd0b2bb8ae0c811c252e13f\nFix trac bug #171: power series ring homomorphism creation.\n\ndiff -r 931f47e34e11 -r 86ad31ae2e4a sage/rings/homset.py\n--- a/sage/rings/homset.py      Fri Jan 12 17:33:06 2007 -0800\n+++ b/sage/rings/homset.py      Fri Jan 12 17:43:31 2007 -0800\n@@ -47,7 +47,7 @@ class RingHomset_generic(HomsetWithBase)\n         try:\n             return morphism.RingHomomorphism_im_gens(self, im_gens, check=check)\n         except (NotImplementedError, ValueError), err:\n-            raise TypeError, \"images do not define a valid homomorphism\"\n+            raise TypeError, \"%s\\nimages do not define a valid homomorphism\"%err\n \n     def natural_map(self):\n         return morphism.RingHomomorphism_coercion(self)\ndiff -r 931f47e34e11 -r 86ad31ae2e4a sage/rings/power_series_ring.py\n--- a/sage/rings/power_series_ring.py   Fri Jan 12 17:33:06 2007 -0800\n+++ b/sage/rings/power_series_ring.py   Fri Jan 12 17:43:31 2007 -0800\n@@ -289,11 +289,27 @@ class PowerSeriesRing_generic(commutativ\n         \n \n     def _is_valid_homomorphism_(self, codomain, im_gens):\n-        ## NOTE: There are no ring homomorphisms from the ring of\n-        ## all formal power series to most rings, e.g, the p-adic\n-        ## field, since you can always (mathematically!) construct\n-        ## some power series that doesn't converge.\n-        ## Note that 0 is not a *ring* homomorphism.\n+        r\"\"\"\n+        This gets called implicitly when one constructs a ring\n+        homomorphism from a power series ring.\n+        \n+        EXAMPLE:\n+            sage: S = RationalField(); R.<t>=PowerSeriesRing(S)\n+            sage: f = R.hom([0])\n+            sage: f(3)\n+            3\n+            sage: g = R.hom([t^2])\n+            sage: g(-1 + 3/5 * t)\n+            -1 + 3/5*t^2\n+            \n+        NOTE: There are no ring homomorphisms from the ring of all\n+        formal power series to most rings, e.g, the p-adic field,\n+        since you can always (mathematically!) construct some power\n+        series that doesn't converge.  Note that 0 is not a\n+        \\emph{ring} homomorphism.\n+        \"\"\"\n+        if im_gens[0] == 0:\n+            return True   # this is allowed.\n         from laurent_series_ring import is_LaurentSeriesRing\n         if is_PowerSeriesRing(codomain) or is_LaurentSeriesRing(codomain):\n             return im_gens[0].valuation() > 0\ndiff -r 931f47e34e11 -r 86ad31ae2e4a sage/rings/power_series_ring_element.py\n--- a/sage/rings/power_series_ring_element.py   Fri Jan 12 17:33:06 2007 -0800\n+++ b/sage/rings/power_series_ring_element.py   Fri Jan 12 17:43:31 2007 -0800\n@@ -754,7 +754,8 @@ class PowerSeries_generic_dense(PowerSer\n     def __call__(self, x):\n         try:\n             if x.parent() is self.parent():\n-                x = x.add_bigoh(self.prec()*x.valuation())\n+                if self.prec() != infinity:\n+                    x = x.add_bigoh(self.prec()*x.valuation())\n         except AttributeError:\n             pass\n         return self.__f(x)\n```\n",
    "created_at": "2007-01-13T01:44:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/171",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/171#issuecomment-784",
    "user": "was"
}
```

Fixed for sage-1.7


```
# HG changeset patch
# User William Stein <wstein@gmail.com>
# Date 1168652611 28800
# Node ID 86ad31ae2e4abe1ce83b5f6cb0ee9a2dc263a1c8
# Parent  931f47e34e11519acdd0b2bb8ae0c811c252e13f
Fix trac bug #171: power series ring homomorphism creation.

diff -r 931f47e34e11 -r 86ad31ae2e4a sage/rings/homset.py
--- a/sage/rings/homset.py      Fri Jan 12 17:33:06 2007 -0800
+++ b/sage/rings/homset.py      Fri Jan 12 17:43:31 2007 -0800
@@ -47,7 +47,7 @@ class RingHomset_generic(HomsetWithBase)
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
@@ -289,11 +289,27 @@ class PowerSeriesRing_generic(commutativ
         
 
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
@@ -754,7 +754,8 @@ class PowerSeries_generic_dense(PowerSer
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

archive/issue_comments_000785.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-01-13T01:44:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/171",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/171#issuecomment-785",
    "user": "was"
}
```

Resolution: fixed
