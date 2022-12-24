# Issue 7462: magma interface -- huge number of doctest failures

archive/issues_007462.json:
```json
{
    "body": "Assignee: was\n\nBecause we don't run the optional doctests regularly, tons of tests fail even in magma.py.  Fix them all.  Much of this is (probably) due to changes in Magma V2.15 over 2.14.\n\n\n```\nflat:interfaces wstein$ sage -t --only_optional=magma magma.py\nsage -t --only_optional=magma \"ge/build/sage/devel/sage-heegner/sage/interfaces/magma.py\"\n**********************************************************************\nFile \"/Users/wstein/sage/build/sage/devel/sage-heegner/sage/interfaces/magma.py\", line 187:\n    sage: y * 1.0                                                         # optional - magma\nExpected:\n    Traceback (most recent call last):\n    ...\n    TypeError: unsupported operand parent(s) for '*': 'Magma' and 'Real Field with 53 bits of precision'\nGot:\n    Traceback (most recent call last):\n      File \"/Users/wstein/s/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/Users/wstein/s/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/Users/wstein/s/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_0[46]>\", line 1, in <module>\n        y * RealNumber('1.0')                                                         # optional - magma###line 187:\n    sage: y * 1.0                                                         # optional - magma\n      File \"element.pyx\", line 1195, in sage.structure.element.RingElement.__mul__ (sage/structure/element.c:10248)\n      File \"coerce.pyx\", line 717, in sage.structure.coerce.CoercionModel_cache_maps.bin_op (sage/structure/coerce.c:6237)\n      File \"coerce.pyx\", line 713, in sage.structure.coerce.bin_op (sage/structure/coerce.c:6181)\n      File \"element.pyx\", line 1193, in sage.structure.element.RingElement.__mul__ (sage/structure/element.c:10229)\n      File \"element.pyx\", line 1197, in sage.structure.element.RingElement._mul_ (sage/structure/element.c:10294)\n      File \"/Users/wstein/s/local/lib/python/site-packages/sage/interfaces/expect.py\", line 1908, in _mul_\n        return self._operation('*', right)\n      File \"/Users/wstein/s/local/lib/python/site-packages/sage/interfaces/expect.py\", line 1865, in _operation\n        raise TypeError, msg\n    TypeError: Error evaluating Magma code.\n    IN:\n[27]:=_sage_[19] * _sage_[25];\n    OUT:\n    >> _sage_[27]:=_sage_[19] * _sage_[25];\n                              ^\n    Runtime error in '*': Bad argument types\n    Argument types given: RngUPolElt[RngInt], FldReElt\n    <BLANKLINE>\n**********************************************************************\nFile \"/Users/wstein/sage/build/sage/devel/sage-heegner/sage/interfaces/magma.py\", line 191:\n    sage: y * (2/3)                                                       # optional - magma\nExpected:\n    Traceback (most recent call last):\n    ...\n    TypeError: unsupported operand parent(s) for '*': 'Magma' and 'Rational Field'\nGot:\n    Traceback (most recent call last):\n      File \"/Users/wstein/s/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/Users/wstein/s/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/Users/wstein/s/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_0[47]>\", line 1, in <module>\n        y * (Integer(2)/Integer(3))                                                       # optional - magma###line 191:\n    sage: y * (2/3)                                                       # optional - magma\n      File \"element.pyx\", line 1195, in sage.structure.element.RingElement.__mul__ (sage/structure/element.c:10248)\n      File \"coerce.pyx\", line 717, in sage.structure.coerce.CoercionModel_cache_maps.bin_op (sage/structure/coerce.c:6237)\n      File \"coerce.pyx\", line 713, in sage.structure.coerce.bin_op (sage/structure/coerce.c:6181)\n      File \"element.pyx\", line 1193, in sage.structure.element.RingElement.__mul__ (sage/structure/element.c:10229)\n      File \"element.pyx\", line 1197, in sage.structure.element.RingElement._mul_ (sage/structure/element.c:10294)\n      File \"/Users/wstein/s/local/lib/python/site-packages/sage/interfaces/expect.py\", line 1908, in _mul_\n        return self._operation('*', right)\n      File \"/Users/wstein/s/local/lib/python/site-packages/sage/interfaces/expect.py\", line 1865, in _operation\n        raise TypeError, msg\n    TypeError: Error evaluating Magma code.\n    IN:\n[29]:=_sage_[19] * _sage_[28];\n    OUT:\n    >> _sage_[29]:=_sage_[19] * _sage_[28];\n                              ^\n    Runtime error in '*': Bad argument types\n    Argument types given: RngUPolElt[RngInt], FldRatElt\n    <BLANKLINE>\n**********************************************************************\nFile \"/Users/wstein/sage/build/sage/devel/sage-heegner/sage/interfaces/magma.py\", line 919:\n    sage: magma.attach('%s/data/extcode/magma/sage/basic.m'%Sage_ROOT)    # optional - magma\nException raised:\n    Traceback (most recent call last):\n      File \"/Users/wstein/s/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/Users/wstein/s/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/Users/wstein/s/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_14[2]>\", line 1, in <module>\n        magma.attach('%s/data/extcode/magma/sage/basic.m'%Sage_ROOT)    # optional - magma###line 919:\n    sage: magma.attach('%s/data/extcode/magma/sage/basic.m'%Sage_ROOT)    # optional - magma\n    NameError: name 'Sage_ROOT' is not defined\n**********************************************************************\nFile \"/Users/wstein/sage/build/sage/devel/sage-heegner/sage/interfaces/magma.py\", line 923:\n    sage: magma.attach('%s/data/extcode/magma/sage/basic2.m'%Sage_ROOT)     # optional - magma\nExpected:\n    Traceback (most recent call last):\n    ...\n    RuntimeError: Error evaluating Magma code...\nGot:\n    Traceback (most recent call last):\n      File \"/Users/wstein/s/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/Users/wstein/s/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/Users/wstein/s/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_14[3]>\", line 1, in <module>\n        magma.attach('%s/data/extcode/magma/sage/basic2.m'%Sage_ROOT)     # optional - magma###line 923:\n    sage: magma.attach('%s/data/extcode/magma/sage/basic2.m'%Sage_ROOT)     # optional - magma\n    NameError: name 'Sage_ROOT' is not defined\n**********************************************************************\nFile \"/Users/wstein/sage/build/sage/devel/sage-heegner/sage/interfaces/magma.py\", line 1069:\n    sage: magma.function_call('PolynomialRing', [QQ,2])      # optional - magma\nExpected:\n    Polynomial ring of rank 2 over Rational Field\n    Lexicographical Order\n    Variables: $.1, $.2\nGot:\n    Polynomial ring of rank 2 over Rational Field\n    Order: Lexicographical\n    Variables: $.1, $.2\n**********************************************************************\nFile \"/Users/wstein/sage/build/sage/devel/sage-heegner/sage/interfaces/magma.py\", line 1471:\n    sage: magma.ideal([x^2, y^3*x])         # optional - magma\nExpected:\n    Ideal of Polynomial ring of rank 2 over Rational Field\n    Graded Reverse Lexicographical Order\n    Variables: x, y\n    Basis:\n    [\n    x^2,\n    x*y^3\n    ]\nGot:\n    Ideal of Polynomial ring of rank 2 over Rational Field\n    Order: Graded Reverse Lexicographical\n    Variables: x, y\n    Homogeneous\n    Basis:\n    [\n    x^2,\n    x*y^3\n    ]\n**********************************************************************\nFile \"/Users/wstein/sage/build/sage/devel/sage-heegner/sage/interfaces/magma.py\", line 504:\n    sage: magma.eval(\"a := %s;\"%(10^10000))    # optional - magma\nExpected:\n    \"\nGot:\n    ''\n**********************************************************************\nFile \"/Users/wstein/sage/build/sage/devel/sage-heegner/sage/interfaces/magma.py\", line 2119:\n    sage: w = V.__iter__(); w                           # optional - magma\nExpected:\n    <generator object at ...>\nGot:\n    <generator object __iter__ at 0x10bb1e7d0>\n**********************************************************************\nFile \"/Users/wstein/sage/build/sage/devel/sage-heegner/sage/interfaces/magma.py\", line 2211:\n    sage: magma.eval('R<x> := PolynomialRing(RationalField()); f := (x-17/2)^3;')     # optional - magma\nExpected:\n    \"\nGot:\n    ''\n**********************************************************************\nFile \"/Users/wstein/sage/build/sage/devel/sage-heegner/sage/interfaces/magma.py\", line 2223:\n    sage: magma.eval('K<a> := CyclotomicField(11)')       # optional - magma\nExpected:\n    \"\nGot:\n    ''\n**********************************************************************\nFile \"/Users/wstein/sage/build/sage/devel/sage-heegner/sage/interfaces/magma.py\", line 630:\n    sage: R                                    # optional - magma\nExpected:\n    Polynomial ring of rank 2 over Rational Field\n    Lexicographical Order\n    Variables: X, Y\nGot:\n    Polynomial ring of rank 2 over Rational Field\n    Order: Lexicographical\n    Variables: X, Y\n**********************************************************************\nFile \"/Users/wstein/sage/build/sage/devel/sage-heegner/sage/interfaces/magma.py\", line 634:\n    sage: S                                    # optional - magma\nExpected:\n    Polynomial ring of rank 2 over Rational Field\n    Lexicographical Order\n    Variables: X, Y\nGot:\n    Polynomial ring of rank 2 over Rational Field\n    Order: Lexicographical\n    Variables: X, Y\n**********************************************************************\nFile \"/Users/wstein/sage/build/sage/devel/sage-heegner/sage/interfaces/magma.py\", line 669:\n    sage: magma('PolynomialRing(RationalField(), 3)', 'x,y,z')  # optional - magma\nExpected:\n    Polynomial ring of rank 3 over Rational Field\n    Lexicographical Order\n    Variables: x, y, z\nGot:\n    Polynomial ring of rank 3 over Rational Field\n    Order: Lexicographical\n    Variables: x, y, z\n**********************************************************************\n9 items had failures:\n   2 of  48 in __main__.example_0\n   2 of   4 in __main__.example_14\n   1 of   8 in __main__.example_18\n   1 of   4 in __main__.example_24\n   1 of   4 in __main__.example_3\n   1 of   8 in __main__.example_44\n   2 of  28 in __main__.example_47\n   2 of   7 in __main__.example_7\n   1 of  17 in __main__.example_8\n***Test Failed*** 13 failures.\nFor whitespace errors, see the file /Users/wstein/.sage//tmp/.doctest_magma.py\n\t [23.2 s]\nexit code: 1024\n \n----------------------------------------------------------------------\nThe following tests failed:\n\n\n\tsage -t --only_optional=magma \"ge/build/sage/devel/sage-heegner/sage/interfaces/magma.py\"\nTotal time for all tests: 23.2 seconds\nflat:interfaces wstein$ \n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7462\n\n",
    "created_at": "2009-11-14T18:54:02Z",
    "labels": [
        "interfaces",
        "major",
        "bug"
    ],
    "title": "magma interface -- huge number of doctest failures",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7462",
    "user": "was"
}
```
Assignee: was

Because we don't run the optional doctests regularly, tons of tests fail even in magma.py.  Fix them all.  Much of this is (probably) due to changes in Magma V2.15 over 2.14.


```
flat:interfaces wstein$ sage -t --only_optional=magma magma.py
sage -t --only_optional=magma "ge/build/sage/devel/sage-heegner/sage/interfaces/magma.py"
**********************************************************************
File "/Users/wstein/sage/build/sage/devel/sage-heegner/sage/interfaces/magma.py", line 187:
    sage: y * 1.0                                                         # optional - magma
