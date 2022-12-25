# Issue 9201: Add missing R modules and make `spkg-check` pass on Solaris

archive/issues_009201.json:
```json
{
    "body": "Assignee: drkirkby\n\nCC:  drkirkby ggrafendorfer @dimpase\n\nSome R modules aren't built/installed on t2.  This makes builds fail when `SAGE_CHECK` is set.  From [comment:ticket:8306:67 this comment] at #8306:\n\nRunning R's `make check` on t2 gives\n\n```\n Collecting examples for package `stats'\n   Extracting from parsed Rd's ..............................\n Running examples in package `stats'\n Error: testing 'stats' failed\n Execution halted\n make[5]: *** [test-Examples-Base] Error 1\n```\n\nHere's some detail from `src/tests/Examples/stats-Ex.Rout.fail`:\n\n```\n > contrasts(ffs) <- contr.sum(5, sparse=TRUE)[,1:2]; contrasts(ffs)\n Error in .Diag(levels, sparse = sparse) :\n   contr*(.., sparse=TRUE) needs package \"Matrix\" correctly installed\n Calls: contr.sum -> .Diag\n Execution halted\n```\n\n[This log](http://sage.math.washington.edu/home/mpatel/trac/8306/r-2.10.1.p2.log) also shows that R's Matrix package isn't built/installed successfully:\n\n```\n Loading required package: Matrix\n Error in dyn.load(file, DLLpath = DLLpath, ...) :\n   unable to load shared library '/scratch/mpatel/sage-4.4.4.alpha0-j64-par-chk/spkg/build/r-2.10.1.p2/src/library/Matrix/libs/Matrix.so':\n   ld.so.1: R: fatal: libgcc_s.so.1: open failed: No such file or directory\n Error : require(Matrix, save = FALSE) is not TRUE\n```\n\nMoreover, comparing the output of `ls SAGE_LOCAL/lib/R/library` on sage.math and t2 builds indicates that we're also missing the class, mgcv, nnet, rpart, spatial, and survival packages on t2.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9201\n\n",
    "created_at": "2010-06-10T07:48:05Z",
    "labels": [
        "component: porting: solaris",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Add missing R modules and make `spkg-check` pass on Solaris",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9201",
    "user": "https://github.com/qed777"
}
```
Assignee: drkirkby

CC:  drkirkby ggrafendorfer @dimpase

Some R modules aren't built/installed on t2.  This makes builds fail when `SAGE_CHECK` is set.  From [comment:ticket:8306:67 this comment] at #8306:

Running R's `make check` on t2 gives

```
 Collecting examples for package `stats'
   Extracting from parsed Rd's ..............................
 Running examples in package `stats'
 Error: testing 'stats' failed
 Execution halted
 make[5]: *** [test-Examples-Base] Error 1
```

Here's some detail from `src/tests/Examples/stats-Ex.Rout.fail`:

```
 > contrasts(ffs) <- contr.sum(5, sparse=TRUE)[,1:2]; contrasts(ffs)
 Error in .Diag(levels, sparse = sparse) :
   contr*(.., sparse=TRUE) needs package "Matrix" correctly installed
 Calls: contr.sum -> .Diag
 Execution halted
```

[This log](http://sage.math.washington.edu/home/mpatel/trac/8306/r-2.10.1.p2.log) also shows that R's Matrix package isn't built/installed successfully:

```
 Loading required package: Matrix
 Error in dyn.load(file, DLLpath = DLLpath, ...) :
   unable to load shared library '/scratch/mpatel/sage-4.4.4.alpha0-j64-par-chk/spkg/build/r-2.10.1.p2/src/library/Matrix/libs/Matrix.so':
   ld.so.1: R: fatal: libgcc_s.so.1: open failed: No such file or directory
 Error : require(Matrix, save = FALSE) is not TRUE
```

Moreover, comparing the output of `ls SAGE_LOCAL/lib/R/library` on sage.math and t2 builds indicates that we're also missing the class, mgcv, nnet, rpart, spatial, and survival packages on t2.


Issue created by migration from https://trac.sagemath.org/ticket/9201





---

archive/issue_comments_085945.json:
```json
{
    "body": "I think we also need a doctest which can detect if these parts of R are functional. It is a bit poor if Sage passes all the doc tests, while 6 packages have not built. \n\nI'm puzzled why libgcc_s.so.1 is not found. I would expect a failure to find that library to cause huge chunks of Sage to be non-functional. It is the gcc library, which is searched for with LD_LIBRARY_PATH:\n\n\n```\nkirkby@t2:[~] $ ls -l  /usr/local/gcc-4.4.1-sun-linker/lib/libgcc_s.so.1\n-rw-r--r--   1 nobody   nobody    259816 Aug  3  2009 /usr/local/gcc-4.4.1-sun-linker/lib/libgcc_s.so.1\nkirkby@t2:[~] $ echo $LD_LIBRARY_PATH\n/usr/local/gcc-4.4.1-sun-linker/lib:/usr/local/gcc-4.4.1-sun-linker/lib/sparcv9:/usr/local/lib\n```\n\n\nI've never written a doc test, and don't know R at all, but I think that each module we build should be tested. \n\nDave",
    "created_at": "2010-06-10T10:28:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9201",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9201#issuecomment-85945",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

I think we also need a doctest which can detect if these parts of R are functional. It is a bit poor if Sage passes all the doc tests, while 6 packages have not built. 

I'm puzzled why libgcc_s.so.1 is not found. I would expect a failure to find that library to cause huge chunks of Sage to be non-functional. It is the gcc library, which is searched for with LD_LIBRARY_PATH:


```
kirkby@t2:[~] $ ls -l  /usr/local/gcc-4.4.1-sun-linker/lib/libgcc_s.so.1
-rw-r--r--   1 nobody   nobody    259816 Aug  3  2009 /usr/local/gcc-4.4.1-sun-linker/lib/libgcc_s.so.1
kirkby@t2:[~] $ echo $LD_LIBRARY_PATH
/usr/local/gcc-4.4.1-sun-linker/lib:/usr/local/gcc-4.4.1-sun-linker/lib/sparcv9:/usr/local/lib
```


I've never written a doc test, and don't know R at all, but I think that each module we build should be tested. 

Dave



---

archive/issue_comments_085946.json:
```json
{
    "body": "Thanks for this important report.  I am not sure why these are not building, because all of these modules are 'Recommended' which we recently re-enabled (and do exist elsewhere, as you noted).  My guess is that these other packages did not build because they rely on Matrix and it didn't build.\n\nIt's not quite clear to me where these doctests would go.  The R interface docs are supposed to test that the interface works, not that R itself built properly.  The easiest way to test these is simply\n\n```\nr.library('package_name')\n```\n",
    "created_at": "2010-06-11T01:11:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9201",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9201#issuecomment-85946",
    "user": "https://github.com/kcrisman"
}
```

Thanks for this important report.  I am not sure why these are not building, because all of these modules are 'Recommended' which we recently re-enabled (and do exist elsewhere, as you noted).  My guess is that these other packages did not build because they rely on Matrix and it didn't build.

It's not quite clear to me where these doctests would go.  The R interface docs are supposed to test that the interface works, not that R itself built properly.  The easiest way to test these is simply

```
r.library('package_name')
```




---

archive/issue_comments_085947.json:
```json
{
    "body": "Replying to [comment:2 kcrisman]:\n> Thanks for this important report.  I am not sure why these are not building, because all of these modules are 'Recommended' which we recently re-enabled (and do exist elsewhere, as you noted).  My guess is that these other packages did not build because they rely on Matrix and it didn't build.\n> \n> It's not quite clear to me where these doctests would go.  The R interface docs are supposed to test that the interface works, not that R itself built properly.  The easiest way to test these is simply\n> {{{\n> r.library('package_name')\n> }}}\n\nI've no idea where the tests would go, or how to write them. But IMHO, if parts of R are non-functional (and it seems to be several parts), this should be detected. We test that some python modules have built, especially those that have known to be problematic, like _hashlib. \n\nI'm still puzzled why R can't find libgcc_s.so.1, as it is definately there. running\n\n```\n$ sage -sh\n$ cd local/lib\n$ ldd * | grep libgcc_s.so.1\n```\n\nI can see numerous parts of Sage link to libgcc_so.1. In fact, there are 127 of them! Here's the first one (certtool), if I run 'ldd' to see what it is linked against\n\n\n```\ncerttool:\n        libgnutls.so.26 =>       /export/home/drkirkby/32/sage-4.4.3/local/lib//libgnutls.so.26\n        libz.so =>       /export/home/drkirkby/32/sage-4.4.3/local/lib//libz.so\n        libgcrypt.so.11 =>       /export/home/drkirkby/32/sage-4.4.3/local/lib//libgcrypt.so.11\n        libgpg-error.so.0 =>     /export/home/drkirkby/32/sage-4.4.3/local/lib//libgpg-error.so.0\n        libreadline.so.6 =>      /export/home/drkirkby/32/sage-4.4.3/local/lib//libreadline.so.6\n        libnsl.so.1 =>   /lib/libnsl.so.1\n        libsocket.so.1 =>        /lib/libsocket.so.1\n        libc.so.1 =>     /lib/libc.so.1\n        libgcc_s.so.1 =>         /usr/local/gcc-4.4.3/lib/libgcc_s.so.1\n        libmp.so.2 =>    /lib/libmp.so.2\n        libmd5.so.1 =>   /lib/libmd5.so.1\n        libscf.so.1 =>   /lib/libscf.so.1\n        libdoor.so.1 =>  /lib/libdoor.so.1\n        libuutil.so.1 =>         /lib/libuutil.so.1\n        libm.so.2 =>     /lib/libm.so.2\n        /platform/SUNW,Sun-Blade-1000/lib/libc_psr.so.1\n        /platform/SUNW,Sun-Blade-1000/lib/libmd5_psr.so.1\n```\n\n\ncertool runs too.\n\n\n```\nsage subshell$ ./certtool\nCerttool help\nUsage: certtool [options]\n     -s, --generate-self-signed \n                              Generate a self-signed certificate.\n     -c, --generate-certificate \n                              Generate a signed certificate.\n     --generate-proxy         Generate a proxy certificate.\n```\n",
    "created_at": "2010-06-11T01:47:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9201",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9201#issuecomment-85947",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Replying to [comment:2 kcrisman]:
> Thanks for this important report.  I am not sure why these are not building, because all of these modules are 'Recommended' which we recently re-enabled (and do exist elsewhere, as you noted).  My guess is that these other packages did not build because they rely on Matrix and it didn't build.
> 
> It's not quite clear to me where these doctests would go.  The R interface docs are supposed to test that the interface works, not that R itself built properly.  The easiest way to test these is simply
> {{{
> r.library('package_name')
> }}}

I've no idea where the tests would go, or how to write them. But IMHO, if parts of R are non-functional (and it seems to be several parts), this should be detected. We test that some python modules have built, especially those that have known to be problematic, like _hashlib. 

I'm still puzzled why R can't find libgcc_s.so.1, as it is definately there. running

```
$ sage -sh
$ cd local/lib
$ ldd * | grep libgcc_s.so.1
```

I can see numerous parts of Sage link to libgcc_so.1. In fact, there are 127 of them! Here's the first one (certtool), if I run 'ldd' to see what it is linked against


```
certtool:
        libgnutls.so.26 =>       /export/home/drkirkby/32/sage-4.4.3/local/lib//libgnutls.so.26
        libz.so =>       /export/home/drkirkby/32/sage-4.4.3/local/lib//libz.so
        libgcrypt.so.11 =>       /export/home/drkirkby/32/sage-4.4.3/local/lib//libgcrypt.so.11
        libgpg-error.so.0 =>     /export/home/drkirkby/32/sage-4.4.3/local/lib//libgpg-error.so.0
        libreadline.so.6 =>      /export/home/drkirkby/32/sage-4.4.3/local/lib//libreadline.so.6
        libnsl.so.1 =>   /lib/libnsl.so.1
        libsocket.so.1 =>        /lib/libsocket.so.1
        libc.so.1 =>     /lib/libc.so.1
        libgcc_s.so.1 =>         /usr/local/gcc-4.4.3/lib/libgcc_s.so.1
        libmp.so.2 =>    /lib/libmp.so.2
        libmd5.so.1 =>   /lib/libmd5.so.1
        libscf.so.1 =>   /lib/libscf.so.1
        libdoor.so.1 =>  /lib/libdoor.so.1
        libuutil.so.1 =>         /lib/libuutil.so.1
        libm.so.2 =>     /lib/libm.so.2
        /platform/SUNW,Sun-Blade-1000/lib/libc_psr.so.1
        /platform/SUNW,Sun-Blade-1000/lib/libmd5_psr.so.1
```


certool runs too.


```
sage subshell$ ./certtool
Certtool help
Usage: certtool [options]
     -s, --generate-self-signed 
                              Generate a self-signed certificate.
     -c, --generate-certificate 
                              Generate a signed certificate.
     --generate-proxy         Generate a proxy certificate.
```




---

archive/issue_comments_085948.json:
```json
{
    "body": "I thought of someplace to put this that would make some sense, at least.  Under install_packages() in r.py, one could show how to get the matrix of all installed packages (which would be relevant), and as a doctest do \n\n```\nsage: a = r.installed_packages()\nsage: [pack in str(a) for pack in ['Matrix', 'package_1',...,'last_base_or_recommended_package']]\n[True, True, ... , True]\n```\n\nOr some more elegant boolean version of this.  You can literally cut and paste this into the current test for install_packages(), I think.\n\nI am sorry to say I can't help on the libgcc_s issue, though.",
    "created_at": "2010-06-12T03:27:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9201",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9201#issuecomment-85948",
    "user": "https://github.com/kcrisman"
}
```

I thought of someplace to put this that would make some sense, at least.  Under install_packages() in r.py, one could show how to get the matrix of all installed packages (which would be relevant), and as a doctest do 

```
sage: a = r.installed_packages()
sage: [pack in str(a) for pack in ['Matrix', 'package_1',...,'last_base_or_recommended_package']]
[True, True, ... , True]
```

Or some more elegant boolean version of this.  You can literally cut and paste this into the current test for install_packages(), I think.

I am sorry to say I can't help on the libgcc_s issue, though.



---

archive/issue_comments_085949.json:
```json
{
    "body": "It was suggested on the r-devel mailing list, that the problem might be the fact that the 'sparcv9' subdirectory (which contains 64-bit libraries), was in LD_LIBRARY_PATH. \n\n\n```\n> And if you look at the other R-help message posted by David Kirby you\n> will find a link to the trouble ticket report in Sage as\n> http://trac.sagemath.org/sage_trac/ticket/9201\n\n>From the link,...\n|  kirkby at t2:[~] $ echo $LD_LIBRARY_PATH\n| /usr/local/gcc-4.4.1-sun-linker/lib:/usr/local/gcc-4.4.1-sun-linker/lib/sparcv9:/usr/local/lib\n`/usr/local/gcc-4.4.1-sun-linker/lib/sparcv9' is 64bit, it is unnecessary.\nI think that this obstructs it.\n-- \nEI-JI Nakama  <nakama (a) ki.rim.or.jp>\n\"\\u4e2d\\u9593\\u6804\\u6cbb\"  <nakama (a) ki.rim.or.jp>\n```\n\n\nI doubted this would be the issue, as the library libgcc_s.so.1 was not found. If a 64-bit version was loaded instead, one would get a **WRONG ELF CLASS** message. Even if removing the sparcv9 directory solved the problem, I would consider this an R bug, as there is nothing wrong with having the 64-bit directories in LD_LIBRARY_PATH. \n\nAnyway, it does not solve the problem. On the same computer 't2.math.washington.edu', which is a Sun T5240 SPARC running Solaris 10 update 7 (, the same problem is observed if LD_LIBRARY_PATH is changed\n\n\n```\nCreating a new generic function for \"qr.resid\" in \"Matrix\"\nCreating a new generic function for \"qr.fitted\" in \"Matrix\"\n** help\n*** installing help indices\n** building package indices ...\nLoading required package: Matrix\nError in dyn.load(file, DLLpath = DLLpath, ...) : \n  unable to load shared library '/rootpool2/local/kirkby/sage-4.4.3/spkg/build/r-2.10.1.p1/src/library/Matrix/libs/Matrix.so':\n  ld.so.1: R: fatal: libgcc_s.so.1: open failed: No such file or directory\nError : require(Matrix, save = FALSE) is not TRUE\nERROR: installing package indices failed\n* removing \u2018/rootpool2/local/kirkby/sage-4.4.3/spkg/build/r-2.10.1.p1/src/library/Matrix\u2019\nmake[2]: *** [Matrix.ts] Error 1\n```\n\n\nwhere\n\n\n```\nkirkby@t2:[~/sage-4.4.3] $ echo $LD_LIBRARY_PATH\n/usr/local/gcc-4.4.1-sun-linker/lib:/usr/local/lib\nkirkby@t2:[~/sage-4.4.3] $ \n```\n\n\n## Testing on another computer\nThe same was observed on another much older computer, which was\n* Sun Blade 1000\n* 2 GB RAM\n* Solaris 10 03/05 (first release of Solaris 10)\n* gcc 4.4.3\n* Same version of Sage (4.4.3) with the same version of R (2.10.1)\n\n\n```\nCreating a new generic function for \"qr.qty\" in \"Matrix\"\nCreating a new generic function for \"qr.coef\" in \"Matrix\"\nCreating a new generic function for \"qr.resid\" in \"Matrix\"\nCreating a new generic function for \"qr.fitted\" in \"Matrix\"\n** help\n*** installing help indices\n** building package indices ...\nLoading required package: Matrix\nError in dyn.load(file, DLLpath = DLLpath, ...) : \n  unable to load shared library '/export/home/drkirkby/32/sage-4.4.3/spkg/build/r-2.10.1.p1/src/library/Matrix/libs/Matrix.so':\n  ld.so.1: /export/home/drkirkby/32/sage-4.4.3/spkg/build/r-2.10.1.p1/src/bin/exec/R: fatal: libgcc_s.so.1: open failed: No such file or directory\nError : require(Matrix, save = FALSE) is not TRUE\nERROR: installing package indices failed\n* removing '/export/home/drkirkby/32/sage-4.4.3/spkg/build/r-2.10.1.p1/src/library/Matrix'\nmake[2]: *** [Matrix.ts] Error 1\nmake[2]: Leaving directory `/export/home/drkirkby/32/sage-4.4.3/spkg/build/r-2.10.1.p1/src/src/library/Recommended'\nmake[1]: *** [recommended-packages] Error 2\nmake[1]: Leaving directory `/export/home/drkirkby/32/sage-4.4.3/spkg/build/r-2.10.1.p1/src/src/library/Recommended'\n```\n",
    "created_at": "2010-06-14T12:21:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9201",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9201#issuecomment-85949",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

It was suggested on the r-devel mailing list, that the problem might be the fact that the 'sparcv9' subdirectory (which contains 64-bit libraries), was in LD_LIBRARY_PATH. 


```
> And if you look at the other R-help message posted by David Kirby you
> will find a link to the trouble ticket report in Sage as
> http://trac.sagemath.org/sage_trac/ticket/9201

>From the link,...
|  kirkby at t2:[~] $ echo $LD_LIBRARY_PATH
| /usr/local/gcc-4.4.1-sun-linker/lib:/usr/local/gcc-4.4.1-sun-linker/lib/sparcv9:/usr/local/lib
`/usr/local/gcc-4.4.1-sun-linker/lib/sparcv9' is 64bit, it is unnecessary.
I think that this obstructs it.
-- 
EI-JI Nakama  <nakama (a) ki.rim.or.jp>
"\u4e2d\u9593\u6804\u6cbb"  <nakama (a) ki.rim.or.jp>
```


I doubted this would be the issue, as the library libgcc_s.so.1 was not found. If a 64-bit version was loaded instead, one would get a **WRONG ELF CLASS** message. Even if removing the sparcv9 directory solved the problem, I would consider this an R bug, as there is nothing wrong with having the 64-bit directories in LD_LIBRARY_PATH. 

Anyway, it does not solve the problem. On the same computer 't2.math.washington.edu', which is a Sun T5240 SPARC running Solaris 10 update 7 (, the same problem is observed if LD_LIBRARY_PATH is changed


```
Creating a new generic function for "qr.resid" in "Matrix"
Creating a new generic function for "qr.fitted" in "Matrix"
** help
*** installing help indices
** building package indices ...
Loading required package: Matrix
Error in dyn.load(file, DLLpath = DLLpath, ...) : 
  unable to load shared library '/rootpool2/local/kirkby/sage-4.4.3/spkg/build/r-2.10.1.p1/src/library/Matrix/libs/Matrix.so':
  ld.so.1: R: fatal: libgcc_s.so.1: open failed: No such file or directory
Error : require(Matrix, save = FALSE) is not TRUE
ERROR: installing package indices failed
* removing ‘/rootpool2/local/kirkby/sage-4.4.3/spkg/build/r-2.10.1.p1/src/library/Matrix’
make[2]: *** [Matrix.ts] Error 1
```


where


```
kirkby@t2:[~/sage-4.4.3] $ echo $LD_LIBRARY_PATH
/usr/local/gcc-4.4.1-sun-linker/lib:/usr/local/lib
kirkby@t2:[~/sage-4.4.3] $ 
```


## Testing on another computer
The same was observed on another much older computer, which was
* Sun Blade 1000
* 2 GB RAM
* Solaris 10 03/05 (first release of Solaris 10)
* gcc 4.4.3
* Same version of Sage (4.4.3) with the same version of R (2.10.1)


```
Creating a new generic function for "qr.qty" in "Matrix"
Creating a new generic function for "qr.coef" in "Matrix"
Creating a new generic function for "qr.resid" in "Matrix"
Creating a new generic function for "qr.fitted" in "Matrix"
** help
*** installing help indices
** building package indices ...
Loading required package: Matrix
Error in dyn.load(file, DLLpath = DLLpath, ...) : 
  unable to load shared library '/export/home/drkirkby/32/sage-4.4.3/spkg/build/r-2.10.1.p1/src/library/Matrix/libs/Matrix.so':
  ld.so.1: /export/home/drkirkby/32/sage-4.4.3/spkg/build/r-2.10.1.p1/src/bin/exec/R: fatal: libgcc_s.so.1: open failed: No such file or directory
Error : require(Matrix, save = FALSE) is not TRUE
ERROR: installing package indices failed
* removing '/export/home/drkirkby/32/sage-4.4.3/spkg/build/r-2.10.1.p1/src/library/Matrix'
make[2]: *** [Matrix.ts] Error 1
make[2]: Leaving directory `/export/home/drkirkby/32/sage-4.4.3/spkg/build/r-2.10.1.p1/src/src/library/Recommended'
make[1]: *** [recommended-packages] Error 2
make[1]: Leaving directory `/export/home/drkirkby/32/sage-4.4.3/spkg/build/r-2.10.1.p1/src/src/library/Recommended'
```




---

archive/issue_comments_085950.json:
```json
{
    "body": "It's also been suggested that crle is used to configure the runtime linking, but I don't really see that as a solution, as then it means one needs to have root access to build Sage. Couple that with the fact a mistake in using crle can result in an unbootable system, I'm not keen. \n\nDave",
    "created_at": "2010-06-14T15:36:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9201",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9201#issuecomment-85950",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

It's also been suggested that crle is used to configure the runtime linking, but I don't really see that as a solution, as then it means one needs to have root access to build Sage. Couple that with the fact a mistake in using crle can result in an unbootable system, I'm not keen. 

Dave



---

archive/issue_comments_085951.json:
```json
{
    "body": "I'm puzzled by the title of this ticket, as R has no spkg-check file in it currently. So how can it fail if SAGE_CHECK is set to yes? \n\nDave",
    "created_at": "2010-06-22T07:34:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9201",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9201#issuecomment-85951",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

I'm puzzled by the title of this ticket, as R has no spkg-check file in it currently. So how can it fail if SAGE_CHECK is set to yes? 

Dave



---

archive/issue_comments_085952.json:
```json
{
    "body": "Replying to [comment:7 drkirkby]:\n> I'm puzzled by the title of this ticket, as R has no spkg-check file in it currently. So how can it fail if SAGE_CHECK is set to yes? \n> \n> Dave \nIgnore that comment - I can see there is a test suite.",
    "created_at": "2010-06-22T07:52:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9201",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9201#issuecomment-85952",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Replying to [comment:7 drkirkby]:
> I'm puzzled by the title of this ticket, as R has no spkg-check file in it currently. So how can it fail if SAGE_CHECK is set to yes? 
> 
> Dave 
Ignore that comment - I can see there is a test suite.



---

archive/issue_comments_085953.json:
```json
{
    "body": "[this](http://groups.google.com/group/sage-release/browse_thread/thread/b2827cba9319bfed/750e7579d0499880?show_docid=750e7579d0499880&pli=1) thread also gives a report by ggrafendorfer that is probably related.",
    "created_at": "2010-08-25T12:48:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9201",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9201#issuecomment-85953",
    "user": "https://github.com/kcrisman"
}
```

[this](http://groups.google.com/group/sage-release/browse_thread/thread/b2827cba9319bfed/750e7579d0499880?show_docid=750e7579d0499880&pli=1) thread also gives a report by ggrafendorfer that is probably related.



---

archive/issue_comments_085954.json:
```json
{
    "body": "Georg, could you attach or give a link to the R build log\n\n`SAGE_ROOT/spkg/logs/r-2.10.1.p3.log`\n\nfor your AMD Phenom II X4 Fedora 13 machine?",
    "created_at": "2010-08-25T22:31:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9201",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9201#issuecomment-85954",
    "user": "https://github.com/qed777"
}
```

Georg, could you attach or give a link to the R build log

`SAGE_ROOT/spkg/logs/r-2.10.1.p3.log`

for your AMD Phenom II X4 Fedora 13 machine?



---

archive/issue_comments_085955.json:
```json
{
    "body": "Is this still an issue on Solaris?",
    "created_at": "2011-04-21T02:15:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9201",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9201#issuecomment-85955",
    "user": "https://github.com/kcrisman"
}
```

Is this still an issue on Solaris?



---

archive/issue_comments_085956.json:
```json
{
    "body": "Replying to [comment:10 mpatel]:\n> Georg, could you attach or give a link to the R build log\n> \n> `SAGE_ROOT/spkg/logs/r-2.10.1.p3.log`\n> \n> for your AMD Phenom II X4 Fedora 13 machine?\n\nThis ended up being [here](http://www.math.ethz.ch/~ggeorg/r-2.10.1.p3.log).  But as it turned out, the issue was #9847 - see the end of the thread referenced in comment 9.\n\nSo the only potential problem on this ticket is still the Solaris one.",
    "created_at": "2011-04-25T14:26:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9201",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9201#issuecomment-85956",
    "user": "https://github.com/kcrisman"
}
```

Replying to [comment:10 mpatel]:
> Georg, could you attach or give a link to the R build log
> 
> `SAGE_ROOT/spkg/logs/r-2.10.1.p3.log`
> 
> for your AMD Phenom II X4 Fedora 13 machine?

This ended up being [here](http://www.math.ethz.ch/~ggeorg/r-2.10.1.p3.log).  But as it turned out, the issue was #9847 - see the end of the thread referenced in comment 9.

So the only potential problem on this ticket is still the Solaris one.



---

archive/issue_comments_085957.json:
```json
{
    "body": "David, can you check whether this is still an issue on Solaris, and if so, for what precise architectures?",
    "created_at": "2011-08-19T13:53:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9201",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9201#issuecomment-85957",
    "user": "https://github.com/kcrisman"
}
```

David, can you check whether this is still an issue on Solaris, and if so, for what precise architectures?



---

archive/issue_comments_085958.json:
```json
{
    "body": "[Here is the install log](http://sage.math.washington.edu/home/palmieri/misc/r-2.10.1.p4.log) from building R on the skynet machine mark2 (Solaris on Sparc), with `SAGE_CHECK=yes`.  Self-tests failed.  Some information about mark2 is on the [appropriate Sage wiki page](http://wiki.sagemath.org/skynet).",
    "created_at": "2011-08-19T17:39:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9201",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9201#issuecomment-85958",
    "user": "https://github.com/jhpalmieri"
}
```

[Here is the install log](http://sage.math.washington.edu/home/palmieri/misc/r-2.10.1.p4.log) from building R on the skynet machine mark2 (Solaris on Sparc), with `SAGE_CHECK=yes`.  Self-tests failed.  Some information about mark2 is on the [appropriate Sage wiki page](http://wiki.sagemath.org/skynet).



---

archive/issue_comments_085959.json:
```json
{
    "body": "Thanks, John.  Looks like the problems are quite similar still.\n\nHere is one example of something bad, pretty much identical to in the ticket description.\n\n```\nLoading required package: Matrix\nError in dyn.load(file, DLLpath = DLLpath, ...) : \n  unable to load shared library '/home/palmieri/mark2/sage-4.7.1.rc1/spkg/r-2.10.1.p4/src/library/Matrix/libs/Matrix.so':\n  ld.so.1: R: fatal: libgcc_s.so.1: open failed: No such file or directory\nError : require(Matrix, save = FALSE) is not TRUE\nERROR: installing package indices failed\n* removing '/home/palmieri/mark2/sage-4.7.1.rc1/spkg/r-2.10.1.p4/src/library/Matrix'\n```\n\nJohn, I assume that libgcc_s.so.1 exists and everything is like David said in [comment:3 comment 3]?\n\nIf changing the various paths doesn't help, I don't know what would.  My guess is that something in the spkg's install is causing us to not find those for some reason, perhaps something to do with the fixes at #8274.  I was hoping I could help more :(",
    "created_at": "2011-08-19T18:05:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9201",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9201#issuecomment-85959",
    "user": "https://github.com/kcrisman"
}
```

Thanks, John.  Looks like the problems are quite similar still.

Here is one example of something bad, pretty much identical to in the ticket description.

```
Loading required package: Matrix
Error in dyn.load(file, DLLpath = DLLpath, ...) : 
  unable to load shared library '/home/palmieri/mark2/sage-4.7.1.rc1/spkg/r-2.10.1.p4/src/library/Matrix/libs/Matrix.so':
  ld.so.1: R: fatal: libgcc_s.so.1: open failed: No such file or directory
Error : require(Matrix, save = FALSE) is not TRUE
ERROR: installing package indices failed
* removing '/home/palmieri/mark2/sage-4.7.1.rc1/spkg/r-2.10.1.p4/src/library/Matrix'
```

John, I assume that libgcc_s.so.1 exists and everything is like David said in [comment:3 comment 3]?

If changing the various paths doesn't help, I don't know what would.  My guess is that something in the spkg's install is causing us to not find those for some reason, perhaps something to do with the fixes at #8274.  I was hoping I could help more :(



---

archive/issue_comments_085960.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2020-07-08T16:36:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9201",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9201#issuecomment-85960",
    "user": "https://github.com/mkoeppe"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_085961.json:
```json
{
    "body": "Outdated, should be closed",
    "created_at": "2020-07-08T16:36:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9201",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9201#issuecomment-85961",
    "user": "https://github.com/mkoeppe"
}
```

Outdated, should be closed



---

archive/issue_comments_085962.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2020-07-08T18:36:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9201",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9201#issuecomment-85962",
    "user": "https://github.com/dimpase"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_085963.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2020-08-17T18:40:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9201",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9201#issuecomment-85963",
    "user": "https://github.com/fchapoton"
}
```

Resolution: invalid
