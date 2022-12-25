# Issue 6207: roots of polynomial have incorrect parent when ring=R is specified

archive/issues_006207.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  cwitty mhansen\n\nKeywords: roots polynomial parent ring inexact\n\nThe attached patch verifies that the roots of a polynomial actually have parent the desired ring.  This bit me in the ass for number fields, but the setup required bizarre embeddings and I don't have an example at hand.  This is not true in a few cases over inexact fields:\n\n\n```\n-*- mode: sage-test; default-directory: \"~/sage/devel/sage/sage/rings/polynomial/\" -*-\nsage-test started at Wed Jun  3 21:29:49\n\n/home/ncalexan/bin/sage -b >/dev/null && /home/ncalexan/bin/sage -tp 4 /home/ncalexan/sage/devel/sage/sage/rings/polynomial/polynomial_element.pyx /home/ncalexan/sage/devel/sage/sage/rings/number_field/number_field.py\n\nreal\t0m3.957s\nuser\t0m0.810s\nsys\t0m0.560s\nGlobal iterations: 1\nFile iterations: 1\nNo cached timings exist; will create upon successful finish.\nDoctesting 2 files doing 4 jobs in parallel\nsage -t  olynomial_element.pyx\n**********************************************************************\nFile \"/home/ncalexan/sage-3.4.2-sage.math-only-x86_64-Linux/devel/sage-main/sage/rings/polynomial/polynomial_element.pyx\", line 3893:\n    sage: f.roots(ring=RIF)\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/mabshoff/sage-4.0.alpha0/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/scratch/mabshoff/sage-4.0.alpha0/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/scratch/mabshoff/sage-4.0.alpha0/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_79[78]>\", line 1, in <module>\n        f.roots(ring=RIF)###line 3893:\n    sage: f.roots(ring=RIF)\n      File \"polynomial_element.pyx\", line 3662, in sage.rings.polynomial.polynomial_element.Polynomial.roots (sage/rings/polynomial/polynomial_element.c:27304)\n        assert rt.parent() is ring\n    AssertionError\n**********************************************************************\nFile \"/home/ncalexan/sage-3.4.2-sage.math-only-x86_64-Linux/devel/sage-main/sage/rings/polynomial/polynomial_element.pyx\", line 3895:\n    sage: f.roots(ring=RIF, multiplicities=False)\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/mabshoff/sage-4.0.alpha0/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/scratch/mabshoff/sage-4.0.alpha0/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/scratch/mabshoff/sage-4.0.alpha0/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_79[79]>\", line 1, in <module>\n        f.roots(ring=RIF, multiplicities=False)###line 3895:\n    sage: f.roots(ring=RIF, multiplicities=False)\n      File \"polynomial_element.pyx\", line 3666, in sage.rings.polynomial.polynomial_element.Polynomial.roots (sage/rings/polynomial/polynomial_element.c:27446)\n        assert rt.parent() is ring\n    AssertionError\n**********************************************************************\nFile \"/home/ncalexan/sage-3.4.2-sage.math-only-x86_64-Linux/devel/sage-main/sage/rings/polynomial/polynomial_element.pyx\", line 3897:\n    sage: f.roots(ring=RealIntervalField(150))\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/mabshoff/sage-4.0.alpha0/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/scratch/mabshoff/sage-4.0.alpha0/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/scratch/mabshoff/sage-4.0.alpha0/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_79[80]>\", line 1, in <module>\n        f.roots(ring=RealIntervalField(Integer(150)))###line 3897:\n    sage: f.roots(ring=RealIntervalField(150))\n      File \"polynomial_element.pyx\", line 3662, in sage.rings.polynomial.polynomial_element.Polynomial.roots (sage/rings/polynomial/polynomial_element.c:27304)\n        assert rt.parent() is ring\n    AssertionError\n**********************************************************************\nFile \"/home/ncalexan/sage-3.4.2-sage.math-only-x86_64-Linux/devel/sage-main/sage/rings/polynomial/polynomial_element.pyx\", line 3902:\n    sage: f.roots(ring=RIF)\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/mabshoff/sage-4.0.alpha0/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/scratch/mabshoff/sage-4.0.alpha0/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/scratch/mabshoff/sage-4.0.alpha0/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_79[83]>\", line 1, in <module>\n        f.roots(ring=RIF)###line 3902:\n    sage: f.roots(ring=RIF)\n      File \"polynomial_element.pyx\", line 3662, in sage.rings.polynomial.polynomial_element.Polynomial.roots (sage/rings/polynomial/polynomial_element.c:27304)\n        assert rt.parent() is ring\n    AssertionError\n**********************************************************************\nFile \"/home/ncalexan/sage-3.4.2-sage.math-only-x86_64-Linux/devel/sage-main/sage/rings/polynomial/polynomial_element.pyx\", line 3904:\n    sage: f.roots(ring=RIF, multiplicities=False)\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/mabshoff/sage-4.0.alpha0/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/scratch/mabshoff/sage-4.0.alpha0/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/scratch/mabshoff/sage-4.0.alpha0/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_79[84]>\", line 1, in <module>\n        f.roots(ring=RIF, multiplicities=False)###line 3904:\n    sage: f.roots(ring=RIF, multiplicities=False)\n      File \"polynomial_element.pyx\", line 3666, in sage.rings.polynomial.polynomial_element.Polynomial.roots (sage/rings/polynomial/polynomial_element.c:27446)\n        assert rt.parent() is ring\n    AssertionError\n**********************************************************************\nFile \"/home/ncalexan/sage-3.4.2-sage.math-only-x86_64-Linux/devel/sage-main/sage/rings/polynomial/polynomial_element.pyx\", line 3985:\n    sage: f.roots(ring=RealIntervalField(150))\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/mabshoff/sage-4.0.alpha0/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/scratch/mabshoff/sage-4.0.alpha0/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/scratch/mabshoff/sage-4.0.alpha0/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_79[112]>\", line 1, in <module>\n        f.roots(ring=RealIntervalField(Integer(150)))###line 3985:\n    sage: f.roots(ring=RealIntervalField(150))\n      File \"polynomial_element.pyx\", line 3662, in sage.rings.polynomial.polynomial_element.Polynomial.roots (sage/rings/polynomial/polynomial_element.c:27304)\n        assert rt.parent() is ring\n    AssertionError\n**********************************************************************\nFile \"/home/ncalexan/sage-3.4.2-sage.math-only-x86_64-Linux/devel/sage-main/sage/rings/polynomial/polynomial_element.pyx\", line 4298:\n    sage: (x^2 - x - 1).real_roots()\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/mabshoff/sage-4.0.alpha0/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/scratch/mabshoff/sage-4.0.alpha0/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/scratch/mabshoff/sage-4.0.alpha0/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_80[3]>\", line 1, in <module>\n        (x**Integer(2) - x - Integer(1)).real_roots()###line 4298:\n    sage: (x^2 - x - 1).real_roots()\n      File \"polynomial_element.pyx\", line 4314, in sage.rings.polynomial.polynomial_element.Polynomial.real_roots (sage/rings/polynomial/polynomial_element.c:30800)\n        return self.roots(ring=RR, multiplicities=False)\n      File \"polynomial_element.pyx\", line 3666, in sage.rings.polynomial.polynomial_element.Polynomial.roots (sage/rings/polynomial/polynomial_element.c:27446)\n        assert rt.parent() is ring\n    AssertionError\n**********************************************************************\n2 items had failures:\n   6 of 132 in __main__.example_79\n   1 of   8 in __main__.example_80\n***Test Failed*** 7 failures.\nFor whitespace errors, see the file /home/ncalexan/sage-3.4.2-sage.math-only-x86_64-Linux/tmp/.doctest_polynomial_element.py\n\t [7.9 s]\nsage -t  /number_field.py\n**********************************************************************\nFile \"/home/ncalexan/sage-3.4.2-sage.math-only-x86_64-Linux/devel/sage-main/sage/rings/number_field/number_field.py\", line 5236:\n    sage: F.Minkowski_embedding()\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/mabshoff/sage-4.0.alpha0/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/scratch/mabshoff/sage-4.0.alpha0/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/scratch/mabshoff/sage-4.0.alpha0/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_121[3]>\", line 1, in <module>\n        F.Minkowski_embedding()###line 5236:\n    sage: F.Minkowski_embedding()\n      File \"/home/ncalexan/sage/local/lib/python2.5/site-packages/sage/rings/number_field/number_field.py\", line 5255, in Minkowski_embedding\n        places = self.places(prec=prec)\n      File \"/home/ncalexan/sage/local/lib/python2.5/site-packages/sage/rings/number_field/number_field.py\", line 5365, in places\n        real_intervals = [ x[0] for x in self.defining_polynomial().roots(R) ]\n      File \"polynomial_element.pyx\", line 3662, in sage.rings.polynomial.polynomial_element.Polynomial.roots (sage/rings/polynomial/polynomial_element.c:27304)\n    AssertionError\n**********************************************************************\nFile \"/home/ncalexan/sage-3.4.2-sage.math-only-x86_64-Linux/devel/sage-main/sage/rings/number_field/number_field.py\", line 5240:\n    sage: F.Minkowski_embedding([1, alpha+2, alpha^2-alpha])\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/mabshoff/sage-4.0.alpha0/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/scratch/mabshoff/sage-4.0.alpha0/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/scratch/mabshoff/sage-4.0.alpha0/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_121[4]>\", line 1, in <module>\n        F.Minkowski_embedding([Integer(1), alpha+Integer(2), alpha**Integer(2)-alpha])###line 5240:\n    sage: F.Minkowski_embedding([1, alpha+2, alpha^2-alpha])\n      File \"/home/ncalexan/sage/local/lib/python2.5/site-packages/sage/rings/number_field/number_field.py\", line 5255, in Minkowski_embedding\n        places = self.places(prec=prec)\n      File \"/home/ncalexan/sage/local/lib/python2.5/site-packages/sage/rings/number_field/number_field.py\", line 5365, in places\n        real_intervals = [ x[0] for x in self.defining_polynomial().roots(R) ]\n      File \"polynomial_element.pyx\", line 3662, in sage.rings.polynomial.polynomial_element.Polynomial.roots (sage/rings/polynomial/polynomial_element.c:27304)\n    AssertionError\n**********************************************************************\nFile \"/home/ncalexan/sage-3.4.2-sage.math-only-x86_64-Linux/devel/sage-main/sage/rings/number_field/number_field.py\", line 5244:\n    sage: F.Minkowski_embedding() * (alpha + 2).vector().transpose()\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/mabshoff/sage-4.0.alpha0/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/scratch/mabshoff/sage-4.0.alpha0/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/scratch/mabshoff/sage-4.0.alpha0/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_121[5]>\", line 1, in <module>\n        F.Minkowski_embedding() * (alpha + Integer(2)).vector().transpose()###line 5244:\n    sage: F.Minkowski_embedding() * (alpha + 2).vector().transpose()\n      File \"/home/ncalexan/sage/local/lib/python2.5/site-packages/sage/rings/number_field/number_field.py\", line 5255, in Minkowski_embedding\n        places = self.places(prec=prec)\n      File \"/home/ncalexan/sage/local/lib/python2.5/site-packages/sage/rings/number_field/number_field.py\", line 5365, in places\n        real_intervals = [ x[0] for x in self.defining_polynomial().roots(R) ]\n      File \"polynomial_element.pyx\", line 3662, in sage.rings.polynomial.polynomial_element.Polynomial.roots (sage/rings/polynomial/polynomial_element.c:27304)\n    AssertionError\n**********************************************************************\nFile \"/home/ncalexan/sage-3.4.2-sage.math-only-x86_64-Linux/devel/sage-main/sage/rings/number_field/number_field.py\", line 5299:\n    sage: F.<alpha> = NumberField(x^3-100*x+1) ; F.places()\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/mabshoff/sage-4.0.alpha0/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/scratch/mabshoff/sage-4.0.alpha0/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/scratch/mabshoff/sage-4.0.alpha0/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_122[2]>\", line 1, in <module>\n        F = NumberField(x**Integer(3)-Integer(100)*x+Integer(1), names=('alpha',)); (alpha,) = F._first_ngens(1); F.places()###line 5299:\n    sage: F.<alpha> = NumberField(x^3-100*x+1) ; F.places()\n      File \"/home/ncalexan/sage/local/lib/python2.5/site-packages/sage/rings/number_field/number_field.py\", line 5365, in places\n        real_intervals = [ x[0] for x in self.defining_polynomial().roots(R) ]\n      File \"polynomial_element.pyx\", line 3662, in sage.rings.polynomial.polynomial_element.Polynomial.roots (sage/rings/polynomial/polynomial_element.c:27304)\n    AssertionError\n**********************************************************************\nFile \"/home/ncalexan/sage-3.4.2-sage.math-only-x86_64-Linux/devel/sage-main/sage/rings/number_field/number_field.py\", line 5315:\n    sage: F.<alpha> = NumberField(x^3+7) ; F.places()\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/mabshoff/sage-4.0.alpha0/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/scratch/mabshoff/sage-4.0.alpha0/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/scratch/mabshoff/sage-4.0.alpha0/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_122[3]>\", line 1, in <module>\n        F = NumberField(x**Integer(3)+Integer(7), names=('alpha',)); (alpha,) = F._first_ngens(1); F.places()###line 5315:\n    sage: F.<alpha> = NumberField(x^3+7) ; F.places()\n      File \"/home/ncalexan/sage/local/lib/python2.5/site-packages/sage/rings/number_field/number_field.py\", line 5365, in places\n        real_intervals = [ x[0] for x in self.defining_polynomial().roots(R) ]\n      File \"polynomial_element.pyx\", line 3662, in sage.rings.polynomial.polynomial_element.Polynomial.roots (sage/rings/polynomial/polynomial_element.c:27304)\n    AssertionError\n**********************************************************************\nFile \"/home/ncalexan/sage-3.4.2-sage.math-only-x86_64-Linux/devel/sage-main/sage/rings/number_field/number_field.py\", line 5336:\n    sage: F.places(prec=10)\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/mabshoff/sage-4.0.alpha0/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/scratch/mabshoff/sage-4.0.alpha0/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/scratch/mabshoff/sage-4.0.alpha0/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_122[5]>\", line 1, in <module>\n        F.places(prec=Integer(10))###line 5336:\n    sage: F.places(prec=10)\n      File \"/home/ncalexan/sage/local/lib/python2.5/site-packages/sage/rings/number_field/number_field.py\", line 5365, in places\n        real_intervals = [ x[0] for x in self.defining_polynomial().roots(R) ]\n      File \"polynomial_element.pyx\", line 3662, in sage.rings.polynomial.polynomial_element.Polynomial.roots (sage/rings/polynomial/polynomial_element.c:27304)\n    AssertionError\n**********************************************************************\nFile \"/home/ncalexan/sage-3.4.2-sage.math-only-x86_64-Linux/devel/sage-main/sage/rings/number_field/number_field.py\", line 5386:\n    sage: F.<alpha> = NumberField(x^4-7) ; F.real_places()\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/mabshoff/sage-4.0.alpha0/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/scratch/mabshoff/sage-4.0.alpha0/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/scratch/mabshoff/sage-4.0.alpha0/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_123[2]>\", line 1, in <module>\n        F = NumberField(x**Integer(4)-Integer(7), names=('alpha',)); (alpha,) = F._first_ngens(1); F.real_places()###line 5386:\n    sage: F.<alpha> = NumberField(x^4-7) ; F.real_places()\n      File \"/home/ncalexan/sage/local/lib/python2.5/site-packages/sage/rings/number_field/number_field.py\", line 5396, in real_places\n        return self.places(prec=prec)[0:self.signature()[0]]\n      File \"/home/ncalexan/sage/local/lib/python2.5/site-packages/sage/rings/number_field/number_field.py\", line 5365, in places\n        real_intervals = [ x[0] for x in self.defining_polynomial().roots(R) ]\n      File \"polynomial_element.pyx\", line 3662, in sage.rings.polynomial.polynomial_element.Polynomial.roots (sage/rings/polynomial/polynomial_element.c:27304)\n    AssertionError\n**********************************************************************\nFile \"/home/ncalexan/sage-3.4.2-sage.math-only-x86_64-Linux/devel/sage-main/sage/rings/number_field/number_field.py\", line 3322:\n    sage: F.reduced_basis(prec=64)\nExpected:\n    Traceback (most recent call last):                 \n    ...                                                \n    PariError: not a definite matrix in lllgram (42)   \nGot:\n    Traceback (most recent call last):\n      File \"/scratch/mabshoff/sage-4.0.alpha0/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/scratch/mabshoff/sage-4.0.alpha0/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/scratch/mabshoff/sage-4.0.alpha0/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_74[7]>\", line 1, in <module>\n        F.reduced_basis(prec=Integer(64))###line 3322:\n    sage: F.reduced_basis(prec=64)\n      File \"/home/ncalexan/sage/local/lib/python2.5/site-packages/sage/rings/number_field/number_field.py\", line 3357, in reduced_basis\n        M = self.Minkowski_embedding(self.integral_basis(), prec=prec)\n      File \"/home/ncalexan/sage/local/lib/python2.5/site-packages/sage/rings/number_field/number_field.py\", line 5262, in Minkowski_embedding\n        sqrt2 = f.roots(R)[1][0]\n      File \"polynomial_element.pyx\", line 3662, in sage.rings.polynomial.polynomial_element.Polynomial.roots (sage/rings/polynomial/polynomial_element.c:27304)\n    AssertionError\n**********************************************************************\nFile \"/home/ncalexan/sage-3.4.2-sage.math-only-x86_64-Linux/devel/sage-main/sage/rings/number_field/number_field.py\", line 3327:\n    sage: F.reduced_basis(prec=96)\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/mabshoff/sage-4.0.alpha0/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/scratch/mabshoff/sage-4.0.alpha0/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/scratch/mabshoff/sage-4.0.alpha0/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_74[8]>\", line 1, in <module>\n        F.reduced_basis(prec=Integer(96))###line 3327:\n    sage: F.reduced_basis(prec=96)\n      File \"/home/ncalexan/sage/local/lib/python2.5/site-packages/sage/rings/number_field/number_field.py\", line 3357, in reduced_basis\n        M = self.Minkowski_embedding(self.integral_basis(), prec=prec)\n      File \"/home/ncalexan/sage/local/lib/python2.5/site-packages/sage/rings/number_field/number_field.py\", line 5262, in Minkowski_embedding\n        sqrt2 = f.roots(R)[1][0]\n      File \"polynomial_element.pyx\", line 3662, in sage.rings.polynomial.polynomial_element.Polynomial.roots (sage/rings/polynomial/polynomial_element.c:27304)\n    AssertionError\n**********************************************************************\nFile \"/home/ncalexan/sage-3.4.2-sage.math-only-x86_64-Linux/devel/sage-main/sage/rings/number_field/number_field.py\", line 3427:\n    sage: F.reduced_gram_matrix(prec=128)\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/mabshoff/sage-4.0.alpha0/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/scratch/mabshoff/sage-4.0.alpha0/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/scratch/mabshoff/sage-4.0.alpha0/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_75[7]>\", line 1, in <module>\n        F.reduced_gram_matrix(prec=Integer(128))###line 3427:\n    sage: F.reduced_gram_matrix(prec=128)\n      File \"/home/ncalexan/sage/local/lib/python2.5/site-packages/sage/rings/number_field/number_field.py\", line 3455, in reduced_gram_matrix\n        M = self.Minkowski_embedding(prec=prec)\n      File \"/home/ncalexan/sage/local/lib/python2.5/site-packages/sage/rings/number_field/number_field.py\", line 5262, in Minkowski_embedding\n        sqrt2 = f.roots(R)[1][0]\n      File \"polynomial_element.pyx\", line 3662, in sage.rings.polynomial.polynomial_element.Polynomial.roots (sage/rings/polynomial/polynomial_element.c:27304)\n    AssertionError\n\n  ***   Warning: large Minkowski bound: certification will be VERY long.\n  ***   Warning: large Minkowski bound: certification will be VERY long.\n  ***   Warning: large Minkowski bound: certification will be VERY long.\n  ***   Warning: large Minkowski bound: certification will be VERY long.\n**********************************************************************\n5 items had failures:\n   3 of   6 in __main__.example_121\n   3 of   6 in __main__.example_122\n   1 of   3 in __main__.example_123\n   2 of   9 in __main__.example_74\n   1 of   8 in __main__.example_75\n***Test Failed*** 10 failures.\nFor whitespace errors, see the file /home/ncalexan/sage-3.4.2-sage.math-only-x86_64-Linux/tmp/.doctest_number_field.py\n\t [17.2 s]\n \n----------------------------------------------------------------------\n\nThe following tests failed:\n\n\tsage -t  olynomial_element.pyx # 7 doctests failed\n\tsage -t  /number_field.py # 10 doctests failed\n----------------------------------------------------------------------\nTotal time for all tests: 17.4 seconds\n\nsage-test finished with failing tests at Wed Jun  3 21:30:10\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6207\n\n",
    "created_at": "2009-06-04T04:34:20Z",
    "labels": [
        "component: algebra",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.2",
    "title": "roots of polynomial have incorrect parent when ring=R is specified",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6207",
    "user": "https://github.com/ncalexan"
}
```
Assignee: tbd

CC:  cwitty mhansen

Keywords: roots polynomial parent ring inexact

The attached patch verifies that the roots of a polynomial actually have parent the desired ring.  This bit me in the ass for number fields, but the setup required bizarre embeddings and I don't have an example at hand.  This is not true in a few cases over inexact fields:


```
-*- mode: sage-test; default-directory: "~/sage/devel/sage/sage/rings/polynomial/" -*-
sage-test started at Wed Jun  3 21:29:49

