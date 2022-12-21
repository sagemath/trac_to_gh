# Issue 6787: 11 doctest failures in devel/sage/doc/en/tutorial/interfaces.rst

Issue created by migration from Trac.

Original creator: drkirkby

Original creation time: 2009-08-20 22:09:58

Assignee: was

On Solaris 10 update 7 (SPARC), the following tests failed. Both ECL and Maxima were updated - ECL version 9.8.4, Maxima version 5.19.1. Sage was built with gcc 4.4.1

```
----------------------------------------------------------------------
----------------------------------------------------------------------
Thu Aug 20 20:02:37 BST 2009
dsage-trial tmp directory doesn't exist - creating ...
This script will run the unit tests for DSage
```

<SNIP>

```
sage -t  "devel/sage/doc/en/tutorial/interfaces.rst"
**********************************************************************
File "/export/home/drkirkby/sage/sage-4.1.1/devel/sage/doc/en/tutorial/interfaces.rst", line 284:
    sage: A.eigenvectors()
Expected:
    [[[0,4],[3,1]],[1,0,0,-4],[0,1,0,-2],[0,0,1,-4/3],[1,2,3,4]]
Got:
    [[[0,4],[3,1]],[[[1,0,0,-4],[0,1,0,-2],[0,0,1,-4/3]],[This is the Trac macro *1,2,3,4* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#1,2,3,4-macro)]]
**********************************************************************
File "/export/home/drkirkby/sage/sage-4.1.1/devel/sage/doc/en/tutorial/interfaces.rst", line 294:
    sage: eigA
Expected:
    [[[-2,-1,1],[1,1,1]],[0,0,1],[0,1,3],[1,1/2,5/6]]
Got:
    [[[-2,-1,1],[1,1,1]],[This is the Trac macro *[0,0,1* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#[0,0,1-macro),[This is the Trac macro *0,1,3* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#0,1,3-macro),[This is the Trac macro *1,1/2,5/6* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#1,1/2,5/6-macro)]]
**********************************************************************
File "/export/home/drkirkby/sage/sage-4.1.1/devel/sage/doc/en/tutorial/interfaces.rst", line 296:
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
        v1 = V(sage_eval(repr(eigA[Integer(1)]))); lambda1 = eigA[Integer(0)][Integer(0)][Integer(0)]###line 296:
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
File "/export/home/drkirkby/sage/sage-4.1.1/devel/sage/doc/en/tutorial/interfaces.rst", line 297:
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
        v2 = V(sage_eval(repr(eigA[Integer(2)]))); lambda2 = eigA[Integer(0)][Integer(0)][Integer(1)]###line 297:
    sage: v2 = V(sage_eval(repr(eigA[2]))); lambda2 = eigA[0][0][1]
      File "/export/home/drkirkby/sage/sage-4.1.1/local/lib/python/site-packages/sage/interfaces/maxima.py", line 2077, in __getitem__
        raise IndexError, "n = (%s) must be between %s and %s"%(n, 0, len(self)-1)
    IndexError: n = (2) must be between 0 and 1
**********************************************************************
File "/export/home/drkirkby/sage/sage-4.1.1/devel/sage/doc/en/tutorial/interfaces.rst", line 298:
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
        v3 = V(sage_eval(repr(eigA[Integer(3)]))); lambda3 = eigA[Integer(0)][Integer(0)][Integer(2)]###line 298:
    sage: v3 = V(sage_eval(repr(eigA[3]))); lambda3 = eigA[0][0][2]
      File "/export/home/drkirkby/sage/sage-4.1.1/local/lib/python/site-packages/sage/interfaces/maxima.py", line 2077, in __getitem__
        raise IndexError, "n = (%s) must be between %s and %s"%(n, 0, len(self)-1)
    IndexError: n = (3) must be between 0 and 1
**********************************************************************
File "/export/home/drkirkby/sage/sage-4.1.1/devel/sage/doc/en/tutorial/interfaces.rst", line 302:
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
        b1 = v1.base_ring()###line 302:
    sage: b1 = v1.base_ring()
    NameError: name 'v1' is not defined
**********************************************************************
File "/export/home/drkirkby/sage/sage-4.1.1/devel/sage/doc/en/tutorial/interfaces.rst", line 303:
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
        AA*v1 == b1(lambda1)*v1###line 303:
    sage: AA*v1 == b1(lambda1)*v1
    NameError: name 'v1' is not defined
**********************************************************************
File "/export/home/drkirkby/sage/sage-4.1.1/devel/sage/doc/en/tutorial/interfaces.rst", line 305:
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
        b2 = v2.base_ring()###line 305:
    sage: b2 = v2.base_ring()
    NameError: name 'v2' is not defined
**********************************************************************
File "/export/home/drkirkby/sage/sage-4.1.1/devel/sage/doc/en/tutorial/interfaces.rst", line 306:
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
        AA*v2 == b2(lambda2)*v2###line 306:
    sage: AA*v2 == b2(lambda2)*v2
    NameError: name 'v2' is not defined
**********************************************************************
File "/export/home/drkirkby/sage/sage-4.1.1/devel/sage/doc/en/tutorial/interfaces.rst", line 308:
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
        b3 = v3.base_ring()###line 308:
    sage: b3 = v3.base_ring()
    NameError: name 'v3' is not defined
**********************************************************************
File "/export/home/drkirkby/sage/sage-4.1.1/devel/sage/doc/en/tutorial/interfaces.rst", line 309:
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
        AA*v3 == b3(lambda3)*v3###line 309:
    sage: AA*v3 == b3(lambda3)*v3
    NameError: name 'v3' is not defined
**********************************************************************
2 items had failures:
   1 of   8 in __main__.example_7
  10 of  17 in __main__.example_8
***Test Failed*** 11 failures.
| Sage Version 4.1.1, Release Date: 2009-08-14                       |
| Type notebook() for the GUI, and license() for information.        |
```



---

Comment by AlexGhitza created at 2009-08-20 23:54:11

Changing keywords from "" to "maxima".


---

Comment by AlexGhitza created at 2009-08-21 00:48:47

This is due to Maxima's new formatting for eigenvectors -- the structure of the resulting list has changed.  See attached patch.


---

Comment by AlexGhitza created at 2009-08-21 00:48:47

Changing status from new to assigned.


---

Comment by AlexGhitza created at 2009-08-21 00:48:47

Changing assignee from was to AlexGhitza.


---

Attachment

apply after spkg's at #6564 and #6699


---

Comment by mvngu created at 2009-09-02 11:02:18

Resolution: fixed


---

Comment by mvngu created at 2009-09-02 11:02:18

This is fixed by #6699.
