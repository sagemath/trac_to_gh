# Issue 6506: further numpy type conversions

Issue created by migration from https://trac.sagemath.org/ticket/6506

Original creator: robertwb

Original creation time: 2009-07-10 06:53:49

Assignee: jkantor

CC:  cwitty

Followup to #5081.


---

Attachment

Carl, as one of the resident experts on precision issues, could you glance at the last part of this patch, which touches real_mpfr.pyx and seems to deal with precision issues?


---

Comment by jason created at 2009-07-19 03:38:08

apply on top of previous patch


---

Attachment

I posted a patch which fixes lots of the documentation errors on #5081.  There are still some problems.

  * printing issues, presumably because of the work from the patch on this ticket on the precision code.  It appears there is one less zero printed in numbers.


```
$ sage -t complex_number.pyx 
sage -t  "devel/sage-main/sage/rings/complex_number.pyx"    
**********************************************************************
File "/home/grout/sage/devel/sage-main/sage/rings/complex_number.pyx", line 1917:
    sage: ComplexNumber(1.000000000000000000000000000,2)
Expected:
    1.000000000000000000000000000 + 2.000000000000000000000000000*I
Got:
    1.00000000000000000000000000 + 2.00000000000000000000000000*I
**********************************************************************
File "/home/grout/sage/devel/sage-main/sage/rings/complex_number.pyx", line 1919:
    sage: ComplexNumber(1,2.000000000000000000000)
Expected:
    1.000000000000000000000 + 2.000000000000000000000*I
Got:
    1.00000000000000000000 + 2.00000000000000000000*I
**********************************************************************
1 items had failures:
   2 of   9 in __main__.example_74
***Test Failed*** 2 failures.
For whitespace errors, see the file /home/grout/sage/tmp/.doctest_complex_number.py
	 [11.8 s]
exit code: 1024
 
----------------------------------------------------------------------
The following tests failed:


	sage -t  "devel/sage-main/sage/rings/complex_number.pyx"
Total time for all tests: 11.8 seconds


$ sage -t real_mpfr.pyx 
sage -t  "devel/sage-main/sage/rings/real_mpfr.pyx"         
**********************************************************************
File "/home/grout/sage/devel/sage-main/sage/rings/real_mpfr.pyx", line 4299:
    sage: RealNumber('1.0000000000000000000000000000000000')
Expected:
    1.0000000000000000000000000000000000
Got:
    1.000000000000000000000000000000000
**********************************************************************
1 items had failures:
   1 of   9 in __main__.example_126
***Test Failed*** 1 failures.
For whitespace errors, see the file /home/grout/sage/tmp/.doctest_real_mpfr.py
	 [15.1 s]
exit code: 1024
 
----------------------------------------------------------------------
The following tests failed:


	sage -t  "devel/sage-main/sage/rings/real_mpfr.pyx"
Total time for all tests: 15.1 seconds



```



  * Another error pointed out on #5081 that is deeper than a printing issue.  There appears to be a bug in the code---the same variable is used in a list comprehension as is used in an enclosing loop.  I rewrote some of the code to not use some numpy and string parsing, instead using python zip and string join methods.  However, there still seems to be an error.  Can someone more familiar with the code look at this?  I think all of these errors stem from the same problem.