/home/ncalexan/bin/sage -b >/dev/null && /home/ncalexan/bin/sage -tp 4 /home/ncalexan/sage/devel/sage/sage/rings/polynomial/polynomial_element.pyx /home/ncalexan/sage/devel/sage/sage/rings/number_field/number_field.py

real	0m3.957s
user	0m0.810s
sys	0m0.560s
Global iterations: 1
File iterations: 1
No cached timings exist; will create upon successful finish.
Doctesting 2 files doing 4 jobs in parallel
sage -t  olynomial_element.pyx
**********************************************************************
File "/home/ncalexan/sage-3.4.2-sage.math-only-x86_64-Linux/devel/sage-main/sage/rings/polynomial/polynomial_element.pyx", line 3893:
    sage: f.roots(ring=RIF)
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/sage-4.0.alpha0/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/mabshoff/sage-4.0.alpha0/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/mabshoff/sage-4.0.alpha0/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_79[78]>", line 1, in <module>
        f.roots(ring=RIF)###line 3893:
    sage: f.roots(ring=RIF)
      File "polynomial_element.pyx", line 3662, in sage.rings.polynomial.polynomial_element.Polynomial.roots (sage/rings/polynomial/polynomial_element.c:27304)
        assert rt.parent() is ring
    AssertionError
