# Issue 9733: Parallel build of Singular 3-1-1-4-package fails in rare case

Issue created by migration from Trac.

Original creator: AlexanderDreyer

Original creation time: 2010-08-12 12:18:45

Assignee: AlexGhitza

CC:  polybori drkirkby malb burcin leif

It was discovered in #8059 , that the parallel build of the Singular 3-1-1-4 packages still breaks in rare cases (many CPU cores, slow hard disk).

There are two patches which should fix this issue upstream:
http://www.singular.uni-kl.de:8002/trac/ticket/250, see

```
svn diff -r 13112:13110 http://www.singular.uni-kl.de/svn/
```



---

Comment by AlexanderDreyer created at 2010-08-12 12:20:01

svn diff -r 13112:13110 http://www.singular.uni-kl.de/svn/


---

Attachment


---

Comment by AlexanderDreyer created at 2010-08-12 12:20:58

Changing assignee from AlexGhitza to AlexanderDreyer.


---

Comment by AlexanderDreyer created at 2010-08-12 12:21:21

Changing component from algebra to build.


---

Comment by mpatel created at 2010-08-13 01:05:13

I repeated the tests in [comment:ticket:8059:112 comment 112] at #8059, this time under `/dev/shm` (a fast RAM disk, I think) on sage.math.  Thirteen of 50 runs failed, all apparently caused by the `gentable*` problem, which should be fixed by [this upstream comment](http://www.singular.uni-kl.de:8002/trac/ticket/250#comment:2).

Thanks for filing the fixes!


---

Comment by fbissey created at 2010-08-13 11:15:18

I will add a small patch to this ticket. While I worked on the Gentoo ebuild
I discovered that parallel make is disabled itself (jobserver not available using -j1) on libsingular and the test because make is called directly as "make" and not $(MAKE) or ${MAKE}.

So while it looks all fine and dandy you are actually not building libsingular in parallel, feel free to forward upstream as I don't have an account with them.


---

Comment by fbissey created at 2010-08-13 11:16:28

replace make by ${MAKE} in top Makefile.in


---

Attachment

But that's actually not a problem for the spkg, because the `spkg-install` does not call these target from the top-level `Makefile`.


---

Comment by fbissey created at 2010-08-13 11:44:46

Replying to [comment:6 AlexanderDreyer]:
> But that's actually not a problem for the spkg, because the `spkg-install` does not call these target from the top-level `Makefile`.

Then I missed something because I just checked spkg-install from the latest available spkg in #8059 and it does build libsingular by calling the top makefile:

```
build_libsingular()
{
    cd $SRC
    if [ $? -ne 0 ]; then
        echo "Unable to change to directory $SRC"
        exit 1
    fi

    make libsingular
```



---

Comment by AlexanderDreyer created at 2010-08-13 11:57:28

You're right, it's the case for factory and libfac, but not libsingular. But it will not change much, because most of the dependencies of libsingular are already built, when the spkg calls build_libsingular().


---

Comment by fbissey created at 2010-08-13 12:43:29

While it probably doesn't improve much the build time, it should be also thought as a QA patch. You should never ever call make directly from a makefile. That give rise to a pile of problems. The first one being that "make" may not be the original Make program invoked.
I didn't originally think about this but it is in fact a much bigger concern than the build time.


---

Comment by AlexanderDreyer created at 2010-08-13 12:51:43

Right, I'll report it upstream.


---

Comment by AlexanderDreyer created at 2010-08-15 14:26:38

Just to report back: for the gentable issue, there will be a better solution upstream. But the patch should be a reasonable workaround for sage.


---

Comment by leif created at 2010-09-09 01:35:05

Changing status from new to needs_review.


---

Comment by leif created at 2010-09-09 01:35:05

ping


---

Comment by fbissey created at 2010-09-09 01:48:29

Works for me on Gentoo linux for x86, amd64 and ppc.


---

Comment by mpatel created at 2010-09-09 02:13:10

Can someone make a new spkg and post a link to it?


---

Comment by AlexanderDreyer created at 2010-09-09 08:41:04

Please try out this one:
http://sage.math.washington.edu/home/dreyer/spkg/singular-3-1-1-4.p1.spkg


---

Comment by leif created at 2010-09-09 16:55:28

