# Issue 8010: f2py broken on some mac systems

Issue created by migration from Trac.

Original creator: flawrence

Original creation time: 2010-01-20 06:42:41

Assignee: tbd

CC:  georgsweber

Any use of f2py, e.g. following the examples at http://www.sagemath.org/doc/numerical_sage/f2py.html lead to a crash:


```
error: Command "sage_fortran -Wall -shared /var/folders/LQ/LQFRAKFTGCCurtDiHcxv1k++-5I/-Tmp-
/tmpisjCMl/var/folders/LQ/LQFRAKFTGCCurtDiHcxv1k++-5I/-Tmp-
/tmpisjCMl/src.macosx-10.6-i386-2.6/fortran_module_0module.o 
/var/folders/LQ/LQFRAKFTGCCurtDiHcxv1k++-5I/-Tmp-
/tmpisjCMl/var/folders/LQ/LQFRAKFTGCCurtDiHcxv1k++-5I/-Tmp-
/tmpisjCMl/src.macosx-10.6-i386-2.6/fortranobject.o 
/var/folders/LQ/LQFRAKFTGCCurtDiHcxv1k++-5I/-Tmp-
/tmpisjCMl/Users/felix/.sage/temp/<my domain name>/52076/tmp_0.o -L"Using built-in specs.
/Applications/sage-4.3.1.rc1/local/bin/../lib/gcc/i686-apple-darwin8/4.2.3/x86_64" 
-lgfortran -o ./fortran_module_0.so" failed with exit status 1

i686-apple-darwin8-gfortran-4.2: no input files
i686-apple-darwin8-gfortran-4.2: no input files
i686-apple-darwin8-gfortran-4.2: unrecognized option '-shared'
i686-apple-darwin8-gfortran-4.2: no input files
i686-apple-darwin8-gfortran-4.2: unrecognized option '-shared'
i686-apple-darwin8-gfortran-4.2: no input files
i686-apple-darwin8-gfortran-4.2: no input files
i686-apple-darwin8-gfortran-4.2: no input files
i686-apple-darwin8-gfortran-4.2: unrecognized option '-shared'
i686-apple-darwin8-gfortran-4.2: no input files
i686-apple-darwin8-gfortran-4.2: unrecognized option '-shared'
i686-apple-darwin8-gfortran-4.2: no input files
Using built-in specs.
Target: i686-apple-darwin8
Configured with: /Builds/unix/gcc/gcc-4.2/configure --prefix=/usr/local 
--mandir=/share/man --program-transform-name=/^[cg][^.-]*$/s/$/-4.2/ 
--build=i686-apple-darwin8 --host=i686-apple-darwin8 --target=i686-apple-
darwin8 --enable-languages=fortran
Thread model: posix
gcc version 4.2.3

<SNIP>
```


This is using 4.3.1rc1 on 10.6, 64-bit.

The problem is that local/lib/python2.6/site-packages/numpy/distutils/fcompiler/gnu.py adds a "-shared" flag when linking, even though OS X doesn't support it.


---

Attachment


---

Comment by flawrence created at 2010-01-20 06:45:46

Changing status from new to needs_review.


---

Comment by mvngu created at 2010-02-15 05:15:43

An updated spkg with Felix's patch is available at

http://sage.math.washington.edu/home/mvngu/spkg/standard/numpy/version2/numpy-1.3.0.p3.spkg

This ticket might clash with #7831.


---

Comment by drkirkby created at 2010-02-18 13:35:47

Has this been checked on Solaris? 

There's general information about building on Solaris at

http://wiki.sagemath.org/solaris

Information specifically for 't2' at 

http://wiki.sagemath.org/devel/Building-Sage-on-the-T5240-t2

Both the source (4.3.0.1 is the latest to build on Solaris) and a binary which will run on any SPARC can be found at http://www.sagemath.org/download-source.html 

Dave


---

Comment by flawrence created at 2010-02-19 05:12:10

I haven't checked this on Solaris, but it shouldn't affect behaviour on any platform other than OS X.  All this patch does is substitute the options "-undefined dynamic_lookup -bundle" for "-shared" under OS X, since on OS X the compiler doesn't support "-shared".

