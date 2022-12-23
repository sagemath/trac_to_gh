# Issue 428: cannot build sage 2.8 on ppc G5, OS 10.4.10

Issue created by migration from https://trac.sagemath.org/ticket/428

Original creator: dmharvey

Original creation time: 2007-08-15 16:30:34

Assignee: was

Build fails somewhere in LAPACK.

Would be great if someone could confirm this on a similar system.

Full install.log is attached.

Here's the end of the log:


```
sage-spkg installed/lapack-20070723 2>&1 
lapack-20070723
Machine:
Darwin George.local 8.10.0 Darwin Kernel Version 8.10.0: Wed May 23 16:50:59 PDT 2007; root:xnu-792.21.3~1/RELEASE_PPC Power Macintosh powerpc
Deleting directories from past builds of previous/current versions of lapack-20070723
Extracting package /Users/david/sage-2.8/spkg/standard/lapack-20070723.spkg ...
-rw-r--r--   1 david  david  3442036 Jul 23 16:27 /Users/david/sage-2.8/spkg/standard/lapack-20070723.spkg
lapack-20070723/
lapack-20070723/.hg/
lapack-20070723/.hg/00changelog.i
lapack-20070723/.hg/dirstate
lapack-20070723/.hg/requires
lapack-20070723/.hg/store/
lapack-20070723/.hg/store/00changelog.i
lapack-20070723/.hg/store/00manifest.i

.......

lapack-20070723/src/TESTING/zsb.in
lapack-20070723/src/TESTING/zsg.in
lapack-20070723/src/TESTING/ztest.in
Finished extraction
****************************************************
Host system
uname -a:
Darwin George.local 8.10.0 Darwin Kernel Version 8.10.0: Wed May 23 16:50:59 PDT 2007; root:xnu-792.21.3~1/RELEASE_PPC Power Macintosh powerpc
****************************************************
****************************************************
GCC Version
gcc -v
Using built-in specs.
Target: powerpc-apple-darwin8
Configured with: /private/var/tmp/gcc/gcc-5247.obj~4/src/configure --disable-checking -enable-werror --prefix=/usr --mandir=/share/man --enable-languages=c,objc,c++,obj-c++ --program-transform-name=/^[cg][^.-]*$/s/$/-4.0/ --with-gxx-include-dir=/include/c++/4.0.0 --build=powerpc-apple-darwin8 --host=powerpc-apple-darwin8 --target=powerpc-apple-darwin8
Thread model: posix
gcc version 4.0.1 (Apple Computer, Inc. build 5247)
****************************************************
( cd INSTALL; make; ./testlsame; ./testslamch; \
  ./testdlamch; ./testsecond; ./testdsecnd; ./testversion )
sage_fortran -fPIC  -c lsame.f -o lsame.o
sage_fortran -fPIC  -c lsametst.f -o lsametst.o
sage_fortran  -o testlsame lsame.o lsametst.o
ld: table of contents for archive: /Users/david/sage-2.8/local/bin/../lib/gcc-lib/powerpc-apple-darwin6.8/4.0.3//libf95.a is out of date; rerun ranlib(1) (can't load from it)
ld: table of contents for archive: /Users/david/sage-2.8/local/bin/../lib/gcc-lib/powerpc-apple-darwin6.8/4.0.3//libgcc.a is out of date; rerun ranlib(1) (can't load from it)
ld: table of contents for archive: /Users/david/sage-2.8/local/bin/../lib/gcc-lib/powerpc-apple-darwin6.8/4.0.3//libgcc_eh.a is out of date; rerun ranlib(1) (can't load from it)
make[3]: *** [testlsame] Error 1
/bin/sh: line 1: ./testlsame: cannot execute binary file
/bin/sh: line 1: ./testslamch: cannot execute binary file
/bin/sh: line 1: ./testdlamch: cannot execute binary file
/bin/sh: line 1: ./testsecond: No such file or directory
/bin/sh: line 1: ./testdsecnd: cannot execute binary file
/bin/sh: line 1: ./testversion: cannot execute binary file
make[2]: *** [lapack_install] Error 126
Error compiling lapack.

real	0m0.419s
user	0m0.149s
sys	0m0.163s
sage: An error occured while installing lapack-20070723
Please email sage-devel http://groups.google.com/group/sage-devel
explaining the problem and send the relevant part of
of /Users/david/sage-2.8/install.log.  Describe your computer, operating system, etc.
If you want to try to fix the problem, yourself *don't* just cd to
/Users/david/sage-2.8/spkg/build/lapack-20070723 and type 'make'.
Instead (using bash) type "source local/bin/sage-env" from the directory
/Users/david/sage-2.8
in order to set all environment variables correctly, then cd to
/Users/david/sage-2.8/spkg/build/lapack-20070723
make[1]: *** [installed/lapack-20070723] Error 1

real	60m26.672s
user	26m56.349s
sys	17m18.560s

```



---

Attachment

full install log for failed build


---

Comment by mabshoff created at 2007-08-20 07:50:47

Check 

http://groups.google.com/group/sage-devel/browse_thread/thread/fa241096f4ecf138/6d994937074ae783

for a detailed discussion.

Cheers,

Michael


---

Comment by dmharvey created at 2007-08-28 22:27:52

Resolution: fixed


---

Comment by dmharvey created at 2007-08-28 22:27:52

Upgraded from XCode 2.2 to 2.4.1 and this resolves the problem.