**********************************************************************
File "/home/ncalexan/sage-3.4.2-sage.math-only-x86_64-Linux/devel/sage-main/sage/rings/polynomial/polynomial_element.pyx", line 3895:
    sage: f.roots(ring=RIF, multiplicities=False)
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/sage-4.0.alpha0/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/mabshoff/sage-4.0.alpha0/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/mabshoff/sage-4.0.alpha0/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_79[79]>", line 1, in <module>
        f.roots(ring=RIF, multiplicities=False)###line 3895:
    sage: f.roots(ring=RIF, multiplicities=False)
      File "polynomial_element.pyx", line 3666, in sage.rings.polynomial.polynomial_element.Polynomial.roots (sage/rings/polynomial/polynomial_element.c:27446)
        assert rt.parent() is ring
    AssertionError
**********************************************************************
File "/home/ncalexan/sage-3.4.2-sage.math-only-x86_64-Linux/devel/sage-main/sage/rings/polynomial/polynomial_element.pyx", line 3897:
    sage: f.roots(ring=RealIntervalField(150))
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/sage-4.0.alpha0/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/mabshoff/sage-4.0.alpha0/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/mabshoff/sage-4.0.alpha0/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_79[80]>", line 1, in <module>
        f.roots(ring=RealIntervalField(Integer(150)))###line 3897:
    sage: f.roots(ring=RealIntervalField(150))
      File "polynomial_element.pyx", line 3662, in sage.rings.polynomial.polynomial_element.Polynomial.roots (sage/rings/polynomial/polynomial_element.c:27304)
        assert rt.parent() is ring
    AssertionError