Replying to [comment:16 AlexanderDreyer]:
> Please try out this one:
> http://sage.math.washington.edu/home/dreyer/spkg/singular-3-1-1-4.p1.spkg


```sh
$ hg status
? spkg-install~
```


Installs ok with `MAKE="make -j16"` on an already loaded system (Sage 4.5.3, Ubuntu 10.04, Core2). I haven't had any problems previously with parallel builds though, and I don't have slow harddisks... ;-)

Unrelated:
 * Any reason to look for `bison` (despite `--without-bison` btw.), but then hardcoding `bison` instead of using ``@`BISON`@``?
 * `CFLAGS` and `CXXFLAGS` are _partly_ ignored. (Instead [only] `CPPFLAGS` are used for compiling C and C++ code.)


---

Comment by mpatel created at 2010-09-09 21:53:45

I think you'll also need to revert changeset 102:017aa4e4766e ("#8059: Restore building in serial, because of parallel build problems"), in order to test parallel builds.


---

Comment by AlexanderDreyer created at 2010-09-09 22:23:13

D'oh! Yeah, I had to revert changeset 102 and removed the tilde-file.
Please have a look at: http://sage.math.washington.edu/home/dreyer/spkg/singular-3-1-1-4.p1.spkg (same place as above)


---

Comment by leif created at 2010-09-09 22:53:42

Despite being significantly faster, same result. ;-)


---

Comment by mpatel created at 2010-09-10 01:22:53

