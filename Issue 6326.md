# Issue 6326: optional doctest failure -- all quadratic forms tests that involve " # optional -- souvigner"

Issue created by migration from https://trac.sagemath.org/ticket/6326

Original creator: was

Original creation time: 2009-06-16 15:00:34

Assignee: tbd

These all fail.  This "souvigner" is not an optional or even experimental spkg.  I have no clue where to get it. Either this code has to go, or Souvigner_AUTO has to be made an optional spkg (which would be a very reasonable way to resolve this ticket).


```
sage -t -long --optional devel/sage/sage/quadratic_forms/quadratic_form__automorphisms.py
sh: /scratch/wstein/build/sage-4.0.2.alpha3/local/bin/Souvigner_AUTO: not found
sh: /scratch/wstein/build/sage-4.0.2.alpha3/local/bin/Souvigner_AUTO: not found
sh: /scratch/wstein/build/sage-4.0.2.alpha3/local/bin/Souvigner_AUTO: not found
**********************************************************************
File "/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/quadratic_forms/quadratic_form__automorphisms.py", line 257:
    sage: Q.number_of_automorphisms()                     # optional -- souvigner
Exception raised:
    Traceback (most recent call last):
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_3[3]>", line 1, in <module>
        Q.number_of_automorphisms()                     # optional -- souvigner###line 257:
    sage: Q.number_of_automorphisms()                     # optional -- souvigner
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/quadratic_forms/quadratic_form__automorphisms.py", line 396, in number_of_automorphisms
        self.__number_of_automorphisms = self.number_of_automorphisms__souvigner()
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/quadratic_forms/quadratic_form__automorphisms.py", line 453, in number_of_automorphisms__souvigner
        raise RuntimeError, "Oops! There is a problem..."
    RuntimeError: Oops! There is a problem...
**********************************************************************
File "/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/quadratic_forms/quadratic_form__automorphisms.py", line 265:
    sage: Q.number_of_automorphisms()                     # optional -- souvigner
Exception raised:
    Traceback (most recent call last):
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_3[7]>", line 1, in <module>
        Q.number_of_automorphisms()                     # optional -- souvigner###line 265:
    sage: Q.number_of_automorphisms()                     # optional -- souvigner
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/quadratic_forms/quadratic_form__automorphisms.py", line 396, in number_of_automorphisms
        self.__number_of_automorphisms = self.number_of_automorphisms__souvigner()
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/quadratic_forms/quadratic_form__automorphisms.py", line 453, in number_of_automorphisms__souvigner
        raise RuntimeError, "Oops! There is a problem..."
    RuntimeError: Oops! There is a problem...
**********************************************************************
File "/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/quadratic_forms/quadratic_form__automorphisms.py", line 363:
    sage: Q.number_of_automorphisms(recompute=True)           # optional -- souvigner
Exception raised:
    Traceback (most recent call last):
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/binsh: /scratch/wstein/build/sage-4.0.2.alpha3/local/bin/Souvigner_AUTO: not found
sh: /scratch/wstein/build/sage-4.0.2.alpha3/local/bin/Souvigner_AUTO: not found
/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_4[5]>", line 1, in <module>
        Q.number_of_automorphisms(recompute=True)           # optional -- souvigner###line 363:
    sage: Q.number_of_automorphisms(recompute=True)           # optional -- souvigner
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/quadratic_forms/quadratic_form__automorphisms.py", line 396, in number_of_automorphisms
        self.__number_of_automorphisms = self.number_of_automorphisms__souvigner()
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/quadratic_forms/quadratic_form__automorphisms.py", line 453, in number_of_automorphisms__souvigner
        raise RuntimeError, "Oops! There is a problem..."
    RuntimeError: Oops! There is a problem...
**********************************************************************
File "/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/quadratic_forms/quadratic_form__automorphisms.py", line 365:
    sage: Q.list_external_initializations()                   # optional -- souvigner
Expected:
    []
Got:
    ['number_of_automorphisms']
**********************************************************************
File "/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/quadratic_forms/quadratic_form__automorphisms.py", line 369:
    sage: Q.number_of_automorphisms()                         # optional -- souvigner
Exception raised:
    Traceback (most recent call last):
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_4[8]>", line 1, in <module>
        Q.number_of_automorphisms()                         # optional -- souvigner###line 369:
    sage: Q.number_of_automorphisms()                         # optional -- souvigner
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/quadratic_forms/quadratic_form__automorphisms.py", line 396, in number_of_automorphisms
        self.__number_of_automorphisms = self.number_of_automorphisms__souvigner()
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/quadratic_forms/quadratic_form__automorphisms.py", line 453, in number_of_automorphisms__souvigner
        raise RuntimeError, "Oops! There is a problem..."
    RuntimeError: Oops! There is a problem...
**********************************************************************
File "/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/quadratic_forms/quadratic_form__automorphisms.py", line 410:
    sage: Q.number_of_automorphisms__souvigner()                           # optional -- souvigner
Exception raised:
    Traceback (most recent call last):
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_5[3]>", line 1, in <module>
        Q.number_of_automorphisms__souvigner()                           # optional -- souvigner###line 410:
    sage: Q.number_of_automorphisms__souvigner()                           # optional -- souvigner
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/quadratic_forms/quadratic_form__automorphisms.py", line 453, in number_of_automorphisms__souvigner
        raise RuntimeError, "Oops! There is a problem..."
    RuntimeError: Oops! There is a problem...
**********************************************************************
3 items had failures:
   2 of  15 in __main__.example_3
   3 of  12 in __main__.example_4
   1 of   5 in __main__.example_5
***Test Failed*** 6 failures.
For whitespace errors, see the file /home/wstein/build/sage-4.0.2.alpha3/tmp/.doctest_quadratic_form__automorphisms.p
```