**********************************************************************
File "/home/ncalexan/sage-3.4.2-sage.math-only-x86_64-Linux/devel/sage-main/sage/rings/polynomial/polynomial_element.pyx", line 3902:
    sage: f.roots(ring=RIF)
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/sage-4.0.alpha0/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/mabshoff/sage-4.0.alpha0/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/mabshoff/sage-4.0.alpha0/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_79[83]>", line 1, in <module>
        f.roots(ring=RIF)###line 3902:
    sage: f.roots(ring=RIF)
      File "polynomial_element.pyx", line 3662, in sage.rings.polynomial.polynomial_element.Polynomial.roots (sage/rings/polynomial/polynomial_element.c:27304)
        assert rt.parent() is ring
    AssertionError
**********************************************************************
File "/home/ncalexan/sage-3.4.2-sage.math-only-x86_64-Linux/devel/sage-main/sage/rings/polynomial/polynomial_element.pyx", line 3904:
    sage: f.roots(ring=RIF, multiplicities=False)
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/sage-4.0.alpha0/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/mabshoff/sage-4.0.alpha0/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/mabshoff/sage-4.0.alpha0/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_79[84]>", line 1, in <module>
        f.roots(ring=RIF, multiplicities=False)###line 3904:
    sage: f.roots(ring=RIF, multiplicities=False)
      File "polynomial_element.pyx", line 3666, in sage.rings.polynomial.polynomial_element.Polynomial.roots (sage/rings/polynomial/polynomial_element.c:27446)
        assert rt.parent() is ring
    AssertionError
