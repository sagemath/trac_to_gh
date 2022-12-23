# Issue 6616: [with patch] higher heegner points

Issue created by migration from https://trac.sagemath.org/ticket/6616

Original creator: robertwb

Original creation time: 2009-07-25 10:23:56

Assignee: was

CC:  was cremona

Extend the heegner point code to compute y_lambda for lambda > 1.


---

Attachment


---

Attachment

Next (?):
   * computing y_c by computing all the conjugates of y_c numerically
   * computing the (huge) Kolyvagin point P_c
   * choosing y-coordinate of y_c correctly.
   * computing degree of ring class field K[c] in all cases (not just Kolyvagin c)
   * optimization


---

Comment by was created at 2009-08-01 22:56:51

This calculation uses massive RAM:

```
sage: E = EllipticCurve([877,0])
sage: P = E.heegner_point(-7)
sage: P
Heegner point of discriminant -7 on curve of conductor 49224256
sage: N(P)
[approx 5GB RAM (?) -- didn't wait for it to crash my laptop]
```


This should get dealt with.  No clue what causes this.


---

Attachment


---

Attachment


---

Comment by was created at 2009-08-30 22:09:52

rebased against 4.1.1


---

Attachment


---

Comment by was created at 2009-08-30 22:13:39

rebased against 4.1.1


---

Attachment

rebased against 4.1.1


---

Attachment


---

Attachment


---

Attachment


---

Attachment


---

Attachment


---

Attachment


---

Attachment


---

Attachment


---

Attachment


---

Attachment


---

Comment by was created at 2009-09-19 09:14:46

clean bundle with 1-16 against sage-4.1.1


---

Attachment

This is a clean bundle against sage-4.2.alpha0:

   http://sage.math.washington.edu/home/wstein/patches/heegner-20091021-rebased_against_4.2.alpha0.hg


---

Attachment

rebased against 4.2.1


---

Comment by was created at 2009-12-04 03:35:54

this is based against 4.2.1 after applying the hg bundle right above this patch.


---

Attachment


---

Attachment

apply just this one patch against a clean sage-4.3


---

Comment by was created at 2010-01-01 02:21:23

This is *finally* ready for review.  Apply just this patch against a clean sage-4.3 build:

    trac-6616-everything_rebased_against_4.3.patch


---

Comment by was created at 2010-01-01 02:21:23

Changing status from needs_work to needs_review.


---

Comment by cremona created at 2010-01-03 16:51:48

Changing status from needs_review to needs_work.


---

Comment by cremona created at 2010-01-03 16:51:48

Review:  I am immensely impressed by the huge amount of work which has gone into this ten thousand-line patch!  It goes far beyond the refactoring of the title.

I read through the patch itself, and liked what I saw.  (There are a few minor typos in the docstrings, which I did not note as I went through -- sorry).  Some docstrings which did not format properly:  numerical_approx, rational_kolyvagin_divisor, KolyvaginPoint.

There are a lot if interesting mathematical and algorithmic issues which are highlighted very well in comments and TODO blocks, which is good.

Testing all files in the elliptic_curves directory I found these problems.

```
	sage -t  "devel/sage-tests/sage/schemes/elliptic_curves/lseries_ell.py"
	sage -t  "devel/sage-tests/sage/schemes/elliptic_curves/heegner.py"
	sage -t  "devel/sage-tests/sage/schemes/elliptic_curves/period_lattice.py"
	sage -t  "devel/sage-tests/sage/schemes/elliptic_curves/ell_rational_field.py"
```

In heegner.py it's mainly a mixture of numerical noise and hash differences (this is on a 32-bit machine), but not all.  Details:

