# Issue 428: cannot build sage 2.8 on ppc G5, OS 10.4.10

archive/issues_000428.json:
```json
{
    "body": "Assignee: @williamstein\n\nBuild fails somewhere in LAPACK.\n\nWould be great if someone could confirm this on a similar system.\n\nFull install.log is attached.\n\nHere's the end of the log:\n\n\n```\nsage-spkg installed/lapack-20070723 2>&1 \nlapack-20070723\nMachine:\nDarwin George.local 8.10.0 Darwin Kernel Version 8.10.0: Wed May 23 16:50:59 PDT 2007; root:xnu-792.21.3~1/RELEASE_PPC Power Macintosh powerpc\nDeleting directories from past builds of previous/current versions of lapack-20070723\nExtracting package /Users/david/sage-2.8/spkg/standard/lapack-20070723.spkg ...\n-rw-r--r--   1 david  david  3442036 Jul 23 16:27 /Users/david/sage-2.8/spkg/standard/lapack-20070723.spkg\nlapack-20070723/\nlapack-20070723/.hg/\nlapack-20070723/.hg/00changelog.i\nlapack-20070723/.hg/dirstate\nlapack-20070723/.hg/requires\nlapack-20070723/.hg/store/\nlapack-20070723/.hg/store/00changelog.i\nlapack-20070723/.hg/store/00manifest.i\n\n.......\n\nlapack-20070723/src/TESTING/zsb.in\nlapack-20070723/src/TESTING/zsg.in\nlapack-20070723/src/TESTING/ztest.in\nFinished extraction\n****************************************************\nHost system\nuname -a:\nDarwin George.local 8.10.0 Darwin Kernel Version 8.10.0: Wed May 23 16:50:59 PDT 2007; root:xnu-792.21.3~1/RELEASE_PPC Power Macintosh powerpc\n****************************************************\n****************************************************\nGCC Version\ngcc -v\nUsing built-in specs.\nTarget: powerpc-apple-darwin8\nConfigured with: /private/var/tmp/gcc/gcc-5247.obj~4/src/configure --disable-checking -enable-werror --prefix=/usr --mandir=/share/man --enable-languages=c,objc,c++,obj-c++ --program-transform-name=/^[cg][^.-]*$/s/$/-4.0/ --with-gxx-include-dir=/include/c++/4.0.0 --build=powerpc-apple-darwin8 --host=powerpc-apple-darwin8 --target=powerpc-apple-darwin8\nThread model: posix\ngcc version 4.0.1 (Apple Computer, Inc. build 5247)\n****************************************************\n( cd INSTALL; make; ./testlsame; ./testslamch; \\\n  ./testdlamch; ./testsecond; ./testdsecnd; ./testversion )\nsage_fortran -fPIC  -c lsame.f -o lsame.o\nsage_fortran -fPIC  -c lsametst.f -o lsametst.o\nsage_fortran  -o testlsame lsame.o lsametst.o\nld: table of contents for archive: /Users/david/sage-2.8/local/bin/../lib/gcc-lib/powerpc-apple-darwin6.8/4.0.3//libf95.a is out of date; rerun ranlib(1) (can't load from it)\nld: table of contents for archive: /Users/david/sage-2.8/local/bin/../lib/gcc-lib/powerpc-apple-darwin6.8/4.0.3//libgcc.a is out of date; rerun ranlib(1) (can't load from it)\nld: table of contents for archive: /Users/david/sage-2.8/local/bin/../lib/gcc-lib/powerpc-apple-darwin6.8/4.0.3//libgcc_eh.a is out of date; rerun ranlib(1) (can't load from it)\nmake[3]: *** [testlsame] Error 1\n/bin/sh: line 1: ./testlsame: cannot execute binary file\n/bin/sh: line 1: ./testslamch: cannot execute binary file\n/bin/sh: line 1: ./testdlamch: cannot execute binary file\n/bin/sh: line 1: ./testsecond: No such file or directory\n/bin/sh: line 1: ./testdsecnd: cannot execute binary file\n/bin/sh: line 1: ./testversion: cannot execute binary file\nmake[2]: *** [lapack_install] Error 126\nError compiling lapack.\n\nreal\t0m0.419s\nuser\t0m0.149s\nsys\t0m0.163s\nsage: An error occured while installing lapack-20070723\nPlease email sage-devel http://groups.google.com/group/sage-devel\nexplaining the problem and send the relevant part of\nof /Users/david/sage-2.8/install.log.  Describe your computer, operating system, etc.\nIf you want to try to fix the problem, yourself *don't* just cd to\n/Users/david/sage-2.8/spkg/build/lapack-20070723 and type 'make'.\nInstead (using bash) type \"source local/bin/sage-env\" from the directory\n/Users/david/sage-2.8\nin order to set all environment variables correctly, then cd to\n/Users/david/sage-2.8/spkg/build/lapack-20070723\nmake[1]: *** [installed/lapack-20070723] Error 1\n\nreal\t60m26.672s\nuser\t26m56.349s\nsys\t17m18.560s\n\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/428\n\n",
    "created_at": "2007-08-15T16:30:34Z",
    "labels": [
        "packages: standard",
        "major",
        "bug"
    ],
    "title": "cannot build sage 2.8 on ppc G5, OS 10.4.10",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/428",
    "user": "dmharvey"
}
```
Assignee: @williamstein

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


Issue created by migration from https://trac.sagemath.org/ticket/428





---

archive/issue_comments_002148.json:
```json
{
    "body": "Attachment [install.log.gz](tarball://root/attachments/some-uuid/ticket428/install.log.gz) by dmharvey created at 2007-08-15 16:30:48\n\nfull install log for failed build",
    "created_at": "2007-08-15T16:30:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/428",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/428#issuecomment-2148",
    "user": "dmharvey"
}
```

Attachment [install.log.gz](tarball://root/attachments/some-uuid/ticket428/install.log.gz) by dmharvey created at 2007-08-15 16:30:48

full install log for failed build



---

archive/issue_comments_002149.json:
```json
{
    "body": "Check \n\nhttp://groups.google.com/group/sage-devel/browse_thread/thread/fa241096f4ecf138/6d994937074ae783\n\nfor a detailed discussion.\n\nCheers,\n\nMichael",
    "created_at": "2007-08-20T07:50:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/428",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/428#issuecomment-2149",
    "user": "mabshoff"
}
```

Check 

http://groups.google.com/group/sage-devel/browse_thread/thread/fa241096f4ecf138/6d994937074ae783

for a detailed discussion.

Cheers,

Michael



---

archive/issue_comments_002150.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-08-28T22:27:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/428",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/428#issuecomment-2150",
    "user": "dmharvey"
}
```

Resolution: fixed



---

archive/issue_comments_002151.json:
```json
{
    "body": "Upgraded from XCode 2.2 to 2.4.1 and this resolves the problem.",
    "created_at": "2007-08-28T22:27:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/428",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/428#issuecomment-2151",
    "user": "dmharvey"
}
```

Upgraded from XCode 2.2 to 2.4.1 and this resolves the problem.