**********************************************************************
File "/home/ncalexan/sage-3.4.2-sage.math-only-x86_64-Linux/devel/sage-main/sage/rings/polynomial/polynomial_element.pyx", line 3985:
    sage: f.roots(ring=RealIntervalField(150))
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/sage-4.0.alpha0/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/mabshoff/sage-4.0.alpha0/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/mabshoff/sage-4.0.alpha0/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_79[112]>", line 1, in <module>
        f.roots(ring=RealIntervalField(Integer(150)))###line 3985:
    sage: f.roots(ring=RealIntervalField(150))
      File "polynomial_element.pyx", line 3662, in sage.rings.polynomial.polynomial_element.Polynomial.roots (sage/rings/polynomial/polynomial_element.c:27304)
        assert rt.parent() is ring
    AssertionError
**********************************************************************
File "/home/ncalexan/sage-3.4.2-sage.math-only-x86_64-Linux/devel/sage-main/sage/rings/polynomial/polynomial_element.pyx", line 4298:
    sage: (x^2 - x - 1).real_roots()
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/sage-4.0.alpha0/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/mabshoff/sage-4.0.alpha0/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/mabshoff/sage-4.0.alpha0/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_80[3]>", line 1, in <module>
        (x**Integer(2) - x - Integer(1)).real_roots()###line 4298:
    sage: (x^2 - x - 1).real_roots()
      File "polynomial_element.pyx", line 4314, in sage.rings.polynomial.polynomial_element.Polynomial.real_roots (sage/rings/polynomial/polynomial_element.c:30800)
        return self.roots(ring=RR, multiplicities=False)
      File "polynomial_element.pyx", line 3666, in sage.rings.polynomial.polynomial_element.Polynomial.roots (sage/rings/polynomial/polynomial_element.c:27446)
        assert rt.parent() is ring
    AssertionError
**********************************************************************
2 items had failures:
   6 of 132 in __main__.example_79
   1 of   8 in __main__.example_80
***Test Failed*** 7 failures.
For whitespace errors, see the file /home/ncalexan/sage-3.4.2-sage.math-only-x86_64-Linux/tmp/.doctest_polynomial_element.py
	 [7.9 s]
sage -t  /number_field.py
**********************************************************************
File "/home/ncalexan/sage-3.4.2-sage.math-only-x86_64-Linux/devel/sage-main/sage/rings/number_field/number_field.py", line 5236:
    sage: F.Minkowski_embedding()
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/sage-4.0.alpha0/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/mabshoff/sage-4.0.alpha0/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/mabshoff/sage-4.0.alpha0/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_121[3]>", line 1, in <module>
        F.Minkowski_embedding()###line 5236:
    sage: F.Minkowski_embedding()
      File "/home/ncalexan/sage/local/lib/python2.5/site-packages/sage/rings/number_field/number_field.py", line 5255, in Minkowski_embedding
        places = self.places(prec=prec)
      File "/home/ncalexan/sage/local/lib/python2.5/site-packages/sage/rings/number_field/number_field.py", line 5365, in places
        real_intervals = [ x[0] for x in self.defining_polynomial().roots(R) ]
      File "polynomial_element.pyx", line 3662, in sage.rings.polynomial.polynomial_element.Polynomial.roots (sage/rings/polynomial/polynomial_element.c:27304)
    AssertionError
**********************************************************************
File "/home/ncalexan/sage-3.4.2-sage.math-only-x86_64-Linux/devel/sage-main/sage/rings/number_field/number_field.py", line 5240:
    sage: F.Minkowski_embedding([1, alpha+2, alpha^2-alpha])
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/sage-4.0.alpha0/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/mabshoff/sage-4.0.alpha0/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/mabshoff/sage-4.0.alpha0/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_121[4]>", line 1, in <module>
        F.Minkowski_embedding([Integer(1), alpha+Integer(2), alpha**Integer(2)-alpha])###line 5240:
    sage: F.Minkowski_embedding([1, alpha+2, alpha^2-alpha])
      File "/home/ncalexan/sage/local/lib/python2.5/site-packages/sage/rings/number_field/number_field.py", line 5255, in Minkowski_embedding
        places = self.places(prec=prec)
      File "/home/ncalexan/sage/local/lib/python2.5/site-packages/sage/rings/number_field/number_field.py", line 5365, in places
        real_intervals = [ x[0] for x in self.defining_polynomial().roots(R) ]
      File "polynomial_element.pyx", line 3662, in sage.rings.polynomial.polynomial_element.Polynomial.roots (sage/rings/polynomial/polynomial_element.c:27304)
    AssertionError
**********************************************************************
File "/home/ncalexan/sage-3.4.2-sage.math-only-x86_64-Linux/devel/sage-main/sage/rings/number_field/number_field.py", line 5244:
    sage: F.Minkowski_embedding() * (alpha + 2).vector().transpose()
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/sage-4.0.alpha0/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/mabshoff/sage-4.0.alpha0/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/mabshoff/sage-4.0.alpha0/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_121[5]>", line 1, in <module>
        F.Minkowski_embedding() * (alpha + Integer(2)).vector().transpose()###line 5244:
    sage: F.Minkowski_embedding() * (alpha + 2).vector().transpose()
      File "/home/ncalexan/sage/local/lib/python2.5/site-packages/sage/rings/number_field/number_field.py", line 5255, in Minkowski_embedding
        places = self.places(prec=prec)
      File "/home/ncalexan/sage/local/lib/python2.5/site-packages/sage/rings/number_field/number_field.py", line 5365, in places
        real_intervals = [ x[0] for x in self.defining_polynomial().roots(R) ]
      File "polynomial_element.pyx", line 3662, in sage.rings.polynomial.polynomial_element.Polynomial.roots (sage/rings/polynomial/polynomial_element.c:27304)
    AssertionError
**********************************************************************
File "/home/ncalexan/sage-3.4.2-sage.math-only-x86_64-Linux/devel/sage-main/sage/rings/number_field/number_field.py", line 5299:
    sage: F.<alpha> = NumberField(x^3-100*x+1) ; F.places()
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/sage-4.0.alpha0/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/mabshoff/sage-4.0.alpha0/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/mabshoff/sage-4.0.alpha0/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_122[2]>", line 1, in <module>
        F = NumberField(x**Integer(3)-Integer(100)*x+Integer(1), names=('alpha',)); (alpha,) = F._first_ngens(1); F.places()###line 5299:
    sage: F.<alpha> = NumberField(x^3-100*x+1) ; F.places()
      File "/home/ncalexan/sage/local/lib/python2.5/site-packages/sage/rings/number_field/number_field.py", line 5365, in places
        real_intervals = [ x[0] for x in self.defining_polynomial().roots(R) ]
      File "polynomial_element.pyx", line 3662, in sage.rings.polynomial.polynomial_element.Polynomial.roots (sage/rings/polynomial/polynomial_element.c:27304)
    AssertionError
