# Issue 6787: 11 doctest failures in devel/sage/doc/en/tutorial/interfaces.rst

archive/issues_006787.json:
```json
{
    "body": "Assignee: was\n\nOn Solaris 10 update 7 (SPARC), the following tests failed. Both ECL and Maxima were updated - ECL version 9.8.4, Maxima version 5.19.1. Sage was built with gcc 4.4.1\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nThu Aug 20 20:02:37 BST 2009\ndsage-trial tmp directory doesn't exist - creating ...\nThis script will run the unit tests for DSage\n```\n\n<SNIP>\n\n```\nsage -t  \"devel/sage/doc/en/tutorial/interfaces.rst\"\n**********************************************************************\nFile \"/export/home/drkirkby/sage/sage-4.1.1/devel/sage/doc/en/tutorial/interfaces.rst\", line 284:\n    sage: A.eigenvectors()\nExpected:\n    [[[0,4],[3,1]],[1,0,0,-4],[0,1,0,-2],[0,0,1,-4/3],[1,2,3,4]]\nGot:\n    [[[0,4],[3,1]],[[[1,0,0,-4],[0,1,0,-2],[0,0,1,-4/3]],[[1,2,3,4]]]]\n**********************************************************************\nFile \"/export/home/drkirkby/sage/sage-4.1.1/devel/sage/doc/en/tutorial/interfaces.rst\", line 294:\n    sage: eigA\nExpected:\n    [[[-2,-1,1],[1,1,1]],[0,0,1],[0,1,3],[1,1/2,5/6]]\nGot:\n    [[[-2,-1,1],[1,1,1]],[[[0,0,1]],[[0,1,3]],[[1,1/2,5/6]]]]\n**********************************************************************\nFile \"/export/home/drkirkby/sage/sage-4.1.1/devel/sage/doc/en/tutorial/interfaces.rst\", line 296:\n    sage: v1 = V(sage_eval(repr(eigA[1]))); lambda1 = eigA[0][0][0]\nException raised:\n    Traceback (most recent call last):\n      File \"/export/home/drkirkby/sage/sage-4.1.1/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/export/home/drkirkby/sage/sage-4.1.1/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/export/home/drkirkby/sage/sage-4.1.1/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_8[6]>\", line 1, in <module>\n        v1 = V(sage_eval(repr(eigA[Integer(1)]))); lambda1 = eigA[Integer(0)][Integer(0)][Integer(0)]###line 296:\n    sage: v1 = V(sage_eval(repr(eigA[1]))); lambda1 = eigA[0][0][0]\n      File \"/export/home/drkirkby/sage/sage-4.1.1/local/lib/python/site-packages/sage/modules/free_module.py\", line 4471, in __call__\n        return FreeModule_generic_field.__call__(self,e)\n      File \"/export/home/drkirkby/sage/sage-4.1.1/local/lib/python/site-packages/sage/modules/free_module.py\", line 804, in __call__\n        return self._element_class(self, x, coerce, copy)\n      File \"vector_rational_dense.pyx\", line 100, in sage.modules.vector_rational_dense.Vector_rational_dense.__init__ (sage/modules/vector_rational_dense.c:2500)\n      File \"rational.pyx\", line 354, in sage.rings.rational.Rational.__init__ (sage/rings/rational.c:5925)\n      File \"rational.pyx\", line 497, in sage.rings.rational.Rational.__set_value (sage/rings/rational.c:7060)\n      File \"rational.pyx\", line 508, in sage.rings.rational.Rational.__set_value (sage/rings/rational.c:7215)\n    TypeError: Unable to coerce [0, 0, 1] (<type 'list'>) to Rational\n**********************************************************************\nFile \"/export/home/drkirkby/sage/sage-4.1.1/devel/sage/doc/en/tutorial/interfaces.rst\", line 297:\n    sage: v2 = V(sage_eval(repr(eigA[2]))); lambda2 = eigA[0][0][1]\nException raised:\n    Traceback (most recent call last):\n      File \"/export/home/drkirkby/sage/sage-4.1.1/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/export/home/drkirkby/sage/sage-4.1.1/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/export/home/drkirkby/sage/sage-4.1.1/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_8[7]>\", line 1, in <module>\n        v2 = V(sage_eval(repr(eigA[Integer(2)]))); lambda2 = eigA[Integer(0)][Integer(0)][Integer(1)]###line 297:\n    sage: v2 = V(sage_eval(repr(eigA[2]))); lambda2 = eigA[0][0][1]\n      File \"/export/home/drkirkby/sage/sage-4.1.1/local/lib/python/site-packages/sage/interfaces/maxima.py\", line 2077, in __getitem__\n        raise IndexError, \"n = (%s) must be between %s and %s\"%(n, 0, len(self)-1)\n    IndexError: n = (2) must be between 0 and 1\n**********************************************************************\nFile \"/export/home/drkirkby/sage/sage-4.1.1/devel/sage/doc/en/tutorial/interfaces.rst\", line 298:\n    sage: v3 = V(sage_eval(repr(eigA[3]))); lambda3 = eigA[0][0][2]\nException raised:\n    Traceback (most recent call last):\n      File \"/export/home/drkirkby/sage/sage-4.1.1/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/export/home/drkirkby/sage/sage-4.1.1/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/export/home/drkirkby/sage/sage-4.1.1/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_8[8]>\", line 1, in <module>\n        v3 = V(sage_eval(repr(eigA[Integer(3)]))); lambda3 = eigA[Integer(0)][Integer(0)][Integer(2)]###line 298:\n    sage: v3 = V(sage_eval(repr(eigA[3]))); lambda3 = eigA[0][0][2]\n      File \"/export/home/drkirkby/sage/sage-4.1.1/local/lib/python/site-packages/sage/interfaces/maxima.py\", line 2077, in __getitem__\n        raise IndexError, \"n = (%s) must be between %s and %s\"%(n, 0, len(self)-1)\n    IndexError: n = (3) must be between 0 and 1\n**********************************************************************\nFile \"/export/home/drkirkby/sage/sage-4.1.1/devel/sage/doc/en/tutorial/interfaces.rst\", line 302:\n    sage: b1 = v1.base_ring()\nException raised:\n    Traceback (most recent call last):\n      File \"/export/home/drkirkby/sage/sage-4.1.1/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/export/home/drkirkby/sage/sage-4.1.1/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/export/home/drkirkby/sage/sage-4.1.1/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_8[11]>\", line 1, in <module>\n        b1 = v1.base_ring()###line 302:\n    sage: b1 = v1.base_ring()\n    NameError: name 'v1' is not defined\n**********************************************************************\nFile \"/export/home/drkirkby/sage/sage-4.1.1/devel/sage/doc/en/tutorial/interfaces.rst\", line 303:\n    sage: AA*v1 == b1(lambda1)*v1\nException raised:\n    Traceback (most recent call last):\n      File \"/export/home/drkirkby/sage/sage-4.1.1/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/export/home/drkirkby/sage/sage-4.1.1/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/export/home/drkirkby/sage/sage-4.1.1/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_8[12]>\", line 1, in <module>\n        AA*v1 == b1(lambda1)*v1###line 303:\n    sage: AA*v1 == b1(lambda1)*v1\n    NameError: name 'v1' is not defined\n**********************************************************************\nFile \"/export/home/drkirkby/sage/sage-4.1.1/devel/sage/doc/en/tutorial/interfaces.rst\", line 305:\n    sage: b2 = v2.base_ring()\nException raised:\n    Traceback (most recent call last):\n      File \"/export/home/drkirkby/sage/sage-4.1.1/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/export/home/drkirkby/sage/sage-4.1.1/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/export/home/drkirkby/sage/sage-4.1.1/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_8[13]>\", line 1, in <module>\n        b2 = v2.base_ring()###line 305:\n    sage: b2 = v2.base_ring()\n    NameError: name 'v2' is not defined\n**********************************************************************\nFile \"/export/home/drkirkby/sage/sage-4.1.1/devel/sage/doc/en/tutorial/interfaces.rst\", line 306:\n    sage: AA*v2 == b2(lambda2)*v2\nException raised:\n    Traceback (most recent call last):\n      File \"/export/home/drkirkby/sage/sage-4.1.1/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/export/home/drkirkby/sage/sage-4.1.1/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/export/home/drkirkby/sage/sage-4.1.1/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_8[14]>\", line 1, in <module>\n        AA*v2 == b2(lambda2)*v2###line 306:\n    sage: AA*v2 == b2(lambda2)*v2\n    NameError: name 'v2' is not defined\n**********************************************************************\nFile \"/export/home/drkirkby/sage/sage-4.1.1/devel/sage/doc/en/tutorial/interfaces.rst\", line 308:\n    sage: b3 = v3.base_ring()\nException raised:\n    Traceback (most recent call last):\n      File \"/export/home/drkirkby/sage/sage-4.1.1/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/export/home/drkirkby/sage/sage-4.1.1/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/export/home/drkirkby/sage/sage-4.1.1/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_8[15]>\", line 1, in <module>\n        b3 = v3.base_ring()###line 308:\n    sage: b3 = v3.base_ring()\n    NameError: name 'v3' is not defined\n**********************************************************************\nFile \"/export/home/drkirkby/sage/sage-4.1.1/devel/sage/doc/en/tutorial/interfaces.rst\", line 309:\n    sage: AA*v3 == b3(lambda3)*v3\nException raised:\n    Traceback (most recent call last):\n      File \"/export/home/drkirkby/sage/sage-4.1.1/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/export/home/drkirkby/sage/sage-4.1.1/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/export/home/drkirkby/sage/sage-4.1.1/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_8[16]>\", line 1, in <module>\n        AA*v3 == b3(lambda3)*v3###line 309:\n    sage: AA*v3 == b3(lambda3)*v3\n    NameError: name 'v3' is not defined\n**********************************************************************\n2 items had failures:\n   1 of   8 in __main__.example_7\n  10 of  17 in __main__.example_8\n***Test Failed*** 11 failures.\n| Sage Version 4.1.1, Release Date: 2009-08-14                       |\n| Type notebook() for the GUI, and license() for information.        |\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6787\n\n",
    "created_at": "2009-08-20T22:09:58Z",
    "labels": [
        "interfaces",
        "major",
        "bug"
    ],
    "title": "11 doctest failures in devel/sage/doc/en/tutorial/interfaces.rst",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6787",
    "user": "drkirkby"
}
```
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
    [[[0,4],[3,1]],[[[1,0,0,-4],[0,1,0,-2],[0,0,1,-4/3]],[[1,2,3,4]]]]
