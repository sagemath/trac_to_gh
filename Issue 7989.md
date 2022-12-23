# Issue 7989: Minpoly doesn't work for all matrices

Issue created by migration from https://trac.sagemath.org/ticket/7989

Original creator: jason

Original creation time: 2010-01-19 02:42:47

Assignee: was

CC:  kcrisman rbeezer mhansen hedtke tscrim

Right now, not all matrices can compute minpolys.  This patch exposes these matrices.


---

Attachment

Here are the bugs (doctests that fail) this patch exposes:


```
	sage -t  "4.3.1.rc0/devel/sage-main/sage/matrix/matrix1.pyx"
	sage -t  "4.3.1.rc0/devel/sage-main/sage/matrix/matrix_dense.pyx"
	sage -t  "4.3.1.rc0/devel/sage-main/sage/matrix/matrix_generic_dense.pyx"
	sage -t  "4.3.1.rc0/devel/sage-main/sage/matrix/matrix_integer_2x2.pyx"
```



---

Comment by jason created at 2010-01-19 03:45:15

Changing status from new to needs_work.


---

Comment by hedtke created at 2011-07-17 10:40:38

Sorry, I don't understand the reason for this function. What is the idea behind it?


---

Comment by was created at 2011-07-17 13:36:13

This is a great patch.   I can't believe this has got ignored for the last 1.5 years. 

Regarding what needs to be fixed, the test failure you claim for matrix_integer_2x2 is:

```

deep:sage wstein$ sage -t matrix/matrix_integer_2x2.pyx
sage -t  "matrix/matrix_integer_2x2.pyx"                    
**********************************************************************
File "/Users/wstein/sage/install/sage-4.7.1.rc0/devel/sage-main/sage/matrix/matrix_integer_2x2.pyx", line 101:
    sage: TestSuite(m).run()
Expected nothing
Got:
    Failure in _test_minpoly:
    Traceback (most recent call last):
      File "/Users/wstein/sage/install/current/local/lib/python/site-packages/sage/misc/sage_unittest.py", line 275, in run
        test_method(tester = tester)
      File "matrix2.pyx", line 1302, in sage.matrix.matrix2.Matrix._test_minpoly (sage/matrix/matrix2.c:8933)
      File "polynomial_element.pyx", line 358, in sage.rings.polynomial.polynomial_element.Polynomial.subs (sage/rings/polynomial/polynomial_element.c:5624)
      File "polynomial_element.pyx", line 557, in sage.rings.polynomial.polynomial_element.Polynomial.__call__ (sage/rings/polynomial/polynomial_element.c:5819)
      File "polynomial_element.pyx", line 638, in sage.rings.polynomial.polynomial_element.Polynomial.__call__ (sage/rings/polynomial/polynomial_element.c:7244)
      File "element.pyx", line 1302, in sage.structure.element.RingElement.__add__ (sage/structure/element.c:11504)
      File "coerce.pyx", line 766, in sage.structure.coerce.CoercionModel_cache_maps.bin_op (sage/structure/coerce.c:7337)
    TypeError: unsupported operand parent(s) for '+': 'Space of 2x2 integer matrices' and 'Integer Ring'
    ------------------------------------------------------------
    The following tests failed: _test_minpoly
**********************************************************************
1 items had failures:
   1 of   6 in __main__.example_7
***Test Failed*** 1 failures.
For whitespace errors, see the file /Users/wstein/.sage//tmp/.doctest_matrix_integer_2x2.py
	 [4.6 s]
```


This is because substitution isn't even implemented for that class:

```
sage: MS = sage.matrix.matrix_integer_2x2.MatrixSpace_ZZ_2x2()
sage: a = MS([1,2,3,4])
sage: a.minpoly()
x^2 - 5*x - 2
sage: a.minpoly()(a)
---------------------------------------------------------------------------
TypeError     
```


Also, if one adds this for minpoly, it would make sense to also add _test_charpoly.

 -- William


---

Comment by hedtke created at 2011-07-17 18:11:26

OK. Works for me, too. Is it favored that we include a test that purposely fails?


---

Comment by rbeezer created at 2011-07-17 18:31:46

Replying to [comment:7 hedtke]:
> OK. Works for me, too. Is it favored that we include a test that purposely fails?

I think the idea is to include the test-suite checking *and* add the fixes needed to make the tests pass.


---

Comment by mmezzarobba created at 2014-03-15 15:08:04

sage-6.2.beta4:

```
sage -t src/sage/matrix/matrix_generic_dense.pyx  # 1 doctest failed
sage -t src/sage/matrix/matrix_dense.pyx  # 1 doctest failed
```



---

Comment by chapoton created at 2022-05-19 09:24:52

New commits:


---

Comment by git created at 2022-05-19 14:19:45

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2022-05-19 14:40:25

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2022-05-19 17:10:56

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2022-05-20 11:38:19

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by chapoton created at 2022-05-20 11:59:42

Changing status from needs_work to needs_review.


---

Comment by chapoton created at 2022-05-21 11:44:25

green patchbot, so please review


---

Comment by tscrim created at 2022-05-23 02:47:46

LGTM.


---

Comment by tscrim created at 2022-05-23 02:47:46

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2022-05-26 22:49:44

Resolution: fixed
