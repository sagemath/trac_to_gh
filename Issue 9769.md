# Issue 9769: SphericalDistribution() is not random

Issue created by migration from https://trac.sagemath.org/ticket/9770

Original creator: schilly

Original creation time: 2010-08-20 10:50:32

Assignee: amhou

In the following list `l`, some elements repeat quite often:


```
sage: l = [ SphericalDistribution(dimension=2).get_random_element() for _ in range(1000)]
sage: uniq = []
sage: for x in l:
    if x not in uniq:
        uniq.append(x)
....:
sage: len(uniq)
34
```


The output is not random. For example, the first line is repeated ~30 times in the 1000 lines of output.	It works fine if SphericalDistribution is only instantiated once!


---

Attachment

The bug is not unique to the spherical distribution; rather, it has to do with whether the distribution is instantiated prior to the use of the random element method.  The worksheet above illustrates the same behavior with the Gaussian and uniform distributions.


---

Comment by dsm created at 2011-10-31 04:03:26

Changing status from new to needs_review.


---

Comment by dsm created at 2011-10-31 04:03:26

Oh, wow.  This is because of the lines


```
            self.seed = random.randint(1, 2^32)
```


2 xor 32 is 34.. and the `^` vs. `**` bug strikes again.


---

Comment by dsm created at 2011-10-31 04:04:09

fix seed randomization


---

Attachment

Wow, good catch.  Affected file passes tests; code looks good.

Can you fill in the author name?


---

Comment by jason created at 2011-12-13 16:18:36

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2011-12-17 09:12:22

Resolution: fixed


---

Comment by jdemeyer created at 2011-12-21 09:22:27

Resolution changed from fixed to 


---

Comment by jdemeyer created at 2011-12-21 09:22:27

Changing status from closed to new.


---

Comment by jdemeyer created at 2011-12-21 09:22:27

On hawk (OpenSolaris 06.2009-32):

```
sage -t -long  -force_lib devel/sage/sage/gsl/probability_distribution.pyx
**********************************************************************
File "/export/home/buildbot/build/sage/hawk-1/hawk_full/build/sage-4.8.alpha5/devel/sage-main/sage/gsl/probability_distribution.pyx", line 339:
    sage: T = RealDistribution('rayleigh', sigma)
Exception raised:
    Traceback (most recent call last):
      File "/export/home/buildbot/build/sage/hawk-1/hawk_full/build/sage-4.8.alpha5/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/export/home/buildbot/build/sage/hawk-1/hawk_full/build/sage-4.8.alpha5/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/export/home/buildbot/build/sage/hawk-1/hawk_full/build/sage-4.8.alpha5/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_12[16]>", line 1, in <module>
        T = RealDistribution('rayleigh', sigma)###line 339:
    sage: T = RealDistribution('rayleigh', sigma)
      File "probability_distribution.pyx", line 503, in sage.gsl.probability_distribution.RealDistribution.__init__ (sage/gsl/probability_distribution.c:2309)
        self.seed = random.randint(1, 2**32)
    OverflowError: long int too large to convert to int
**********************************************************************
[...many more like this...]

sage -t -long  -force_lib devel/sage/sage/matrix/constructor.py
**********************************************************************
File "/export/home/buildbot/build/sage/hawk-1/hawk_full/build/sage-4.8.alpha5/devel/sage-main/sage/matrix/constructor.py", line 2944:
    sage: print "ignore this";  B=random_matrix(FiniteField(7), 4, 4, algorithm='echelon_form', num_pivots=3); B # random
Exception raised:
    Traceback (most recent call last):
      File "/export/home/buildbot/build/sage/hawk-1/hawk_full/build/sage-4.8.alpha5/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/export/home/buildbot/build/sage/hawk-1/hawk_full/build/sage-4.8.alpha5/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/export/home/buildbot/build/sage/hawk-1/hawk_full/build/sage-4.8.alpha5/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_19[10]>", line 1, in <module>
        print "ignore this";  B=random_matrix(FiniteField(Integer(7)), Integer(4), Integer(4), algorithm='echelon_form', num_pivots=Integer(3)); B # random###line 2944:
    sage: print "ignore this";  B=random_matrix(FiniteField(7), 4, 4, algorithm='echelon_form', num_pivots=3); B # random
      File "/export/home/buildbot/build/sage/hawk-1/hawk_full/build/sage-4.8.alpha5/local/lib/python/site-packages/sage/matrix/constructor.py", line 1250, in random_matrix
        return random_rref_matrix(parent, *args, **kwds)
      File "/export/home/buildbot/build/sage/hawk-1/hawk_full/build/sage-4.8.alpha5/local/lib/python/site-packages/sage/matrix/constructor.py", line 3020, in random_rref_matrix
        pivot_generator=pd.RealDistribution("beta",[1.6,4.3])
      File "probability_distribution.pyx", line 503, in sage.gsl.probability_distribution.RealDistribution.__init__ (sage/gsl/probability_distribution.c:2309)
    OverflowError: long int too large to convert to int
**********************************************************************
[...]
```