```
sage -t  "devel/sage-tests/sage/schemes/elliptic_curves/heegner.py"
**********************************************************************
File "/home/john/sage-4.3/devel/sage-tests/sage/schemes/elliptic_curves/heegner.py", line 2582:
    sage: hash(y)
Expected:
    -5236815264926108755
Got:
    733770669
**********************************************************************
File "/home/john/sage-4.3/devel/sage-tests/sage/schemes/elliptic_curves/heegner.py", line 2886:
    sage: hash(EllipticCurve('389a').heegner_point(-7,5))
Expected:
    ???                              
Got:
    733770669
**********************************************************************
File "/home/john/sage-4.3/devel/sage-tests/sage/schemes/elliptic_curves/heegner.py", line 3010:
    sage: P.numerical_approx()
Expected:
    (-3.41893279409096e-16 - 2.00036208715867e-16*I : 3.42282625853674e-16 + 2.00035300823576e-16*I : 1.00000000000000)
Got:
    (-3.41901661684534e-16 - 2.00073402416951e-16*I : 3.42011575310552e-16 + 2.00035300823576e-16*I : 1.00000000000000)
**********************************************************************
File "/home/john/sage-4.3/devel/sage-tests/sage/schemes/elliptic_curves/heegner.py", line 3032:
    sage: P = E.heegner_point(-19); y = P._trace_numerical_conductor_1(); y
Expected:
    (-9.52657106432722e-17 - 1.11102282864639e-16*I : -1.00000000000000 + 2.21773554381910e-16*I : 1.00000000000000)
Got:
    (-9.53960112385537e-17 - 1.11192361105451e-16*I : -1.00000000000000 + 2.21827764490534e-16*I : 1.00000000000000)
**********************************************************************
File "/home/john/sage-4.3/devel/sage-tests/sage/schemes/elliptic_curves/heegner.py", line 3039:
    sage: P = E.heegner_point(-68); P._trace_numerical_conductor_1()
Expected:
    (9.20680004622768e28 - 1.55670186905154e28*I : -2.76369626392776e43 + 7.09357788995373e42*I : 1.00000000000000)
Got:
    (9.22516515637394e28 - 1.48330779290131e28*I : -2.77483419563894e43 + 6.76511130239484e42*I : 1.00000000000000)
**********************************************************************
File "/home/john/sage-4.3/devel/sage-tests/sage/schemes/elliptic_curves/heegner.py", line 3106:
    sage: P.numerical_approx()
Expected:
    (-3.41893279409096e-16 - 2.00036208715867e-16*I : 3.42282625853674e-16 + 2.00035300823576e-16*I : 1.00000000000000)
Got:
    (-3.41901661684534e-16 - 2.00073402416951e-16*I : 3.42011575310552e-16 + 2.00035300823576e-16*I : 1.00000000000000)
**********************************************************************
File "/home/john/sage-4.3/devel/sage-tests/sage/schemes/elliptic_curves/heegner.py", line 3110:
    sage: P.numerical_approx(100)[0]
Expected:
    8.4419827889841225189186778139e-31 + 6.0876476174448148263632780203e-31*I
Got:
    8.4419827889841225189186778139e-31 + 6.0876476185623182015101748774e-31*I
**********************************************************************
File "/home/john/sage-4.3/devel/sage-tests/sage/schemes/elliptic_curves/heegner.py", line 3114:
    sage: P.numerical_approx()
Expected:
    (-6.68094502209485e-16 + 1.41421356237310*I : 1.00000000000000 - 1.41421356237309*I : 1.00000000000000)
Got:
    (-6.68276051475152e-16 + 1.41421356237310*I : 1.00000000000000 - 1.41421356237309*I : 1.00000000000000)
**********************************************************************
File "/home/john/sage-4.3/devel/sage-tests/sage/schemes/elliptic_curves/heegner.py", line 3123:
    sage: P.numerical_approx()
Expected:
    (4.08580183114324e28 + 1.50348132882460e28*I : -7.84283601876376e42 - 4.58366020722762e42*I : 1.00000000000000)
Got:
    (0 : 1.00000000000000 : 0)
**********************************************************************
File "/home/john/sage-4.3/devel/sage-tests/sage/schemes/elliptic_curves/heegner.py", line 3558:
    sage: P._trace_numerical_conductor_1()
Expected:
    (1.00000000000000 + 4.49510220712490e-16*I : 1.77646525961750e-16 - 4.49510220712490e-16*I : 1.00000000000000)
Got:
    (1.00000000000000 + 4.49618640929739e-16*I : 1.77809156287623e-16 - 4.49672851038363e-16*I : 1.00000000000000)
**********************************************************************
File "/home/john/sage-4.3/devel/sage-tests/sage/schemes/elliptic_curves/heegner.py", line 3939:
    sage: P.numerical_approx()
Expected:
    (-3.41893279409096e-16 - 2.00036208715867e-16*I : 3.42282625853674e-16 + 2.00035300823576e-16*I : 1.00000000000000)
Got:
    (-3.41901661684534e-16 - 2.00073402416951e-16*I : 3.42011575310552e-16 + 2.00035300823576e-16*I : 1.00000000000000)
**********************************************************************
File "/home/john/sage-4.3/devel/sage-tests/sage/schemes/elliptic_curves/heegner.py", line 3943:
    sage: P.numerical_approx(100)[0]
Expected:
    8.4419827889841225189186778139e-31 + 6.0876476174448148263632780203e-31*I
Got:
    8.4419827889841225189186778139e-31 + 6.0876476185623182015101748774e-31*I
**********************************************************************
File "/home/john/sage-4.3/devel/sage-tests/sage/schemes/elliptic_curves/heegner.py", line 3989:
    sage: P.point_exact()
Expected:
    Traceback (most recent call last):
    ...
    RuntimeError: insufficient precision to find exact point
Got:
    (0 : 1 : 0)
**********************************************************************
File "/home/john/sage-4.3/devel/sage-tests/sage/schemes/elliptic_curves/heegner.py", line 4082:
    sage: P.numerical_approx()
Expected:
    (6.00000000000000 + 8.04701070793563e-16*I : -15.0000000000000 - 2.96897922913431e-15*I : 1.00000000000000)
Got:
    (6.00000000000000 + 8.05181817160869e-16*I : -15.0000000000000 - 2.96897922913431e-15*I : 1.00000000000000)
**********************************************************************
File "/home/john/sage-4.3/devel/sage-tests/sage/schemes/elliptic_curves/heegner.py", line 605:
    sage: hash(G)
Expected:
    -6198252699510613726
Got:
    1905285410
**********************************************************************
File "/home/john/sage-4.3/devel/sage-tests/sage/schemes/elliptic_curves/heegner.py", line 607:
    sage: hash((G.field(), G.base_field()))
Expected:
    -6198252699510613726
Got:
    1905285410
**********************************************************************
File "/home/john/sage-4.3/devel/sage-tests/sage/schemes/elliptic_curves/heegner.py", line 6189:
    sage: P.numerical_approx()
Expected:
    (6.00000000000000 + 8.04701070793563e-16*I : -15.0000000000000 - 2.96897922913431e-15*I : 1.00000000000000)
Got:
    (6.00000000000000 + 8.05181817160869e-16*I : -15.0000000000000 - 2.96897922913431e-15*I : 1.00000000000000)
**********************************************************************
File "/home/john/sage-4.3/devel/sage-tests/sage/schemes/elliptic_curves/heegner.py", line 1253:
    sage: conj = G.complex_conjugation(); hash(conj)
Expected:
    1347197483068745902
Got:
    480045230
**********************************************************************
File "/home/john/sage-4.3/devel/sage-tests/sage/schemes/elliptic_curves/heegner.py", line 1447:
    sage: hash(s)
Expected:
    ??                      
Got:
    -1994029223
**********************************************************************
File "/home/john/sage-4.3/devel/sage-tests/sage/schemes/elliptic_curves/heegner.py", line 274:
    sage: hash(K5)
Expected:
    -3713088127102618519
Got:
    1817441385
**********************************************************************
File "/home/john/sage-4.3/devel/sage-tests/sage/schemes/elliptic_curves/heegner.py", line 276:
    sage: hash((-7,5))
Expected:
    -3713088127102618519
Got:
    1817441385
**********************************************************************
File "/home/john/sage-4.3/devel/sage-tests/sage/schemes/elliptic_curves/heegner.py", line 1688:
    sage: hash(H)
Expected:
    6187687223143458874
Got:
    -458201030
**********************************************************************
15 items had failures:
```