```
$ sage -t rings/number_field/totallyreal_rel.py 
sage -t  "devel/sage-main/sage/rings/number_field/totallyreal_rel.py"
**********************************************************************
File "/home/grout/sage/devel/sage-main/sage/rings/number_field/totallyreal_rel.py", line 156:
    sage: T = sage.rings.number_field.totallyreal_rel.tr_data_rel(F, 2, 2000)
Exception raised:
    Traceback (most recent call last):
      File "/home/grout/sage/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/grout/sage/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/grout/sage/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_3[3]>", line 1, in <module>
        T = sage.rings.number_field.totallyreal_rel.tr_data_rel(F, Integer(2), Integer(2000))###line 156:
    sage: T = sage.rings.number_field.totallyreal_rel.tr_data_rel(F, 2, 2000)
      File "/home/grout/sage/local/lib/python/site-packages/sage/rings/number_field/totallyreal_rel.py", line 200, in __init__
        anm1s[i] += sum([m*Z_Fbasis[i]*adj[i].__int__()//adj[self.d].__int__() for i in range(self.d)])
    IndexError: list index out of range
**********************************************************************
File "/home/grout/sage/devel/sage-main/sage/rings/number_field/totallyreal_rel.py", line 568:
    sage: enumerate_totallyreal_fields_rel(F, 2, 2000)
Exception raised:
    Traceback (most recent call last):
      File "/home/grout/sage/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/grout/sage/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/grout/sage/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_5[4]>", line 1, in <module>
        enumerate_totallyreal_fields_rel(F, Integer(2), Integer(2000))###line 568:
    sage: enumerate_totallyreal_fields_rel(F, 2, 2000)
      File "/home/grout/sage/local/lib/python/site-packages/sage/rings/number_field/totallyreal_rel.py", line 646, in enumerate_totallyreal_fields_rel
        T = tr_data_rel(F,m,B,a)
      File "/home/grout/sage/local/lib/python/site-packages/sage/rings/number_field/totallyreal_rel.py", line 200, in __init__
        anm1s[i] += sum([m*Z_Fbasis[i]*adj[i].__int__()//adj[self.d].__int__() for i in range(self.d)])
    IndexError: list index out of range
**********************************************************************
File "/home/grout/sage/devel/sage-main/sage/rings/number_field/totallyreal_rel.py", line 577:
    sage: ls = enumerate_totallyreal_fields_rel(F, 2, 10^4)
Exception raised:
    Traceback (most recent call last):
      File "/home/grout/sage/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/grout/sage/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/grout/sage/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_5[6]>", line 1, in <module>
        ls = enumerate_totallyreal_fields_rel(F, Integer(2), Integer(10)**Integer(4))###line 577:
    sage: ls = enumerate_totallyreal_fields_rel(F, 2, 10^4)
      File "/home/grout/sage/local/lib/python/site-packages/sage/rings/number_field/totallyreal_rel.py", line 646, in enumerate_totallyreal_fields_rel
        T = tr_data_rel(F,m,B,a)
      File "/home/grout/sage/local/lib/python/site-packages/sage/rings/number_field/totallyreal_rel.py", line 200, in __init__
        anm1s[i] += sum([m*Z_Fbasis[i]*adj[i].__int__()//adj[self.d].__int__() for i in range(self.d)])
    IndexError: list index out of range
**********************************************************************
File "/home/grout/sage/devel/sage-main/sage/rings/number_field/totallyreal_rel.py", line 578:
    sage: print "ignore this";  ls # random (the second factor is platform-dependent)
Exception raised:
    Traceback (most recent call last):
      File "/home/grout/sage/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/grout/sage/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/grout/sage/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_5[7]>", line 1, in <module>
        print "ignore this";  ls # random (the second factor is platform-dependent)###line 578:
    sage: print "ignore this";  ls # random (the second factor is platform-dependent)
    NameError: name 'ls' is not defined
**********************************************************************
File "/home/grout/sage/devel/sage-main/sage/rings/number_field/totallyreal_rel.py", line 600:
    sage: [ f[0] for f in ls ]
Exception raised:
    Traceback (most recent call last):
      File "/home/grout/sage/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/grout/sage/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/grout/sage/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_5[8]>", line 1, in <module>
        [ f[Integer(0)] for f in ls ]###line 600:
    sage: [ f[0] for f in ls ]
    NameError: name 'ls' is not defined
**********************************************************************
File "/home/grout/sage/devel/sage-main/sage/rings/number_field/totallyreal_rel.py", line 603:
    sage: [NumberField(ZZx(x[1]), 't').is_galois() for x in ls]
Exception raised:
    Traceback (most recent call last):
      File "/home/grout/sage/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/grout/sage/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/grout/sage/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_5[9]>", line 1, in <module>
        [NumberField(ZZx(x[Integer(1)]), 't').is_galois() for x in ls]###line 603:
    sage: [NumberField(ZZx(x[1]), 't').is_galois() for x in ls]
    NameError: name 'ls' is not defined
**********************************************************************
2 items had failures:
   1 of   4 in __main__.example_3
   5 of  12 in __main__.example_5
***Test Failed*** 6 failures.
For whitespace errors, see the file /home/grout/sage/tmp/.doctest_totallyreal_rel.py
	 [4.3 s]
exit code: 1024
 
----------------------------------------------------------------------
The following tests failed:


	sage -t  "devel/sage-main/sage/rings/number_field/totallyreal_rel.py"
Total time for all tests: 4.3 seconds
```



