# Issue 8527: libcocoa-0.9930 indicates its sucessfully installed when it has not.

Issue created by migration from Trac.

Original creator: drkirkby

Original creation time: 2010-03-13 20:00:31

Assignee: tbd

In trying to rid libcocoa-0.9930 of the GNUims that 
prevents this installing on on Solaris (see #8521), I found another problem with this package. It appears that the error codes are not properly checked, so even if there are build failures, the package indicates it has been successfully installed. See below:


```
Compiling RegisterServerOps.o
Compiling TmpFrobby.o
Compiling RegisterServerOpsFrobby.o
Compiling directory CoCoALib/src/AlgebraicCore/TmpFactorDir/
make[4]: Entering directory `/export/home/drkirkby/sage-4.3.4.alpha1/local/lib/cocoa-0.9930.p0/src/src/AlgebraicCore/TmpFactorDir'
Makefile:4: ../../../../configuration/autoconf.mk: No such file or directory
make[4]: *** No rule to make target `../../../../configuration/autoconf.mk'.  Stop.
make[4]: Leaving directory `/export/home/drkirkby/sage-4.3.4.alpha1/local/lib/cocoa-0.9930.p0/src/src/AlgebraicCore/TmpFactorDir'
***** Compilation of CoCoALib/src/AlgebraicCore/TmpFactorDir/ FAILED *****
make[3]: *** [../../lib/libcocoa.a] Error 1
make[3]: Leaving directory `/export/home/drkirkby/sage-4.3.4.alpha1/local/lib/cocoa-0.9930.p0/src/src/AlgebraicCore'
*****[[Compilation[failed[in[CoCoA[library[source[subdirectory[AlgebraicCore/[[*****
*****  Compilation failed in CoCoA library source subdirectory AlgebraicCore/  *****
*****[[Compilation[failed[in[CoCoA[library[source[subdirectory[AlgebraicCore/[[*****
make[2]: *** [library] Error 1
make[2]: Leaving directory `/export/home/drkirkby/sage-4.3.4.alpha1/local/lib/cocoa-0.9930.p0/src/src'
make[1]: *** [library] Error 2
make[1]: Leaving directory `/export/home/drkirkby/sage-4.3.4.alpha1/local/lib/cocoa-0.9930.p0/src'
make: *** [default] Error 2
Doing the build in the following directory:
/export/home/drkirkby/sage-4.3.4.alpha1/local/lib/cocoa-0.9930.p0
./configure  --with-libgmp=$SAGE_LOCAL/lib/libgmp.so
Now running Make
make
There are known test failures that should be listed above.
They are literally 'not yet implemented' errors from the
CoCOA library.   I.e., CoCOA releases purposely don't pass
their own test suite at present.
libcocoa.a built!

----------------------------------------------------------------------

To play with libcocoa, type 'sage -sh', then cd to the directory

   /export/home/drkirkby/sage-4.3.4.alpha1/local/lib/cocoa-0.9930.p0/src/examples

and try making and running some of the examples.
When you're done, it is completely safe to delete directory:

   /export/home/drkirkby/sage-4.3.4.alpha1/local/lib/cocoa-0.9930.p0

----------------------------------------------------------------------

real    4m38.333s
user    4m13.925s
sys     0m21.973s
Successfully installed libcocoa-0.9930.p0
```




---

Comment by slelievre created at 2019-04-13 13:35:07

Changing status from new to needs_review.


---

Comment by slelievre created at 2019-04-13 13:35:07

Propose to close this ticket as obsolete.
- The experimental libcocoa package seems to have been removed long ago, see #14962.
- There is a new cocoalib package, see #25707.
Please review.


---

Comment by mkoeppe created at 2019-06-06 18:30:20

Changing status from needs_review to positive_review.


---

Comment by chapoton created at 2019-06-06 18:35:28

Resolution: wontfix
