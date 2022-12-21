# Issue 6541: [with patch, needs review] functions numerator and denominator for univariate polynomials

Issue created by migration from Trac.

Original creator: lftabera

Original creation time: 2009-07-16 03:39:14

Assignee: tbd

Sage univariaty polynomials do not admit numerator and denominator by default:


```
sage: K.<x>=RR['x']
sage: f=x+1
sage: numerator(f)
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)

/home/luisfe/.sage/temp/mychabol/11442/_home_luisfe__sage_init_sage_0.py in <module>()

/opt/SAGE/sage/local/lib/python2.6/site-packages/sage/misc/functional.py in numerator(x)
    686     if isinstance(x, (int, long)):
    687         return x
--> 688     return x.numerator()
    689
    690 def numerical_approx(x, prec=None, digits=None):

AttributeError: 'sage.rings.polynomial.polynomial_real_mpfr_dense.P' object has no attribute 'numerator'
```


The same happens for multivariate polynomials, see #6496

SAGE implements denominators for some univariate polynomial ring and numerators for sage.rings.polynomial.polynomial_element_generic.Polynomial_rational_dense

For denominators, first, it trys to compute the lcm of the denominators of the coefficients of the polynomial. If the coefficients do not have a denominator method or these denominators do not have a lcm method then the function fails with an exception.

Numerators of polynomials with rational coefficients are polynomials over the integers.

I propose to add the following methods:

1.- Change the denominator function. First try to compute the denominator as it is done now, if it fails, return a generic denominator
self.parent()_one_element()

2.- Add a numerator function returning self * self.denominator()

This will not change the cases where denominators are used.

A patch with the feature

```
diff -r ca1f31d6f6bf sage/rings/polynomial/polynomial_element.pyx
--- a/sage/rings/polynomial/polynomial_element.pyx      Thu Jul 09 15:14:36 2009 -0700
+++ b/sage/rings/polynomial/polynomial_element.pyx      Wed Jul 15 20:25:10 2009 -0700
`@``@` -1954,9 +1954,15 `@``@`

     def denominator(self):
         """
-        Return the least common multiple of the denominators of the entries
-        of self, when this makes sense, i.e., when the coefficients have a
-        denominator function.
+        Return a denominator of self.
+
+        First, the lcm of the denominators of the entries of self
+        is computed and returned. If this computation fails, the
+        unit of the parent of self is returned.
+
+        Note that some subclases may implement its own denominator
+        function. For example:
+        sage.rings.polynomial.polynomial_element_generic.Polynomial_rational_dense

         .. warning::

`@``@` -1997,19 +2003,91 `@``@`
             sage: f = x + RR('0.3'); f
             1.00000000000000*x + 0.300000000000000
             sage: f.denominator()
-            Traceback (most recent call last):
-            ...
-            AttributeError: 'sage.rings.real_mpfr.RealNumber' object has no attribute 'denominator'
+            1.00000000000000
         """
         if self.degree() == -1:
             return 1
-        R = self.base_ring()
+        #This code was in the original algorithm it seems useless
+        #R = self.base_ring()
         x = self.list()
-        d = x[0].denominator()
-        for y in x:
-            d = d.lcm(y.denominator())
-        return d
-
+        try:
+            d = x[0].denominator()
+            for y in x:
+                d = d.lcm(y.denominator())
+            #If we return self.parent(d) instead, automatic test
+            #start to fail, ex. "sage/rings/polynomial/complex_roots.py"
+            return d
+        except(AttributeError):
+            return self.parent().one_element()
+
+    def numerator(self):
+        """
+        Return a numerator of self computed as self * self.denominator()
+
+        Note that some subclases may implement its own numerator
+        function. For example:
+        sage.rings.polynomial.polynomial_element_generic.Polynomial_rational_dense
+
+        .. warning::
+
+        This is not the numerator of the rational function
+        defined by self, which would always be self since self is a
+        polynomial.
+
+        EXAMPLES:
+
+        First we compute the numerator of a polynomial with
+        integer coefficients, which is of course self.
+
+        ::
+
+            sage: R.<x> = ZZ[]
+            sage: f = x^3 + 17*x + 1
+            sage: f.numerator()
+            x^3 + 17*x + 1
+            sage: f == f.numerator()
+            True
+
+        Next we compute the numerator of a polynomial with rational
+        coefficients.
+
+        ::
+
+            sage: R.<x> = PolynomialRing(QQ)
+            sage: f = (1/17)*x^19 - (2/3)*x + 1/3; f
+            1/17*x^19 - 2/3*x + 1/3
+            sage: f.numerator()
+            3*x^19 - 34*x + 17
+            sage: f == f.numerator()
+            False
+
+        We try to compute the denominator of a polynomial with
+        coefficients in the real numbers, which is a ring whose elements do
+        not have a denominator method.
+
+        ::
+
+            sage: R.<x> = RR[]
+            sage: f = x + RR('0.3'); f
+            1.00000000000000*x + 0.300000000000000
+            sage: f.numerator()
+            1.00000000000000*x + 0.300000000000000
+
+        We check that the computation the numerator and denominator
+        are valid
+
+        ::
+
+            sage: K=NumberField(symbolic_expression('x^3+2'),'a')['s,t']['x']
+            sage: f=K.random_element()
+            sage: f.numerator() / f.denominator() == f
+            True
+            sage: R=RR['x']
+            sage: f=R.random_element()
+            sage: f.numerator() / f.denominator() == f
+            True
+        """
+        return self * self.denominator()

     def derivative(self, *args):
         r"""
```





---

Comment by kcrisman created at 2009-10-27 14:26:04

The attached patch is identical to that posted above by the author, except rebased for 4.2.  Positive review.


---

Attachment


---

Comment by ylchapuy created at 2009-10-28 10:48:50

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2009-10-31 09:31:08

Resolution: fixed
