# Issue 9308: Add an spkg-check file for GnuTLS

Issue created by migration from https://trac.sagemath.org/ticket/9308

Original creator: drkirkby

Original creation time: 2010-06-22 13:28:23

Assignee: tbd

CC:  leif jhpalmieri pjeremy

GnuTLS is one of the many standard packages in Sage (see #9281 for a list), which do not have a spkg-check file. This means that if one builds Sage with the environment variable SAGE_CHECK set to "yes", no self-tests of the package will be run. This is silly, as GnuTLS has a test suite.

After adding the required file, the test suite is run and at least on my OpenSolaris laptop, passes all tests. 

Dave


---

Comment by drkirkby created at 2010-06-22 14:01:01

Changing status from new to needs_review.


---

Comment by drkirkby created at 2010-06-22 14:01:01

After this is added, we can see the results - in this case all 15 tests pass, on a Sony laptop running OpenSolaris 06/2009. 


```
PASS: resume
===================
All 15 tests passed
===================
make[3]: Leaving directory `/export/home/drkirkby/sage-4.4.4.alpha1/spkg/build/gnutls-2.2.1.p6/src/tests'
make[2]: Leaving directory `/export/home/drkirkby/sage-4.4.4.alpha1/spkg/build/gnutls-2.2.1.p6/src/tests'
make[1]: Leaving directory `/export/home/drkirkby/sage-4.4.4.alpha1/spkg/build/gnutls-2.2.1.p6/src/tests'
Making check in po
make[1]: Entering directory `/export/home/drkirkby/sage-4.4.4.alpha1/spkg/build/gnutls-2.2.1.p6/src/po'
make[1]: Leaving directory `/export/home/drkirkby/sage-4.4.4.alpha1/spkg/build/gnutls-2.2.1.p6/src/po'
make[1]: Entering directory `/export/home/drkirkby/sage-4.4.4.alpha1/spkg/build/gnutls-2.2.1.p6/src'
make[1]: Leaving directory `/export/home/drkirkby/sage-4.4.4.alpha1/spkg/build/gnutls-2.2.1.p6/src'
Now cleaning up tmp files.
rm: Cannot remove any directory in the path of the current working directory
/export/home/drkirkby/sage-4.4.4.alpha1/spkg/build/gnutls-2.2.1.p6
Making Sage/Python scripts relocatable...
Making script relocatable
Finished installing gnutls-2.2.1.p6.spkg
```


The revised package may be found at 

http://boxen.math.washington.edu/home/kirkby/patches/gnutls-2.2.1.p6.spkg


---

Comment by drkirkby created at 2010-06-22 14:01:44

Mercurial patch to add an spkg-check to enable self-tests


---

Attachment

Again, cc'ing a few people who seem keen to improve the quality of Sage. 

Dave


---

Comment by jdemeyer created at 2012-10-05 09:11:12

Resolution: invalid


---

Comment by jdemeyer created at 2012-10-05 09:11:12

Invalid since GNUTLS is no longer part of Sage.
