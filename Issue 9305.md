# Issue 9305: Add an spkg-check file for R (statistics package)

Issue created by migration from https://trac.sagemath.org/ticket/9305

Original creator: drkirkby

Original creation time: 2010-06-22 07:45:54

Assignee: tbd

CC:  kcrisman amhou

R is one of the many standard packages in Sage (see #9281 for a list), which do not have a spkg-check file. This means that if one builds Sage with the environment variable SAGE_CHECK set to "yes", no self-tests of the package will be run. This is silly, as R has a test suite.

After adding the file spkg-check


```
make check
```


will be run which is the documented way to test R. 

On a Solaris system I tested on, running the test suite uncovered errors. 


```
Making script relocatable
Finished installing rpy2-2.0.8.spkg

real    26m53.457s
user    22m28.215s
sys     3m2.030s
Successfully installed r-2.10.1.p2
Running the test suite.
make[1]: Entering directory `/export/home/drkirkby/sage-4.4.4.alpha1/spkg/build/r-2.10.1.p2/src/tests'
make[2]: Entering directory `/export/home/drkirkby/sage-4.4.4.alpha1/spkg/build/r-2.10.1.p2/src/tests'
make[3]: Entering directory `/export/home/drkirkby/sage-4.4.4.alpha1/spkg/build/r-2.10.1.p2/src/tests/Examples'

Collecting examples for package 'base'
  Extracting from parsed Rd's .......................................
Running examples in package 'base'

Collecting examples for package 'tools'
  Extracting from parsed Rd's ....
Running examples in package 'tools'

Collecting examples for package 'utils'
  Extracting from parsed Rd's ...........
Running examples in package 'utils'

Collecting examples for package 'grDevices'
  Extracting from parsed Rd's .....
Running examples in package 'grDevices'

Collecting examples for package 'graphics'
  Extracting from parsed Rd's ......
Running examples in package 'graphics'

Collecting examples for package 'stats'
  Extracting from parsed Rd's ..............................
Running examples in package 'stats'
Error: testing 'stats' failed
Execution halted
make[3]: *** [test-Examples-Base] Error 1
make[3]: Leaving directory `/export/home/drkirkby/sage-4.4.4.alpha1/spkg/build/r-2.10.1.p2/src/tests/Examples'
make[2]: *** [test-Examples] Error 2
make[2]: Leaving directory `/export/home/drkirkby/sage-4.4.4.alpha1/spkg/build/r-2.10.1.p2/src/tests'
make[1]: *** [test-all-basics] Error 1
make[1]: Leaving directory `/export/home/drkirkby/sage-4.4.4.alpha1/spkg/build/r-2.10.1.p2/src/tests'
make: *** [check] Error 2
One or more errors occured while testing R
Now cleaning up tmp files.
rm: Cannot remove any directory in the path of the current working directory
/export/home/drkirkby/sage-4.4.4.alpha1/spkg/build/r-2.10.1.p2
Making Sage/Python scripts relocatable...
Making script relocatable
Finished installing r-2.10.1.p2.spkg
```





---

Comment by drkirkby created at 2010-06-22 07:50:04

Resolution: invalid


---

Comment by drkirkby created at 2010-06-22 07:50:04

Oops, my mistake, there was a test package!