Incidentally that test takes 90s which is rather long (I have not tested it with "-long" yet!)

Some of this might be caused by the fact that I have a new version of lcalc (from reviewing another ticket) although this is a fresh clone?

```
sage -t  "devel/sage-tests/sage/schemes/elliptic_curves/lseries_ell.py"
**********************************************************************
File "/home/john/sage-4.3/devel/sage-tests/sage/schemes/elliptic_curves/lseries_ell.py", line 258:
    sage: E.lseries().zeros_in_interval(6, 10, 0.1)      # long
Exception raised:
    Traceback (most recent call last):
      File "/home/john/sage-4.3/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/john/sage-4.3/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/john/sage-4.3/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_10[3]>", line 1, in <module>
        E.lseries().zeros_in_interval(Integer(6), Integer(10), RealNumber('0.1'))      # long###line 258:
    sage: E.lseries().zeros_in_interval(6, 10, 0.1)      # long
      File "/home/john/sage-4.3/local/lib/python/site-packages/sage/schemes/elliptic_curves/lseries_ell.py", line 262, in zeros_in_interval
        return lcalc.zeros_in_interval(x, y, stepsize, L=self.__E)
      File "/home/john/sage-4.3/local/lib/python/site-packages/sage/lfunctions/lcalc.py", line 162, in zeros_in_interval
        return [tuple([RR(z) for z in t.split()]) for t in X.split('\n')]
      File "parent.pyx", line 538, in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:4956)
      File "coerce_maps.pyx", line 82, in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:3142)
      File "coerce_maps.pyx", line 77, in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:3040)
      File "real_mpfr.pyx", line 384, in sage.rings.real_mpfr.RealField._element_constructor_ (sage/rings/real_mpfr.c:5053)
      File "real_mpfr.pyx", line 1009, in sage.rings.real_mpfr.RealNumber._set (sage/rings/real_mpfr.c:8794)
    TypeError: Unable to convert x (='You') to real number.
**********************************************************************
File "/home/john/sage-4.3/devel/sage-tests/sage/schemes/elliptic_curves/lseries_ell.py", line 311:
    sage: print "ignore this";  E.lseries().twist_values(1, -12, -4)    # slightly random output depending on architecture
Exception raised:
    Traceback (most recent call last):
      File "/home/john/sage-4.3/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/john/sage-4.3/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/john/sage-4.3/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_12[3]>", line 1, in <module>
        print "ignore this";  E.lseries().twist_values(Integer(1), -Integer(12), -Integer(4))    # slightly random output depending on architecture###line 311:
    sage: print "ignore this";  E.lseries().twist_values(1, -12, -4)    # slightly random output depending on architecture
      File "/home/john/sage-4.3/local/lib/python/site-packages/sage/schemes/elliptic_curves/lseries_ell.py", line 321, in twist_values
        return lcalc.twist_values(s - RationalField()('1/2'), dmin, dmax, L=self.__E)
      File "/home/john/sage-4.3/local/lib/python/site-packages/sage/lfunctions/lcalc.py", line 296, in twist_values
        d,x,y = a.split()
    ValueError: too many values to unpack
**********************************************************************
File "/home/john/sage-4.3/devel/sage-tests/sage/schemes/elliptic_curves/lseries_ell.py", line 343:
    sage: E.lseries().twist_zeros(3, -4, -3)         # long
Exception raised:
    Traceback (most recent call last):
      File "/home/john/sage-4.3/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/john/sage-4.3/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/john/sage-4.3/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_13[3]>", line 1, in <module>
        E.lseries().twist_zeros(Integer(3), -Integer(4), -Integer(3))         # long###line 343:
    sage: E.lseries().twist_zeros(3, -4, -3)         # long
      File "/home/john/sage-4.3/local/lib/python/site-packages/sage/schemes/elliptic_curves/lseries_ell.py", line 347, in twist_zeros
        return lcalc.twist_zeros(n, dmin, dmax, L=self.__E)
      File "/home/john/sage-4.3/local/lib/python/site-packages/sage/lfunctions/lcalc.py", line 342, in twist_zeros
        d, x = a.split()
    ValueError: too many values to unpack
**********************************************************************
File "/home/john/sage-4.3/devel/sage-tests/sage/schemes/elliptic_curves/lseries_ell.py", line 226:
    sage: E.lseries().zeros(2)
Exception raised:
    Traceback (most recent call last):
      File "/home/john/sage-4.3/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/john/sage-4.3/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/john/sage-4.3/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_9[3]>", line 1, in <module>
        E.lseries().zeros(Integer(2))###line 226:
    sage: E.lseries().zeros(2)
      File "/home/john/sage-4.3/local/lib/python/site-packages/sage/schemes/elliptic_curves/lseries_ell.py", line 236, in zeros
        return lcalc.zeros(n, L=self.__E)
      File "/home/john/sage-4.3/local/lib/python/site-packages/sage/lfunctions/lcalc.py", line 126, in zeros
        return [RR(z) for z in X.split()]
      File "parent.pyx", line 538, in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:4956)
      File "coerce_maps.pyx", line 82, in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:3142)
      File "coerce_maps.pyx", line 77, in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:3040)
      File "real_mpfr.pyx", line 384, in sage.rings.real_mpfr.RealField._element_constructor_ (sage/rings/real_mpfr.c:5053)
      File "real_mpfr.pyx", line 1009, in sage.rings.real_mpfr.RealNumber._set (sage/rings/real_mpfr.c:8794)
    TypeError: Unable to convert x (='You') to real number.
**********************************************************************
4 items had failures:
```


