# Issue 6279: spkg-check fails for the R spkg

archive/issues_006279.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  @kcrisman\n\nI build sage-4.0.2.alpha3 on sage.math with \n\n```\nexport SAGE_CHECK=\"yes\"\n```\n\nand it failed as follows:\n\n\n```\n...\nSuccessfully installed r-2.6.1.p22\nRunning the test suite.\nmake[2]: Entering directory `/scratch/wstein/build/sage-4.0.2.alpha3/spkg/build/r-2.6.1.p22/src'\nmake[3]: Entering directory `/scratch/wstein/build/sage-4.0.2.alpha3/spkg/build/r-2.6.1.p22/src/tests'\nmake[4]: Entering directory `/scratch/wstein/build/sage-4.0.2.alpha3/spkg/build/r-2.6.1.p22/src/tests'\nmake[5]: Entering directory `/scratch/wstein/build/sage-4.0.2.alpha3/spkg/build/r-2.6.1.p22/src/tests/Examples'\nmake[6]: Entering directory `/scratch/wstein/build/sage-4.0.2.alpha3/spkg/build/r-2.6.1.p22/src/tests/Examples'\nmake[6]: Leaving directory `/scratch/wstein/build/sage-4.0.2.alpha3/spkg/build/r-2.6.1.p22/src/tests/Examples'\nmake[6]: Entering directory `/scratch/wstein/build/sage-4.0.2.alpha3/spkg/build/r-2.6.1.p22/src/tests/Examples'\ncollecting examples for package 'base' ...\nmake[7]: Entering directory `/scratch/wstein/build/sage-4.0.2.alpha3/spkg/build/r-2.6.1.p22/src/src/library'\n >>> Building/Updating help pages for package 'base'\n     Formats: text html latex example\nmake[7]: Leaving directory `/scratch/wstein/build/sage-4.0.2.alpha3/spkg/build/r-2.6.1.p22/src/src/library'\nmake[6]: *** No rule to make target `0', needed by `base-Ex.Rout'.  Stop.\nmake[6]: Leaving directory `/scratch/wstein/build/sage-4.0.2.alpha3/spkg/build/r-2.6.1.p22/src/tests/Examples'\nmake[5]: *** [test-Examples-Base] Error 2\nmake[5]: Leaving directory `/scratch/wstein/build/sage-4.0.2.alpha3/spkg/build/r-2.6.1.p22/src/tests/Examples'\nmake[4]: *** [test-Examples] Error 2\nmake[4]: Leaving directory `/scratch/wstein/build/sage-4.0.2.alpha3/spkg/build/r-2.6.1.p22/src/tests'\nmake[3]: *** [test-all-basics] Error 1\nmake[3]: Leaving directory `/scratch/wstein/build/sage-4.0.2.alpha3/spkg/build/r-2.6.1.p22/src/tests'\nmake[2]: *** [check] Error 2\nmake[2]: Leaving directory `/scratch/wstein/build/sage-4.0.2.alpha3/spkg/build/r-2.6.1.p22/src'\nError while running the R testsuite ... exiting\n*************************************Error testing package ** r-2.6.1.p22 **\n*************************************\nsage: An error occurred while testing r-2.6.1.p22\nPlease email sage-devel http://groups.google.com/group/sage-devel\nexplaining the problem and send the relevant part of\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6279\n\n",
    "created_at": "2009-06-14T09:21:13Z",
    "labels": [
        "component: build",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.2",
    "title": "spkg-check fails for the R spkg",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6279",
    "user": "https://github.com/williamstein"
}
```
Assignee: tbd

CC:  @kcrisman

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


Issue created by migration from https://trac.sagemath.org/ticket/6279





---

archive/issue_comments_050047.json:
```json
{
    "body": "This fails for 4.1 on sage.math. Looking in the tests directory, I see a couple \"`Rout.fail`\" files, and both complain\n\n```\nError in .find.package(package, lib.loc, verbose = verbose) : \n  there is no package called 'MASS'\n```\n\nGoogling around, it looks like we'd need to install the recommended packages: https://stat.ethz.ch/pipermail/r-help/2002-May/021259.html. It looks like there is a \"--without-recommended\" flag for ./configure, but it may not do what we want: https://stat.ethz.ch/pipermail/r-devel/2008-April/049054.html\n\nSadly, you can't even get through the testsuite without the recommended packages.",
    "created_at": "2009-07-11T09:10:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6279",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6279#issuecomment-50047",
    "user": "https://github.com/dandrake"
}
```

This fails for 4.1 on sage.math. Looking in the tests directory, I see a couple "`Rout.fail`" files, and both complain

```
Error in .find.package(package, lib.loc, verbose = verbose) : 
  there is no package called 'MASS'
