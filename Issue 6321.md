# Issue 6321: optional doctest failure -- sympow

Issue created by migration from https://trac.sagemath.org/ticket/6321

Original creator: was

Original creation time: 2009-06-16 14:51:52

Assignee: tbd


```
sage -t -long --optional devel/sage/sage/lfunctions/sympow.py
**********************************************************************
File "/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/lfunctions/sympow.py", line 127:
    sage: a = sympow.L(EllipticCurve('11a'), 2, 16); a   # optional
Expected:
    '1.057599244590958E+00'
Got:
    "Inertia Group is  C1 MULTIPLICATIVE REDUCTION\nConductor is 11\n**ERROR** P02L not found in param_data file\nIt can be added with './sympow -new_data 2'"
**********************************************************************
File "/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/lfunctions/sympow.py", line 129:
    sage: RR(a)                    # optional -- requires precomputations
Exception raised:
    Traceback (most recent call last):
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_4[3]>", line 1, in <module>
        RR(a)                    # optional -- requires precomputations###line 129:
    sage: RR(a)                    # optional -- requires precomputations
      File "parent.pyx", line 323, in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:4130)
      File "coerce_maps.pyx", line 82, in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:3058)
      File "coerce_maps.pyx", line 77, in sage.structure.coerce_maps._call_ (sage/structure/coerce_maps.c:2949)
      File "real_mpfr.pyx", line 379, in sage.rings.real_mpfr.RealField._element_constructor_ (sage/rings/real_mpfr.c:5241)
      File "real_mpfr.pyx", line 983, in sage.rings.real_mpfr.RealNumber._set (sage/rings/real_mpfr.c:8892)
    TypeError: Unable to convert x (='InertiaGroupisC1MULTIPLICATIVEREDUCTION
    Conductoris11
    **ERROR**P02Lnotfoundinparam_datafile
    Itcanbeaddedwith'./sympow-new_data2'') to real number.
**********************************************************************
1 items had failures:
   2 of   4 in __main__.example_4
***Test Failed*** 2 failures.
For whitespace errors, see the file /home/wstein/build/sage-4.0.2.alpha3/tmp/.doctest_sympow.py
	 [6.5 s]
```



---

Comment by was created at 2009-06-16 14:52:13

More failures:

```
sage -t -long --optional devel/sage/sage/schemes/elliptic_curves/lseries_ell.py
**********************************************************************
File "/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/schemes/elliptic_curves/lseries_ell.py", line 165:
    sage: a      # optional
Expected:
    '2.492262044273650E+00'
Got:
    "Inertia Group is  C1 MULTIPLICATIVE REDUCTION\nConductor is 37\n**ERROR** P02L not found in param_data file\nIt can be added with './sympow -new_data 2'"
**********************************************************************
File "/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/schemes/elliptic_curves/lseries_ell.py", line 167:
    sage: RR(a)                      # optional
Exception raised:
    Traceback (most recent call last):
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_7[5]>", line 1, in <module>
        RR(a)                      # optional###line 167:
    sage: RR(a)                      # optional
      File "parent.pyx", line 323, in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:4130)
      File "coerce_maps.pyx", line 82, in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:3058)
      File "coerce_maps.pyx", line 77, in sage.structure.coerce_maps._call_ (sage/structure/coerce_maps.c:2949)
      File "real_mpfr.pyx", line 379, in sage.rings.real_mpfr.RealField._element_constructor_ (sage/rings/real_mpfr.c:5241)
      File "real_mpfr.pyx", line 983, in sage.rings.real_mpfr.RealNumber._set (sage/rings/real_mpfr.c:8892)
    TypeError: Unable to convert x (='InertiaGroupisC1MULTIPLICATIVEREDUCTION
    Conductoris37
    **ERROR**P02Lnotfoundinparam_datafile
    Itcanbeaddedwith'./sympow-new_data2'') to real number.
**********************************************************************
File "/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/schemes/elliptic_curves/lseries_ell.py", line 193:
    sage: print E.lseries().sympow_derivs(1,16,2)      # optional -- requires precomputing "sympow('-new_data 2')"
Expected:
    sympow 1.018 RELEASE  (c) Mark Watkins --- see README and COPYING for details
    Minimal model of curve  is [0,0,1,-1,0]
    At 37: Inertia Group is  C1 MULTIPLICATIVE REDUCTION
    Conductor is 37
    sp 1: Conductor at 37 is 1+0, root number is 1
    sp 1: Euler factor at 37 is 1+1*x
    1st sym power conductor is 37, global root number is -1
    NT 1d0: 35
    NT 1d1: 32
    NT 1d2: 28
    Maximal number of terms is 35
    Done with small primes 1049
    Computed:  1d0  1d1  1d2
    Checked out:  1d1
     1n0: 3.837774351482055E-01
     1w0: 3.777214305638848E-01
     1n1: 3.059997738340522E-01
     1w1: 3.059997738340524E-01
     1n2: 1.519054910249753E-01
     1w2: 1.545605024269432E-01
Got:
    sympow 1.018 RELEASE  (c) Mark Watkins --- see README and COPYING for details
    Minimal model of curve  is [0,0,1,-1,0]
    At 37: Inertia Group is  C1 MULTIPLICATIVE REDUCTION
    Conductor is 37
    **ERROR** P01E not found in param_data file
    It can be added with sympow('-new_data 1d0')
**********************************************************************
2 items had failures:
   2 of   6 in __main__.example_7
   1 of   4 in __main__.example_8
***Test Failed*** 3 failures.
```



---

Comment by jdemeyer created at 2015-09-06 17:52:45


```
$ ./sage -t --long --optional=all src/sage/lfunctions/sympow.py
too many failed tests, not using stored timings
Running doctests with ID 2015-09-06-19-51-28-9336e066.
Git branch: t/19146/brial_python
Using --optional=all
Doctesting 1 file.
sage -t --long src/sage/lfunctions/sympow.py
    [13 tests, 3.39 s]
----------------------------------------------------------------------
All tests passed!
----------------------------------------------------------------------
Total time for all tests: 3.4 seconds
    cpu time: 0.1 seconds
    cumulative wall time: 3.4 seconds
```



---

Comment by jdemeyer created at 2015-09-06 17:52:45

Changing status from new to needs_review.


---

Comment by jdemeyer created at 2015-09-06 17:52:51

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2015-09-12 13:57:49

Resolution: worksforme