This platform-check and substitution is already being done elsewhere in the file (in the Sage_FCompiler class), but was not being done in Sage_FCompiler_1, so it's a pretty innocuous patch.

Cheers,
Felix


---

Comment by drkirkby created at 2010-02-19 09:33:48

Changing status from needs_review to needs_info.


---

Comment by drkirkby created at 2010-02-19 09:33:48

The title says this breaks on "on some mac systems", but the patch is applied on all Mac systems (well, all running OS X). Is that wise? 

It would be good if it could be tested on Solaris too, as often what are perceived as pretty innocuous patches do break on some systems.


---

Comment by flawrence created at 2010-02-19 11:21:32

Changing status from needs_info to needs_review.


---

Comment by flawrence created at 2010-02-19 11:21:32

Mac OS X (Darwin) compilers do not support the "-shared" option.  The class Sage_FCompiler_1 currently calls compilers on all platforms using the "-shared" option.  So whenever this class is used on Mac, it fails.  On my computer, this led to f2py failing.  This is a five line patch (plus documentation) that changes the compiler options on Mac to be in line with those already used in Sage_FCompiler, while leaving the compiler options on other platforms such as Solaris unchanged.  If you'd like to check it on Solaris, then go ahead, but the patch was intentionally written to avoid changing behaviour on platforms other than OS X.

This breaks "on some mac systems" - f2py is broken on my 64-bit sage, but seems to be working on 32-bit mac systems without this patch.  My guess is that 32-bit macs use Sage_FCompiler rather than Sage_FCompiler_1.  Anyone who is familiar with the numpy spkg, please confirm or correct me!


---

Comment by was created at 2010-06-02 05:45:18

This looks good for me, and works for people who've tested it.  Hence a positive review.


---

Comment by was created at 2010-06-02 05:45:18

Changing status from needs_review to positive_review.


---

Comment by rlm created at 2010-06-25 05:34:28

There is another ticket updating numpy as well: #7831. These two conflicting spkg's need to be resolved.


---

Comment by rlm created at 2010-06-28 17:05:57

Changing status from positive_review to needs_work.


---

Comment by flawrence created at 2010-06-28 23:33:50

How does this conflict with #7831?  What can I do to resolve the problem?


---

Comment by rlm created at 2010-06-28 23:39:22

These are both independent patches to the numpy package. take one, and incorporate the changes in the other, and post a new spkg. Then I will merge it and close both as merged, so the release note gives proper credit.


---

Comment by kcrisman created at 2010-09-09 12:59:30

Was this reported upstream?  Did it have to be?


---

Comment by flawrence created at 2010-09-09 13:16:10

>Was this reported upstream? Did it have to be?
I haven't reported this upstream.  The change was made to a class called Sage_FCompiler_1, which sounds like Sage-specific code.  The problem was already fixed in the very similar Sage_FCompiler.


---

Comment by kcrisman created at 2010-09-09 13:20:49

I see, so there were already custom patches made to numpy.


---

Comment by flawrence created at 2010-11-03 05:57:31

This is a duplicate of #7465


---

Comment by mvngu created at 2010-11-03 06:29:59

Closed as a duplicate of #7465.


---

Comment by mvngu created at 2010-11-03 06:30:13

Resolution: duplicate


---

Comment by kcrisman created at 2010-11-03 12:58:32

It is frustrating that this detailed ticket, which includes information about possible solutions, is closed, while the nearly totally uninformative #7465 is kept open.   Minh, could you at the very least take relevant information from #8010 and put it on the non-closed ticket? 

Also, it would be worth investigating the status of this issue (as well as #7831) in light of the fact that we have now upgraded to newer versions (see #9808).  I haven't compiled 4.6.1.alpha0 yet, but that should be tested.


---

Comment by mvngu created at 2010-11-04 11:56:07

Replying to [comment:19 kcrisman]:
> Minh, could you at the very least take relevant information from #8010 and put it on the non-closed ticket? 

Done.