---

Comment by jason created at 2009-07-19 03:45:47

See the documentation patch (the second patch above) for changes to the totallyreal_rel.py file, including a comment about where a bug probably is.


---

Comment by jason created at 2009-07-19 03:56:32

I should mention that I'm not qualified to correct the code in totallyreal_rel.py, since I don't know which i is from the comprehension and which i is from the outer loop.


---

Comment by robertwb created at 2009-07-25 10:48:18

Jason, your code looks good to me. I've fixed totallyreal_rel.py--I don't totally understand the code/error either but did extensive comparison with the original code. I also fixed the remaining precision issues--the missing 0 is due to the fact that the decimal point is no longer considered a significant digit. 

It'd be nice to get this into 4.1.1.


---

Attachment

All doctests pass now.  I assume your comments mean that you are giving a positive review to my changes in totallyreal_rel.py (correct me if I'm wrong!).  Doctests now pass in totallyreal_rel.py and the other files mentioned above, so I'm changing this to a positive review and marking you as a reviewer too.

I agree that it would be very, very nice to get this into 4.1.1, especially considering how many times it's come up on the mailing lists just in the past week.


---

Comment by jason created at 2009-07-27 16:27:20

When I say above that all doctests pass, I mean the doctests pointed out in my comment above.  I assume that when this patch is merged, *all* doctests will be run and any errors will kick this ticket back to "needs work".


---

Comment by mvngu created at 2009-07-29 11:51:44

I applied patches in this order:
 1. patch at #5081
 1. `6506-numpy-types.patch`
 1. `trac-6506-doc-fixes.patch`
 1. `6506-numpy-types-fixes.patch`
Doctesting revealed the following failures, which are mostly numerical noise:

```
sage -t -long devel/sage-main/sage/symbolic/expression.pyx
**********************************************************************
File "/scratch/mvngu/release/sage-4.1.1.alpha1/devel/sage-main/sage/symbolic/expression.pyx", line 4360:
    sage: SR(1.0000000000000000000000000).cosh()
Expected:
    cosh(1.0000000000000000000000000)
Got:
    cosh(1.000000000000000000000000)
**********************************************************************
1 items had failures:
   1 of  12 in __main__.example_111
***Test Failed*** 1 failures.
For whitespace errors, see the file /scratch/mvngu/release/sage-4.1.1.alpha1/tmp/.doctest_expression.py
	 [30.5 s]

sage -t -long devel/sage-main/sage/functions/special.py
**********************************************************************
File "/scratch/mvngu/release/sage-4.1.1.alpha1/devel/sage-main/sage/functions/special.py", line 655:
    sage: bessel_I(0,1,"maxima")
Expected:
    1.26606587775200...
Got:
    1.26606587775201
**********************************************************************
1 items had failures:
   1 of   8 in __main__.example_8
***Test Failed*** 1 failures.
For whitespace errors, see the file /scratch/mvngu/release/sage-4.1.1.alpha1/tmp/.doctest_special.py
	 [5.7 s]

sage -t -long devel/sage-main/sage/combinat/combinat.py
**********************************************************************
File "/scratch/mvngu/release/sage-4.1.1.alpha1/devel/sage-main/sage/combinat/combinat.py", line 1733:
    sage: hurwitz_zeta(11/10,1/2,50)
Expected:
    12.103813495683755105709077412966680619033648618088
Got:
    12.10381349568375510570907741296668061903364861809
**********************************************************************
1 items had failures:
   1 of   5 in __main__.example_76
***Test Failed*** 1 failures.
For whitespace errors, see the file /scratch/mvngu/release/sage-4.1.1.alpha1/tmp/.doctest_combinat.py
	 [4.0 s]

sage -t -long devel/sage-main/sage/rings/rational_field.py
**********************************************************************
File "/scratch/mvngu/release/sage-4.1.1.alpha1/devel/sage-main/sage/rings/rational_field.py", line 118:
    sage: 6530219459687219.0/281474976710656
Expected:
    23.199999999999999
Got:
    23.20000000000000
**********************************************************************
1 items had failures:
   1 of  24 in __main__.example_1
***Test Failed*** 1 failures.
For whitespace errors, see the file /scratch/mvngu/release/sage-4.1.1.alpha1/tmp/.doctest_rational_field.py
	 [2.9 s]

sage -t -long devel/sage-main/sage/functions/transcendental.py
**********************************************************************
File "/scratch/mvngu/release/sage-4.1.1.alpha1/devel/sage-main/sage/functions/transcendental.py", line 395:
    sage: dickman_rho(10.00000000000000000000000000000000000000)
Expected:
    2.770171837725958988758121200634342326343e-11
Got:
    2.77017183772595898875812120063434232634e-11
**********************************************************************
1 items had failures:
   1 of   6 in __main__.example_8
***Test Failed*** 1 failures.
For whitespace errors, see the file /scratch/mvngu/release/sage-4.1.1.alpha1/tmp/.doctest_transcendental.py
	 [3.5 s]

sage -t -long devel/sage-main/sage/rings/complex_interval.pyx
**********************************************************************
File "/scratch/mvngu/release/sage-4.1.1.alpha1/devel/sage-main/sage/rings/complex_interval.pyx", line 1052:
    sage: ComplexIntervalFieldElement(1.234567890123456789012345, 5.4321098654321987654321)
Expected:
    1.2345678901234567890123450? + 5.4321098654321987654321000?*I
Got:
    1.234567890123456789012350? + 5.432109865432198765432000?*I
**********************************************************************
1 items had failures:
   1 of   9 in __main__.example_32
***Test Failed*** 1 failures.
For whitespace errors, see the file /scratch/mvngu/release/sage-4.1.1.alpha1/tmp/.doctest_complex_interval.py
	 [2.9 s]
```



---

Comment by robertwb created at 2009-07-29 12:03:00

I believe these are due to the correction of real number precision, not numerical noise. They all look fine to me--I'll try and post a patch later today.


---

Comment by robertwb created at 2009-07-29 12:17:53

The above issues are resolved.


---

Comment by mvngu created at 2009-07-29 12:39:03

With the patch at #5081 and the patches on this ticket, I still get a doctest failure:

```
sage -t -long devel/sage-main/sage/combinat/combinat.py
**********************************************************************
File "/scratch/mvngu/release/sage-4.1.1.alpha1/devel/sage-main/sage/combinat/combinat.py", line 1733:
    sage: hurwitz_zeta(11/10,1/2,50)
Expected:
    12.103813495683755105709077412966680619033648618088
Got:
    12.10381349568375510570907741296668061903364861809
**********************************************************************
1 items had failures:
   1 of   5 in __main__.example_76
***Test Failed*** 1 failures.
For whitespace errors, see the file /scratch/mvngu/release/sage-4.1.1.alpha1/tmp/.doctest_combinat.py
	 [3.9 s]
```



---

Attachment

Oh, somehow I missed that one. I've refreshed the patch.


---

Comment by mvngu created at 2009-07-29 13:46:57

Merged all four patches.


---

Comment by mvngu created at 2009-07-29 13:46:57

Resolution: fixed


---

Comment by jdemeyer created at 2015-12-22 13:04:29

What's this?

```
            if self._prec <= 57: # max size of repr(float)
```

The "57" makes no sense to me. How is `repr()` even related?


---

Comment by jdemeyer created at 2016-01-07 11:13:53

The "57" has been fixed in #19758.
