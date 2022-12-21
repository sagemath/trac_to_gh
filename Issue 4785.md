# Issue 4785: Failure of tests in sage/schemes/elliptic_curves/ell_generic.py due to non installed magma

Issue created by migration from Trac.

Original creator: jsp

Original creation time: 2008-12-13 21:16:24

Assignee: was

This is sage-3.2.2.alpha2 on Fedora 9, 32 bits.
The following test failed:
 

```
sage -t  "devel/sage/sage/schemes/elliptic_curves/ell_generic.py"

**********************************************************************
File "/home/jaap/work/downloads/sage-3.2.2.alpha0/devel/sage/sage/schemes/elliptic_curves/ell_generic.py", line 191, in __main__.example_8
Failed example:
    magma(E)###line 308:_sage_    >>> magma(E)
Exception raised:
    Traceback (most recent call last):
      File "/home/jaap/downloads/sage-3.2.1.alpha2/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/jaap/downloads/sage-3.2.1.alpha2/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/jaap/downloads/sage-3.2.1.alpha2/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_8[4]>", line 1, in <module>
        magma(E)###line 308:_sage_    >>> magma(E)
      File "/home/jaap/downloads/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/interfaces/magma.py", line 554, in __call__
        A = Expect.__call__(self, x)
      File "/home/jaap/downloads/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 967, in __call__
        return self._coerce_from_special_method(x)
      File "/home/jaap/downloads/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/interfaces/magma.py", line 591, in _coerce_from_special_method
        s = x._magma_init_(self)
      File "/home/jaap/downloads/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/ell_generic.py", line 316, in _magma_init_
        kmn = magma(self.base_ring())._ref()
      File "/home/jaap/downloads/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/interfaces/magma.py", line 554, in __call__
        A = Expect.__call__(self, x)
      File "/home/jaap/downloads/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 967, in __call__
        return self._coerce_from_special_method(x)
      File "/home/jaap/downloads/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/interfaces/magma.py", line 591, in _coerce_from_special_method
        s = x._magma_init_(self)
      File "ring.pyx", line 1566, in sage.rings.ring.FiniteField._magma_init_ (sage/rings/ring.c:8004)
      File "polynomial_element.pyx", line 2956, in sage.rings.polynomial.polynomial_element.Polynomial._magma_init_ (sage/rings/polynomial/polynomial_element.c:22024)
      File "/home/jaap/downloads/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/interfaces/magma.py", line 554, in __call__
        A = Expect.__call__(self, x)
      File "/home/jaap/downloads/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 967, in __call__
        return self._coerce_from_special_method(x)
      File "/home/jaap/downloads/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/interfaces/magma.py", line 591, in _coerce_from_special_method
        s = x._magma_init_(self)
      File "/home/jaap/downloads/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/rings/polynomial/polynomial_ring.py", line 387, in _magma_init_
        B = magma(self.base_ring())
      File "/home/jaap/downloads/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/interfaces/magma.py", line 554, in __call__
        A = Expect.__call__(self, x)
      File "/home/jaap/downloads/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 967, in __call__
        return self._coerce_from_special_method(x)
      File "/home/jaap/downloads/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/interfaces/magma.py", line 592, in _coerce_from_special_method
        a = self(s)
      File "/home/jaap/downloads/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/interfaces/magma.py", line 554, in __call__
        A = Expect.__call__(self, x)
      File "/home/jaap/downloads/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 965, in __call__
        return cls(self, x, name=name)
      File "/home/jaap/downloads/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 1335, in __init__
        raise TypeError, x
    TypeError: Unable to start magma because the command 'magma -n' failed.

**********************************************************************
File "/home/jaap/work/downloads/sage-3.2.2.alpha0/devel/sage/sage/schemes/elliptic_curves/ell_generic.py", line 193, in __main__.example_8
Failed example:
    magma(EllipticCurve([Integer(1)/Integer(2),Integer(2)/Integer(3),-Integer(4)/Integer(5),Integer(6)/Integer(7),Integer(8)/Integer(9)]))###line 310:_sage_    >>> magma(EllipticCurve([1/2,2/3,-4/5,6/7,8/9]))
Exception raised:
    Traceback (most recent call last):
      File "/home/jaap/downloads/sage-3.2.1.alpha2/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/jaap/downloads/sage-3.2.1.alpha2/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/jaap/downloads/sage-3.2.1.alpha2/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_8[5]>", line 1, in <module>
        magma(EllipticCurve([Integer(1)/Integer(2),Integer(2)/Integer(3),-Integer(4)/Integer(5),Integer(6)/Integer(7),Integer(8)/Integer(9)]))###line 310:_sage_    >>> magma(EllipticCurve([1/2,2/3,-4/5,6/7,8/9]))
      File "/home/jaap/downloads/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/interfaces/magma.py", line 554, in __call__
        A = Expect.__call__(self, x)
      File "/home/jaap/downloads/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 967, in __call__
        return self._coerce_from_special_method(x)
      File "/home/jaap/downloads/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/interfaces/magma.py", line 591, in _coerce_from_special_method
        s = x._magma_init_(self)
      File "/home/jaap/downloads/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/ell_generic.py", line 316, in _magma_init_
        kmn = magma(self.base_ring())._ref()
      File "/home/jaap/downloads/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/interfaces/magma.py", line 554, in __call__
        A = Expect.__call__(self, x)
      File "/home/jaap/downloads/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 967, in __call__
        return self._coerce_from_special_method(x)
      File "/home/jaap/downloads/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/interfaces/magma.py", line 592, in _coerce_from_special_method
        a = self(s)
      File "/home/jaap/downloads/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/interfaces/magma.py", line 554, in __call__
        A = Expect.__call__(self, x)
      File "/home/jaap/downloads/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 965, in __call__
        return cls(self, x, name=name)
      File "/home/jaap/downloads/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 1335, in __init__
        raise TypeError, x
    TypeError: Unable to start magma because the command 'magma -n' failed.

**********************************************************************
File "/home/jaap/work/downloads/sage-3.2.2.alpha0/devel/sage/sage/schemes/elliptic_curves/ell_generic.py", line 196, in __main__.example_8
Failed example:
    magma(EllipticCurve([x,Integer(1)+x]))###line 313:_sage_    >>> magma(EllipticCurve([x,1+x]))
Exception raised:
    Traceback (most recent call last):
      File "/home/jaap/downloads/sage-3.2.1.alpha2/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/jaap/downloads/sage-3.2.1.alpha2/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/jaap/downloads/sage-3.2.1.alpha2/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_8[7]>", line 1, in <module>
        magma(EllipticCurve([x,Integer(1)+x]))###line 313:_sage_    >>> magma(EllipticCurve([x,1+x]))
      File "/home/jaap/downloads/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/interfaces/magma.py", line 554, in __call__
        A = Expect.__call__(self, x)
      File "/home/jaap/downloads/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 967, in __call__
        return self._coerce_from_special_method(x)
      File "/home/jaap/downloads/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/interfaces/magma.py", line 591, in _coerce_from_special_method
        s = x._magma_init_(self)
      File "/home/jaap/downloads/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/ell_generic.py", line 316, in _magma_init_
        kmn = magma(self.base_ring())._ref()
      File "/home/jaap/downloads/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/interfaces/magma.py", line 554, in __call__
        A = Expect.__call__(self, x)
      File "/home/jaap/downloads/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 967, in __call__
        return self._coerce_from_special_method(x)
      File "/home/jaap/downloads/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/interfaces/magma.py", line 591, in _coerce_from_special_method
        s = x._magma_init_(self)
      File "/home/jaap/downloads/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/rings/fraction_field.py", line 286, in _magma_init_
        s = 'FieldOfFractions(%s)'%self.ring()._magma_init_(magma)
      File "/home/jaap/downloads/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/rings/polynomial/polynomial_ring.py", line 387, in _magma_init_
        B = magma(self.base_ring())
      File "/home/jaap/downloads/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/interfaces/magma.py", line 554, in __call__
        A = Expect.__call__(self, x)
      File "/home/jaap/downloads/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 967, in __call__
        return self._coerce_from_special_method(x)
      File "/home/jaap/downloads/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/interfaces/magma.py", line 592, in _coerce_from_special_method
        a = self(s)
      File "/home/jaap/downloads/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/interfaces/magma.py", line 554, in __call__
        A = Expect.__call__(self, x)
      File "/home/jaap/downloads/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 965, in __call__
        return cls(self, x, name=name)
      File "/home/jaap/downloads/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 1335, in __init__
        raise TypeError, x
    TypeError: Unable to start magma because the command 'magma -n' failed.

**********************************************************************
1 items had failures:
   3 of   8 in __main__.example_8
***Test Failed*** 3 failures.

**********************************************************************
File "/home/jaap/work/downloads/sage-3.2.2.alpha0/devel/sage/sage/schemes/elliptic_curves/ell_generic.py", line 191, in __main__.example_8
Failed example:
    magma(E)###line 308:_sage_    >>> magma(E)
Exception raised:
    Traceback (most recent call last):
      File "/home/jaap/downloads/sage-3.2.1.alpha2/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/jaap/downloads/sage-3.2.1.alpha2/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/jaap/downloads/sage-3.2.1.alpha2/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_8[4]>", line 1, in <module>
        magma(E)###line 308:_sage_    >>> magma(E)
      File "/home/jaap/downloads/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/interfaces/magma.py", line 554, in __call__
        A = Expect.__call__(self, x)
      File "/home/jaap/downloads/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 967, in __call__
        return self._coerce_from_special_method(x)
      File "/home/jaap/downloads/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/interfaces/magma.py", line 591, in _coerce_from_special_method
        s = x._magma_init_(self)
      File "/home/jaap/downloads/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/ell_generic.py", line 316, in _magma_init_
        kmn = magma(self.base_ring())._ref()
      File "/home/jaap/downloads/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/interfaces/magma.py", line 554, in __call__
        A = Expect.__call__(self, x)
      File "/home/jaap/downloads/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 967, in __call__
        return self._coerce_from_special_method(x)
      File "/home/jaap/downloads/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/interfaces/magma.py", line 591, in _coerce_from_special_method
        s = x._magma_init_(self)
      File "ring.pyx", line 1566, in sage.rings.ring.FiniteField._magma_init_ (sage/rings/ring.c:8004)
      File "polynomial_element.pyx", line 2956, in sage.rings.polynomial.polynomial_element.Polynomial._magma_init_ (sage/rings/polynomial/polynomial_element.c:22024)
      File "/home/jaap/downloads/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/interfaces/magma.py", line 554, in __call__
        A = Expect.__call__(self, x)
      File "/home/jaap/downloads/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 967, in __call__
        return self._coerce_from_special_method(x)
      File "/home/jaap/downloads/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/interfaces/magma.py", line 591, in _coerce_from_special_method
        s = x._magma_init_(self)
      File "/home/jaap/downloads/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/rings/polynomial/polynomial_ring.py", line 387, in _magma_init_
        B = magma(self.base_ring())
      File "/home/jaap/downloads/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/interfaces/magma.py", line 554, in __call__
        A = Expect.__call__(self, x)
      File "/home/jaap/downloads/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 967, in __call__
        return self._coerce_from_special_method(x)
      File "/home/jaap/downloads/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/interfaces/magma.py", line 592, in _coerce_from_special_method
        a = self(s)
      File "/home/jaap/downloads/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/interfaces/magma.py", line 554, in __call__
        A = Expect.__call__(self, x)
      File "/home/jaap/downloads/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 965, in __call__
        return cls(self, x, name=name)
      File "/home/jaap/downloads/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 1335, in __init__
        raise TypeError, x
    TypeError: Unable to start magma because the command 'magma -n' failed.

**********************************************************************
File "/home/jaap/work/downloads/sage-3.2.2.alpha0/devel/sage/sage/schemes/elliptic_curves/ell_generic.py", line 193, in __main__.example_8
Failed example:
    magma(EllipticCurve([Integer(1)/Integer(2),Integer(2)/Integer(3),-Integer(4)/Integer(5),Integer(6)/Integer(7),Integer(8)/Integer(9)]))###line 310:_sage_    >>> magma(EllipticCurve([1/2,2/3,-4/5,6/7,8/9]))
Exception raised:
    Traceback (most recent call last):
      File "/home/jaap/downloads/sage-3.2.1.alpha2/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/jaap/downloads/sage-3.2.1.alpha2/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/jaap/downloads/sage-3.2.1.alpha2/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_8[5]>", line 1, in <module>
        magma(EllipticCurve([Integer(1)/Integer(2),Integer(2)/Integer(3),-Integer(4)/Integer(5),Integer(6)/Integer(7),Integer(8)/Integer(9)]))###line 310:_sage_    >>> magma(EllipticCurve([1/2,2/3,-4/5,6/7,8/9]))
      File "/home/jaap/downloads/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/interfaces/magma.py", line 554, in __call__
        A = Expect.__call__(self, x)
      File "/home/jaap/downloads/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 967, in __call__
        return self._coerce_from_special_method(x)
      File "/home/jaap/downloads/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/interfaces/magma.py", line 591, in _coerce_from_special_method
        s = x._magma_init_(self)
      File "/home/jaap/downloads/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/ell_generic.py", line 316, in _magma_init_
        kmn = magma(self.base_ring())._ref()
      File "/home/jaap/downloads/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/interfaces/magma.py", line 554, in __call__
        A = Expect.__call__(self, x)
      File "/home/jaap/downloads/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 967, in __call__
        return self._coerce_from_special_method(x)
      File "/home/jaap/downloads/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/interfaces/magma.py", line 592, in _coerce_from_special_method
        a = self(s)
      File "/home/jaap/downloads/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/interfaces/magma.py", line 554, in __call__
        A = Expect.__call__(self, x)
      File "/home/jaap/downloads/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 965, in __call__
        return cls(self, x, name=name)
      File "/home/jaap/downloads/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 1335, in __init__
        raise TypeError, x
    TypeError: Unable to start magma because the command 'magma -n' failed.

**********************************************************************
File "/home/jaap/work/downloads/sage-3.2.2.alpha0/devel/sage/sage/schemes/elliptic_curves/ell_generic.py", line 196, in __main__.example_8
Failed example:
    magma(EllipticCurve([x,Integer(1)+x]))###line 313:_sage_    >>> magma(EllipticCurve([x,1+x]))
Exception raised:
    Traceback (most recent call last):
      File "/home/jaap/downloads/sage-3.2.1.alpha2/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/jaap/downloads/sage-3.2.1.alpha2/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/jaap/downloads/sage-3.2.1.alpha2/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_8[7]>", line 1, in <module>
        magma(EllipticCurve([x,Integer(1)+x]))###line 313:_sage_    >>> magma(EllipticCurve([x,1+x]))
      File "/home/jaap/downloads/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/interfaces/magma.py", line 554, in __call__
        A = Expect.__call__(self, x)
      File "/home/jaap/downloads/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 967, in __call__
        return self._coerce_from_special_method(x)
      File "/home/jaap/downloads/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/interfaces/magma.py", line 591, in _coerce_from_special_method
        s = x._magma_init_(self)
      File "/home/jaap/downloads/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/ell_generic.py", line 316, in _magma_init_
        kmn = magma(self.base_ring())._ref()
      File "/home/jaap/downloads/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/interfaces/magma.py", line 554, in __call__
        A = Expect.__call__(self, x)
      File "/home/jaap/downloads/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 967, in __call__
        return self._coerce_from_special_method(x)
      File "/home/jaap/downloads/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/interfaces/magma.py", line 591, in _coerce_from_special_method
        s = x._magma_init_(self)
      File "/home/jaap/downloads/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/rings/fraction_field.py", line 286, in _magma_init_
        s = 'FieldOfFractions(%s)'%self.ring()._magma_init_(magma)
      File "/home/jaap/downloads/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/rings/polynomial/polynomial_ring.py", line 387, in _magma_init_
        B = magma(self.base_ring())
      File "/home/jaap/downloads/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/interfaces/magma.py", line 554, in __call__
        A = Expect.__call__(self, x)
      File "/home/jaap/downloads/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 967, in __call__
        return self._coerce_from_special_method(x)
      File "/home/jaap/downloads/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/interfaces/magma.py", line 592, in _coerce_from_special_method
        a = self(s)
      File "/home/jaap/downloads/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/interfaces/magma.py", line 554, in __call__
        A = Expect.__call__(self, x)
      File "/home/jaap/downloads/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 965, in __call__
        return cls(self, x, name=name)
      File "/home/jaap/downloads/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 1335, in __init__
        raise TypeError, x
    TypeError: Unable to start magma because the command 'magma -n' failed.

**********************************************************************
1 items had failures:
   3 of   8 in __main__.example_8
***Test Failed*** 3 failures.

	 [37.7 s]
exit code: 1024
 


```



Jaap


---

Attachment


---

Comment by mabshoff created at 2008-12-14 08:58:42

Jaap,

can you review?


---

Comment by jsp created at 2008-12-14 16:44:39

Patch worked for me:



```
sage -t  "devel/sage/sage/schemes/elliptic_curves/ell_generic.py"
	 [106.0 s]
 
----------------------------------------------------------------------
All tests passed!

```


Jaap


---

Comment by mabshoff created at 2008-12-14 16:49:44

Resolution: fixed


---

Comment by mabshoff created at 2008-12-14 16:49:44

Merged in Sage 3.2.2.rc0