The perennial noise issues in period_lattice.py:

```
sage -t  "devel/sage-tests/sage/schemes/elliptic_curves/period_lattice.py"
**********************************************************************
File "/home/john/sage-4.3/devel/sage-tests/sage/schemes/elliptic_curves/period_lattice.py", line 1111:
    sage: L.elliptic_exponential(z)
Expected:
    (1.06844510091205e-15 : 2.00000000000000 : 1.00000000000000)
Got:
    (1.06663809729124e-15 : 2.00000000000000 : 1.00000000000000)
**********************************************************************
File "/home/john/sage-4.3/devel/sage-tests/sage/schemes/elliptic_curves/period_lattice.py", line 1119:
    sage: L.elliptic_exponential(z)
Expected:
    (-1.0773137765183430387827930528831385613292568270511670949401e-60 : 2.0000000000000000000000000000000000000000000000000000000000 : 1.0000000000000000000000000000000000000000000000000000000000)
Got:
    (-1.0773140994173990301711557437150639986876632707626675784012e-60 : 2.0000000000000000000000000000000000000000000000000000000000 : 1.0000000000000000000000000000000000000000000000000000000000)
```


Lastly, in ell_rational_field.py, we have some more of the same plus a very weird issue with "rubenstein":

```
sage -t  "devel/sage-tests/sage/schemes/elliptic_curves/ell_rational_field.py"
**********************************************************************
File "/home/john/sage-4.3/devel/sage-tests/sage/schemes/elliptic_curves/ell_rational_field.py", line 1334:
    sage: E.analytic_rank(algorithm='rubinstein')
Exception raised:
    Traceback (most recent call last):
      File "/home/john/sage-4.3/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/john/sage-4.3/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/john/sage-4.3/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_28[4]>", line 1, in <module>
        E.analytic_rank(algorithm='rubinstein')###line 1334:
    sage: E.analytic_rank(algorithm='rubinstein')
      File "/home/john/sage-4.3/local/lib/python/site-packages/sage/schemes/elliptic_curves/ell_rational_field.py", line 1363, in analytic_rank
        raise RuntimeError, "unable to compute analytic rank using rubinstein algorithm ('%s')"%msg
    RuntimeError: unable to compute analytic rank using rubinstein algorithm ('unable to convert x (=eed to uncomment the line: PARI_DEFINE = -DINCLUDE_PARI
    in the Makefile and do: 'make clean', then 'make' if you wish to use
    elliptic curve L-functions. Requires that you already have pari installed
    on your machine.) to an integer')
**********************************************************************
File "/home/john/sage-4.3/devel/sage-tests/sage/schemes/elliptic_curves/ell_rational_field.py", line 1340:
    sage: E.analytic_rank(algorithm='all')
Exception raised:
    Traceback (most recent call last):
      File "/home/john/sage-4.3/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/john/sage-4.3/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/john/sage-4.3/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_28[6]>", line 1, in <module>
        E.analytic_rank(algorithm='all')###line 1340:
    sage: E.analytic_rank(algorithm='all')
      File "/home/john/sage-4.3/local/lib/python/site-packages/sage/schemes/elliptic_curves/ell_rational_field.py", line 1372, in analytic_rank
        self.analytic_rank('rubinstein'), self.analytic_rank('sympow')]))
      File "/home/john/sage-4.3/local/lib/python/site-packages/sage/schemes/elliptic_curves/ell_rational_field.py", line 1363, in analytic_rank
        raise RuntimeError, "unable to compute analytic rank using rubinstein algorithm ('%s')"%msg
    RuntimeError: unable to compute analytic rank using rubinstein algorithm ('unable to convert x (=eed to uncomment the line: PARI_DEFINE = -DINCLUDE_PARI
    in the Makefile and do: 'make clean', then 'make' if you wish to use
    elliptic curve L-functions. Requires that you already have pari installed
    on your machine.) to an integer')
**********************************************************************
File "/home/john/sage-4.3/devel/sage-tests/sage/schemes/elliptic_curves/ell_rational_field.py", line 1347:
    sage: EllipticCurve([1234567,89101112]).analytic_rank(algorithm='rubinstein')
Expected:
    Traceback (most recent call last):
    ...
    RuntimeError: unable to compute analytic rank using rubinstein algorithm ('unable to convert x (= 6.19283e+19 and is too large) to an integer')
Got:
    Traceback (most recent call last):
      File "/home/john/sage-4.3/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/john/sage-4.3/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/john/sage-4.3/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_28[7]>", line 1, in <module>
        EllipticCurve([Integer(1234567),Integer(89101112)]).analytic_rank(algorithm='rubinstein')###line 1347:
    sage: EllipticCurve([1234567,89101112]).analytic_rank(algorithm='rubinstein')
      File "/home/john/sage-4.3/local/lib/python/site-packages/sage/schemes/elliptic_curves/ell_rational_field.py", line 1363, in analytic_rank
        raise RuntimeError, "unable to compute analytic rank using rubinstein algorithm ('%s')"%msg
    RuntimeError: unable to compute analytic rank using rubinstein algorithm ('unable to convert x (=eed to uncomment the line: PARI_DEFINE = -DINCLUDE_PARI
    in the Makefile and do: 'make clean', then 'make' if you wish to use
    elliptic curve L-functions. Requires that you already have pari installed
    on your machine.) to an integer')
**********************************************************************
File "/home/john/sage-4.3/devel/sage-tests/sage/schemes/elliptic_curves/ell_rational_field.py", line 2901:
    sage: E.elliptic_exponential(z)
Expected:
    (-7.4445166218537606141680653627e-30 : 2.0000000000000000000000000000 : 1.0000000000000000000000000000)
Got:
    (-7.4445166228333392396252290308e-30 : 2.0000000000000000000000000000 : 1.0000000000000000000000000000)
**********************************************************************
File "/home/john/sage-4.3/devel/sage-tests/sage/schemes/elliptic_curves/ell_rational_field.py", line 2904:
    sage: E.elliptic_exponential(z)
Expected:
    (-1.0773137765183430387827930528831385613292568270511670949401e-60 : 2.0000000000000000000000000000000000000000000000000000000000 : 1.0000000000000000000000000000000000000000000000000000000000)
Got:
    (-1.0773140994173990301711557437150639986876632707626675784012e-60 : 2.0000000000000000000000000000000000000000000000000000000000 : 1.0000000000000000000000000000000000000000000000000000000000)
**********************************************************************
File "/home/john/sage-4.3/devel/sage-tests/sage/schemes/elliptic_curves/ell_rational_field.py", line 2916:
    sage: E.elliptic_exponential(P.elliptic_logarithm())
Expected:
    (-1.0000000000000000000000000000 + 4.3761255281366123414673626379e-31*I : 1.0000000000000000000000000000 - 1.4587084969798853407242847702e-31*I : 1.0000000000000000000000000000)
Got:
    (-1.0000000000000000000000000000 + 4.3761255295105644085291631657e-31*I : 1.0000000000000000000000000000 - 1.4587084969798853407242847702e-31*I : 1.0000000000000000000000000000)
**********************************************************************
2 items had failures:
   3 of   9 in __main__.example_28
   3 of  22 in __main__.example_61
***Test Failed*** 6 failures.
For whitespace errors, see the file /home/john/.sage//tmp/.doctest_ell_rational_field.py
	 [69.0 s]
```