**********************************************************************
File "/home/ncalexan/sage-3.4.2-sage.math-only-x86_64-Linux/devel/sage-main/sage/rings/number_field/number_field.py", line 5315:
    sage: F.<alpha> = NumberField(x^3+7) ; F.places()
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/sage-4.0.alpha0/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/mabshoff/sage-4.0.alpha0/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/mabshoff/sage-4.0.alpha0/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_122[3]>", line 1, in <module>
        F = NumberField(x**Integer(3)+Integer(7), names=('alpha',)); (alpha,) = F._first_ngens(1); F.places()###line 5315:
    sage: F.<alpha> = NumberField(x^3+7) ; F.places()
      File "/home/ncalexan/sage/local/lib/python2.5/site-packages/sage/rings/number_field/number_field.py", line 5365, in places
        real_intervals = [ x[0] for x in self.defining_polynomial().roots(R) ]
      File "polynomial_element.pyx", line 3662, in sage.rings.polynomial.polynomial_element.Polynomial.roots (sage/rings/polynomial/polynomial_element.c:27304)
    AssertionError
**********************************************************************
File "/home/ncalexan/sage-3.4.2-sage.math-only-x86_64-Linux/devel/sage-main/sage/rings/number_field/number_field.py", line 5336:
    sage: F.places(prec=10)
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/sage-4.0.alpha0/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/mabshoff/sage-4.0.alpha0/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/mabshoff/sage-4.0.alpha0/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_122[5]>", line 1, in <module>
        F.places(prec=Integer(10))###line 5336:
    sage: F.places(prec=10)
      File "/home/ncalexan/sage/local/lib/python2.5/site-packages/sage/rings/number_field/number_field.py", line 5365, in places
        real_intervals = [ x[0] for x in self.defining_polynomial().roots(R) ]
      File "polynomial_element.pyx", line 3662, in sage.rings.polynomial.polynomial_element.Polynomial.roots (sage/rings/polynomial/polynomial_element.c:27304)
    AssertionError
**********************************************************************
File "/home/ncalexan/sage-3.4.2-sage.math-only-x86_64-Linux/devel/sage-main/sage/rings/number_field/number_field.py", line 5386:
    sage: F.<alpha> = NumberField(x^4-7) ; F.real_places()
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/sage-4.0.alpha0/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/mabshoff/sage-4.0.alpha0/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/mabshoff/sage-4.0.alpha0/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_123[2]>", line 1, in <module>
        F = NumberField(x**Integer(4)-Integer(7), names=('alpha',)); (alpha,) = F._first_ngens(1); F.real_places()###line 5386:
    sage: F.<alpha> = NumberField(x^4-7) ; F.real_places()
      File "/home/ncalexan/sage/local/lib/python2.5/site-packages/sage/rings/number_field/number_field.py", line 5396, in real_places
        return self.places(prec=prec)[0:self.signature()[0]]
      File "/home/ncalexan/sage/local/lib/python2.5/site-packages/sage/rings/number_field/number_field.py", line 5365, in places
        real_intervals = [ x[0] for x in self.defining_polynomial().roots(R) ]
      File "polynomial_element.pyx", line 3662, in sage.rings.polynomial.polynomial_element.Polynomial.roots (sage/rings/polynomial/polynomial_element.c:27304)
    AssertionError
**********************************************************************
File "/home/ncalexan/sage-3.4.2-sage.math-only-x86_64-Linux/devel/sage-main/sage/rings/number_field/number_field.py", line 3322:
    sage: F.reduced_basis(prec=64)
Expected:
    Traceback (most recent call last):                 
    ...                                                
    PariError: not a definite matrix in lllgram (42)   
Got:
    Traceback (most recent call last):
      File "/scratch/mabshoff/sage-4.0.alpha0/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/mabshoff/sage-4.0.alpha0/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/mabshoff/sage-4.0.alpha0/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_74[7]>", line 1, in <module>
        F.reduced_basis(prec=Integer(64))###line 3322:
    sage: F.reduced_basis(prec=64)
      File "/home/ncalexan/sage/local/lib/python2.5/site-packages/sage/rings/number_field/number_field.py", line 3357, in reduced_basis
        M = self.Minkowski_embedding(self.integral_basis(), prec=prec)
      File "/home/ncalexan/sage/local/lib/python2.5/site-packages/sage/rings/number_field/number_field.py", line 5262, in Minkowski_embedding
        sqrt2 = f.roots(R)[1][0]
      File "polynomial_element.pyx", line 3662, in sage.rings.polynomial.polynomial_element.Polynomial.roots (sage/rings/polynomial/polynomial_element.c:27304)
    AssertionError
**********************************************************************
File "/home/ncalexan/sage-3.4.2-sage.math-only-x86_64-Linux/devel/sage-main/sage/rings/number_field/number_field.py", line 3327:
    sage: F.reduced_basis(prec=96)
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/sage-4.0.alpha0/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/mabshoff/sage-4.0.alpha0/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/mabshoff/sage-4.0.alpha0/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_74[8]>", line 1, in <module>
        F.reduced_basis(prec=Integer(96))###line 3327:
    sage: F.reduced_basis(prec=96)
      File "/home/ncalexan/sage/local/lib/python2.5/site-packages/sage/rings/number_field/number_field.py", line 3357, in reduced_basis
        M = self.Minkowski_embedding(self.integral_basis(), prec=prec)
      File "/home/ncalexan/sage/local/lib/python2.5/site-packages/sage/rings/number_field/number_field.py", line 5262, in Minkowski_embedding
        sqrt2 = f.roots(R)[1][0]
      File "polynomial_element.pyx", line 3662, in sage.rings.polynomial.polynomial_element.Polynomial.roots (sage/rings/polynomial/polynomial_element.c:27304)
    AssertionError
**********************************************************************
File "/home/ncalexan/sage-3.4.2-sage.math-only-x86_64-Linux/devel/sage-main/sage/rings/number_field/number_field.py", line 3427:
    sage: F.reduced_gram_matrix(prec=128)
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/sage-4.0.alpha0/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/mabshoff/sage-4.0.alpha0/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/mabshoff/sage-4.0.alpha0/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_75[7]>", line 1, in <module>
        F.reduced_gram_matrix(prec=Integer(128))###line 3427:
    sage: F.reduced_gram_matrix(prec=128)
      File "/home/ncalexan/sage/local/lib/python2.5/site-packages/sage/rings/number_field/number_field.py", line 3455, in reduced_gram_matrix
        M = self.Minkowski_embedding(prec=prec)
      File "/home/ncalexan/sage/local/lib/python2.5/site-packages/sage/rings/number_field/number_field.py", line 5262, in Minkowski_embedding
        sqrt2 = f.roots(R)[1][0]
      File "polynomial_element.pyx", line 3662, in sage.rings.polynomial.polynomial_element.Polynomial.roots (sage/rings/polynomial/polynomial_element.c:27304)
    AssertionError

  ***   Warning: large Minkowski bound: certification will be VERY long.
  ***   Warning: large Minkowski bound: certification will be VERY long.
  ***   Warning: large Minkowski bound: certification will be VERY long.
  ***   Warning: large Minkowski bound: certification will be VERY long.
