# Issue 6532: R packages installation problem

Issue created by migration from https://trac.sagemath.org/ticket/6532

Original creator: wdj

Original creation time: 2009-07-14 11:15:08

Assignee: mabshoff

CC:  jason mvngu schilly

This was reported by Aleksey G:


```
I tried to install package "cluster" for R and got this:

----------------------------------------------------------------------
----------------------------------------------------------------------
sage: r.install_package("cluster")
Error: object "sage1" not found
```

Minh N replied that the (positively reviewed) patch #6379 
should be applied but "after applying that
patch, installing cluster, restart Sage, and import the library
cluster, Sage still doesn't recognize the cluster package. For
example, here is what I did under Sage 4.1:"
| Sage Version 4.0.2, Release Date: 2009-06-18                       |
| Type notebook() for the GUI, and license() for information.        |

```
sage: hg_sage.apply("http://www.sagetrac.org/sage_trac/raw-attachment/ticket/6379/trac_6379-Rdoctest.patch")
<applying the above patch>
sage: exit
Exiting SAGE (CPU time 0m0.09s, Wall time 0m18.86s).
[mvngu@sage sage-4.1-sage.math.washington.edu-x86_64-Linux]$ ./sage -br main
<now install cluster>
sage: r.install_packages("cluster")
<now restart Sage>
sage: exit
Exiting SAGE (CPU time 0m0.50s, Wall time 0m22.15s).
[mvngu@sage sage-4.1-sage.math.washington.edu-x86_64-Linux]$ ./sage -br main
<now import the package cluster>
sage: r.library("cluster")
---------------------------------------------------------------------------
ImportError                               Traceback (most recent call last)

/home/mvngu/.sage/temp/sage.math.washington.edu/16587/_home_mvngu__sage_init_sage_0.py
in <module>()

/scratch/mvngu/sage-4.1-sage.math.washington.edu-x86_64-Linux/local/lib/python2.6/site-packages/sage/interfaces/r.pyc
in library(self, library_name)
   557             # not all warnings (e.g. "closing unused
connection 3") are fatal

   558             if 'library(' in ret:       # locale-independent key-word
--> 559                 raise ImportError, "%s"%ret
   560         else:
   561             try:

ImportError: Loading required package: cluster
Warning message:
In library(package, lib.loc = lib.loc, character.only = TRUE,
logical.return = TRUE,  :
 there is no package called 'cluster'
```

from
Minh suspects that cluster has not been installed in a
directory where R (the one bundled with Sage) recognizes.



---

Comment by jason created at 2009-09-16 16:36:34

Changing status from new to assigned.


---

Comment by jason created at 2009-09-16 16:36:34

Changing assignee from mabshoff to jason.


---

Comment by kcrisman created at 2009-12-08 15:16:06

Okay, after trying the Sage Ed Day 1 talk I know what happens here.  There are certain packages which are recommended, not required, and those are basically not available on any mirrors, because it is assumed they are in your binary.  Cluster is one, as is MASS.  

So I am going to change the title to "Make R build with recommended packages."