So the conclusion is, regretfully,  "needs work", though the work that needs doing is trivial compared with what has been done already (which is probably worth a PhD thesis for someone!).


---

Attachment

apply this and the previous patch; then this should past all tests on 32-bit as well as 64-bit.


---

Comment by was created at 2010-01-13 15:12:18

Changing status from needs_work to needs_review.


---

Comment by was created at 2010-01-13 15:14:27

I posted a new patch fixing all the issues above, except possibly the "very weird" ell_rational_field issue.  I couldn't replicate that on any test machine yet. 

I also didn't carefully reformat the docstrings.  Which ones aren't formatted correctly?  I thought I had got them right.


---

Attachment

apply instead of previous one


---

Comment by cremona created at 2010-01-13 16:23:55

cremona>> The patches say they are based on 4.3 rather than 4.3.1.  the first
>> one produced one failed hunk when I applied it to 4.3.1 (see attached
>> -- looks minor).
>
was> That's in a doctest for something probably unrelated, so can be safely
> ignored for refereeing.

Ignoring that, there was just one small thing (testing on 64-bit), namely

```
File "/home/jec/sage-4.3.1.alpha1/devel/sage-tests/sage/schemes/elliptic_curves/heegner.py", line 277:
    sage: hash((-7,5))
Expected:
    -3713088127102618519     
    1817441385
Got:
    -3713088127102618519
```

which is just because someone forgot to add the tag # 32-bit.  I added that by editing the patch, and the corrected version is now attached here.

So: positive review on 64-bit.  I'll test on 32-bit when I get home (leaving now, hope I do not get buried in the snow...)


---

Comment by cremona created at 2010-01-13 18:20:58

Apply after previous (reviewer's patch fixing some docstring issues)


---

Comment by cremona created at 2010-01-13 18:23:04

Changing status from needs_review to positive_review.


---

Attachment

Positive review after testing on 32-bit, and also fixing lots of documentation glitches (in the reviewer's patch).  These were mainly found by actually running "sage -docbuild all html" and reading the error messages (hint hint).  Most common error was double :: where they shouldn't be.

Great work!


---

Comment by rlm created at 2010-01-14 01:21:13

Applied:

```
trac-6616-everything_rebased_against_4.3.patch
trac-6616-everything_rebased_against_4.3-part2.2.patch
trac-6616-review.patch
```



---

Comment by rlm created at 2010-01-14 01:21:13

Resolution: fixed
