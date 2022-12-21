# Issue 9063: wrong type for denominator

Issue created by migration from Trac.

Original creator: cjh

Original creation time: 2010-05-27 06:51:35

Assignee: AlexGhitza

If you create a polynomial in one variable over a finite field and ask for the denominator, then the answer you get has the wrong type when the polynomial is the zero polynomial.  Here's an example:


```
sage: R.<t> = GF(5)['t']
sage: x = R(0)
sage: type(x.denominator())
<type 'int'>
```



---

Comment by lftabera created at 2010-06-23 13:42:27

If the element of the ring is zero or the base_ring does not have a denominator function, the code returned the "wrong 1", either int 1 or polynomial 1. The patch correct this.


---

Comment by lftabera created at 2010-06-23 13:42:27

Changing status from new to needs_review.


---

Attachment

Corrected a typo in documentation


---

Comment by cremona created at 2010-08-18 12:26:53

Changing status from needs_review to needs_work.


---

Comment by cremona created at 2010-08-18 12:26:53

This looks good to me.  It applied ok to 4.5.3.alpha1, and all (long) tests pass, except for one:

```

sage -t -long "sage/matrix/matrix2.pyx"                     
**********************************************************************
File "/storage/jec/sage-4.5.3.alpha1/devel/sage-tests/sage/matrix/matrix2.pyx", line 4665:
    sage: M.weak_popov_form()
Exception raised:
    Traceback (most recent call last):
      File "/home/jec/sage-current/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/jec/sage-current/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/jec/sage-current/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_68[7]>", line 1, in <module>
        M.weak_popov_form()###line 4665:
    sage: M.weak_popov_form()
      File "matrix2.pyx", line 4748, in sage.matrix.matrix2.Matrix.weak_popov_form (sage/matrix/matrix2.c:26417)
        ::
      File "/home/jec/sage-current/local/lib/python/site-packages/sage/matrix/matrix_misc.py", line 90, in weak_popov_form
        den = R(lcm([a.denominator() for a in M.list()]))
      File "/home/jec/sage-current/local/lib/python/site-packages/sage/rings/arith.py", line 1527, in lcm
        return __LCM_sequence(seq)
      File "/home/jec/sage-current/local/lib/python/site-packages/sage/rings/arith.py", line 1583, in __LCM_sequence
        g = vi.lcm(g)
      File "element.pyx", line 306, in sage.structure.element.Element.__getattr__ (sage/structure/element.c:2632)
        return getattr_from_other_class(self, self.parent().category().element_class, name)
      File "parent.pyx", line 268, in sage.structure.parent.getattr_from_other_class (sage/structure/parent.c:2835)
        raise_attribute_error(self, name)
      File "parent.pyx", line 170, in sage.structure.parent.raise_attribute_error (sage/structure/parent.c:2602)
        raise AttributeError, "'%s.%s' object has no attribute '%s'"%(cls.__module__, cls.__name__, name)
    AttributeError: 'sage.rings.finite_rings.integer_mod.IntegerMod_int' object has no attribute 'lcm'
**********************************************************************
1 items had failures:
```


The problem is in the function weak_popov_form() in sage/rings/matrix/matrix_misc.py  (which was only merged into Sage receontly -- and I was, by chance, its reviewer).  There one has matrices of polynomials over fields and the code tries to clear denominators, by forming the LCM of the denominators;  and that now fails when those denominators are all equal to 1 in a finite field!

Rather than mess with the weakpopov form code, this could be solved if there was an lcm function for finite field elements which always returned 1 (except lcm(0,0)=0, perhaps).


---

Comment by lftabera created at 2010-08-26 09:18:14

Well, 

The issue of adding a lcm function for finite fields has some problems associated:

- Except is degenerate cases, all elements are units, so the lcm being 1 is not nonsense.

- The problem is that currently, sage already does some lcm for finite fields if the elements can be coerced to ZZ.


```
sage: m = GF(5)
sage: a= m(4)
sage: lcm(a,a)
4
```


So this approach will add a backwards incompatibility at least.


---

Comment by cremona created at 2010-08-26 09:29:54

Replying to [comment:5 lftabera]:
> Well, 
> 
> The issue of adding a lcm function for finite fields has some problems associated:
> 
> - Except is degenerate cases, all elements are units, so the lcm being 1 is not nonsense.
> 
> - The problem is that currently, sage already does some lcm for finite fields if the elements can be coerced to ZZ.
> 
> {{{
> sage: m = GF(5)
> sage: a= m(4)
> sage: lcm(a,a)
> 4
> }}}
> 
> So this approach will add a backwards incompatibility at least.

Well spotted!  I think that this current behavour is a bug:

```
sage: a = GF(5)(4)
sage: type(a)
<type 'sage.rings.finite_rings.integer_mod.IntegerMod_int'>
sage: lcm(a,a)
4
sage: type(lcm(a,a))
<type 'sage.rings.integer.Integer'>
```

since it makes no mathematical sense at all.  It's the same for gcd:

```
sage: gcd(a,a)
4
sage: type(gcd(a,a))
<type 'sage.rings.integer.Integer'>
```

Both of these would not happen if finite field elements have gcd and lcm methods, and in my opinion that would be better.

Someone should try to implement this and do a full test to see if any existing code (tests) is broken.  I hope not -- I cannot imagine anyone relying on this rather crazy behaviour.


---

Comment by lftabera created at 2010-08-27 10:56:10

I have added a new bug dealing with the issue of lcm. So this bug now depends on #9819


---

Comment by cremona created at 2010-08-27 11:39:12

Replying to [comment:7 lftabera]:
> I have added a new bug dealing with the issue of lcm. So this bug now depends on #9819

I hope you do not mean exactly what you wrote!


---

Comment by lftabera created at 2010-09-01 07:53:40

Replying to [comment:8 cremona]:
> Replying to [comment:7 lftabera]:
> > I have added a new bug dealing with the issue of lcm. So this bug now depends on #9819
> 
> I hope you do not mean exactly what you wrote!

What do you exactly mean? I think this is the correct wayy to go. The problem may be solved by a workaround on weak_popov_form, but surely will appear on other instances of fields or other methods that may be added in the future.


---

Attachment

I have attached another patch that solves the problem in weak_popov_form.

I follow the python mantra of 'explicit better than implicit'. The algorithm expects as entries a matrix with rational functions as entries.

If the entries are polynomials, then the algorithm may fail because the denominators will be elements in a field and currently sage does not consider this case for all fields.

Now, the algorithm first transforms the input matrix to a matrix with rational functions as entries which is the domain the algorithm is expected to work. The denominators will then be polynomials and the algorithm will work as expected.

I have added a doctest to check that the output is the same in the polynomial and rational function case.

As a side effect, I correct a typo in the documentation of weak_popov_form. The documentation asserts that the output is (W, N, t) where W and N are matrices of rational functions. In fact, N is a matrix of polynomials.

Both patches can be applied in any order. With this patch bug #9819 does not apply.


---

Comment by lftabera created at 2010-09-03 11:37:47

Changing status from needs_work to needs_review.


---

Comment by burcin created at 2010-09-25 18:46:59

Changing status from needs_review to needs_work.


---

Comment by burcin created at 2010-09-25 18:46:59

AFAICT, the `weak_popov_form` function clears the denominators to work over the polynomial ring instead of the fraction field. When a matrix over the polynomial ring is given, it seems inefficient to first coerce all entries to the fraction field, then find the denominator `1` and go back to the polynomials we were given.

Can't we just avoid clearing the denominators if `R` (in the first line) is a field (and not call `lcm()`)?


---

Attachment

I have added a new patch to weak_popov_form so it does not perform any cleaning of denominadors when the matrix has polynomial entries.

Apply:


trac_9063.patch

weak-popof-form.2.patch

In any order


---

Comment by lftabera created at 2010-10-08 16:15:14

Changing status from needs_work to needs_review.


---

Comment by gagansekhon created at 2011-01-08 02:29:30

failed on coverage for both files 

./sage -coverage sage/rings/polynomial/multi_polynomial.pyx
----------------------------------------------------------------------
sage/rings/polynomial/multi_polynomial.pyx
ERROR: Please add a `TestSuite(s).run()` doctest.
SCORE sage/rings/polynomial/multi_polynomial.pyx: 89% (33 of 37)

Missing documentation:
	 * is_MPolynomial(x):
	 * _polynomial_(self, R):
	 * __hash__(self):


Missing doctests:
	 * truncate(self, var, n):

----------------------------------------------------------------------

./sage -coverage sage/matrix/matrix2.pyx ----------------------------------------------------------------------
sage/matrix/matrix2.pyx
SCORE sage/matrix/matrix2.pyx: 92% (104 of 112)

Missing documentation:
	 * _row_ambient_module(self, base_ring=None):
	 * _column_ambient_module(self):
	 * _decomposition_using_kernels(self, is_diagonalizable=False, dual=False):


Missing doctests:
	 * _decomposition_spin_generic(self, is_diagonalizable=False):
	 * eigenspaces(self, var='a', even_if_inexact=None):
	 * _echelon_classical(self):
	 * _cholesky_decomposition_(self):
	 * cmp_pivots(x,y):

----------------------------------------------------------------------


---

Comment by gagansekhon created at 2011-01-08 02:29:30

Changing status from needs_review to needs_work.


---

Comment by gagansekhon created at 2011-01-08 02:58:57

Changing status from needs_work to needs_review.


---

Comment by gagansekhon created at 2011-01-08 02:58:57

Sorry, I was following developers guide, which stated if coverage is less than 100% than it needs work. However, given the functions that you changed are not the ones where coverage failed, I put it back to needs_review. I will be running other test now


---

Comment by aly.deines created at 2011-01-10 20:00:42

Changing status from needs_review to positive_review.


---

Comment by aly.deines created at 2011-01-10 20:00:42

Looks good to me.


---

Comment by jdemeyer created at 2011-01-19 22:20:03

Resolution: fixed