Expected:
    Traceback (most recent call last):
    ...
    TypeError: unsupported operand parent(s) for '*': 'Magma' and 'Real Field with 53 bits of precision'
Got:
    Traceback (most recent call last):
      File "/Users/wstein/s/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/Users/wstein/s/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/Users/wstein/s/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[46]>", line 1, in <module>
        y * RealNumber('1.0')                                                         # optional - magma###line 187:
    sage: y * 1.0                                                         # optional - magma
      File "element.pyx", line 1195, in sage.structure.element.RingElement.__mul__ (sage/structure/element.c:10248)
      File "coerce.pyx", line 717, in sage.structure.coerce.CoercionModel_cache_maps.bin_op (sage/structure/coerce.c:6237)
      File "coerce.pyx", line 713, in sage.structure.coerce.bin_op (sage/structure/coerce.c:6181)
      File "element.pyx", line 1193, in sage.structure.element.RingElement.__mul__ (sage/structure/element.c:10229)
      File "element.pyx", line 1197, in sage.structure.element.RingElement._mul_ (sage/structure/element.c:10294)
      File "/Users/wstein/s/local/lib/python/site-packages/sage/interfaces/expect.py", line 1908, in _mul_
        return self._operation('*', right)
      File "/Users/wstein/s/local/lib/python/site-packages/sage/interfaces/expect.py", line 1865, in _operation
        raise TypeError, msg
    TypeError: Error evaluating Magma code.
    IN:
[27]:=_sage_[19] * _sage_[25];
    OUT:
    >> _sage_[27]:=_sage_[19] * _sage_[25];
                              ^
    Runtime error in '*': Bad argument types
    Argument types given: RngUPolElt[RngInt], FldReElt
    <BLANKLINE>
**********************************************************************
File "/Users/wstein/sage/build/sage/devel/sage-heegner/sage/interfaces/magma.py", line 191:
    sage: y * (2/3)                                                       # optional - magma
Expected:
    Traceback (most recent call last):
    ...
    TypeError: unsupported operand parent(s) for '*': 'Magma' and 'Rational Field'
Got:
    Traceback (most recent call last):
      File "/Users/wstein/s/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/Users/wstein/s/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/Users/wstein/s/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[47]>", line 1, in <module>
        y * (Integer(2)/Integer(3))                                                       # optional - magma###line 191:
    sage: y * (2/3)                                                       # optional - magma
      File "element.pyx", line 1195, in sage.structure.element.RingElement.__mul__ (sage/structure/element.c:10248)
      File "coerce.pyx", line 717, in sage.structure.coerce.CoercionModel_cache_maps.bin_op (sage/structure/coerce.c:6237)
      File "coerce.pyx", line 713, in sage.structure.coerce.bin_op (sage/structure/coerce.c:6181)
      File "element.pyx", line 1193, in sage.structure.element.RingElement.__mul__ (sage/structure/element.c:10229)
      File "element.pyx", line 1197, in sage.structure.element.RingElement._mul_ (sage/structure/element.c:10294)
      File "/Users/wstein/s/local/lib/python/site-packages/sage/interfaces/expect.py", line 1908, in _mul_
        return self._operation('*', right)
      File "/Users/wstein/s/local/lib/python/site-packages/sage/interfaces/expect.py", line 1865, in _operation
        raise TypeError, msg
    TypeError: Error evaluating Magma code.
    IN:
