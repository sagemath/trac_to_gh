# Issue 6329: optional doctest failure -- bad data type breakage in the sage-->magma interface

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-06-16 15:06:55

Assignee: tbd


```
sage -t -long --optional devel/sage/sage/rings/rational.pyx
**********************************************************************
File "/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/rings/rational.pyx", line 3087:
    sage: magma(3/1).Type()             # optional
Expected:
    FldRatElt
Got:
    RngIntElt
**********************************************************************
1 items had failures:
   1 of   5 in __main__.example_84
***Test Failed*** 1 failures.
```



---

Comment by was created at 2009-06-16 15:10:31

More failures:

```
sage -t -long --optional devel/sage/sage/schemes/hyperelliptic_curves/hyperelliptic_g2_generic.py
**********************************************************************
File "/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/schemes/hyperelliptic_curves/hyperelliptic_g2_generic.py", line 218:
    sage: magma(HyperellipticCurve(f)).IgusaClebschInvariants() # optional - magma
Expected:
    [ 0, -2048/375, -4096/25, -4881645568/84375 ]
Got:
    [ -640, -20480, 1310720, 52160364544 ]
**********************************************************************
File "/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/schemes/hyperelliptic_curves/hyperelliptic_g2_generic.py", line 220:
    sage: magma(HyperellipticCurve(f(2*x))).IgusaClebschInvariants() # optional - magma
Expected:
    [ 0, -8388608/375, -1073741824/25, -5241627016305836032/84375 ]
Got:
    [ -40960, -83886080, 343597383680, 56006764965979488256 ]
**********************************************************************
File "/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/schemes/hyperelliptic_curves/hyperelliptic_g2_generic.py", line 222:
    sage: magma(HyperellipticCurve(f, x)).IgusaClebschInvariants() # optional - magma
Expected:
    [ -8/15, 17504/5625, -23162896/140625, -420832861216768/7119140625 ]
Got:
    [ -640, 17920, -1966656, 52409511936 ]
**********************************************************************
File "/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/schemes/hyperelliptic_curves/hyperelliptic_g2_generic.py", line 224:
    sage: magma(HyperellipticCurve(f(2*x), 2*x)).IgusaClebschInvariants() # optional - magma
Expected:
    [ -512/15, 71696384/5625, -6072014209024/140625, -451865844002031331704832/7119140625 ]
Got:
    [ -40960, 73400320, -515547070464, 56274284941110411264 ]
**********************************************************************
1 items had failures:
   4 of  12 in __main__.example_7
***Test Failed*** 4 failures.

```



---

Comment by was created at 2009-06-16 15:19:18

More failures:

```
sage -t -long --optional devel/sage/sage/interfaces/magma.py
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
      File "<doctest __main__.example_20[2]>", line 1, in <module>
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
      File "<doctest __main__.example_20[3]>", line 1, in <module>
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
    Loading "/scratch/wstein/sage//temp/sage.math.washington.edu/31604/a.m"
    hi
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
File "/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/interfaces/magma.py", line 463:
    sage: magma.eval("a := %s;"%(10^10000))    # optional - magma
Expected:
    "
Got:
    ''
**********************************************************************
4 items had failures:
   2 of   4 in __main__.example_20
   1 of   5 in __main__.example_22
   2 of  28 in __main__.example_64
   1 of   4 in __main__.example_9
***Test Failed*** 6 failures.
For whitespace errors, see the file /home/wstein/build/sage-4.0.2.alpha3/tmp/.doctest_magma.py
	 [32.9 s]

```



---

Attachment


---

Comment by mariah created at 2011-05-25 18:35:39

[attachment: trac_6329.patch] corrects the test output in the problem in the description.  The Got output is correct - there is *not* a breakage in the sage<-->magma interface.  'magma(3/1)' returns the integer '3' (after coercion), so Type() returns that
the value is an integer.

The other two reports of failures are no longer valid, as they seem to already be fixed in sage-4.7.rc4.


---

Comment by mariah created at 2011-05-25 18:35:39

Changing status from new to needs_review.


---

Comment by mariah created at 2011-05-25 18:35:39

Changing priority from major to minor.


---

Comment by kcrisman created at 2011-06-14 03:11:39

Changing component from optional packages to interfaces.


---

Comment by mhansen created at 2011-08-23 01:15:48

Changing status from needs_review to needs_info.


---

Comment by mhansen created at 2011-08-23 01:15:48

It seems like the correct fix would be to always put the denominator in the _magma_init_ method.


```
        s = self.numerator()._magma_init_(magma)
        s += '/' + self.denominator()._magma_init_(magma)
        return s
```


instead of 


```
        s = self.numerator()._magma_init_(magma)
        if not self.is_integral():
            s += '/' + self.denominator()._magma_init_(magma)
        return s

```



---

Comment by was created at 2011-08-23 05:04:52

Mhansen, you're right, the patch Mariah posted is wrong.   I'll post a correct patch, and hopefully you can review it.


---

Attachment

apply only this one


---

Comment by was created at 2011-08-23 05:39:46

Changing status from needs_info to needs_review.


---

Comment by was created at 2011-08-23 05:39:46

Patch up that is ready for review (the .2 one).  This was a result of some overzealous optimization on my part a few years ago.  Reverting this change will barely slow things down.


---

Comment by mhansen created at 2011-08-23 05:49:03

We should add a doctest for the integral case.


---

Comment by was created at 2011-08-24 04:49:28

Replying to [comment:8 mhansen]:
> We should add a doctest for the integral case.

What do you mean by this?  If you mean `sage: magma(3/1).Type()`, which is in the ticket description, then there is *already* a doctest for this case, which is how we found this bug in the first place. 

Or do you mean adding something to integer.pyx???


---

Comment by was created at 2011-08-24 23:36:45

Changing keywords from "" to "sd32".


---

Comment by mhansen created at 2011-08-24 23:40:24

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2011-08-24 23:40:24

I was thinking about the old code and verifying that the "is_integral" code path worked (since that test was missing before).  However, it is obviously not needed now.

Positive review.


---

Comment by leif created at 2011-09-12 19:27:00

Resolution: fixed


---

Comment by was created at 2012-01-22 21:57:34

Shame on the idiot who wrote this with no tests... and who forgot that there are optional tests all over Sage that would be broken by this: see #12006, where I'm doing my penance.
