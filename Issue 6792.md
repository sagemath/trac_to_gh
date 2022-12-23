# Issue 6792: 11 doctest failures in devel/sage/doc/fr/tutorial/interfaces.rst

Issue created by migration from https://trac.sagemath.org/ticket/6792

Original creator: drkirkby

Original creation time: 2009-08-20 22:56:31

Assignee: tba

On Solaris 10 update 7 (SPARC), the following test failed. Both ECL and Maxima were updated - ECL version 9.8.4, Maxima version 5.19.1. Sage was built with gcc 4.4.1

```
----------------------------------------------------------------------
----------------------------------------------------------------------
Thu Aug 20 20:02:37 BST 2009
dsage-trial tmp directory doesn't exist - creating ...
This script will run the unit tests for DSage
```

<SNIP>

```
File "/export/home/drkirkby/sage/sage-4.1.1/devel/sage/doc/fr/tutorial/tour_algebra.rst", line 184:
    sage: lde1 = de1.laplace("t","s"); lde1
Expected:
    2*(-?%at('diff(x(t),t,1),t=0)+s^2*?%laplace(x(t),t,s)-x(0)*s)-2*?%laplace(y(t),t,s)+6*?%laplace(x(t),t,s)
Got:
    2*(-?%at('diff(x(t),t,1),t=0)+s^2*'laplace(x(t),t,s)-x(0)*s)-2*'laplace(y(t),t,s)+6*'laplace(x(t),t,s)
**********************************************************************
File "/export/home/drkirkby/sage/sage-4.1.1/devel/sage/doc/fr/tutorial/tour_algebra.rst", line 199:
    sage: lde2 = de2.laplace("t","s"); lde2
Expected:
    -?%at('diff(y(t),t,1),t=0)+s^2*?%laplace(y(t),t,s)+2*?%laplace(y(t),t,s)-2*?%laplace(x(t),t,s)-y(0)*s
Got:
    -?%at('diff(y(t),t,1),t=0)+s^2*'laplace(y(t),t,s)+2*'laplace(y(t),t,s)-2*'laplace(x(t),t,s)-y(0)*s
**********************************************************************
File "/export/home/drkirkby/sage/sage-4.1.1/devel/sage/doc/fr/tutorial/tour_algebra.rst", line 389:
    sage: maxima.eval("f:bessel_y(v, w)")
Expected:
    '?%bessel_y(v,w)'
Got:
    'bessel_y(v,w)'
**********************************************************************
File "/export/home/drkirkby/sage/sage-4.1.1/devel/sage/doc/fr/tutorial/tour_algebra.rst", line 391:
    sage: maxima.eval("diff(f,w)")
Expected:
    '(?%bessel_y(v-1,w)-?%bessel_y(v+1,w))/2'
Got:
    '(bessel_y(v-1,w)-bessel_y(v+1,w))/2'
**********************************************************************
3 items had failures:
   1 of   4 in __main__.example_11
   1 of   4 in __main__.example_12
   2 of   4 in __main__.example_20
***Test Failed*** 4 failures.
For whitespace errors, see the file /export/home/drkirkby/sage/sage-4.1.1/tmp/.doctest_tour_algebra.py
         [21.5 s]
sage -t  "devel/sage/doc/fr/tutorial/index.rst"
         [0.2 s]
sage -t  "devel/sage/doc/fr/tutorial/interfaces.rst"
**********************************************************************
File "/export/home/drkirkby/sage/sage-4.1.1/devel/sage/doc/fr/tutorial/interfaces.rst", line 285:
    sage: A.eigenvectors()
Expected:
    [[[0,4],[3,1]],[1,0,0,-4],[0,1,0,-2],[0,0,1,-4/3],[1,2,3,4]]
Got:
    [[[0,4],[3,1]],[[[1,0,0,-4],[0,1,0,-2],[0,0,1,-4/3]],[[1,2,3,4]]]]
**********************************************************************
File "/export/home/drkirkby/sage/sage-4.1.1/devel/sage/doc/fr/tutorial/interfaces.rst", line 295:
    sage: eigA
Expected:
    [[[-2,-1,1],[1,1,1]],[0,0,1],[0,1,3],[1,1/2,5/6]]
Got:
    [[[-2,-1,1],[1,1,1]],[[[0,0,1]],[[0,1,3]],[[1,1/2,5/6]]]]
**********************************************************************
File "/export/home/drkirkby/sage/sage-4.1.1/devel/sage/doc/fr/tutorial/interfaces.rst", line 297:
    sage: v1 = V(sage_eval(repr(eigA[1]))); lambda1 = eigA[0][0][0]
Exception raised:
    Traceback (most recent call last):
      File "/export/home/drkirkby/sage/sage-4.1.1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/export/home/drkirkby/sage/sage-4.1.1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/export/home/drkirkby/sage/sage-4.1.1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_8[6]>", line 1, in <module>
        v1 = V(sage_eval(repr(eigA[Integer(1)]))); lambda1 = eigA[Integer(0)][Integer(0)][Integer(0)]###line 297:
    sage: v1 = V(sage_eval(repr(eigA[1]))); lambda1 = eigA[0][0][0]
      File "/export/home/drkirkby/sage/sage-4.1.1/local/lib/python/site-packages/sage/modules/free_module.py", line 4471, in __call__
        return FreeModule_generic_field.__call__(self,e)
      File "/export/home/drkirkby/sage/sage-4.1.1/local/lib/python/site-packages/sage/modules/free_module.py", line 804, in __call__
        return self._element_class(self, x, coerce, copy)
      File "vector_rational_dense.pyx", line 100, in sage.modules.vector_rational_dense.Vector_rational_dense.__init__ (sage/modules/vector_rational_dense.c:2500)
      File "rational.pyx", line 354, in sage.rings.rational.Rational.__init__ (sage/rings/rational.c:5925)
      File "rational.pyx", line 497, in sage.rings.rational.Rational.__set_value (sage/rings/rational.c:7060)
      File "rational.pyx", line 508, in sage.rings.rational.Rational.__set_value (sage/rings/rational.c:7215)
    TypeError: Unable to coerce [0, 0, 1] (<type 'list'>) to Rational
**********************************************************************
File "/export/home/drkirkby/sage/sage-4.1.1/devel/sage/doc/fr/tutorial/interfaces.rst", line 298:
    sage: v2 = V(sage_eval(repr(eigA[2]))); lambda2 = eigA[0][0][1]
Exception raised:
    Traceback (most recent call last):
      File "/export/home/drkirkby/sage/sage-4.1.1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/export/home/drkirkby/sage/sage-4.1.1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/export/home/drkirkby/sage/sage-4.1.1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_8[7]>", line 1, in <module>
        v2 = V(sage_eval(repr(eigA[Integer(2)]))); lambda2 = eigA[Integer(0)][Integer(0)][Integer(1)]###line 298:
    sage: v2 = V(sage_eval(repr(eigA[2]))); lambda2 = eigA[0][0][1]
      File "/export/home/drkirkby/sage/sage-4.1.1/local/lib/python/site-packages/sage/interfaces/maxima.py", line 2077, in __getitem__
        raise IndexError, "n = (%s) must be between %s and %s"%(n, 0, len(self)-1)
    IndexError: n = (2) must be between 0 and 1
**********************************************************************
File "/export/home/drkirkby/sage/sage-4.1.1/devel/sage/doc/fr/tutorial/interfaces.rst", line 299:
    sage: v3 = V(sage_eval(repr(eigA[3]))); lambda3 = eigA[0][0][2]
Exception raised:
    Traceback (most recent call last):
      File "/export/home/drkirkby/sage/sage-4.1.1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/export/home/drkirkby/sage/sage-4.1.1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/export/home/drkirkby/sage/sage-4.1.1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_8[8]>", line 1, in <module>
        v3 = V(sage_eval(repr(eigA[Integer(3)]))); lambda3 = eigA[Integer(0)][Integer(0)][Integer(2)]###line 299:
    sage: v3 = V(sage_eval(repr(eigA[3]))); lambda3 = eigA[0][0][2]
      File "/export/home/drkirkby/sage/sage-4.1.1/local/lib/python/site-packages/sage/interfaces/maxima.py", line 2077, in __getitem__
        raise IndexError, "n = (%s) must be between %s and %s"%(n, 0, len(self)-1)
    IndexError: n = (3) must be between 0 and 1
**********************************************************************
File "/export/home/drkirkby/sage/sage-4.1.1/devel/sage/doc/fr/tutorial/interfaces.rst", line 303:
    sage: b1 = v1.base_ring()
Exception raised:
    Traceback (most recent call last):
      File "/export/home/drkirkby/sage/sage-4.1.1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/export/home/drkirkby/sage/sage-4.1.1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/export/home/drkirkby/sage/sage-4.1.1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_8[11]>", line 1, in <module>
        b1 = v1.base_ring()###line 303:
    sage: b1 = v1.base_ring()
    NameError: name 'v1' is not defined
**********************************************************************
File "/export/home/drkirkby/sage/sage-4.1.1/devel/sage/doc/fr/tutorial/interfaces.rst", line 304:
    sage: AA*v1 == b1(lambda1)*v1
Exception raised:
    Traceback (most recent call last):
      File "/export/home/drkirkby/sage/sage-4.1.1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/export/home/drkirkby/sage/sage-4.1.1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/export/home/drkirkby/sage/sage-4.1.1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_8[12]>", line 1, in <module>
        AA*v1 == b1(lambda1)*v1###line 304:
    sage: AA*v1 == b1(lambda1)*v1
    NameError: name 'v1' is not defined
**********************************************************************
File "/export/home/drkirkby/sage/sage-4.1.1/devel/sage/doc/fr/tutorial/interfaces.rst", line 306:
    sage: b2 = v2.base_ring()
Exception raised:
    Traceback (most recent call last):
      File "/export/home/drkirkby/sage/sage-4.1.1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/export/home/drkirkby/sage/sage-4.1.1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/export/home/drkirkby/sage/sage-4.1.1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_8[13]>", line 1, in <module>
        b2 = v2.base_ring()###line 306:
    sage: b2 = v2.base_ring()
    NameError: name 'v2' is not defined
**********************************************************************
File "/export/home/drkirkby/sage/sage-4.1.1/devel/sage/doc/fr/tutorial/interfaces.rst", line 307:
    sage: AA*v2 == b2(lambda2)*v2
Exception raised:
    Traceback (most recent call last):
      File "/export/home/drkirkby/sage/sage-4.1.1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/export/home/drkirkby/sage/sage-4.1.1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/export/home/drkirkby/sage/sage-4.1.1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_8[14]>", line 1, in <module>
        AA*v2 == b2(lambda2)*v2###line 307:
    sage: AA*v2 == b2(lambda2)*v2
    NameError: name 'v2' is not defined
**********************************************************************
File "/export/home/drkirkby/sage/sage-4.1.1/devel/sage/doc/fr/tutorial/interfaces.rst", line 309:
    sage: b3 = v3.base_ring()
Exception raised:
    Traceback (most recent call last):
      File "/export/home/drkirkby/sage/sage-4.1.1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/export/home/drkirkby/sage/sage-4.1.1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/export/home/drkirkby/sage/sage-4.1.1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_8[15]>", line 1, in <module>
        b3 = v3.base_ring()###line 309:
    sage: b3 = v3.base_ring()
    NameError: name 'v3' is not defined
**********************************************************************
File "/export/home/drkirkby/sage/sage-4.1.1/devel/sage/doc/fr/tutorial/interfaces.rst", line 310:
    sage: AA*v3 == b3(lambda3)*v3
Exception raised:
    Traceback (most recent call last):
      File "/export/home/drkirkby/sage/sage-4.1.1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/export/home/drkirkby/sage/sage-4.1.1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/export/home/drkirkby/sage/sage-4.1.1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_8[16]>", line 1, in <module>
        AA*v3 == b3(lambda3)*v3###line 310:
    sage: AA*v3 == b3(lambda3)*v3
    NameError: name 'v3' is not defined
**********************************************************************
2 items had failures:
   1 of   8 in __main__.example_7
  10 of  17 in __main__.example_8
***Test Failed*** 11 failures.
```



---

Comment by AlexGhitza created at 2009-08-21 00:00:20

Changing keywords from "" to "maxima".


---

Comment by AlexGhitza created at 2009-08-21 00:56:46

Changing status from new to assigned.


---

Comment by AlexGhitza created at 2009-08-21 00:56:46

Same story as #6787, this time narrated in French.  See attached patch.


---

Comment by AlexGhitza created at 2009-08-21 00:56:46

Changing assignee from tba to AlexGhitza.


---

Comment by AlexGhitza created at 2009-08-21 00:57:26

apply after spkg's at #6564 and #6699


---

Attachment


---

Comment by mvngu created at 2009-09-02 11:03:31

Resolution: fixed


---

Comment by mvngu created at 2009-09-02 11:03:31

This is fixed by #6699.