[29]:=_sage_[19] * _sage_[28];
    OUT:
    >> _sage_[29]:=_sage_[19] * _sage_[28];
                              ^
    Runtime error in '*': Bad argument types
    Argument types given: RngUPolElt[RngInt], FldRatElt
    <BLANKLINE>
**********************************************************************
File "/Users/wstein/sage/build/sage/devel/sage-heegner/sage/interfaces/magma.py", line 919:
    sage: magma.attach('%s/data/extcode/magma/sage/basic.m'%Sage_ROOT)    # optional - magma
Exception raised:
    Traceback (most recent call last):
      File "/Users/wstein/s/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/Users/wstein/s/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/Users/wstein/s/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_14[2]>", line 1, in <module>
        magma.attach('%s/data/extcode/magma/sage/basic.m'%Sage_ROOT)    # optional - magma###line 919:
    sage: magma.attach('%s/data/extcode/magma/sage/basic.m'%Sage_ROOT)    # optional - magma
    NameError: name 'Sage_ROOT' is not defined
**********************************************************************
File "/Users/wstein/sage/build/sage/devel/sage-heegner/sage/interfaces/magma.py", line 923:
    sage: magma.attach('%s/data/extcode/magma/sage/basic2.m'%Sage_ROOT)     # optional - magma
Expected:
    Traceback (most recent call last):
    ...
    RuntimeError: Error evaluating Magma code...
Got:
    Traceback (most recent call last):
      File "/Users/wstein/s/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/Users/wstein/s/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/Users/wstein/s/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_14[3]>", line 1, in <module>
        magma.attach('%s/data/extcode/magma/sage/basic2.m'%Sage_ROOT)     # optional - magma###line 923:
    sage: magma.attach('%s/data/extcode/magma/sage/basic2.m'%Sage_ROOT)     # optional - magma
    NameError: name 'Sage_ROOT' is not defined
**********************************************************************
File "/Users/wstein/sage/build/sage/devel/sage-heegner/sage/interfaces/magma.py", line 1069:
    sage: magma.function_call('PolynomialRing', [QQ,2])      # optional - magma
Expected:
    Polynomial ring of rank 2 over Rational Field
    Lexicographical Order
    Variables: $.1, $.2
Got:
    Polynomial ring of rank 2 over Rational Field
    Order: Lexicographical
    Variables: $.1, $.2
**********************************************************************
File "/Users/wstein/sage/build/sage/devel/sage-heegner/sage/interfaces/magma.py", line 1471:
    sage: magma.ideal([x^2, y^3*x])         # optional - magma
Expected:
    Ideal of Polynomial ring of rank 2 over Rational Field
    Graded Reverse Lexicographical Order
    Variables: x, y
    Basis:
    [
    x^2,
    x*y^3
    ]
Got:
    Ideal of Polynomial ring of rank 2 over Rational Field
    Order: Graded Reverse Lexicographical
    Variables: x, y
    Homogeneous
    Basis:
    [
    x^2,
    x*y^3
    ]
**********************************************************************
File "/Users/wstein/sage/build/sage/devel/sage-heegner/sage/interfaces/magma.py", line 504:
    sage: magma.eval("a := %s;"%(10^10000))    # optional - magma
Expected:
    "
Got:
    ''
**********************************************************************
File "/Users/wstein/sage/build/sage/devel/sage-heegner/sage/interfaces/magma.py", line 2119:
    sage: w = V.__iter__(); w                           # optional - magma
Expected:
    <generator object at ...>
Got:
    <generator object __iter__ at 0x10bb1e7d0>
**********************************************************************
File "/Users/wstein/sage/build/sage/devel/sage-heegner/sage/interfaces/magma.py", line 2211:
    sage: magma.eval('R<x> := PolynomialRing(RationalField()); f := (x-17/2)^3;')     # optional - magma
Expected:
    "
Got:
    ''
**********************************************************************
File "/Users/wstein/sage/build/sage/devel/sage-heegner/sage/interfaces/magma.py", line 2223:
    sage: magma.eval('K<a> := CyclotomicField(11)')       # optional - magma
Expected:
    "
Got:
    ''
**********************************************************************
File "/Users/wstein/sage/build/sage/devel/sage-heegner/sage/interfaces/magma.py", line 630:
    sage: R                                    # optional - magma
Expected:
    Polynomial ring of rank 2 over Rational Field
    Lexicographical Order
    Variables: X, Y
Got:
    Polynomial ring of rank 2 over Rational Field
    Order: Lexicographical
    Variables: X, Y