---

Comment by dsm created at 2011-12-21 16:46:12

Changing status from new to needs_info.


---

Comment by dsm created at 2011-12-21 16:46:12

Urf.  Probably (?) we can simply replace `2**32` here with sys.maxint, but I can't be sure because I can't reproduce.

Emailed a guy who I know has access to a solaris box :-) but haven't heard back.  If anyone with an account on hawk could report the results of a cut-and-paste of the following


```
preparser(False)
import random, sys

nn = [2**31, 2**32, sys.maxint]
for n in nn:
    for d in -1, 0, 1:
        print n, d, n+d, repr(n+d), type(n+d)
        try:
            seed = random.randint(1, n+d)
        except Exception as err:
            print err
        try:
            random.seed(n+d)
        except Exception as err:
            print err
```


from within Sage, that would test whether I understand what's going on.


---

Comment by jdemeyer created at 2011-12-22 12:42:45

Output of your Sage script on `hawk`:

```
2147483648 -1 2147483647 2147483647L <type 'long'>
2147483648 0 2147483648 2147483648L <type 'long'>
2147483648 1 2147483649 2147483649L <type 'long'>
4294967296 -1 4294967295 4294967295L <type 'long'>
4294967296 0 4294967296 4294967296L <type 'long'>
4294967296 1 4294967297 4294967297L <type 'long'>
2147483647 -1 2147483646 2147483646 <type 'int'>
2147483647 0 2147483647 2147483647 <type 'int'>
2147483647 1 2147483648 2147483648L <type 'long'>
```



---

Comment by jdemeyer created at 2012-01-24 09:13:40

** bump **


---

Comment by dsm created at 2012-02-05 04:43:11

hopefully maxint-safe version


---

Comment by dsm created at 2012-02-05 04:44:50

Changing status from needs_info to needs_review.


---

Attachment

Version modified to (hopefully) avoid overflow errors without sacrificing entropy.  `@`jdemeyer, you mind trying it on hawk?


---

Comment by davidloeffler created at 2012-03-11 14:35:05

Apply trac_9770_fix_distribution_seeds_v2.patch

(for the patchbot, which is trying to install both patches at once)


---

Comment by davidloeffler created at 2012-03-11 16:43:07

Changing status from needs_review to needs_work.


---

Comment by davidloeffler created at 2012-03-11 16:43:07

This seems to conflict (in a rather trivial way) with #9958, and hence doesn't apply to the latest Sage beta.


---

Attachment

rebased to 5.0.beta7


---

Comment by dsm created at 2012-03-12 02:46:25

Changing status from needs_work to needs_review.


---

Comment by davidloeffler created at 2012-03-12 07:48:15

Apply trac_9770_fix_distribution_seeds_v4.patch

(for patchbot)


---

Comment by jdemeyer created at 2012-03-15 20:07:46

Let's not anthropomorphize the PatchBot :-)


---

Comment by jdemeyer created at 2012-03-19 16:14:03

Seems to work as it should...


---

Comment by jdemeyer created at 2012-03-19 16:14:03

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2012-03-21 22:03:58

Resolution: fixed
