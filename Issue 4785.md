# Issue 4785: Failure of tests in sage/schemes/elliptic_curves/ell_generic.py due to non installed magma

archive/issues_004785.json:
```json
{
    "body": "Assignee: @williamstein\n\nThis is sage-3.2.2.alpha2 on Fedora 9, 32 bits.\nThe following test failed:\n \n\n```\nsage -t  \"devel/sage/sage/schemes/elliptic_curves/ell_generic.py\"\n\n**********************************************************************\nFile \"/home/jaap/work/downloads/sage-3.2.2.alpha0/devel/sage/sage/schemes/elliptic_curves/ell_generic.py\", line 191, in __main__.example_8\nFailed example:\n    magma(E)###line 308:_sage_    >>> magma(E)\nException raised:\n    Traceback (most recent call last):\n      File \"/home/jaap/downloads/sage-3.2.1.alpha2/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/home/jaap/downloads/sage-3.2.1.alpha2/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/home/jaap/downloads/sage-3.2.1.alpha2/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_8[4]>\", line 1, in <module>\n        magma(E)###line 308:_sage_    >>> magma(E)\n      File \"/home/jaap/downloads/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/interfaces/magma.py\", line 554, in __call__\n        A = Expect.__call__(self, x)\n      File \"/home/jaap/downloads/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/interfaces/expect.py\", line 967, in __call__\n        return self._coerce_from_special_method(x)\n      File \"/home/jaap/downloads/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/interfaces/magma.py\", line 591, in _coerce_from_special_method\n        s = x._magma_init_(self)\n      File \"/home/jaap/downloads/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/ell_generic.py\", line 316, in _magma_init_\n        kmn = magma(self.base_ring())._ref()\n      File \"/home/jaap/downloads/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/interfaces/magma.py\", line 554, in __call__\n        A = Expect.__call__(self, x)\n      File \"/home/jaap/downloads/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/interfaces/expect.py\", line 967, in __call__\n        return self._coerce_from_special_method(x)\n      File \"/home/jaap/downloads/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/interfaces/magma.py\", line 591, in _coerce_from_special_method\n        s = x._magma_init_(self)\n      File \"ring.pyx\", line 1566, in sage.rings.ring.FiniteField._magma_init_ (sage/rings/ring.c:8004)\n      File \"polynomial_element.pyx\", line 2956, in sage.rings.polynomial.polynomial_element.Polynomial._magma_init_ (sage/rings/polynomial/polynomial_element.c:22024)\n      File \"/home/jaap/downloads/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/interfaces/magma.py\", line 554, in __call__\n        A = Expect.__call__(self, x)\n      File \"/home/jaap/downloads/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/interfaces/expect.py\", line 967, in __call__\n        return self._coerce_from_special_method(x)\n      File \"/home/jaap/downloads/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/interfaces/magma.py\", line 591, in _coerce_from_special_method\n        s = x._magma_init_(self)\n      File \"/home/jaap/downloads/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/rings/polynomial/polynomial_ring.py\", line 387, in _magma_init_\n        B = magma(self.base_ring())\n      File \"/home/jaap/downloads/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/interfaces/magma.py\", line 554, in __call__\n        A = Expect.__call__(self, x)\n      File \"/home/jaap/downloads/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/interfaces/expect.py\", line 967, in __call__\n        return self._coerce_from_special_method(x)\n      File \"/home/jaap/downloads/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/interfaces/magma.py\", line 592, in _coerce_from_special_method\n        a = self(s)\n      File \"/home/jaap/downloads/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/interfaces/magma.py\", line 554, in __call__\n        A = Expect.__call__(self, x)\n      File \"/home/jaap/downloads/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/interfaces/expect.py\", line 965, in __call__\n        return cls(self, x, name=name)\n      File \"/home/jaap/downloads/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/interfaces/expect.py\", line 1335, in __init__\n        raise TypeError, x\n    TypeError: Unable to start magma because the command 'magma -n' failed.\n\n**********************************************************************\nFile \"/home/jaap/work/downloads/sage-3.2.2.alpha0/devel/sage/sage/schemes/elliptic_curves/ell_generic.py\", line 193, in __main__.example_8\nFailed example:\n    magma(EllipticCurve([Integer(1)/Integer(2),Integer(2)/Integer(3),-Integer(4)/Integer(5),Integer(6)/Integer(7),Integer(8)/Integer(9)]))###line 310:_sage_    >>> magma(EllipticCurve([1/2,2/3,-4/5,6/7,8/9]))\nException raised:\n    Traceback (most recent call last):\n      File \"/home/jaap/downloads/sage-3.2.1.alpha2/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/home/jaap/downloads/sage-3.2.1.alpha2/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/home/jaap/downloads/sage-3.2.1.alpha2/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_8[5]>\", line 1, in <module>\n        magma(EllipticCurve([Integer(1)/Integer(2),Integer(2)/Integer(3),-Integer(4)/Integer(5),Integer(6)/Integer(7),Integer(8)/Integer(9)]))###line 310:_sage_    >>> magma(EllipticCurve([1/2,2/3,-4/5,6/7,8/9]))\n      File \"/home/jaap/downloads/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/interfaces/magma.py\", line 554, in __call__\n        A = Expect.__call__(self, x)\n      File \"/home/jaap/downloads/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/interfaces/expect.py\", line 967, in __call__\n        return self._coerce_from_special_method(x)\n      File \"/home/jaap/downloads/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/interfaces/magma.py\", line 591, in _coerce_from_special_method\n        s = x._magma_init_(self)\n      File \"/home/jaap/downloads/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/ell_generic.py\", line 316, in _magma_init_\n        kmn = magma(self.base_ring())._ref()\n      File \"/home/jaap/downloads/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/interfaces/magma.py\", line 554, in __call__\n        A = Expect.__call__(self, x)\n      File \"/home/jaap/downloads/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/interfaces/expect.py\", line 967, in __call__\n        return self._coerce_from_special_method(x)\n      File \"/home/jaap/downloads/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/interfaces/magma.py\", line 592, in _coerce_from_special_method\n        a = self(s)\n      File \"/home/jaap/downloads/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/interfaces/magma.py\", line 554, in __call__\n        A = Expect.__call__(self, x)\n      File \"/home/jaap/downloads/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/interfaces/expect.py\", line 965, in __call__\n        return cls(self, x, name=name)\n      File \"/home/jaap/downloads/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/interfaces/expect.py\", line 1335, in __init__\n        raise TypeError, x\n    TypeError: Unable to start magma because the command 'magma -n' failed.\n\n**********************************************************************\nFile \"/home/jaap/work/downloads/sage-3.2.2.alpha0/devel/sage/sage/schemes/elliptic_curves/ell_generic.py\", line 196, in __main__.example_8\nFailed example:\n    magma(EllipticCurve([x,Integer(1)+x]))###line 313:_sage_    >>> magma(EllipticCurve([x,1+x]))\nException raised:\n    Traceback (most recent call last):\n      File \"/home/jaap/downloads/sage-3.2.1.alpha2/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/home/jaap/downloads/sage-3.2.1.alpha2/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/home/jaap/downloads/sage-3.2.1.alpha2/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_8[7]>\", line 1, in <module>\n        magma(EllipticCurve([x,Integer(1)+x]))###line 313:_sage_    >>> magma(EllipticCurve([x,1+x]))\n      File \"/home/jaap/downloads/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/interfaces/magma.py\", line 554, in __call__\n        A = Expect.__call__(self, x)\n      File \"/home/jaap/downloads/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/interfaces/expect.py\", line 967, in __call__\n        return self._coerce_from_special_method(x)\n      File \"/home/jaap/downloads/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/interfaces/magma.py\", line 591, in _coerce_from_special_method\n        s = x._magma_init_(self)\n      File \"/home/jaap/downloads/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/ell_generic.py\", line 316, in _magma_init_\n        kmn = magma(self.base_ring())._ref()\n      File \"/home/jaap/downloads/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/interfaces/magma.py\", line 554, in __call__\n        A = Expect.__call__(self, x)\n      File \"/home/jaap/downloads/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/interfaces/expect.py\", line 967, in __call__\n        return self._coerce_from_special_method(x)\n      File \"/home/jaap/downloads/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/interfaces/magma.py\", line 591, in _coerce_from_special_method\n        s = x._magma_init_(self)\n      File \"/home/jaap/downloads/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/rings/fraction_field.py\", line 286, in _magma_init_\n        s = 'FieldOfFractions(%s)'%self.ring()._magma_init_(magma)\n      File \"/home/jaap/downloads/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/rings/polynomial/polynomial_ring.py\", line 387, in _magma_init_\n        B = magma(self.base_ring())\n      File \"/home/jaap/downloads/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/interfaces/magma.py\", line 554, in __call__\n        A = Expect.__call__(self, x)\n      File \"/home/jaap/downloads/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/interfaces/expect.py\", line 967, in __call__\n        return self._coerce_from_special_method(x)\n      File \"/home/jaap/downloads/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/interfaces/magma.py\", line 592, in _coerce_from_special_method\n        a = self(s)\n      File \"/home/jaap/downloads/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/interfaces/magma.py\", line 554, in __call__\n        A = Expect.__call__(self, x)\n      File \"/home/jaap/downloads/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/interfaces/expect.py\", line 965, in __call__\n        return cls(self, x, name=name)\n      File \"/home/jaap/downloads/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/interfaces/expect.py\", line 1335, in __init__\n        raise TypeError, x\n    TypeError: Unable to start magma because the command 'magma -n' failed.\n\n**********************************************************************\n1 items had failures:\n   3 of   8 in __main__.example_8\n***Test Failed*** 3 failures.\n\n**********************************************************************\nFile \"/home/jaap/work/downloads/sage-3.2.2.alpha0/devel/sage/sage/schemes/elliptic_curves/ell_generic.py\", line 191, in __main__.example_8\nFailed example:\n    magma(E)###line 308:_sage_    >>> magma(E)\nException raised:\n    Traceback (most recent call last):\n      File \"/home/jaap/downloads/sage-3.2.1.alpha2/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/home/jaap/downloads/sage-3.2.1.alpha2/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/home/jaap/downloads/sage-3.2.1.alpha2/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_8[4]>\", line 1, in <module>\n        magma(E)###line 308:_sage_    >>> magma(E)\n      File \"/home/jaap/downloads/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/interfaces/magma.py\", line 554, in __call__\n        A = Expect.__call__(self, x)\n      File \"/home/jaap/downloads/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/interfaces/expect.py\", line 967, in __call__\n        return self._coerce_from_special_method(x)\n      File \"/home/jaap/downloads/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/interfaces/magma.py\", line 591, in _coerce_from_special_method\n        s = x._magma_init_(self)\n      File \"/home/jaap/downloads/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/ell_generic.py\", line 316, in _magma_init_\n        kmn = magma(self.base_ring())._ref()\n      File \"/home/jaap/downloads/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/interfaces/magma.py\", line 554, in __call__\n        A = Expect.__call__(self, x)\n      File \"/home/jaap/downloads/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/interfaces/expect.py\", line 967, in __call__\n        return self._coerce_from_special_method(x)\n      File \"/home/jaap/downloads/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/interfaces/magma.py\", line 591, in _coerce_from_special_method\n        s = x._magma_init_(self)\n      File \"ring.pyx\", line 1566, in sage.rings.ring.FiniteField._magma_init_ (sage/rings/ring.c:8004)\n      File \"polynomial_element.pyx\", line 2956, in sage.rings.polynomial.polynomial_element.Polynomial._magma_init_ (sage/rings/polynomial/polynomial_element.c:22024)\n      File \"/home/jaap/downloads/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/interfaces/magma.py\", line 554, in __call__\n        A = Expect.__call__(self, x)\n      File \"/home/jaap/downloads/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/interfaces/expect.py\", line 967, in __call__\n        return self._coerce_from_special_method(x)\n      File \"/home/jaap/downloads/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/interfaces/magma.py\", line 591, in _coerce_from_special_method\n        s = x._magma_init_(self)\n      File \"/home/jaap/downloads/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/rings/polynomial/polynomial_ring.py\", line 387, in _magma_init_\n        B = magma(self.base_ring())\n      File \"/home/jaap/downloads/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/interfaces/magma.py\", line 554, in __call__\n        A = Expect.__call__(self, x)\n      File \"/home/jaap/downloads/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/interfaces/expect.py\", line 967, in __call__\n        return self._coerce_from_special_method(x)\n      File \"/home/jaap/downloads/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/interfaces/magma.py\", line 592, in _coerce_from_special_method\n        a = self(s)\n      File \"/home/jaap/downloads/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/interfaces/magma.py\", line 554, in __call__\n        A = Expect.__call__(self, x)\n      File \"/home/jaap/downloads/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/interfaces/expect.py\", line 965, in __call__\n        return cls(self, x, name=name)\n      File \"/home/jaap/downloads/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/interfaces/expect.py\", line 1335, in __init__\n        raise TypeError, x\n    TypeError: Unable to start magma because the command 'magma -n' failed.\n\n**********************************************************************\nFile \"/home/jaap/work/downloads/sage-3.2.2.alpha0/devel/sage/sage/schemes/elliptic_curves/ell_generic.py\", line 193, in __main__.example_8\nFailed example:\n    magma(EllipticCurve([Integer(1)/Integer(2),Integer(2)/Integer(3),-Integer(4)/Integer(5),Integer(6)/Integer(7),Integer(8)/Integer(9)]))###line 310:_sage_    >>> magma(EllipticCurve([1/2,2/3,-4/5,6/7,8/9]))\nException raised:\n    Traceback (most recent call last):\n      File \"/home/jaap/downloads/sage-3.2.1.alpha2/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/home/jaap/downloads/sage-3.2.1.alpha2/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/home/jaap/downloads/sage-3.2.1.alpha2/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_8[5]>\", line 1, in <module>\n        magma(EllipticCurve([Integer(1)/Integer(2),Integer(2)/Integer(3),-Integer(4)/Integer(5),Integer(6)/Integer(7),Integer(8)/Integer(9)]))###line 310:_sage_    >>> magma(EllipticCurve([1/2,2/3,-4/5,6/7,8/9]))\n      File \"/home/jaap/downloads/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/interfaces/magma.py\", line 554, in __call__\n        A = Expect.__call__(self, x)\n      File \"/home/jaap/downloads/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/interfaces/expect.py\", line 967, in __call__\n        return self._coerce_from_special_method(x)\n      File \"/home/jaap/downloads/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/interfaces/magma.py\", line 591, in _coerce_from_special_method\n        s = x._magma_init_(self)\n      File \"/home/jaap/downloads/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/ell_generic.py\", line 316, in _magma_init_\n        kmn = magma(self.base_ring())._ref()\n      File \"/home/jaap/downloads/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/interfaces/magma.py\", line 554, in __call__\n        A = Expect.__call__(self, x)\n      File \"/home/jaap/downloads/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/interfaces/expect.py\", line 967, in __call__\n        return self._coerce_from_special_method(x)\n      File \"/home/jaap/downloads/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/interfaces/magma.py\", line 592, in _coerce_from_special_method\n        a = self(s)\n      File \"/home/jaap/downloads/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/interfaces/magma.py\", line 554, in __call__\n        A = Expect.__call__(self, x)\n      File \"/home/jaap/downloads/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/interfaces/expect.py\", line 965, in __call__\n        return cls(self, x, name=name)\n      File \"/home/jaap/downloads/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/interfaces/expect.py\", line 1335, in __init__\n        raise TypeError, x\n    TypeError: Unable to start magma because the command 'magma -n' failed.\n\n**********************************************************************\nFile \"/home/jaap/work/downloads/sage-3.2.2.alpha0/devel/sage/sage/schemes/elliptic_curves/ell_generic.py\", line 196, in __main__.example_8\nFailed example:\n    magma(EllipticCurve([x,Integer(1)+x]))###line 313:_sage_    >>> magma(EllipticCurve([x,1+x]))\nException raised:\n    Traceback (most recent call last):\n      File \"/home/jaap/downloads/sage-3.2.1.alpha2/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/home/jaap/downloads/sage-3.2.1.alpha2/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/home/jaap/downloads/sage-3.2.1.alpha2/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_8[7]>\", line 1, in <module>\n        magma(EllipticCurve([x,Integer(1)+x]))###line 313:_sage_    >>> magma(EllipticCurve([x,1+x]))\n      File \"/home/jaap/downloads/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/interfaces/magma.py\", line 554, in __call__\n        A = Expect.__call__(self, x)\n      File \"/home/jaap/downloads/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/interfaces/expect.py\", line 967, in __call__\n        return self._coerce_from_special_method(x)\n      File \"/home/jaap/downloads/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/interfaces/magma.py\", line 591, in _coerce_from_special_method\n        s = x._magma_init_(self)\n      File \"/home/jaap/downloads/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/ell_generic.py\", line 316, in _magma_init_\n        kmn = magma(self.base_ring())._ref()\n      File \"/home/jaap/downloads/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/interfaces/magma.py\", line 554, in __call__\n        A = Expect.__call__(self, x)\n      File \"/home/jaap/downloads/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/interfaces/expect.py\", line 967, in __call__\n        return self._coerce_from_special_method(x)\n      File \"/home/jaap/downloads/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/interfaces/magma.py\", line 591, in _coerce_from_special_method\n        s = x._magma_init_(self)\n      File \"/home/jaap/downloads/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/rings/fraction_field.py\", line 286, in _magma_init_\n        s = 'FieldOfFractions(%s)'%self.ring()._magma_init_(magma)\n      File \"/home/jaap/downloads/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/rings/polynomial/polynomial_ring.py\", line 387, in _magma_init_\n        B = magma(self.base_ring())\n      File \"/home/jaap/downloads/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/interfaces/magma.py\", line 554, in __call__\n        A = Expect.__call__(self, x)\n      File \"/home/jaap/downloads/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/interfaces/expect.py\", line 967, in __call__\n        return self._coerce_from_special_method(x)\n      File \"/home/jaap/downloads/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/interfaces/magma.py\", line 592, in _coerce_from_special_method\n        a = self(s)\n      File \"/home/jaap/downloads/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/interfaces/magma.py\", line 554, in __call__\n        A = Expect.__call__(self, x)\n      File \"/home/jaap/downloads/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/interfaces/expect.py\", line 965, in __call__\n        return cls(self, x, name=name)\n      File \"/home/jaap/downloads/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/interfaces/expect.py\", line 1335, in __init__\n        raise TypeError, x\n    TypeError: Unable to start magma because the command 'magma -n' failed.\n\n**********************************************************************\n1 items had failures:\n   3 of   8 in __main__.example_8\n***Test Failed*** 3 failures.\n\n\t [37.7 s]\nexit code: 1024\n \n\n\n```\n\n\n\nJaap\n\nIssue created by migration from https://trac.sagemath.org/ticket/4785\n\n",
    "created_at": "2008-12-13T21:16:24Z",
    "labels": [
        "component: number theory",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2.2",
    "title": "Failure of tests in sage/schemes/elliptic_curves/ell_generic.py due to non installed magma",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4785",
    "user": "https://github.com/jaapspies"
}
```
Assignee: @williamstein

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

Issue created by migration from https://trac.sagemath.org/ticket/4785





---

archive/issue_comments_036202.json:
```json
{
    "body": "Attachment [trac_4785.patch](tarball://root/attachments/some-uuid/ticket4785/trac_4785.patch) by mabshoff created at 2008-12-14 08:58:12",
    "created_at": "2008-12-14T08:58:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4785",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4785#issuecomment-36202",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [trac_4785.patch](tarball://root/attachments/some-uuid/ticket4785/trac_4785.patch) by mabshoff created at 2008-12-14 08:58:12



---

archive/issue_comments_036203.json:
```json
{
    "body": "Jaap,\n\ncan you review?",
    "created_at": "2008-12-14T08:58:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4785",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4785#issuecomment-36203",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Jaap,

can you review?



---

archive/issue_comments_036204.json:
```json
{
    "body": "Patch worked for me:\n\n\n\n```\nsage -t  \"devel/sage/sage/schemes/elliptic_curves/ell_generic.py\"\n\t [106.0 s]\n \n----------------------------------------------------------------------\nAll tests passed!\n\n```\n\n\nJaap",
    "created_at": "2008-12-14T16:44:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4785",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4785#issuecomment-36204",
    "user": "https://github.com/jaapspies"
}
```

Patch worked for me:



```
sage -t  "devel/sage/sage/schemes/elliptic_curves/ell_generic.py"
	 [106.0 s]
 
----------------------------------------------------------------------
All tests passed!

```


Jaap



---

archive/issue_events_005029.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-12-14T16:49:44Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4785",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4785#event-5029"
}
```



---

archive/issue_comments_036205.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-12-14T16:49:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4785",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4785#issuecomment-36205",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_036206.json:
```json
{
    "body": "Merged in Sage 3.2.2.rc0",
    "created_at": "2008-12-14T16:49:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4785",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4785#issuecomment-36206",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.2.2.rc0