**********************************************************************
File "/Users/wstein/sage/build/sage/devel/sage-heegner/sage/interfaces/magma.py", line 634:
    sage: S                                    # optional - magma
Expected:
    Polynomial ring of rank 2 over Rational Field
    Lexicographical Order
    Variables: X, Y
Got:
    Polynomial ring of rank 2 over Rational Field
    Order: Lexicographical
    Variables: X, Y
**********************************************************************
File "/Users/wstein/sage/build/sage/devel/sage-heegner/sage/interfaces/magma.py", line 669:
    sage: magma('PolynomialRing(RationalField(), 3)', 'x,y,z')  # optional - magma
Expected:
    Polynomial ring of rank 3 over Rational Field
    Lexicographical Order
    Variables: x, y, z
Got:
    Polynomial ring of rank 3 over Rational Field
    Order: Lexicographical
    Variables: x, y, z
**********************************************************************
9 items had failures:
   2 of  48 in __main__.example_0
   2 of   4 in __main__.example_14
   1 of   8 in __main__.example_18
   1 of   4 in __main__.example_24
   1 of   4 in __main__.example_3
   1 of   8 in __main__.example_44
   2 of  28 in __main__.example_47
   2 of   7 in __main__.example_7
   1 of  17 in __main__.example_8
***Test Failed*** 13 failures.
For whitespace errors, see the file /Users/wstein/.sage//tmp/.doctest_magma.py
	 [23.2 s]
exit code: 1024
 
----------------------------------------------------------------------
The following tests failed:


	sage -t --only_optional=magma "ge/build/sage/devel/sage-heegner/sage/interfaces/magma.py"
