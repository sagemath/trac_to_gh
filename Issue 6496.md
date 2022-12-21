# Issue 6496: functions numerator() and denominator() for multivariate polynomials

Issue created by migration from Trac.

Original creator: mvngu

Original creation time: 2009-07-09 08:34:55

Assignee: tbd

Keywords: numerator, denominator, multivariate polynomials

This issue was raised in [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/e6fa735733c86635):

```
The problem is that multivariate polynomials do not admit numerator
and
denominator

sage: K.<x,y>=QQ['x,y']
sage: f=x+y
sage: numerator(f)
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call
last)

/home/luisfe/.sage/temp/mychabol/5681/
_home_luisfe__sage_init_sage_0.py in
<module>()

/opt/SAGE/sage/local/lib/python2.5/site-packages/sage/misc/
functional.pyc in
numerator(x)
    686     if isinstance(x, (int, long)):
    687         return x
--> 688     return x.numerator()
    689
    690 def numerical_approx(x, prec=None, digits=None):

AttributeError: 'sage.rings.polynomial.multi_polynomial_libsingular' object has no attribute 'numerator'
```

The person who reported the bug also attached a patch to fix this:

```
I have writen a trivial patch for the class MPolynomial. I am not sure
if
denominator should return 1 or self.parent(one) I write 1 because it
seems
inoffensive to me

diff -r 2e793d2a0e12 sage/rings/polynomial/multi_polynomial.pyx
--- a/sage/rings/polynomial/multi_polynomial.pyx        Thu Jun 18
23:52:34
2009 -0700
+++ b/sage/rings/polynomial/multi_polynomial.pyx        Thu Jul 09
00:05:29
2009 -0700
`@``@` -980,6 +980,28 `@``@`
         from sage.structure.factorization import Factorization
         return Factorization(v, unit)

+    def numerator(self):
+        """
+        Numerator of a polynomial
+
+        EXAMPLES:
+        sage: K.<x,y> = QQ['x,y']
+        sage: f = x + y
+        sage: f.numerator()
+        x + y
+        """
+        return self
+
+    def denominator(self):
+        """
+        Denominator of a polynomial
+        EXAMPLES:
+        sage: K.<x,y> = QQ['x,y']
+        sage: f = x + y
+        sage: f.denominator()
+        1
+        """
+        return 1

 cdef remove_from_tuple(e, int ind): 
```



---

Comment by malb created at 2009-07-09 08:52:04

A quick comment: denominator should return the right "1", I guess the one in the base ring `self.base_ring()(1)` or the parent `sage.parent()(1)`.


---

Comment by lftabera created at 2009-07-16 03:56:15

I sent the original patch. I have realized that SAGE does neither implement numerator and denominator for univariate polynomials in general. I have open a ticket with patches in #6541 so maybe is better to wait until that patch is accepted to review this one.

I have written a new patch trying to be compatible to the univariate case.

a new function denominator in MPolynomial:

1.- First it tries to compute the lcm of the denominators of the coefficients. Returns this computation as result.

2.- If it cannot compute the previous denominator, returns a generic denominator. self.parent().one_element()

a new function numerator in MPolynomial:

returns self * self.denominator()

In the univariate case there is a special case, the numerator of a polynomial with rational coefficients QQ['x'] in a polynomial with integer coefficients ZZ['x'] So I have added another patch to MPolynomial_libsingular.

3.- If the base ring of the polynomial is the field of rational numbers, the numerator is coerced to the ring of multivariate polynomials over the integers, with the same variables and same ordering as self.parent()


```
diff -r ca1f31d6f6bf sage/rings/polynomial/multi_polynomial.pyx
--- a/sage/rings/polynomial/multi_polynomial.pyx        Thu Jul 09 15:14:36 2009 -0700
+++ b/sage/rings/polynomial/multi_polynomial.pyx        Wed Jul 15 20:51:20 2009 -0700
`@``@` -980,8 +980,136 `@``@`
         from sage.structure.factorization import Factorization
         return Factorization(v, unit)

-
-
+    def denominator(self):
+        """
+        Return a denominator of self.
+
+        First, the lcm of the denominators of the entries of self
+        is computed and returned. If this computation fails, the
+        unit of the parent of self is returned.
+
+        Note that some subclases may implement its own denominator
+        function.
+
+        .. warning::
+
+           This is not the denominator of the rational function
+           defined by self, which would always be 1 since self is a
+           polynomial.
+
+        EXAMPLES:
+
+        First we compute the denominator of a polynomial with
+        integer coefficients, which is of course 1.
+
+        ::
+
+            sage: R.<x,y> = ZZ[]
+            sage: f = x^3 + 17*y + x + y
+            sage: f.denominator()
+            1
+
+        Next we compute the denominator of a polynomial over a number field.
+
+        ::
+
+            sage: R.<x,y> = NumberField(symbolic_expression(x^2+3)  ,'a')['x,y']
+            sage: f = (1/17)*x^19 + (1/6)*y - (2/3)*x + 1/3; f
+            1/17*x^19 - 2/3*x + 1/6*y + 1/3
+            sage: f.denominator()
+            102
+
+        Finally, we try to compute the denominator of a polynomial with
+        coefficients in the real numbers, which is a ring whose elements do
+        not have a denominator method.
+
+        ::
+
+            sage: R.<a,b,c> = RR[]
+            sage: f = a + b + RR('0.3'); f
+            a + b + 0.300000000000000
+            sage: f.denominator()
+            1.00000000000000
+        """
+        if self.degree() == -1:
+            return 1
+        #R was defined for univariate polynomials. Is it useless?
+        #R = self.base_ring()
+        x = self.coefficients()
+        try:
+            d = x[0].denominator()
+            for y in x:
+                d = d.lcm(y.denominator())
+            return d
+        except(AttributeError):
+            return self.parent().one_element()
+
+    def numerator(self):
+        """
+        Return a numerator of self computed as self * self.denominator()
+
+        Note that some subclases may implement its own numerator
+        function.
+
+        .. warning::
+
+           This is not the numerator of the rational function
+           defined by self, which would always be self since self is a
+           polynomial.
+
+        EXAMPLES:
+
+        First we compute the numerator of a polynomial with
+        integer coefficients, which is of course self.
+
+        ::
+
+            sage: R.<x, y> = ZZ[]
+            sage: f = x^3 + 17*x + y + 1
+            sage: f.numerator()
+            x^3 + 17*x + y + 1
+            sage: f == f.numerator()
+            True
+
+        Next we compute the numerator of a polynomial over a number field.
+
+        ::
+
+            sage: R.<x,y> = NumberField(symbolic_expression(x^2+3)  ,'a')['x,y']
+            sage: f = (1/17)*y^19 - (2/3)*x + 1/3; f
+            1/17*y^19 - 2/3*x + 1/3
+            sage: f.numerator()
+            3*y^19 - 34*x + 17
+            sage: f == f.numerator()
+            False
+
+        We try to compute the numerator of a polynomial with coefficients in
+        the finite field of 3 elements.
+
+        ::
+
+            sage: K.<x,y,z> = GF(3)['x, y, z']
+            sage: f = 2*x*z + 2*z^2 + 2*y + 1; f
+            -x*z - z^2 - y + 1
+            sage: f.numerator()
+            -x*z - z^2 - y + 1
+
+        We check that the computation the numerator and denominator
+        are valid
+
+        ::
+
+            sage: K=NumberField(symbolic_expression('x^3+2'),'a')['x']['s,t']
+            sage: f=K.random_element()
+            sage: f.numerator() / f.denominator() == f
+            True
+            sage: R=RR['x,y,z']
+            sage: f=R.random_element()
+            sage: f.numerator() / f.denominator() == f
+            True
+        """
+        return self * self.denominator()
+
 cdef remove_from_tuple(e, int ind):
     w = list(e)
     del w[ind]
```



