# Issue 5270: [with patch, needs review] implement plotting of affine and projective algebraic curves

Issue created by migration from https://trac.sagemath.org/ticket/5270

Original creator: AlexGhitza

Original creation time: 2009-02-14 13:49:49

Assignee: AlexGhitza

The patch implements plot() methods for affine and projective algebraic curves.  In the affine case it simply calls the plot() method of the defining ideal of the curve.  In the projective case it calls the plot() method of an affine patch of the curve.

This is mostly a usability enhancement.  I ran into a few bugs while working on this, so the patch should be applied only after #5267 and #5269 get merged.



---

Comment by AlexGhitza created at 2009-02-14 13:54:02

I forgot to mention this: I also modified plot() for an ideal so that ideals over any subring of RR can be plotted (not just over QQ).


---

Comment by cremona created at 2009-02-15 12:44:05

Looks great -- I think this ability to plot the idfferent affine patches of a projective curve is a very nice feature.

Patch applies fine to 3.3.rc0.  I had doctest problems in projective_curve.py:

```
sage -t  "devel/sage-5270/sage/schemes/plane_curves/projective_curve.py"
**********************************************************************
File "/home/john/sage-3.3.rc0/devel/sage-5270/sage/schemes/plane_curves/projective_curve.py", line 208:
    sage: C.plot(patch=0)
Exception raised:
    Traceback (most recent call last):
      File "/home/john/sage-3.3.rc0/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/john/sage-3.3.rc0/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/john/sage-3.3.rc0/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_4[5]>", line 1, in <module>
        C.plot(patch=Integer(0))###line 208:
    sage: C.plot(patch=0)
      File "/home/john/sage-3.3.rc0/local/lib/python2.5/site-packages/sage/schemes/plane_curves/projective_curve.py", line 232, in plot
        return C.plot(*args, **kwds)
      File "/home/john/sage-3.3.rc0/local/lib/python2.5/site-packages/sage/schemes/plane_curves/affine_curve.py", line 206, in plot
        return I.plot(*args, **kwds)
      File "/home/john/sage-3.3.rc0/local/lib/python2.5/site-packages/sage/rings/polynomial/multi_polynomial_ideal.py", line 2389, in plot
        roots = f.subs({v:i}).univariate_polynomial().change_ring(RR).roots()
      File "multi_polynomial_libsingular.pyx", line 3161, in sage.rings.polynomial.multi_polynomial_libsingular.MPolynomial_libsingular.univariate_polynomial (sage/rings/polynomial/multi_polynomial_libsingular.cpp:21299)
    IndexError: list index out of range
**********************************************************************
File "/home/john/sage-3.3.rc0/devel/sage-5270/sage/schemes/plane_curves/projective_curve.py", line 222:
    sage: C.plot()
Exception raised:
    Traceback (most recent call last):
      File "/home/john/sage-3.3.rc0/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/john/sage-3.3.rc0/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/john/sage-3.3.rc0/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_4[15]>", line 1, in <module>
        C.plot()###line 222:
    sage: C.plot()
      File "/home/john/sage-3.3.rc0/local/lib/python2.5/site-packages/sage/schemes/plane_curves/projective_curve.py", line 231, in plot
        C = Curve(self.affine_patch(patch))
      File "/home/john/sage-3.3.rc0/local/lib/python2.5/site-packages/sage/schemes/plane_curves/constructor.py", line 135, in Curve
        return Curve(F.defining_polynomials())
      File "/home/john/sage-3.3.rc0/local/lib/python2.5/site-packages/sage/schemes/plane_curves/constructor.py", line 139, in Curve
        return Curve(F[0])
      File "/home/john/sage-3.3.rc0/local/lib/python2.5/site-packages/sage/schemes/plane_curves/constructor.py", line 185, in Curve
        return ProjectiveCurve_generic(P2, F)
      File "/home/john/sage-3.3.rc0/local/lib/python2.5/site-packages/sage/schemes/plane_curves/projective_curve.py", line 44, in __init__
        Curve_generic_projective.__init__(self, A, [f])
      File "/home/john/sage-3.3.rc0/local/lib/python2.5/site-packages/sage/schemes/generic/algebraic_scheme.py", line 208, in __init__
        G = self._validate(G)
      File "/home/john/sage-3.3.rc0/local/lib/python2.5/site-packages/sage/schemes/generic/algebraic_scheme.py", line 572, in _validate
        "defining polynomials (= %s) must be homogeneous"%G
    TypeError: defining polynomials (= -4*x0^5 + 30*x0^3 + x1^2 - 45*x0 + 22) must be homogeneous
**********************************************************************
File "/home/john/sage-3.3.rc0/devel/sage-5270/sage/schemes/plane_curves/projective_curve.py", line 223:
    sage: C.plot(patch=0)
Exception raised:
    Traceback (most recent call last):
      File "/home/john/sage-3.3.rc0/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/john/sage-3.3.rc0/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/john/sage-3.3.rc0/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_4[16]>", line 1, in <module>
        C.plot(patch=Integer(0))###line 223:
    sage: C.plot(patch=0)
      File "/home/john/sage-3.3.rc0/local/lib/python2.5/site-packages/sage/schemes/plane_curves/projective_curve.py", line 231, in plot
        C = Curve(self.affine_patch(patch))
      File "/home/john/sage-3.3.rc0/local/lib/python2.5/site-packages/sage/schemes/plane_curves/constructor.py", line 135, in Curve
        return Curve(F.defining_polynomials())
      File "/home/john/sage-3.3.rc0/local/lib/python2.5/site-packages/sage/schemes/plane_curves/constructor.py", line 139, in Curve
        return Curve(F[0])
      File "/home/john/sage-3.3.rc0/local/lib/python2.5/site-packages/sage/schemes/plane_curves/constructor.py", line 185, in Curve
        return ProjectiveCurve_generic(P2, F)
      File "/home/john/sage-3.3.rc0/local/lib/python2.5/site-packages/sage/schemes/plane_curves/projective_curve.py", line 44, in __init__
        Curve_generic_projective.__init__(self, A, [f])
      File "/home/john/sage-3.3.rc0/local/lib/python2.5/site-packages/sage/schemes/generic/algebraic_scheme.py", line 208, in __init__
        G = self._validate(G)
      File "/home/john/sage-3.3.rc0/local/lib/python2.5/site-packages/sage/schemes/generic/algebraic_scheme.py", line 572, in _validate
        "defining polynomials (= %s) must be homogeneous"%G
    TypeError: defining polynomials (= x0^2*x1^3 + 22*x1^5 - 45*x1^4 + 30*x1^2 - 4) must be homogeneous
**********************************************************************
File "/home/john/sage-3.3.rc0/devel/sage-5270/sage/schemes/plane_curves/projective_curve.py", line 224:
    sage: C.plot(patch=1)
Exception raised:
    Traceback (most recent call last):
      File "/home/john/sage-3.3.rc0/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/john/sage-3.3.rc0/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/john/sage-3.3.rc0/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_4[17]>", line 1, in <module>
        C.plot(patch=Integer(1))###line 224:
    sage: C.plot(patch=1)
      File "/home/john/sage-3.3.rc0/local/lib/python2.5/site-packages/sage/schemes/plane_curves/projective_curve.py", line 231, in plot
        C = Curve(self.affine_patch(patch))
      File "/home/john/sage-3.3.rc0/local/lib/python2.5/site-packages/sage/schemes/plane_curves/constructor.py", line 135, in Curve
        return Curve(F.defining_polynomials())
      File "/home/john/sage-3.3.rc0/local/lib/python2.5/site-packages/sage/schemes/plane_curves/constructor.py", line 139, in Curve
        return Curve(F[0])
      File "/home/john/sage-3.3.rc0/local/lib/python2.5/site-packages/sage/schemes/plane_curves/constructor.py", line 185, in Curve
        return ProjectiveCurve_generic(P2, F)
      File "/home/john/sage-3.3.rc0/local/lib/python2.5/site-packages/sage/schemes/plane_curves/projective_curve.py", line 44, in __init__
        Curve_generic_projective.__init__(self, A, [f])
      File "/home/john/sage-3.3.rc0/local/lib/python2.5/site-packages/sage/schemes/generic/algebraic_scheme.py", line 208, in __init__
        G = self._validate(G)
      File "/home/john/sage-3.3.rc0/local/lib/python2.5/site-packages/sage/schemes/generic/algebraic_scheme.py", line 572, in _validate
        "defining polynomials (= %s) must be homogeneous"%G
    TypeError: defining polynomials (= -4*x0^5 + 30*x0^3*x1^2 - 45*x0*x1^4 + 22*x1^5 + x1^3) must be homogeneous
**********************************************************************
1 items had failures:
   4 of  18 in __main__.example_4
***Test Failed*** 4 failures.
For whitespace errors, see the file /home/john/sage-3.3.rc0/tmp/.doctest_projective_curve.py
	 [5.2 s]
exit code: 1024
 }}}

I think these are all in the hyperelliptic example.

PS I wonder how the doctests run without all the graphs popping up!


---

Comment by AlexGhitza created at 2009-02-15 22:20:01

Hi John,

Did you first apply the patches at #5267 and #5269?  This patch builds on those fixes.


---

Comment by cremona created at 2009-02-15 22:27:15

Replying to [comment:3 AlexGhitza]:
> Hi John,
> 
> Did you first apply the patches at #5267 and #5269?  This patch builds on those fixes.

No -- my mistake!  I saw those tickets were closed, but that's because they were merged in rc1 ans I was using rc0.  Sorry -- not time to do it again now.


---

Comment by AlexGhitza created at 2009-02-15 22:29:49

Changing status from new to assigned.


---

Comment by AlexGhitza created at 2009-02-15 22:29:49

No problem.  I should have been more precise about that -- I just didn't expect someone would review it before rc1 was out :)


---

Comment by was created at 2009-03-15 22:21:18

Alex, this needs to be rebased for sage-3.4:

```
sage: hg_sage.apply('http://trac.sagemath.org/sage_trac/attachment/ticket/5270/trac_5270.patch')
Attempting to load remote file: http://trac.sagemath.org/sage_trac/raw-attachment/ticket/5270/trac_5270.patch
Loading: [..]
cd "/home/wstein/build/sage-3.4/devel/sage" && hg status
cd "/home/wstein/build/sage-3.4/devel/sage" && hg status
cd "/home/wstein/build/sage-3.4/devel/sage" && hg import   "/scratch/wstein/sage/temp/sage.math.washington.edu/12908/tmp_1.patch"
applying /scratch/wstein/sage/temp/sage.math.washington.edu/12908/tmp_1.patch
patching file sage/rings/polynomial/multi_polynomial_ideal.py
Hunk #1 FAILED at 2315
Hunk #2 succeeded at 2761 with fuzz 2 (offset 409 lines).
1 out of 3 hunks FAILED -- saving rejects to file sage/rings/polynomial/multi_polynomial_ideal.py.rej
patching file sage/schemes/elliptic_curves/ell_generic.py
Hunk #1 FAILED at 2517
1 out of 1 hunks FAILED -- saving rejects to file sage/schemes/elliptic_curves/ell_generic.py.rej
patching file sage/schemes/hyperelliptic_curves/hyperelliptic_generic.py
Hunk #1 FAILED at 1
Hunk #2 FAILED at 77
2 out of 2 hunks FAILED -- saving rejects to file sage/schemes/hyperelliptic_curves/hyperelliptic_generic.py.rej
abort: patch failed to apply
```



---

Attachment


---

Comment by AlexGhitza created at 2009-03-16 02:54:19

Alright, I've rebased it against 3.4.  It took a bit longer than I thought because I'm still getting used to writing ReST docs.


---

Comment by cremona created at 2009-04-12 09:50:52

Positive review -- works on 3.4.1.rc2.  Sorry I forgot about this.


---

Comment by mabshoff created at 2009-04-13 06:50:10

Merged in Sage 3.4.1.rc3.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-13 06:50:10

Resolution: fixed
