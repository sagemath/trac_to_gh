# Issue 6207: roots of polynomial have incorrect parent when ring=R is specified

Issue created by migration from Trac.

Original creator: ncalexan

Original creation time: 2009-06-04 04:34:20

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



---

Attachment


---

Comment by burcin created at 2009-07-17 15:55:29

I don't think this was really meant for review. Nick's patch just demonstrates that the function `.roots()` fails the requirement that the returned roots are in the base ring of the polynomial field. Hopefully someone will go through the failing doctests above, and fix the real problems.


---

Attachment

Apply only the patch I posted. 

Note -- with the first patch the checks about parents are left on, so the referee can run the test suite with them on.  The second part2 patch turns them off.

NOTE: I did not fix the issues with precision being too hire for CIF and RIF, since that behavior is already very clearly documented (IMHO) by Carl Witty in the roots method. 

In part2 I get rid of all the debug code.  My reasoning is:

  (1) I want the roots docstring to be on that method.

  (2) The code was really specifically for debugging this problem, which turned out to be mostly caused by my non-uniqueness of the RealField object. 

By the way, the main work of this patch is to make it so RealField caching and naming is more sensible, systematic, correct, and the same as is already done for ComplexField.


---

Attachment


---

Comment by was created at 2010-01-17 06:10:31

Changing status from new to needs_review.


---

Comment by AlexGhitza created at 2010-01-20 07:34:29

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

Comment by AlexGhitza created at 2010-01-20 07:34:29

Changing status from needs_review to needs_work.


---

Comment by AlexGhitza created at 2010-01-20 07:43:31

In `ext/interpreters/wrapper_rr.pxd`, changing `RealField` to `RealField_class` in the line


```
from sage.rings.real_mpfr cimport RealField, RealNumber
```


makes Sage build ok.  Is this the right fix?  I'm a bit thrown off by that file starting with the line `# Automatically generated.  Do not edit!`

I'm running tests now.


---

Comment by AlexGhitza created at 2010-01-20 07:56:35

After reading William's first patch more carefully, I now know that the fix needs to be made in `ext/gen_interpreters.py`

I'll attach a reviewer patch in a second, and run tests.


---

Comment by AlexGhitza created at 2010-01-20 08:14:06

apply after the previous two patches


---

Attachment

OK, this looks good.  I give a positive review to William's two patches.

It remains for someone to look at my reviewer patch -- this should be very quick now.  Note that, apart from fixing the build, I made the comment at the top of the interpreter files a little more explicit.


---

Comment by AlexGhitza created at 2010-01-20 09:37:26

Changing status from needs_work to needs_review.


---

Comment by was created at 2010-01-20 09:58:49

Changing status from needs_review to positive_review.


---

Comment by was created at 2010-01-20 09:58:49

I approve of the reviewer patch.


---

Comment by mvngu created at 2010-01-22 15:34:35

Resolution: fixed


---

Comment by mvngu created at 2010-01-25 18:42:20

Merged in this order:

 1. [trac_6207.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/6207/trac_6207.patch)
 1. [trac_6207-part2.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/6207/trac_6207-part2.patch)
 1. [trac_6207-review.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/6207/trac_6207-review.patch)
