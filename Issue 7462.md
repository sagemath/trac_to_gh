# Issue 7462: magma interface -- huge number of doctest failures

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-11-14 18:54:02

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



---

Comment by GeorgSWeber created at 2009-11-14 20:22:55

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

Attachment


---

Comment by klee created at 2009-11-16 06:05:02

The patch is made against Magma V2.15-9.


---

Comment by klee created at 2009-11-16 06:05:02

Changing status from new to needs_review.


---

Comment by GeorgSWeber created at 2009-11-16 16:52:07

Changing status from needs_review to positive_review.


---

Comment by GeorgSWeber created at 2009-11-16 16:52:07

Tested OK with Sage-4.2.1 and Magma V2.15-14.


---

Comment by GeorgSWeber created at 2009-11-16 16:57:44

(The summary is no longer used to display the status, see "Action".)


---

Comment by mhansen created at 2009-11-17 06:01:31

Resolution: fixed
