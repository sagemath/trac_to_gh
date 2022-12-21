# Issue 4868: optional polymake spkg quickly fails to build on sage.math

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-12-24 05:56:01

Assignee: mabshoff


```
sage: install_package('polymake-2.2.p4')
...
**********************************************************************
* Unable to download cddlib-094b.p1
* Please see http://www.sagemath.org//packages for a list of valid
* packages or check the package name.
**********************************************************************
sage: Failed to download package cddlib-094b.p1 from http://www.sagemath.org/
tar: /usr/local/sage/spkg/standard/cddlib-094b.p1.spkg: Cannot open: No such file or directory
```


This is even after installing cddlib. 




---

Comment by was created at 2008-12-24 07:03:17

I fixed a few problems in the spkg, so now it fails after only 30 minutes as follows:

```
                 from ../../../apps/polytope/src/cdd_interface.cc:19:
../../../lib/gmp_wrapper/include/Integer.h:783: warning: overflow in implicit constant conversion
../../../lib/gmp_wrapper/include/Integer.h:784: warning: overflow in implicit constant conversion
ld -r -o cdd_interface.o cdd_interface-tmp.o ../../external/cdd/libcddgmp.a
ld: ../../external/cdd/libcddgmp.a: No such file: No such file or directory
make[2]: *** [cdd_interface.o] Error 1
make[1]: *** [all] Error 2
make: *** [all] Error 2
echo "" | make
Error building polymake

real    0m29.741s
user    0m26.640s
sys     0m3.020s
sage: An error occurred while installing polymake-2.2.p5
Please email sage-devel http://groups.google.com/group/sage-devel
explaining the problem and send the relevant part of
of /usr/local/sage/install.log.  Describe your computer, operating system, etc.
If you want to try to fix the problem, yourself *don't* just cd to
/usr/local/sage/spkg/build/polymake-2.2.p5 and type 'make'.
Instead type "/usr/local/sage/sage -sh"
in order to set all environment variables correctly, then cd to
/usr/local/sage/spkg/build/polymake-2.2.p5
(When you are done debugging, you can type "exit" to leave the
subshell.)
```


The new spkg is here and should replace the original one. Also, I think this should be moved to experimental, in which case we could close this ticket:

http://sage.math.washington.edu/home/was/patches/polymake-2.2.p5.spkg


---

Comment by was created at 2008-12-24 07:09:49

I get the same with mpi4py:

```
sage: install_package('mpi4py-0.3.1')
Possible names of non-installed packages starting with 'mpi4py-0.3.1':
  mpi4py-0.3.1
  mpi4py-0.3.1
```



---

Comment by mabshoff created at 2008-12-24 11:44:25

Resolution: duplicate


---

Comment by mabshoff created at 2008-12-24 11:44:25

This is a dupe of #3640.

Cheers,

Michael