Total time for all tests: 23.2 seconds
flat:interfaces wstein$ 
```


Issue created by migration from https://trac.sagemath.org/ticket/7462





---

archive/issue_comments_062852.json:
```json
{
    "body": "For the record, there are \"only\" 5 items, instead of 9, with failures when tested Sage-4.2 against Magma v2.14-9 (I didn't install v2.15 yet):\n\n```\nsage -t --only_optional=magma \"devel/sage/sage/interfaces/magma.py\"\n**********************************************************************\nFile \"/Users/Shared/sage/build/sage-4.2/devel/sage/sage/interfaces/magma.py\", line 147:\n    sage: y * 1.0                                                         # optional - magma\nExpected:\n    Traceback (most recent call last):\n    ...\n    TypeError: unsupported operand parent(s) for '*': 'Magma' and 'Real Field with 53 bits of precision'\nGot:\n    Traceback (most recent call last):\n      File \"/Users/Shared/sage/build/sage-4.2/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/Users/Shared/sage/build/sage-4.2/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/Users/Shared/sage/build/sage-4.2/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_0[40]>\", line 1, in <module>\n        y * RealNumber('1.0')                                                         # optional - magma###line 147:\n    sage: y * 1.0                                                         # optional - magma\n      File \"element.pyx\", line 1195, in sage.structure.element.RingElement.__mul__ (sage/structure/element.c:10248)\n      File \"coerce.pyx\", line 717, in sage.structure.coerce.CoercionModel_cache_maps.bin_op (sage/structure/coerce.c:6237)\n      File \"coerce.pyx\", line 713, in sage.structure.coerce.bin_op (sage/structure/coerce.c:6181)\n      File \"element.pyx\", line 1193, in sage.structure.element.RingElement.__mul__ (sage/structure/element.c:10229)\n      File \"element.pyx\", line 1197, in sage.structure.element.RingElement._mul_ (sage/structure/element.c:10294)\n      File \"/Users/Shared/sage/build/sage-4.2/local/lib/python/site-packages/sage/interfaces/expect.py\", line 1908, in _mul_\n        return self._operation('*', right)\n      File \"/Users/Shared/sage/build/sage-4.2/local/lib/python/site-packages/sage/interfaces/expect.py\", line 1865, in _operation\n        raise TypeError, msg\n    TypeError: Error evaluating Magma code.\n    IN:\n[27]:=_sage_[19] * _sage_[25];\n    OUT:\n    >> _sage_[27]:=_sage_[19] * _sage_[25];\n                              ^\n    Runtime error in '*': Bad argument types\n    Argument types given: RngUPolElt[RngInt], FldReElt\n    <BLANKLINE>\n**********************************************************************\nFile \"/Users/Shared/sage/build/sage-4.2/devel/sage/sage/interfaces/magma.py\", line 151:\n    sage: y * (2/3)                                                       # optional - magma\nExpected:\n    Traceback (most recent call last):\n    ...\n    TypeError: unsupported operand parent(s) for '*': 'Magma' and 'Rational Field'\nGot:\n    Traceback (most recent call last):\n      File \"/Users/Shared/sage/build/sage-4.2/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/Users/Shared/sage/build/sage-4.2/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/Users/Shared/sage/build/sage-4.2/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_0[41]>\", line 1, in <module>\n        y * (Integer(2)/Integer(3))                                                       # optional - magma###line 151:\n    sage: y * (2/3)                                                       # optional - magma\n      File \"element.pyx\", line 1195, in sage.structure.element.RingElement.__mul__ (sage/structure/element.c:10248)\n      File \"coerce.pyx\", line 717, in sage.structure.coerce.CoercionModel_cache_maps.bin_op (sage/structure/coerce.c:6237)\n      File \"coerce.pyx\", line 713, in sage.structure.coerce.bin_op (sage/structure/coerce.c:6181)\n      File \"element.pyx\", line 1193, in sage.structure.element.RingElement.__mul__ (sage/structure/element.c:10229)\n      File \"element.pyx\", line 1197, in sage.structure.element.RingElement._mul_ (sage/structure/element.c:10294)\n      File \"/Users/Shared/sage/build/sage-4.2/local/lib/python/site-packages/sage/interfaces/expect.py\", line 1908, in _mul_\n        return self._operation('*', right)\n      File \"/Users/Shared/sage/build/sage-4.2/local/lib/python/site-packages/sage/interfaces/expect.py\", line 1865, in _operation\n        raise TypeError, msg\n    TypeError: Error evaluating Magma code.\n    IN:\n[29]:=_sage_[19] * _sage_[28];\n    OUT:\n    >> _sage_[29]:=_sage_[19] * _sage_[28];\n                              ^\n    Runtime error in '*': Bad argument types\n    Argument types given: RngUPolElt[RngInt], FldRatElt\n    <BLANKLINE>\n**********************************************************************\nFile \"/Users/Shared/sage/build/sage-4.2/devel/sage/sage/interfaces/magma.py\", line 879:\n    sage: magma.attach('%s/data/extcode/magma/sage/basic.m'%Sage_ROOT)    # optional - magma\nException raised:\n    Traceback (most recent call last):\n      File \"/Users/Shared/sage/build/sage-4.2/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/Users/Shared/sage/build/sage-4.2/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/Users/Shared/sage/build/sage-4.2/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_14[2]>\", line 1, in <module>\n        magma.attach('%s/data/extcode/magma/sage/basic.m'%Sage_ROOT)    # optional - magma###line 879:\n    sage: magma.attach('%s/data/extcode/magma/sage/basic.m'%Sage_ROOT)    # optional - magma\n    NameError: name 'Sage_ROOT' is not defined\n**********************************************************************\nFile \"/Users/Shared/sage/build/sage-4.2/devel/sage/sage/interfaces/magma.py\", line 883:\n    sage: magma.attach('%s/data/extcode/magma/sage/basic2.m'%Sage_ROOT)     # optional - magma\nExpected:\n    Traceback (most recent call last):\n    ...\n    RuntimeError: Error evaluating Magma code...\nGot:\n    Traceback (most recent call last):\n      File \"/Users/Shared/sage/build/sage-4.2/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/Users/Shared/sage/build/sage-4.2/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/Users/Shared/sage/build/sage-4.2/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_14[3]>\", line 1, in <module>\n        magma.attach('%s/data/extcode/magma/sage/basic2.m'%Sage_ROOT)     # optional - magma###line 883:\n    sage: magma.attach('%s/data/extcode/magma/sage/basic2.m'%Sage_ROOT)     # optional - magma\n    NameError: name 'Sage_ROOT' is not defined\n**********************************************************************\nFile \"/Users/Shared/sage/build/sage-4.2/devel/sage/sage/interfaces/magma.py\", line 464:\n    sage: magma.eval(\"a := %s;\"%(10^10000))    # optional - magma\nExpected:\n    \"\nGot:\n    ''\n**********************************************************************\nFile \"/Users/Shared/sage/build/sage-4.2/devel/sage/sage/interfaces/magma.py\", line 2079:\n    sage: w = V.__iter__(); w                           # optional - magma\nExpected:\n    <generator object at ...>\nGot:\n    <generator object __iter__ at 0x112684e0>\n**********************************************************************\nFile \"/Users/Shared/sage/build/sage-4.2/devel/sage/sage/interfaces/magma.py\", line 2171:\n    sage: magma.eval('R<x> := PolynomialRing(RationalField()); f := (x-17/2)^3;')     # optional - magma\nExpected:\n    \"\nGot:\n    ''\n**********************************************************************\nFile \"/Users/Shared/sage/build/sage-4.2/devel/sage/sage/interfaces/magma.py\", line 2183:\n    sage: magma.eval('K<a> := CyclotomicField(11)')       # optional - magma\nExpected:\n    \"\nGot:\n    ''\n**********************************************************************\n5 items had failures:\n   2 of  42 in __main__.example_0\n   2 of   4 in __main__.example_14\n   1 of   4 in __main__.example_3\n   1 of   8 in __main__.example_44\n   2 of  28 in __main__.example_47\n***Test Failed*** 8 failures.\nFor whitespace errors, see the file /Users/georgweber/.sage//tmp/.doctest_magma.py\n         [50.6 s]\nexit code: 1024\n \n----------------------------------------------------------------------\nThe following tests failed:\n\n\n        sage -t --only_optional=magma \"devel/sage/sage/interfaces/magma.py\"\n```\n",
    "created_at": "2009-11-14T20:22:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7462",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7462#issuecomment-62852",
    "user": "GeorgSWeber"
}
```

For the record, there are "only" 5 items, instead of 9, with failures when tested Sage-4.2 against Magma v2.14-9 (I didn't install v2.15 yet):

```
sage -t --only_optional=magma "devel/sage/sage/interfaces/magma.py"
**********************************************************************
File "/Users/Shared/sage/build/sage-4.2/devel/sage/sage/interfaces/magma.py", line 147:
    sage: y * 1.0                                                         # optional - magma
