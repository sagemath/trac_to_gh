# Issue 9063: wrong type for denominator

archive/issues_009063.json:
```json
{
    "body": "Assignee: AlexGhitza\n\nIf you create a polynomial in one variable over a finite field and ask for the denominator, then the answer you get has the wrong type when the polynomial is the zero polynomial.  Here's an example:\n\n\n```\nsage: R.<t> = GF(5)['t']\nsage: x = R(0)\nsage: type(x.denominator())\n<type 'int'>\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9063\n\n",
    "created_at": "2010-05-27T06:51:35Z",
    "labels": [
        "algebra",
        "major",
        "bug"
    ],
    "title": "wrong type for denominator",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9063",
    "user": "cjh"
}
```
Assignee: AlexGhitza

If you create a polynomial in one variable over a finite field and ask for the denominator, then the answer you get has the wrong type when the polynomial is the zero polynomial.  Here's an example:


```
sage: R.<t> = GF(5)['t']
sage: x = R(0)
sage: type(x.denominator())
<type 'int'>
```


Issue created by migration from https://trac.sagemath.org/ticket/9063





---

archive/issue_comments_084091.json:
```json
{
    "body": "If the element of the ring is zero or the base_ring does not have a denominator function, the code returned the \"wrong 1\", either int 1 or polynomial 1. The patch correct this.",
    "created_at": "2010-06-23T13:42:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9063",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9063#issuecomment-84091",
    "user": "lftabera"
}
```

If the element of the ring is zero or the base_ring does not have a denominator function, the code returned the "wrong 1", either int 1 or polynomial 1. The patch correct this.



---

archive/issue_comments_084092.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-06-23T13:42:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9063",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9063#issuecomment-84092",
    "user": "lftabera"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_084093.json:
```json
{
    "body": "Attachment\n\nCorrected a typo in documentation",
    "created_at": "2010-06-24T11:26:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9063",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9063#issuecomment-84093",
    "user": "lftabera"
}
```

Attachment

Corrected a typo in documentation



---

archive/issue_comments_084094.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-08-18T12:26:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9063",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9063#issuecomment-84094",
    "user": "cremona"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_084095.json:
```json
{
    "body": "This looks good to me.  It applied ok to 4.5.3.alpha1, and all (long) tests pass, except for one:\n\n```\n\nsage -t -long \"sage/matrix/matrix2.pyx\"                     \n**********************************************************************\nFile \"/storage/jec/sage-4.5.3.alpha1/devel/sage-tests/sage/matrix/matrix2.pyx\", line 4665:\n    sage: M.weak_popov_form()\nException raised:\n    Traceback (most recent call last):\n      File \"/home/jec/sage-current/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/home/jec/sage-current/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/home/jec/sage-current/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_68[7]>\", line 1, in <module>\n        M.weak_popov_form()###line 4665:\n    sage: M.weak_popov_form()\n      File \"matrix2.pyx\", line 4748, in sage.matrix.matrix2.Matrix.weak_popov_form (sage/matrix/matrix2.c:26417)\n        ::\n      File \"/home/jec/sage-current/local/lib/python/site-packages/sage/matrix/matrix_misc.py\", line 90, in weak_popov_form\n        den = R(lcm([a.denominator() for a in M.list()]))\n      File \"/home/jec/sage-current/local/lib/python/site-packages/sage/rings/arith.py\", line 1527, in lcm\n        return __LCM_sequence(seq)\n      File \"/home/jec/sage-current/local/lib/python/site-packages/sage/rings/arith.py\", line 1583, in __LCM_sequence\n        g = vi.lcm(g)\n      File \"element.pyx\", line 306, in sage.structure.element.Element.__getattr__ (sage/structure/element.c:2632)\n        return getattr_from_other_class(self, self.parent().category().element_class, name)\n      File \"parent.pyx\", line 268, in sage.structure.parent.getattr_from_other_class (sage/structure/parent.c:2835)\n        raise_attribute_error(self, name)\n      File \"parent.pyx\", line 170, in sage.structure.parent.raise_attribute_error (sage/structure/parent.c:2602)\n        raise AttributeError, \"'%s.%s' object has no attribute '%s'\"%(cls.__module__, cls.__name__, name)\n    AttributeError: 'sage.rings.finite_rings.integer_mod.IntegerMod_int' object has no attribute 'lcm'\n**********************************************************************\n1 items had failures:\n```\n\n\nThe problem is in the function weak_popov_form() in sage/rings/matrix/matrix_misc.py  (which was only merged into Sage receontly -- and I was, by chance, its reviewer).  There one has matrices of polynomials over fields and the code tries to clear denominators, by forming the LCM of the denominators;  and that now fails when those denominators are all equal to 1 in a finite field!\n\nRather than mess with the weakpopov form code, this could be solved if there was an lcm function for finite field elements which always returned 1 (except lcm(0,0)=0, perhaps).",
    "created_at": "2010-08-18T12:26:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9063",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9063#issuecomment-84095",
    "user": "cremona"
}
```

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

archive/issue_comments_084096.json:
```json
{
    "body": "Well, \n\nThe issue of adding a lcm function for finite fields has some problems associated:\n\n- Except is degenerate cases, all elements are units, so the lcm being 1 is not nonsense.\n\n- The problem is that currently, sage already does some lcm for finite fields if the elements can be coerced to ZZ.\n\n\n```\nsage: m = GF(5)\nsage: a= m(4)\nsage: lcm(a,a)\n4\n```\n\n\nSo this approach will add a backwards incompatibility at least.",
    "created_at": "2010-08-26T09:18:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9063",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9063#issuecomment-84096",
    "user": "lftabera"
}
```

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

archive/issue_comments_084097.json:
```json
{
    "body": "Replying to [comment:5 lftabera]:\n> Well, \n> \n> The issue of adding a lcm function for finite fields has some problems associated:\n> \n> - Except is degenerate cases, all elements are units, so the lcm being 1 is not nonsense.\n> \n> - The problem is that currently, sage already does some lcm for finite fields if the elements can be coerced to ZZ.\n> \n> {{{\n> sage: m = GF(5)\n> sage: a= m(4)\n> sage: lcm(a,a)\n> 4\n> }}}\n> \n> So this approach will add a backwards incompatibility at least.\n\nWell spotted!  I think that this current behavour is a bug:\n\n```\nsage: a = GF(5)(4)\nsage: type(a)\n<type 'sage.rings.finite_rings.integer_mod.IntegerMod_int'>\nsage: lcm(a,a)\n4\nsage: type(lcm(a,a))\n<type 'sage.rings.integer.Integer'>\n```\n\nsince it makes no mathematical sense at all.  It's the same for gcd:\n\n```\nsage: gcd(a,a)\n4\nsage: type(gcd(a,a))\n<type 'sage.rings.integer.Integer'>\n```\n\nBoth of these would not happen if finite field elements have gcd and lcm methods, and in my opinion that would be better.\n\nSomeone should try to implement this and do a full test to see if any existing code (tests) is broken.  I hope not -- I cannot imagine anyone relying on this rather crazy behaviour.",
    "created_at": "2010-08-26T09:29:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9063",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9063#issuecomment-84097",
    "user": "cremona"
}
```

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

archive/issue_comments_084098.json:
```json
{
    "body": "I have added a new bug dealing with the issue of lcm. So this bug now depends on #9819",
    "created_at": "2010-08-27T10:56:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9063",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9063#issuecomment-84098",
    "user": "lftabera"
}
```

I have added a new bug dealing with the issue of lcm. So this bug now depends on #9819



---

archive/issue_comments_084099.json:
```json
{
    "body": "Replying to [comment:7 lftabera]:\n> I have added a new bug dealing with the issue of lcm. So this bug now depends on #9819\n\nI hope you do not mean exactly what you wrote!",
    "created_at": "2010-08-27T11:39:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9063",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9063#issuecomment-84099",
    "user": "cremona"
}
```

Replying to [comment:7 lftabera]:
> I have added a new bug dealing with the issue of lcm. So this bug now depends on #9819

I hope you do not mean exactly what you wrote!



---

archive/issue_comments_084100.json:
```json
{
    "body": "Replying to [comment:8 cremona]:\n> Replying to [comment:7 lftabera]:\n> > I have added a new bug dealing with the issue of lcm. So this bug now depends on #9819\n> \n> I hope you do not mean exactly what you wrote!\n\nWhat do you exactly mean? I think this is the correct wayy to go. The problem may be solved by a workaround on weak_popov_form, but surely will appear on other instances of fields or other methods that may be added in the future.",
    "created_at": "2010-09-01T07:53:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9063",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9063#issuecomment-84100",
    "user": "lftabera"
}
```

Replying to [comment:8 cremona]:
> Replying to [comment:7 lftabera]:
> > I have added a new bug dealing with the issue of lcm. So this bug now depends on #9819
> 
> I hope you do not mean exactly what you wrote!

What do you exactly mean? I think this is the correct wayy to go. The problem may be solved by a workaround on weak_popov_form, but surely will appear on other instances of fields or other methods that may be added in the future.



---

archive/issue_comments_084101.json:
```json
{
    "body": "Attachment\n\nI have attached another patch that solves the problem in weak_popov_form.\n\nI follow the python mantra of 'explicit better than implicit'. The algorithm expects as entries a matrix with rational functions as entries.\n\nIf the entries are polynomials, then the algorithm may fail because the denominators will be elements in a field and currently sage does not consider this case for all fields.\n\nNow, the algorithm first transforms the input matrix to a matrix with rational functions as entries which is the domain the algorithm is expected to work. The denominators will then be polynomials and the algorithm will work as expected.\n\nI have added a doctest to check that the output is the same in the polynomial and rational function case.\n\nAs a side effect, I correct a typo in the documentation of weak_popov_form. The documentation asserts that the output is (W, N, t) where W and N are matrices of rational functions. In fact, N is a matrix of polynomials.\n\nBoth patches can be applied in any order. With this patch bug #9819 does not apply.",
    "created_at": "2010-09-03T11:37:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9063",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9063#issuecomment-84101",
    "user": "lftabera"
}
```

Attachment

I have attached another patch that solves the problem in weak_popov_form.

I follow the python mantra of 'explicit better than implicit'. The algorithm expects as entries a matrix with rational functions as entries.

If the entries are polynomials, then the algorithm may fail because the denominators will be elements in a field and currently sage does not consider this case for all fields.

Now, the algorithm first transforms the input matrix to a matrix with rational functions as entries which is the domain the algorithm is expected to work. The denominators will then be polynomials and the algorithm will work as expected.

I have added a doctest to check that the output is the same in the polynomial and rational function case.

As a side effect, I correct a typo in the documentation of weak_popov_form. The documentation asserts that the output is (W, N, t) where W and N are matrices of rational functions. In fact, N is a matrix of polynomials.

Both patches can be applied in any order. With this patch bug #9819 does not apply.



---

archive/issue_comments_084102.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-09-03T11:37:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9063",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9063#issuecomment-84102",
    "user": "lftabera"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_084103.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-09-25T18:46:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9063",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9063#issuecomment-84103",
    "user": "burcin"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_084104.json:
```json
{
    "body": "AFAICT, the `weak_popov_form` function clears the denominators to work over the polynomial ring instead of the fraction field. When a matrix over the polynomial ring is given, it seems inefficient to first coerce all entries to the fraction field, then find the denominator `1` and go back to the polynomials we were given.\n\nCan't we just avoid clearing the denominators if `R` (in the first line) is a field (and not call `lcm()`)?",
    "created_at": "2010-09-25T18:46:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9063",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9063#issuecomment-84104",
    "user": "burcin"
}
```

AFAICT, the `weak_popov_form` function clears the denominators to work over the polynomial ring instead of the fraction field. When a matrix over the polynomial ring is given, it seems inefficient to first coerce all entries to the fraction field, then find the denominator `1` and go back to the polynomials we were given.

Can't we just avoid clearing the denominators if `R` (in the first line) is a field (and not call `lcm()`)?



---

archive/issue_comments_084105.json:
```json
{
    "body": "Attachment\n\nI have added a new patch to weak_popov_form so it does not perform any cleaning of denominadors when the matrix has polynomial entries.\n\nApply:\n\n\ntrac_9063.patch\n\nweak-popof-form.2.patch\n\nIn any order",
    "created_at": "2010-10-08T16:08:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9063",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9063#issuecomment-84105",
    "user": "lftabera"
}
```

Attachment

I have added a new patch to weak_popov_form so it does not perform any cleaning of denominadors when the matrix has polynomial entries.

Apply:


trac_9063.patch

weak-popof-form.2.patch

In any order



---

archive/issue_comments_084106.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-10-08T16:15:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9063",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9063#issuecomment-84106",
    "user": "lftabera"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_084107.json:
```json
{
    "body": "failed on coverage for both files \n\n./sage -coverage sage/rings/polynomial/multi_polynomial.pyx\n----------------------------------------------------------------------\nsage/rings/polynomial/multi_polynomial.pyx\nERROR: Please add a `TestSuite(s).run()` doctest.\nSCORE sage/rings/polynomial/multi_polynomial.pyx: 89% (33 of 37)\n\nMissing documentation:\n* is_MPolynomial(x):\n* _polynomial_(self, R):\n* __hash__(self):\n\n\nMissing doctests:\n* truncate(self, var, n):\n\n----------------------------------------------------------------------\n\n./sage -coverage sage/matrix/matrix2.pyx ----------------------------------------------------------------------\nsage/matrix/matrix2.pyx\nSCORE sage/matrix/matrix2.pyx: 92% (104 of 112)\n\nMissing documentation:\n* _row_ambient_module(self, base_ring=None):\n* _column_ambient_module(self):\n* _decomposition_using_kernels(self, is_diagonalizable=False, dual=False):\n\n\nMissing doctests:\n* _decomposition_spin_generic(self, is_diagonalizable=False):\n* eigenspaces(self, var='a', even_if_inexact=None):\n* _echelon_classical(self):\n* _cholesky_decomposition_(self):\n* cmp_pivots(x,y):\n\n----------------------------------------------------------------------",
    "created_at": "2011-01-08T02:29:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9063",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9063#issuecomment-84107",
    "user": "gagansekhon"
}
```

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

archive/issue_comments_084108.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2011-01-08T02:29:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9063",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9063#issuecomment-84108",
    "user": "gagansekhon"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_084109.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-01-08T02:58:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9063",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9063#issuecomment-84109",
    "user": "gagansekhon"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_084110.json:
```json
{
    "body": "Sorry, I was following developers guide, which stated if coverage is less than 100% than it needs work. However, given the functions that you changed are not the ones where coverage failed, I put it back to needs_review. I will be running other test now",
    "created_at": "2011-01-08T02:58:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9063",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9063#issuecomment-84110",
    "user": "gagansekhon"
}
```

Sorry, I was following developers guide, which stated if coverage is less than 100% than it needs work. However, given the functions that you changed are not the ones where coverage failed, I put it back to needs_review. I will be running other test now



---

archive/issue_comments_084111.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-01-10T20:00:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9063",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9063#issuecomment-84111",
    "user": "aly.deines"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_084112.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2011-01-10T20:00:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9063",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9063#issuecomment-84112",
    "user": "aly.deines"
}
```

Looks good to me.



---

archive/issue_comments_084113.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-01-19T22:20:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9063",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9063#issuecomment-84113",
    "user": "jdemeyer"
}
```

Resolution: fixed