**********************************************************************
File "/export/home/drkirkby/sage/sage-4.1.1/devel/sage/doc/en/tutorial/interfaces.rst", line 294:
    sage: eigA
Expected:
    [[[-2,-1,1],[1,1,1]],[0,0,1],[0,1,3],[1,1/2,5/6]]
Got:
    [[[-2,-1,1],[1,1,1]],[[[0,0,1]],[[0,1,3]],[[1,1/2,5/6]]]]
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


Issue created by migration from https://trac.sagemath.org/ticket/6787





---

archive/issue_comments_055934.json:
```json
{
    "body": "Changing keywords from \"\" to \"maxima\".",
    "created_at": "2009-08-20T23:54:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6787",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6787#issuecomment-55934",
    "user": "AlexGhitza"
}
```

Changing keywords from "" to "maxima".



---

archive/issue_comments_055935.json:
```json
{
    "body": "This is due to Maxima's new formatting for eigenvectors -- the structure of the resulting list has changed.  See attached patch.",
    "created_at": "2009-08-21T00:48:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6787",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6787#issuecomment-55935",
    "user": "AlexGhitza"
}
```

This is due to Maxima's new formatting for eigenvectors -- the structure of the resulting list has changed.  See attached patch.



---

archive/issue_comments_055936.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-08-21T00:48:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6787",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6787#issuecomment-55936",
    "user": "AlexGhitza"
}
```

Changing status from new to assigned.



---

archive/issue_comments_055937.json:
```json
{
    "body": "Changing assignee from was to AlexGhitza.",
    "created_at": "2009-08-21T00:48:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6787",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6787#issuecomment-55937",
    "user": "AlexGhitza"
}
```

Changing assignee from was to AlexGhitza.



---

archive/issue_comments_055938.json:
```json
{
    "body": "Attachment\n\napply after spkg's at #6564 and #6699",
    "created_at": "2009-08-21T00:49:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6787",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6787#issuecomment-55938",
    "user": "AlexGhitza"
}
```

Attachment

apply after spkg's at #6564 and #6699



---

archive/issue_comments_055939.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-09-02T11:02:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6787",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6787#issuecomment-55939",
    "user": "mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_055940.json:
```json
{
    "body": "This is fixed by #6699.",
    "created_at": "2009-09-02T11:02:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6787",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6787#issuecomment-55940",
    "user": "mvngu"
}
```

This is fixed by #6699.