Here is the fix, due to Jason Grout, from [this thread](http://groups.google.com/group/sage-support/browse_thread/thread/1237cbecacfa6190/97e3a5876d8f6d0a#97e3a5876d8f6d0a):

```
I just modified the R spkg-install thusly: 
diff -r b73bca59a75a spkg-install 
--- a/spkg-install      Sun Sep 20 18:25:26 2009 -0700 
+++ b/spkg-install      Mon Nov 23 20:35:29 2009 -0600 
@@ -77,19 +77,17 @@ 
  CFLAGS="-I$SAGE_LOCAL/include -L$SAGE_LOCAL/lib/ "$CFLAGS; export CFLAGS 
  LDFLAGS="-L$SAGE_LOCAL/lib/ "$LDFLAGS; export LDFLAGS 
-# do not build recommended packages for now, for speed. 
- 
  if [ `uname` = "Darwin" ]; then 
       echo "Configuring R for OSX" 
-    ./configure --prefix="$SAGE_LOCAL" --with-recommended-packages=no 
--enable-R-shlib --with-x=$XSUPPORT --with-readline="$SAGE_LOCAL" $OSXFW 
+    ./configure --prefix="$SAGE_LOCAL" --enable-R-shlib 
--with-x=$XSUPPORT --with-readline="$SAGE_LOCAL" $OSXFW 
  else 
       echo "Configuring R with ATLAS" 
-    ./configure --prefix="$SAGE_LOCAL" --with-recommended-packages=no 
--enable-R-shlib --with-x=$XSUPPORT --with-readline="$SAGE_LOCAL" 
--with-blas="-L$SAGE_LOCAL/lib -lf77blas -latlas" 
--with-lapack="-L$SAGE_LOCAL/lib -llapack -lcblas" $SUN_FLAGS 
+    ./configure --prefix="$SAGE_LOCAL" --enable-R-shlib 
--with-x=$XSUPPORT --with-readline="$SAGE_LOCAL" 
--with-blas="-L$SAGE_LOCAL/lib -lf77blas -latlas" 
--with-lapack="-L$SAGE_LOCAL/lib -llapack -lcblas" $SUN_FLAGS 
  fi 
  if [ $? -ne 0 ]; then 
       echo "Configuring R with fallback options" 
-    ./configure --prefix="$SAGE_LOCAL" --with-recommended-packages=no 
--enable-R-shlib --with-x=no --with-readline="$SAGE_LOCAL" $OSXFW $SUN_FLAGS 
+    ./configure --prefix="$SAGE_LOCAL" --enable-R-shlib --with-x=no 
--with-readline="$SAGE_LOCAL" $OSXFW $SUN_FLAGS 
  fi 
  if [ $? -ne 0 ]; then 
(I just removed the --with-recommended-packages=no switch from all 
command lines) 
```



---

Comment by kcrisman created at 2009-12-11 20:05:56

See also #2198, where however there is no discussion.  This issue is nearly two years old - a lifetime for Sage.


---

Comment by kcrisman created at 2009-12-11 20:13:53

Incidentally, we might as well upgrade now too - see http://www.r-project.org/, where 2.10.0 has been released, and in a few days 2.10.1 will be.


---

Attachment

Based on 4.3


---

Comment by kcrisman created at 2009-12-27 01:53:41

This patch will take care of the upgrade.  Whether adding various other packages will work is dealt with on other tickets.  Spkg will come as soon as sage.math is accessible again.


---

Comment by kcrisman created at 2009-12-27 03:26:50

Spkg is at [http://boxen.math.washington.edu/home/kcrisman/r-2.10.1.spkg](http://boxen.math.washington.edu/home/kcrisman/r-2.10.1.spkg)


---

Comment by kcrisman created at 2009-12-27 03:26:50

Changing status from new to needs_review.


---

Comment by pjeremy created at 2010-01-05 21:08:47

At least on FreeBSD, r-2.10.1 is more broken than r-2.9.2.  Neither version correctly detects libiconv.  The older version at least reports that it's missing a required library during configuration and aborts.  The new version just continues on and compilation fails when it can't #include iconv.h.

In addition, spkg-install still contains the following quoting errors:

```
CFLAGS="-I$SAGE_LOCAL/include -L$SAGE_LOCAL/lib/ "$CFLAGS; export CFLAGS
LDFLAGS="-L$SAGE_LOCAL/lib/ "$LDFLAGS; export LDFLAGS   
```

which should be written as:

```
CFLAGS="-I$SAGE_LOCAL/include -L$SAGE_LOCAL/lib/ $CFLAGS"; export CFLAGS
LDFLAGS="-L$SAGE_LOCAL/lib/ $LDFLAGS"; export LDFLAGS
```



I'm not giving this a negative review as overall, it is no worse than it was before.


---

Comment by kcrisman created at 2010-01-15 19:38:23

Okay, I've incorporated the (positively reviewed) changes at #7833 in this spkg, so it is ready to roll and be reviewed.


---

Comment by wjp created at 2010-01-19 00:39:47

spkg_check doesn't succeed for me when running this. In the current `r-2.9.2.spkg` the only failing tests were because of missing recommended packages, but in this spkg different tests seem to be failing. (See also #6279.)


---

Comment by kcrisman created at 2010-01-19 16:54:28

Hmm, I don't get this.  I also can't find the files involved - probably they were in the temp directory, maybe I had to set a different flag?  Here is my test log from the R installation, on Macintel 10.5.  Can you post your examples?  I have noticed that some other errors seem to be system-dependent.

```
Successfully installed r-2.10.1
Running the test suite.

Collecting examples for package ‘base’
  Extracting from parsed Rd's .......................................
Running examples in package ‘base’

Collecting examples for package ‘tools’
  Extracting from parsed Rd's ....
Running examples in package ‘tools’

Collecting examples for package ‘utils’
  Extracting from parsed Rd's ...........
Running examples in package ‘utils’

Collecting examples for package ‘grDevices’
  Extracting from parsed Rd's .....
Running examples in package ‘grDevices’

Collecting examples for package ‘graphics’
  Extracting from parsed Rd's ......
Running examples in package ‘graphics’

Collecting examples for package ‘stats’
  Extracting from parsed Rd's ..............................
Running examples in package ‘stats’

Collecting examples for package ‘datasets’
  Extracting from parsed Rd's ........
Running examples in package ‘datasets’

Collecting examples for package ‘methods’
  Extracting from parsed Rd's .......
Running examples in package ‘methods’

Collecting examples for package ‘grid’
  Extracting from parsed Rd's .......
Running examples in package ‘grid’

Collecting examples for package ‘splines’
  Extracting from parsed Rd's .
Running examples in package ‘splines’

Collecting examples for package ‘stats4’
  Extracting from parsed Rd's .
Running examples in package ‘stats4’

Collecting examples for package ‘tcltk’
  Extracting from parsed Rd's .
Running examples in package ‘tcltk’
running strict specific tests
running code in 'eval-etc.R' ... OK
comparing 'eval-etc.Rout' to './eval-etc.Rout.save' ... OK
running code in 'simple-true.R' ... OK
comparing 'simple-true.Rout' to './simple-true.Rout.save' ... OK
running code in 'arith-true.R' ... OK
comparing 'arith-true.Rout' to './arith-true.Rout.save' ... OK
running code in 'arith.R' ... OK
comparing 'arith.Rout' to './arith.Rout.save' ... OK
running code in 'lm-tests.R' ... OK
comparing 'lm-tests.Rout' to './lm-tests.Rout.save' ... OK
running code in 'ok-errors.R' ... OK
comparing 'ok-errors.Rout' to './ok-errors.Rout.save' ... OK
running code in 'method-dispatch.R' ... OK
comparing 'method-dispatch.Rout' to './method-dispatch.Rout.save' ... OK
running code in 'd-p-q-r-tests.R' ... OK
comparing 'd-p-q-r-tests.Rout' to './d-p-q-r-tests.Rout.save' ... OK
running sloppy specific tests
running code in 'complex.R' ... OK
comparing 'complex.Rout' to './complex.Rout.save' ... OK
running code in 'print-tests.R' ... OK
comparing 'print-tests.Rout' to './print-tests.Rout.save' ... OK
running code in 'lapack.R' ... OK
comparing 'lapack.Rout' to './lapack.Rout.save' ... OK
running code in 'datasets.R' ... OK
comparing 'datasets.Rout' to './datasets.Rout.save' ... OK
running regression tests ...
running code in 'reg-tests-1.R' ... OK
running code in 'reg-tests-2.R' ... OK
comparing 'reg-tests-2.Rout' to './reg-tests-2.Rout.save' ... OK
running code in 'reg-IO.R' ... OK
comparing 'reg-IO.Rout' to './reg-IO.Rout.save' ... OK
running code in 'reg-IO2.R' ... OK
comparing 'reg-IO2.Rout' to './reg-IO2.Rout.save' ... OK
running code in 'reg-plot.R' ... OK
comparing 'reg-plot.ps' to './reg-plot.ps.save' ... OK
running code in 'reg-S4.R' ... OK
comparing 'reg-S4.Rout' to './reg-S4.Rout.save' ... OK
running code in 'reg-tests-3.R' ... OK
comparing 'reg-tests-3.Rout' to './reg-tests-3.Rout.save' ... OK
running tests of plotting Latin-1
  expect failure or some differences if not in a Latin or UTF-8 locale
running code in 'reg-plot-latin1.R' ... OK
comparing 'reg-plot-latin1.ps' to './reg-plot-latin1.ps.save' ... OK
running tests of Internet and socket functions
  expect some differences
running code in 'internet.R' ... OK
comparing 'internet.Rout' to './internet.Rout.save' ...17c17
< [1] 2141
---
> [1] 2088
 OK
Now cleaning up tmp files.
Making Sage/Python scripts relocatable...
Making script relocatable
Finished installing r-2.10.1.spkg
```



---

Comment by kcrisman created at 2010-01-19 19:35:43

Perhaps this is somehow (weirdly) platform-dependent, or maybe there are add-ons R assumes one has... here is the report from boxen.math:

```
Collecting examples for package ‘base’
  Extracting from parsed Rd's .......................................
Running examples in package ‘base’
Error: testing 'base' failed
Execution halted
make[3]: *** [test-Examples-Base] Error 1
make[3]: Leaving directory `/home/.../sage-4.3-linux-sage.math.washington.edu-x86_64-Linux/spkg/build/r-2.10.1/src/tests/Examples'
make[2]: *** [test-Examples] Error 2
make[2]: Leaving directory `/home/.../sage-4.3-linux-sage.math.washington.edu-x86_64-Linux/spkg/build/r-2.10.1/src/tests'
make[1]: *** [test-all-basics] Error 1
make[1]: Leaving directory `/home/.../sage-4.3-linux-sage.math.washington.edu-x86_64-Linux/spkg/build/r-2.10.1/src/tests'
make: *** [check] Error 2
Error while running the R testsuite ... exiting
*************************************
Error testing package ** r-2.10.1 **
*************************************
sage: An error occurred while testing r-2.10.1
```



---

Comment by wjp created at 2010-01-19 20:12:18

It looks like the failing tests on my system were due to the `Matrix` package failing to build correctly because I hadn't set `SAGE_FORTRAN` properly before building sage. After doing that right, `spkg-check` ran without any trouble.


This is the snippet from the build log that shows the problem:


```
** building package indices ...
Loading required package: Matrix
Error in dyn.load(file, DLLpath = DLLpath, ...) : 
  unable to load shared library '/data/sage/sage-4.3.1.rc0/spkg/standard/r-2.10.1/src/library/Matrix/libs/Matrix.so':
  /data/sage/sage-4.3.1.rc0/local/lib/gcc-lib/i686-pc-linux-gnu/4.0.3/libgcc_s.so.1: version `GCC_4.2.0' not found (required by /usr/lib/libstdc++.so.6)
Error : require(Matrix, save = FALSE) is not TRUE
ERROR: installing package indices failed
* removing ‘/data/sage/sage-4.3.1.rc0/spkg/standard/r-2.10.1/src/library/Matrix’
make[2]: *** [Matrix.ts] Error 1
make[2]: Leaving directory `/data/sage/sage-4.3.1.rc0/spkg/standard/r-2.10.1/src/src/library/Recommended'
```



---

Comment by kcrisman created at 2010-01-19 20:22:48

This makes sense - the various R packages have heavy intertwined dependencies as well as dependencies on outside programs, and some of them won't build right on various machines (the Sage cluster, for instance, doesn't have OpenGL so it can't build a mostly computational package, depth, which requires rgl for displaying its computations). 

Do you know how I might go about checking what SAGE_FORTRAN is on a Linux machine?  I mean other than 

```
echo $SAGE_FORTRAN
```

which of course gives me nothing.  Maybe the spkg-install needs to be even better about finding the "right" Fortran?  Currently it is 

```
FC=sage_fortran; export FC
F77=sage_fortran; export F77
```

Also, make check just exits when something dies.  It would be nice if spkg-check actually returned a useful error message, but I have no idea how to do that, as I am not a shell script guru.


---

Comment by wjp created at 2010-01-19 20:26:54

`sage_fortran` should always be the right Fortran. The `SAGE_FORTRAN` variable is (only) used by the fortran spkg to setup the `sage_fortran` script correctly. Incidentally, #7485 improves this a lot and would have avoided the problem entirely for me.


---

Comment by kcrisman created at 2010-01-19 20:43:32

Hmm, that is very interesting.  I will try rebuilding on boxen.math with that fortran spkg.


---

Comment by wjp created at 2010-01-19 20:51:25

You'll have to manually remove the `local/lib/gcc-lib/` directory to get rid of the old one, by the way. It would be good if this caused your test failures as well.

For the `"Error: testing 'base' failed"` error you mentioned, you can get more info 
by looking at the `src/tests/Examples/base-Ex.Rout.fail` file it should have created.


---

Comment by kcrisman created at 2010-01-19 20:55:04

Replying to [comment:17 wjp]:
> You'll have to manually remove the `local/lib/gcc-lib/` directory to get rid of the old one, by the way. It would be good if this caused your test failures as well.
> 

Hmm, I didn't even have to do that.  As far as I can tell, this fixed the problem!

> For the `"Error: testing 'base' failed"` error you mentioned, you can get more info 
> by looking at the `src/tests/Examples/base-Ex.Rout.fail` file it should have created.

Yes, I already did that and asked for help on the R list, though hopefully this will do it.  We'll see.


---

Comment by kcrisman created at 2010-01-25 19:20:41

Reviewing this should close #6279, #2198, and I believe also #5246 and #4959.  It may also resolve #7833, and will enable a better resolution to #7521.  Try it out!


---

Comment by mvngu created at 2010-01-25 23:15:23

Prior to installation, I exported the check variable:

```
export SAGE_CHECK=yes
```

The updated R package was checked after successful compilation. After successfully installing [r-2.10.1.spkg](http://boxen.math.washington.edu/home/kcrisman/r-2.10.1.spkg), I installed the cluster package with `r.install_packages("cluster")`. It works:

```
sage: r_console()

R version 2.10.1 (2009-12-14)
Copyright (C) 2009 The R Foundation for Statistical Computing
ISBN 3-900051-07-0

R is free software and comes with ABSOLUTELY NO WARRANTY.
You are welcome to redistribute it under certain conditions.
Type 'license()' or 'licence()' for distribution details.

  Natural language support but running in an English locale

R is a collaborative project with many contributors.
Type 'contributors()' for more information and
'citation()' on how to cite R or R packages in publications.

Type 'demo()' for some demos, 'help()' for on-line help, or
'help.start()' for an HTML browser interface to help.
Type 'q()' to quit R.

> library("cluster")
> data(votes.repub)
> agn1 <- agnes(votes.repub, metric="manhattan", stand=TRUE)
> agn1
Call:	 agnes(x = votes.repub, metric = "manhattan", stand = TRUE) 
Agglomerative coefficient:  0.7977555 
Order of objects:
 [1] Alabama        Georgia        Arkansas       Louisiana      Mississippi   
 [6] South Carolina Alaska         Vermont        Arizona        Montana       
[11] Nevada         Colorado       Idaho          Wyoming        Utah          
[16] California     Oregon         Washington     Minnesota      Connecticut   
[21] New York       New Jersey     Illinois       Ohio           Indiana       
[26] Michigan       Pennsylvania   New Hampshire  Wisconsin      Delaware      
[31] Kentucky       Maryland       Missouri       New Mexico     West Virginia 
[36] Iowa           South Dakota   North Dakota   Kansas         Nebraska      
[41] Maine          Massachusetts  Rhode Island   Florida        North Carolina
[46] Tennessee      Virginia       Oklahoma       Hawaii         Texas         
Height (summary):
   Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
  8.382  12.800  18.530  23.120  28.410  87.460 

Available components:
[1] "order"     "height"    "ac"        "merge"     "diss"      "call"     
[7] "method"    "order.lab" "data"
```

The installation (of at least the "cluster" package) works both from within the R console (i.e. r_console()), and using the command r.install_packages(). Positive review from me.


---

Comment by mvngu created at 2010-01-25 23:15:23

Changing status from needs_review to positive_review.


---

Comment by mvngu created at 2010-01-25 23:18:46

Resolution: fixed


---

Comment by mvngu created at 2010-01-25 23:18:46

Merged in this order:

 1. [r-2.10.1.spkg](http://boxen.math.washington.edu/home/kcrisman/r-2.10.1.spkg) in the standard spkg repository
 1. [trac_6532-r-upgrade.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/6532/trac_6532-r-upgrade.patch)
