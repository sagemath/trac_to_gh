# Issue 6196: mpmath support

Issue created by migration from https://trac.sagemath.org/ticket/6196

Original creator: fredrik.johansson

Original creation time: 2009-06-03 17:32:58

Assignee: mabshoff

Patch description:

Adds sage.libs.mpmath which provides wrapper functions and
monkey patches some internal mpmath functions for speed. Mpmath
functions can be called from Sage as follows (with forward
and backward conversions handled automatically):

sage: import sage.libs.mpmath.all as a
sage: a.call(a.hyp2f1, 2, 2/3, -1/2, 3+4*I)
-0.111907858412569 - 0.536467867510390*I
sage: a.call(a.hyp2f1, 2, 2/3, -1/2, 3+4*I, prec=100)
-0.11190785841256900204178259859 - 0.53646786751038954277574814099*I

Some partial support for direct conversion from Sage -> mpmath
is also implemented (this is not completely working yet).


---

Attachment


---

Comment by ncalexan created at 2009-06-19 18:56:30

I am interested in using mpmath for numerical integration, but unfortunately I get major build errors with 4.0.2.alpha0.  See http://pastebin.com/d13f03d03 for details.  Any thoughts?


---

Comment by mhansen created at 2009-06-19 22:20:55

Changing assignee from mabshoff to mhansen.


---

Attachment

I put an spkg at http://sage.math.washington.edu/home/mhansen/mpmath-0.12.spkg


---

Comment by mhansen created at 2009-06-19 22:20:55

Changing status from new to assigned.


---

Comment by ncalexan created at 2009-06-19 22:52:00

Apply all patches.


---

Comment by ncalexan created at 2009-06-19 22:52:51

Positive review for me.  Change status after my tiny patch is refereed.


---

Attachment


---

Comment by mhansen created at 2009-06-19 22:57:25

Nick's changes look good.


---

Comment by boothby created at 2009-06-24 18:21:14

Doctest failures:


```

sage -t -long devel/sage/sage/rings/real_mpfr.pyx
**********************************************************************
File "/space/boothby/sage-4.0.3/devel/sage-main/sage/rings/real_mpfr.pyx", line 2284:
    sage: RR(-1.5)._mpmath_()
Exception raised:
    Traceback (most recent call last):
      File "/space/boothby/sage-4.0.3/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/space/boothby/sage-4.0.3/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/space/boothby/sage-4.0.3/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_65[2]>", line 1, in <module>
        RR(-RealNumber('1.5'))._mpmath_()###line 2284:
    sage: RR(-1.5)._mpmath_()
      File "real_mpfr.pyx", line 2289, in sage.rings.real_mpfr.RealNumber._mpmath_ (sage/rings/real$
        from sage.libs.mpmath.all import make_mpf
      File "/space/boothby/sage-4.0.3/local/lib/python2.5/site-packages/sage/libs/mpmath/all.py", l$
        import mpmath
    ImportError: No module named mpmath
**********************************************************************
1 items had failures:
   1 of   3 in __main__.example_65
***Test Failed*** 1 failures.
```



```
sage -t -long devel/sage/sage/rings/complex_number.pyx
**********************************************************************
File "/space/boothby/sage-4.0.3/devel/sage-main/sage/rings/complex_number.pyx", line 484:
    sage: CC(1,2)._mpmath_()
Exception raised:
    Traceback (most recent call last):
      File "/space/boothby/sage-4.0.3/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/space/boothby/sage-4.0.3/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/space/boothby/sage-4.0.3/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_15[2]>", line 1, in <module>
        CC(Integer(1),Integer(2))._mpmath_()###line 484:
    sage: CC(1,2)._mpmath_()
      File "complex_number.pyx", line 489, in sage.rings.complex_number.ComplexNumber._mpmath_ (sag$
        from sage.libs.mpmath.all import make_mpc
      File "/space/boothby/sage-4.0.3/local/lib/python2.5/site-packages/sage/libs/mpmath/all.py", l$
        import mpmath
    ImportError: No module named mpmath
**********************************************************************
1 items had failures:
   1 of   3 in __main__.example_15
***Test Failed*** 1 failures.
```



```
sage -t -long devel/sage/sage/structure/element.pyx
**********************************************************************
File "/space/boothby/sage-4.0.3/devel/sage-main/sage/structure/element.pyx", line 426:
    sage: from sage.libs.mpmath.all import mp, mpmathify
Exception raised:
    Traceback (most recent call last):
      File "/space/boothby/sage-4.0.3/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/space/boothby/sage-4.0.3/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/space/boothby/sage-4.0.3/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_13[2]>", line 1, in <module>
        from sage.libs.mpmath.all import mp, mpmathify###line 426:
    sage: from sage.libs.mpmath.all import mp, mpmathify
      File "/space/boothby/sage-4.0.3/local/lib/python2.5/site-packages/sage/libs/mpmath/all.py", l$
        import mpmath
    ImportError: No module named mpmath
**********************************************************************
File "/space/boothby/sage-4.0.3/devel/sage-main/sage/structure/element.pyx", line 427:
    sage: mp.dps = 30
Exception raised:
    Traceback (most recent call last):
      File "/space/boothby/sage-4.0.3/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/space/boothby/sage-4.0.3/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/space/boothby/sage-4.0.3/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_13[3]>", line 1, in <module>
        mp.dps = Integer(30)###line 427:
    sage: mp.dps = 30
    NameError: name 'mp' is not defined
**********************************************************************
File "/space/boothby/sage-4.0.3/devel/sage-main/sage/structure/element.pyx", line 428:
    sage: 25._mpmath_(53)
Exception raised:
    Traceback (most recent call last):
      File "/space/boothby/sage-4.0.3/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/space/boothby/sage-4.0.3/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/space/boothby/sage-4.0.3/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs

...
```




```

sage -t -long devel/sage/sage/libs/mpmath/utils.pyx
**********************************************************************
File "/space/boothby/sage-4.0.3/devel/sage-main/sage/libs/mpmath/utils.pyx", line 27:
    sage: from mpmath.libmpf import from_man_exp
Exception raised:
    Traceback (most recent call last):
      File "/space/boothby/sage-4.0.3/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/space/boothby/sage-4.0.3/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/space/boothby/sage-4.0.3/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[2]>", line 1, in <module>
        from mpmath.libmpf import from_man_exp###line 27:
    sage: from mpmath.libmpf import from_man_exp
    ImportError: No module named mpmath.libmpf
**********************************************************************
File "/space/boothby/sage-4.0.3/devel/sage-main/sage/libs/mpmath/utils.pyx", line 28:
    sage: from_man_exp(-6, -1)
Exception raised:
    Traceback (most recent call last):
      File "/space/boothby/sage-4.0.3/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/space/boothby/sage-4.0.3/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/space/boothby/sage-4.0.3/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
...
```



---

Comment by ncalexan created at 2009-06-24 18:37:25

There's an spkg; this looks a lot like you didn't install it.  I did *exactly* the same thing with malb's singular spkg update when I was release manager.  Maybe we need sage -merge to yell if it sees certain things, like spkgs?


---

Comment by boothby created at 2009-06-24 18:39:05

Oh damn.  Thanks, Nick.


---

Comment by rlm created at 2009-07-02 21:07:15

Resolution: fixed


---

Comment by mvngu created at 2009-07-12 10:35:10

The milestone for this ticket should be 4.1. I can't change it, since I don't have admin privileges on trac.