Expected:
    Traceback (most recent call last):
    ...
    TypeError: unsupported operand parent(s) for '*': 'Magma' and 'Real Field with 53 bits of precision'
Got:
    Traceback (most recent call last):
      File "/Users/Shared/sage/build/sage-4.2/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/Users/Shared/sage/build/sage-4.2/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/Users/Shared/sage/build/sage-4.2/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[40]>", line 1, in <module>
        y * RealNumber('1.0')                                                         # optional - magma###line 147:
    sage: y * 1.0                                                         # optional - magma
      File "element.pyx", line 1195, in sage.structure.element.RingElement.__mul__ (sage/structure/element.c:10248)
      File "coerce.pyx", line 717, in sage.structure.coerce.CoercionModel_cache_maps.bin_op (sage/structure/coerce.c:6237)
      File "coerce.pyx", line 713, in sage.structure.coerce.bin_op (sage/structure/coerce.c:6181)
      File "element.pyx", line 1193, in sage.structure.element.RingElement.__mul__ (sage/structure/element.c:10229)
      File "element.pyx", line 1197, in sage.structure.element.RingElement._mul_ (sage/structure/element.c:10294)
      File "/Users/Shared/sage/build/sage-4.2/local/lib/python/site-packages/sage/interfaces/expect.py", line 1908, in _mul_
        return self._operation('*', right)
      File "/Users/Shared/sage/build/sage-4.2/local/lib/python/site-packages/sage/interfaces/expect.py", line 1865, in _operation
        raise TypeError, msg
    TypeError: Error evaluating Magma code.
    IN:
[27]:=_sage_[19] * _sage_[25];
    OUT:
    >> _sage_[27]:=_sage_[19] * _sage_[25];
                              ^
    Runtime error in '*': Bad argument types
    Argument types given: RngUPolElt[RngInt], FldReElt
    <BLANKLINE>
**********************************************************************
File "/Users/Shared/sage/build/sage-4.2/devel/sage/sage/interfaces/magma.py", line 151:
    sage: y * (2/3)                                                       # optional - magma
Expected:
    Traceback (most recent call last):
    ...
    TypeError: unsupported operand parent(s) for '*': 'Magma' and 'Rational Field'
Got:
    Traceback (most recent call last):
      File "/Users/Shared/sage/build/sage-4.2/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/Users/Shared/sage/build/sage-4.2/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/Users/Shared/sage/build/sage-4.2/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[41]>", line 1, in <module>
        y * (Integer(2)/Integer(3))                                                       # optional - magma###line 151:
    sage: y * (2/3)                                                       # optional - magma
      File "element.pyx", line 1195, in sage.structure.element.RingElement.__mul__ (sage/structure/element.c:10248)
      File "coerce.pyx", line 717, in sage.structure.coerce.CoercionModel_cache_maps.bin_op (sage/structure/coerce.c:6237)
      File "coerce.pyx", line 713, in sage.structure.coerce.bin_op (sage/structure/coerce.c:6181)
      File "element.pyx", line 1193, in sage.structure.element.RingElement.__mul__ (sage/structure/element.c:10229)
      File "element.pyx", line 1197, in sage.structure.element.RingElement._mul_ (sage/structure/element.c:10294)
      File "/Users/Shared/sage/build/sage-4.2/local/lib/python/site-packages/sage/interfaces/expect.py", line 1908, in _mul_
        return self._operation('*', right)
      File "/Users/Shared/sage/build/sage-4.2/local/lib/python/site-packages/sage/interfaces/expect.py", line 1865, in _operation
        raise TypeError, msg
    TypeError: Error evaluating Magma code.
    IN:
[29]:=_sage_[19] * _sage_[28];
    OUT:
    >> _sage_[29]:=_sage_[19] * _sage_[28];
                              ^
    Runtime error in '*': Bad argument types
    Argument types given: RngUPolElt[RngInt], FldRatElt
    <BLANKLINE>
**********************************************************************
File "/Users/Shared/sage/build/sage-4.2/devel/sage/sage/interfaces/magma.py", line 879:
    sage: magma.attach('%s/data/extcode/magma/sage/basic.m'%Sage_ROOT)    # optional - magma
