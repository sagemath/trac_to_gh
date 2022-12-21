# Issue 7090: R test suite fails when building with SAGE_CHECK

Issue created by migration from Trac.

Original creator: davidloeffler

Original creation time: 2009-10-01 15:58:21

Assignee: tbd

Keywords: R

Building 4.1.2.rc0 with SAGE_CHECK set to "yes", I got the following failure in the R test suite:


```
Successfully installed r-2.9.2
Running the test suite.
make[2]: Entering directory `/home/david/sage-4.1.2.rc0/spkg/build/r-2.9.2/src'
make[3]: Entering directory `/home/david/sage-4.1.2.rc0/spkg/build/r-2.9.2/src/test
s'
make[4]: Entering directory `/home/david/sage-4.1.2.rc0/spkg/build/r-2.9.2/src/test
s'
make[4]: warning: -jN forced in submake: disabling jobserver mode.
make[5]: Entering directory `/home/david/sage-4.1.2.rc0/spkg/build/r-2.9.2/src/test
s/Examples'
make[5]: warning: -jN forced in submake: disabling jobserver mode.

Collecting examples for package ‘base’
Running examples in package ‘base’

Collecting examples for package ‘tools’
Running examples in package ‘tools’

Collecting examples for package ‘utils’
Running examples in package ‘utils’
Error: testing 'utils' failed
Execution halted
make[5]: *** [test-Examples-Base] Error 1
make[5]: Leaving directory `/home/david/sage-4.1.2.rc0/spkg/build/r-2.9.2/src/tests
/Examples'
make[4]: *** [test-Examples] Error 2
make[4]: Leaving directory `/home/david/sage-4.1.2.rc0/spkg/build/r-2.9.2/src/tests
'
make[3]: *** [test-all-basics] Error 1
make[3]: Leaving directory `/home/david/sage-4.1.2.rc0/spkg/build/r-2.9.2/src/tests
'
make[2]: *** [check] Error 2
make[2]: Leaving directory `/home/david/sage-4.1.2.rc0/spkg/build/r-2.9.2/src'
Error while running the R testsuite ... exiting
*************************************
Error testing package ** r-2.9.2 **
*************************************
```



---

Comment by davidloeffler created at 2009-10-16 09:25:57

(Same happens in 4.1.2 final.)


---

Comment by mvngu created at 2010-02-03 06:59:25

Resolution: fixed


---

Comment by mvngu created at 2010-02-03 06:59:25

As of Sage 4.3.2.alpha1, ticket #6532 upgrades R to version 2.10.1. This fixes the issue regarding running the R test suite:

```
Successfully installed r-2.10.1
Running the test suite.
make[1]: Entering directory `/dev/shm/mvngu/sage-4.3.2.alpha1/spkg/build/r-2.10.1/src/tests'
make[2]: Entering directory `/dev/shm/mvngu/sage-4.3.2.alpha1/spkg/build/r-2.10.1/src/tests'
make[3]: Entering directory `/dev/shm/mvngu/sage-4.3.2.alpha1/spkg/build/r-2.10.1/src/tests/Examples'

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
make[3]: Leaving directory `/dev/shm/mvngu/sage-4.3.2.alpha1/spkg/build/r-2.10.1/src/tests/Examples'
make[2]: Leaving directory `/dev/shm/mvngu/sage-4.3.2.alpha1/spkg/build/r-2.10.1/src/tests'
make[2]: Entering directory `/dev/shm/mvngu/sage-4.3.2.alpha1/spkg/build/r-2.10.1/src/tests'
running strict specific tests
make[3]: Entering directory `/dev/shm/mvngu/sage-4.3.2.alpha1/spkg/build/r-2.10.1/src/tests'
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
make[3]: Leaving directory `/dev/shm/mvngu/sage-4.3.2.alpha1/spkg/build/r-2.10.1/src/tests'
running sloppy specific tests
make[3]: Entering directory `/dev/shm/mvngu/sage-4.3.2.alpha1/spkg/build/r-2.10.1/src/tests'
running code in 'complex.R' ... OK
comparing 'complex.Rout' to './complex.Rout.save' ... OK
running code in 'print-tests.R' ... OK
comparing 'print-tests.Rout' to './print-tests.Rout.save' ... OK
running code in 'lapack.R' ... OK
comparing 'lapack.Rout' to './lapack.Rout.save' ... OK
running code in 'datasets.R' ... OK
comparing 'datasets.Rout' to './datasets.Rout.save' ... OK
make[3]: Leaving directory `/dev/shm/mvngu/sage-4.3.2.alpha1/spkg/build/r-2.10.1/src/tests'
make[2]: Leaving directory `/dev/shm/mvngu/sage-4.3.2.alpha1/spkg/build/r-2.10.1/src/tests'
make[2]: Entering directory `/dev/shm/mvngu/sage-4.3.2.alpha1/spkg/build/r-2.10.1/src/tests'
running regression tests ...
make[3]: Entering directory `/dev/shm/mvngu/sage-4.3.2.alpha1/spkg/build/r-2.10.1/src/tests'
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
make[3]: Leaving directory `/dev/shm/mvngu/sage-4.3.2.alpha1/spkg/build/r-2.10.1/src/tests'
make[3]: Entering directory `/dev/shm/mvngu/sage-4.3.2.alpha1/spkg/build/r-2.10.1/src/tests'
running code in 'reg-tests-3.R' ... OK
comparing 'reg-tests-3.Rout' to './reg-tests-3.Rout.save' ... OK
running tests of plotting Latin-1
  expect failure or some differences if not in a Latin or UTF-8 locale
running code in 'reg-plot-latin1.R' ... OK
comparing 'reg-plot-latin1.ps' to './reg-plot-latin1.ps.save' ... OK
make[3]: Leaving directory `/dev/shm/mvngu/sage-4.3.2.alpha1/spkg/build/r-2.10.1/src/tests'
make[2]: Leaving directory `/dev/shm/mvngu/sage-4.3.2.alpha1/spkg/build/r-2.10.1/src/tests'
make[2]: Entering directory `/dev/shm/mvngu/sage-4.3.2.alpha1/spkg/build/r-2.10.1/src/tests'
running tests of Internet and socket functions
  expect some differences
make[3]: Entering directory `/dev/shm/mvngu/sage-4.3.2.alpha1/spkg/build/r-2.10.1/src/tests'
running code in 'internet.R' ... OK
comparing 'internet.Rout' to './internet.Rout.save' ...17c17
< [1] 2163
---
> [1] 2088
 OK
make[3]: Leaving directory `/dev/shm/mvngu/sage-4.3.2.alpha1/spkg/build/r-2.10.1/src/tests'
make[2]: Leaving directory `/dev/shm/mvngu/sage-4.3.2.alpha1/spkg/build/r-2.10.1/src/tests'
make[1]: Leaving directory `/dev/shm/mvngu/sage-4.3.2.alpha1/spkg/build/r-2.10.1/src/tests'
Now cleaning up tmp files.
Making Sage/Python scripts relocatable...
Making script relocatable
Finished installing r-2.10.1.spkg
```

Closing this ticket as fixed by #6532.