```
diff -r ca1f31d6f6bf sage/rings/polynomial/multi_polynomial_libsingular.pyx
--- a/sage/rings/polynomial/multi_polynomial_libsingular.pyx    Thu Jul 09 15:14:36 2009 -0700
+++ b/sage/rings/polynomial/multi_polynomial_libsingular.pyx    Wed Jul 15 20:51:20 2009 -0700
`@``@` -4866,7 +4866,69 `@``@`
             i.append( new_MP(self._parent, pDiff(self._poly, k)))

         return i
-
+
+    def numerator(self):
+        """
+        Return a numerator of self computed as self * self.denominator()
+
+        If the base_field of self is the Rational Field then the
+        numerator is a polynomial whose base_ring is the Integer Ring,
+        this is done for compatibility to the univariate case.
+
+    .. warning::
+
+        This is not the numerator of the rational function
+        defined by self, which would always be self since self is a
+        polynomial.
+
+    EXAMPLES:
+
+    First we compute the numerator of a polynomial with
+    integer coefficients, which is of course self.
+
+    ::
+
+        sage: R.<x, y> = ZZ[]
+        sage: f = x^3 + 17*y + 1
+        sage: f.numerator()
+        x^3 + 17*y + 1
+        sage: f == f.numerator()
+        True
+
+    Next we compute the numerator of a polynomial with rational
+    coefficients.
+
+    ::
+
+        sage: R.<x,y> = PolynomialRing(QQ)
+        sage: f = (1/17)*x^19 - (2/3)*y + 1/3; f
+        1/17*x^19 - 2/3*y + 1/3
+        sage: f.numerator()
+        3*x^19 - 34*y + 17
+        sage: f == f.numerator()
+        False
+        sage: f.numerator().base_ring()
+        Integer Ring
+
+    We check that the computation the numerator and denominator
+    are valid
+
+    ::
+
+        sage: K=QQ['x,y']
+        sage: f=K.random_element()
+        sage: f.numerator() / f.denominator() == f
+        True
+        """
+        if self.base_ring() == RationalField():
+            #This part is for compatibility with the univariate case,
+            #where the numerator of a polynomial over RationalField
+            #is a polynomial over IntegerRing
+            integer_polynomial_ring = MPolynomialRing_libsingular(ZZ,self.parent().ngens(),self.parent().gens(),order=self.parent().term_order())
+            return integer_polynomial_ring(self * self.denominator())
+        else:
+            return self * self.denominator()
+
 def unpickle_MPolynomial_libsingular(MPolynomialRing_libsingular R, d):
     """
     Deserialize an ``MPolynomial_libsingular`` object
```



---

Comment by lftabera created at 2009-11-06 23:22:53

Changing status from new to needs_review.


---

Comment by malb created at 2009-11-07 00:42:24

Could you attach your new patch instead of inlining it?


---

Attachment

Tested with sage 4.2


---

Attachment

apply on top of other


---

Comment by robertwb created at 2009-11-20 04:30:32

Looks good and passes tests. I added one tiny change--the denominator should probably live in the basering, not the parent. Other than that, positive review (which can be set as soon as my patch is looked at).


---

Comment by hivert created at 2009-11-21 14:32:05

Changing status from needs_review to positive_review.


---

Comment by hivert created at 2009-11-21 14:32:05

Replying to [comment:6 robertwb]:
> Looks good and passes tests. I added one tiny change--the denominator should probably live in the basering, not the parent. Other than that, positive review (which can be set as soon as my patch is looked at). 

Done ! Everything alright (That was an easy one) => Positive review.

Florent


---

Comment by mhansen created at 2009-11-22 07:31:12

Resolution: fixed