Exception raised:
    Traceback (most recent call last):
      File "/Users/Shared/sage/build/sage-4.2/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/Users/Shared/sage/build/sage-4.2/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/Users/Shared/sage/build/sage-4.2/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_14[2]>", line 1, in <module>
        magma.attach('%s/data/extcode/magma/sage/basic.m'%Sage_ROOT)    # optional - magma###line 879:
    sage: magma.attach('%s/data/extcode/magma/sage/basic.m'%Sage_ROOT)    # optional - magma
    NameError: name 'Sage_ROOT' is not defined
**********************************************************************
File "/Users/Shared/sage/build/sage-4.2/devel/sage/sage/interfaces/magma.py", line 883:
    sage: magma.attach('%s/data/extcode/magma/sage/basic2.m'%Sage_ROOT)     # optional - magma
Expected:
    Traceback (most recent call last):
    ...
    RuntimeError: Error evaluating Magma code...
Got:
    Traceback (most recent call last):
      File "/Users/Shared/sage/build/sage-4.2/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/Users/Shared/sage/build/sage-4.2/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/Users/Shared/sage/build/sage-4.2/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_14[3]>", line 1, in <module>
        magma.attach('%s/data/extcode/magma/sage/basic2.m'%Sage_ROOT)     # optional - magma###line 883:
    sage: magma.attach('%s/data/extcode/magma/sage/basic2.m'%Sage_ROOT)     # optional - magma
    NameError: name 'Sage_ROOT' is not defined
**********************************************************************
File "/Users/Shared/sage/build/sage-4.2/devel/sage/sage/interfaces/magma.py", line 464:
    sage: magma.eval("a := %s;"%(10^10000))    # optional - magma
Expected:
    "
Got:
    ''
**********************************************************************
File "/Users/Shared/sage/build/sage-4.2/devel/sage/sage/interfaces/magma.py", line 2079:
    sage: w = V.__iter__(); w                           # optional - magma
Expected:
    <generator object at ...>
Got:
    <generator object __iter__ at 0x112684e0>
**********************************************************************
File "/Users/Shared/sage/build/sage-4.2/devel/sage/sage/interfaces/magma.py", line 2171:
    sage: magma.eval('R<x> := PolynomialRing(RationalField()); f := (x-17/2)^3;')     # optional - magma
Expected:
    "
Got:
    ''
**********************************************************************
File "/Users/Shared/sage/build/sage-4.2/devel/sage/sage/interfaces/magma.py", line 2183:
    sage: magma.eval('K<a> := CyclotomicField(11)')       # optional - magma
Expected:
    "
Got:
    ''
**********************************************************************
5 items had failures:
   2 of  42 in __main__.example_0
   2 of   4 in __main__.example_14
   1 of   4 in __main__.example_3
   1 of   8 in __main__.example_44
   2 of  28 in __main__.example_47
***Test Failed*** 8 failures.
For whitespace errors, see the file /Users/georgweber/.sage//tmp/.doctest_magma.py
         [50.6 s]
exit code: 1024
 
----------------------------------------------------------------------
The following tests failed:


        sage -t --only_optional=magma "devel/sage/sage/interfaces/magma.py"
```




---

archive/issue_comments_062853.json:
```json
{
    "body": "Attachment [trac_7462.patch](tarball://root/attachments/some-uuid/ticket7462/trac_7462.patch) by klee created at 2009-11-16 06:00:56",
    "created_at": "2009-11-16T06:00:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7462",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7462#issuecomment-62853",
    "user": "klee"
}
```

Attachment [trac_7462.patch](tarball://root/attachments/some-uuid/ticket7462/trac_7462.patch) by klee created at 2009-11-16 06:00:56



---

archive/issue_comments_062854.json:
```json
{
    "body": "The patch is made against Magma V2.15-9.",
    "created_at": "2009-11-16T06:05:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7462",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7462#issuecomment-62854",
    "user": "klee"
}
```

The patch is made against Magma V2.15-9.



---

archive/issue_comments_062855.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-11-16T06:05:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7462",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7462#issuecomment-62855",
    "user": "klee"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_062856.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-11-16T16:52:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7462",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7462#issuecomment-62856",
    "user": "GeorgSWeber"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_062857.json:
```json
{
    "body": "Tested OK with Sage-4.2.1 and Magma V2.15-14.",
    "created_at": "2009-11-16T16:52:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7462",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7462#issuecomment-62857",
    "user": "GeorgSWeber"
}
```

Tested OK with Sage-4.2.1 and Magma V2.15-14.



---

archive/issue_comments_062858.json:
```json
{
    "body": "(The summary is no longer used to display the status, see \"Action\".)",
    "created_at": "2009-11-16T16:57:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7462",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7462#issuecomment-62858",
    "user": "GeorgSWeber"
}
```

(The summary is no longer used to display the status, see "Action".)



---

archive/issue_comments_062859.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-11-17T06:01:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7462",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7462#issuecomment-62859",
    "user": "mhansen"
}
```

Resolution: fixed