```

Googling around, it looks like we'd need to install the recommended packages: https://stat.ethz.ch/pipermail/r-help/2002-May/021259.html. It looks like there is a "--without-recommended" flag for ./configure, but it may not do what we want: https://stat.ethz.ch/pipermail/r-devel/2008-April/049054.html

Sadly, you can't even get through the testsuite without the recommended packages.



---

archive/issue_comments_050048.json:
```json
{
    "body": "In the r-2.9.2 spkg, the failing tests are\n\n\n```\nsrc/library/utils/R-ex/capture.output.R\nsrc/library/utils/R-ex/ls_str.R\nsrc/library/grDevices/R-ex/densCols.R\nsrc/library/graphics/R-ex/smoothscatter.R\nsrc/library/stats/R-ex/add1.R\nsrc/library/stats/R-ex/alias.R\nsrc/library/stats/R-ex/anova.glm.R\nsrc/library/stats/R-ex/aov.R\nsrc/library/stats/R-ex/dummy.coef.R\nsrc/library/stats/R-ex/extractAIC.R\nsrc/library/stats/R-ex/glm.R\nsrc/library/stats/R-ex/nls.R\nsrc/library/stats/R-ex/stat.anova.R \nsrc/library/stats/R-ex/summary.glm.R\n```\n\n\nas well as the test for (R) issue #2586 in `reg-tests-1.R` and\nthe test labelled `## as.matrix.data.frame with coercion` in `reg-tests-3.R`.\n\nThey seem to be caused by missing packages `MASS`, `KernSmooth`, `survival`.\n\nMaybe we can just remove the failing tests?",
    "created_at": "2010-01-17T03:58:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6279",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6279#issuecomment-50048",
    "user": "https://github.com/wjp"
}
```

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

archive/issue_comments_050049.json:
```json
{
    "body": "See #6235 for follow-up with a new spkg which apparently has different failures.",
    "created_at": "2010-01-19T19:35:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6279",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6279#issuecomment-50049",
    "user": "https://github.com/kcrisman"
}
```

See #6235 for follow-up with a new spkg which apparently has different failures.



---

archive/issue_comments_050050.json:
```json
{
    "body": "Replying to [comment:4 kcrisman]:\n> See #6235 for follow-up with a new spkg which apparently has different failures.\n\nI mean #6532.  Also note this is only on some hardware.",
    "created_at": "2010-01-19T19:38:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6279",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6279#issuecomment-50050",
    "user": "https://github.com/kcrisman"
}
```

Replying to [comment:4 kcrisman]:
> See #6235 for follow-up with a new spkg which apparently has different failures.

I mean #6532.  Also note this is only on some hardware.



---

archive/issue_comments_050051.json:
```json
{
    "body": "This may be fixed by #7485; see #6532 for details.",
    "created_at": "2010-01-19T20:56:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6279",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6279#issuecomment-50051",
    "user": "https://github.com/kcrisman"
}
```

This may be fixed by #7485; see #6532 for details.



---

archive/issue_comments_050052.json:
```json
{
    "body": "I have tried this on a Linux and Macintel, and it seems that this is now fixed when one puts in all recommended packages and after #7485.  I don't feel comfortable closing it, though, since I made the new spkg at #6532. Putting as \"needs review\", though it doesn't exactly...",
    "created_at": "2010-01-25T19:07:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6279",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6279#issuecomment-50052",
    "user": "https://github.com/kcrisman"
}
```

I have tried this on a Linux and Macintel, and it seems that this is now fixed when one puts in all recommended packages and after #7485.  I don't feel comfortable closing it, though, since I made the new spkg at #6532. Putting as "needs review", though it doesn't exactly...



---

archive/issue_comments_050053.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-25T19:07:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6279",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6279#issuecomment-50053",
    "user": "https://github.com/kcrisman"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_050054.json:
```json
{
    "body": "Close as fixed by #6532.",
    "created_at": "2010-01-25T23:22:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6279",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6279#issuecomment-50054",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Close as fixed by #6532.



---

archive/issue_comments_050055.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-25T23:22:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6279",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6279#issuecomment-50055",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed



---

archive/issue_events_006523.json:
```json
{
    "actor": "mvngu",
    "created_at": "2010-01-25T23:22:18Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6279",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6279#event-6523"
}
```
