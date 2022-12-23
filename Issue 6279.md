# Issue 6279: spkg-check fails for the R spkg

Issue created by migration from https://trac.sagemath.org/ticket/6279

Original creator: was

Original creation time: 2009-06-14 09:21:13

Assignee: tbd

CC:  kcrisman

I build sage-4.0.2.alpha3 on sage.math with 

```
export SAGE_CHECK="yes"
```

and it failed as follows:


```
...
Successfully installed r-2.6.1.p22
Running the test suite.
make[2]: Entering directory `/scratch/wstein/build/sage-4.0.2.alpha3/spkg/build/r-2.6.1.p22/src'
make[3]: Entering directory `/scratch/wstein/build/sage-4.0.2.alpha3/spkg/build/r-2.6.1.p22/src/tests'
make[4]: Entering directory `/scratch/wstein/build/sage-4.0.2.alpha3/spkg/build/r-2.6.1.p22/src/tests'
make[5]: Entering directory `/scratch/wstein/build/sage-4.0.2.alpha3/spkg/build/r-2.6.1.p22/src/tests/Examples'
make[6]: Entering directory `/scratch/wstein/build/sage-4.0.2.alpha3/spkg/build/r-2.6.1.p22/src/tests/Examples'
make[6]: Leaving directory `/scratch/wstein/build/sage-4.0.2.alpha3/spkg/build/r-2.6.1.p22/src/tests/Examples'
make[6]: Entering directory `/scratch/wstein/build/sage-4.0.2.alpha3/spkg/build/r-2.6.1.p22/src/tests/Examples'
collecting examples for package 'base' ...
make[7]: Entering directory `/scratch/wstein/build/sage-4.0.2.alpha3/spkg/build/r-2.6.1.p22/src/src/library'
 >>> Building/Updating help pages for package 'base'
     Formats: text html latex example
make[7]: Leaving directory `/scratch/wstein/build/sage-4.0.2.alpha3/spkg/build/r-2.6.1.p22/src/src/library'
make[6]: *** No rule to make target `0', needed by `base-Ex.Rout'.  Stop.
make[6]: Leaving directory `/scratch/wstein/build/sage-4.0.2.alpha3/spkg/build/r-2.6.1.p22/src/tests/Examples'
make[5]: *** [test-Examples-Base] Error 2
make[5]: Leaving directory `/scratch/wstein/build/sage-4.0.2.alpha3/spkg/build/r-2.6.1.p22/src/tests/Examples'
make[4]: *** [test-Examples] Error 2
make[4]: Leaving directory `/scratch/wstein/build/sage-4.0.2.alpha3/spkg/build/r-2.6.1.p22/src/tests'
make[3]: *** [test-all-basics] Error 1
make[3]: Leaving directory `/scratch/wstein/build/sage-4.0.2.alpha3/spkg/build/r-2.6.1.p22/src/tests'
make[2]: *** [check] Error 2
make[2]: Leaving directory `/scratch/wstein/build/sage-4.0.2.alpha3/spkg/build/r-2.6.1.p22/src'
Error while running the R testsuite ... exiting
*************************************Error testing package ** r-2.6.1.p22 **
*************************************
sage: An error occurred while testing r-2.6.1.p22
Please email sage-devel http://groups.google.com/group/sage-devel
explaining the problem and send the relevant part of
```



---

Comment by ddrake created at 2009-07-11 09:10:04

This fails for 4.1 on sage.math. Looking in the tests directory, I see a couple "`Rout.fail`" files, and both complain

```
Error in .find.package(package, lib.loc, verbose = verbose) : 
  there is no package called 'MASS'
```

Googling around, it looks like we'd need to install the recommended packages: https://stat.ethz.ch/pipermail/r-help/2002-May/021259.html. It looks like there is a "--without-recommended" flag for ./configure, but it may not do what we want: https://stat.ethz.ch/pipermail/r-devel/2008-April/049054.html

Sadly, you can't even get through the testsuite without the recommended packages.


---

Comment by wjp created at 2010-01-17 03:58:01

In the r-2.9.2 spkg, the failing tests are


```
src/library/utils/R-ex/capture.output.R
src/library/utils/R-ex/ls_str.R
src/library/grDevices/R-ex/densCols.R
src/library/graphics/R-ex/smoothscatter.R
src/library/stats/R-ex/add1.R
src/library/stats/R-ex/alias.R
src/library/stats/R-ex/anova.glm.R
src/library/stats/R-ex/aov.R
src/library/stats/R-ex/dummy.coef.R
src/library/stats/R-ex/extractAIC.R
src/library/stats/R-ex/glm.R
src/library/stats/R-ex/nls.R
src/library/stats/R-ex/stat.anova.R 
src/library/stats/R-ex/summary.glm.R
```


as well as the test for (R) issue #2586 in `reg-tests-1.R` and
the test labelled `## as.matrix.data.frame with coercion` in `reg-tests-3.R`.

They seem to be caused by missing packages `MASS`, `KernSmooth`, `survival`.

Maybe we can just remove the failing tests?


---

Comment by kcrisman created at 2010-01-19 19:35:25

See #6235 for follow-up with a new spkg which apparently has different failures.


---

Comment by kcrisman created at 2010-01-19 19:38:32

Replying to [comment:4 kcrisman]:
> See #6235 for follow-up with a new spkg which apparently has different failures.

I mean #6532.  Also note this is only on some hardware.


---

Comment by kcrisman created at 2010-01-19 20:56:12

This may be fixed by #7485; see #6532 for details.


---

Comment by kcrisman created at 2010-01-25 19:07:45

I have tried this on a Linux and Macintel, and it seems that this is now fixed when one puts in all recommended packages and after #7485.  I don't feel comfortable closing it, though, since I made the new spkg at #6532. Putting as "needs review", though it doesn't exactly...


---

Comment by kcrisman created at 2010-01-25 19:07:45

Changing status from new to needs_review.


---

Comment by mvngu created at 2010-01-25 23:22:18

Close as fixed by #6532.


---

Comment by mvngu created at 2010-01-25 23:22:18

Resolution: fixed