**********************************************************************
5 items had failures:
   3 of   6 in __main__.example_121
   3 of   6 in __main__.example_122
   1 of   3 in __main__.example_123
   2 of   9 in __main__.example_74
   1 of   8 in __main__.example_75
***Test Failed*** 10 failures.
For whitespace errors, see the file /home/ncalexan/sage-3.4.2-sage.math-only-x86_64-Linux/tmp/.doctest_number_field.py
	 [17.2 s]
 
----------------------------------------------------------------------

The following tests failed:

	sage -t  olynomial_element.pyx # 7 doctests failed
	sage -t  /number_field.py # 10 doctests failed
----------------------------------------------------------------------
Total time for all tests: 17.4 seconds

sage-test finished with failing tests at Wed Jun  3 21:30:10
```


Issue created by migration from https://trac.sagemath.org/ticket/6207





---

archive/issue_comments_049488.json:
```json
{
    "body": "Attachment [roots-parent-2.patch](tarball://root/attachments/some-uuid/ticket6207/roots-parent-2.patch) by @aghitza created at 2009-07-11 10:44:51",
    "created_at": "2009-07-11T10:44:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6207",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6207#issuecomment-49488",
    "user": "https://github.com/aghitza"
}
```

Attachment [roots-parent-2.patch](tarball://root/attachments/some-uuid/ticket6207/roots-parent-2.patch) by @aghitza created at 2009-07-11 10:44:51



---

archive/issue_comments_049489.json:
```json
{
    "body": "I don't think this was really meant for review. Nick's patch just demonstrates that the function `.roots()` fails the requirement that the returned roots are in the base ring of the polynomial field. Hopefully someone will go through the failing doctests above, and fix the real problems.",
    "created_at": "2009-07-17T15:55:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6207",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6207#issuecomment-49489",
    "user": "https://github.com/burcin"
}
```

I don't think this was really meant for review. Nick's patch just demonstrates that the function `.roots()` fails the requirement that the returned roots are in the base ring of the polynomial field. Hopefully someone will go through the failing doctests above, and fix the real problems.



---

archive/issue_comments_049490.json:
```json
{
    "body": "Attachment [trac_6207.patch](tarball://root/attachments/some-uuid/ticket6207/trac_6207.patch) by @williamstein created at 2010-01-17 06:10:11\n\nApply only the patch I posted. \n\nNote -- with the first patch the checks about parents are left on, so the referee can run the test suite with them on.  The second part2 patch turns them off.\n\nNOTE: I did not fix the issues with precision being too hire for CIF and RIF, since that behavior is already very clearly documented (IMHO) by Carl Witty in the roots method. \n\nIn part2 I get rid of all the debug code.  My reasoning is:\n\n  (1) I want the roots docstring to be on that method.\n\n  (2) The code was really specifically for debugging this problem, which turned out to be mostly caused by my non-uniqueness of the RealField object. \n\nBy the way, the main work of this patch is to make it so RealField caching and naming is more sensible, systematic, correct, and the same as is already done for ComplexField.",
    "created_at": "2010-01-17T06:10:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6207",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6207#issuecomment-49490",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac_6207.patch](tarball://root/attachments/some-uuid/ticket6207/trac_6207.patch) by @williamstein created at 2010-01-17 06:10:11

Apply only the patch I posted. 

Note -- with the first patch the checks about parents are left on, so the referee can run the test suite with them on.  The second part2 patch turns them off.

NOTE: I did not fix the issues with precision being too hire for CIF and RIF, since that behavior is already very clearly documented (IMHO) by Carl Witty in the roots method. 

In part2 I get rid of all the debug code.  My reasoning is:

  (1) I want the roots docstring to be on that method.

  (2) The code was really specifically for debugging this problem, which turned out to be mostly caused by my non-uniqueness of the RealField object. 

By the way, the main work of this patch is to make it so RealField caching and naming is more sensible, systematic, correct, and the same as is already done for ComplexField.



---

archive/issue_comments_049491.json:
```json
{
    "body": "Attachment [trac_6207-part2.patch](tarball://root/attachments/some-uuid/ticket6207/trac_6207-part2.patch) by @williamstein created at 2010-01-17 06:10:23",
    "created_at": "2010-01-17T06:10:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6207",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6207#issuecomment-49491",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac_6207-part2.patch](tarball://root/attachments/some-uuid/ticket6207/trac_6207-part2.patch) by @williamstein created at 2010-01-17 06:10:23



---

archive/issue_comments_049492.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-17T06:10:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6207",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6207#issuecomment-49492",
    "user": "https://github.com/williamstein"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_049493.json:
```json
{
    "body": "I applied `trac_6207.patch` to a fresh sage-4.3.1.rc1, but doing sage -b gives me errors:\n\n\n```\npython `which cython` --embed-positions --directive cdivision=True -I/opt/sage-4.3.1.rc1/devel/sage-main -o sage/ext/interpreters/wrapper_rr.c sage/ext/interpreters/wrapper_rr.pyx\n\nError converting Pyrex file to C:\n------------------------------------------------------------\n...\n\nfrom python_object cimport PyObject\n\nfrom sage.ext.fast_callable cimport Wrapper\n\nfrom sage.rings.real_mpfr cimport RealField, RealNumber\n^\n------------------------------------------------------------\n\n/opt/sage-4.3.1.rc1/devel/sage-main/sage/ext/interpreters/wrapper_rr.pxd:7:0: 'RealField.pxd' not found\n\nError converting Pyrex file to C:\n------------------------------------------------------------\n...\n\nfrom python_object cimport PyObject\n\nfrom sage.ext.fast_callable cimport Wrapper\n\nfrom sage.rings.real_mpfr cimport RealField, RealNumber\n                                 ^\n------------------------------------------------------------\n\n/opt/sage-4.3.1.rc1/devel/sage-main/sage/ext/interpreters/wrapper_rr.pxd:7:34: Name 'RealField' not declared in module 'sage.rings.real_mpfr'\n\nError converting Pyrex file to C:\n------------------------------------------------------------\n...\n\nfrom sage.rings.real_mpfr cimport RealField, RealNumber\nfrom sage.libs.mpfr cimport *\n\ncdef class Wrapper_rr(Wrapper):\n    cdef RealField_class domain\n        ^\n------------------------------------------------------------\n\n/opt/sage-4.3.1.rc1/devel/sage-main/sage/ext/interpreters/wrapper_rr.pxd:11:9: 'RealField_class' is not a type identifier\n\nError converting Pyrex file to C:\n\n\nError running command, failed with status 256.\nsage: There was an error installing modified sage library code.\n\n\n\n\nreal\t0m48.095s\nuser\t0m42.444s\nsys\t0m1.370s\n```\n",
    "created_at": "2010-01-20T07:34:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6207",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6207#issuecomment-49493",
    "user": "https://github.com/aghitza"
}
```

I applied `trac_6207.patch` to a fresh sage-4.3.1.rc1, but doing sage -b gives me errors:


```
python `which cython` --embed-positions --directive cdivision=True -I/opt/sage-4.3.1.rc1/devel/sage-main -o sage/ext/interpreters/wrapper_rr.c sage/ext/interpreters/wrapper_rr.pyx

Error converting Pyrex file to C:
------------------------------------------------------------
...

from python_object cimport PyObject

from sage.ext.fast_callable cimport Wrapper

from sage.rings.real_mpfr cimport RealField, RealNumber
^
------------------------------------------------------------

/opt/sage-4.3.1.rc1/devel/sage-main/sage/ext/interpreters/wrapper_rr.pxd:7:0: 'RealField.pxd' not found

Error converting Pyrex file to C:
------------------------------------------------------------
...

from python_object cimport PyObject

from sage.ext.fast_callable cimport Wrapper

from sage.rings.real_mpfr cimport RealField, RealNumber
                                 ^
------------------------------------------------------------

/opt/sage-4.3.1.rc1/devel/sage-main/sage/ext/interpreters/wrapper_rr.pxd:7:34: Name 'RealField' not declared in module 'sage.rings.real_mpfr'

Error converting Pyrex file to C:
------------------------------------------------------------
...

from sage.rings.real_mpfr cimport RealField, RealNumber
from sage.libs.mpfr cimport *

cdef class Wrapper_rr(Wrapper):
    cdef RealField_class domain
        ^
------------------------------------------------------------

/opt/sage-4.3.1.rc1/devel/sage-main/sage/ext/interpreters/wrapper_rr.pxd:11:9: 'RealField_class' is not a type identifier

Error converting Pyrex file to C:


Error running command, failed with status 256.
sage: There was an error installing modified sage library code.




real	0m48.095s
user	0m42.444s
sys	0m1.370s
```




---

archive/issue_comments_049494.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-01-20T07:34:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6207",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6207#issuecomment-49494",
    "user": "https://github.com/aghitza"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_049495.json:
```json
{
    "body": "In `ext/interpreters/wrapper_rr.pxd`, changing `RealField` to `RealField_class` in the line\n\n\n```\nfrom sage.rings.real_mpfr cimport RealField, RealNumber\n```\n\n\nmakes Sage build ok.  Is this the right fix?  I'm a bit thrown off by that file starting with the line `# Automatically generated.  Do not edit!`\n\nI'm running tests now.",
    "created_at": "2010-01-20T07:43:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6207",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6207#issuecomment-49495",
    "user": "https://github.com/aghitza"
}
```

In `ext/interpreters/wrapper_rr.pxd`, changing `RealField` to `RealField_class` in the line


```
from sage.rings.real_mpfr cimport RealField, RealNumber
```


makes Sage build ok.  Is this the right fix?  I'm a bit thrown off by that file starting with the line `# Automatically generated.  Do not edit!`

I'm running tests now.



---

archive/issue_comments_049496.json:
```json
{
    "body": "After reading William's first patch more carefully, I now know that the fix needs to be made in `ext/gen_interpreters.py`\n\nI'll attach a reviewer patch in a second, and run tests.",
    "created_at": "2010-01-20T07:56:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6207",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6207#issuecomment-49496",
    "user": "https://github.com/aghitza"
}
```

After reading William's first patch more carefully, I now know that the fix needs to be made in `ext/gen_interpreters.py`

I'll attach a reviewer patch in a second, and run tests.



---

archive/issue_comments_049497.json:
```json
{
    "body": "apply after the previous two patches",
    "created_at": "2010-01-20T08:14:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6207",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6207#issuecomment-49497",
    "user": "https://github.com/aghitza"
}
```

apply after the previous two patches



---

archive/issue_comments_049498.json:
```json
{
    "body": "Attachment [trac_6207-review.patch](tarball://root/attachments/some-uuid/ticket6207/trac_6207-review.patch) by @aghitza created at 2010-01-20 09:37:26\n\nOK, this looks good.  I give a positive review to William's two patches.\n\nIt remains for someone to look at my reviewer patch -- this should be very quick now.  Note that, apart from fixing the build, I made the comment at the top of the interpreter files a little more explicit.",
    "created_at": "2010-01-20T09:37:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6207",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6207#issuecomment-49498",
    "user": "https://github.com/aghitza"
}
```

Attachment [trac_6207-review.patch](tarball://root/attachments/some-uuid/ticket6207/trac_6207-review.patch) by @aghitza created at 2010-01-20 09:37:26

OK, this looks good.  I give a positive review to William's two patches.

It remains for someone to look at my reviewer patch -- this should be very quick now.  Note that, apart from fixing the build, I made the comment at the top of the interpreter files a little more explicit.



---

archive/issue_comments_049499.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-01-20T09:37:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6207",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6207#issuecomment-49499",
    "user": "https://github.com/aghitza"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_049500.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-20T09:58:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6207",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6207#issuecomment-49500",
    "user": "https://github.com/williamstein"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_049501.json:
```json
{
    "body": "I approve of the reviewer patch.",
    "created_at": "2010-01-20T09:58:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6207",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6207#issuecomment-49501",
    "user": "https://github.com/williamstein"
}
```

I approve of the reviewer patch.



---

archive/issue_comments_049502.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-22T15:34:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6207",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6207#issuecomment-49502",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed



---

archive/issue_events_014561.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2010-01-22T15:34:35Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6207",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6207#event-14561"
}
```



---

archive/issue_comments_049503.json:
```json
{
    "body": "Merged in this order:\n\n1. [trac_6207.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/6207/trac_6207.patch)\n2. [trac_6207-part2.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/6207/trac_6207-part2.patch)\n3. [trac_6207-review.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/6207/trac_6207-review.patch)",
    "created_at": "2010-01-25T18:42:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6207",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6207#issuecomment-49503",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Merged in this order:

1. [trac_6207.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/6207/trac_6207.patch)
2. [trac_6207-part2.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/6207/trac_6207-part2.patch)
3. [trac_6207-review.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/6207/trac_6207-review.patch)
