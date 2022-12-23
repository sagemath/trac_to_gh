# Issue 9201: Add missing R modules and make `spkg-check` pass on Solaris

Issue created by migration from https://trac.sagemath.org/ticket/9201

Original creator: mpatel

Original creation time: 2010-06-10 07:48:05

Assignee: drkirkby

CC:  drkirkby ggrafendorfer dimpase

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



---

Comment by drkirkby created at 2010-06-10 10:28:19

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

Comment by kcrisman created at 2010-06-11 01:11:00

Thanks for this important report.  I am not sure why these are not building, because all of these modules are 'Recommended' which we recently re-enabled (and do exist elsewhere, as you noted).  My guess is that these other packages did not build because they rely on Matrix and it didn't build.

It's not quite clear to me where these doctests would go.  The R interface docs are supposed to test that the interface works, not that R itself built properly.  The easiest way to test these is simply

```
r.library('package_name')
```



---

Comment by drkirkby created at 2010-06-11 01:47:57

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

Comment by kcrisman created at 2010-06-12 03:27:36

I thought of someplace to put this that would make some sense, at least.  Under install_packages() in r.py, one could show how to get the matrix of all installed packages (which would be relevant), and as a doctest do 

```
sage: a = r.installed_packages()
sage: [pack in str(a) for pack in ['Matrix', 'package_1',...,'last_base_or_recommended_package']]
[True, True, ... , True]
```

Or some more elegant boolean version of this.  You can literally cut and paste this into the current test for install_packages(), I think.

I am sorry to say I can't help on the libgcc_s issue, though.


---

Comment by drkirkby created at 2010-06-14 12:21:43

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


I doubted this would be the issue, as the library libgcc_s.so.1 was not found. If a 64-bit version was loaded instead, one would get a *WRONG ELF CLASS* message. Even if removing the sparcv9 directory solved the problem, I would consider this an R bug, as there is nothing wrong with having the 64-bit directories in LD_LIBRARY_PATH. 

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

Comment by drkirkby created at 2010-06-14 15:36:17

It's also been suggested that crle is used to configure the runtime linking, but I don't really see that as a solution, as then it means one needs to have root access to build Sage. Couple that with the fact a mistake in using crle can result in an unbootable system, I'm not keen. 

Dave


---

Comment by drkirkby created at 2010-06-22 07:34:25

I'm puzzled by the title of this ticket, as R has no spkg-check file in it currently. So how can it fail if SAGE_CHECK is set to yes? 

Dave


---

Comment by drkirkby created at 2010-06-22 07:52:35

Replying to [comment:7 drkirkby]:
> I'm puzzled by the title of this ticket, as R has no spkg-check file in it currently. So how can it fail if SAGE_CHECK is set to yes? 
> 
> Dave 
Ignore that comment - I can see there is a test suite.


---

Comment by kcrisman created at 2010-08-25 12:48:45

[this](http://groups.google.com/group/sage-release/browse_thread/thread/b2827cba9319bfed/750e7579d0499880?show_docid=750e7579d0499880&pli=1) thread also gives a report by ggrafendorfer that is probably related.


---

Comment by mpatel created at 2010-08-25 22:31:31

Georg, could you attach or give a link to the R build log

`SAGE_ROOT/spkg/logs/r-2.10.1.p3.log`

for your AMD Phenom II X4 Fedora 13 machine?


---

Comment by kcrisman created at 2011-04-21 02:15:59

Is this still an issue on Solaris?


---

Comment by kcrisman created at 2011-04-25 14:26:13

Replying to [comment:10 mpatel]:
> Georg, could you attach or give a link to the R build log
> 
> `SAGE_ROOT/spkg/logs/r-2.10.1.p3.log`
> 
> for your AMD Phenom II X4 Fedora 13 machine?

This ended up being [here](http://www.math.ethz.ch/~ggeorg/r-2.10.1.p3.log).  But as it turned out, the issue was #9847 - see the end of the thread referenced in comment 9.

So the only potential problem on this ticket is still the Solaris one.


---

Comment by kcrisman created at 2011-08-19 13:53:25

David, can you check whether this is still an issue on Solaris, and if so, for what precise architectures?


---

Comment by jhpalmieri created at 2011-08-19 17:39:26

[Here is the install log](http://sage.math.washington.edu/home/palmieri/misc/r-2.10.1.p4.log) from building R on the skynet machine mark2 (Solaris on Sparc), with `SAGE_CHECK=yes`.  Self-tests failed.  Some information about mark2 is on the [appropriate Sage wiki page](http://wiki.sagemath.org/skynet).


---

Comment by kcrisman created at 2011-08-19 18:05:57

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

Comment by mkoeppe created at 2020-07-08 16:36:02

Changing status from new to needs_review.


---

Comment by mkoeppe created at 2020-07-08 16:36:02

Outdated, should be closed


---

Comment by dimpase created at 2020-07-08 18:36:55

Changing status from needs_review to positive_review.


---

Comment by chapoton created at 2020-08-17 18:40:11

Resolution: invalid