* 50 of 50 serial installs of `singular-3-1-1-4.p1.spkg` succeed on sage.math with [ccache](http://ccache.samba.org/) _enabled_.  After the last run, I ran the long doctests.  They pass.

 * 50 of 50 parallel installs of `singular-3-1-1-4.p1.spkg` succeed on sage.math with [ccache](http://ccache.samba.org/) _enabled_.  However, 5 of the runs (not including the last) have the message `ranlib: 'libkernel_g.a': No such file`.  Is this a problem?  [Here's](http://sage.math.washington.edu/home/mpatel/trac/9733/singular-3-1-1-4-j20.log.6) a sample log file.  After the last run, I ran the long doctests.  They pass.  

 * 25 of 25 parallel installs of `singular-3-1-1-4.p1.spkg` succeed on sage.math with [ccache](http://ccache.samba.org/) _disabled_.  None gives the ranlib message above.  I'll run the tests after the other 25 runs are done and add a comment if there are problems.

 * Are the object files for `libcf.a`, `libsingcf_g.a`, `libfac.a`, and `libsingfac.a` built in parallel?

 * Is the message `install:  libsingcf_p.a does not exist` harmless?  It's printed three times per install.

I did all of the runs above under `/scratch`.


---

Comment by jhpalmieri created at 2010-09-10 03:40:15

> Is the message install: libsingcf_p.a does not exist harmless? It's printed three times per install.

I see this in logs from older versions of singular, too, for what that's worth.


---

Comment by fbissey created at 2010-09-10 04:11:49

Replying to [comment:22 jhpalmieri]:
> > Is the message install: libsingcf_p.a does not exist harmless? It's printed three times per install.
> 
> I see this in logs from older versions of singular, too, for what that's worth.
> 
And it is not used by sage itself or macaulay2 as far as I know. I think that's old cruft in the Makefile.


---

Comment by AlexanderDreyer created at 2010-09-10 07:57:15

THis patch adresses ranlib issue of comment 21


---

Attachment

>  * 50 of 50 parallel installs of `singular-3-1-1-4.p1.spkg` succeed on sage.math with [ccache](http://ccache.samba.org/) _enabled_.  However, 5 of the runs (not including the last) have the message `ranlib: 'libkernel_g.a': No such file`.  Is this a problem?  [Here's](http://sage.math.washington.edu/home/mpatel/trac/9733/singular-3-1-1-4-j20.log.6) a sample log file.  After the last run, I ran the long doctests.  They pass.  
I think I have fixed that issue, see the patche above and the new spkg at http://sage.math.washington.edu/home/dreyer/spkg/singular-3-1-1-4.p1.spkg (same place)

>  * Are the object files for `libcf.a`, `libsingcf_g.a`, `libfac.a`, and `libsingfac.a` built in parallel?
From the Makefiles there's no restriction, so the dependencies of each of which can be build in parallel. But there may be dependencies, that that there is no parallel build in fact.

>  * Is the message `install:  libsingcf_p.a does not exist` harmless?  It's printed three times per install.
> 
> I did all of the runs above under `/scratch`.
As fbissey said, this should not cause problems here.


---

Comment by mpatel created at 2010-09-11 06:08:06

Replying to [comment:24 AlexanderDreyer]:
> >  * 50 of 50 parallel installs of `singular-3-1-1-4.p1.spkg` succeed on sage.math with [ccache](http://ccache.samba.org/) _enabled_.  However, 5 of the runs (not including the last) have the message `ranlib: 'libkernel_g.a': No such file`.  Is this a problem?  [Here's](http://sage.math.washington.edu/home/mpatel/trac/9733/singular-3-1-1-4-j20.log.6) a sample log file.  After the last run, I ran the long doctests.  They pass.  
> I think I have fixed that issue, see the patche above and the new spkg at http://sage.math.washington.edu/home/dreyer/spkg/singular-3-1-1-4.p1.spkg (same place)

I repeated the three 50-run tests above.  The new package fixes the ranlib problem for me.

Could you fix this:

```sh
$ hg stat
? patches/kernel-Makefile.in.orig
? spkg-install~
```

?


---

Comment by AlexanderDreyer created at 2010-09-12 21:17:19

Ok, I fixed this also. Is this a positive review then?


---

Comment by mpatel created at 2010-09-12 21:39:18

Could you change the permissions so the package is accessible?

```sh
$ ls -l ~dreyer/spkg/singular-3-1-1-4.p1.spkg
7.9M -rw-r----- 1 dreyer dreyer 7.8M 2010-09-12 14:14 /home/dreyer/spkg/singular-3-1-1-4.p1.spkg
```



---

Comment by AlexanderDreyer created at 2010-09-13 07:23:57

Oh, sorry! It readable now.


---

Comment by mpatel created at 2010-09-13 07:39:32

Changing component from build to packages.


---

Comment by mpatel created at 2010-09-13 07:39:32

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-09-13 07:39:32

Thanks!

## Release manager

Merge just this package:

 http://sage.math.washington.edu/home/dreyer/spkg/singular-3-1-1-4.p1.spkg


---

Comment by mpatel created at 2010-09-13 07:41:39

Replying to [comment:17 leif]:
> Unrelated:
>  * Any reason to look for `bison` (despite `--without-bison` btw.), but then hardcoding `bison` instead of using ``@`BISON`@``?
>  * `CFLAGS` and `CXXFLAGS` are _partly_ ignored. (Instead [only] `CPPFLAGS` are used for compiling C and C++ code.)

Should we try to push these upstream?


---

Comment by AlexanderDreyer created at 2010-09-13 08:00:30

Sure, I can report this to Singular's trac.

The bison issue is - at least - confusion. For the flags, I need some additional information; The meaning (and names) of flags highly depend on the build system of a given software. So, each spkg-maintainer does need this knowledge for the system he/she maintains anyway. But `CFLAGS` and `CXXFLAGS` would be more standard-conforming, right?

BTW Singular compiles a lot of C-like code using the C++ compiler. This may result in the observation, that the `CFLAGS` were ignored.


---

Comment by leif created at 2010-09-13 09:47:10

Replying to [comment:30 mpatel]:
> Replying to [comment:17 leif]:
> > Unrelated:
> >  * Any reason to look for `bison` (despite `--without-bison` btw.), but then hardcoding `bison` instead of using ``@`BISON`@``?
> > 
> >  * `CFLAGS` and `CXXFLAGS` are _partly_ ignored. (Instead [only] `CPPFLAGS` are used for compiling C and C++ code.)
> 
> Should we try to push these upstream?

That's why I mentioned it here, considering Alexander upstream (or at least an upstream proxy)... ;-)


---

Comment by leif created at 2010-09-13 10:17:25

Replying to [comment:31 AlexanderDreyer]:
> Sure, I can report this to Singular's trac.

Thanks, that would be nice.

> [...] For the flags, I need some additional information; The meaning (and names) of flags highly depend on the build system of a given software.

The names shouldn't, they're standard. _How_ a package uses them might differ, i.e. _some_ flags might intentionally get overridden, but they should never be ignored. Also, some packages won't e.g. use `LDFLAGS` because they use `libtool` or use the C compiler driver for linking.
 
> So, each spkg-maintainer does need this knowledge for the system he/she maintains anyway.

I agree an spkg maintainer should know the upstream's build process... ;-)

> But `CFLAGS` and `CXXFLAGS` would be more standard-conforming, right?

? If this refers to (the use of) `CPPFLAGS`, these are the flags for the C preprocessor, `cpp`. The preprocessor is rarely used directly, but in the other case one should either pass them directly to the compiler driver as well, or e.g. prepend them to `CFLAGS` and `CXXFLAGS`.

> BTW Singular compiles a lot of C-like code using the C++ compiler. This may result in the observation, that the `CFLAGS` were ignored.

I haven't noticed that (but haven't inspected that either).

In that case, `CXXFLAGS` should have been used (when compiling C code with e.g. `g++`), but that's not the case. I can give more details on which files were compiled only using `CPPFLAGS` later. (To see which flags are actually used, simply `export CFLAGS=-DHONORS_CFLAGS` etc.)


---

Comment by AlexanderDreyer created at 2010-09-13 11:20:48

Now I understand: there are *compiled* targets in Singular, for instance the .og files, which do obey `CPPFLAGS`, but neither `CFLAGS` not `CXXFLAGS`.
I think, these files are intentionally compiled with other options than "ordinary" targets. For the .og files there is a `CXXFLAGSG` in the `Makefile.in`, but it is not managed by the `./configure` script.

Is there a best practice for such special targets?


---

Comment by leif created at 2010-09-13 13:08:13

For the purpose of Sage (I think) we should anyway compile with `-g` (and not build the "special" targets).

`CXXFLAGSG` should perhaps simply be `"$CXXFLAGS -g"` (or `-g` replaced by the appropriate option, depending on the compiler used), if `CXXFLAGS` do not already contain that. Otherwise one could drop the ".og" targets, or just build those; a matter of taste.

If nothing else than adding debug symbols differentiates the normal targets from their ".og" versions, one should simply build *once* _with_ debug symbols, copy the generated files, and create "non-.og" versions by stripping the made copies, then installing both (if requested).

I haven't yet looked at the sources (`configure`, `Makefile.in` etc.) though.


---

Comment by AlexanderDreyer created at 2010-09-13 13:23:19

> If nothing else than adding debug symbols differentiates the normal targets from their ".og" versions, one should simply build *once* _with_ debug symbols, copy the generated files, and create "non-.og" versions by stripping the made copies, then installing both (if requested).
Unfortunately it's not that easy. Singular's debug version is build via completely different targets. This might change somewhen in the (hopefully) not to far future. (This would obsolete our `CPPFLAGS` issue here also.)


---

Comment by AlexanderDreyer created at 2010-09-13 13:59:10

Upstream reports:

 * http://www.singular.uni-kl.de:8002/trac/ticket/269
 * http://www.singular.uni-kl.de:8002/trac/ticket/270


---

Comment by AlexanderDreyer created at 2010-09-13 21:12:17

First responde: the option `--without-bison` is not a valid option of Singular's `./configure` (See `./configure --help`). Bison is not used in the normal build process. (The Singular sources already include the processed files.)


---

Comment by mpatel created at 2010-09-16 00:48:42

Resolution: fixed


---

Comment by drkirkby created at 2010-09-17 07:27:34

Despite this being closed as fixed, this has failed for me on OpenSolaris 06/2009, with a missing header file, which would indicate the problem has not been solved. I suggest you might want to revisit this. 

I'm attaching a log. 

Dave


---

Attachment

Log of a failed build on a Sun Ultra 27 (4 cores, hyperthreaded), using MAKKE="make -j12"


---

Comment by mpatel created at 2010-09-17 08:30:07

Dave, thanks for reporting this problem.  Could someone please investigate it?  I'll "unmerge" this ticket from 4.6.alpha1, unless there's a positively reviewed fix within about a day or so.  I'm also waiting for a response to a build error at #4000.


---

Comment by mpatel created at 2010-09-17 08:30:07

Changing status from closed to needs_work.


---

Comment by fbissey created at 2010-09-17 11:27:58

The patch I just posted has unforseen issues, so don't use it.


---

Attachment

tentative patch for the latest parallel make issue (bis repetitas)


---

Comment by leif created at 2010-09-17 12:20:03

Dave, can you test François' latest patch? It cannot confirm it solves "your" problem (though it should).


---

Comment by fbissey created at 2010-09-17 12:22:46

Replying to [comment:44 leif]:
> Dave, can you test François' latest patch? It cannot confirm it solves "your" problem (though it should).

I was in the process of answering. It has to be applied after SingularSvn13111-13112.patch because it touches a neighboring area of code.


---

Comment by leif created at 2010-09-17 12:56:53

Works for me with `make -j` (unlimited). I've in addition changed the rule for `libsingcf_p.a`, but this might be superfluous.


---

Comment by leif created at 2010-09-17 13:10:52

(We do not build `libsingcf_p.a`.)

There are however race conditions (?) in deleting files and directories:

```
cd ftest && make -j distclean
make[1]: Entering directory `/home/leif/Sage/sage-4.6.alpha1/spkg/build/singular-3-1-1-4.p1-new/src/factory/ftest'
rm -f commonden degree deriv divides divrem extgcd factorize fbinops feval gcd gcd.ntl insert norm resultant revert sqrfree size totaldegree commonden.cc degree.cc deriv.cc divides.cc divrem.cc extgcd.cc factorize.cc fbinops.cc feval.cc gcd.cc gcd.ntl.cc insert.cc norm.cc resultant.cc revert.cc sqrfree.cc size.cc totaldegree.cc *.o
rm -f GNUmakefile
make[1]: Leaving directory `/home/leif/Sage/sage-4.6.alpha1/spkg/build/singular-3-1-1-4.p1-new/src/factory/ftest'
rmdir ftest
rmdir: failed to remove `ftest': Directory not empty
make: [ftestdistclean] Error 1 (ignored)
cd ftest && make -j clean
make[1]: Entering directory `/home/leif/Sage/sage-4.6.alpha1/spkg/build/singular-3-1-1-4.p1-new/src/factory/ftest'
make[1]: *** No rule to make target `clean'.  Stop.
make[1]: Leaving directory `/home/leif/Sage/sage-4.6.alpha1/spkg/build/singular-3-1-1-4.p1-new/src/factory/ftest'
make: [ftestclean] Error 2 (ignored)
```

Or perhaps just the list of files isn't complete.

Though ignored, should probably be fixed upstream, too.


---

Comment by AlexanderDreyer created at 2010-09-17 13:17:42

Another missing dependency


---

Attachment

I attached another patch, which should fix this issue.
The spkg is here:
http://sage.math.washington.edu/home/dreyer/spkg/singular-3-1-1-4.p2.spkg


---

Comment by leif created at 2010-09-17 13:40:13

Replying to [comment:48 AlexanderDreyer]:
> I attached another patch, which should fix this issue.
> The spkg is here:
> http://sage.math.washington.edu/home/dreyer/spkg/singular-3-1-1-4.p2.spkg

Works for me as well (`make -j`).


---

Comment by leif created at 2010-09-17 13:41:10

And all changes committed... :)


---

Comment by leif created at 2010-09-17 13:59:56

Changing status from needs_work to needs_review.


---

Comment by drkirkby created at 2010-09-17 15:20:31

I'm building this in a loop 100 times. I'll let you know if it fails at all

Dave


---

Comment by drkirkby created at 2010-09-17 17:11:22

This is looking good. Built this package 50 times so far without failure. 

Should have 100 done in about 1 hour and 20 minutes from now. 

Dave


---

Comment by drkirkby created at 2010-09-17 18:46:00

I've now built this 110 times, on the following hardware: 

 * Sun Ultra 27
 * 3.33 GHz Intel Xeon processor
 * 12 GB RAM
 * OpenSolaris 06/2009. 
 * Local hard drives using 128-bit ZFS file system. 

The method used was: 

 * Use 4 previous builds of Sage (different, but fairly recent versions)
 * Copied the `singular-3-1-1-4.p2.spkg` package to `$SAGE_ROOT/spkg/standard`
 * Created a script to run ` sage -f singular-3-1-1-4.p2.spkg`
 * set MAKE="make -j2" in one directory
 * set MAKE="make -j12" in two different directories. 
 * set MAKE="make -j30" in another directory. 

I did _'not_
 * Test the package with `SAGE_CHECK=yes`
 * Run any doctests. 

So at any one time, 4 builds of singular would take place, each in parallel, with either 2, 12 or 30 threads. The load average of the machine changed from around 9 to 11, but averaged about 10.  Each build took just over 6 minutes, but since 4 builds were taking place in parallel, this was an average build time of about 1.5 minutes/build. 

So there does not appear to be any parallel build issues. 

So positive review.


---

Comment by drkirkby created at 2010-09-17 18:46:00

Changing status from needs_review to positive_review.


---

Comment by leif created at 2010-09-17 19:02:18

Hope you don't spend the weekend reading the build logs... ;-)


---

Comment by mpatel created at 2010-09-17 21:32:29

Many thanks to everyone for reporting, patching, reviewing, and testing.  I apologize for not having caught this problem.


---

Comment by fbissey created at 2010-09-19 02:03:27

Would you believe it. I committed the latest patch to the sage-on-gentoo tree 3 hours ago and 1 hour ago about one of our users reported a new parallel make failure at -j2 on x86.... in libfac this time.

```
ar cr libsingcf_g.a canonicalform.og cf_algorithm.og cf_binom.og cf_char.og cf_chinese.og cf_cyclo.og cf_eval.og cf_factor.og cf_factory.og cf_gcd.og cf_gcd_charp.og cf_gcd_smallp.og cf_generator.og cf_globals.og cf_inline.og cf_irred.og cf_iter.og cf_iter_inline.og cf_linsys.og cf_map.og cf_map_ext.og cf_ops.og cf_primes.og cf_random.og cf_resultant.og cf_reval.og cf_switches.og cf_util.og debug.og DegreePattern.og ExtensionInfo.og fac_berlekamp.og fac_cantzass.og fac_distrib.og fac_ezgcd.og fac_iterfor.og fac_multihensel.og fac_multivar.og fac_sqrfree.og fac_univar.og fac_util.og facFqBivar.og facFqBivarUtil.og facFqFactorize.og facFqFactorizeUtil.og facFqSquarefree.og facHensel.og fieldGCD.og ffops.og ffreval.og gf_tabutil.og gfops.og imm.og initgmp.og int_cf.og int_int.og int_intdiv.og int_poly.og int_pp.og int_rat.og sm_sparsemod.og sm_util.og variable.og NTLconvert.og abs_fac.og bifac.og lgs.og singext.og
ranlib libsingcf_g.a
ar cr libsingcf.a canonicalform.o cf_algorithm.o cf_binom.o cf_char.o cf_chinese.o cf_cyclo.o cf_eval.o cf_factor.o cf_factory.o cf_gcd.o cf_gcd_charp.o cf_gcd_smallp.o cf_generator.o cf_globals.o cf_inline.o cf_irred.o cf_iter.o cf_iter_inline.o cf_linsys.o cf_map.o cf_map_ext.o cf_ops.o cf_primes.o cf_random.o cf_resultant.o cf_reval.o cf_switches.o cf_util.o debug.o DegreePattern.o ExtensionInfo.o fac_berlekamp.o fac_cantzass.o fac_distrib.o fac_ezgcd.o fac_iterfor.o fac_multihensel.o fac_multivar.o fac_sqrfree.o fac_univar.o fac_util.o facFqBivar.o facFqBivarUtil.o facFqFactorize.o facFqFactorizeUtil.o facFqSquarefree.o facHensel.o fieldGCD.o ffops.o ffreval.o gf_tabutil.o gfops.o imm.o initgmp.o int_cf.o int_int.o int_intdiv.o int_poly.o int_pp.o int_rat.o sm_sparsemod.o sm_util.o variable.o NTLconvert.o abs_fac.o bifac.o lgs.o singext.o
ranlib libsingcf.a
./bin/mkinstalldirs /var/tmp/portage/sci-mathematics/singular-3.1.1.4-r1/work/Singular-3-1-1/build/lib
./bin/mkinstalldirs /var/tmp/portage/sci-mathematics/singular-3.1.1.4-r1/work/Singular-3-1-1/build/include
./bin/mkinstalldirs /var/tmp/portage/sci-mathematics/singular-3.1.1.4-r1/work/Singular-3-1-1/build/include/templates
mkdir /var/tmp/portage/sci-mathematics/singular-3.1.1.4-r1/work/Singular-3-1-1/build/include/templates
./bin/install-sh -c -m 644 libsingcf.a /var/tmp/portage/sci-mathematics/singular-3.1.1.4-r1/work/Singular-3-1-1/build/lib/libsingcf.a
./bin/install-sh -c -m 644 libsingcf_g.a /var/tmp/portage/sci-mathematics/singular-3.1.1.4-r1/work/Singular-3-1-1/build/lib/libsingcf_g.a
./bin/install-sh -c -m 644 libsingcf_p.a /var/tmp/portage/sci-mathematics/singular-3.1.1.4-r1/work/Singular-3-1-1/build/lib/libsingcf_p.a
install:  libsingcf_p.a does not exist
make[2]: [installcf] Error 1 (ignored)
./bin/install-sh -c -m 644 factory.h /var/tmp/portage/sci-mathematics/singular-3.1.1.4-r1/work/Singular-3-1-1/build/include/factory.h
./bin/install-sh -c -m 644 cf_gmp.h /var/tmp/portage/sci-mathematics/singular-3.1.1.4-r1/work/Singular-3-1-1/build/include/cf_gmp.h
./bin/install-sh -c -m 644 factoryconf.h /var/tmp/portage/sci-mathematics/singular-3.1.1.4-r1/work/Singular-3-1-1/build/include/factoryconf.h
./bin/install-sh -c -m 644 ./ftmpl_inst.cc /var/tmp/portage/sci-mathematics/singular-3.1.1.4-r1/work/Singular-3-1-1/build/include/templates/ftmpl_inst.cc
for file in ftmpl_array.cc ftmpl_factor.cc ftmpl_functions.h ftmpl_list.cc ftmpl_matrix.cc ftmpl_array.h ftmpl_factor.h ftmpl_list.h ftmpl_matrix.h; do \
		  ./bin/install-sh -c -m 644 ./templates/$file /var/tmp/portage/sci-mathematics/singular-3.1.1.4-r1/work/Singular-3-1-1/build/include/templates/$file; \
		done
ranlib /var/tmp/portage/sci-mathematics/singular-3.1.1.4-r1/work/Singular-3-1-1/build/lib/libsingcf.a
make[2]: Leaving directory `/var/tmp/portage/sci-mathematics/singular-3.1.1.4-r1/work/Singular-3-1-1/factory'
make install in libfac
make[2]: Entering directory `/var/tmp/portage/sci-mathematics/singular-3.1.1.4-r1/work/Singular-3-1-1/libfac'
./mkinstalldirs OPTOBJ
i686-pc-linux-gnu-g++ -O2 -march=athlon-xp -msse2 -pipe -fomit-frame-pointer -fPIC -fno-implicit-templates -I./factor -I./charset -I. -I./factor -I/var/tmp/portage/sci-mathematics/singular-3.1.1.4-r1/work/Singular-3-1-1/build/include   -DHAVE_CONFIG_H  -c factor/SqrFree.cc -o OPTOBJ/SqrFree.o
mkdir OPTOBJ
Assembler messages:
Fatal error: can't create OPTOBJ/SqrFree.o: No such file or directory
i686-pc-linux-gnu-g++ -O2 -march=athlon-xp -msse2 -pipe -fomit-frame-pointer -fPIC -fno-implicit-templates -I./factor -I./charset -I. -I./factor -I/var/tmp/portage/sci-mathematics/singular-3.1.1.4-r1/work/Singular-3-1-1/build/include   -DHAVE_CONFIG_H  -c factor/Factor.cc -o OPTOBJ/Factor.o
make[2]: *** [OPTOBJ/SqrFree.o] Error 2
make[2]: *** Waiting for unfinished jobs....
make[2]: Leaving directory `/var/tmp/portage/sci-mathematics/singular-3.1.1.4-r1/work/Singular-3-1-1/libfac'
make[1]: *** [install] Error 1
```


I have a fix for him to try, I'll report back when I know the fix works for him.


---

Comment by fbissey created at 2010-09-19 03:11:37

fixing parallel make issue in libfac


---

Attachment

So he reported back and the patch worked for him.


---

Comment by mpatel created at 2010-09-19 05:56:00

Replying to [comment:58 fbissey]:
> So he reported back and the patch worked for him.

François, could you add your patch to #9946?

I'm going to release 4.6.alpha1 with #9946 as a known problem, since alpha1 _is_ an alpha and we need more real-world tests.