---

Comment by jonhanke created at 2011-01-09 07:57:02

Souvigner auto/isomorphism code tarball


---

Attachment

I have attached the Souvigner tarball sent to me by Gabi Nebe in March 2008.  I'm not sure how to arrange Sage to build it, but the two files ISOM64 and AUTO64 that the makeflie produces need to renamed as Souvigner_ISOM and Souvigner_AUTO and moved to sage-4.x/local/bin.


---

Comment by jonhanke created at 2011-01-12 04:29:14

Changing assignee from tbd to justin.


---

Comment by jonhanke created at 2011-01-12 04:29:14

Changing component from optional packages to quadratic forms.


---

Comment by jonhanke created at 2011-01-12 04:29:14

There is a bug within the interface the Souvigner code that produces false results:

```
sage: Q1 = DiagonalQuadraticForm(ZZ, [1,3,5])
sage: Q2 = QuadraticForm(ZZ, 3, [1,0,0, 2,2, 8])
sage: Q1.theta_series()
1 + 2*q + 2*q^3 + 6*q^4 + 2*q^5 + 4*q^6 + 4*q^7 + 4*q^8 + 14*q^9 + O(q^10)
sage: Q2.theta_series()
1 + 2*q + 2*q^2 + 4*q^3 + 2*q^4 + 4*q^6 + 6*q^8 + 14*q^9 + O(q^10)
sage: Q1.is_globally_equivalent_to(Q2)    ## Correct
False
sage: Q2.is_globally_equivalent_to(Q1)    ## Incorrect
True
```


The problem results from the differing possible failure messages ("...not isometric..." or "...not isomorphic...") returned from the Souvigner Code.  A patch is attached.


---

Comment by jonhanke created at 2011-01-12 04:36:15

Fixes a bug in the quadratic forms global equivalence testing using Souvigner's code


---

Comment by jonhanke created at 2011-01-12 04:45:58

Changing status from new to needs_review.


---

Attachment


---

Comment by rlm created at 2011-03-11 06:06:28

In order for this to get into Sage proper, we'll need to make an spkg which installs the right things to the right places.


---

Comment by rlm created at 2011-03-11 06:06:28

Changing status from needs_review to needs_work.


---

Attachment


---

Comment by jdemeyer created at 2015-06-10 20:21:49

If anybody cares about this: this functionality is now also provided by the PARI functions `qfisom()` and `qfauto()`.


---

Comment by jdemeyer created at 2015-06-10 21:36:09

New commits:


---

Comment by git created at 2015-06-10 21:36:37

Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:


---

Comment by jdemeyer created at 2015-06-10 21:37:54

Changing status from needs_work to needs_review.


---

Comment by git created at 2015-06-11 08:53:17

Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:


---

Comment by chapoton created at 2015-06-12 15:27:50

Changing keywords from "" to "quadratic form".


---

Comment by chapoton created at 2015-06-12 15:27:50

Changing status from needs_review to positive_review.


---

Comment by chapoton created at 2015-06-12 15:27:50

Looks good to me.


---

Comment by vbraun created at 2015-06-12 22:58:50

Resolution: fixed
