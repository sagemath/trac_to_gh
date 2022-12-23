# Issue 6284: fix the numerous broken optional magma doctests

Issue created by migration from https://trac.sagemath.org/ticket/6284

Original creator: was

Original creation time: 2009-06-14 10:36:29

Assignee: tbd


```
wstein@sage:~/build/sage-4.0.2.alpha3$  ./sage -tp 30 --only_optional=magma devel/sage/sage/
...

        sage -t --only_optional=magma devel/sage/sage/symbolic/expression.pyx # 1 doctests failed
        sage -t --only_optional=magma devel/sage/sage/schemes/hyperelliptic_curves/hyperelliptic_g2_generic.py # 4 doctests fa
iled
        sage -t --only_optional=magma devel/sage/sage/interfaces/magma.py # 6 doctests failed
```


The actual failures

```
sage -t --only_optional=magma devel/sage/sage/symbolic/expression.pyx
**********************************************************************
File "/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/symbolic/expression.pyx", line 473:
    sage: magma(f)                         # optional - magma
Expected:
    sin(cos(x^2) + log(x))
Got:
    sin(log(x) + cos(x^2))
**********************************************************************
1 items had failures:
   1 of   7 in __main__.example_0


sage -t --only_optional=magma devel/sage/sage/schemes/hyperelliptic_curves/hyperelliptic_g2_generic.py
**********************************************************************
File "/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/schemes/hyperelliptic_curves/hyperelliptic_g2_generic.py",
line 218:
    sage: magma(HyperellipticCurve(f)).IgusaClebschInvariants() # optional - magma
Expected:
    [ 0, -2048/375, -4096/25, -4881645568/84375 ]
Got:
    [ -640, -20480, 1310720, 52160364544 ]
**********************************************************************
File "/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/schemes/hyperelliptic_curves/hyperelliptic_g2_generic.py",
line 220:
    sage: magma(HyperellipticCurve(f(2*x))).IgusaClebschInvariants() # optional - magma
Expected:
    [ 0, -8388608/375, -1073741824/25, -5241627016305836032/84375 ]
Got:
    [ -40960, -83886080, 343597383680, 56006764965979488256 ]
**********************************************************************
File "/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/schemes/hyperelliptic_curves/hyperelliptic_g2_generic.py",
line 222:
    sage: magma(HyperellipticCurve(f, x)).IgusaClebschInvariants() # optional - magma
Expected:
    [ -8/15, 17504/5625, -23162896/140625, -420832861216768/7119140625 ]
Got:
    [ -640, 17920, -1966656, 52409511936 ]
**********************************************************************
File "/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/schemes/hyperelliptic_curves/hyperelliptic_g2_generic.py",
line 224:
    sage: magma(HyperellipticCurve(f(2*x), 2*x)).IgusaClebschInvariants() # optional - magma
Expected:
    [ -512/15, 71696384/5625, -6072014209024/140625, -451865844002031331704832/7119140625 ]
Got:
    [ -40960, 73400320, -515547070464, 56274284941110411264 ]
**********************************************************************
1 items had failures:
   4 of  12 in __main__.example_3
***Test Failed*** 4 failures.


sage -t --only_optional=magma devel/sage/sage/interfaces/magma.py
**********************************************************************
File "/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/interfaces/magma.py", line 856:
    sage: magma.attach('%s/data/extcode/magma/sage/basic.m'%Sage_ROOT)    # optional - magma
Exception raised:
    Traceback (most recent call last):
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_14[2]>", line 1, in <module>
        magma.attach('%s/data/extcode/magma/sage/basic.m'%Sage_ROOT)    # optional - magma###line 856:
    sage: magma.attach('%s/data/extcode/magma/sage/basic.m'%Sage_ROOT)    # optional - magma
    NameError: name 'Sage_ROOT' is not defined
**********************************************************************
File "/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/interfaces/magma.py", line 860:
    sage: magma.attach('%s/data/extcode/magma/sage/basic2.m'%Sage_ROOT)     # optional - magma
Expected:
    Traceback (most recent call last):
    ...
    RuntimeError: Error evaluating Magma code...
Got:
    Traceback (most recent call last):
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_14[3]>", line 1, in <module>
        magma.attach('%s/data/extcode/magma/sage/basic2.m'%Sage_ROOT)     # optional - magma###line 860:
    sage: magma.attach('%s/data/extcode/magma/sage/basic2.m'%Sage_ROOT)     # optional - magma
    NameError: name 'Sage_ROOT' is not defined
**********************************************************************
File "/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/interfaces/magma.py", line 917:
    sage: print magma.load(SAGE_TMP + 'a.m')      # optional - magma
Expected:
    Loading ".../.sage//temp/.../a.m"
    hi
Got:
    Loading "/scratch/wstein/sage//temp/sage.math.washington.edu/19243/a.m"
    hi
**********************************************************************
File "/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/interfaces/magma.py", line 463:
    sage: magma.eval("a := %s;"%(10^10000))    # optional - magma
Expected:
    "
Got:
    ''
**********************************************************************
**********************************************************************
File "/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/interfaces/magma.py", line 2148:
    sage: magma.eval('R<x> := PolynomialRing(RationalField()); f := (x-17/2)^3;')     # optional - magma
Expected:
    "
Got:
    ''
**********************************************************************
File "/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/interfaces/magma.py", line 2160:
    sage: magma.eval('K<a> := CyclotomicField(11)')       # optional - magma
Expected:
    "
Got:
    ''
**********************************************************************
4 items had failures:
   2 of   4 in __main__.example_14
   1 of   5 in __main__.example_16
   1 of   4 in __main__.example_3
   2 of  28 in __main__.example_47
***Test Failed*** 6 failures.
```


}}}




---

Comment by mariah created at 2011-05-24 20:17:11

I believe this ticket can be closed as it has been superceded by #7870.


---

Comment by mariah created at 2011-05-24 20:17:11

Changing status from new to needs_review.


---

Comment by was created at 2011-08-23 05:19:29

Resolution: duplicate


---

Comment by was created at 2011-08-24 23:44:49

Changing keywords from "" to "sd32".
